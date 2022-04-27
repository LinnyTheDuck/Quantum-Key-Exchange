from Quantum.Qubit import *
from Quantum.XOR import *
import socket, sys, random

ENCODING = "utf8"
class Server:
    def __init__(self, addr):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
        self.connection.bind(addr) # bind socket
        self.addr = addr # keep clients address

        self.clientPolar = ""
        self.serverPolar = ""
        self.serverValues = ""
        self.key = ""

    def send(self, msg):
        key = self.key #format(0b001, '03b')
        msg = msg.encode(ENCODING)
        msg = self.encrypt(key, msg)
        self.connection.sendto(msg,self.addr) # send message to client

    def receive(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        key = self.key #format(0b001, '03b')
        requestData = self.decrypt(key, requestData)
        requestData = requestData.decode(ENCODING)
        #requestData.strip().strip('\x00') # strip the null bytes
        return requestData

    def close(self):
        self.connection.close() # disconnect the server

    # Encryption Stuff
    def encrypt(self, key, message):
        message = int.from_bytes(message, byteorder=sys.byteorder)
        length = len(bin(message)) - 2 # -2 to remove 0b
        key = XOR.repeatKey(key, length)
        encrypted = XOR.cipher(key, message)
        return encrypted.to_bytes(length, byteorder=sys.byteorder)

    def decrypt(self, key, encrypted): # the same as encrypt but exists for clearing my head
        encrypted = int.from_bytes(encrypted, byteorder=sys.byteorder)
        length = len(bin(encrypted)) - 2 # -2 to remove 0b
        key = XOR.repeatKey(key, length)
        message = XOR.cipher(key, encrypted)
        return message.to_bytes(length, byteorder=sys.byteorder)

    # Qubit Stuff
    def recievequbit(self):
        requestData, self.addr = self.connection.recvfrom(4096)
        requestData = requestData.decode(ENCODING)

        chunks = requestData.split(',')
        self.clientPolar = chunks[0]
        values = chunks[1]
        length = len(self.clientPolar)

        for i in range(length):
            polar_bit = random.randint(0,1) # need to do the polarisation here
            self.serverPolar += str(polar_bit) 

            qubit = Qubit(int(values[i]),int(self.clientPolar[i]))
            measure = qubit.measure(polar_bit) # measure with a random value
            self.serverValues += str(measure)

        self.key = self.getkey()

    def sendpolar(self):
        self.connection.sendto(self.serverPolar.encode(ENCODING), self.addr) # send the polarisation

    def recievepolar(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        self.clientPolar = requestData.decode(ENCODING)

    def getkey(self):
        length = len(self.clientPolar) # get length of string
        anded = ""
        for i in range(length): # and them
            if self.clientPolar[i] == self.serverPolar[i]:
                anded += "1"
            else:
                anded += "0"

        key = ""
        for i in range(length):
            if anded[i] == "1":
                key += self.serverValues[i] # append to string
        
        print(key)
        return key