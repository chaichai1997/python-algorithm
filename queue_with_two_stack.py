# -*- coding: utf-8 -*-
# author = "chaichai"
from stack_create import Stack

"""
用两个栈实现队列操作
A代表插入栈
B代表弹出栈
"""


class StackQueue:
    def __init__(self):
        self.A = Stack()
        self.B = Stack()

    def push(self, data):
        self.A.push(data)

    def pop(self):
        if self.B.is_empty():
            while not self.A.is_empty():
                self.B.push(self.A.top())
                self.A.pop()
        first = self.B.top()
        self.B.pop()
        return first


if __name__ == '__main__':
    stack = StackQueue()
    stack.push(1)
    stack.push(2)
    print("队列首部元素：", stack.pop())