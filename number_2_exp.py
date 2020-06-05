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


"""
与操作
若 n是 2的次方
则 其二进制为 00001000
n-1 00000111
与操作结果为0
"""


def is_power_2(n):
    if n < 1:
        return False
    m = n & (n-1)
    return m == 0


if __name__ == '__main__':
    if is_power(8):
        print("8 is 2's power")
    else:
        print("8 isn't 2's power")
    if is_power(15):
        print("15 is 2's power")
    else:
        print("15 isn't 2's power")
    if is_power_2(8):
        print("8 is 2's power")
    else:
        print("8 isn't 2's power")
    if is_power_2(15):
        print("15 is 2's power")
    else:
        print("15 isn't 2's power")