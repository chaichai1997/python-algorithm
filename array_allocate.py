# -*- coding: utf-8 -*-
# author = "chaichai"


"""
实现任务调度
方法：贪心
"""


def calculate_process_time(time, number):
    if time is None or number <= 0:
        return None
    n_t = len(time)
    p_time = [0] * n_t
    for i in range(number):
        min_time = p_time[0] + time[0]
        min_index = 0  # 指机器数目
        j = 1
        while j < n_t:
            if min_time > p_time[j] + time[j]:
                min_time = p_time[j] + time[j]
                min_index = j
            j += 1
        p_time[min_index] = min_time
        i += 1
    return p_time


if __name__ == '__main__':
    t = [7, 10]
    n = 6
    p_tine = calculate_process_time(t, n)
    if p_tine is None:
        print("无法分配")
    else:
        totap = p_tine[0]
        i = 0
        while i < len(p_tine):
            print(str(i+1), str(p_tine[i]/t[i]), str(p_tine[i]))
            if p_tine[i] > totap:
                totap = p_tine[i]
            i += 1

        print(totap)



