# -*- coding: utf-8 -*-

class Stack(object):
    """ 栈 """
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit  # 栈容量极限

    def push(self, data):
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量极限')
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')

    def peek(self):
        """ 查看栈顶元素"""
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)


