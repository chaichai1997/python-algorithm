# -*- coding: utf-8 -*-
# author = "chaichai"


"""
判断一个数是否为2的n次方
"""


"""
method 1：
Construction
"""


def is_power(n):
    if n < 1:
        return False
    i = 1
    while i <= n:
        if i == n:
            return True
        i *= 2
    return False


if __name__ == '__main__':
    if is_power(8):
        print("8 is 2's power")
    else:
        print("8 isn't 2's power")
    if is_power(15):
        print("15 is 2's power")
    else:
        print("15 isn't 2's power")