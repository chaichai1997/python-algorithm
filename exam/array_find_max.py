# -*- coding: utf-8 -*-
# author = "chaichai"


"""
从1~n,每篇笔记都有点赞数
获取点赞数最多，挑选笔记最少的
规则：
不能出现连续编号的笔记
总点赞数最多
"""


def find_max(a):
    len_a = len(a)
    max_c = [a[0], max(a[0], a[1])]
    count = [1, 1]
    for j in range(2, len_a):
        if max_c[j - 2] + a[j] > max_c[j - 1]:
            max_c.append(max_c[j - 2] + a[j])
            count.append(count[j-2] + 1)
        else:
            max_c.append(max_c[j - 1])
            count.append(count[j - 1])
    return max_c[-1], count[-1]


if __name__ == '__main__':
    n = input()
    num = input()
    data = num.split()
    for i in range(len(data)):
        data[i] = int(data[i])
    result = find_max(data)
    print(result[0], result[1])
