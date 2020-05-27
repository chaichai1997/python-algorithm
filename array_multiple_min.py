# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何获取最好的矩阵链相乘方法
eg  [40, 20, 30, 10, 30]
  表示四个矩阵：
  a 40 * 20
  b 20 * 30
  c 30 * 10
  d 10 * 30
  最好乘法 (a(bc))d
"""


"""
方法一：递归法
"""


def matrix_chain(p, i, j):
    if i == j:
        return 0
    mins = 2 ** 32
    k = i
    while k < j:
        count = matrix_chain(p, i, k) + matrix_chain(p, k+1, j) + p[i-1] * p[k] * p[j]
        if count < mins:
            mins = count
        k += 1
    return mins


"""
动态规划方法
"""


def matrix_chain_order(p, n):
    cost = [([None]*n) for i in range(n)]
    i = 1
    while i < n:
        cost[i][i] == 0
        i += 1
    c = 2
    while c < n:
        i = 1
        while i < n-c + 1:
            j = i + c - 1
            cost[i][j] = 2**32
            k = i
            while k <= j-1:
                q = cost[i][k] + cost[k+1][j] + p[i-1] * p[k] * p[j]
                if q < cost[i][j]:
                    cost[i][j] = q
                k += 1
            i += 1
        c += 1
    return cost[1][n-1]


if __name__ == '__main__':
    array = [40, 20, 30, 10, 30]
    print(matrix_chain(array, 1, len(array)-1))
    print(matrix_chain_order(array, len(array)))

