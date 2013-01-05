#!/usr/bin/python
# wigaserver.py
# Author: Zex

from wigabasic import *

def message_handler(connection, message):

  	print 'Message: [', message, ']'

		if message == 'quit' :
			global running
			running = False
			print 'Server: shutting down...'
		else :
			reply = 'Received message: [' + message + ']'
			connection.send(reply)
			
def main ():

	sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sk.bind((host, port))
	sk.listen(listen_backlog)
	print 'Socket name: [', sk.getsockname(), ']'
#	print 'Socket options: [', sk.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE), ']'
	print 'Server: listening...'

	global running
	running = True

	while (running) :
		connection, address = sk.accept()
		print 'Client: [', address, ']'
		message = connection.recv(read_buf_size)
		if not message: continue
		message_handler(connection, message)
		connection.close()

	print 'Server: quit...'
	sk.close()

if __name__ == '__main__':
	main()
