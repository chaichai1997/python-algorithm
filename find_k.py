# -*- coding: utf-8 -*-
# author = "chaichai"


"""
目标：找出单链表中倒数第k个元素
思路：两个指针，一个比另一个先移动k步，先行指针到None时，满指针指向的节点就是目标节点
"""


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


# 构造一个单链表
def construct_link():
    i = 1
    head = LNode()
    head.next = None
    temp = None
    cur = head
    while i < 8:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = cur.next  # cur = tmp
        i += 1
    return head


# 顺序打印
def print_link(head):
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next


# 找出链表倒数第k个节点
def find_k_node(head, k):
    if head.next is None or head is None:
        return
    else:
        # slow = LNode()
        # fast = LNode()
        slow = head.next
        fast = head.next
        i = 0
        while i < k and fast is not  None:
            fast = fast.next
            i += 1
        if i < k:
            return None
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == '__main__':
    head = construct_link()
    result = None
    print("链表：", end='')
    print_link(head)
    result = find_k_node(head, 3)
    if result is not None:
        print('\n链表的倒数第三个元素：', str(result.data))
