#!/usr/bin/env python
import socket
import pickle
import sys
#   why were address packets earlier being recceived disoriented? in that address +"\n" +str(port)form
sock=socket.socket()
tracker_address=("0.0.0.0",3151)
sock.bind(tracker_address)
sock.listen(20)
listp=[]
k=""
while True:
	try:
		connection,address=sock.accept()
		message=connection.recv(200)
		
		try:
			k=pickle.dumps(listp)
			address=pickle.loads(message)
			listp.append(address)
			print listp
			connection.sendall(k)
		except:
			if message=="exit":
				listp.remove(address)
		'''for ob in listp:
			if ob!=address:
				qsock=socket.socket()
				qsock.connect(ob)
				k=pickle.dumps([address])
				qsock.sendall(k)
				qsock.close()	
		'''		
	finally:
		connection.close()
		
