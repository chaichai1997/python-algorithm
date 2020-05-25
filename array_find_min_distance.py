# -*- coding: utf-8 -*-
# author = "chaichai"

"""
求数组中两个元素的最小距离
"""

"""
方法一：蛮力法
"""


def find_distance(array, a, b):
    list_a = []
    list_b = []
    for i, v in enumerate(array):
        if v == a:
            list_a.append(i)
        if v == b:
            list_b.append(i)
    dis = 2 ** 32
    for i in list_a:
        for j in list_b:
            d = abs(j - i)
            if d < dis:
               dis = d
    return dis


"""
方法二： 动态规划
"""


def find_min_distance(array, num1, num2):
    l = len(array)
    if array is None and l < 1:
        print("非法")
        return
    p_1 = -1
    p_2 = -1
    dis = 2 ** 32
    for i, v in enumerate(array):
        if v == num1:
            p_1 = i
            if p_2 >= 0:
                dis = min(dis, p_1-p_2)

        if v == num2:
            p_2 = i
            if p_1 >= 0:
                dis = min(dis, p_2-p_1)
    return dis


if __name__ == '__main__':
    array = [4, 6, 7, 4, 7, 4, 6, 4, 7, 8, 5, 6, 4, 3, 10, 8]
    num1 = 4
    num2 = 8
    print(find_distance(array, num1, num2))
    print(find_min_distance(array, num1, num2))
