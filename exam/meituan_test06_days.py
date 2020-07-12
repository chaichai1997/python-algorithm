# -*- coding: utf-8 -*-
# author = "chaichai"
"""
判断给定年月的天数
"""


def find_days(year, month):
    d_1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d_2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(d_2[month - 1])
    else:
        print(d_1[month - 1])


if __name__ == '__main__':
    # pyhton 读入多行数据
    while True:
        try:
            year, month = map(int, input().split())
            find_days(year, month)
        except:
            break



