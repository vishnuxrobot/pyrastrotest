import time
import socket
import sys
import os
s = socket.socket()
host = ""
port = 8080
s.connect ((host, port))
print("Connected to Server")
Command = s.recv(1024)
Command = Command.decode()
if Command == "open":
    print("Command Received".encode())
    os.system('ls')  