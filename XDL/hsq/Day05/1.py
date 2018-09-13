"""
函数
"""
"""
参数：
1.位置参数
2.关键字参数
3.默认值参数
"""
"""
全局变量与局部变量
"""
B = "我是全局变量"


def myfunc():
    global A
    A = "我是局部变量"
    print(A)
    print(B)


myfunc()
print(A)
print(B)

"""
不定长参数
"""


def myfunc1(*args, **kwargs):
    print(args, kwargs)


myfunc1(1, 2, 3, 4, 5, name='miss', age=23)

"""
闭包函数
内部函数引用外部函数的变量，称这个内部函数为闭包
外部函数的返回值 为 内部函数
"""


def outer(A):
    def inner(B):
        return A * B

    return inner


func = outer(12)
res = func(12)
print(res)
