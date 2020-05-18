# -*- coding: utf-8 -*-
# author = "chaichai"
from stack_create import Stack

"""
根据入栈顺序判断可能存在的出栈顺序
"""


def pop_series(push, pop):
    if push is None or pop is None:
        return False
    push_len = len(push)
    pop_len = len(pop)
    if push_len != pop_len:
        return False
    push_index = 0
    pop_index = 0
    stack = Stack()
    while push_index < push_len:
        stack.push(push[push_index])
        push_index += 1
        # 栈顶元素出栈
        while(not stack.is_empty()) and stack.top() == pop[pop_index]:
            stack.pop()
            pop_index += 1
    return stack.is_empty() and pop_index == pop_len


if __name__ == '__main__':
    push = "12345"
    pop = "32541"
    if pop_series(push, pop):
        print(pop + " is " + push + ' series')
    else:
        print(pop + " isn't " + push + ' series')


