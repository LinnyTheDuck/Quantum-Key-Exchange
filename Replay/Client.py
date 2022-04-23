#!/usr/bin/env python3

from .Interface import NodeInterface

# Random and Crypto
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class Client(NodeInterface):
    def __init__(self, upstream=None, key :bytes = None):
        self.nonce = 0

        super().__init__(upstream, key)
        assert(self.key == key)

    def SendUpstream(self, data):
        if(self.upstream):
            ctx = AESGCM(self.key)

            # Encrypts using AES-256-GCM. 96b (12B) nonce is supplied in little endian
            encData = ctx.encrypt(self.nonce.to_bytes(12, "little"), data, None)

            # Prepend the nonce. Otherwise, the server will get confused
            retData = self.upstream.ReceiveDownstream(self.nonce.to_bytes(12, "little") + encData)

            # Increment the nonce. The server will do too
            self.nonce += 1

            decData = ctx.decrypt(self.nonce.to_bytes(12, "little"), retData, None)

            # Increment again to prevent nonce reuse
            self.nonce += 1

            return decData

    def ReceiveDownstream(self, data):
        return data
        