# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求数字的组合
思路：
根据点构造连通图，然后深度优先遍历连通图，得到数字的组合
"""


class Test:

    def __init__(self, arr):
        self.numbers = arr
        # 标记节点是否被遍历
        self.Visited = [None] * len(self.numbers)
        # 图的二位数组表示
        self.graph = [([None] * len(self.numbers)) for i in range(len(self.numbers))]
        self.n = 6
        # 数字的组合
        self.combination = ''
        # 存储所有的组合
        self.s = set()

    """
     从start开始深度遍历
    """

    def depth_search(self, start):
        self.Visited[start] = True
        self.combination += str(self.numbers[start])
        if len(self.combination) == self.n:
            if self.combination.index("4") != 2:
                self.s.add(self.combination)
        j = 0
        while j < self.n:
            if self.graph[start][j] == 1 and self.Visited[j] is False:
                self.depth_search(j)
            j += 1
        self.combination = self.combination[: -1]
        self.Visited[start] = False

    """
    构造图
    """

    def construct(self):
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if i == j:
                    self.graph[i][j] = 0
                else:
                    self.graph[i][j] = 1
                j += 1
            i += 1
        self.graph[3][5] = 0
        self.graph[5][3] = 0

    """
    遍历得到所有
    """

    def search(self):
        for i in range(self.n):
            self.depth_search(i)
        for i in self.s:
            print(i)


if __name__ == '__main__':
    array = [1, 2, 2, 3, 4, 5]
    t = Test(array)
    t.construct()
    t.search()
