# -*- coding:utf-8 -*-
"""
九九乘法表，while循环
"""
# 倒右三角
print("#" * 46 + "倒右三角" + "#" * 46)
i = 9
while i >= 1:
    k = 9
    while k > i:
        print("", end=' ' * 11)
        k -= 1
    j = i
    while 0 < j <= i:
        print("%s x %s = %-2d" % (j, i, j * i), end=' ' * 1)
        j -= 1
    print()
    i -= 1

# 倒左三角
print("#" * 46 + "倒左三角" + "#" * 46)
i = 9
while i >= 1:
    j = 1
    while j <= i:
        print("%s x %s = %-2d" % (i, j, j * i), end=' ' * 1)
        j += 1
    print()
    i -= 1

# 正左三角
print("#" * 46 + "正左三角" + "#" * 46)
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%s x %s = %-2d" % (i, j, i * j), end=" ")
        j += 1
    print()
    i += 1

# 正右三角
print("#" * 46 + "正右三角" + "#" * 46)
i = 1
while i <= 9:
    k = 9
    while k > i:
        print(end=" " * 11)
        k -= 1
    j = i
    while 0 < j <= i:
        print("%s x %s = %-2d" % (i, j, i * j), end=' ')
        j -= 1
    print()
    i += 1
