#!/usr/bin/env python
# encoding: utf-8
# @Detail: 全局配置文件

class FlaskConfig(object):
	# 配置了数据库服务相关信息，如账户、密码等
	SQLALCHEMY_DATABASE_URI = 'mysql://qa:1qaz@localhost/qa'