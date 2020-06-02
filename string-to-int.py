# -*- coding: utf-8 -*-
# author = "chaichai"


"""
判断字符串是否是整数
"""


"""
递归法实现
"""


class Test:
    def __init__(self):
        self.flag = None

    def is_number(self, e):
        return '0' <= e <= '9'

    def get_flag(self):
        return self.flag

    def str_string(self, strs, length):
        if length > 1:
            if not self.is_number(strs[length-1]):
                print("不是数字")
                self.flag = False
                return -1
            if strs[0] == '-':
                return self.str_string(strs, length-1) * 10 - (ord(strs[length-1]) - ord('0'))
            else:
                return self.str_string(strs, length-1) * 10 + (ord(strs[length-1]) - ord('0'))
        else:
            if strs[0] == '-':
                return 0
            else:
                if not self.is_number(strs[0]):
                    print("不是数字")
                    self.flag = False
                    return -1
                return ord(strs[0]) - ord('0')

    def transform(self, s):
        self.flag = True
        if s is None or list(s)[0] == '-' and len(s) == 1:
            print("不是数字")
            self.flag = False
            return -1
        if list(s)[0] == '+':
            return self.str_string(s[1:len(s)], len(s)-1)
        else:
            return self.str_string(s, len(s))


"""
非递归法实现
"""


class Test2:
    def __init__(self):
        self.flag = None

    def is_number(self, e):
        return '0' <= e <= '9'

    def get_flag(self):
        return self.flag

    def string_int(self, strs):
        if strs is None:
            self.flag = False
            print("not is int")
            return -1
        self.flag = True
        i = 0
        res = 0
        minus = False
        if strs[i] == '-':
            minus = True
            i += 1
        if strs[i] == '+':
            minus = False
            i += 1
        while i < len(strs):
            if self.is_number(strs[i]):
                res = res * 10 + ord(strs[i]) - ord('0')
            else:
                self.flag = False
                print("not is int")
                return -1
            i += 1
        return -res if minus else res


if __name__ == '__main__':
    # t = Test()
    t = Test2()
    s = '-543'
    print(t.string_int(s))
    # print(t.transform(s))
    s2 = '543'
    print(t.string_int(s2))
    # print(t.transform(s2))
    s3 = '++54'
    # print(t.transform(s3))
    t.string_int(s3)



