import socket
from encrypt import *

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(4096)
            print(data)
            data = data.decode()
            print(data)
            if not data:
                break
            print(decrypt(data))
