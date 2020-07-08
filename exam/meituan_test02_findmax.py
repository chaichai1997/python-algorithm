# -*- coding: utf-8 -*-
# author = "chaichai"

"""
找到最大的山峰元素
"""


def find_max(data):
    data.insert(0, float('-inf'))
    data.append(float('-inf'))
    n = len(data)
    big = []
    for i in range(1, n-1):
        if data[i] >= data[i-1] and data[i] >= data[i+1]:
            big.append(i-1)
    return big


if __name__ == '__main__':
    s = input()
    data = s.split()
    n = len(data)
    if n > 100000:
        print("")
    else:
        for i in range(len(data)):
            data[i] = int(data[i])
        result = find_max(data)
        print(result[-1])
