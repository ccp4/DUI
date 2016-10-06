#from subprocess import call as shell_func
import subprocess
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Queue import Queue

class WriteStream(object):
    def __init__(self, queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)



class MyThread(QThread):

    def __init__(self, parent):
        super(QThread, self).__init__()
        self.my_parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        print "in run()"
        for rep in xrange(10):
            print "rep =", rep

        self.thrd_queue = Queue()
        sys.stdout = WriteStream(self.thrd_queue)

        self.capturing()

    def capturing(self):
        while True:
            text = self.thrd_queue.get()



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
        a = MyThread(self)
        a.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
