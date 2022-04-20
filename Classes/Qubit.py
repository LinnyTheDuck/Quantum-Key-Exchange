import random
global value, polarisation # polar is either 1 or 0

def new(v, p): # this is wrong
    value = v
    polarisation = p

def set(v, p):
    value = v
    polarisation = p

def measure(polarisation):
    if(value == polarisation): # return value if polarisation matches ?? is it supposed to match value
        return value
    else: # set the polarization to the new type - I don't feel this is right
        polarisation = random.randint(0,1) # Set the value to 0 or 1 with 50/50 chance
        return value # Return the new value