import socket
from encrypt import *

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    data = input("Enter data")
    newdata = encrypt(data)
    newdata = newdata.encode()

    s.sendall(newdata)
