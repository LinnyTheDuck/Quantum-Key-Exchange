import socket, sys

class Server:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
        self.socket.bind((host, port)) # bind socket
        self.socket.listen(1) # listen, only allows 1 connection
    
    def accept(self):
        self.stream, addr = self.socket.accept() # client accepts connection
        print("CONNECTION FROM:", str(addr)) # connection sucsessful, display client addr

    def send(self, message):
        self.stream.send(message.encode()) # send message to client

    def close(self):
        self.stream.close() # disconnect the server