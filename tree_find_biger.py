# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import array_to_tree, BiNode


"""
在二叉排序树种找出第一个大于中间值的节点
f = (min + max)//2
找到离f最近、大于f的节点
思路：先找到最大值于最小值，左下角为最小，右下角为最大,然后对二叉树进行遍历
"""


"""
function：找到最小点
"""


def find_min(root):
    if root is None:
        return
    while root.left is not None:
        root = root.left
    return root


"""
function：找到最大点
"""


def find_max(root):
    if root is None:
        return
    while root.right is not None:
        root = root.right
    return root


"""
找到接近目标点且大于该点的节点
"""


def get_node(root):
    max_node = find_max(root)
    min_node = find_min(root)
    mid = (max_node.data + min_node.data) // 2
    while root is not None:
        if root.data > mid:
            result = root
            root = root.left
        else:
            root = root.right
    return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = array_to_tree(arr, 0, len(arr)-1)
    dst = get_node(root)
    print(dst.data)


