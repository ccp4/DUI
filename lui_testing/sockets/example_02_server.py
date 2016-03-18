import socket

s = socket.socket()
host = socket.gethostname()
port = 12
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("Connection accepted from " + repr(addr[1]))

    c.send("Server approved connection\n")
    print repr(addr[1]) + ": " + c.recv(1026)
    c.close()

'''
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print buf
        brea
'''