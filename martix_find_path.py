# -*- coding: utf-8 -*-
# author = "chaichai"


"""
解决迷宫问题
思路： 回溯法，当前点无路径是则回退至上一步
"""


class Maze:
    def __init__(self):
        self.n = 4

    def print_path(self, sol):
        i = 0
        while i < self.n:
            j = 0
            while j < self.n:
                print(sol[i][j], end=' ')
                j += 1
            print()
            i += 1

    def is_seaf(self, maze, x, y):
        return 0 <= x < self.n and 0 <= y <= self.n and maze[x][y] == 1

    """
    使用回溯法寻找路径，maze表示迷宫
    x, y 表示起点， sol为路径
    """
    def find_path(self, maze, x, y, sol):
        if x == self.n-1 and y == self.n-1:
            sol[x][y] = 1
            return True
        if self.is_seaf(maze, x, y):
            sol[x][y] = 1
            if self.find_path(maze, x+1, y, sol):
                return True
            if self.find_path(maze, x, y+1, sol):
                return True
            sol[x][y] = 0
            return False
        return False


if __name__ == '__main__':
    res = Maze()
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    sol = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    if not res.find_path(maze, 0, 0, sol):
        print("not find")
    else:
        res.print_path(sol)