#!/usr/bin/env python3

from .Interface import NodeInterface

class MiddleMan(NodeInterface):
    def __init__(self, upstream):
        self.bFreeze = False
        self.MitmResponse = None
        self.CapturedPacket = None

        super().__init__(upstream, None)

        assert(self.key == None)


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