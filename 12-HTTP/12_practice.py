import socket

S = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP Connection, standard AF_INET type
S.connect(('data.pr4e.org', 80))  #connect to given the socket a host and port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()  #Get Request command
#cmd2 = 'GET http://data.pr4e.org/romeo.txt '.encode()


S.send(cmd) #Send the initial request, recv function receives.

while True:
	data = S.recv(512) # Recieved in 512 bit chucks
	if len(data) < 1:
		break
	print(data.decode(),end='')

S.close()

