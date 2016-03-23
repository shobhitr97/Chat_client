#!/usr/bin/env python
import sys
from timeout import timeout
import socket
import pickle
import select

name=raw_input("enter your name:")
tport=int(raw_input("enter tracker port:"))
port=int(raw_input("enter a port no.:"))
myaddress=("0.0.0.0",port)
tracker_address=("0.0.0.0",tport)

psock=socket.socket()          #socket.AF_INET,socket.SOCK_STREAM)
psock.connect(tracker_address)

x=""
x=pickle.dumps(myaddress)	
psock.sendall(x)

s=""
listp=[]

s=psock.recv(200)
listp=pickle.loads(s)
#psock.close()

print listp

nsock=socket.socket()         #socket.AF_INET,socket.SOCK_STREAM)
nsock.bind(myaddress)
nsock.listen(20)
socklist=[nsock]


for p in listp:
	print p
	sock=socket.socket()  #socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(p)
	socklist.append(sock)

@timeout(1)                                       #don't use floating numbers
def takeinput():
	p=raw_input()
	return p

@timeout(1)                                       #don't use floating numbers
def grecv(Socket):	
	m=""
	m=Socket.recv(200)
	return m


while True:
	inputr,outputr,errorr=select.select(socklist,socklist,[],120.0)
	for s in inputr:
		if s!=nsock:
			try:
				message=grecv(s)
			except:
				message=None
			if message:
				if message!="exit":
					print message
				else:
					socklist.remove(s)
					s.close()
		else:
			print "adding connection"
			connection,address=nsock.accept()
			print address
			socklist.append(connection)
			#listp.append(address)       as this will not affect the working of code we don't need the list after addition
	
	try: 	
		mess=takeinput()
	except:
		mess=None
	if mess:
		if mess!="exit":
			mess=name+":"+mess
		for k in outputr:
			if k!=nsock:
				k.sendall(mess)
		if mess=="exit":
			sok_t=socket.socket()
			sok_t.connect(tracker_address)
			sok_t.sendall(pickle.dumps(myaddress))
			break
			#notify the tracker
				





















		                                           
