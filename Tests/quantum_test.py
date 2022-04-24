#!/usr/bin/env python3
from Quantum.Qubit import *
from Quantum.XOR import *
import os

'''
def test_server():
    psk = os.urandom(32)
    serv = Server(key=psk)
    client = Client(serv, key=psk)

    data = client.SendUpstream("test")
    serv.RecieveDownstream(data)

    assert(1==1)
'''

def test_qubit():
    qubit = Qubit(1,0) # enter a 1 or 0
    value = qubit.measure(1)
    qubit.set(1,1)
    value = qubit.measure(1)
    assert(value == 1 or value == 0) # check it's a 1 or a 0

def test_xor():
    key = 0b0010010010010010
    message = 0b0100110101100101
    encrypted = XOR.cipher(key, message)

    # expected = 0b0110100111110111 # just used as a midway check
    # assert (encrypted == expected)

    original = XOR.cipher(key,encrypted)
    assert (message == original) # check if both encryption and decryption works with integrity of orig msg

def test_qke():
    print("hi")
    assert(1 == 1)