#! /usr/bin/env python
# encoding: utf-8


from flask import Flask
from .config import FlaskConfig


# 创建Flask实例
app = Flask(__name__)
app.config.from_object(FlaskConfig)