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

    def receiveFromClient(self):
        clientReqData, self.clientAddr = self.clientConnection.recvfrom(1024)
        return clientReqData

    def sendToClient(self, msg):
        self.clientConnection.sendto(msg.encode(ENCODING), self.clientAddr)

    def recieveFromServer(self):
        serverReqData, self.serverAddr = self.serverConnection.recvfrom(1024)
        return serverReqData

    def sendToServer(self, msg):
        self.serverConnection.sendto(msg.encode(ENCODING), self.serverAddr)


