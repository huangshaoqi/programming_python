import time


def func():
    while True:
        print("this is a process2")
        time.sleep(1.5)


if __name__ == '__main__':
    while True:
        print("this is a process1")
        time.sleep(1)

    func()
