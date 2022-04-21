import socket, sys

class Client:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def receive(self):
        msg = self.socket.recv(1024) # recieve string from server 1024 bytes at a time
        fullMessage = msg
        
        while msg: # repeat as long as message string not empty
            print('Received:' + msg.decode())
            fullMessage += msg # concatenate messages
            msg = self.socket.recv(1024)

        self.socket.close() # disconnect client
        return fullMessage