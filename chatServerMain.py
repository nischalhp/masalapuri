import socket , select

#to do:
#shall store these messages wrt to user on mongo
#need to build chat client ui that picks up info from mongo
#when all online , need to show their names and their status

#doing:
#when the server recieves a message it sends it to everybody who is connected

def broadcast_data(sock,message):
	#should not send message to master socket and the client who has send us the message
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != sock:
			try :
				socket.send(message)
			except :
				#socket conencted may be broken or they pressed ctrl + c
				socket.close()
				CONNECTION_LIST.remove(socket)


if __name__ == "__main__":

	CONNECTION_LIST = []
	RECV_BUFFER = 4096
	HOST = '' #all available interfaces
	PORT = 5000

	server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	server_socket.bind((HOST,PORT))
	server_socket.listen(5)

	#Add server socket to the list of readable connections
	CONNECTION_LIST.append(server_socket)

	print "masala puri initialized and started"

	while 1:
		#now check for which are the sockets that are ready to be read through select

		read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

		for sock in read_sockets:
			if sock == server_socket:
				#incoming new connection
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print " Client (%s,%s) connected " %addr
				broadcast_data(sockfd, "[%s:%s] entered room\n" %addr)

			else:
				#incoming new message
				try:
					data = sock.recv(RECV_BUFFER)
					if data:
						broadcast_data(sock, "\r" + " < " + str(sock.getpeername()) + ' >' + data)					
				except:
					broadcast_data(sock, "Client (%s,%s) is offline" %addr)
					print "Client (%s,%s) is offline" %addr
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue
        	print len(CONNECTION_LIST)
	server_socket.close()

