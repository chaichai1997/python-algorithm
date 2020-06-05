# -*- coding: utf-8 -*-
# author = "chaichai"


"""
将 long型数字转换为16 进制与 2 进制
"""


def int_to_binary(n):
    num = 8 * 8
    bit = []
    for i in range(num):
        b = n >> i
        c, d = divmod(b, 2)
        bit.append(str(d))
    return bit[::-1]


def int_to_hex(n):
    hex = ''
    remain = 0
    while n != 0:
        remain = n % 16
        if remain < 10:
            hex = str(remain + int('0')) + hex
        else:
            hex = str(remain - 10 + ord('A')) + hex
        n = n >> 4
    return chr(int(hex))


if __name__ == '__main__':
    print(int_to_binary(10))
    print(int_to_hex(10))
