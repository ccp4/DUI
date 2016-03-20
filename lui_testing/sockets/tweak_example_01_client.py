import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

while True:
    a = str(raw_input())
    print "a =", a
    clientsocket.send(a)
