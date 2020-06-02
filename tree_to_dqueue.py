# -*- coding: utf-8 -*-
# author = "chaichai"
from tree_array_transform import BiNode, array_to_tree

"""
将二叉树转换为双向队列
参照中序遍历
"""


class Queue:
    def __init__(self):
        self.p_head = None
        self.p_end = None

    def tree_to_dequeue(self, root):
        if root is None:
            return
        self.tree_to_dequeue(root.left)
        root.left = self.p_end
        if self.p_end is None:
            self.p_head = root
        else:
            self.p_end.right = root
        self.p_end = root
        self.tree_to_dequeue(root.right)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    queue = Queue()
    root = array_to_tree(arr, 0, len(arr)-1)
    queue.tree_to_dequeue(root)
    print("转换后遍历：")
    cur = queue.p_head
    while cur is not None:
        print(cur.data, end=' ')
        cur = cur.right