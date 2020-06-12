# -*- coding: utf-8 -*-
# author = "chaichai"

s = input()
data = []
w = s.split()
data = w[::-1]
for i in data:
    if len(i) > 0:
        print(i, end=' ')
