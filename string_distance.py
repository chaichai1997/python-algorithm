# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何求字符串的编辑距离
编辑距离：两个字符串之前由一个转换成另一个所需要的编辑次数
"""


class EditDistance:
    def edit(self, s1, s2, weight):
        if s1 is None and s2 is None:
            return 0
        if s1 is None:
            return len(s2)
        if s2 is None:
            return len(s1)
        l_1 = len(s1)
        l_2 = len(s2)
        Distance = [([None] * (l_2 + 1)) for i in range(l_1+1)]
        for i in range(l_1+1):
            Distance[i][0] = i
        for i in range(l_2+1):
            Distance[0][i] = i
        for i in range(1, l_1+1):
            for j in range(1, l_2 + 1):
                if s1[i-1] == s2[j-1]:
                    Distance[i][j] = min(Distance[i-1][j]+1, Distance[i][j-1]+1, Distance[i-1][j-1])
                else:
                    Distance[i][j] = min(Distance[i-1][j]+1, Distance[i][j-1]+1, Distance[i-1][j-1]+weight)

        print('*********')
        for i in Distance:
            print(i)
        dis = Distance[l_1][l_2]
        return dis


if __name__ == '__main__':
    s1 = 'bciln'
    s2 = 'fciling'
    ed = EditDistance()
    print('distance：', ed.edit(s1, s2, 1))

