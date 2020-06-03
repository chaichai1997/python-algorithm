# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求一个串中出现的第一个最长重复子串
"""


"""
传统方法
"""


def find_child(strs, start, length, child):
    l_s = len(strs)
    child.append(strs[start:start + length])
    if length == l_s:
        return child
    if start + length >= l_s:
        find_child(strs, 0, length+1, child)
    elif start + length < l_s:
        find_child(strs, start+1, length, child)


def find_repeat_child(child):
    max_count = 0
    max_child = None
    l_c = len(child)
    for i in range(l_c):
        for j in range(l_c):
            if child[i] == child[j] and i != j:
                if len(child[i]) > max_count:
                    max_child = child[i]
                    max_count = len(child[i])
    return max_child


"""
后缀数组法
"""
if __name__ == '__main__':
    strs = 'banana'
    dst = []
    find_child(strs, 0, 1, dst)
    max = find_repeat_child(dst)
    print(max)