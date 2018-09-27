from multiprocessing import Process, Pool
import time, random


def fun(i):
    print("子进程启动--%s" % i)
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time() - start
    print("子进程结束--%s，消耗时间为：%0.2f" % (i, end))


if __name__ == '__main__':
    print("父进程启动--")

    pp = Pool(4)

    for i in range(10):
        pp.apply_async(fun, args=(i,))
    pp.close()
    pp.join()
    print("父进程结束--")
