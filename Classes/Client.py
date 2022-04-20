import socket, sys

tcpSocket = socket.create_connection(('localhost', 88)) # create connection to server
 
try:
    data = bytes('Hi. I am a TCP client sending data to the server', 'UTF-8')
    tcpSocket.sendall(data)
 
finally:
    print("Closing socket") # closing the socket
    tcpSocket.close()