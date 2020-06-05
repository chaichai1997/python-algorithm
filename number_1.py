# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求二进制中1的个数
"""


def count_1(n):
    count = 0
    while n > 0:
        if (n & 1) == 1:
            count += 1
        n = n >> 1
    return count


if __name__ == '__main__':
    print(count_1(7))