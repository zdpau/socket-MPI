import socket
import time
import sys
import struct
import argparse

BUFSIZE=4096

def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def server(port, handler):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    print('Server ready...')
    while True:
        conn, address = s.accept()
        print('Connected by:', conn, address)
        handler(conn)        

def recvInt(s):
    return socket.ntohl(struct.unpack('I', recv4bytes(s))[0])
    
def sendInt(s, data):
    s.sendall(struct.pack('I', socket.htonl(data)))
    

def recv4bytes(s):
    buf = b""
    while len(buf) < 4:
        tmp = s.recv(4-len(buf))
        buf += tmp
    return buf
        
def recvall(s, size):
    recvd = 0
    while recvd < size:
        buf = s.recv(BUFSIZE)
        recvd += len(buf)

