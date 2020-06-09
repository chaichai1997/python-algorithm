# -*- coding: utf-8 -*-
# author = "chaichai"


"""
选择排序
基本原理：对于给定的一组记录，第一轮选择最小(大)值，与第一条记录进行交换。
然后从剩余元素中，找出最小(大)值，与第二条记录进行交换，知道记录中未排序元素个数为0.
时间复杂度：O（n * n ）
"""


def sort_search(data):
    n = len(data)
    for i in range(n):
        tmp = i
        for j in range(i+1, n):
            if data[tmp] > data[j]:
                tmp = j
        max = data[tmp]
        data[tmp] = data[i]
        data[i] = max
        print(data)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    sort_search(lists)




