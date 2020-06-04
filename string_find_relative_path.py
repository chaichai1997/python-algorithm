# -*- coding: utf-8 -*-
# author = "chaichai"


"""
已知两个路径求其相对路径
"""


def find_relative_path(s1, s2):
    if s1 is None or s2 is None:
        print("illegal")
        return
    r = ""
    d_1 = 0
    d_2 = 0
    l_1 = len(s1)
    l_2 = len(s2)
    i = 0
    j = 0
    while i < l_1 and j < l_2:
        if s1[i] == s2[j]:
            if s1[i] == '/':
                d_1 = i
                d_2 = j
            i += 1
            j += 1
        else:
            d_1 += 1
            while d_1 < l_1:
                if s1[d_1] == '/':
                    r += '../'
                d_1 += 1
            d_2 += 1
            r += s2[d_2:]
            break
    return r


if __name__ == '__main__':
    path1 = " /algorithm/program/code/string_find_relative_path"
    path2 = "/algorithm/program/code"
    print(find_relative_path(path1, path2))