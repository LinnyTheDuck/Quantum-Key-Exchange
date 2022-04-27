#!/usr/bin/env python3
import socket

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
        self.serverPolar = ""
        self.key = ""

    def receiveFromClient(self):
        clientReqData, self.clientAddr = self.clientConnection.recvfrom(1024)
        #clientReqData = clientReqData.decode(ENCODING)

        '''if self.clientValues == "":
            self.measureQubits(clientReqData)
        else: # key has already been worked out by this stage
            self.decodeMsg(clientReqData)'''

        self.sendToServer(clientReqData)

    def sendToClient(self, msg):
        self.clientConnection.sendto(msg, self.clientAddr)
        #self.clientConnection.sendto(msg.encode(ENCODING), self.clientAddr)

    def recieveFromServer(self):
        serverReqData, self.servAddr = self.serverConnection.recvfrom(1024)
        #serverReqData = serverReqData.decode(ENCODING)

        '''if self.key == "":
            self.recordPolar()
            self.getKey()
        else:
            self.decodeMsg(serverReqData)'''

        self.sendToClient(serverReqData)

    def sendToServer(self, msg):
        self.serverConnection.sendto(msg, self.servAddr)
        #self.serverConnection.sendto(msg.encode(ENCODING), self.servAddr)

    def measureQubits(self, data):
        # simulate measurement of qubits (and any changes)
        # value of data will change
        self.sendToServer(data)

    def recordPolar(self):
        print("hi")

    def getKey(self):
        print("hi")

    def decodeMsg(self, msg):
        decodedmsg = msg
        print(decodedmsg)