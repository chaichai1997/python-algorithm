# -*- coding: utf-8 -*-
# author = "chaichai"


"""
堆排序：
将目标数据转换为顺序存储的二叉树，将堆的最后一个元素与二叉树根节点交换，
后计算n-1 个
"""


def adjust(lists, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    maxs = i
    if i < size /2:
        if l < size and lists[l] > lists[maxs]:
            maxs = l
        if r < size and lists[r] > lists[maxs]:
            maxs = r
        if maxs != i:
            lists[maxs], lists[i] = lists[i], lists[maxs]
            adjust(lists, maxs, size)


def build_heap(lists, size):
    for i in range(0, size//2)[::-1]:
        adjust(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust(lists, 0, i)


if __name__ == '__main__':
    lists = [3, 4, 2, 8, 9, 5, 1]
    heap_sort(lists)