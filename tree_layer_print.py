# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode, array_to_tree
from collections import deque
"""
实现二叉树的层次遍历
"""


def layer_print(root):
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.data, end=' ')
        if p.left is not None:
            queue.append(p.left)
        if p.right is not None:
            queue.append(p.right)


def layer_print_regression(root, level):
    if root is None or level < 0:
        return 0
    elif level == 0:
        print(root.data)
        return 1
    else:
        return layer_print_regression(root.left, level-1) + layer_print_regression(root.right, level - 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
    root = array_to_tree(arr, 0, len(arr)-1)
    print("层次遍历：")
    layer_print(root)
