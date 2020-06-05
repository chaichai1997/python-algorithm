# -*- coding: utf-8 -*-
# author = "chaichai"


from math import sqrt


"""
方法一：调用库函数
"""


def is_sqrt(n):
    if isinstance(sqrt(n), int):
        return sqrt(n)
    else:
        print("can't sqrt")


"""
方法二：直接计算
时间复杂度：O(sqrt(n))
"""


def is_sqrt_2(n):
    if n <= 0:
        print("not natural number")
        return False
    i = 0
    while i * i <= n:
        if i * i == n:
            print("can sqrt")
            return True
        i += 1
    print("can't sqrt")
    return False


"""
方法二：二分查找法
时间复杂度： O(log n)
"""


def find_sqrt(n):
    low = 1
    high = n
    while low < high:
        mid = (low+high)//2
        s = mid * mid
        if s < n:
            low = mid + 1
        elif s > n:
            high = mid - 1
        else:
            print("can sqrt")
            return True
    print("can't sqrt")
    return False


if __name__ == '__main__':
    n1 = 15
    n2 = 16
    is_sqrt_2(n1)
    is_sqrt_2(n2)
    find_sqrt(n1)
    find_sqrt(n2)



