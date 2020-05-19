# -*- coding: utf-8 -*-
# author = "chaichai"
from collections import deque


"""
实现LRU：
Least Recently Used  最近最少使用
hash表代表cache
双向链表实现的队列表示内存
当需要访问的页面在内存中，则将该页面移动至页表头。
当需要访问的页面不在内存中，则将该页面加入cache与内存，并将其放入队列头部，若队列已满，则将队列尾部元素删掉后加入当前页面。
"""


class LRU:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()   # 队列
        self.hashset = set()   # hash表

    def is_full(self):   # 判断内存是否已满
        if len(self.queue) == self.cache_size:
            return True

    def in_queue(self, page_num):   # 将页面加入内存与cache
        if self.is_full():
            self.hashset.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(page_num)
        self.hashset.add(page_num)

    def access_page(self, page_num):   # 访问页面，并将该页面移动至队列首部
        if page_num not in self.hashset:   # 当前页面不在cache中，则加入
            self.in_queue(page_num)
        elif page_num != self.queue[0]:   # 当前页面移动至队列首部
            self.queue.remove(page_num)
            self.queue.appendleft(page_num)

    def print_queue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft(), end=' ')


if __name__ == '__main__':
    i = LRU(3)
    i.access_page(1)
    i.access_page(2)
    i.access_page(5)
    i.access_page(1)
    i.access_page(16)
    i.access_page(17)
    i.print_queue()

