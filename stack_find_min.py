# -*- coding: utf-8 -*-
# author = "chaichai"
from stack_create import Stack


"""
用时间复杂度为o(1)的算法求栈中最小元素
思路：以空间换时间。两个栈，一个用于存储数据，一个用于存储最小值
"""


class StackMin:
    def __init__(self):
        self.elem = Stack()  # 用于存储栈中元素
        self.min = Stack()  # 用于存储栈中最小值

    def push(self, data):
        self.elem.push(data)
        if self.min.is_empty():
            self.min.push(data)
        else:
            if data < self.min.top():
                self.min.push(data)

    def pop(self):
        if self.elem.is_empty():
            return None
        top = self.elem.top()
        self.elem.pop()
        if top == self.min.top():
            self.min.pop()
        return top

    def small(self):
        if self.min.is_empty():
            return None
        else:
            return self.min.top()


if __name__ == '__main__':
    s = StackMin()
    s.push(5)
    print("最小值：", s.small())
    s.push(6)
    print("最小值：", s.small())
    s.push(3)
    print("最小值：", s.small())