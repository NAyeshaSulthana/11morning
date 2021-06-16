# socket::socket is the module to connect server and client which runs continously to show actions..
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.bind((socket.gethostname(),1234))

client.listen(5)

while True:
	sc1,ip_address = client.accept()
	print("Connection Established with {}".format(ip_address))

	sc1.send(bytes("Welcome to Digital Lync",'utf-8'))

	sc1.close()