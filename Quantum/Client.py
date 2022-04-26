from Qubit import *
import socket, sys

class Client:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.polar = 0b0 # this bit will be replaced, just making it global ig
        self.rpolar = 0b0
        self.array = [] # array or recieved bits

    def receive(self):
        msg = self.socket.recv(1024) # recieve string from server 1024 bytes at a time
        fullMessage = msg
        
        while msg: # repeat as long as message string not empty
            print('Received:' + msg.decode())
            fullMessage += msg # concatenate messages
            msg = self.socket.recv(1024)

        self.socket.close() # disconnect client
        return fullMessage
    
    def recievequbit(self):
        msg = self.socket.recv(4096) # recieve array from server in one chunk

        for i in msg: # for each item in the array
            self.array.append(i.measure)
        
        self.polar = 0b0



    def sendpolar(self):
        self.stream.send(self.polar) # send the polarisation

    def recievepolar(self):
        self.rpolar = self.socket.recv(1024)