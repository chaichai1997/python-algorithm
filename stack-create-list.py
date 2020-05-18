# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import LNode
"""
如何实现栈,使其具有压栈、弹栈、取栈顶元素、判断是否为空等
方法1：借助python list结构实现
"""


class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0

    def count(self):
        return len(self.item)

    def top(self):
        if not self.is_empty():
            return self.item[len(self.item)-1]
        else:
            return None

    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
        else:
            print("栈为空")
            return None

    def push(self, item):
        self.item.append(item)


"""
方法二： 借助链表实现
"""


class Stack_2:
    def __init__(self):  # 头节点初始化
        self.data = None
        self.next = None

    def is_empty(self):
        if self.next is not None:
            return True
        else:
            return False

    def count(self):
        size = 0
        p = self.next
        while p is not None:
            size += 1
            p = p.next
        return size

    def push(self, e):
        p = LNode()
        p.data = e
        p.next = self.next
        self.next = p

    def pop(self):
        tmp = self.next
        if tmp is not None:
            self.next = tmp.next
            return tmp.data
        else:
            print("栈为空")
            return None

    def top(self):
        if self.next is not None:
            return self.next.data
        else:
            print("栈为空")
            return None


if __name__ == '__main__':
    s = Stack_2()
    s.push(4)
    print("栈顶元素:", s.top())
    s.pop()
    print("栈元素个数:", s.count())




