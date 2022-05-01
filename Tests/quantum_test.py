#!/usr/bin/env python3
import pytest
from Quantum.Qubit import *
from Quantum.XOR import *
from Quantum import Server, Client
import os

# ports n stuf
host = "127.0.0.1"
port = 54328

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
    key = format(0b001, '03b')
    message = 0b0100110101100101

    # get length of message
    length = len(bin(message)) - 2 # -2 to remove 0b
    key = XOR.repeatKey(key, length)

    encrypted = XOR.cipher(key, message)

    # expected = 0b0110100111110111 # just used as a midway check
    # assert (encrypted == expected)

    original = XOR.cipher(key,encrypted)
    assert (message == original) # check if both encryption and decryption works with integrity of orig msg

testdata = [
    (16, "my name's jeff"),
    (256, "I am the Globglogabgalab"),
    (1024, "it's the most wonderful time of the YE")
]

@pytest.mark.parametrize("keylen, msg", testdata)
def test_qke_algorithm(keylen, msg):
    # setup server and client ONLY
    serverAddress = (host, port)
    server = Server.Server(serverAddress) # use serverAddress for BOTH if just client/server
    client = Client.Client(serverAddress)
    
    # QKE key exchange, pass in keylen
    client.sendqubits(keylen)
    server.recievequbit()
    server.sendpolar()
    client.recievepolar()

    # server sends message to client
    client.send(msg) # send something to the server
    len = client.length() # passing the length
    server.setlen(len)
    recv = server.receive().strip('\x00') # why do I have to strip the null bytes here?

    server.close()
    assert(msg == recv)