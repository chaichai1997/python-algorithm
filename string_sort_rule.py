# -*- coding: utf-8 -*-
# author = "chaichai"


"""
按照给定字母顺序对字符数组排序
"""


"""
比较大小
"""


def compare(str1, str2, rule):
    l_1 = len(str1)
    l_2 = len(str2)
    i = 0
    j = 0
    while i < l_1 and j < l_2:
        if str1[i] not in rule.keys():
            rule[str1[i]] = -1
        if str2[j] not in rule.keys():
            rule[str2[j]] = -1
        if rule[str1[i]] < rule[str2[j]]:
            return -1
        elif rule[str1[i]] > rule[str2[j]]:
            return 1
        else:
            i += 1
            j += 1
    if i == l_1 and j == l_2:
        return 0
    elif i == l_1:
        return -1
    else:
        return 1


"""
排序算法
"""


def sort(s, rule):
    l_s = len(s)
    for i in range(1, l_s):
        tmp = s[i]
        j = i-1
        while j >= 0:
            if compare(tmp, s[j], rule) == -1:
                s[j+1] = s[j]
            else:
                break
            j -= 1
        s[j+1] = tmp


if __name__ == '__main__':
    s = ['bed', 'dog', 'dear', 'eyes']
    se = 'dgecfboa'
    l_se = len(se)
    rule = dict()
    for i in range(l_se):
        rule[se[i]]=i
    sort(s, rule)
    print(s)


