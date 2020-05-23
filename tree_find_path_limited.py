# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode
from tree_is_equal import construct


"""
找到满足目标整数的序列
思路：采用先序遍历，并计算当前路径值，到叶子节点后于目标整数比较
"""


"""
function:打印满足目标的路径
input： root 根节点 num 目标整数 sums：当前路径和 v:存储路径
"""


def find_path(root, num, sums, v):
    sums += root.data
    v.append(root.data)
    if root.left is None and root.right is None and sums == num:
        print(v)
    if root.left is not None:
        find_path(root.left, num, sums, v)
    if root.right is not None:
        find_path(root.right, num, sums, v)
    sums = sums - v[-1]
    v.remove(v[-1])


if __name__ == '__main__':
    root = construct()
    s = []
    print("满足条件的点：")
    find_path(root, 8, 0, s)




