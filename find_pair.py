# -*- coding: utf-8 -*-
# author = "chaichai"


"""
给定一个数组,找出数组中是否有两个数对，使得a + b = c + d
"""


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def find_pairs(data):
    sum_pair = dict()
    n = len(data)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            s = data[i] + data[j]
            if s not in sum_pair.keys():
                sum_pair[s] = Pair(data[i], data[j])
            else:     # 字典中已存在和相同的数对
                p = sum_pair[s]
                print('(' + str(p.first) + ',' + str(p.second) + '),' + '(' + str(data[i]) + ',' + str(data[j]) + ')')
                return True
            j += 1
        i += 1
    return False


if __name__ == '__main__':
    data = [3, 4, 7, 10, 20, 9, 8]
    find_pairs(data)