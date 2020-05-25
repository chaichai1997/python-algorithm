# -*- coding: utf-8 -*-
# author = "chaichai"


"""
找到最小三元组距离
三元组距离为
dis = max(|a[i]-b[j]|, |a[i]-c[k]|, |b[j]-c[k]|)
"""


"""
法一：蛮力法
"""


def find_min_tripe(a, b, c):
    min_dis = max(abs(a[0]-b[0]), abs(a[0]-c[0]), abs(b[0]-c[0]))
    for i in a:
        for j in b:
            for k in c:
                dist = max(abs(i-j), abs(i-k), abs(j-k))
                if dist < min_dis:
                    min_dis = dist
    return min_dis


"""
最小距离法 结合数组升序特性
当且仅当三元组中最小值增大时，三元组距离减小
"""


def find_min_distance(a, b, c):
    i = 0
    j = 0
    k = 0
    min_dist = 2 ** 32
    while True:
        dis = max(abs(a[i]-b[j]), abs(a[i]-c[k]), abs(b[j]-c[k]))
        if dis < min_dist:
            min_dist = dis
        min_p = min(a[i], b[j], c[k])
        if min_p == a[i]:
            i += 1
            if i >= len(a):
                break
        if min_p == b[j]:
            j += 1
            if j >= len(b):
                break
        if min_p == c[k]:
            k += 1
            if k >= len(c):
                break
    return min_dist


if __name__ == '__main__':
    a = [3, 4, 5, 7, 15]
    b = [10, 12, 14, 16, 17]
    c = [20, 21, 23, 24, 37, 30]
    print(find_min_tripe(a, b, c))
    print(find_min_distance(a, b, c))
