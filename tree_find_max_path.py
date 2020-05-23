# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode, array_to_tree


"""
在二叉树种找出路径最大的和
思路：
假设以root为起点，所有路径已遍历，已知最大路径为max
已root.left为起点，叶子节点为中，最大路径为max_left
已root.right 为起点，叶子节点为中，最大路径为max_right
tmp = max(root.val + max_left, root.val + max_right,  root.val + max_right + max_left) 与max比较，并更新
"""


class Inf:
    def __init__(self):
        self.val = None


"""
寻找最长路径
"""


def find_max_path(root, maxs):
    if root is None:
        return 0
    sum_left = find_max_path(root.left, maxs)
    sum_right = find_max_path(root.right, maxs)
    tmp = max(sum_left + root.data, sum_right + root.data, sum_right + sum_left + root.data)
    maxs.val = max(tmp, maxs.val)
    sub_max = sum_left if sum_left > sum_right else sum_right
    return root.data + sub_max


def find(root):
    maxs = Inf()
    maxs.val = -2 ** 30
    find_max_path(root, maxs)
    return maxs.val


if __name__ == '__main__':
    arr = [2, 3, 5]
    root = array_to_tree(arr, 0, len(arr)-1)
    print(find(root))
