#!/usr/bin/env python3

class NodeInterface(object):
    def __init__(self, upstream = None, key :bytes = None):
        self.key = key
        self.upstream = upstream

    def SendUpstream(self, data): # sends data upstream
        if(self.upstream):
            return self.upstream.ReceiveDownstream(data)

    def ReceiveDownstream(self, data): # recieves data downstream
        return data
        