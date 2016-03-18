import socket
'''
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
clientsocket.send('hello')
'''
s = socket.socket()
host = 111.111.0.11
port = 1247
s.connect((host, port))
print s.recv(1024)
inpt = raw_input('type anything and click enter... ')
s.send(inpt)
print "the message has been sent"