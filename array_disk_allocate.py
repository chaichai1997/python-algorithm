# -*- coding: utf-8 -*-
# author = "chaichai"

"""
对磁盘进行分配
"""


def allocate(d, p):  # d- disk p- process
    d_index = 0
    for i in p:
        while d_index < len(d) and i > d[d_index]:
            d_index += 1
        if d_index >= len(d):
            return False
        d[d_index] -= i

    return True


if __name__ == '__main__':
    d = [120, 120, 120]
    p = [60, 80, 80, 20, 80]
    if allocate(d, p):
        print("succeed")
    else:
        print("False")
