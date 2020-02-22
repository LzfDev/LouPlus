# -*- coding: utf-8 -*-
"""
给定俩个值，这俩个值都在单链表的链点中，
1.交换这两个链点在单链表中的位置
2.不改变其他链点在链表中的位置
思路：
1.找到两个链点的位置D1, D2，和他们的前一个结点位置prevD1，prevD2
2.改变索引位置，完成交换。
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # 遍历链表，依次打印元素
        print('linked_list:')
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def insert(self, data):
        # 在头部插入元素
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def swap_nodes(self, d1, d2):
        prevD1, prevD2 = None, None
        D1, D2 = self.head, self.head
        if d1 == d2:
            return

        # 查找D1,D2结点和前结点prevD1, prevD2
        while D1 is not None and D1.data != d1:
            prevD1 = D1
            D1 = D1.next
        while D2 is not None and D2.data != d2:
            prevD2 = D2
            D2 = D2.next
        # 没有找到D1和D2
        if D1 is None or D2 is None:
            return
        # 头结点的前结点为None
        if prevD1 is not None:
            prevD1.next = D2
        else:
            self.head = D2
        if prevD2 is not None:
            prevD2.next = D1
        else:
            self.head = D1

        temp = D1.next
        D1.next = D2.next
        D2.next = temp


if __name__ == '__main__':
    list = LinkedList()
    list.insert(5)
    list.insert(4)
    list.insert(3)
    list.insert(2)
    list.insert(1)
    list.print_list()
    d1 = int(input('input swap data1:'))
    d2 = int(input('input swap data2:'))
    list.swap_nodes(d1, d2)
    print('After swapping')
    list.print_list()

