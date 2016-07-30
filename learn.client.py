#!/usr/bin/env python
import socket
import sys
#sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname="0.0.0.0"
server_address=(hostname,3151)
print >>sys.stderr , 'connection to %s port %s' % server_address
sock = socket.create_connection(server_address, timeout=10)
sock.settimeout(10.0)
# add while for continuous chat 

try:    
	while True:
		message=raw_input("->")
		sock.sendall(message)
		data=sock.recv(200)
		if data:
			print>> sys.stderr ,'S:%s'% data
finally:
	print >>sys.stderr ,'closing socket'
	sock.close()	
