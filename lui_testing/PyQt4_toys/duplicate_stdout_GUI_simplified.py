import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import time
import subprocess

class OutputWrapper( QObject):
    outputWritten =  pyqtSignal(object)

    def __init__(self, parent, stdout=True):
        QObject.__init__(self, parent)
        self._stream = sys.stdout
        sys.stdout = self

    def write(self, text):
        self._stream.write(text)
        self.outputWritten.emit(text)

    def __getattr__(self, name):
        return getattr(self._stream, name)

    def __del__(self):
        try:
            sys.stdout = self._stream
        except AttributeError:
            pass


def imprime_algo(n = 3):

    for rep in xrange(n):
        time.sleep(1)
        print "rep =", rep

    # The next line will NOT be redirected from stdout
    #subprocess.call("./sec_interval.sh", shell=True)



class Window( QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        widget =  QWidget(self)
        layout =  QVBoxLayout(widget)
        self.setCentralWidget(widget)
        self.terminal =  QTextBrowser(self)
        self.button =  QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout.addWidget(self.terminal)
        layout.addWidget(self.button)

        stdout = OutputWrapper(self, True)
        stdout.outputWritten.connect(self.handleOutput)

    def handleOutput(self, text):
        self.terminal.moveCursor( QTextCursor.End)
        self.terminal.insertPlainText(text)

    def handleButton(self):
        imprime_algo()

if __name__ == '__main__':

    app =  QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 300, 200)
    window.show()
    sys.exit(app.exec_())