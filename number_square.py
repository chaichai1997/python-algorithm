# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何在不使用库函数的条件下计算n的平方根
"""


def square(n, e):
    new = n
    last = 1.0
    while new-last > e:
        new = (new + last)/2
        last = n / new
    return new


if __name__ == '__main__':
    n = 50
    e = 0.000001
    print(square(n, e))