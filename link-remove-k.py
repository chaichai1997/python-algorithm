# -*- coding: utf-8 -*-
# author = "chaichai"

"""
在只给定某个节点指针的情况下 删除该节点
"""

from link_find_k import LNode,  print_link


"""
方法功能：在给定单个节点指针的情况下，删除该节点
"""


def remove_node(p):
    if p.next is None or p is None:
        return False
    p.data = p.next.data
    p.next = p.next.next
    return True


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    p = None
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i == 5:
            p = tmp
        i += 1
    print_link(head)
    result = remove_node(p)
    if result:
        print("删除后：")
        print_link(head)

