# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import construct_link
from link_find_k import print_link


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def rotate_k(head, k):
    if head.next is None or head is None:
        return
    else:
        fast = head.next
        slow = head.next
        i = 0
        while i < k and fast is not None:
            fast = fast.next
            i += 1
        if i < k:
            return
        else:
            while fast.next is not None:
                slow = slow.next
                fast = fast.next
            tmp = slow
            slow = slow.next
            tmp.next = None
            fast.next = head.next
            head.next = slow


if __name__ == '__main__':
    head = construct_link()
    print("未旋转链表：", end='')
    print_link(head)
    rotate_k(head, 3)
    print("旋转后：", end='')
    print_link(head)
