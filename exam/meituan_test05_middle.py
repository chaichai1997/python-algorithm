# -*- coding: utf-8 -*-
# author = "chaichai"

"""
找到滑动窗口的中位数
"""


def find_middle(n, k, data):
    result = []
    for i in range(n-k+1):
        list = data[i:k+i]
        list.sort()
        if k % 2 == 1:
            result.append(list[k//2])
        else:
            result.append((list[k//2] + list[k//2-1])/2)
    return result

if __name__ == '__main__':
    n = input().split()
    k = int(n[0])
    n = int(n[1])
    number = input().split()
    data = []
    for i in number:
        data.append(float(i))
    result = find_middle(k, n, data)
    for i in result:
        print(i, end=' ')
