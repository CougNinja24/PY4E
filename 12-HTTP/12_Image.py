import socket as S
import time as T

HOST,PORT = 'data.pr4e.org',80
mysock = S.socket(S.AF_INET,S.SOCK_STREAM)
mysock.connect((HOST,PORT))

count,picstring = 0, b''
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')

while True:
    data = mysock.recv(5120)
    if len(data) < 1:
        break
    #T.sleep(0.25) #Give enough time for data to download
    count = count + len(data) # data in bytes to add to picture string
    print('length of data : {}, count = {}'.format(len(data),count))
    picstring += data #Keep adding the newest data to string
    
mysock.close() #Close after loop and socket have finished


    

