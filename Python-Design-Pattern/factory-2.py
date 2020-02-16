# -*- coding: utf-8 -*-
import random
import abc


class BasicCourse(object):
	
	def get_labs(self):
		return "basic_course: labs"
		
	def __str__(self):
		return "BasicCourse"
		

class ProjectCourse(object):
	
	def get_labs(self):
		return "project_course: labs"
		
	def __str__(self):
		return "ProjectCourse"
		

class Factory(metaclass=abc.ABCMeta):
	
	@abc.abstractmethod
	def create_course(self):
		pass
		
		
class BasicCourseFactory(Factory):
	
	def create_course(self):
		return BasicCourse()
		
		
class ProjectCourseFactory(Factory):
	
	def create_course(self):
		return ProjectCourse()
		
		
def get_factory():
	return random.choice([BasicCourseFactory, ProjectCourseFactory])()
	
	
if __name__ == '__main__':
	factory = get_factory()
	course = factory.create_course()
	print(course.get_labs())

