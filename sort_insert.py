# -*- coding: utf-8 -*-
# author = "chaichai"


"""
插入排序
将一个记录插入到已经排好序的有序表中，从而一个新的、记录数增1的有序表.
"""


def sort_insert(data):
    n = len(data)
    for i in range(1, n):
        tmp = data[i]
        j = i - 1
        while j >= 0:
            if data[j] > tmp:
                data[j+1] = data[j]
                data[j] = tmp
            j -= 1
        print(data)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    sort_insert(lists)