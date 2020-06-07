# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何判断还有几盏灯亮着
第一次全部打开，第二次每隔一个灯泡关掉一个，第三次每个两个灯泡，按一次开关，即将开着的灯关掉，关着的等打开。
思路：100个数字中约数个数是奇数的灯亮着
"""


def factors_is_odd(a):
    total = 0
    i = 1
    while i <= a:
        if a % i == 0:
            total += 1
        i += 1
    if total % 2 == 1:
        return 1
    else:
        return 0


def total_count(num, n):
    count = 0
    i = 0
    while i < n:
        if factors_is_odd(num[i]) == 1:
            print(num[i])
            count += 1
        i += 1
    return count


if __name__ == '__main__':
    num = [None] * 100
    i = 0
    while i < 100:
        num[i] = i + 1
        i += 1
    count = total_count(num, 100)
    print(count)