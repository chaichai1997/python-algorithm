# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求字符串里最长回文子串
回文串：从左至右遍历与从右至左遍历结果相同 abcba
"""


"""
方法一：动态规划法
p（i,j）=1 si,..sj为回文子串
si+1=sj+1 p(i+1, j+1)=P(i, j)
si=si+1 p(i, i+1)=1
"""


class Test:
    def __init__(self):
        self.start_index = None
        self.len = None

    def get_start_index(self):
        return self.start_index

    def get_lens(self):
        return self.len

    def find_reg_child(self, strs):
        if strs is None:
            return
        n = len(strs)
        self.start_index = 0
        self.len = 1
        # 存放历史记录
        his = [([None] * n) for i in range(n)]
        for i in range(n):
            for j in range(n):
                his[i][j] = 0
        # 长度为1
        for i in range(n):
            his[i][i] = 1
        # 长度为2
        for i in range(n-1):
            if strs[i] == strs[i+1]:
                his[i][i+1] = 1
                self.start_index = i
                self.len = 2
        # 长度为3
        l_p = 3
        while l_p < n:
            i = 0
            while i < n - l_p + 1:
                j = i + l_p - 1
                if strs[i] == strs[j] and his[i+1][j-1] == 1:
                    his[i][j] = 1
                    self.start_index = i
                    self.len = l_p
                i += 1
            l_p += 1


"""
中心扩展法
"""


class Test2:
    def __init__(self):
        self.start_index = None
        self.len = 0

    def get_start_index(self):
        return self.start_index

    def get_lens(self):
        return self.len

    # 对字符串以C1 和 c2为中心像两侧寻找回文子串
    def expand_side(self, string, c1, c2):
        n = len(string)
        while c1 >= 0 and c2 <= n and string[c2] == string[c1]:
            c1 -= 1
            c2 += 1
        tmp_start = c1 + 1
        tmp_len = c2-c1-1
        if tmp_len > self.len:
            self.len = tmp_len
            self.start_index = tmp_start

    # 找到最长的回文子串
    def get_max_child(self, string):
        if string is None:
            return
        n = len(string)
        for i in range(n-1):
            self.expand_side(string, i, i)
            self.expand_side(string, i, i+1)


if __name__ == '__main__':
    strs = 'abcdefgfedxyz'
    # t = Test()
    # t.find_reg_child(strs)
    t = Test2()
    t.get_max_child(strs)
    if t.get_start_index() != -1 and t.get_lens() != -1:
        i = t.get_start_index()
        while i < t.get_start_index()+t.get_lens():
            print(strs[i], end=' ')
            i += 1
    else:
        print("not find")

