# -*- coding: utf-8 -*-
# author = "chaichai"

"""
实现链表的逆序
"""


# 定义一个链表的节点
class LNode:
    def __init__(self):
        self.data = None  # 数据域
        self.next = None  # 指针域


"""
主要思路：将链表的指针域指向前一个节点
input： head 头节点
"""


def reverse(head):
    if head == None or head.next == None:  # 判断列表是否为空
        return
    pre = None  # 前驱节点
    cur = None  # 当前节点
    next = None  # 后继节点

    # 将列表首节点变为尾节点
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next

    # 当前遍历的节点cur指向前驱节点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    # 链表的头节点指向倒数第二个节点
    cur.next = pre
    # 链表的头节点指向原链表的尾节点
    head.next = cur


"""
 使用递归法实现逆序
"""


def recursive_reverse(head):
    if head is None or head.next is None:  # 如果链表中只有一个元素
        return head
    else:
        new_head = recursive_reverse(head.next)
        head.next.next = head
        head.next = None
    return new_head


def reverse_2(head):
    if head is None:
        return
    else:
        frist_node = head.next
        new_head = recursive_reverse(frist_node)
        head.next = new_head
        return new_head


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print('逆序前链表：', end='')
    cur = head.next
    while cur != None:
        print(cur.data, end='')
        cur = cur.next

    print('\n逆序后链表：', end='')
    # Reverse(head)
    reverse_2(head)
    cur = head.next
    while cur != None:
        print(cur.data, end='')
        cur = cur.next

