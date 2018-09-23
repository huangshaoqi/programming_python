from functools import partial

"""
partial 偏函数使用
在函数调用前已知其中一个函数参数，其他参数是在函数调用后才知道，
可以使用偏函数在函数调用后，再将其余参数赋值给函数
"""


def my_add(a, b):
    return a + b


par1 = partial(my_add, 100)
print(par1(100))
