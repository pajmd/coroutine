#!/usr/bin/env python

from socket import *
import threading


def echo_server(addr_port):
	'''
	sever using threads
	'''	
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(addr_port)
	sock.listen(1)
	while True:
		client, client_port = sock.accept()
		print('Connection from ', client_port)
		t= threading.Thread(target = echo_handler, args=(client,))
		t.start()

def echo_handler(client):
	while True:
		data = client.recv(1000)
		if not data:
			break
		client.sendall('Got: '+data)
	print('Connection closed')
	client.close()

if __name__ == '__main__':
	echo_server(('',8000))