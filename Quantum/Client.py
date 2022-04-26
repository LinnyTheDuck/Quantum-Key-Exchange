#from Qubit import *
import socket #, Qubit

ENCODING = "utf8"
class Client:
    def __init__(self, addr):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = addr # keep server address

        #self.polar = 0b0 # this bit will be replaced, just making it global ig
        #self.rpolar = 0b0
        #self.array = [] # array or recieved bits

    def send(self, msg):
        self.connection.sendto(msg.encode(ENCODING), self.addr)

    def receive(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        return requestData.decode(ENCODING)
    
    def close(self):
        self.connection.close()

'''
    def recievequbit(self):
        msg = self.socket.recv(4096) # recieve array from server in one chunk

        for i in msg: # for each item in the array
            self.array.append(i.measure)
        
        self.polar = 0b0

    def sendpolar(self):
        self.stream.send(self.polar) # send the polarisation

    def recievepolar(self):
        self.rpolar = self.socket.recv(1024)
'''