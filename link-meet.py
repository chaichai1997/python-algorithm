# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import LNode
"""
判断两个链表是是否存在交点
1 2 3 4
          6 7
2 3 4 5
方法1：Hashset保存其中一个链表的所有地址，遍历另一个链表时查看地址是否与Hashset中一致
方法2：将两个链表首尾相接，判断是否存在环
方法3：判断两个链表尾节点是否一致，然后长链表比短链表先走n1-n2步，相遇时则为交点
"""


def is_meet(head1, head2):
    if head1 is None or head1.next is None or head2 is None or head2.next is None:
        return None
    tmp1 = head1.next
    tmp2 = head2.next
    n1 = 0
    n2 = 0
    while tmp1.next is not None:
        tmp1 = tmp1.next
        n1 += 1
    while tmp2.next is not None:
        tmp2 = tmp2.next
        n2 += 1

    if tmp1 == tmp2:
        if n1 > n2:
            while n1 - n2 > 0:
                head1 = head1.next
                n1 -= 1
        if n1 < n2:
            while n2 - n1 >0:
                head2 = head2.next
                n2 -= 1
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None


if __name__ == '__main__':
    i = 1
    head1 = LNode()
    head2 = LNode()
    head1.next = None
    head2.next = None
    cur = head1
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    cur = head2
    i = 1
    while i<5:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    cur.next = p
    interNode = is_meet(head1,head2)
    if interNode is None:
        print("链表不相交")
    else:
        print("交点为:", interNode.data)