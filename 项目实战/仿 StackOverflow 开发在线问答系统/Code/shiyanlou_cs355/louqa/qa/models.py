#!/usr/bin/env python
# encoding: utf-8

from ..dbs import db
from sqlalchemy import (Column, Integer, String, Text,
	DateTime, ForeignKey)
from ..funcs import get_current_time


class Question(db.Model):

	__tablename__ = 'questions'

	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)
	content = Column(Text(1024))
	answers_count = Column(Integer, default=0)
	create_time = Column(DateTime, default=get_current_time)

	author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
	author = db.relationship('User', backref=db.backref(
		'questions', lazy='dynamic'), uselist=False)


class Answer(db.Model):

	__tablename__ = 'answers'

	id = Column(Integer, primary_key=True)
	content = Column(Text(1024))
	comments_count = Column(Integer, default=0)
	create_time = Column(DateTime, default=get_current_time)

	author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
	author = db.relationship('User', backref=db.backref(
		'answers', lazy='dynamic'), uselist=False)

	question_id = Column(Integer, ForeignKey('questions.id', ondelete='CASCADE'))
	author = db.relationship('Question', backref=db.backref(
		'answers', lazy='dynamic'), uselist=False)


class Comment(db.Model):

	__tablename__ = 'comments'

	id = Column(Integer, primary_key=True)
	content = Column(Text(1024))
	create_time = Column(DateTime, default=get_current_time)

	author_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
	author = db.relationship('User', backref=db.backref(
		'answers', lazy='dynamic'), uselist=False)

	answer_id = Column(Integer, ForeignKey('answers.id', ondelete='CASCADE'))
	answer = db.relationship('Answer', backref=db.backref(
		'comments', lazy='dynamic'), uselist=False) 