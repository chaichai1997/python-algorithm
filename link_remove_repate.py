# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import print_link


"""
删除链重复项
"""


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


"""
双重循环实现
"""
def remove_repeate(head):
    if head is None or head.next is None:
        return
    outer_cur = head.next
    while outer_cur is not None:
        inner_cur = outer_cur.next
        inner_pre = outer_cur
        while inner_cur is not None:
            if outer_cur.data == inner_cur.data:
                inner_pre.next = inner_cur.next
                inner_cur = inner_cur.next
            else:
                inner_pre = inner_cur
                inner_cur = inner_cur.next
        outer_cur = outer_cur.next


"""
递归实现
"""


def remove_repeat_recurisive(head):
    if head.next is None:
        return
    cur = head
    head.next = remove_repeat_recurisive(head.next)
    pointer = head.next
    while pointer is not None:
        if head.data == pointer.data:
            cur.next = pointer.next
            pointer = cur.next
        else:
            pointer = pointer.next
            cur = cur.next
    return head


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.data = None
    head.next = None
    cur = head
    while i < 7:
        tmp = LNode()
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("未处理前：", end='')
    print_link(head)
    remove_repeate(head)
    # remove_repeat_recurisive(head)
    print("处理后：", end='')
    print_link(head)
