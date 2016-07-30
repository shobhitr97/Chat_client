#!/usr/bin/env python
#filename :learn.server.py
import socket
import sys

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
localhost="0.0.0.0"
server_address=(localhost,3151)
print >> sys.stderr, 'starting up on %s port %s ' % server_address
sock.bind(server_address)
sock.listen(10)
message="play hard or go home"
# add a while loop for continuous chat
while True:
	#sock.listen(10)
	print >> sys.stderr ,'waiting for a connection'
	(connection,client_address)=sock.accept() #sock.accept returns a socket object and an address in a tuple
	
	#print >>sys.stderr, 'connection from %s ' % client_address
	while True:
		data=connection.recv(200)
		print >>sys.stderr, 'C:%s' % data
		if data:
			message=data
			connection.sendall(message)
		#print >> sys.stderr, 'no more data from client ' % client_address
		else:
			print >>sys.stderr ,'closing this connection'				
			connection.close()		
			break
		
