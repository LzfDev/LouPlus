# Flask预备知识

## 一、实验说明

本节实验为实验楼训练营课程《仿 StackOverflow 开发在线问答系统》第1节，希望与大家一起完成下面两项任务：

1. Flask 开发环境搭建
2. 完成 Flask 可运行的代码框

### 1. 前期准备

#### 1.1 安装 `virtualenv` 软件包

`virtualenv` 是一个用于创建隔离 Python 环境的工具。所谓隔离是指 `virtualenv` 可以为每个 Pyhon 程序创建虚拟环境，并保证该程序只能访问该虚拟环境下的包，解决了“项目 X 依赖于版本 1.x ，而项目 Y 需要版本 4.x ”的两难问题，从而保持全局 python 环境的干净整洁。另外使用 `virtualenv` 还有个好处，那就是在安装 python 扩展包的时候不需要管理员权限。

在 Ubuntu 中通过 `apt-get` 命令安装 `virtualenv`，过程如下：

```
sudo apt-get update
sudo pip install virtualenv
```

> 补充：想了解更多关于 virtualenv 的信息可以参考 [Python 指南——虚拟环境](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html)。

#### 1.2 提交代码

注意，为了保持一个良好的代码习惯，在关闭实验之前记得把自己在实验楼环境下编写的代码上传到实验楼的 git 下，以便下次继续修改代码（更多问题见《[我的代码库](https://www.shiyanlou.com/questions/360)》）。

#### 1.3 添加 `.gitignore`

由于`venv`目录包含所有依赖的软件包，接近29M，所以我们在提交代码时无需提交该目录，创建`.gitignore`文件可以达到这个目的，这个文件中可以使用通配符，文件名及目录名来告诉`git`忽略一些文件或文件夹。

```
cd /home/shiyanlou/Code/shiyanlou_cs355  # 将此路径改成你自己的路径
touch .gitignore
echo "venv" >> .gitignore
```

## 二、欢迎来到 Flask 的世界

Flask 是一个使用 Python 开发的微型开发框架，基于 Werkzeug WSGI 工具箱和 Jinja2 模板引擎。 Flask 也被称为 “microframework” ，因为它具有极简的核心，然而却可以通过扩展的方式增加其他功能。 Flask 默认不支持数据库连接，不支持用户登陆认证等功能。但是，我们可以通过各种扩展获得对这些功能的支持，比如：数据库 ORM、表单验证、文件上传、开放式身份验证技术。这使得 Flask 成为具有高度扩展性和灵活性的 Python Web 框架。

### 1. 为什么要学习 Flask ？

1. 正如上面所说， Flask 是一个 web “微”框架，我们使用 Flask 可以快速的搭建我们的网站，在互联网时代，一个好的 idea 不能尽快的展现在人们的面前，确实是令开发者很苦恼的事情。
2. 容易学习。学完了 Python 基础之后想要接触 web 开发。 Flask 非常易于使用，同时，稍后你能看到示例代码所展示的那样，是一个十分简单的框架。你的大脑很自然地就适应它了，使用 Flask ，可以更快地开发。
3. Flask 有非常活跃、生机勃勃的社区：很多人会推荐你从 Flask 入手， Flask 是最好的现代 web 开发的 python 框架之一。

### 2. “微”是什么意思？

“微”并不代表整个应用只能塞在一个 Python 文件内，当然塞在单一文件内也是小事一桩。“微”也不代表 Flask 功能不强。微框架中的“微”字表示 Flask 的目标是保持核心简单但是可扩展。 Flask 不会替你做决定，比如选用何种数据库。类似的决定，如使用何种模板引擎，是非常容易改变的。 Flask 可以变成你任何想要的东西，不会变成任何你不想要的东西，一切由你做主。

缺省情况下， Flask 不包含数据库抽象层、表单验证或者其他已有的库可以处理的东西。然而， Flask 通过扩展为你的应用支持这些功能，就如同这些功能是 Flask 原生的一样。有无数的扩展可以支持数据库整合、表单验证、上传处理和各种开放验证等等。Flask 可能是“微小”的，但绝不简单，可以满足各种生产需要。

## 三、程序的基本结构

### 3.1 创建项目文件夹

首先在 `/home/shiyanlou/Code` 目录下，执行以下命令：

```
$ mkdir shiyanlou_cs355
$ cd shiyanlou_cs355 
```

该语句在 `Code/` 目录下创建了文件夹 `shiyanlou_cs355` 文件夹，并切换到 `shiyanlou_cs355/` 文件夹之下。

然后执行以下命令，创建项目相关文件夹。

```
$ mkdir -p louqa/qa
$ mkdir -p louqa/static
$ mkdir -p louqa/templates
```

刚刚创建的三个文件的作用分别是：

- `louqa/qa` ：用于存放问答系统程序。
- `louqa/static` ：用于存放静态文件（如：图片、JS 文件以及 css 文件等）。
- `louqa/templates` ： 用于存放模板文件。

### 3.2 创建虚拟环境

使用 `virtualenv` 在 `shiyanlou_cs355` 目录之下创建虚拟环境 `venv` ，并指定 Python 版本为 `Python3` 。

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ virtualenv -p /usr/bin/python3  venv  
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472118630704.png/wm)

执行完后，在目录 `/home/shiyanlou/Code/shiyanlou_cs355` 下会增加一个名为`venv`的文件夹。

接下来激活虚拟环境。

```
source venv/bin/activate
```

虚拟环境被激活后，其中 Python 解释器的路径就被添加进 `PATH` 中，但这种改变不是永久性的，它只会影响当前的命令行会话。为了提醒你已经激活了虚拟环境，激活虚拟环境的命令会修改命令行提示符，在 `$` 前面加入环境名，如下图所示：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472118873186.png/wm)

### 3.3 在虚拟环境中安装 flask 包

安装 `flask` 。

```
(venv) $ pip install flask
```

然后执行

```
(venv) $ python -c "import flask"
```

若无任何提示，表示 flask 安装成功

> 提示：可以使用命令 `(venv) $ deactivate` 来退出虚拟环境

### 3.4 创建程序文件

执行以下指令创建程序所需文件。

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ touch run.py
$ touch louqa/__init__.py
$ touch louqa/flask_app.py
$ touch louqa/qa/__init__.py
$ touch louqa/qa/views.py
```

这些文件的作用分别是：

- `run.py` ：配置运行 flask 程序的文件；
- `louqa/__init__.py` ：python 只会把包含 `__init__.py` 的目录当作 python 的模块来对待；
- `louqa/flask_app.py` ：用于初始化 flask 的 `app` 对象；
- `louqa/qa/views.py` ：`views` 程序负责处理用户请求。

至此，整个项目的目录树如下：

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472120145222.png/wm)

> 提示：`tree` 是一个可以以目录树的形式展示目录文件结构的工具，可以通过命令 `$ sudo apt-get install tree` 进行安装。

### 3.5 编写 `louqa/flask_app.py` 文件

使用 gedit 或者 GVIM 打开 `flask_app.py` 文件进行编辑，写入如下代码。

```
#! /usr/bin/env python
# encoding: utf-8

from flask import Flask

# 创建 Flask 程序实例
app = Flask(__name__)  
```

所有 Flask 程序都必须创建一个程序实例。 Web 服务器把接收来自客户端的所有请求都转交给该实例对象处理。程序实例是 Flask 类的对象。 Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。而在大多数程序中， Python 的 `__name__` 变量会存储这些值。

### 3.6 编写 `louqa/qa/views.py` 文件

```
#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint  

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/')
def index():
    # 返回带有 HTML 标签装饰的 'Hello World'
    return "<p>Hello World</p>"  
```

Flask 用蓝图 `blueprint` 的概念来在一个应用中或跨应用制作应用组件和支持通用的模式。通过不同的 `url_prefix` ，从而使用户的请求到达不同模块的 `view` 函数。

用户在访问一个网站的时候，浏览器把请求发送给 Web 服务器， Web 服务器再把请求发送给 Flask 程序实例。程序实例需要知道对每个 URL 请求要调用哪些函数方法进行处理响应，所以保存了一个 URL 到 Python 函数的映射关系。

在 Flask 框架中处理 URL 和函数之间映射关系的程序称为路由。在本次程序中定义路由的方式是 `Blueprint` 生成的 `qa.route` 修饰器，把修饰的函数注册为路由。我们将 `index` 函数注册为 `qa` 模块的根地址，又由于 `qa` 模块的 `url_prefix` 为 `''` （即为空），因此该 `index` 函数也为整个flask程序根目录。

### 3.7 编写 `louqa/qa/__init__.py` 文件

```
#!/usr/bin/env python
# encoding: utf-8

from .views import qa
```

从 `views` 模块导入对象实例 `qa` ，使 flask 程序可以在 `veiws.py` 文件之外使用实例 `qa` 。

`.views` 的 `.` 为相对路径的标识，表示当前目录下的 `views.py` 文件。

### 3.8 编写 `louqa/__init__.py` 文件

> 注意：上一个 `__init__.py` 文件是 `louqa/qa/` 目录下的，而这个是 `louqa/` 目录下的。

```
#!/usr/bin/env python
# encoding: utf-8

from .qa import qa
from .flask_app import app

app.register_blueprint(qa)
```

将 `qa/views.py` 中的 `Blueprint` 的实例 `qa` 注册到 Flask 的实例 `app` 上。

### 3.9 编写 `run.py` 文件

```
#!/usr/bin/env python
# encoding: utf-8

from louqa import app

app.run(debug=True, port=9000)
```

这段程序从我们的 `louqa` 包中导入 `app` 变量并且调用它的 `run` 方法来启动服务器。

请记住 `app` 变量中含有我们在之前创建的 Flask 实例。

其中我们开启了 `debug` 模式，并指定了访问端口为 `9000`，`port` 参数如果没有指定，则默认为 `5000` 。

> 提示：端口号可以随意指定，只要数字设置得大一些，一般都不会存在被占用的情况。

### 3.10 运行服务器程序

服务器的基本框架我们已经搭建好了，要运行这个服务器分为以下几个步骤：

1. 打开 Xface 终端，进入到目录 `/home/shiyanlou/Code/shiyanlou_cs355` 之中。
2. 激活虚拟环境
3. 编译运行服务器

以上几步操作的命令对应如下：

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ source venv/bin/activate
(venv) $ python run.py
```

在服务器初始化后，它将会监听在 `9000` 号端口。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472178399088.png/wm)

现在打开实验桌面上的浏览器输入 URL `http://127.0.0.1:9000` 进行访问，如下图，浏览器展示了一段 `Hello World` 说明我们的服务器已经能正常运行和响应请求了。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472178744789.png/wm)

这时候我们查看后台服务器，发现后台对请求以及响应状态也有相应的输出。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472178987568.png/wm)

> 提示：可以通过 `Ctrl+C` 来终止后台服务器程序的运行。

## 四、Flask 模板

通过之前的操作，我们已经实现了一个最简单的基于 Flask 框架的服务器。但只是目前我们的这个页面还是相当朴素的，另外如果我们要展示一个稍微复杂点的页面，显然还只是通过之前 `louqa/qa/views.py` 程序中使用 `return "Hello World"` 这样的方式是很不合理的，因此 Flask 自动为你配置好 [Jinja2](http://docs.jinkan.org/docs/jinja2/) 模版。接下来我们将学习 Jinja2 模板引擎。

为了便于同学们学习时参考使用，我先将当前项目的文件结构树展示出来：

```python
/home/shiyanlou/Code/shiyanlou_cs355/
|-- louqa/
|   |-- __init__.py
|   |-- flask_app.py
|   |-- qa/
|   |   |-- __init__.py
|   |   `-- views.py
|   |-- static/
|   `-- templates/
|-- run.py
`-- venv/
```

### 4.1 Jinja2 模板引擎简介

模板是一个包含响应文本的文件，其中包含用占位变量表示的动态部分，其具体值只在请求的上下文中才能知道。使用真实值替换变量，再返回最终得到的响应字符串，这一过程称为渲染。为了渲染模板，Flask使用了一个名为 Jinja2 的强大模板引擎。

执行以下命令创建新的模板文件。

```python
cd /home/shiyanlou/Code/shiyanlou_cs355/
mkdir louqa/templates/qa/
touch louqa/templates/qa/index.html
```

### 4.2 编写 `louqa/templates/qa/index.html` 模板

```
<html>
    <head>
        {% if title %}
        <title> {{ title }}</title>
        {% else %}
        <title> no title </title>
        {% endif %}
    </head>
    <body>
        <h1>hello, {{ tem_str }}</h1>
    </body>
</html>
```

类似于 `{{ title }}` 的 `{{ }}` 结构,它是一种特殊的占位符，告诉模板引擎在这个位置的值在渲染时使用从程序中传来的参数进行替换。 Jinja2 能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象。在 `{{ }}` 中使用他们和在普通Python一样。

而类似于`{% if title %}`为 jinja2 的控制结构，下面这个例子展示了如何在模板中使用条件控制语句。

```
{% if title %}
     <title> {{ title }}</title>
      {% else %}
     <title> no title </title>
 {% endif %}
```

另一种常见需求是在模板中渲染一组元素。下例展示了如何使用 `for` 循环实现这一需求：

```
<ul>
    {% for item in item_list %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

> 补充：关于 Jinjia2 模板的更多信息请参考 [Template Designer Documentation](http://jinja.pocoo.org/docs/dev/templates/) 。

同时为了让 `views` 程序能返回我们的模板，我们也需要修改 `louqa/qa/views.py` 文件，修改之后的完整程序如下：

```
#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint
from flask import render_template

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
    return render_template("qa/index.html", title=title, tem_str="world")
```

细心的同学一定发现了我们从 flask 包中新导入一个名为 `render_template` 的函数，这个函数集成了 Jinja2 模板引擎。

`render_template` 函数的第一个参数指明了模板的地址，采用的是相对地址，程序默认模板在 `templates/` 文件夹之下。随后的参数都是键值对，表示模板中变量对应的真实值。

比如说，第二个参数 `title=title` 表示模板收到一个名为 `title` 的变量，在实际渲染过程中，程序就会使用传递进去的参数 `title` 对实际模板中的 `title` 变量进行替换。

另外可以发现与上一次代码的另外一个不同点在于路由定义部分：

```
... ...
@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
... ...
```

形如 `` 这样的表达式，尖括号中的内容就是动态部分，任何能匹配静态部分的 URL 都会映射到这个路由上。

在获取到 URL 请求之后服务器调用视图函数时， Flask 会将动态部分作为参数传入函数。路由中的动态部分默认使用字符串类型，不过也可使用类型定义。例如，路由 `/user/` 只会匹配动态片段 `id` 为整数的 URL 。

Flask 支持在路由中使用 `int` 、 `float` 和 `path` 类型。其中 `path` 类型也是字符串，但不把斜线视作分隔符，而将其当作动态片段的一部分。

我们可以在路由里面设置 `defaults` 来给变量设置默认值。如， `@qa.route('/', defaults={'title': None})` 表示用户直接访问根目录时将 `title` 初始化为 `None` ，用来表示没有获取到 `title` 时的值。

### 4.3 运行服务器

依然要先进入目录 `/home/shiyanlou/Code/shiyanlou_cs355` ，在虚拟环境中启动服务器。

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ source venv/bin/activate
( venv ) $ python run.py
```

此时访问 `http://127.0.0.1:9000` 页面标题显示 `no title` 。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472187623271.png/wm)

访问 `http://127.0.0.1:9000/shiyanlou` ， 页面标题显示 `shiyanlou`。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472187686322.png/wm)

## 五、数据库

如果你依照上面的实验的话，你应当有一个完全工作的简单的 web 应用程序，我们项目的文件目录树如下:

```python
/home/shiyanlou/Code/shiyanlou_cs355/
|-- louqa/
|   |-- __init__.py
|   |-- flask_app.py
|   |-- qa/
|   |   |-- __init__.py
|   |   `-- views.py
|   |-- static/
|   `-- templates/
|       `-- qa/
|           `-- index.html
|-- run.py
`-- venv/
```

你可以在虚拟环境下执行 `python run.py` 来运行应用程序，接着在通过网页浏览器访问 `http://127.0.0.1:9000` 。

我们接下来讲述的正是我们上一章离开的地方，所以你可能要确保应用程序正确地安装和工作。

### 5.1 数据库简介

数据库按照一定规则保存程序数据，程序再发起查询取回所需的数据。最常用的数据库是基于关系模型，这种数据库也称为 SQL 数据库，因为它们使用结构化查询语言。不过最近几年文档数据库和键值对数据库成了流行的替代选择，这两种数据库合称 NoSQL 数据库。而本次教程选择使用传统的关系型数据库 MySQL 。

### 5.2 安装 mysql 与 mysqlclient

由于实验楼环境中已经安装了 MySQL ，所以该步骤可以略过。

> 补充：这里还是介绍一下 ubuntu 操作系统中安装 MySQL 的方法。命令如下：

> ```
> sudo apt-get install mysql-server
> ```
>
> 安装过程会提示设置用户名与密码，这个需要注意设置。

而实验楼环境中的 MySQL 用户名为 `root` ，密码为空。

接下来安装 mysqlclient 。要想使 python 可以操作 mysql 就需要 MySQLdb 驱动，它是 python 操作 mysql 必不可少的模块。

```
(venv) $ pip install mysqlclient
```

启动 MySQL 服务器，以 `root` 账户登录。

```
$ sudo service mysql start
$ sudo mysql -u root 
```

进入了 MySQL 控制台。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472191755303.png/wm)

然后依次执行以下命令：

```
// 在本地创建一个名为 'qa' 的用户，它的密码为 '1qaz'
mysql> create user 'qa'@'localhost' IDENTIFIED BY '1qaz';

// 创建一个名为 'qa' 的数据库，字符编码方式为 'utf8'
mysql> create database qa character set = utf8;

// 赋予用户 'qa' 在数据库 'qa'上所有权限
mysql> grant all on qa.* to 'qa'@'localhost';
```

> 提示：退出数据库可以通过命令 `mysql> quit;`

### 5.3 Flask-SQLAlchemy

Flask-SQLAlchemy 是一个 Flask 扩展，简化了在 Flask 程序中使用 SQLAlchemy 的操作。 SQLAlchemy 是一个很强大的关系型数据库框架，支持多种数据库后台。 SQLAlchemy 提供了高层 ORM ，也提供使用数据库原生 SQL 的低层功能。

#### 5.3.1 安装 Flask-SQLAlchemy

还是老惯例，先进入目录 `/home/shiyanlou/Code/shiyanlou_cs355` ，开启虚拟环境，在虚拟环境中执行 Flask-SQLAlchemy 的安装操作。

```
# 
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ source venv/bin/activate  # 已在虚拟环境中则不需要重新启动虚拟环境，此步可忽略


// 安装 Flask-SQLAlchemy
(venv) $ pip install mysqlclient

(venv) $ pip install flask-sqlalchemy

(venv) $ pip install flask-script

(venv) $ pip install flask-migrate
```

`flask-script` 是一个 Flask 扩展，为 Flask 程序添加了一个命令行解析器。 Flask-Script 自带了一组常用选项，而且还支持自定义命令。

`flask-migrate` 是一个对 [Alembic 库](http://my.oschina.net/banxi/blog/126695) 的轻量级包装。并集成到 Flask-Script 中，所有操作都通过 `flask-script` 命令完成。其中 `Alembic` 是 SQLAlchemy 的迁移框架（当我们需要修改数据库模型时，可以通过迁移框架来自动完成数据库的变化）。

安装完成后退出虚拟环境 `venv` 。

```
(venv) $ deactivate
```

#### 5.3.2 Flask-SQLAlchemy 与 mysql 的连接

创建以下文件。

```
cd /home/shiyanlou/Code/shiyanlou_cs355/
touch louqa/config.py
touch louqa/dbs.py
touch manage.py
```

编写 `louqa/config.py` 文件。

**config.py:**

```
#!/usr/bin/env python
# encoding: utf-8


class FlaskConfig(object):
    # 配置了数据库服务相关信息，如账号、密码等
    SQLALCHEMY_DATABASE_URI = "mysql://qa:1qaz@localhost/qa"
```

`config.py` 为放置 flask 全局配置的文件，本次我们只需要在该文件配置 'SQLALCHEMY_DATABASE_URI' 一项即可。

> 补充：关于 Flask-SQLAlchemy 的配置详情请参考 [Flask-SQLAlchemy 快速入门](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)。

编写 `louqa/dbs.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from flask_sqlalchemy import SQLAlchemy
from .flask_app import app

db = SQLAlchemy(app)
```

该文件主要用于初始化数据库的对象。

同时还需要修改 `/home/shiyanlou/Code/shiyanlou_cs355/louqa` 目录下的 2 个文件。

- flask_app.py
- __init__.py

首先修改 `louqa/flask_app.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from .config import FlaskConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)
```

该文件主要增加了 `app.config.from_object(FlaskConfig)` ，表示 `app` 从 `FlaskConfig` 中初始化配置，从而使 `dbs.py` 中的 `db` 实例初始化时得到数据库相关信息。

然后修改 `louqa/__init__.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8
from .qa import qa
from .flask_app import app
from .dbs import db

app.register_blueprint(qa)
```

该文件主要增加了`from .dbs import db` 以方便外部的文件调用。

再编写 `shiyanlou_cs355/manage.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from louqa import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
```

`manage.py` 的功能为管理数据库迁移，它的使用将在下文出现。

### 5.4 模型

模型这个术语表示程序使用的持久化实体。在 ORM 中，模型一般是一个 Python 类，类中的属性对应数据库表中的列。 Flask-SQLAlchemy 创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函数，可用于定义模型的结构。

#### 5.4.1 实现一个简单的模型

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355/

// 新建一个 'user' 模块
$ mkdir -p louqa/user

// 新建一个models.py文件，用于实现模型
$ touch louqa/user/models.py

$ touch louqa/user/__init__.py
```

以上的代码在 `/home/shiyanlou/Code/shiyanlou_cs355/louqa/` 目录底下新建了一个 `user` 模块，用于实现模型。

编写 `louqa/user/models.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from ..dbs import db
from sqlalchemy import Column


class User(db.Model):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(32), nullable=False, unique=True)
```

`User` 类定义的属性 `__tablename__` 定义了在数据库中使用的表名为 `users` 。如果没有定义 `__tablename__` 属性 ，则 Flask-SQLAlchemy 会使用一个默认名字，其余的类属性都是该模型的属性，而且都被定义为 `Column` 类的一个实例。

`Column` 类构造函数的第一个参数定义了 `users` 表某一列的 类型（也即模型某一属性的类型），其余的参数指定该列的配置选项。

另外值得注意的是，要确保有一个 `Column` 类实例被设置为 `primary_key=True` （即将当前列设为主键），而通常的做法是将 `id` 设为主键。

> 补充：更多详细的配置情况请查看 [sqlalchemy Column and Data Types](http://docs.sqlalchemy.org/en/rel_1_0/core/type_basics.html?highlight=column) 。

因此，这里的 `User` 类定义了一张名为 `users` 的表，表中含有两列，分别为 `id` 和 `name` 。其中 `id` 的类型是整型，为主键；`name` 的类型为最大长度为 32 个字符的字符串，不能为空且唯一。

编写 `louqa/user/__init__.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from .models import User
```

还要修改 `louqa/qa/views.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template
from ..user import User

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
      user = User.query.filter().first()
      return render_template("qa/index.html", title=title, tem_str=user.name)
```

`from ..user import User` 表示从 `user` 模块导入 `User` 类。

`user = User.query.filter().first()` 表示对 `User` 类操作。如字面上的意思 它表示对 `User` 类查询，过滤条件为空（即无限制），取符合条件的第一个数据。此时表 `users` 为空，所以下文中我们将手工往表 `users` 中插入一条数据。

#### 5.4.2 初始化数据库

执行以下命令初始化数据库。

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ source venv/bin/activate
(venv) $ python manage.py db init
(venv) $ python manage.py db migrate
(venv) $ python manage.py db upgrade
(venv) $ deactivate
```

`python manage.py db init` 命令将创建迁移仓库，它执行后会在 `/home/shiyanlou/Code/shiyanlou_cs355` 目录下生成一个名为 `migrations` 的文件夹。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472199498218.png/wm)

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472199508953.png/wm)

`python manage.py db migrate` 用来自动创建迁移脚本，并且还会在数据库 `qa` 下创建一个名为 `alembic_version` 的表，可以进入 MySQL 使用 `show tables` 命令进行查看。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472199939438.png/wm)

`python manage.py db upgrade` 命令把迁移中的改动应用到数据库中，这一步将在数据库 `qa` 中创建表 `users` 。

#### 5.4.3 登录 MySQL 服务器

使用之前创建的 MySQL 账户 'qa' 进行登录。

```
$ mysql -u qa -p
```

执行上方命令之后，按照提示输入密码（1qaz），登录数据库服务器。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472200461554.png/wm)

执行 `mysql> use qa;` 选择 `qa` 数据库为后续操作对象。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472200586135.png/wm)

再执行 `mysql> show tables;` ，发现多了一张 `users` 表。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472200700559.png/wm)

然后输入`insert into users (name) values ('shiyanlou');`，这条语句向 `users` 表中插入一个用户名为 `shiyanlou` 的用户。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472200909710.png/wm)

输入 `quit;` 退出 MySQL 。

### 5.5 测试

执行以下命令

```
$ cd /home/shiyanlou/Code/shiyanlou_cs355
$ source venv/bin/activate
(venv) $ python run.py
```

然后通过浏览器访问 `http://127.0.0.1:9000` 发现网页内容变为了 `hello, shiyanlou` ，表明该数据是从数据库中读取出来的。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1110timestamp1472201257299.png/wm)

## 六、本节总结及下节预告

本节实验主要进行了开发环境的搭建以及 Flask Web 应用的框架开发。 本章节完整代码

```
wget http://labfile.oss.aliyuncs.com/courses/355/shiyanlou_cs355_v1.zip
unzip shiyanlou_cs355_v1.zip
```

完整代码开启虚拟环境后可使用 pip 读取文件方式安装

```
pip3 install -r  pip_req/requirements_1.txt # 安装
```

下一节将主要介绍问答系统中用户管理系统的实现。

## 七、实验报告

在实验报告中详细描述你的操作过程。



## 用户管理

# 用户系统

对于一个问答网站，我们需要分别知道问题和回答的发表人，所以我们需要一个用户系统，用于认证用户。同时只有认证的用户才能发表问题和回答。本次课程我们主要内容是利用 flask 开发一个完整的用户认证系统。

## 一、准备工作

### 1.1 在实现用户系统中需要用到的库

1. `Flask-Login`：管理已登录用户的用户会话。
2. `Werkzeug`：一个 [WSGI](http://baike.baidu.com/link?url=54ktjMwK0UEl8nStv9uzln8qJrpRtwnDsIp9-LxuImNDchpIqAqRJECY4ylN_2wMxk4BxeuklT0Xh_qh1mY9y_) 工具箱，提供了很多开发网站的实用工具，Flask 框架基层依赖 Werkzeug ， 我们将使用它进行计算密码散列值并核对。
3. 下载 demo 代码（ 此demo为含有第一周的代码以及第二周用到的前端实现代码）

```
$ cd /home/shiyanlou/Code/
$ wget http://labfile.oss.aliyuncs.com/courses/355/shiyanlou_cs355_v2-1.zip
$ unzip shiyanlou_cs355_v2-1.zip
$ cd shiyanlou_cs355_v2-1
```

### 1.2 配置虚拟环境

```
// 创建虚拟环境
$ virtualenv -p /usr/bin/python3 venv

// 激活虚拟环境
$ source venv/bin/activate

// 安装依赖模块
(venv)$ pip install -r pip_req/requirements_1.txt
```

由于新的实验环境中没有配置我们项目的用户，仍然需要执行下述步骤来配置 MySQL ：

> 温馨提示：如果你的 MySQL 中已经存在了 `qa` 数据库，那么便不用执行以下操作，可跳到初始化数据库操作那一步。

```
$ sudo service mysql start
$ mysql -u root -e "create user 'qa'@'localhost' IDENTIFIED BY '1qaz';"
$ mysql -u root -e "create database qa character set = utf8;"
$ mysql -u root -e "grant all on qa.* to 'qa'@'localhost';"
```

接下来再进行初始化数据库的操作：

> 温馨提示：如果你的 `qa` 数据库中已经存在表 `alembic_version` 以及表 `users` ，可以执行 `drop table 表名;` 进行删除。

> **注意**：由于 demo 中已经编写好了部分代码，下面将会对未实现的代码文件进行讲解，同学们可以根据这些讲解以及本章节结束时的代码示例基础上继续补充完善。

## 二、用户模型

在上节课中，我们实现了一个仅有 `id` 和 `name` 两列的表 `users` 。然后这节课我们要在它的基础上增加一些其他的属性。

通常来说，对一名用户的认证是通过对身份证明（用户名或者邮箱）以及密码进行匹配检验来实现的。因此我们需要给 `users` 表添加两个表项。

1. 用户邮箱
2. 密码

此外考虑到目前网络上日益严重[*拖库事件*](http://baike.baidu.com/view/7146795.htm)，所以我们不能使用明文方式直接保存密码到数据库中，而是采用存储密码的[ hash 值](http://baike.baidu.com/view/20089.htm)密文。

利用密码的 hash 值用户认证的大致思想是：计算密码散列值的函数接收密码明文作为输入，使用一种或多种加密算法转换密码，最终得到一个和原始密码没有关系的字符序列，也就是密文写入数据库中。核对密码时，从数据库中取出加密后的密码进行校验，因为计算散列值的函数是可复现的：只要再次输入的明文密码一样，则加密后的结果也就一样。

在这里我们使用 `Werkzeug` 库下的 `security` 模块实现密码散列。

### 2.1 实现密码 hash

查看[ Werkzeug 文档](http://werkzeug.pocoo.org/docs/0.10/utils/#module-werkzeug.security)，发现函数 `werkzeug.security.generate_password_hash(password, method='pbkdf2:sha1', salt_length=8）` 可以用来生成明文密码对应的 hash 密文。然后函数 `werkzeug.security.check_password_hash(pwhash, password)` 可以用来检测明文密码是否与密文相等。

> 提示：由于 `Werkzeug` 库为 `flask` 的依赖，所以不需要再单独安装。

### 2.2 `User` 类

`louqa/user/models.py` 中对 `User` 类的定义如下。

```
#!/usr/bin/env python
# encoding: utf-8

from ..dbs import db
from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)

    name = Column(db.String(32), nullable=False, unique=True)
    email = Column(db.String(64), nullable=False, unique=True)

    __password = Column(db.String(128))

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.__password, password)
```

这段代码给 `User` 类增加了 `email` 和 `__password` 两个属性， 另外还添加了 `set_password` 与 `verify_password` 两个方法，分别用于加密明文密码与验证密码。

## 三、用户注册

### 3.1 添加用户注册视图函数

在 `user` 下，增加一个 `views.py` 文件，专门用于放置与用户数据处理相关的视图函数，并新增加一个 `user` 蓝图。

编写 `louqa/user/views.py` 文件。

```
#!/usr/bin/env python
# encoding: utf-8

from flask import (Blueprint, request, current_app, redirect, url_for,
        jsonify)
from .models import User
from sqlalchemy import or_
from ..dbs import db


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/signup', methods=['POST'])
def signup_user():
    try:
        user_instance = User.query.filter(or_(User.name==request.form['name'],
                                            User.email==request.form['email'])).first()
        if user_instance:
            return jsonify(status="error", info=u"已存在该用户")
        else:
            # 创建 User 类实例，获取表单信息，写入数据库
            user_instance = User()
            user_instance.name = request.form['name']
            user_instance.email = request.form['email']
            user_instance.set_password(request.form['password'])
            db.session.add(user_instance)
            db.session.commit()
            return jsonify(status="success", info=u"创建成功")
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))
```

在 `views.py` 文件里面，我们新增加了一个 `user` 蓝图，并实现了注册用户的视图函数（现在暂不考虑安全性） `signup_user()` 。

在这个函数的最开始，它先去查数据库里面有没有与新注册的用户同样的用户或一样的电子邮件地址，`or_` 函数表示，该条件为或。如果数据库里面存在，表明不能注册该用户，因为已经存在，并返回提示信息。

通过 `jsonify` 这个函数将信息以 `json` 格式进行包装返回。 在 louqa/user/`__init__`.py 中注册 user

```
from .views import user
```

还需要修改 `louqa/qa/views.py` 。

```
#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template
from ..user import User

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
    return render_template("qa/index.html")
```

这里把 `index` 函数做了调整，删去了 `user = User.query.filter().first()` 查询数据库操作，也删除了传递给模板的 `title` 和 `tem_str` 参数。另外这里所用的 `index.html` 模板也做了一些的修改，因为网页前端不是本课的重点，所以这里我们直接拿来用就行。

在上面我们完成了用户注册，然而注册之后，我们需要在页面上标识用户，所以接下来我们实现用户的登录。

## 四、用户登录

我们将使用 `Flask-Login` 来管理已登录用户的用户会话。

### 4.1 初始化 `Flask-Login`

按照 [Flask-Login](https://flask-login.readthedocs.org/en/latest/) 文档的说明，我们在 `louqa/` 新建了一个名为 `extensions.py` 文件，文件内容如下。

#### `extensions.py`

```
#!/usr/bin/env python
# encoding: utf-8

from flask_login import LoginManager

login_manager = LoginManager()
```

然后在 `louqa/__init__.py` 中初始化 `login_manager` 。

#### `louqa/__init__.py`

```
from .extensions import login_manager
from .user import User
....
def configure_login(app):
    login_manager.login_view = 'qa.index'
    login_manager.refresh_view = 'qa.index'
    login_manager.login_message = None
    login_manager.session_protection = "basic"
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    login_manager.setup_app(app)
....
configure_login(app)
```

`login_view` 属性为当未登录状态的用户试图访问只有登录状态用户才能访问的网页时，web 程序要重定向的地址。`load_user` 函数为让 Flask-Login 通过用户 `id` 查询 `users` 表，获得相应的用户信息。

为了使用 `login_manager` ，我们也需要在我们的 `User` 类增加几个属性让 `login_manager` 使用。 `login_manager` 提供了一个名为 `UserMixin` ，我们可以让我们的 `User` 类继承它从而得到它需要的属性。

因此 `louqa/user/models.py` 文件修改如下。

#### `louqa/user/models.py`

```
.....
from flask_login import UserMixin

class User(db.Model, UserMixin):
.....
```

### 4.2 实现登录

`flask-login` 通过 `flask_login.login_user(user, remember=False, force=False, fresh=True)` 方法来实现一个用户的登录。

接下来看看 `louqa/user/views.py` 文件。

#### `louqa/user/views.py`

```
....
from flask_login import login_user
....

@user.route('/login', methods=['POST'])
def login_users():
    try:
        user_instance = User.query.filter(User.name==request.form['name']).first()
        if user_instance:
            if user_instance.verify_password(request.form['password']):
                login_user(user_instance)
        return redirect(url_for('qa.index'))
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))
```

当用户填写的用户名与密码和数据库里面一致时，使用 `login_user()` 使用户登录。

### 4.3 `flask-login`的使用

`flask-login` 主要通过 `current_user` 来访问当前浏览页面的用户信息。因为增加了用户登录的功能，所以我们在首页实现一个简单的功能，当用户登录后，原先显示登录状态的地方显示用户的用户名。

此时首页视图函数如下。

#### `louqa/qa/views.py`

```
....
from flask_login import current_user
....
@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
    return render_template("qa/index.html", current_user=current_user)
....
```

在该视图函数中我们向模板文件传递了current_user 实例。

为了使用 current_user ， `louqa/templates/qa/base.html` 中原先显示为登录按钮的代码修改如下。

```
....
{% if current_user.is_authenticated %}
   <ul>
       <li><a><i class="icon-user"></i>{{ current_user.name }}</a></li>
   </ul>
{% else %}
    <ul>
        <li><a href="login.html" id="login-panel"><i class="icon-user"></i>Login</a></li>
    </ul>
{% endif %}
....
```

如模板文件中所显示的一样。我们可以通过 `current_user` 的 `is_authenticated` 方法判断浏览该网页的用户是否登录。然后如果用户处于登录状态，那么我们可以通过 `current_user` 去调用 `User` 的属性与方法，否则就依然显示登录按钮。

## 五、运行代码

#### 本章节完整代码

```
wget http://labfile.oss.aliyuncs.com/courses/355/shiyanlou_cs355_v2-2.zip
unzip shiyanlou_cs355_v2-2.zip
```

完整代码开启 `虚拟环境`后可使用 `pip` 读取文件方式安装

```
pip3 install -r  pip_req/requirements_1.txt # 安装
// 激活虚拟环境
$ source venv/bin/activate
```

接下来再进行初始化数据库的操作：

> 在本节课中我们对 数据信息做了更改，所以需要 升级我们之前的数据库表。

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

运行服务器。

```
(venv)$ python run.py
```

访问 `http://127.0.0.1:9000` ，点击「注册」按钮，注册用户名和密码，进行登录。![此处输入图片的描述](https://doc.shiyanlou.com/document-uid457169labid1149timestamp1521447544899.png/wm)

现在的数据库字段 可以使用 desc查看；

```
mysql> desc users;
```

## 六、本节总结及下节预告

本节实验熟悉了问答系统中用户管理系统的实现。下一节将主要介绍问答系统中问答模块的实现。

## 七、实验报告

在实验报告中详细描述你的操作过程。



# 问答模块

首先下载本次课程所需使用的 demo 代码

1. 下载 demo 代码（ 此demo为含有前两周的代码以及第三周用到的前端部分实现代码）

```bash
$ cd /home/shiyanlou/Code/
$ wget http://labfile.oss.aliyuncs.com/courses/355/shiyanlou_cs355_v3-1.zip
$ unzip shiyanlou_cs355_v3-1.zip
$ cd shiyanlou_cs355_v3-1/
$ virtualenv -p /usr/bin/python3 venv3
$ source venv3/bin/activate
$ pip install -r pip_req/requirements_1.txt
```

> 这里要删除上一周的 demo 文件夹，移除的前提是你的虚拟机中还保存存着上节课的 demo 。不要忘记重新创建虚拟环境

由于实验环境中没有配置我们项目的用户，仍然需要执行下述步骤来配置 MySQL ：

> 温馨提示：如果你的 MySQL 中已经存在了 `qa` 数据库，那么便不用执行以下操作，可跳到初始化数据库操作那一步。

```
$ sudo service mysql start
$ mysql -u root -e "create user 'qa'@'localhost' IDENTIFIED BY '1qaz';"
$ mysql -u root -e "create database qa character set = utf8;"
$ mysql -u root -e "grant all on qa.* to 'qa'@'localhost';"
```

接下来再进行初始化数据库的操作：

> 温馨提示：如果你的 `qa` 数据库中已经存在表 `alembic_version` 以及表 `users` ，可以执行 `drop table 表名;` 进行删除。

## 一、数据库模型

对于大多数的问答系统（如 [quora](https://www.quora.com/) ，[知乎](http://www.zhihu.com/)），都存在下面结构。

```
问题
|__回答一
|  |__ 回答一的评论一
|  |__ 回答一的评论二
|
|__回答二
|
......
```

所以我们也将按照这样的结构去实现一个最简单的问答系统。

首先我们在 `/shiyanlou/Code/shiyanlou_cs355_v3-1/louqa/qa` 文件夹下面新添加了一个 `models.py` 文件。(下载的文件夹中已包含此文件，但内容为空，可以直接编写代码)

### 1.1 `Question` 模型

对于一个问题，它肯定具有标题、内容、问题发起人。

所以我们先实现一个最基本的 `Question` 数据库模型，代码如下。

#### `louqa/qa/models.py 中 Question 模型编写`

```
from ..dbs import db
from sqlalchemy import Column
from ..funcs import get_current_time

class Question(db.Model):

    __tablename__ = 'questions'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(128), nullable=False)
    content = Column(db.Text(1024))
    answers_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    author = db.relationship("User", backref=db.backref(
                            "questions", lazy="dynamic"), uselist=False)
```

这个最基本的 `Question` 模型包含了：

1. 问题的名字 `name`
2. 问题的详细描述 `content`
3. 回复答案的个数 `answers_count`
4. 问题的创建时间 `create_time`
5. 提问者的数据库编号 `author_id` 和用户名 `author`

另外与之前定义 `User` 模型比较不同的一点是，这里多了一个 `db.relationship` 函数， `relationship` 相当于一个可以访问其它模型的属性的代理，在 `sqlalchemy` 里面实现 `relationship` ，只需要先声明一个要连接的模型的外键。比如，在 `Question` 里面 `author_id` 被定义为外键，它连接的是 `User` 模型的 `id` 属性，它存储的是发表该问题的人的 `User.id` 。

然后声明一个 `db.relationship` ，如，这里为 `author` ， 可以通过它去访问发表该问题的用户的 `User` 的所有信息。其中第一个参数 `"User"` 表明它要代理的模型为 `User` 类，第二个参数 `backref` 是反向的作用即我们现在可以通过 `Question.author` 去访问 `User` ，那么通过设置该参数，然后通过 `User.questions` 来访问到 `Question` ，它的第一个参数即为 `Question` 在 `User` 中的名字。 `uselist=False` ，如果不设置该参数，那么访问 `author` 属性可能得到的是一个列表，但是很明显，从逻辑上而言一个问题的创建者只有一个，所以使用 `uselist=False` 。

> 参考：想获取更多关于 `db.relationship` 模式的资料可以访问 [Basic Relationship Patterns](http://docs.sqlalchemy.org/en/rel_1_0/orm/basic_relationships.html)。

### 1.2 `Answer` 模型

对于一条回答，一般来说我们需要存储的信息有

1. 答案的内容
2. 答案的创建时间
3. 答案的评论数
4. 答案作者的用户名
5. 答案回复所针对的问题

接下来就让我们来看看 `Answer` 模型该如何定义。

#### `louqa/qa/models.py 的 Answer 类编写`

```
class Answer(db.Model):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    content = Column(db.Text(1024))
    comments_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    author = db.relationship("User", backref=db.backref(
                            "answers", lazy="dynamic"), uselist=False)

    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    question = db.relationship("Question", backref=db.backref(
                            "answers", lazy="dynamic"), uselist=False)
```

回答的模型与问题的模型差不多，当然它增加的了一个与问题的关系。

### 1.3 `Comment` 模型

对每条答案的回复评论一般需要存储以下几个内容：

1. 评论的内容
2. 评论时间
3. 评论的用户
4. 评论所针对的答案

#### `louqa/qa/models.py 的 Comment 类编写`

```
class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = Column(db.Text(1024))
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    author = db.relationship("User", uselist=False)

    answer_id = Column(db.Integer, db.ForeignKey("answers.id"))
    answer = db.relationship("Answer", backref=db.backref(
                            "comments", lazy="dynamic"), uselist=False)
```

## 二、问答模块的视图函数

对于一个基本的问答系统来说，它至少需要具备下列的功能：

1. 发表问题
2. 发表问题的答案
3. 对答案的既评论与显示这些数据

### 2.1 增加问题与显示问题列表

增加问题与显示问题列表在一个视图函数中实现，代码如下（如果无法输入中文的话可以使用英文进行替换）：

#### `louqa/qa/views.py 中 question_info 函数实现`

```
from flask import Blueprint, render_template, current_app, jsonify, request, redirect, url_for
from ..user import User
from flask_login import current_user
from .models import Question, Answer, Comment
from ..dbs import db

@qa.route('/question/add', methods=["GET"])
def add_question():
    return render_template("qa/ask_question.html")



@qa.route('/question', methods=["GET", "POST"])
def question_info():
    try:
        if request.method == "POST":
            if not current_user.is_authenticated:
                return jsonify(status="error", info=u"请先登录")
            question_instance = Question.query.filter(Question.name==request.form['title']).first()
            if question_instance:
                return jsonify(status="error", info=u"已存在该问题")
            else:
                question_instance = Question()
                question_instance.author_id = current_user.id
                question_instance.name = request.form['title']
                question_instance.content = request.form['content']
                db.session.add(question_instance)
                db.session.commit()
                return jsonify(status="success", info=u"创建成功")
        else:
            question_list = Question.query.filter().all()
            return render_template("qa/questions.html", qss=question_list)
    except Exception as e:
        current_app.logger.error(e)
        if request.method == "POST":
            return jsonify(status="error", info=u"错误")
        else:
            return redirect(url_for('qa.index'))
```

在上面的代码中，我们使用 HTTP 的 `POST` 和 `GET` 方法去区分增加问题和显示问题列表。

当增加问题的时候，首先网页里面的 `js` 程序向 `/question` 发送 `POST` 请求。

#### `louqa/static/js/ask.js`

```
$(document).ready(function() {
    $("#nav-ask").addClass("current_page_item");
    $("#publish-question").click(function(){
        var title = $("#question-title").val();
        var content = $("#question-details").val();
        var post_url = $("#question-data").attr("url");
        $.post(post_url, {"title": title, "content": content }, function(data){
            alert(data.info);
        });
    });
});
```

可以发现这个程序只是简单的向 `question_info()` 发送 `post` 请求，它发送的数据包括包含：

1. 标题 `title`
2. 内容 `content`

现在回到前面的 `views.py` 文件中的 `question_info()` 函数，它用于接受前端 `js` 发送的请求，并创建新的问题。

首先检测发送 `POST` 请求的用户是否登录，如果没有登陆则返回没有登陆的提示的 `json` 文件。然后检测有数据库中是否有和请求里面标题一样的问题存在。如果存在则返回错误信息，不存在就创建新的问题。

当显示问题列表的时候，直接返回所有的问题。

```
question_list = Question.query.filter().all()
return render_template("qa/questions.html", qss=question_list)
```

当然当数据项非常多的时候，应该进行分页，`Flask-SQLAlchemy` 提供 [Pagination](https://pythonhosted.org/Flask-SQLAlchemy/api.html#flask.ext.sqlalchemy.Pagination) 来完成这个。

对于该视图函数的中出现的

```
try:
....
....
except Exception as e:
        current_app.logger.error(e)
        if request.method == "POST":
            return jsonify(status="error", info=u"错误")
        else:
            return redirect(url_for('qa.index'))
```

该异常处理语句表示如果在程序运行过程中出现错误，该语句会通过 `current_app.logger.error(e)` 记录错误信息，并返回相关信息。

### 2.2 显示单个问题详情

#### `louqa/qa/views.py questions`

```
@qa.route('/question/<int:question_id>', methods=['GET', 'POST'])
def questions(question_id):
    try:
        if request.method == "GET":
            question_instance = Question.query.filter(Question.id==question_id).first()
            if question_instance:
                return render_template("qa/question_detail.html", qs=question_instance)
            return redirect(url_for('qa.index'))
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))
```

可以发现该视图函数非常简单，通过传入问题 `id` 查询数据库，如果查询获得记录则将记录返回给模板进行渲染展示，如果不存在该问题，则转跳到首页 `qa.index` 。

### 2.3 提交答案与提交回答

提交答案与提交回答与最上面的创建问题的流程差不多。代码如下：

#### `louqa/qa/views.py add_answer`

```
@qa.route('/question/<int:question_id>/answer', methods=['POST'])
def add_answer(question_id):
    try:
        if not current_user.is_authenticated:
            return jsonify(status="error", info=u"请先登录")
        question_instance = Question.query.filter(Question.id==question_id).first()
        if not question_instance:
            return jsonify(status="error", info=u"不存在该问题")
        else:
            if request.form['rtype'] == "1":
                answer_instance = Answer()
                answer_instance.content = request.form['content']
                answer_instance.author_id = current_user.id
                answer_instance.question_id = question_id
                question_instance.answers_count += 1
                db.session.add(question_instance)
                db.session.add(answer_instance)
            elif request.form['rtype'] == "2":
                answer_instance = Answer.query.filter(Answer.id==request.form['rid']).first()
                if not answer_instance:
                    return jsonify(status="error", info=u"错误")
                comment_instance = Comment()
                comment_instance.content = request.form['content']
                comment_instance.author_id = current_user.id
                comment_instance.answer_id = answer_instance.id
                answer_instance.comments_count += 1
                db.session.add(answer_instance)
                db.session.add(comment_instance)
            else:
                return jsonify(status="error", info=u"错误")

            db.session.commit()
            return jsonify(status="success", info=u"回复成功")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(status="error", info=u"错误")
```

可以看出，该视图函数是通过 `post` 的参数来判断是添加答案或者答案的评论的，这是因为整个问题详情页面就一个回复框，通过 `js` 来改变 `post` 参数。当表单当中 `rtype` 的值为 1 时，是添加答案；而当 `rtype` 的值为 2 时，是添加评论。

#### `louqa/static/js/questions.js`

```
$(document).ready(function() {
    $("#nav-question").addClass("current_page_item");
    $("#submit").click(function(){
        var content = $("#comment").val();
        $.post($("#reply-info").attr("qs-url"), {"rid": $("#reply-info").attr("rid"), "rtype": $("#reply-info").attr("rtype"), "content": content }, function(data){
            $("#reply-info").attr("rtype", "1");
            if(data.status == "success"){
                window.location.reload();
            }else{
                alert(data.info);
            }
        });
    });
    $("[id=reply-answer]").click(function(){
        $("#reply-info").attr("rtype", "2");
        $("#reply-info").attr("rid", $(this).attr("ans-id"));
        console.log($("#reply-info").attr("rid"));
    });
});
```

可以发现，在这个js里面一共创建2个监听器。

一个是页面最下方的 `submit` 按键的监听器，它主要用于通过 `post` 方式提交数据到上面的 `add_answer` 函数。

第二个监听器是监听所有的回复答案的按钮，它主要负责当用户按下回复答案按钮时，修改回复框的数据，好使后台程序识别到它在回复答案和回复的那个答案。

## 三、效果展示

首页登录，选择提问。 接下来再进行初始化数据库的操作：

> 在本节课中我们对 数据信息做了更改，所以需要 升级我们之前的数据库表。

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

运行服务器。

```
$ python run.py
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1150timestamp1472534448561.png/wm)

跳转至输入问题的界面。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1150timestamp1472534509114.png/wm)

编辑问题进行提交，查询数据库可发现问题写入。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1150timestamp1472534524408.png/wm)

问题列表上展出问题。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1150timestamp1472534571141.png/wm)

点击问题进行回答。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1150timestamp1472534607746.png/wm)

回答问题之后，答案展示出来。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid242676labid1150timestamp1472534653681.png/wm)

## 四、增强

在 `demo` 中，提供了一个具备基本功能的 `QA` 系统。更进一步的，你可以按照你的想法为这个 `QA` 系统增加新的功能。

## 五、代码下载

#### 本章节完整代码

```
wget http://labfile.oss.aliyuncs.com/courses/355/shiyanlou_cs355_v3-2.zip
unzip shiyanlou_cs355_v3-2.zip
```

完整代码开启 `虚拟环境`后可使用 `pip` 读取文件方式安装

```
pip3 install -r  pip_req/requirements_1.txt # 安装
```

## 六、总结

本试验已完成 `QA` 系统的主要功能, 下节我们将完成项目的部署。

## 七、实验报告

在实验报告中详细描述你的操作过程。