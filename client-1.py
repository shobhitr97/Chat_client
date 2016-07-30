#!/usr/bin/env python
import sys
import socket
import time
sock=socket.socket()
global ch
ch=0                                                   # need to set timeout everywhere
server_address=("0.0.0.0",3150)
str1=raw_input("enter your name:")
while True:
	sock=socket.socket()
	sock.connect(server_address)
	global ch                 			#to alternate between sending and receiving at two different ports
	try:
		if ch:
			data=sock.recv(200)
			if data:
				print "-",data
			ch=0
		else:
			message=raw_input("->")
			if message:
				sock.sendall(str1+":"+message)
				ch=1
	except:
		print("Unable to do sending and receiving\n")
	sock.close()
