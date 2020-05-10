# -*- coding: utf-8 -*-
# author = "chaichai"

"""
实现链表的重新排序
原链表：0,1,2, 3, 4, 5，...,n-2,n-1,n
新链表：0,n,1,n-1,...,
要求：
不能申请新的节点
只能修改指针域
"""


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


"""
功能：找出链表的中间节点，将其断为两个子段
输入参数：head
输出：中间节点
"""


def find_middle_node(head):
    if head is None or head.next is None:
        return head
    else:
        fast = head   # 向前两步
        slow = head   # 向前一步
        slow_pre = head  # fast到链表尾部时，slow到链表中部
        while fast is not None and fast.next is not None:
            slow_pre = slow
            slow = slow.next
            fast = fast.next.next
        # 将链表切分为两个
        slow_pre.next = None
        return slow


"""
对不带头节点的单链表进行逆序
输入参数：head 链表头节点
"""


def reverse(head):
    if head is None or head.next is None:
        return head
    else:
        pre = head
        cur = head.next
        pre.next = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


"""
对列表进行排序
输入：head
"""


def re_order(head):
    if head is None or head.next is None:
        return
    else:
        cur1 = head.next
        mid = find_middle_node(head.next)
        cur2 = reverse(mid)
        tmp = None
        while cur1.next is not None:
            tmp = cur1.next
            cur1.next = cur2
            cur1 = tmp

            tmp = cur2.next
            cur2.next = cur1
            cur2 = tmp
        cur1.next = cur2


if __name__ == '__main__':
    i = 1
    head = LNode()
    head.next = None
    tmp = None
    cur = head
    # 构造链表
    while i < 5:
        tmp = LNode()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("排序前：", end='')
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next
    re_order(head)
    print("排序后：", end='')
    cur = head.next
    while cur is not None:
        print(cur.data, end='')
        cur = cur.next





