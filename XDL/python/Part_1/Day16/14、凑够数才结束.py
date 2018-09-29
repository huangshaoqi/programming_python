import threading, time

sem = threading.Semaphore(10)
bar = threading.Barrier(10)


def run():
    with sem:
        print("%s--start..." % (threading.current_thread().name))
        time.sleep(1)
        bar.wait()
        print("%s--end..." % (threading.current_thread().name))


if __name__ == '__main__':
    for i in range(21):
        t = threading.Thread(target=run)
        t.start()
