import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((socket.gethostname(),1234))

# message = client.recv(8)

# print(message.decode('utf-8'))

full_message=""
while True:
	message = client.recv(8)
	message = message.decode('utf-8')
	if len(message) <=0:
		break
	full_message = full_message+message

print(full_message)

a={}
for j in range(1,5):
	name=input("Enter your name:-")
	dob=input("Enter your DOB:-")
	if name in a:
		a[name]=a[name]+[dob,]
	else:
		a[name]=[dob]
print(a)
