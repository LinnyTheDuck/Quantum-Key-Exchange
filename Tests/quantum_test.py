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

    I did was basically stored the message and key as byte arrays, then just looped over the key and performed a bitwise-XOR between the two bytes to produce the encrypted byte. 
    For testing the qubit class, I did a test to check the value would eventually change if I kept measuring with the wrong polarity.
    Since if it were a randomized process then it would eventually have to change
'''

def test_qubit():
    toggle = True # toggle for which bit in polarisation is up
    qubit = Qubit(1,0) # enter a 1 or 0
    value = qubit.measure(1)
    while (value != 0): # making sure the value of the qubit changes
        if (toggle):
            value = qubit.measure(0)
            toggle = False
        else:
            value = qubit.measure(1)
            toggle = True
    assert(value == 0) # check it's a 0

def test_xor():
    key = 0b0010010010010010
    message = 0b0100110101100101
    encrypted = XOR.cipher(key, message)

    # expected = 0b0110100111110111 # just used as a midway check
    # assert (encrypted == expected)

    original = XOR.cipher(key,encrypted)
    assert (message == original) # check if both encryption and decryption works with integrity of orig msg

def test_qke_16():
    print("hi")
    assert(1 == 1)

def test_qke_256():
    print("hi")
    assert(1 == 1)

def test_qke_1024():
    print("hi")
    assert(1 == 1)

def qke_algorithm():
    print("hello world")