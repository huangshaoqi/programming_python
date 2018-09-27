import threading

num = 0


def run(n):
    global num
    for i in range(1000000):
        num += n
        num -= n


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("num =", num)
