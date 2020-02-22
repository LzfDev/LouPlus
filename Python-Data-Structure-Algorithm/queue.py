# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next


class Queue(object):
    """ 链表实现队列 """
    def __init__(self):
        self.head = None
        self.rear = None  # 尾部链点

    def is_empty(self):
        return self.head is None

    def enqueue(self, elem):
        # 入队
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p

        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):
        # 出队
        if self.is_empty():
            print('Queue_is_empty')
        else:
            result = self.head.elem
            self.head = self.head.next
            return result

    def peak(self):
        # 返回队头元素
        if self.is_empty():
            print('NOT_FOUND')
        else:
            return self.head.elem

    def print_queue(self):
        print('queue:')
        temp = self.head
        myqueue = []
        while temp is not None:
            myqueue.append(temp.elem)
            temp = temp.next
        print(myqueue)


