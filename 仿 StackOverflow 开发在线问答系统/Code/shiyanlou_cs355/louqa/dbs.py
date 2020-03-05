#!/usr/bin/env python
# encoding: utf-8
# @Detail: 初始化数据库对象


from flask_sqlalchemy import SQLAlchemy
from .flask_app import app


db = SQLAlchemy(app)