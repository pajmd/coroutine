'''
sever using threads
'''

from socket import *
import asyncio


async def echo_server(addr_port, loop):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(addr_port)
	sock.listen(1)
	sock.setblocking(False)
	while True:
		client, client_port = await loop.sock_accept(sock)
		print('Connection from ', client_port)
		loop.create_task(echo_handler(client, loop))


async def echo_handler(client, loop):
	while True:
		data = await loop.sock_recv(client, 1000)
		if not data:
			break
		await loop.sock_sendall(client, b'Got: '+data) # to convert to bytes
	print('Connection closed')
	client.close()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(echo_server(('',8000), loop))
