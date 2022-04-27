import operator

class XOR:
    def __init__ (self, key, msg):
        self.key = key
        self.msg = msg

    def cipher(key, msg): # returns the XOR value of the key and message
        return operator.xor(key, msg)

    def repeatKey(key, length):
        origkey = key # preserve the original key
        keylen = len(key)# get length of key
        length -= keylen # the rest of the length we have to fill up

        while length > keylen:
            key += origkey
            #print(key)
            keylen = len(key) - 2
            
        if keylen < length:
            rem = keylen - (length % keylen)
            first_char = ""
            for i in range(0, rem):
                first_char = first_char + origkey[i]
            key += first_char
            keylen = len(key)

        #print(keylen)
        #print(length)
        #print(key)
        return int(key, 2)