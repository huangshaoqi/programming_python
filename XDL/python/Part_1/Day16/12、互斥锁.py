import threading

# 创建一个锁对象
lock = threading.Lock()
num = 0


def run(n):
    global num
    for i in range(1000000):
        """
        # 线程一旦进入循环立即加锁
        # 加锁  为了确保锁中的代码只能由一个线程从头到尾的执行
        # 会阻止多线程的并发执行,所以效率会大大降低
        lock.acquire()
        try:
            num += n
            num -= n
        # 计算完毕之后一定要解锁
        finally:
            lock.release()
        """
        with lock:
            num += n
            num -= n


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    print("num =", num)
