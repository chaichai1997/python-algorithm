# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode
from tree_find_max_child import Test


"""
判断两个二叉树是否相等 ：
结构相等，相同位置的值也相等
"""


def tree_is_equal(root1, root2):
    if root1 is None and root2 is not None:
        return False
    elif root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is None:
        return False
    elif root1.data == root2.data:
        return tree_is_equal(root1.left, root2.left) and tree_is_equal(root1.right, root2.right)
    else:
        return False


def construct():
    root = BiNode()
    node1 = BiNode()
    node2 = BiNode()
    node3 = BiNode()
    node4 = BiNode()
    root.data = 6
    node1.data = 3
    node2.data = -7
    node3.data = -1
    node4.data = 9
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node2.right = node3.left = node3.right = node4.right = node4.left = None
    return root


if __name__ == '__main__':
    root1 = construct()
    root2 = construct()
    equal = tree_is_equal(root1, root2)
    if equal:
        print("两棵树相等")
    else:
        print("两棵树不相等")
