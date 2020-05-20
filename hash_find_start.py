# -*- coding: utf-8 -*-
# author = "chaichai"

"""
给定一趟旅途的车票信息，从中找出路线
根据hash实现，python中为集合，
先找起点，后找下一站
"""


def find_start(inputs):
    r_input = dict()
    for k, v in inputs.items():
        r_input[v] = k                # 字典反转

    for k, v in inputs.items():
        if k not in r_input:
            start = k
            break

    if start is None:
        print("输入不合理")
        return

    while start in inputs.keys():
        to = inputs[start]
        print(start + ' -> ' + to)
        start = to


if __name__ == '__main__':
    inputs = dict()
    inputs["西安"] = "成都"
    inputs["北京"] = "上海"
    inputs["大连"] = "西安"
    inputs["上海"] = "大连"
    find_start(inputs)