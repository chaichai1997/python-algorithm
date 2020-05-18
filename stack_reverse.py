# -*- coding: utf-8 -*-
# author = "chaichai"
from stack_create import Stack

"""
实现栈中元素的翻转
"""


"""
把栈底元素移动到栈顶
参数：栈的引用
"""


def move_bottom_to_top(s):
    if s.is_empty():
        return
    top1 = s.top()
    s.pop()   # 弹出栈顶元素
    if not s.is_empty():
        move_bottom_to_top(s)   # 递归处理不包含栈顶元素的子栈
        top2 = s.top()
        s.pop()
        # 交换栈顶与子栈栈顶元素
        s.push(top1)
        s.push(top2)
    else:
        s.push(top1)


"""
翻转栈内元素
"""


def stack_reverse(s):
    if s.is_empty():
        return
    move_bottom_to_top(s)
    top = s.top()
    s.pop()
    stack_reverse(s)
    s.push(top)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    stack_reverse(s)
    print("反转后：")
    while not s.is_empty():
        print(s.top())
        s.pop()