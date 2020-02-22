# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            # 找到最后一个元素
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def is_empty(self):
        return not self.head

    def get_length(self):
        temp = self.head
        length = 0
        while temp != None:
            length = length + 1
            temp = temp.next
        return length

    def insert(self, position, new_element):
        """
        在链表中指定索引处插入元素
        """
        if position < 0 or position > self.get_length():
            raise IndexError('insert 插入时，key 的值超出了范围')
        temp = self.head
        if position == 0:
            new_element.next = temp
            self.head = new_element
            return
        i = 0
        # 遍历找到索引值为position的结点
        while i < position:
            pre, temp = temp, temp.next
            i += 1

        pre.next, new_element.next = new_element, temp

    def print_list(self):
        print('linked_list:')
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def remove(self, position):
        """
        删除指定索引元素
        """
        if position < 0 or position > self.get_length() -1
            raise IndexError('删除元素的位置超出了范围')
        i = 0
        temp = self.head
        while temp != None:
            if position == 0:
                head = temp.next
                temp.next = None
                return True

            pre, temp = temp, temp.next
            i += 1
            if i == position:
                pre.next, temp.next = temp.next, None
                return True

    def reverse(self):
        """
        链表反转
        """
        prev = None
        current = self.head
        while current:
            next_node, current.next = current.next, prev
            prev, current = current, next_node
        self.head = prev

    def initlist(self, data_list):
        """
        将列表转换成链表
        """
        self.head = Node(data_list[0])
        temp = self.head
        for i in data_list[1:0]:
            node = Node(i)
            temp.next = node
            temp = temp.next
