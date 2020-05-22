# -*- coding: utf-8 -*-
# author = "chaichai"


"""
判断一个数组是否为二叉搜索树的后序序列
二叉搜索树：左子树上所有节点的值都小于节点值
           右子树上所有节点值都大于节点值
思路:数组最后一个元素为根节点，大于该元素的为右子树、小于该元素的为左子树，递归
"""


def is_tree_after(arr, start, end):
    if arr is None:
        return False
    root = arr[end]
    i = start
    # 找到第一个大于root的值，前面的所有节点都位于左子树
    while i < end:
        if arr[i] > root:
            break
        i += 1
    j = i
    # 从i开始的所有节点都大于root
    while j < end:
        if arr[j] < root:
            return False
        j += 1
    left_is_order = True
    right_is_order = True
    if i > start:
        left_is_order = is_tree_after(arr, start, i-1)
    if j < end:
        right_is_order = is_tree_after(arr, i, end)
    return left_is_order and right_is_order


if __name__ == '__main__':
    arr = [1, 3, 2, 5, 7, 6, 4]
    result = is_tree_after(arr, 0, len(arr)-1)
    print(arr, end= ' ')
    if result:
        print("是某一二元查找树的后序遍历序列")
    else:
        print("不是某一二元查找树的后序遍历序列")