# -*- coding: utf-8 -*-
# author = "chaichai"


"""
快速排序
采用分治的方法，通过一次排序，将序列切分为两部分，前部分的记录均比后部分的记录小。
然后再按此方法对这两部分数据分别进行快速排序，递归实现。
"""


def sort_quickly(data, left, right):
    if left >= right:
        return data
    key = data[left]
    low = left
    high = right
    while left < right:
        while left < right and data[right] >= key:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= key:
            left += 1
        data[right] = data[left]
    data[right] = key
    sort_quickly(data, low, left-1)
    sort_quickly(data, left+1, high)
    return data


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    print(sort_quickly(lists, 0, len(lists)-1))