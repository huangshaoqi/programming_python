from multiprocessing import Process

num = 100


def run1():
    print("孙子进程开始...")
    print("孙子进程结束...%s" % (num))


def run():
    print("子进程开始...")
    global num
    num += 1
    print(num)
    p1 = Process(target=run1)
    p1.start()
    print("子进程结束...")


if __name__ == '__main__':
    print("父进程开始...")
    num += 1
    p = Process(target=run)
    p.start()
    p.join()
    # 所有进程对全局变量的修改  都不会影响其它进程
    #  我们在进程中修改全局变量的时候  其实是对全局变量做了一个备份
    print("父进程结束...%s" % (num))
