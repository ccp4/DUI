import socket

n_connections = 15

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
#serversocket.bind((8089))
serversocket.listen(n_connections) # become a server socket, maximum 15 connections
buf = ""
for i in xrange(n_connections):
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        print "buf =", buf
        if( buf == "stop" ):
            break

    else:
        print "len(buf) <= 0"

    print "\n connection num ", i


