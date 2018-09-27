from multiprocessing import Process
import time


def func():
    print("子进程启动...")
    time.sleep(1)
    print("子进程结束...")


# 主程序在此处启动
if __name__ == '__main__':
    print("父进程启动...")
    p = Process(target=func)
    p.start()
    # p.join()  让父进程等待子进程结束之后父进程再结束
    # timeout  等待超时
    p.join()
    time.sleep(0.5)
    print("父进程结束...")
