from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import time
from multiprocessing import Pipe, Process
from threading import Thread

class RedirectText2Pipe(object):
    def __init__(self, pipe_inlet):
        self.pipe_inlet = pipe_inlet
    def write(self, string):
        self.pipe_inlet.send(string)
    def flush(self):
        return None

class Run1(Process):
    def __init__(self, pipe_inlet):
        Process.__init__(self)
        self.pipe_std = pipe_inlet

    def run(self):
        redir = RedirectText2Pipe(self.pipe_std)
        sys.stdout = redir
        sys.stderr = redir

        for i in range(30):
            time.sleep(0.1)
            print i,'Hi'

class RedirectedWorkerThread(Thread):
    """Worker Thread Class."""
    def __init__(self, my_parent):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        #self.stdout_target_ = stdout_target
        self.my_parent = my_parent

    def run(self):
        """
        In this function, actually run the process and pull any output from the
        pipes while the process runs
        """
        pipe_outlet, pipe_inlet = Pipe(duplex = False)
        p = Run1(pipe_inlet)
        p.daemon = True
        p.start()

        while p.is_alive():

            #Collect all display output from process
            while pipe_outlet.poll():
                p_out = pipe_outlet.recv()
                p_text = str(p_out)
                self.my_parent.pipe_this_text(p_text)

        self.my_parent._running = False


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.btn1 = QPushButton('\n\n     Click ME    \n\n', self)
        self.btn1.clicked.connect(self.B_clicked1)

        self.textedit = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.textedit)

        self._running = False

        self.setGeometry(1200, 200, 450, 350)
        self.setLayout(vbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def B_clicked1(self, event):
        if( self._running == False ):
            self._running = True
            t1 = RedirectedWorkerThread(self)
            t1.daemon = True
            t1.start()
        else:
            print "currently Running"

    def pipe_this_text(self, text):
        time.sleep(0.005)
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

