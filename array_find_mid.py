# -*- coding: utf-8 -*-
# author = "chaichai"


"""
在不排序的前提下求数组的中位数
思路：借鉴快速排序，将问题转换为求数组中第[len/2 + 1]小的数
"""


class Test:
    def __init__(self):
        self.p = 0

    def spilt(self, array, low, high):
        key = array[low]
        while low < high:
            while low < high and array[high] >= key:
                high -= 1
            array[low] = array[high]
            while low < high and array[low] <= key:
                low += 1
            array[high] = array[low]
        array[low] = key
        self.p = low

    def get_mid(self, array):
        low = 0
        high = len(array) - 1
        mid = (low + high) // 2
        while True:
            self.spilt(array, low, high)
            print(array)
            if self.p == mid:
                break
            elif self.p > mid:
                high = self.p - 1
            else:
                low = self.p + 1
        return array[mid] if len(array) % 2 != 0 else (array[mid]+array[mid+1])/2


if __name__ == '__main__':
    array = [7, 5, 3, 1, 11, 9]
    dst = Test().get_mid(array)
    print(dst)