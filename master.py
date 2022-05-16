import time
import socket
import sys
import os
s = socket.socket()
host = socket.gethostname()
port = 8080
s.blind(('', port))
s.listen()
conn, addr = s.accept()
print(addr, "is conncetd to server")
command = input(str("EnterCommand :"))
conn.send(command.encode())
print("command has been sent successfully.")
data = conn.recv(1024)
if data:
    print("command received and executed successfully")