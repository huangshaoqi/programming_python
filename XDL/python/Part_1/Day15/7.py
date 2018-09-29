import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(("",8888))
sock.listen(10)

while True:
	con,add = sock.accept()

	print(con)
	print(add)
	a = 1
	while a:
		print("%s 已经连接！" % add[0])

		recvs = con.recv(512)
		if recvs.decode("utf-8") == "break":
			print(recvs.decode("utf-8"))
			
			a = 0
			break
		else:
			print(recvs.decode("utf-8"))

		sends = input(">>>")
		if sends == "break":
			a = 0
			break
		else:
			con.send(sends.encode("utf-8"))
			

sock.close()