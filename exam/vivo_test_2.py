# -*- coding: utf-8 -*-
# author = "chaichai"

"""
计算m的数位之积等于n的数
例如： n = 36
      m = 49
思路：累除法
"""


def solution(n):
    s = []
    # while n > 1:
    i = 9
    while i > 1:
        if n % i == 0:
            n = n / i
            s.append(i)
            i = 9
        else:
            i -= 1
    sum = 0
    for i in range(len(s)):
        sum = sum +s[i] * 10 ** i
    if n != 1:
        return -1
    else:
        return sum
