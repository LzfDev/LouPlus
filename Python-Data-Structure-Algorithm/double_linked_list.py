# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    def __init__(self):
        self._head = None


    def is_empty(self):
        return self._head == None

    def get_length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        # 在头部插入元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        # 在尾部插入元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            # 循环移动到链表尾部结点的位置
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        # 在指定位置添加结点
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.appent(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos -1):
                count += 1
                cur = cur.next

            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 首节点的元素即是要删除的元素
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

