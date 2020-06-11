# -*- coding: utf-8 -*-
# author = "chaichai"

"""
寻找字符串的最长重复子串
"""


"""
方法1：寻找子序列后判断
"""


def find_child(strs, start, length, child):
    l_s = len(strs)
    child.append(strs[start:start + length])
    if length == l_s:
        return child
    if start + length >= l_s:
        find_child(strs, 0, length+1, child)
    elif start + length < l_s:
        find_child(strs, start+1, length, child)


def find_repeat_child(child):
    for i in child:
        print(i)
        n = len(i)
        if n > 2 and n % 2 == 0:
            if i[:n//2] == i[n//2:]:
                return n


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
后缀数组法
后缀是指从某个位置i开始到字符串末尾的子串
将找重复子串问题转换为比对相邻两个子串的公共串长度
"""


class SubString:

    # 找出最长公共子串的长度
    def find_max_length(self, s1, s2):
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] == s2[i]:
                i += 1
            else:
                break
            i += 1
        return i

    # 获取最长公共子串
    def get_max_child(self, txt):
        n = len(txt)
        end = [None] * n  # 存储后缀数组
        len_max = 0
        len_child = None
        # 获取后缀数组
        i = 0
        while i < n:
            end[i] = txt[i:]
            i += 1
        end.sort()
        i = 1
        while i < n:
            tmp = self.find_max_length(end[i], end[i-1]*2)
            if tmp > len_max:
                len_max = tmp
                len_child = end[i][0:i+1]
            i += 1
        return len_child


if __name__ == '__main__':
    strs = input()
    # print(find_repeat(strs))
    test = SubString()
    print(test.get_max_child(strs))
