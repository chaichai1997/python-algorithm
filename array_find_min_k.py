# -*- coding: utf-8 -*-
# author = "chaichai"
"""
在数组array中找出第k小的值
输入： array， low 起始下标、high右边界下标
输出：第k小的值
"""


def find_min_k(array, low, high, k):
    i = low
    j = high
    # 边界初始点
    ref = array[i]
    while i < j:
        # 大于ref位于ref的右边
        while i < j and array[j] >= ref:
            j -= 1
        # 更新子数组右 边界点，该数组都小于ref
        if i < j:
            array[i] = array[j]
            i += 1
        # 小于ref位于ref的左边
        while i < j and array[i] <= ref:
            i += 1
        # 更新子数组的边界点，该数组都小于ref
        if i < j:
            array[j] = array[i]
    array[i] = ref
    sub_index = i - low
    if sub_index == k-1:
        return array[i]
    elif sub_index > k-1:
        return find_min_k(array, low, i-1, k)
    else:
        return find_min_k(array, i+1, high, k-(i-low)-1)


if __name__ == '__main__':
    array = [4, 0, 1, 0, 2, 3]
    k = 3
    print(str(find_min_k(array, 0, len(array)-1, k)))
