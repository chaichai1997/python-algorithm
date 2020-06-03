# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求一个串中出现的第一个最长重复子串
"""


"""
传统方法
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
    max_count = 0
    max_child = None
    l_c = len(child)
    for i in range(l_c):
        for j in range(l_c):
            if child[i] == child[j] and i != j:
                if len(child[i]) > max_count:
                    max_child = child[i]
                    max_count = len(child[i])
    return max_child


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
            tmp = self.find_max_length(end[i], end[i-1])
            if tmp > len_max:
                len_max = tmp
                len_child = end[i][0:i+1]
            i += 1
        return len_child


if __name__ == '__main__':
    strs = 'banana'
    dst = []
    find_child(strs, 0, 1, dst)
    max = find_repeat_child(dst)
    print(max)
    test = SubString()
    print(test.get_max_child(strs))
