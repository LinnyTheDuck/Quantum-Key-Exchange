import operator

def cipher(key, msg): # returns the XOR value of the key and message
    return operator.xor(key, msg)