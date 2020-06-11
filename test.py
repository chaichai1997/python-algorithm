# -*- coding: utf-8 -*-
# author = "chaichai"

i = 1
count = 1
while count < 1500:
    if i % 2 == 0 or i % 3 == 0 or i % 5 ==0:
        count += 1
    i += 1
print(i)