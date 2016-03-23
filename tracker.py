#!/usr/bin/env python
import socket
import pickle
import sys
#   why were address packets earlier being recceived disoriented? in that address +"\n" +str(port)form
port=int(raw_input("enter tracker port:"))
sock=socket.socket()#esocket.AF_INET,socket.SOCK_STREAM)
tracker_address=("0.0.0.0",port)
sock.bind(tracker_address)
sock.listen(20)
listp=[]
k=""
#p=()
ch=0
while True:
	try:
		connection,address=sock.accept()
		message=connection.recv(200)
		address=pickle.loads(message)
		ch=1
		for p in listp:
			if p==address:
				ch=0
		if ch:
			k=pickle.dumps(listp)
			listp.append(address)
			connection.sendall(k)
		else:
			listp.remove(address)
				
	finally:
		print listp
		if ch==1:
			connection.close()
		
