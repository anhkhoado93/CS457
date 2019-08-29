# TCP echo client

import socket

HOST = '10.0.2.15'    # MODIFY THIS LINE TO USE THE SERVER'S IP ADDRESS!!!!
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, Jared')  # modify this to say hello to your name
    data = s.recv(1024)
    
print('Received', repr(data))
