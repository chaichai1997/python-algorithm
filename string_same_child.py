# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求两个字符串的最大公共子串
"""

"""
方法一：动态规划
以f[i, j]存储以i为结尾的字串与以j结尾的字串的公共长度
"""


def find_array_child(str1, str2):
    l_1 = len(str1)
    l_2 = len(str2)
    str1 = list(str1)
    str2 = list(str2)
    max_l = 0  # 最大公共子串长度
    e = 0  # 公共子串末尾位置
    f = []
    for i in range(l_1 + 1):
        f_1 = []
        for j in range(l_2 + 1):
            f_1.append(0)
        f.append(f_1)
    for i in range(1, l_1 + 1):
        for j in range(1, l_2 + 1):
            if str1[i - 1] == str2[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
                if f[i][j] > max_l:
                    max_l = f[i][j]
                    e = i
            else:
                f[i][j] = 0
    s = e - max_l
    child = ''
    while s < e:
        child += str1[s]
        s += 1
    return child


"""
方法二：滑动比较法
一个字符串位置不变，移动另一个判断其公共子串
"""


def find_same_child_slip(str1, str2):
    l_1 = len(str1)
    l_2 = len(str2)
    max_len = 0
    tmp_len = 0
    end = 0
    i = 0
    while i < l_1 + l_2:
        s_1 = 0  # 当前比较的位置
        s_2 = 0
        if i < l_1:
            s_1 = l_1 - i
        else:
            s_2 = i - l_1
        j = 0
        while (s_1 +j < l_1) and (s_2 + j < l_2):
            if str1[s_1 +j] == str2[(s_2 + j)]:
                tmp_len += 1
            else:
                if tmp_len > max_len:
                    max_len = tmp_len
                    end = s_1 + j
                else:
                    tmp_len = 0
            j += 1
        i += 1
    s = end - max_len
    child = ''
    while s < end:
        child += str1[s]
        s += 1
    return child


if __name__ == '__main__':
    str_1 = 'abcade'
    str_2 = 'dgcadde'
    print(find_array_child(str_1, str_2))
    print(find_same_child_slip(str_1, str_2))