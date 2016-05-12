#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
 
PORT = int(raw_input("Listen on port: "))
HOST = raw_input("Listen on host: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST, PORT))
except socket.error as msg:
    print 'Failed to bind port: ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit(0)
 
sock.listen(0)
conn = None
characterArray = []

while 1:
    try:
        if not conn:
            conn, addr = sock.accept()
            print 'Connection incoming from ' + addr[0] + ':' + str(addr[1])
            conn.send("Connected to " + str(socket.gethostbyname(socket.gethostname())) + "\r\n\r\nInput: ")
        incData = conn.recv(512)
        if incData:
            if incData[-2:] != "\r\n":
                characterArray.append(incData)
                print "Received " + repr(incData)
            else:
                characterArray.append(incData)
                conn.send("Received message: " + ''.join(characterArray) + "\r\nInput: ")
                print("Received message: " + repr(''.join(characterArray)))
                characterArray = []

    except:
        if conn:
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sys.exit("Port un-bound. Exiting...")