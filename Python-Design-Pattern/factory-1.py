# -*- coding: utf-8 -*-

import random


class BasicCourse(object):
	"""docstring for BasicCourse"""
	def get_labs(self):
		return "basic_course: labs"

	def __str__(self):
		return "BasicCourse"


class ProjectCourse(object):

	def get_labs(self):
		return "project_course: labs"

	def __str__(self):
		return "ProjectCourse"

		
class SimpleCourseFactory(object):

	def create_course(type):
		if type == 'bc':
			return BasicCourse()

		elif type == 'pc':
			return ProjectCourse()


if __name__ == '__main__':
	t = random.choice(['bc', 'pc'])
	course = SimpleCourseFactory.create_course(t)
	print(course.get_labs())