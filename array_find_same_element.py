# -*- coding: utf-8 -*-
# author = "chaichai"

"""
找出三个有序数组的公共元素
思路1：
先找a and b ，然后再and c
思路二：
动态规划if a = b = c 公共点
if a < b a++
if b < c b++
else  c++
"""


def find_common(a, b, c):
    l_a = len(a)
    l_b = len(b)
    l_c = len(c)
    i = 0
    j = 0
    k = 0
    while i < l_a and j < l_b and k < l_c:
        if a[i] == b[j] == c[k]:
            print(a[i], end=' ')
            i += 1
            k += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1


if __name__ == '__main__':
    a = [2, 5, 12, 20, 45, 85]
    b = [16, 19, 20, 85]
    c = [3, 4, 15, 20, 39, 72, 85]
    find_common(a, b, c)