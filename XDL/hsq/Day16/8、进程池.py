from multiprocessing import Pool, Process
import time, random


def func(name):
    print("子进程%s启动..." % (name))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time() - start
    print("子进程%s结束...耗时%.2f" % (name, end))


if __name__ == '__main__':
    print("父进程启动...")
    # 创建一个进程池
    pp = Pool(10)
    for i in range(20):
        # 创建进程
        pp.apply_async(func, args=(i,))
    # 进程池关闭    进程池一旦关闭  就不能再添加新的进程了
    pp.close()
    # 进程池调用join，等待进程池中的所有进程结束之后再结束父进程
    pp.join()
    print("父进程结束...")
