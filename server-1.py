#!/usr/bin/env python
import sys
import socket
count=-1
m=0
p=int(raw_input("enter the number of clients:"))
n=0
_list=[]
server_address=("0.0.0.0",3150)
sock=socket.socket()
sock.bind(server_address)
sock.listen(50)
while True:
	print >> sys.stderr , 'Waiting for connection.....'					#add timeout
	(connection,client_address)=sock.accept()
	data=connection.recv(200)
	if data:
		_list.append(data)
		m=m+1
	if n==0:
		if count+1<=m:
			if _list[count+1] :
				count=count+1
			n=p-1  									#n=2-1  because with n-2 it does not go n-- and hence the program sends the same message thrice
	else:
		n=n-1
	connection.sendall(_list[count])	
	connection.close()
