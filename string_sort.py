# -*- coding: utf-8 -*-
# author = "chaichai"


"""
对包含大写字母与雄安写字母的字符串进行重新组合，使小写字母排在大写字母前
思路：快速排序，遍历首位，若满足交换条件则交换
"""


def string_sort(string):
    l = len(string)
    s = 0
    e = l-1
    while s < e:
        while 'z' >= string[s] >= 'a' and s < e:
            s += 1
        while 'Z' >= string[e] >= 'A' and s < e:
            e -= 1
        tmp = string[s]
        string[s] = string[e]
        string[e] = tmp


if __name__ == '__main__':
    data = list('aBcAbC')
    string_sort(data)
    print(data)