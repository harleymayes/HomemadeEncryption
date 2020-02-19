import random


def generatekey():
    keystore = open("key.txt", 'w')

    word = input("Enter encryption word:")
    length = len(word)
    multiplier = random.randint(1,length)
    key = length * multiplier

    keystore.write(str(key))
    keystore.close()
    return(key)

def retrievekey():
    keystore = open("key.txt", 'r')
    key = keystore.read()
    keystore.close()
    return(key)
