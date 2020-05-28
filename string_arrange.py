# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何求一个字符串的全排列
"""


def swap(string, a, b):
    tmp = string[a]
    string[a] = string[b]
    string[b] = tmp


def string_arrange(string, start):
    if start is None or start < 0:
        return
    if start == len(string) - 1:
        print("".join(string), end=' ')
    else:
        i = start
        while i < len(string):
            swap(string, start, i)
            string_arrange(string, start + 1)
            swap(string, start, i)
            i += 1


# # 根据当前字符串组合
#
# def get_next(str):
#     end = len(string) - 1
#     cur = end
#     while cur != 0:
#         suc = cur   # cur的后继
#         cur -= 1
#         if str[cur] < str[suc]:
#             tmp = end
#             while str[tmp] < str[cur]:
#                 tmp -= 1
#             swap(str, cur, tmp)
#             reverse(str, cur, tmp)
#             return True
#     return False
#
#
# def reverse(str, begin, end):
#     i = begin
#     j = end
#     while i < j:
#         swap(str, i, j)
#         i += 1
#         j -= 1
#
if __name__ == '__main__':
    a = 'abcd'
    string = list(a)
    string_arrange(string, 0)
    print()
