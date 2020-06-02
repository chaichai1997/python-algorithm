# -*- coding: utf-8 -*-
# author = "chaichai"


"""
实现字符串的匹配
"""


"""
直接计算法
时间复杂度： m *n 
"""


def match(s, p):
    if s is None or p is None:
        print("参数不合理")
        return -1
    l_s = len(s)
    l_p = len(p)
    if l_s < l_p:
        return -1
    i = 0
    j = 1
    while i < l_s and j < l_p:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            # 后退重新比较
            i = i - j + 1
            j = 0
            if i > (l_s-l_p):
                return -1
    if j >= l_p:
        return i - l_p
    return -1


"""
KMP方法
主串的第i个字符与模式串的第j个字符匹配失败，则接着比较第i个字符串与模式的第k个字符
"""


"""
求字符串的next数组
next[i] = m ==> i[1], i[2], ...i[m-1] = i[i-m],...i[i-1] 
"""


def get_next(p, next):
    i = 0
    j = -1
    next[0] = -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]


def match(s, p, next):
    if s is None or p is None:
        print("参数不合理")
        return -1
    l_s = len(s)
    l_p = len(p)
    if l_s < l_p:
        return -1
    i = 0
    j = 1
    while i < l_s and j < l_p:
        print(i, j)
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j >= l_p:
        return i - l_p
    return -1


if __name__ == '__main__':
    s = 'xyzsabc'
    y = 'abc'
    lens = len(y)
    next = [0] * (lens +1)
    get_next(y, next)
    print("next数组为：", next[0])
    i = 1
    while i < lens - 1:
        print("," + str(next[i]))
        i += 1
    print(match(s, y, next))
    # print(match(s, y))
