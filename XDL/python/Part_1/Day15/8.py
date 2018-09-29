import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(("127.0.0.1",8888))
print(sock)
while True:

	sends = input(">>>")
	if sends == "break":

		sock.send(sends.encode("utf-8"))

		recvs = sock.recv(512)
		break
	else:
		sock.send(sends.encode("utf-8"))

		recvs = sock.recv(512)

		print(recvs.decode("utf-8"))

socket.close()