# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何在二位数组中寻找最短路径
"""


"""
方法1：递归
path[i][j] = min{path[i-1][j], path[i][j-1] + arr[i][j]
递归结束条件为： 遍历到arr[0][0]时结束递归
"""


def string_find_path(arr, i, j):
    if arr is None:
        return 0
    elif i == 0 and j == 0:
        return arr[i][j]
    elif i > 0 and j > 0:
        return arr[i][j] + min(string_find_path(arr, i-1, j), string_find_path(arr, i, j-1))
    elif i > 0 and j == 0:
        return arr[i][j] + string_find_path(arr, i-1, j)
    else:
        return arr[i][j] + string_find_path(arr, i, j-1)


"""
方法2：动态规划
path[i][j] = min{path[i-1][j], path[i][j-1] + arr[i][j]
"""


def string_find_path_2(arr, i, j):
    if arr is None:
        return 0
    r = len(arr)
    c = len(arr[0])
    cache = [([None] * c) for i in range(r)]
    cache[0][0] = arr[0][0]
    for i in range(1, r):
        cache[i][0] = cache[i-1][0] + arr[i][0]
    for j in range(1, c):
        cache[0][j] = cache[0][j-1] + arr[0][j]
    # 遍历二位数组，更新path
    for i in range(1, r):
        for j in range(1, c):
            cache[i][j] = min(cache[i-1][j], cache[i][j-1]) + arr[i][j]
    return cache[r-1][c-1]


if __name__ == '__main__':
    arr = [
        [1, 4, 3],
        [8, 7, 5],
        [2, 1, 5]
    ]
    print(string_find_path(arr, len(arr)-1, len(arr[0])-1))
    print(string_find_path_2(arr, len(arr)-1, len(arr[0])-1))
