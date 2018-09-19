import time

n = 0
while True:
    print("▌" * (n % 100 + 1) + " %s" % (n % 100 + 1) + "%")
    n += 1
    time.sleep(0.3)
    if n == 100:
        print("下载完成！")
        break
