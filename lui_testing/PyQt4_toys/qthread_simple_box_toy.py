#from subprocess import call as shell_func
import subprocess
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

pyside_template = '''
class MyThread (QThread):
    def run():
        socket = QTcpSocket()
        # connect QTcpSocket's signals somewhere meaningful
        # ...
        socket.connectToHost(hostName, portNumber)
        self.exec_()

'''

class YourThreadName(QThread):

    def __init__(self):
        QThread.__init__(self)
        print "in __init__"

    def __del__(self):
        self.wait()

    def run(self):
        print "in run()"

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.btn1 = QPushButton('\n\n     Click ME    \n\n', self)
        self.btn1.clicked.connect(self.B_clicked1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)

        bg_box = QVBoxLayout(self)
        bg_box.addLayout(vbox)

        self.setGeometry(1200, 200, 450, 350)
        self.setLayout(bg_box)
        self.setWindowTitle('Shell dialog')
        self.show()

    def B_clicked1(self):
        print "B_clicked1"
        a = YourThreadName()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
