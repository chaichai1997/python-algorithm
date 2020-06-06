# -*- coding: utf-8 -*-
# author = "chaichai"
import random

"""
如何求拿到最多金币的概率
思路： 模拟n次实验
"""


def find_max(n):
    if n < 1:
        print('illegal')
        return
    a = [None] * n
    for i in range(n):
        a[i] = random.uniform(1, n)  # 生成1到n的随机数
    max_a = 0
    i = 0
    if i < 4:
        if a[i] > max_a:
            max_a = a[i]
        i += 1
    for i in range(4, n-1):
        if a[i] > max_a:
            return True
    return False


if __name__ == '__main__':
    count = 10000
    c = 0
    for i in range(count):
        if find_max(10):
            c += 1
    print(c)
    print(c/count)


