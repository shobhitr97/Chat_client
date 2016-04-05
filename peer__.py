#!usr/bin/env python
import sys,socket,select,pickle,time
from timeout import timeout


#Now i have to pass a message that can be that can recognize if the peer is active or not
#So in the starting only I must know the address of the successor of the successor so that i can establish a connection with the next peer in case of failure of immediate successor


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


ticks=0.0
tick=0.0
name=raw_input("enter your name:")

myport=int(raw_input("enter the listening port:"))
my_add=("0.0.0.0",myport)

key=1	
message=""
string1=""
phrase=""
key_i=1
s_add=()
s_s_add=()

s_add=my_add
s_s_add=s_add
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(my_add)
sock.listen(20)
socklist=[sock]

connection,add1=sock.accept()
message=connection.recv(200)
phrase,string1=pickle.loads(message)
if phrase=="connect":
	add=pickle.loads(string1)
	print "the requesting client :"
	print add
	connection.sendall(pickle.dumps(s_add))
	s_add=add
	n_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	n_sock.connect(add)
	n_sock.sendall(str(key))
	key=key+1
	#socklist.append(n_sock)




while True:
	#try:
	inputr,outputr,errorr=select.select(socklist,[],[],0.5)

	if inputr:
		for obj in inputr:
			if obj==sock:
				connection,add=sock.accept()
				message=grecv(connection)
				phrase,string1=pickle.loads(message)
				if phrase=="connect":
					add=pickle.loads(string1)
					connection.sendall(pickle.dumps(s_add))
					s_s_add=s_add
					s_add=add
					print "the successor address: "
					print s_add
					n_sock.close()
					n_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					n_sock.connect(add)
					n_sock.sendall(str(key))
					key=key+1
					#socklist.append(n_sock)
				else:
					connection.sendall(pickle.dumps(s_add))
					socklist.append(connection)
			else:
				try:
					message=grecv(obj)
					if message!="#":
						key_i,string1=pickle.loads(message)
						if key_i != key:
							print string1
							n_sock.sendall(message)
						
							#print string1
					else:
						print "yeah"
			
					
				except:
					message=None
					#print "did not receive"
					
	try:	
		string1=getin()
		#print string1
		string1=name+":"+string1
	
	except:
		#print "did not get input"
		string1=None

	#except:
	#	print "someone exited"
	

	try:
		if string1:
			n_sock.sendall(pickle.dumps((key,string1)))
		else:
			tick=time.clock()
			if tick-ticks>10.0:
				n_sock.sendall("#")
				ticks=tick
	except:
		if my_add!=s_s_add:
			print "peer removed"
			#n_sock.close()
			n_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			n_sock.connect(s_s_add)
			socklist.append(n_sock)
			s_add=s_s_add
			n_sock.sendall(str(key-2))
			message=grecv(n_sock)
			s_s_add=pickle.loads(message)
			print "removed:"
			print s_s_add
			print "added:"
			print s_add





#in this case two consecutive peers can not exit

























				
