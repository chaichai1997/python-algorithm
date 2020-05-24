# -*- coding: utf-8 -*-
# author = "chaichai"


def get_min_l(arr, low, high):
    if high < low:
        return arr[0]
    # 只剩下一个元素，一定是最小值
    if high == low:
        return arr[low]
    # 右移一位，防止溢出
    mid = low + ((high - low) >> 1)
    # 判断arr[mid]是否为最小值
    if arr[mid] < arr[mid - 1]:
        return arr[mid]
    # 判断arr[mid+1]是否为最小值
    elif arr[mid + 1] < arr[mid]:
        return arr[mid+1]
    # 最小值在左半部分
    elif arr[mid] > arr[low]:
        return get_min(arr, low, mid-1)
    elif arr[mid] > arr[low]:
        return get_min(arr, mid + 1, high)
    else:
        return min(get_min(arr, low, mid + 1), get_min(arr, mid + 1, high))


def get_min(arr):
    if arr is None:
        print("非法")
        return
    else:
        return get_min_l(arr, 0, len(arr)-1)


if __name__ == '__main__':
    array = [5, 6, 1, 2, 3, 4]
    mins = get_min(array)
    print(mins)

