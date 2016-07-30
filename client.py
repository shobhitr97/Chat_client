#!/usr/bin/env python
import sys
from timeout import timeout
import socket
import select
@timeout(1)
def takemes():
	message=raw_input()
	return message
server_address=("0.0.0.0",3151)
c_sock=socket.socket()
name=raw_input("enter your name:")
c_sock.connect(server_address)
@timeout(1)
def sockrecv(Socket):
	data=Socket.recv(200)
	return data
	
ch=1
while True:
	if ch:
		c_sock.sendall(name+":"+"Hello")
		ch=0
	
	try:
		data=sockrecv(c_sock)
	except:
		data=None
	#c_sock = socket.create_connection(server_address, timeout=20)
	
	#c_sock.settimeout(20.0)
	
	if data :
		print data
	#message=raw_input("->")
	try:
		message=takemes()
	except:
		message=None
	if message:
		if message!="exit":
			c_sock.sendall("\n"+name+":"+message)
		else:
			c_sock.sendall("exit")
			break
	
c_sock.close()
