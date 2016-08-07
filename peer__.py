#!usr/bin/env python
import sys,socket,select,pickle
import time
from timeout import timeout


#Now i have to pass a message that can be that can recognize if the peer is active or not
#So in the starting only I must know the address of the successor of the successor so that i can establish a connection with the next peer in case of failure of immediate successor


@timeout(1)          #decorator	
def getin():
	m=""
	m=raw_input()#"->")
	return m

@timeout(1)	
def grecv(socket):
	message=""
	message=socket.recv(200)
	return message
#note:add address of the deleted node
def notify_tracker(add):
	new_socket=socket.socket()
	new_socket.connect(tracker_add)
	new_socket.sendall(pickle.dumps(add))


ticks=time.time()
name=raw_input("enter your name:")

myport=int(raw_input("enter the listening port:"))
my_add=("0.0.0.0",myport)

#tracker_port=int(raw_input("enter tracker port:"))
#tracker_add=("0.0.0.0",tracker_port)

key=1	
message=""
string1=""
phrase=""
key_i=1
s_add=()
s_s_add=()

s_add=my_add
s_s_add=s_add
sock=socket.socket()
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
	n_sock=socket.socket()
	n_sock.connect(add)
	n_sock.sendall(str(key))
	key=key+1
	#socklist.append(n_sock)

'''
#to add new peer to the tracker's list
n_sock=socket.socket()
n_sock.connect(tracker_add)
n_sock.sendall(pickle.dumps(my_add))
message=n_sock.recv(200)
p_add=pickle.loads(message)
n_sock.close()

#to get the address of the successor peer 
n_sock=socket.socket()
n_sock.connect(p_add)
n_sock.sendall(pickle.dumps(("connect",pickle.dumps(my_add))))
message=n_sock.recv(200)
s=pickle.loads(message)
print "the successor:"
print s_add
n_sock.close()

#to the predecessor
connection,address=sock.accept()
key=int(connection.recv(200))
socklist.append(connection)
'''

#assign a key

#to the successor
n_sock=socket.socket()
n_sock.connect(s_add)
n_sock.sendall(str(key))
key=key+1

while True:
	#try:
	inputr,outputr,errorr=select.select(socklist,[],[],2.0)

	if inputr:
		for obj in inputr:
			if obj==sock:
				connection,add=sock.accept()
				message=connection.recv(200)
				phrase,string1=pickle.loads(message)
				if phrase=="connect":
					add=pickle.loads(string1)
					connection.sendall(pickle.dumps(s_add))
					s_s_add=s_add
					s_add=add
					print "the successor address: "
					print s_add
					n_sock.close()
					n_sock=socket.socket()
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
							try:
								n_sock.sendall(message)
							except:
								if s_s_add!=my_add:
									print "peer removed"
									#notify_tracker(s_add)
									#n_sock.close()
									n_sock=socket.socket()
									n_sock.connect(s_s_add)
									#socklist.append(n_sock)
									s_add=s_s_add
									n_sock.sendall(str(key-2))
									message=n_sock.recv(200)
									s_s_add=pickle.loads(message)
									print "removed:"
									print s_s_add
									print "added:"
									print s_add
								
							#print string1
					#else:
					#	print "\n received # \n"
			
					
				except:
					message=None
					#print "did not receive"
					
	try:	
		string1=getin()
		#print string1
		string1=name+":"+string1
	
	except:
		string1=None

	#except:
	#	print "someone exited"
	

	try:
		if string1:
			n_sock.sendall(pickle.dumps((key,string1)))
		
		tick=time.time()
		if tick-ticks > 10:
			n_sock.sendall("#")
			ticks=tick
			#	print tick
			'''print "successor:"
			print s_add
			print "successor to successor"
			print s_s_add'''
			
			#print " sent #"
				
	except:
		if s_s_add!=my_add:
			print "peer removed"
			print "removed:"
			print s_add
			print "added:"
			print s_s_add
			#socklist.remove(n_sock)
			n_sock=socket.socket()
			n_sock.connect(s_s_add)
			socklist.append(n_sock)
			s_add=s_s_add
			n_sock.sendall(str(key-2))
			message=n_sock.recv(200)
			s_s_add=pickle.loads(message)
			print "successor to succcessor"
			print s_s_add
		#notify_tracker()






#in this case two consecutive peers can not exit
