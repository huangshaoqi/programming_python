#
# def fu(n):
#     if n == 1:
#         return 1
#     else:
#         return fu(n-1) + n
#
# print(fu(100))
# print(sum(range(101)))
#
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return jc(n-1) * n
#
# print(jc(3))
#
# # 1,1,2,3,5,8
# def fun(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fun(n-2) + fun(n-1)
#
# print(fun(4))

"""
汉诺塔游戏
"""
m = 0


def hannota(n, a, b, c):
    global m
    if n == 1:
        print(a, "-->", c)
        m += 1
    else:
        hannota(n - 1, a, c, b)
        print(a, "-->", c)
        m += 1
        hannota(n - 1, b, a, c)
    return "总共移动%s次" % m


print(hannota(15, "a", "b", "c"))
print(pow(2, 64) - 1)
