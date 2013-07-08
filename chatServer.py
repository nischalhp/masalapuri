import socket
import sys
from thread import *

HOST = '' #all available interfaces
PORT = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket created'

try:
	s.bind((HOST,PORT))
except socket.error , msg:
	print 'Binding failed'
	sys.exit()

print 'Socket has been bound'

s.listen(10)

print 'server socketListening to incoming connections'

#live server - accpet connections and create separate threads for them

def clientthread(conn):
	conn.send('Welcome to masala puri. Type something and hit enter\n')
	#this keeps the thread alive forever - need to figure out a way so that 
	#i can kill this later when i close
	while True:
		data = conn.recv(1024)
		reply = "OK" + data
		if not data:
			break

		conn.sendall(reply)

	print 'came out of connection loop on server'
	conn.close()

while 1:
	conn,addr = s.accept()
	print 'Connected with client' +addr[0] + ':' + str(addr[1])

	#create thread for each connectiong 
	start_new_thread(clientthread ,( conn,))

s.close()