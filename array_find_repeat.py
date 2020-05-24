# -*- coding: utf-8 -*-
# author = "chaichai"

"""
找到数组中的唯一重复元素
"""


"""
借助字典实现，以空间换时间
"""


def find(array):
    if array is None:
        return -1
    lens = len(array)
    hash_table = dict()
    for i in range(lens):
        hash_table[array[i]] = 0
    j = 0
    for j in range(lens):
        if hash_table[array[j]] == 0:
            hash_table[array[j]] = 1
        else:
            return array[j]
    return -1


"""
异或法
"""


def find_xor(array):
    if array is None:
        return -1
    lens = len(array)
    result = 0
    for i in range(lens):
        result ^= array[i]
    for j in range(lens):
        result ^= j
    return result


"""
数据映射
"""


def find_map(array):
    if array is None:
        return -1
    lens = len(array)
    index = 0
    i = 0
    while True:
        if array[i] >= lens:
            return -1
        if array[index] < 0:
            break
        array[index] *= -1
        index = -1 * array[index]
        if index >= lens:
            print("非法")
            return -1
    return index


if __name__ == '__main__':
    array = [1, 3, 4, 2, 5, 3]
    print(find(array))
    print(find_xor(array))
