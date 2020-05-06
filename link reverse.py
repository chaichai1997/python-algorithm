# -*- coding: utf-8 -*-
# author = "chaichai"

"""
实现链表的逆序
主要思路：将链表的指针域指向前一个节点
"""


# 定义一个链表的节点
class LNode:
    def __init__(self):
        self.data = None    # 数据域
        self.next = None    # 指针域


def Reverse(head):
    if head == None or head.next == None:  # 判断列表是否为空
        return
    pre = None   # 前驱节点
    cur = None   # 当前节点
    next = None  # 后继节点




if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next=None

