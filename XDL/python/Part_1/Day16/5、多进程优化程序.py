from multiprocessing import Process
import time, os


def func():
    while True:
        print("我启动了...")
        time.sleep(1)


def foo(str1):
    # os.getpid()  获取当前进程号
    # os.getppid() 获取父进程号
    p1 = Process(target=func)
    p1.start()
    while True:
        print("this is process2--%s--%s--%s" % (os.getpid(), os.getppid(), str1))
        time.sleep(5)


if __name__ == '__main__':
    print("主进程启动...--%s--%s" % (os.getpid(), os.getppid()))
    # 创建一个新的进程
    # target 表明进程任务
    # args   给进程函数传参
    p = Process(target=foo, args=("python",))
    # 启动子进程
    p.start()
    while True:
        print("this is a process1")
        time.sleep(1)
