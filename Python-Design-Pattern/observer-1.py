# -*- coding: utf-8 -*-

import abc


class Subject(object):
	"""
	被观察对象的基类
	"""
	
	def __init__(self):
		self._observers = []

	def attch(self, observer):
		"""
		注册一个观察者
		"""
		if observer not in self._observers:
			self._observers.append(observer)
		
	def detach(self, observer):
		"""
		注销一个观察者
		"""
		try:
			self._observers.remove(observer)
		except ValueError:
			pass
			
	def notify(self):
		"""
		通知所有观察者，执行观察者的更新方法
		"""
		for observer in self._observers:
			observer.update(self)
			
			
class Course(Subject):
	"""
	课程对象，被观察的对象
	"""
	

		
