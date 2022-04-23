#!/usr/bin/env python3

from .Interface import NodeInterface

import os

# Crypto
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Signing
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.hashes import SHA512_256
from cryptography.hazmat.backends import default_backend

import json

from base64 import b64encode, b64decode

import datetime

class Server(NodeInterface):
    def __init__(self, key :bytes = None):
        self.DoorOpen = False
        self.signingKey = os.urandom(32)
        
        self.nonceList = [] #HERe IS A NONCE LIST

        super().__init__(None, key)
        assert(self.key == key)


    def SendUpstream(self, data):
        # We have no upstream
        return

    def __TryVerifySignature(self, sig, token):
        dsa = HMAC(self.signingKey, SHA512_256(), default_backend())
        dsa.update(token)
       
        try:
            # Lib is a bit annoying about it's use of exceptions
            # As control flow, but hey
            dsa.verify(sig)
            return True
        except:
            return False

    def __TryVerifyTime(self, token):
        # Sig is valid, so we did sign this token
        # But is it still valid?

        # Default = No
        valid = False

        # Load JSON
        asJson = json.loads(token)

        # Time Now
        dtNow = datetime.datetime.now()
        validFromStamp = datetime.datetime.fromisoformat(asJson["timeIssued"])
        validTillStamp = datetime.datetime.fromisoformat(asJson["timeExpired"])

        if dtNow >= validFromStamp and dtNow < validTillStamp:
            valid = True
        
        return valid

    def __TryVerifyPermissions(self, token):
        # Sig is valid and time is valid
        # Do we have permissions?

        # Default = No
        valid = False

        # Load JSON
        asJson = json.loads(token)

        # Hardcoded cause I'm evil
        if asJson["user"] == "admin":
            valid = True

        return valid

    def __TryVerify(self, token):
        token = b64decode(token)

        sig = token[-32:]
        text = token[:-32]

        return self.__TryVerifySignature(sig, text) and self.__TryVerifyTime(text) and self.__TryVerifyPermissions(text)
        

    def __GenerateSessionToken(self, user, password):
        token = json.dumps({
            "user": user,
            "timeIssued": datetime.datetime.now().isoformat(),
            "timeExpired": (datetime.datetime.now() + datetime.timedelta(minutes = 10)).isoformat()
        }).encode()

        dsa = HMAC(self.signingKey, SHA512_256(), default_backend())
        dsa.update(token)
        signature = dsa.finalize()

        return (token + signature)

        # print(self.__TryVerify(token + signature))


    def ReceiveDownstream(self, data):
        ctx = AESGCM(self.key)

        # Decrypt
        # NOTE: This library throws exceptions when it
        # fails to decrypt...
        decData = ctx.decrypt(data[:12], data[12:], None)
        
        #Check if the list contains nonce
        recNonce = int.from_bytes(data[:12], "little")
        
        #return ctx.encrypt(decData, returnValue, None)
        
        # Increment the nonce
        #incNonce = int.from_bytes(data[:12], "little") + 1
        incNonce = recNonce + 1

        cmd = json.loads(decData.decode())

        returnValue = None
        if recNonce in self.nonceList:
            returnValue = json.dumps({"success": False, "reason": "Authentication Failed"}).encode()
        else:
            #add nonce to the list
            self.nonceList.append(recNonce)

            # Check Action is auth, otherwise it's a privileged action
            if cmd["action"] == "auth":
                # Ignore the hard-coded credentials :\
                if cmd["user"] == "admin" and cmd["pass"] == "compx304":
                    returnValue = b64encode(self.__GenerateSessionToken(cmd["user"], cmd["pass"]))
                    
            # Check AuthToken
            elif self.__TryVerify(cmd["token"]):
                # Valid, check action
                if cmd["action"] == "open_door":
                    self.DoorOpen = True
                    returnValue = json.dumps({"success": True, "reason": ""}).encode()
                if cmd["action"] == "close_door":
                    self.DoorOpen = False
                    returnValue = json.dumps({"success": True, "reason": ""}).encode()

            else:
                returnValue = json.dumps({"success": False, "reason": "Authentication Failure"}).encode()

        return ctx.encrypt(incNonce.to_bytes(12, "little"), returnValue, None)
