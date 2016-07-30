#!/usr/bin/env python

import socket 
import pickle
import sys

sock=socket.socket()
tracker_address=("0.0.0.0",3151)
sock.connect(tracker_address)
sock.sendall("enter")
listp=[]
address=tracker_address
p=sock.recv(200)
listp=pickle.loads(p)
print listp

