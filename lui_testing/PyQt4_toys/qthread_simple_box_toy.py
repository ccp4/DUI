import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Queue import Queue

import time

class EmittingStream(QObject):

    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

class MyThread(QThread):

    def __init__(self, parent):
        super(QThread, self).__init__()
        self.my_parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        print "in run() begin"

        for rep in xrange(3):
            print "rep =", rep
            time.sleep(1)

        print "in run() End"


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.btn1 = QPushButton('\n\n     Click ME    \n\n', self)
        self.btn1.clicked.connect(self.B_clicked1)

        self.textedit = QTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.textedit)

        sys.stdout = EmittingStream(textWritten=self.append_text)

        self.setGeometry(1200, 200, 450, 350)
        self.setLayout(vbox)
        self.setWindowTitle('Shell dialog')
        self.show()


    def B_clicked1(self):
        print "B_clicked1"
        a = MyThread(self)
        a.start()


    def append_text(self, text):
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText( text )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
