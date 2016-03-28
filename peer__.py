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

name=raw_input("enter your name:")

myport=int(raw_input("enter the listening port:"))
my_add=("0.0.0.0",myport)

key=1	
message=""
string1=""
phrase=""
key_i=1

s_add=()
s_add=my_add
sock=socket.socket()
sock.bind(my_add)
sock.listen(20)
socklist=[sock]

connection,add1=sock.accept()
message=connection.recv(200)
phrase,string1=pickle.loads(message)
if phrase=="connect":
	add=pickle.loads(string1)
	print add
	connection.sendall(pickle.dumps(s_add))
	s_add=add
	n_sock=socket.socket()
	n_sock.connect(add)
	n_sock.sendall(str(key))
	key=key+1
	#socklist.append(n_sock)




while True:
	try:
		inputr,outputr,errorr=select.select(socklist,[],[],0.5)
	except:
		print "someone exited"
		socklist=inputr=[sock]
	if inputr:
		for obj in inputr:
			if obj==sock:
				connection,add=sock.accept()
				message=grecv(connection)
				phrase,string1=pickle.loads(message)
				if phrase=="connect":
					add=pickle.loads(string1)
					connection.sendall(pickle.dumps(s_add))
					s_add=add
					print add
					n_sock.close()
					n_sock=socket.socket()
					n_sock.connect(add)
					n_sock.sendall(str(key))
					key=key+1
					#socklist.append(n_sock)
				else:
					socklist.append(connection)
			else:
				try:
					message=grecv(obj)
					key_i,string1=pickle.loads(message)
					if key_i != key:
						print string1
						n_sock.sendall(message)
				except:
					message=None
					#print "did not receive"
					
					
								
	try:	
		string1=getin()
		#print string1
		string1=name+":"+string1
		n_sock.sendall(pickle.dumps((key,string1)))
	except:
		#print "did not get input"
		string1=None
				
