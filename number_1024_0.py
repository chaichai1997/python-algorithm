# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何判断 1024！ 末尾有多少个0
"""


"""
方法1： 蛮力法，直接求阶乘
"""


"""
方法二： 因子法
5与任何一个偶数相乘都会增加末尾0的个数
5 与 偶数 0  一个因子
25 与 偶数 00  两个因子
"""


def zero_count(n):
    count = 0
    while n > 0:
        n = n//5
        count += n
    return count


if __name__ == '__main__':
    print(zero_count(1024))