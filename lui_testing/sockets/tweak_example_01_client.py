import socket



while True:

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    a = str(raw_input())
    print "a =", a
    clientsocket.send(a)
    clientsocket.close()
    if( a == "stop" ):
        break
