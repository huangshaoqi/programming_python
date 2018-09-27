import socket


# 版本号:包编号:发送者姓名:发送者主机名:命令字:附加信息（消息内容）

def send_contents(ip,data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    content = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:%s" % data
    sock.sendto(content.encode("gbk"), ((ip, 2425)))
    sock.close()

send_contents("192.168.73.87","您好")