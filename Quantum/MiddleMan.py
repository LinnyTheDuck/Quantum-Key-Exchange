#!/usr/bin/env python3
import socket

class MiddleMan:
    def __init__(self, clientAddr, servAddr):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create socket
        self.connection.bind(addr) # bind socket


    def SendUpstream(self, data):
        if(self.upstream):
            return self.upstream.ReceiveDownstream(data)


    def ReceiveDownstream(self, data):
        # Received from below
        self.CapturedPacket = data

        # Do this first
        clientData = self.SendUpstream(data)

        if not self.bFreeze:
            self.MitmResponse = data

        return clientData

    def Freeze(self):
        self.bFreeze = True