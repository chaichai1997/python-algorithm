# -*- coding: utf-8 -*-
# author = "chaichai"


"""
手机解锁图案问题，至少链接【m,n]个键
解锁图案中所有键不同
若当前连线经过某一点，则该点必须选中
"""


class Solution:
    def __init__(self):
        self.count = 0

    def search(self, a, i, j, c, m, n):
        if c >= m:
            self.count += 1
        if c >= n:
            return
        # 一个点走向周围包含24种情况,构成5 * 5 矩阵
        for x in range(-i, 3-i):
            for y in range(-j, 3-j):
                # 将要访问的点位于棋盘内，且未被访问
                if a[i + x][j + y] == 0:
                    # 两点连线经过中间点时 需确认中间点已经被访问
                    if x % 2 or y % 2 or (~(x % 2) and ~(y % 2) and a[i + int(x / 2)][j + int(y / 2)] == 1):
                        a[i + x][j + y] = 1
                        self.search(a, i + x, j + y, c + 1, m, n)
                        a[i + x][j + y] = 0

    def solution(self, m, n):
        a = []
        for i in range(3):
            a_i = []
            for j in range(3):
                a_i.append(0)
            a.append(a_i)

        if m > n or n <= 0:
            return 0
        for a1 in range(3):
            for a2 in range(3):
                a[a1][a2] = 1
                self.search(a, a1, a2, 1, m, n)
                a[a1][a2] = 0
        return self.count


if __name__ == '__main__':
    count = 0
    s = Solution()
    print(s.solution(1, 2))
