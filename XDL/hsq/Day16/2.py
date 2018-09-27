from multiprocessing import Process
import os, time


def fun():
    print("子进程开始启动\t子进程pid是： %s\t父进程pid是: %s" % (os.getpid(), os.getppid()))
    time.sleep(2)


if __name__ == '__main__':
    print("我是主进程\tpid是：%s" % os.getpid())
    for i in range(3):
        p = Process(target=fun)
        p.start()
        p.join(timeout=1)

    print("主进程结束！")
