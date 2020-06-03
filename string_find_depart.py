# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何找到由其他单词组成的最长单词
"""


class LongWord:

    """
    查找输入是否在字符串中
    """
    def find(self, array, strs):
        for i in array:
            if i == strs:
                return True
        return False

    # 判断输入是否由其他单词组成
    def compose(self, array, strs, length):
        l_s = len(strs)
        if l_s == 0:
            return True
        for i in range(1, l_s+1):
            if i == length:
                return False
            dst = strs[0:i]
            if self.find(array, dst):
                if self.compose(array, strs[i:], length):
                    return True
        return False

    # 找出能由其他字符串组成的最长字符串
    def find_max(self, array):
        array = sorted(array, key=len, reverse=True)
        for i in array:
            if self.compose(array, i, len(i)):
                return i
        return None


if __name__ == '__main__':
    strs = ['test', 'tester', 'testertest', 'testing', 'apple', 'seattle', 'banana', 'batting', 'ngcat', 'batti',
            'testingtester', 'bat', 'testbattingcat']
    lw = LongWord()
    long = lw.find_max(strs)
    if long is not None:
        print(long)
    else:
        print('不存在')


