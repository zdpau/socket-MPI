import socket
import time
import sys
import argparse
import util


def pingpong(host, port, size):
		s = util.connect(host, port)
		n_trials = 10 if size < 100000 else 1
		util.sendInt(s, size)   # sending the number of bytes
		util.sendInt(s, n_trials)
		before = time.time()
		data = b'x' * size
		for _ in range(n_trials):
				s.sendall(data)
				util.recvall(s, size)
		after = time.time()
		return (size * n_trials) / (after - before)

parser = argparse.ArgumentParser(description="ping client")
parser.add_argument('--host', help='server host name', default='localhost')
parser.add_argument('--port', type=int, help='server port number',  default=3000)
parser.add_argument('datasize', type=int, help='data size to be transferred')

def main():
		args = parser.parse_args()
		print('Throughput = {:.2f} MiB/sec'.format(pingpong(args.host, args.port, args.datasize) / (1024 * 1024.0)))

if __name__ == "__main__":
	 main()