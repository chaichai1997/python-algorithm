# -*- coding: utf-8 -*-
# author = "chaichai"

"""
计算数字的组合种类
例如（5， 2）
1 + 4 = 5
2 + 3 =5
return 2
"""


def seperate(n, m):
    if m == 1 or n - m == 1 or n == m:
        dict[(n, m)] = 1
    elif m == 2:
        dict[(n, m)] = int(n / 2)
    else:
        left, i, total = n-m, 1, 0
        if (left, i) in dict.keys():
            total = total + dict[(left, i)]
            i = i + 1
        else:
            seperate(left, i)
        dict[(n, m)] = total


if __name__ == '__main__':
    n, m = map(int, input().split())
    dict = {}
    seperate(n, m)
    print(dict[n, m])