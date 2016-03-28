#!usr/bin/env python 
import sys,socket,select,pickle
from timeout import timeout

@timeout(1)
def getin():
	m=""
	m=raw_input()#"->")
	return m

@timeout(1)
def grecv(socket):
	message=""
	message=socket.recv(200)
	return message



port=int(raw_input("enter the port to be requested:"))
the_add=("0.0.0.0",port)

name=raw_input("enter your name:")

port1=int(raw_input("enter your port:"))
my_add1=("0.0.0.0",port1)
message=""
socklist=[]
key=1							#we have to give the key
string1=""
k=""

#to the predecessor
s_sock=socket.socket()
s_sock.bind(my_add1)
s_sock.listen(20)
socklist=[s_sock]

#to get the address of the successor peer 
sock=socket.socket()
sock.connect(the_add)
sock.sendall(pickle.dumps(("connect",pickle.dumps(my_add1))))
message=sock.recv(200)
s=pickle.loads(message)
print s
sock.close()

#to the predecessor
connection,address=s_sock.accept()
key=int(connection.recv(200))
socklist.append(connection)


#assign a key

#to the successor
r_sock=socket.socket()
r_sock.connect(s)
#k=r_sock.recv(200)                              #spam - not of any use
r_sock.sendall(pickle.dumps(("to_successor","")))		#any message can be used instead of k
#socklist.append(r_sock)


while True:
	try:
		inputr,outputr,errorr=select.select(socklist,[],[],2.0)
	except :
		print "something went wrong"
		socklist=inputr=[s_sock]
	if inputr:
		for t in inputr:
			if t==s_sock:
				connection,address=s_sock.accept()
				message=grecv(connection)
				socklist.append(connection)
			else:
				try:
					message=grecv(t)
					key_i,string1=pickle.loads(message)
					if key_i != key:
						print string1
						r_sock.sendall(message)#pickle.dumps((key_i,string1)))
				except:
					message=None
					
								
	try:	
		string1=getin()
		#print string1
		string1=name+":"+string1
		r_sock.sendall(pickle.dumps((key,string1)))
	except:
		#print "did not get input"
		string1=None











						
