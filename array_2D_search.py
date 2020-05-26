# -*- coding: utf-8 -*-
# author = "chaichai"


"""
实现二维有序数组的高效查找
a[i,j]
if a[i][j]>data, j=j-1
if a[i][j]<data, i = i+1
"""


def search_2D(array, data):
    if array is None:
        return False
    i = 0
    r = len(array)
    c = len(array[0])
    j = c-1
    while i < r and j >= 0:
        if array[i][j] == data:
            return True
        elif array[i][j] >= data:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    array=[
        [1, 2, 3],
        [3, 4, 5],
        [4, 7, 9]
    ]
    data = 9
    print(search_2D(array, data))

