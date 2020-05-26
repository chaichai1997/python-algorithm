# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求集合的所有自己
"""


def find_child(array, mask, c):
    l = len(array)
    if c == l:
        print('{', end=' ')
        for i in range(l):
            if mask[i] == 1:
                print(array[i], end=' ')
        print('}', end='\n')
    else:
        mask[c] = 1
        find_child(array, mask, c+1)
        mask[c] = 0
        find_child(array, mask, c+1)


if __name__ == '__main__':
    array = [1, 2, 3]
    mask = [0] * len(array)
    find_child(array, mask, 0)