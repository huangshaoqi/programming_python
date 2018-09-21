L = ["JaCk", "LoseR", "jEEry", "pYthOn"]


def myfunc1(x):
    return x.title()


list1 = list(map(myfunc1, L))
print(list1)

var = "1ab2cde456f8"

from functools import reduce


def myfunc2(x):
    if x.isdigit():
        return x
    else:
        return ""


# list1 = list(map(myfunc2,var))
#
# int1 = int("".join(list1))
# print(int1)


def myfunc3(x, y):
    return 10 * int(x) + int(y)


int1 = reduce(myfunc3, "".join(list(map(myfunc2, var))))
print(int1)
