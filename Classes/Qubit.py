import random

class Qubit:
    def __init__(self, v, p):
        self.value = v
        self.polarisation = p # can only be a 1 or 0

    def set(self, v, p):
        self.value = v
        self.polarisation = p

    def measure(self, p):
        if(self.value == p): # return value if polarisation matches ?? is it supposed to match value
            return self.value
        else: # set the polarization to the new type - I don't feel this is right
            self.polarisation = random.randint(0,1) # Set the value to 0 or 1 with 50/50 chance
            return self.value # Return the new value