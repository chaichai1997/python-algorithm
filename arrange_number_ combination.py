# -*- coding: utf-8 -*-
# author = "chaichai"


"""
找到组成一个整数的所有组合
例如 4: 1+1+2 1+3 1+1+1 2+2 4
思路：递归
"""


"""
sums:目标整数
result： 存储结果组合
count：组合中数字个数
"""


def get_combination(sums, result, count):
    if sums < 0:
        print('illegal')
        return
    if sums == 0:
        print("满足条件的组合：", end= '')
        i = 0
        while i < count:
            print(result[i], end=' ')
            i += 1
        print()
        return
    if count == 0:
        i = 1
    else:
        i = result[count - 1]
    while i <= sums:
        result[count] = i
        count += 1
        get_combination(sums-i, result, count)
        count -= 1
        i += 1


def show_all(n):
    if n < 1:
        print('illegal')
        return
    result = [None] * n
    get_combination(n, result, 0)


if __name__ == '__main__':
    show_all(5)