# -*- coding: utf-8 -*-
# author = "chaichai"
from link_find_k import LNode
"""
基于数组的队列的实现
push：队列尾部加入元素
pop：队列首部弹出元素
"""


class Queue:
    def __init__(self):
        self.item = []
        self.front = 0
        self.end = 0

    def is_empty(self):
        return self.front == self.end

    def size(self):
        return self.end - self.front

    def push(self, e):
        self.item.append(e)
        self.end += 1

    def pop(self):
        if self.end > self.front:
            self.front += 1
        else:
            print("队列为空")

    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.item[self.front]

    def get_end(self):
        if self.is_empty():
            return None
        else:
            return self.item[self.end-1]


"""
链表实现队列
存在两个指针 head， end
"""


class QueueLink:
    def __init__(self):
        self.qhead = None
        self.qend = None

    def is_empyt(self):
        return self.qhead is None

    def size(self):
        size = 0
        p = self.qhead
        while p is not None:
            p = p.next
            size += 1
        return size

    def push(self, e):
        p = LNode()
        p.next = None
        p.data = e
        if self.is_empyt():
            self.qhead = p
            self.qend = p
        else:
            self.qend.next = p
            self.qend = p

    def pop(self):
        if self.is_empyt():
            return None
        else:
            p = self.qhead
            self.qhead = p.next

    def get_front(self):
        if self.is_empyt():
            return None
        else:
            return self.qhead.data

    def get_end(self):
        if self.is_empyt():
            return None
        else:
            return self.qend.data


if __name__ == '__main__':
    # queue = Queue()
    queue = QueueLink()
    queue.push(1)
    queue.push(2)
    queue.push(6)
    print("队列首部元素", queue.get_front())
    print("队列尾部元素", queue.get_end())
    queue.pop()
    print("队列长度", queue.size())