#!/usr/bin/env python3
from Quantum.Qubit import *
from Quantum.XOR import *
import socket, sys

ENCODING = "utf8"
class MiddleMan:
    def __init__(self, servAddr, clientAddr):
        self.clientConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
        self.clientConnection.bind(clientAddr) # bind socket
        self.clientAddr = clientAddr

        self.serverConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
        self.servAddr = servAddr

        self.clientValues = "" # values to steal mwahaha
        self.clientPolar = ""
        self.serverPolar = "" # the polar value that the server sends to the client
        self.serverPolarMeasured = "" # the polar values to send to the client after measuring the qubits
        self.key = ""

        self.len = 0

    def receiveFromClient(self):
        clientReqData, self.clientAddr = self.clientConnection.recvfrom(1024)
        flag = True # just a flag to trigger utf8 encoding

        if self.clientValues == "": # havent gotten qubits yet
            clientReqData = clientReqData.decode(ENCODING)
            clientReqData = self.measureQubits(clientReqData)
        else: # key has already been worked out by this stage
            copy = self.decodeMsg(clientReqData) # new copy of clientReqData so we don't need to re-encode
            try:
                copy = copy.decode(ENCODING) #decode utf8 after xor otherwise will break
            except:
                print("Cannot decode UTF-8")
            print("MiddleMan Recieved Message: " + str(copy))
            flag = False # toggle flag to send without reencoding

        self.sendToServer(clientReqData, flag)

    def sendToClient(self, msg, flag):
        '''if flag:
            self.clientConnection.sendto(msg.encode(ENCODING), self.clientAddr)
        else:'''
        self.clientConnection.sendto(msg, self.clientAddr)

    def recieveFromServer(self):
        serverReqData, self.servAddr = self.serverConnection.recvfrom(1024)
        flag = True # just a flag to trigger utf8 encoding

        if self.key == "": # no key yet, looks like we steal the polarisation
            self.recordPolar(serverReqData.decode(ENCODING))
            self.getKey()
        else:
            copy = self.decodeMsg(serverReqData)
            copy = copy.decode(ENCODING) 
            print("MiddleMan Recieved Message: " + copy)
            flag = False # toggle flag to send without reencoding

        self.sendToClient(serverReqData, flag)

    def sendToServer(self, msg, flag):
        if flag:
            self.serverConnection.sendto(msg.encode(ENCODING), self.servAddr)
        else:
            self.serverConnection.sendto(msg, self.servAddr)

    def measureQubits(self, data):
        chunks = data.split(',')
        self.clientPolar = chunks[0] # get clientPolarisations
        values = chunks[1]

        # simulate measurement of qubits, value of data will change
        length = len(self.clientPolar)
        self.clientValues = "" # can get rid of this line
        #serverPolar = ""

        for i in range(length):
            polar_bit = random.randint(0,1) # need to do the polarisation here
            #serverPolar += str(polar_bit) 

            qubit = Qubit(int(values[i]),int(self.clientPolar[i]))
            measure = qubit.measure(polar_bit) # measure with a random value
            self.clientValues += str(measure)
            self.serverPolarMeasured += str(qubit.getPolar())
        
        dataRepacked = self.serverPolarMeasured + ',' + self.clientValues # repack the values
        return dataRepacked

    def recordPolar(self, polar):
        self.serverPolar = polar

    def getKey(self):
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
        
        print("Middle Man Key: " + key)
        self.key = key
        #return key

    def decodeMsg(self, msg):
        encrypted = int.from_bytes(msg, byteorder=sys.byteorder) # decode xor
        length = self.len #len(bin(encrypted)) - 2 # -2 to remove 0b
        key = XOR.repeatKey(self.key, length)
        message = XOR.cipher(key, encrypted)
        decodedmsg = message.to_bytes(length, byteorder=sys.byteorder)
        return decodedmsg

    def setlen(self, len):
        self.len = len

    def length(self): # cheating the length here
        return self.len