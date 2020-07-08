# -*- coding: utf-8 -*-
# author = "chaichai"

"""
翻转给出中心位置的周围点
"""


def string_to_list(data):
    data = data[2:-2]
    data = data.split('],[')
    t = []
    for i in range(len(data)):
        t_i = []
        for j in (data[i].split(',')):
            t_i.append(j)
        t.append(t_i)
    return t


def reverse(data, pos):
    for p in pos:
        p = [int(p[0])-1, int(p[1])-1]
        print(p)
        l_p = [[p[0]-1, p[1]], [p[0]+1, p[1]], [p[0], p[1]-1], [p[0], p[1]+1]]
        for i in l_p:
            if 0 <= i[0] <= 3 and 0 <= i[1] <= 3:
                print(i[0], i[1])
                if data[i[0]][i[1]] == '0':
                    data[i[0]][i[1]] = '1'
                elif data[i[0]][i[1]] == '1':
                    data[i[0]][i[1]] = '0'
    return data


if __name__ == '__main__':
    n = input()
    p = input()
    t = string_to_list(n)
    p = string_to_list(p)
    result = reverse(t, p)
    s = '['
    for i in range(4):
        s = s + '['
        for j in range(4):
            if j < 3:
                s = s + result[i][j] + ','
            elif j == 3:
                if i == 3:
                    s = s + result[i][j] +']'
                else:
                    s = s + result[i][j] +'],'
    s = s + ']'
    print(s)




