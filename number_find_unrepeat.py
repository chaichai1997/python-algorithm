# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何找最小的不重复数
不重复数：相邻位置数据不同
"""


"""
处理数字相加的进位
输入： 字符数字， pos为加1操作对应的下标位置
"""


def carry(num, pos):
    while pos > 0:
        if int(num[pos]) > 9:
            num[pos] = '0'
            num[pos-1] = str(int(num[pos-1])+1)
        pos -= 1


"""
获取大于n的最小不重复数
"""


def find_unrepeat(n):
    count = 0
    n_char = list(str(n+1))
    ch = [None] * (len(n_char) + 2)
    ch[0] = '0'
    ch[len(ch)-1] ='0'
    i = 0
    while i < len(n_char):
        ch[i+1] = n_char[i]
        i += 1
    lens = len(ch)
    i = lens - 2
    while i > 0:
        count += 1
        if ch[i-1] == ch[i]:
            ch[i] = str(int(ch[i])+1)
            carry(ch, i)
            j = i + 1
            while j < lens:
                if (j-i) % 2 == 1:
                    ch[j] = '0'
                else:
                    ch[j] = '1'
                j += 1
            i += 1
        else:
            i -= 1
    print(count)
    print(int(''.join(ch)))


if __name__ == '__main__':
    find_unrepeat(23345)