import socket,select,string,sys

def prompt():
	sys.stdout.write('<You>')
	sys.stdout.flush()

if __name__ == "__main__":

	# if(len(sys.argv) < 3):
	# 	print 'Usage : python chatClientMain.py hostname port'
	# 	sys.exit()

	host = 'localhost'
	port = 5000

	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.settimeout(2) #timeout time

	try:
		s.connect((host,port))
	except:
		print 'Unable to connect'
		sys.exit()

	print 'Connected to remote host . Start sending messages'
	prompt()

	while 1:
		socket_list = [s]

		#Get the list of sockets that are readable
		read_sockets , write_sockets , error_sockets = select.select(socket_list , [] , [])

		for sock in read_sockets:
			#incoming messages from server
			if sock == s:
				data = sock.recv(4096)
				if not data:
					print '\n Disconnected from chat server'
					sys.exit()
				else:
					#print data
					sys.stdout.write(data)
					prompt()
			else:
				msg = sys.stdin.readline()
				s.send(msg)
				promt()




