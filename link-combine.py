# -*- coding: utf-8 -*-
# author = "chaichai"

from link_find_k import LNode, print_link


def constract_link(start):
    i = start
    head = LNode()
    head.next = None
    cur = head
    while i < 7:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 2
    return head


"""
函数功能，合并两个链表
输入:head1,head2两个单链表
输出：合并链表
"""


def merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next
    cur2 = head2.next
    if cur1.data > cur2.data:
        head = head2
        cur = cur2
        cur2 = cur2.next
    else:
        head = head1
        cur = cur1
        cur1 = cur1.next
    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    if cur1 is not None:
        cur.next = cur1
    if cur2 is not None:
        cur.next = cur2
    return head


if __name__ == '__main__':
    head1 = constract_link(1)
    head2 = constract_link(2)
    print("链表1：")
    print_link(head1)
    print("\n 链表2：")
    print_link(head2)
    print("\n 合并后链表")
    head = merge(head1, head2)
    print_link(head)