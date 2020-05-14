# -*- coding: utf-8 -*-
# author = "chaichai"

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


if __name__ == '__main__':
    s = Stack()
    s.push(4)
    print("栈顶元素:", s.top())
    print("栈元素个数:", s.count())
    print("栈元素个数:", s.count())




