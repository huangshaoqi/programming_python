"""
九九乘法表，for循环
"""
# 正左三角
print("#" * 46 + "正左三角" + "#" * 46)
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%s x %s = %-2d" % (i, j, i * j), end=" ")
    print()

# 倒左三角
print("#" * 46 + "倒左三角" + "#" * 46)
for a in reversed(range(1, 10)):
    for b in range(1, a + 1):
        print("%s x %s = %-2d" % (a, b, a * b), end=" ")
    print()

# 正右三角
print("#" * 46 + "正右三角" + "#" * 46)
for m in range(1, 10):
    for k in reversed(range(1, 10 - m)):
        print(end=" " * 11)
    for n in reversed(range(1, m + 1)):
        print("%s x %s = %-2d" % (m, n, m * n), end=" ")
    print()

# 倒右三角
print("#" * 46 + "倒右三角" + "#" * 46)
for i in reversed(range(1, 10)):
    for k in range(1, 10 - i):
        print(end=" " * 11)
    for j in reversed(range(1, i + 1)):
        print("%s x %s = %-2d" % (i, j, i * j), end=" ")
    print()
