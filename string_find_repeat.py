# -*- coding: utf-8 -*-
# author = "chaichai"


"""
判断字符串中是否包含重复元素
"""


"""
方法一：蛮力法 时间复杂度 O(n^2)
"""


def find_repeat(strs):
    l_s = len(strs)
    for i in range(l_s):
        for j in range(i+1, l_s):
            if strs[i] == strs[j]:
                print("repeat")
                return
    print("not repeat")


"""
方法二： 以时间换空间 时间复杂度O(n)
"""


def find_repeat_time(strs):
    l_s = len(s)
    sign = [False] * 256
    for i in range(l_s):
        index = ord(strs[i])-ord('0')
        if sign[index] is True:
            print("repeat")
            return
        sign[index] = True
    print("not repeat")


if __name__ == '__main__':
    s = 'god'
    find_repeat(s)
    find_repeat_time(s)