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


class LinuxVm(object):
	
	def start(self):
		return "Linux vm running"
		

class MacVm(object):
	
	def start(self):
		return "Maco OSX vm running"
		

class Factory(metaclass=abc.ABCMeta):
	
	@abc.abstractmethod
	def create_course(self):
		pass
		
	@abc.abstractmethod
	def create_vm(self):
		pass
		

class BasicCourseLinuxFactory(Factory):
	
	def create_course(self):
		return BasicCourse()
		
	def create_vm(self):
		return LinuxVm()
		
		
class ProjectCourseMacFactory(Factory):
	
	def create_course(self):
		return ProjectCourse()
		
	def create_vm(self):
		return MacVm()
		
		
def get_factory():
	return random.choice([BasicCourseLinuxFactory, ProjectCourseMacFactory])()
	
	
if __name__ == '__main__':
	factory = get_factory()
	course = factory.create_course()
	vm = factory.create_vm()
	print(course.get_labs())
	print(vm.start())
