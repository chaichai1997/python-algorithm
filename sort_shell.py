# -*- coding: utf-8 -*-
# author = "chaichai"


"""
希尔排序是
把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
"""


def shell_sort(data):
    n = len(data)
    step = 2
    group = n//step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < n:
                k = j - group
                key = data[j]
                while k >= 0:
                    if data[k] > key:
                        data[k + group] = data[k]
                        data[k] = key
                    k -= group
                j += group
        group = group//step
    return data


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    print(shell_sort(lists))