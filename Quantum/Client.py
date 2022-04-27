from Quantum.Qubit import *
from Quantum.XOR import *
import socket, sys #, Qubit

ENCODING = "utf8"
class Client:
    def __init__(self, addr):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = addr # keep server address

        #self.polar = 0b0 # this bit will be replaced, just making it global ig
        #self.rpolar = 0b0
        #self.array = [] # array or recieved bits

    def send(self, msg):
        key = 0b001
        msg = msg.encode(ENCODING)
        msg = self.encrypt(key, msg)
        self.connection.sendto(msg, self.addr)

    def receive(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        key = 0b001
        requestData = self.decrypt(key, requestData)
        requestData = requestData.decode(ENCODING)
        return requestData
    
    def close(self):
        self.connection.close()

    # Encryption stuff
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

    #Qubit stuff
    def recievequbit(self):
        msg = self.socket.recv(4096) # recieve array from server in one chunk

        for i in msg: # for each item in the array
            self.array.append(i.measure)
        
        self.polar = 0b0

    def sendpolar(self):
        self.stream.send(self.polar) # send the polarisation

    def recievepolar(self):
        self.rpolar = self.socket.recv(1024)