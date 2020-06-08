# -*- coding: utf-8 -*-
# author = "chaichai"


"""
冒泡排序
基本原理：比较相邻的元素，根据比较结果就交换个。 对每一对相邻元素做同样的工作，第一轮比较结果为：第n个元素最大(小)的数。
 针对n-1个元素重复以上的步骤，直到没有任何一对数字需要比较。
"""


def sort_bubble(data):
    n = len(data)
    i = n
    while i >= 1:
        for j in range(i-1):
            if data[j] > data[j+1]:
                tmp = data[j+1]
                data[j+1] = data[j]
                data[j] = tmp
        i -= 1
        print(data)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    sort_bubble(lists)


