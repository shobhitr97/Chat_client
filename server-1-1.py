#!/usr/bin/env python
import sys
import socket
socks=socket.socket()
sockr=socket.socket()
server_addresss=("0.0.0.0",3150)
server_addressr=("0.0.0.0",3151)
socks.bind(server_addresss)
sockr.bind(server_addressr)
socks.listen(20)
sockr.listen(25)

