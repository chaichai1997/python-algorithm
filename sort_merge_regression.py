# -*- coding: utf-8 -*-
# author = "chaichai"


"""
递归排序
利用分治思想将数字序列划分，，对子表进行排序，然后利用递归操作合并子表。
"""


def merge(left, right):
    l_l = len(left)
    l_r = len(right)
    i = 0
    j = 0
    result = []
    while i < l_l and j < l_r:
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    result += left[i:]
    result += right[j:]
    print(result)
    return result


def merge_sort(data):
    n = len(data)
    if n <= 1:
        return data
    num = n // 2
    left = merge_sort(data[:num])
    right = merge_sort(data[num:])
    return merge(left, right)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    merge_sort(lists)

