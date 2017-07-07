import sys
from PySide.QtGui import *
from PySide.QtCore import *
import time
import subprocess

class MyThread (QThread):

    def run(self):
        self.cmd_to_run = "./sec_interval.sh"
        print "Hi from QThread(run)"

        print "before subprocess"
        p = subprocess.Popen([self.cmd_to_run],
                             stdout = subprocess.PIPE,
                             stderr = subprocess.STDOUT,
                             bufsize = 1)
        print "after subprocess"

        for line in iter(p.stdout.readline, b''):
            single_line = line[0:len(line)-1]
            print ">>", single_line

        p.wait()
        p.stdout.close()

        print "after ...close()"

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        self.thrd = MyThread(self)
        self.thrd.finished.connect(self.tell_finished)
        main_box = QHBoxLayout()

        self.textedit = QTextEdit()
        main_box.addWidget(self.textedit)

        self.pushbutton = QPushButton('Click Me')
        main_box.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.start_thread)

        self.setLayout(main_box)
        self.show()

    def start_thread(self):
        print "Staring thread"
        self.thrd.start()

    def tell_finished(self):
        print "finished thread"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

