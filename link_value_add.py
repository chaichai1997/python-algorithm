# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import LNode, print_link


def add(h1, h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1
    c = 0   # 用于记录进位
    p1 = h1.next
    p2 = h2.next
    result_head = LNode()
    result_head.next = None
    p = result_head
    while p1 is not None and p2 is not None:
        tmp = LNode()
        tmp.next = None
        sum = p1.data + p2.data + c
        tmp.data = int(sum % 10)
        c = sum / 10
        p.next = tmp
        p = tmp
        p1 = p1.next
        p2 = p2.next
    if p1 is None:
        while p2 is not None:
            tmp = LNode()
            tmp.next = None
            sum = p2.data + c
            tmp.data = int(sum % 10)
            c = sum / 10
            p.next = tmp
            p = tmp
            p2 = p2.next
    if p2 is None:
        while p1 is not None:
            tmp = LNode()
            tmp.next = None
            sum = p1.data + c
            tmp.data = int(sum % 10)
            c = sum / 10
            p.next = tmp
            p = tmp
            p1 = p1.next

    if c == 1:
        tmp = LNode()
        tmp.next = None
        tmp.data = 1
        p.next = tmp

    return result_head


if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head1.next = None
    head2 = LNode()
    head2.next = None

    cur = head1
    # 构造第一个
    while i < 7:
        tmp = LNode()
        tmp.data = i + 2
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1

    # 构造第一个
    i = 9
    cur = head2
    while i > 4:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i -= 1

    print("\n link1:", end='')
    print_link(head1)

    print("\n link2:", end='')
    print_link(head2)

    add_result = add(head1, head2)
    print("\n after add:", end='')

    print_link(add_result)


