# -*- coding: utf-8 -*-
# author = "chaichai"


"""
用 += 操作实现加减乘除
"""


def add(a, b):
    if a < 0 and b < 0:
        print("can't realize")
        return -1
    a += b
    return a


def subtract(a, b):
    if a < b:
        print("can't realize")
        return -1
    count = 0
    while a != b:
        b += 1
        count += 1
    return count


def multiply(a, b):
    if a < 0 or b < 0:
        print("can't realize")
        return -1
    n = b
    s = a
    while n > 1:
        a += s
        n += -1
    return a


def divide(a, b):
    if a < 0 or b < 0:
        print("can't realize")
        return -1
    result = 1
    tmp = 0
    while True:
        tmp = multiply(b, result)
        if tmp <= a:
            result += 1
        else:
            break
    return result-1


if __name__ == '__main__':
    print(add(1, 2))
    print(subtract(3, 1))
    print(multiply(2, 4))
    print(divide(4, 2))

