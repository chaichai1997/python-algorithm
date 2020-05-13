# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import print_link, LNode, construct_link

"""
对不带头节点的链表进行反转
"""


def reverse(head):
    if head is None or head.next is None:
        return
    pre = head
    cur = head.next
    pre.next = None
    while cur is not None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


"""
对链表按照固定长度K进行旋转
"""


def rotate_limit(head, k):
    if head is None or head.next is None or k <2:
        return
    i = 1
    pre = head
    begin = head.next
    while begin is not None:
        end = begin
        while i < k:
            if end.next is not None:
                end = end.next
            else:
                return
            i += 1
        p_next = end.next
        end.next = None
        pre.next = reverse(begin)
        begin.next = p_next
        pre = begin
        begin = begin.next
        i = 1


if __name__ == '__main__':
    head = construct_link()
    print("排序前：")
    print_link(head)
    rotate_limit(head, 3)
    print("\n 排序后：")
    print_link(head)