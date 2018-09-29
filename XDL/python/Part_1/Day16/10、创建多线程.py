import threading, time


def func(num):
    print("子线程%s开始..." % (threading.current_thread().name))
    time.sleep(2)
    print(num)
    time.sleep(2)
    print("子线程%s结束..." % (threading.current_thread().name))


if __name__ == '__main__':
    # current_thread()   获取当前线程的实例
    # current_thread().name  获取当前线程的实例属性name
    print("主线程%s启动..." % (threading.current_thread().name))
    # 创建子线程
    t = threading.Thread(target=func, args=(6,))
    t.start()
    t.join()
    print("主线程%s结束..." % (threading.current_thread().name))
