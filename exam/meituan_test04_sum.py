# -*- coding: utf-8 -*-
# author = "chaichai"

"""
计算员工工时
"""
data_list_1 = input().split()
data_list_2 = input().split()
total = int(data_list_2[2]) + int(data_list_2[4]) + int(data_list_2[6])
print(data_list_1[1]+" " + data_list_2[2] + " " + data_list_2[4] + " " + data_list_2[6] + " " + str(total))
