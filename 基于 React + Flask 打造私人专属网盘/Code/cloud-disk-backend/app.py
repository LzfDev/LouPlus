import os
import hashlib
import random

_random = random.SystemRandom()

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
from itsdangerous import (TimedJSONWebSignatureSerializer as
        URLSafeSerializer, BadSignature, SignatureExpired)
from functools import wraps
from model import Folder, File
import peewee
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)
app.config.from_object('config')

# 允许跨域
CORS(app)


def verify_auth_token(token):
    s = URLSafeSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    return 'key' in data and data['key'] == app.config['SECRET_KEY']


def test_authorization():
    cookies = request.cookies
    headers = request.headers
    args = request.args
    token = None
    if 'token' in cookies:
        token = cookies['token']
    elif 'Authorization' in headers:
        token = headers['Authorization']
    elif 'token' in args:
        token = args['token']
    else:
        return False

    return verify_auth_token(token)


def authorization_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not test_authorization():
            return jsonify(message='unauthorized'), 401
        return f(*args, **kwargs)
    return wrapper


def generate_filename(folder, filename):
    return hashlib.md5(
            (folder + '_' + filename).encode('utf-8')).hexdigest()


def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))


# 用于生成短地址
def generate_url():
    return base36_encode(get_random_long_int())


def generate_password():
    return base36_encode(get_random_short_int())


def get_random_long_int():
    return _random.randint(1000000000, 9999999999)


def get_random_short_int():
    return _random.randint(100000, 999999)


@app.route('/auth', methods=['GET'])
@authorization_required
def auth():
    return jsonify(message='OK')


@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    if req['email'] == app.config['EMAIL'] and req['password'] == app.config['PASSWORD']:
        s = URLSafeSerializer(app.config['SECRET_KEY'], expires_in=7 * 24 * 3600)
        return jsonify(message='OK',
                token=s.dumps({'key': app.config['SECRET_KEY']}).decode('utf-8'))
    else:
        return jsonify(message='unauthorized'), 401


@app.route('/folders', methods=['GET', 'POST'])
# TODO: @authorization_required
def folders():
    if request.method == 'POST':
        req = request.get_json()
        try:
            f = Folder.create(name=req['name'])
            f.save()
            return jsonify(message='OK'), 201
        except peewee.IntegrityError as e:
            return jsonify(message='error'), 409

    query = Folder.select()
    if(query.exists()):
        return jsonify(message='OK', data=[model_to_dict(folder) for folder in query])
    else:
        return jsonify(message='OK', data=[])


@app.route('/folders/<folder_name>', methods=['GET', 'POST', 'DELETE'])
# TODO @authorization_rquired
def folder(folder_name):
    try:
        folder = Folder.get(Folder.name == folder_name)
    except peewee.DoesNotExist:
        return jsonify(message='error'), 404

    if request.method == 'POST':
        f = request.files['file']
        if f:
            # 生成文件名的hash
            actual_filename = generate_filename(folder_name, f.filename)
            target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)
            if os.path.exists(target_file):
                return jsonify(message='error'), 409
            try:
                # 保存文件，并写入数据库，生成短地址，默认关闭分享
                f.save(target_file)
                f2 = File.create(folder=folder,
                        filename=f.filename,
                        public_share_url=generate_url(),
                        private_share_url=generate_url(),
                        private_share_password=generate_password(),
                        open_public_share=False,
                        open_private_share=False)
                f2.save()
            except Exception as e:
                app.logger.exception(e)
                return jsonify(message='error'), 500
            return jsonify(message='OK'), 201

    if request.method == 'GET':
        return jsonify(message='OK', data=model_to_dict(folder, backrefs=True))

    if request.method == 'DELETE':
        try:
            folder.delete_instance()
        except peewee.IntegrityError:
            return jsonify(message='error'), 409
    return jsonify(message='OK')


# 通常PATCH 用来更新modeld的一部分，PUT用来更新整个model
@app.route('/folders/<folder_name>/<filename>', methods=['GET', 'PATCH', 'DELETE'])
# TODO:@authorization_required
def files(folder_name, filename):
    # 取文件路径
    actual_filename = generate_filename(folder_name, filename)
    target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']), actual_filename)
    try:
        f = File.get(filename=filename)
    except peewee.DoesNotExist:
        return jsonify(message='error'), 404

    if request.method == 'GET':
        args = request.args
        # query = info, 返回文件信息
        if 'query' in args and args['query'] == 'info':
            return jsonify(message='OK', data=model_to_dict(f))

        # 直接GET，则发送文件
        if os.path.exists(target_file):
            return send_file(target_file)
        else:
            return jsonify(message='error'), 404

    if request.method == 'PATCH':
        share_type = request.args.get('shareType')
        if share_type == 'private':
            f.open_private_share = True
            f.open_public_share = False

        if share_type == 'public':
            f.open_public_share = True
            f.open_private_share = False

        elif share_type == 'none':
            f.open_public_share = False
            f.open_private_share = False

        f.save()
        return jsonify(message='OK')

    if request.method == 'DELETE':
        if os.path.exists(target_file):
            try:
                # 删除文件及文件在数据库中的记录
                f.delete_instance()
                os.remove(target_file)
                return jsonify(message='OK')
            except Exception as e:
                app.logger.exception(e)
                return jsonify(message='error'), 500
        else:
            return jsonify(message='error'), 404


@app.route('/share/<path>', methods=['GET'])
def share(path):
    is_public = False
    is_private = False

    try:
        # 查找对应的文件
        f = File.get(File.public_share_url == path)
        is_public = True
    except peewee.DoesNotExist:
        # 处理私密分享
        try:
            f = File.get(File.private_share_url == path)
            is_private = True
        except peewee.DoesNotExist:
            return jsonify(message='error'), 404

    actual_filename = generate_filename(f.folder.name, f.filename)
    target_file = os.path.join(os.path.expanduser(app.config['UPLOAD_FOLDER']),
                               actual_filename
                               )

    if not ((is_public and f.open_public_share) or 
            (is_private and f.open_private_share)):
        return jsonify(message='error'), 404

    s = URLSafeSerializer(app.config['SECRET_KEY'], 
                          expires_in=24 * 3600)
                          
    args = request.args
    if args.get('download') == 'true':
        # 如果是下载，验证Cookie
        token = None
        cookies = request.cookies
        if 'token' in cookies:
            token = cookies['token']
            try:
                data = s.loads(token)
                if data['path'] == path:
                    if os.path.exists(target_file):
                        return send_file(target_file)
                    else:
                        return jsonify(message='error'), 404
                else:
                    return jsonify(message='unauthorized'), 401
            except:
                return jsonify(message='unauthorized'), 401

    # 如果是获取信息，设置上Cookie
    # 这里设置的Token和登录的不同,不能用于验证登录有关
    token = s.dumps({'path': path}).decode('utf-8')
    payload = {
        'filename': f.filename,
        'folder': f.folder.name,
        'open_public_share': f.open_public_share,
        'open_private_share': f.open_private_share,
        'token': token,
    }
    
    # 校验密码，密码不对不返回token
    if is_private:
        if 'password' not in args or args['password'] != f.private_share_password:
            payload['token'] = ''

    return jsonify(message='OK', data=payload)


@app.route('/s/<path>', methods=['GET'])
def share_static(path):
    return app.send_static_file('index.html')
    

@app.route('/', methods=['GET'])
def index_static():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)
