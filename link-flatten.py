# -*- coding: utf-8 -*-
# author = "chaichai"


class LNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None


class MergeList:
    def __init__(self):
        self.head = None

    # 合并两个有序链表
    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data > b.data:
            result = b
            result.down = self.merge(a, b.down)

        else:
            result = a
            result.down = self.merge(a.down, b)
        return result

    # 将链表扁平化处理
    def flatten(self, root):
        if root is None or root.right is None:
            return root
        root.right = self.flatten(root.right)
        root = self.merge(root, root.right)
        return root

    # 把data拆入链表头
    def insert(self, head_ref, data):
        node = LNode(data)
        node.down = head_ref
        head_ref = node
        return head_ref

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.down


if __name__ == '__main__':
    L = MergeList()
    L.head = L.insert(L.head, 31)
    L.head = L.insert(L.head, 8)
    L.head = L.insert(L.head, 6)
    L.head = L.insert(L.head, 3)
    L.head.right = L.insert(L.head.right, 21)
    L.head.right = L.insert(L.head.right, 11)
    L.head.right.right = L.insert(L.head.right.right, 50)
    L.head.right.right = L.insert(L.head.right.right, 22)
    L.head.right.right = L.insert(L.head.right.right, 15)
    L.head.right.right.right = L.insert(L.head.right.right.right, 55)
    L.head.right.right.right = L.insert(L.head.right.right.right, 40)
    L.head.right.right.right = L.insert(L.head.right.right.right, 39)
    L.head.right.right.right = L.insert(L.head.right.right.right, 30)

    L.head = L.flatten(L.head)
    L.print_list()


