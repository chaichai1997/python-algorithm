# -*- coding: utf-8 -*-
# author = "chaichai"


"""
判断字符串中是否包含重复元素
"""


"""
方法一：蛮力法
"""


def find_repeat(strs):
    l_s = len(strs)
    for i in range(l_s):
        for j in range(i+1, l_s):
            if strs[i] == strs[j]:
                print("repeat")
                return
    print("not repeat")


if __name__ == '__main__':
    s = 'good'
    find_repeat(s)