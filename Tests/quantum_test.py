#!/usr/bin/env python3
from Quantum.Qubit import *
from Quantum.XOR import *
from Quantum import Server, Client
import os

# ports n stuf
host = "127.0.0.1"
port = 54321

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
    key = 0b001
    message = 0b0100110101100101

    # get length of message
    length = len(bin(message)) - 2 # -2 to remove 0b
    key = XOR.repeatKey(key, length)

    encrypted = XOR.cipher(key, message)

    # expected = 0b0110100111110111 # just used as a midway check
    # assert (encrypted == expected)

    original = XOR.cipher(key,encrypted)
    assert (message == original) # check if both encryption and decryption works with integrity of orig msg


def test_qke_16():
    msg = "my names Jeff"
    recv = qke_algorithm(16, msg)
    assert(msg == recv)

def test_qke_256():
    msg = "I am the Globglogabgalab"
    recv = qke_algorithm(256, msg)
    assert(msg == recv)

def test_qke_1024():
    msg = "it's the most wonderful time of the YE"
    recv = qke_algorithm(1024, msg)
    assert(msg == recv)

def qke_algorithm(keylen, msg):
    # setup server and client ONLY
    serverAddress = (host, port)
    server = Server.Server(serverAddress) # use serverAddress for BOTH if just client/server
    client = Client.Client(serverAddress)
    
    # QKE key exchange, pass in keylen
    ### Write some code here ###

    # server sends message to client
    client.send(msg) # send something to the server
    msg = server.receive()

    server.close()
    return msg