import socket 
import sys

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #sock stream is a type for tcp 
except socket.error , msg:
	print 'Failed to create socket Error code' + str(msg[0]) + 'Error message ' +msg[1]
	sys.exit()

print 'Socket Created'

host = "localhost" #here we provide the server ip that is running the server side of the socket
port = 5000
try:
	remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    #could not resolve host
    print 'hostname not resolved'
    sys.exit()

print 'Ip address of ' + host + 'is' + remote_ip
s.connect((remote_ip,port))
print 'Socket connected to ' + host + 'on ip ' + remote_ip

#sending data
message = "Hello world from client"

try:
	s.sendall(message)
except  socket.error:
	print 'Send failed'
	sys.exit()

print 'Message send successfully' 

#recieveing data
reply = s.recv(4096)

print reply

s.close()