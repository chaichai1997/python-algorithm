# -*- coding: utf-8 -*-
# author = "chaichai"
from  link_find_k import print_link, LNode


def construct_link():
    i = 1
    head = LNode()
    head.next = None
    cur = head
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = head.next.next.next   # 构造一个有环链表
    return head


"""
判断链表是否有环
输入：head
输出：None：无环  或 返回 fast与slow相遇节点
"""


def if_loop(head):
    if head is None or head.next is None:
        return
    else:
        slow = head.next
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow.data == fast.data:
                return slow


"""
找到环的入口点
输入： head 相遇点
输出: 入口点
"""


def find_loop_node(head, meet):
    first = head.next
    while first != meet:
        first = first.next
        meet = meet.next
    return first


if __name__ == '__main__':
    head = construct_link()
    meet = if_loop(head)
    if meet is not None:
        print('该链表有环')
        loop_node = find_loop_node(head, meet)
        print("链表入口：", loop_node.data)
    else:
        print('该链表无环')