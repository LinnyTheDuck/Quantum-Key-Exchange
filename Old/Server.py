#!/usr/bin/env python3

from .Interface import NodeInterface

import os

class Server(NodeInterface):
    def __init__(self, key :bytes = None):
        self.DoorOpen = False
        self.signingKey = os.urandom(32)

        super().__init__(None, key)
        assert(self.key == key)

    def SendUpstream(self, data):
        # We have no upstream
        return

    def ReceiveDownstream(self, data):
        return data
