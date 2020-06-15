# -*- coding: utf-8 -*-
# author = "chaichai"


"""
小红书算法题三：
N只魔物，血量为[h1,..hn]
M为法力数，每次魔法攻击伤害值为X，消耗为1
物理攻击伤害值为1， 次数不限
求可在T回合内获胜的最小x值
"""


"""
判断是否匹配
"""


def is_match(b, t, m, x):
    count = 0
    remain = []
    # 对每个魔物使用法力攻击。计算总次数与剩余血量
    for i in b:
        count += i//x
        remain.append(i % x)
    remain_b = sum(remain)
    if count >= m:
        need = x * (count - m)
        need += remain_b
        if m + need <= t:
            return True
        else:
            return False
    else:
        remain.sort(reverse=True)
        phy = sum(remain[m-count:])
        if m + phy <= t:
            return True
        else:
            return False


"""
计算得到T的最小值
b:血量
n:魔物数
t：回合数
m:法力
"""


def find_min_x(b, t, m):
    h = sorted(b, reverse=True)
    total = sum(h)
    # 寻找必杀技造成的固定伤害范围,即法力伤害最大值
    max_x = h[0]   # 血量最大的魔物
    # (总血量-最少物理攻击次数)/法力值，即法力伤害最小值
    min_x = (total - (t-m))//m
    # 每回合杀掉一个魔物也无法全部解决所有魔物
    if m + sum(h[m:]) > t:
        return -1
    while min_x < max_x:
        index = (min_x + max_x) // 2
        if is_match(h, t, m, index):
            max_x = index
        else:
            min_x = index + 1
    return min_x


if __name__ == '__main__':
    data = input()
    data = data.split()
    N = int(data[0])
    T = int(data[1])
    M = int(data[2])
    value = input()
    value = value.split()
    blood = []
    for i in value:
        blood.append(int(i))
    print(find_min_x(blood, T, M))
