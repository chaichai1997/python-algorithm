# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode,array_to_tree
from tree_layer_print import layer_print

"""
对二叉树进行镜像反转、即交换左右子树
"""


def reverse_tree(root):
    if root is None:
        return
    reverse_tree(root.left)
    reverse_tree(root.right)
    tmp = root.left
    root.left = root.right
    root.right = tmp


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = array_to_tree(arr, 0, len(arr)-1)
    print("反转前层次遍历")
    layer_print(root)
    reverse_tree(root)
    print("反转后层次遍历")
    layer_print(root)
