from encrypt import *

data  = input("Enter data")
newdata = encrypt(data)
print(newdata)
print(decrypt(newdata))
