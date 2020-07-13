# -*- coding: utf-8 -*-
# author = "chaichai"

"""
计算数字的组合种类
例如（5， 2）
1 + 4 = 5
2 + 3 =5
return 2
"""


# def seperate(n, m, result, count, c):
#     if n < 0 or m == 0:
#         return
#     else:
#         if 0 > count > m:
#             return
#         elif count == m:
#             if n == 0:
#                 c.append(1)
#                 return
#             else:
#                 return
#     if count == 0:
#         i = 1
#     else:
#         i = result[count - 1]
#     while i <= n:
#         try:
#             result[count] = i
#             count += 1
#             seperate(n - i, m, result, count, c)
#             count -= 1
#             i += 1
#         except:
#             break
#     return c


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
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    count = 0
    c = []
    result = [0] * m
    # dict = {}
    print(len(seperate(n, m, result, count, c)))
    # seperate(n, m)
    # print(dict[n, m])
