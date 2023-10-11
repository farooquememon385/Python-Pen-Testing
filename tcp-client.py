import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.1.1'
port = 4800

clientSocket.connect((host, port))
message = clientSocket.recv(1024)
clientSocket.close()
print(message.decode())