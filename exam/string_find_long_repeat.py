# -*- coding: utf-8 -*-
# author = "chaichai"

"""
寻找字符串的最长重复子串
重复子串， 首尾相接
123123  输出 6
"""


"""
方法1：寻找子序列后判断
"""

#
# def find_child(strs, start, length, child):
#     l_s = len(strs)
#     child.append(strs[start:start + length])
#     if length == l_s:
#         return child
#     if start + length >= l_s:
#         find_child(strs, 0, length+1, child)
#     elif start + length < l_s:
#         find_child(strs, start+1, length, child)
#
#
# def find_repeat_child(child):
#     for i in child:
#         print(i)
#         n = len(i)
#         if n > 2 and n % 2 == 0:
#             if i[:n//2] == i[n//2:]:
#                 return n
#

"""
切割后判断
"""


def find_repeat(strs):
    n = len(strs)
    max_len = 0
    for i in range(n):
        for j in range(i+1, n):
            dst = strs[i:j+1]
            l = len(dst)
            if l > 2 and l % 2 == 0:
                if dst[:l//2] == dst[l//2:]:
                    max_len = max(max_len, l)
    return max_len


"""
队列实现
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


def find(strs):
    n = len(strs)
    queue = Queue()
    count = 0
    max_count = 0
    same = []
    for i in range(n):
        if queue.is_empty():
            queue.push(strs[i])
            max_count = max(max_count, count)
            count = 0
            same = []
        elif queue.get_front() == strs[i]:
            queue.pop()
            count += 2
            same.append(strs[i])
        elif queue.get_front() != strs[i]:
            queue.push(strs[i])
            max_count = max(max_count, count)
            count = 0
            same = []
        print(same)
    max_count = max(max_count, count)
    return max_count


if __name__ == '__main__':
    strs = input()
    # print(find(strs))
    print(find_repeat(strs))

