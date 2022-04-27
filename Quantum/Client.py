from Quantum.Qubit import *
from Quantum.XOR import *
import socket, sys #, Qubit

ENCODING = "utf8"
class Client:
    def __init__(self, addr):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = addr # keep server address

        self.clientValues = ""
        self.clientPolar = ""
        self.serverPolar = ""
        self.key = ""

    def send(self, msg):
        key = self.key #format(0b001, '03b')
        msg = msg.encode(ENCODING)
        msg = self.encrypt(key, msg)
        self.connection.sendto(msg, self.addr)

    def receive(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        key = self.key #format(0b001, '03b')
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
    def sendqubits(self, length): # experiment with 16, 256, 1024
        # I dont *actually* have to make qubits here, right?
        count = 0
        while count < length:
            value_bit = random.randint(0,1)
            polar_bit = random.randint(0,1)
            self.clientValues += str(value_bit)
            self.clientPolar += str(polar_bit)
            count += 1

        msg = self.clientPolar + ',' + self.clientValues # concatenate the values
        self.connection.sendto(msg.encode(ENCODING), self.addr) # send the array

    def sendpolar(self):
        self.connection.sendto(self.clientPolar.encode(ENCODING), self.addr) # send the polarisation

    def recievepolar(self):
        requestData, self.addr = self.connection.recvfrom(1024)
        self.serverPolar = requestData.decode(ENCODING)

        self.key = self.getkey()
    
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
                key += self.clientValues[i] # append to string
        
        print(key)
        return key