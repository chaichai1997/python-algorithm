# -*- coding: utf-8 -*-
# author = "chaichai"


"""
求组合1、2、5这三个数组成100的组合数
"""


def compose(n):
    count = 0
    num1 = n
    num2 = n//2
    num5 = n//4
    x = 0
    while x <= num1:
        y = 0
        while y <= num2:
            z = 0
            while z <= num5:
                if x + 2*y + 5 * z == 100:
                    count += 1
                z += 1
            y += 1
        x += 1
    return count


if __name__ == '__main__':
    n = compose(100)
    print(n)

