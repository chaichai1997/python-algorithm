# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import array_to_tree, BiNode,print_mid


"""
复制二叉树
"""


def copy(root):
    if root is None:
        return None
    c = BiNode()
    c.data = root.data
    c.left = copy(root.left)
    c.right = copy(root.right)
    return c


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    root = array_to_tree(arr, 0, len(arr)-1)
    back = copy(root)
    print("原二叉树：")
    print_mid(root)
    print("复制得到的数组")
    print_mid(back)
