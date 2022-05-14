import socket
import threading
import sys

server = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port)) # bind server and port to socket
except socket.error as e:
    str(e)
s.listen(4)
print("waiting for a connection, Server started")

