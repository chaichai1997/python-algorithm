# -*- coding: utf-8 -*-
# author = "chaichai"
from collections import deque

"""
设计一个排序系统，让每个进入队伍的用户都能看到自己的位置及变换，任何用户都可以随时加入与退出
"""


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def get_name(self):
        return self.name

    def get_seq(self):
        return self.seq

    def set_seq(self, seq):
        self.seq = seq

    def get_id(self):
        return self.id

    def introduction(self):
        return "id: " + str(self.get_id()) + " name: " + self.get_name() + ' seq: ' + str(self.get_seq())


class QueueSort:
    def __init__(self):
        self.squeue = deque()

    def in_queue(self, user):
        user.set_seq(len(self.squeue)+1)
        self.squeue.append(user)

    def out_queue(self):
        self.squeue.popleft()
        self.update()

    def random_out(self, user):
        self.squeue.remove(user)
        self.update()

    def update(self):
        i = 1
        for user in self.squeue:
            user.set_seq(i)
            i += 1

    def print_queue(self):
        for user in self.squeue:
            print(user.introduction())


if __name__ == '__main__':
    user1 = User(1, "user1")
    user2 = User(2, "user2")
    user3 = User(3, "user3")
    user4 = User(4, "user4")
    queue = QueueSort()
    queue.in_queue(user1)
    queue.in_queue(user2)
    queue.in_queue(user3)
    queue.in_queue(user4)
    queue.out_queue()
    queue.random_out(user3)
    queue.in_queue(user1)
    queue.print_queue()