#!/usr/bin/env python3

from .Interface import NodeInterface

import os

class Client(NodeInterface):
    def __init__(self, upstream=None, key :bytes = None):
        self.nonce = 0

        super().__init__(upstream, key)
        assert(self.key == key)

    def SendUpstream(self, data):
        if self.upstream:
            return data

    def ReceiveDownstream(self, data):
        return data
        