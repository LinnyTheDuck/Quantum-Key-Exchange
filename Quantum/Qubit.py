#!/usr/bin/env python3
import random

class Qubit:
    def __init__(self, v, p):
        self.value = v
        self.polarisation = p # can only be a 1 or 0

    def set(self, v, p):
        self.value = v
        self.polarisation = p

    def measure(self, p):
        if(self.polarisation == p): # return value if polarisation matches
            return self.value
        else: # set the polarization to the new type - I don't feel this is right
            self.polarisation = 0b0 if self.polarisation == 0b1 else 0b1 # ternary to flip bit
            self.value = random.getrandbits(1) # Set the value to 0 or 1 with 50/50 chance
            return self.value # Return the new value