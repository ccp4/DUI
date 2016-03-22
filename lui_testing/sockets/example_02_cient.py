import socket

host = ''
port = 50000
backlog = 5


for times in xrange(backlog):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    inpt = raw_input('type anything and click enter... ')
    s.send(inpt)
    print "the message has been sent"
    s.close()


