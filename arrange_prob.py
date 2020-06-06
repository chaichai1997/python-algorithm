# -*- coding: utf-8 -*-
# author = "chaichai"


"""
用一个随机函数，生成另一个
"""
import random


def func_1():
    return int(round(random.random()))


def func_2():
    a1 = func_1()
    a2 = func_1()
    if a1 + a2 > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    i = 0
    while i < 16:
        print(func_2(), end=' ')
        i += 1