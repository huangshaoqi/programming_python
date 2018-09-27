import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sock.connect(("192.168.15.10"))
sends = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:python-15"
for i in range(1, 255):
    ip = "192.168.15.%d" % (i)
    print(ip)
    sock.sendto(sends.encode("gbk"), (ip, 2425))
sock.close()
