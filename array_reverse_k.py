# -*- coding: utf-8 -*-
# author = "chaichai"


"""
对数组进行循环移位
"""


def reverse(array, start, end):
    while start < end:
        tmp = array[start]
        array[start] = array[end]
        array[end] = tmp
        start += 1
        end -= 1


def shift(array, k):
    if array is None:
        print('unreasonable')
        return
    l = len(array)
    reverse(array, l-k, l-1)
    reverse(array, 0, l-k-1)
    reverse(array, 0, l-1)


if __name__ == '__main__':
    k = 2
    arr = [1, 2, 3, 4, 5, 6]
    shift(arr, k)
    print(arr)
