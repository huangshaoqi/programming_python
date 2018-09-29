import time


def outer(fn):
    def inner():
        start = time.time()
        fn()
        run = time.time() - start
        print(run)

    return inner


@outer  # @ 就叫装饰器 ---> 语法糖
def func():
    for i in range(9999999):
        pass
    print("hello")


func()  # ===> inner()

# func = outer(func)()
