#!/usr/bin/env python
import sys
import socket
import select
server_address=("0.0.0.0",3151)
sock=socket.socket()
sock.bind(server_address)
sock.listen(50)
inputl=[sock]
while True:
	#sock_t=socket.socket()
	
	inputr,outputr,errorr=select.select(inputl,inputl,[],120.0)

	for sock_t in inputr:
		if sock_t == sock:
			(connection,client_address)=sock_t.accept()
			inputl.append(connection)
			print >> sys.stderr, 'Adding new connection'
		
		else:
			data=sock_t.recv(200)
			i=0
			if data!="exit":
				for s in outputr:
					try:
						if s==sock_t:
							continue
						else:
							s.sendall(data)
						#i=i+1
					except:
						print >> sys.stderr,'.....'#'timed out socket'
						#i=i+1
			else:
				inputl.remove(s)
				s.close()
     	
