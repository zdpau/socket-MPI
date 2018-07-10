import socket
import time
import sys
import argparse
import util


parser = argparse.ArgumentParser(description="ping server")
parser.add_argument('--port', type=int, help='server port number',  default=3000)

def pingpong_handler(s):
    size = util.recvInt(s)
    times = util.recvInt(s)
    print ('data size = {}'.format(size))
    print ('times = {}'.format(times))
    data = b'x' * size
    for _ in range(times):
        util.recvall(s, size)
        s.sendall(data)


def main():
    args = parser.parse_args()
    util.server(args.port, pingpong_handler)

if __name__ == '__main__':
    main()
