# -*- coding: utf-8 -*-
# author = "chaichai"


"""
把一个有序整数数组放到二叉树中
"""


class BiNode:
    def __init__(self):
        self.data = None
        self.right = None
        self.left = None


# 将有序数组转换为二叉树
def array_to_tree(array, start, end):
    if end >= start:
        root = BiNode()
        mid = (start + end + 1) // 2
        root.data = array[mid]
        print(mid)
        root.left = array_to_tree(array, start, mid - 1)
        root.right = array_to_tree(array, mid + 1, end)
    else:
        root = None
    return root


# 二叉树中序遍历
def print_mid(root):
    if root is None:
        return
    if root.left is not None:
        print_mid(root.left)
    print(root.data, end=' ')
    if root.right is not None:
        print_mid(root.right)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    print(array)
    root = array_to_tree(array, 0, len(array)-1)
    print("转化为树后中序遍历为：")
    print_mid(root)


