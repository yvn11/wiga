#!/usr/bin/python
# wigaclient.py
# Author: Zex

from wigabasic import *

def main():

  try:
		sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, err:
		print 'Fail on creating socket: [', str(err[0]), '], ', err[1]
		sys.exit()

	address = socket.gethostbyname(host)
	print host, 'is at', address

	try:
		sk.connect((host, port))
	except socket.error, err:
		print 'Fail on connecting to remote server: [', str(err[0]), '], ', err[1]
		sk.close()
		sys.exit()

	print 'Remote server: [', sk.getpeername(), ']'

#	message = 'Saying Hi~'
	message = 'quit'
	sk.send(message)
	reply = sk.recv(read_buf_size)
	print 'Reply: [', reply, ']'

	sk.close()

if __name__ == '__main__':
	main()
