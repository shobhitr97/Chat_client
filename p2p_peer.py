#!/usr/bin/env python
from timeout import timeout
import socket
import pickle
import sys
import select
@timeout(1.0)
def grecv(Socket):
	message=Socket.recv(200)
	return message

@timeout(1.0)
def takeinput():
	p=raw_input("->")
	return p

name=raw_input("enter your name:")
port=int(raw_input("enter a port no.:"))
myaddress=("0.0.0.0",port)
tracker_address=("0.0.0.0",3151)
psock=socket.socket()
psock.connect(tracker_address)
psock.sendall(pickle.dumps(myaddress))
s=""
listp=[]
s=psock.recv(200)
listp=pickle.loads(s)
psock.close()
print listp
nsock=socket.socket()
nsock.bind(myaddress)


'''rsock=socket.socket()
rsock.bind(myaddress)
rsock.listen(20)
socklist=[rsock]'''
nsock.listen(20)
socklist=[nsock]


for p in listp:
	print p
	sock=socket.socket()
	sock.connect(p)
	socklist.append(sock)

while True:
	
	inputr,outputr,errorr=select.select(socklist,socklist,[],60.0)
	print inputr
	#also include the code for entry and exit
	for s in inputr:
		if s==nsock:
			connection,address=nsock.accept()
			socklist.append(connection)
			listp.append(address)
		else:
			message=grecv(s)
			if message!="exit":
				print message
			else:
				socklist.remove(s)
				try:
					outputr.remove(s)
				except:
					ch=1
			try:
				message=takeinput()
			except:
				message=""
			if message:
				if message!="exit":
					message=name+":"+message
				for k in outputr:
					k.sendall(message)
						
			#notify the tracker
				





















		                                           
