# -*- coding: utf-8 -*-
# author = "chaichai"

"""
右移多少步找到比当前点大
"""


def find_right(data):
    n = len(data)
    i = 0
    stack = []
    result = [-1] * n
    print(len(result))
    while i < n:
        if (not(len(stack) == 0)) and (data[i] > data[stack[-1]]):
            cur = stack.pop()
            result[cur] = i - cur
        else:
            stack.append(i)
            i += 1

    for i in range(len(result)):
        print(result[i])


if __name__ == '__main__':
    n = input()
    data = []
    for i in range(int(n)):
        data.append(int(input()))
    find_right(data)
