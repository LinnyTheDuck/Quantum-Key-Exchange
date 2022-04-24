import operator

class XOR:
    def __init__ (self, key, msg):
        self.key = key
        self.msg = msg

    def cipher(key, msg): # returns the XOR value of the key and message
        return operator.xor(key, msg)