#!/usr/bin/python3
import socket

# AF_INET for IPV4
# SOCK_STREAM for TCP
# SOCK_DGRAM for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind, listen, accept, send, recieve, close

host = socket.gethostbyname(socket.gethostname())
port = 4800
print(host)
sock.bind((host,port))
sock.listen(4)
while True:
    clientSock, address = sock.accept()

    print("recieved connection request from " % str(address))

    message = "Thanks for connecting" + '\r\n'
    
    clientSock.send(message.encode())

    clientSock.close()