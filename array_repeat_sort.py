# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何对大量重复数字的数组进行排序
"""


"""
使用AVL树
"""


"""
方法2：哈希
"""



def sort_repeat(array):
    data_count = dict()
    for i in array:
        if str(i) in data_count:
            data_count[str(i)] = data_count.get(str(i)) + 1
        else:
            data_count[str(i)] = 1
    index = 0
    for key, value in data_count.items():
        i = value
        while i > 0:
            array[index] = key
            index += 1
            i -= 1


if __name__ == '__main__':
    a = [1,  3, 2, 5, 6, 4, 4, 4, 3, 3]
    sort_repeat(a)
    print(a)