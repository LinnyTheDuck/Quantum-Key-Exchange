#from Qubit import *
import socket, sys, random #, Qubit

ENCODING = "utf8"
class Server:
    def __init__(self, addr):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
        self.connection.bind(addr) # bind socket

        self.addr = addr # keep clients address

        #self.polar = 0b0 # this bit will be replaced, just making it global ig
        #self.rpolar = 0b0

    def send(self, msg):
        self.connection.sendto(msg.encode(ENCODING),self.addr) # send message to client

    def receive(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        return requestData.decode(ENCODING)

    def close(self):
        self.connection.close() # disconnect the server

'''

    def sendqubits(self, length): # experiment with 16, 256, 1024
        qubit_array = [] # array of qubits
        polar_bit = random.getrandbits(1)
        self.polar = polar_bit # set the first bit
        qubit = Qubit(random.getrandbits(1), polar_bit)
        qubit_array.append(qubit) # add to the array

        for i in range(length - 1): # generate length many polarisations
            self.polar << 1 # bit shift to the left
            polar_bit = random.getrandbits(1) # new polar bit 
            self.polar = self.polar or polar_bit # OR the bits together
            qubit = Qubit(random.getrandbits(1), polar_bit) # create a qubit
            qubit_array.append(qubit) # add to the array
            #self.stream.send(qubit) # send the qubit? Or should I make an arary of them? 
              
        self.stream.send(qubit_array) # send the array

    def sendpolar(self):
        self.stream.send(self.polar) # send the polarisation

    def recievepolar(self):
        self.rpolar = self.connection.recv(1024)
'''