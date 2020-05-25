# -*- coding: utf-8 -*-
# author = "chaichai"


"""
找出数组中和最大的子序列
"""


"""
方法一： 蛮力法
先找到子序列，即array[i,...j],然后求该子序列的和与之前存贮的最大值比较
时间复杂度O(n^3)
"""


def find_max_chid_1(array):
    l = len(array)
    if array is None or l < 1:
        print("数组不存在")
        return
    sum_max = 0
    i = 0
    while i < l:
        j = i
        while j < l:
            k = i
            sum_aray = 0
            while k < j:
                sum_aray += array[k]
                k += 1
            if sum_aray > sum_max:
                sum_max = sum_aray
            j += 1
        i += 1
    return sum_max


"""
方法二：重复利用已经计算的子序列和，即array[i, ..j] = array[i,...j-1] + array[j]
时间复杂度O(n^2)
"""


def find_max_child_2(array):
    l = len(array)
    if array is None or l < 1:
        print("数组不存在")
        return
    sum_max = 0
    i = 0
    while i < l:
        sum_array = 0
        j = i
        while j < l:
            sum_array = sum_array + array[j]
            if sum_array > sum_max:
                sum_max = sum_array
            j += 1
        i += 1
    return sum_max


"""
方法三：动态规划法
将array[1,..i-1]的最大子序列和分为三种情况：
1. 最大子序列包含a[i-1], 和为s[1, ..i-1]
2. a[i-1]单独为最大子序列
3. a[i-1] 不属于最大子序列
sum array[1, ..i-1] = max(s[1, ..., i-1], a[i-1], sum array[1,... i-2])
时间复杂度 O(n) 空间复杂度O(n)
"""


def find_max_child_3(array):
    l = len(array)
    if array is None or l < 1:
        print("数组不存在")
        return
    i_max = [None] * l  # [1,..i-1]的最大序列和
    i_sum = [None] * l    # 包含i-1的序列和
    # i_max[l-1] = array[l-1]
    # i_sum[l-1] = array[l-1]
    i = 1
    i_sum[0] = i_max[0] = array[0]
    while i < l:
        i_sum[i] = max(i_sum[i-1] + array[i], array[i])
        i_max[i] = max(i_sum[i], i_max[i-1])
        i += 1
    return i_max[l-1]


"""
方法4：改进的动态规划，仅保存i_sum[i-1]与i_max[i-1]
"""


def find_max_child_4(array):
    l = len(array)
    if array is None or l < 1:
        print("数组不存在")
        return
    i = 1
    i_sum = i_max = array[0]
    while i < l:
        i_sum = max(i_sum + array[i], array[i])
        i_max = max(i_sum, i_max)
        i += 1
    return i_max


"""
找到最大子序列的位置
思路 i_sum[i-1]<0, 则i_sum[i]= array[i], i即为子序列的起点
"""


class Test:
    def __init__(self):
        self.begin = 0
        self.end = 0

    def find_position(self, array):
        i_max = -2 ** 31
        n_sum = 0
        n_start = 0
        i = 0
        while i < len(array):
            if n_sum < 0:
                n_sum = array[i]
                n_start = i
            else:
                n_sum += array[i]
            if n_sum > i_max:
                i_max = n_sum
                self.begin = n_start
                self.end = i
            i += 1
        return i_max

    def get_begin(self):
        return self.begin

    def get_end(self):
        return self.end


if __name__ == '__main__':
    arr = [1, -2, 4, 8, -4, 7, -1, -5]
    t = Test()
    print(find_max_chid_1(arr))
    print(find_max_child_2(arr))
    print(find_max_child_3(arr))
    print(find_max_child_4(arr))
    print(str(t.find_position(arr)))
    print("start:" + str(t.get_begin()) + ' end:' + str(t.get_end()) )
