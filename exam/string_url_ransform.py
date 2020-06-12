# -*- coding: utf-8 -*-
# author = "chaichai"


"""
在URL字符串中，如果百分号%后面跟了两个十六进制数字，那么它表示相应ASCII值所对应的字符，如%2F表示'/'，%32表示'2'。
%编码还可以进行嵌套，如%%32F可以解码成%2F，再进一步解码成/。如果没有任何百分号后面跟的是两个十六进制数字则无法再进行解码。
"""

n = input("")
for j in range(int(n)):
    strs = input()
    n = len(strs)
    s = strs[::-1]
    stack = []
    for i in s:
        stack.append(i)
        if i == '%':
            c = '%'
            while c == '%':
                stack.pop()
                # if len(stack) < 2:
                #     break
                data_0 = stack.pop()
                data_1 = stack.pop()
                c = chr(int("" + data_0 + data_1, 16))
                stack.append(c)
    print("".join(stack[::-1]))

