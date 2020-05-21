# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode


"""
求一颗二叉树的最大子树和
思路：后序遍历 遍历过程中，如果当前节点与左右子树和小于最大值，则更新最大值
"""


class Test:
    def __init__(self):
        self.max_sums = -2 ** 32

    def tree_find_max_child(self, root, max_root):
        if root is None:
            return 0
        l_max = self.tree_find_max_child(root.left, max_root)
        r_max = self.tree_find_max_child(root.right, max_root)
        sums = l_max + r_max + root.data
        if sums > self.max_sums:
            self.max_sums = sums
            max_root.data = root.data
        return sums   # 返回值为整个树的和

    def construct(self):
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
    test = Test()
    root = test.construct()
    max_root = BiNode()
    sum = test.tree_find_max_child(root, max_root)
    print("最大子树和：", str(test.max_sums) )