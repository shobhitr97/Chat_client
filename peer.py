#!usr/bin/env python 
import sys,socket,select,pickle
import time
from timeout import timeout

@timeout(1)
def getin():
	m=""
	m=raw_input()			#"->")
	return m

@timeout(1)
def grecv(socket):
	message=""
	message=socket.recv(200)
	return message			

ticks=time.time()

name=raw_input("enter your name:")

port1=int(raw_input("enter your port:"))
my_add1=("0.0.0.0",port1)

port=int(raw_input("enter the port to be requested:"))
the_add=("0.0.0.0",port)

message=""
socklist=[]
key=1							#we have to give the key
string1=""
k=""
s=()                         #the address of the successor
s_s=()			     #the address of successor of successor
#to the predecessor and new peers
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
print "the successor:"
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
r_sock.sendall(pickle.dumps(("to_successor","")))
message=grecv(r_sock)
s_s=pickle.loads(message)
print "the succcessor to successor - "
print s_s

while True:

	inputr,outputr,errorr=select.select(socklist,[],[],2.0)
	'''except :
		print "something went wrong"
		socklist=inputr=[s_sock]
'''
	if inputr:
		for t in inputr:
			if t==s_sock:		
				connection,address=t.accept()
				message=connection.recv(200)
				connection.sendall(pickle.dumps(s))
				socklist.append(connection)
				print "the predecessor -"
				print address
			else:
				try:
					message=grecv(t)
					if message!="#":
						key_i,string1=pickle.loads(message)
						if key_i != key:
							print string1
							try:
								r_sock.sendall(message)
							except:
									print "peer removed"
									#r_sock.close()
									r_sock=socket.socket()
									print "connecting to - "
									print s_s
									r_sock.connect(s_s)
									#socklist.append(r_sock)
									s=s_s
									if s_s!=the_add:
										r_sock.sendall(str(key-2))
										message=r_sock.recv(200)
										s_s=pickle.loads(message)
										print "removed:"
										print s_s
										print "added:"
										print s
									else:
										r_sock.sendall(pickle.dumps(("no","")))
										message=r_sock.recv(200)
										s_s=pickle.loads(message)

					#else:
					#	print "\n received # \n"

				except:
					message=None
					
								
	try:	
		string1=getin()
		#print string1
		string1=name+":"+string1
		#r_sock.sendall(pickle.dumps((key,string1)))
	except:
		#print "did not get input"
		string1=None
	
	try:
		if string1:
			r_sock.sendall(pickle.dumps((key,string1)))
		
		tick=time.time()
		if tick-ticks> 10:
			r_sock.sendall("#")
			ticks=tick
			#print tick
			'''print "successor:"
			print s
			print "successor to successor"
			print s_s'''
			
			#print "sent #" 		
	except:
		print "peer removed"
		#sockist.remove(r_sock)
		r_sock=socket.socket()
		print "connecting to - "
		print s_s
		r_sock.connect(s_s)
		#socklist.append(r_sock)
		s=s_s
		if s_s!=the_add:
			r_sock.sendall(str(key-2))
			message=r_sock.recv(200)
			s_s=pickle.loads(message)
			print "removed:"
			print s_s
			print "added:"
			print s
		else:
			r_sock.sendall(pickle.dumps(("no","")))
			message=r_sock.recv(200)
			s_s=pickle.loads(message)
		










						
