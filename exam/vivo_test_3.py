# -*- coding: utf-8 -*-
# author = "chaichai"

"""
统计手机产量
第一天能生成一台  2，3天生产2台， 4，5，6天生产3台
思路： 计算日期序列和
"""


def solution(n):
    # write code here
    t = []
    i = 1
    sum = 0
    while n > 0:
        if n > i:
            n = n-i
            t.append(i)
            i += 1
        else:
            t.append(n)
            n = 0
    print(t)
    for index, value in enumerate(t):
        sum = sum + (index+1) * value
    return sum


if __name__ == '__main__':
    n = 5
    print(solution(n))
