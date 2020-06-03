# -*- coding: utf-8 -*-
# author = "chaichai"


"""
如何统计字符串中连续的重复字符个数
"""


"""
非递归方法
"""


def find_repeat(strs):
    max_len = 0
    l_s = len(strs)
    tmp_count = 1
    for i in range(1, l_s):
        if strs[i] == strs[i-1]:
            tmp_count += 1
        else:
            if tmp_count > max_len:
                max_len = tmp_count
            tmp_count = 1
    if tmp_count > max_len:
        max_len = tmp_count
    return max_len


"""
递归方法
"""


def find_repeat_r(strs, start_index, tmp_len, max_len):
    if start_index == len(strs) - 1:
        return max(tmp_len, max_len)
    if strs[start_index] == strs[start_index + 1]:
        return find_repeat_r(strs, start_index + 1, tmp_len + 1, max_len)
    else:
        return find_repeat_r(strs, start_index + 1, 1, max(tmp_len, max_len))


if __name__ == '__main__':
    str = 'abbbbbssss'
    print(find_repeat(str))
    print(find_repeat_r(str, 0, 1, 0))


