import socket, sys

def send(message):
    tcpSocket = socket.create_connection(('localhost', 88)) # create connection to server
    
    try:
        data = bytes(message, 'UTF-8') # sends message to the server
        tcpSocket.sendall(data)
    
    finally:
        print("Closing socket") # closing the socket
        tcpSocket.close()