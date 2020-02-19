import random
from key import *

def encrypt(data):

    key = str(generatekey())
    newdata = ''

    digit1 = random.randint(10,30)
    character = ord(data[0])
    character = character + int(key)
    character = character + digit1
    newdata = newdata + str(digit1)
    newdata = newdata + chr(character)

    length = len(data)

    for i in range(1, length):
        character = ord(data[i])
        character = character + int(key)
        character = character + ord(newdata[i+1])%15
        newdata = newdata + chr(character)
    return(newdata)

def decrypt(data):

    key = retrievekey()
    constant = int(data[0:2])
    newdata = ''

    character = ord(data[2])
    character = character - constant
    character = character - int(key)
    newdata = newdata + chr(character)
    
    length = len(data)
    for i in range(3, length):
        character = ord(data[i])
        character = character - ord(data[i-1])%15
        character = character - int(key)
        newdata = newdata + chr(character)
    return(newdata)
