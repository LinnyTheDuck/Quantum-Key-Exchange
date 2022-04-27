import operator

class XOR:
    def __init__ (self, key, msg):
        self.key = key
        self.msg = msg

    def cipher(key, msg): # returns the XOR value of the key and message
        return operator.xor(key, msg)

    def repeatKey(key, length):
        origkey = key # preserve the original key
        keylen = len(bin(key)) - 2 # get length of key
        length -= keylen # the rest of the length we have to fill up
        while length != 0:
            if length >= keylen:
                key << keylen # shift it over by num of bits in key
                key = key and origkey
                length -= keylen
            else: # keylen < length
                key << length
                origkey >> (keylen - (length % keylen) )
                key = key and origkey
                length = 0
        print(key)
        return key