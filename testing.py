#!/usr/bin/env python
p="kamikaze"
p+="&"
k=13233
p+=str(k)
t=0
t=p.find("&")
print p[0:t]
c=int(p[(t+1):])
print c;
'''print "hey you"
