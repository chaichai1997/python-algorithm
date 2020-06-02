# -*- coding: utf-8 -*-
# author = "chaichai"


"""
消除字符串内的内嵌括号
"""


def remove_bracket(string):
    if string is None:
        return
    b_num = 0
    if list(string)[0] != '(' or list(string)[-1] != ')':
        return None
    sb = '('
    i = 1
    while i < len(string)-1:
        ch = list(string)[i]
        if ch == '(':
            b_num += 1
        elif ch == ')':
            b_num -= 1
        else:
            sb = sb + list(string)[i]
        i += 1
    if b_num != 0:
        print("不匹配")
        return None
    sb = sb + ')'
    return sb


if __name__ == '__main__':
    str_1 = "(1, (2, 3), (4, (5, 6), 7))"
    print(remove_bracket(str_1))