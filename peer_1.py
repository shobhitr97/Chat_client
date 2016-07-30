#!usr/bin/env python 
import sys,socket,select,pickle
from timeout import timeout


#Scratch the whole




@timeout(1)
def getin():
	m=""
	m=raw_input("->")
	return m
'''
port=int(raw_input("enter port number of predecessor:"))
port1=int(raw_input("enter the port number to be bound:"))
name=raw_input("enter your name:")
padd=("0.0.0.0",port)
my_add1=("0.0.0.0",port1)
my_add2=("0.0.0.0",port2)                                 #first peer will always receive the request
sadd=()'''

port=int(raw_input("enter the port to be requested:"))
the_add=("0.0.0.0",port)

name=raw_input("enter your name:")

port1=int(raw_input("enter your port:"))
my_add=("0.0.0.0",port)
message=""
socklist=[]
key=1							#we have to give the key
stri=""
k=""
'''
#to get the address of the successor peer
sock=socket.socket()
sock.connect(the_add)
message=sock.recv(200)
s=pickle.loads(message)	
sock.sendall(pickle.dumps("connect",pickle.dumps(my_add1)))
sock.close()
'''
'''
#top the predecessor
s_sock=socket.socket()
s_sock.bind(my_add)
s_sock.listen(20)
connection,address=s_sock.accept()
socklist.append(connection)
'''
#assign a key

#to the successor
r_sock=socket.socket()
r_sock.connect(s)
k=r_sock.recv(200)                              #spam - not of any use
r_sock.sendall(pickle.loads("no",k))		#any message can be used instead of k
socklist.append(r_sock)

a_sock=socket.socket()					#for new peers
a_sock.bind(my_add2)
a_sock.listen(20)
socklist.append(a_sock)
while True:
	inputr,outputr,errorr=select.select(socklist,[],[],120.0)
	if inputr:
		for t in inputr:
			if t==a_sock:
				connection,address=a_sock.accept()
				connection.sendall(pickle.dumps(s))
				phrase,message=pickle.loads(connection.recv(200))
				if phrase=="connect":
					sock=socket.socket()
					sock.connect(pickle.loads(message))
					socklist.append(sock)
			else:
				message=t.recv(200)
				key_c,stri=pickle.loads(message)
				if key_c!=key:
					print stri
					try:	
						stri=getin()
					except:
						stri=None
					if stri:
					r_sock.sendall(pickle.dumps(key,stri))					
			



















						
