# -*- coding:utf-8 -*-
"""
雇员和领导都属于员工，都会实现Worker.work()方法，
只要执行了该方法，就代表了员工开始工作了。
"""
import abc


class Woker(object):
    """
    员工抽象类
    """
    __metaclass__= abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def work(self):
        pass


class Employee(Woker):
    """
    员工类
    """
    __metaclass__ = abc.ABCMeta

    def work(self):
        print('Employ: %s start to work ' % self.name)


class Leader(Woker):
    """
    领导类
    """

    def __init__(self, name):
        self.members = []
        super().__init__(name)

    def add_member(self, employee):
        if employee not in self.members:
            self.members.append(employee)

    def remove_member(self, employee):
        if employee in self.members:
            self.members.remove(employee)

    def work(self):
        print('Leader: %s start to work' % self.name)
        for employee in self.members:
            employee.work()


if __name__ == '__main__':
    employee_1 = Employee('employee_1')
    employee_2 = Employee('employee_2')
    leader_1 = Leader('leader_1')
    leader_1.add_member(employee_1)
    leader_1.add_member(employee_2)

    employee_3 = Employee('employee_3')
    leader_2 = Leader('leader_2')
    leader_2.add_member(employee_3)
    leader_2.add_member(leader_1)

    leader_2.work()

