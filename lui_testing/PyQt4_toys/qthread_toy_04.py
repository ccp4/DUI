import sys
#from PySide.QtGui import *
#from PySide.QtCore import *
import time
import subprocess

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

def run_cli_prss(cmd_to_run = None, ref_to_class = None):

    print "before subprocess"
    p = subprocess.Popen([cmd_to_run],
                            stdout = subprocess.PIPE,
                            stderr = subprocess.STDOUT,
                            bufsize = 1)
    print "after subprocess"

    for line in iter(p.stdout.readline, b''):
        single_line = line[0:len(line)-1]
        try:
            ref_to_class.emit_print_signal(single_line)

        except:
            print single_line

    p.wait()
    p.stdout.close()


class MyThread (QThread):

    str_print_signal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyThread, self).__init__()

    def run(self):
        self.cmd_to_run = "./sec_interval.sh"
        print "Hi from QThread(run)"

        #run_cli_prss(cmd_to_run = self.cmd_to_run, ref_to_class = self)
        run_cli_prss(cmd_to_run = self.cmd_to_run)

        print "after ...close()"

    def emit_print_signal(self, str_lin):
        self.str_print_signal.emit(str_lin)

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        self.thrd = MyThread()
        self.thrd.finished.connect(self.tell_finished)
        main_box = QHBoxLayout()

        self.thrd.str_print_signal.connect(self.cli_out)

        self.textedit = QTextEdit()
        main_box.addWidget(self.textedit)

        self.pushbutton = QPushButton('Click Me')
        main_box.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.thrd.start)

        self.setLayout(main_box)
        self.show()

    def tell_finished(self):
        print "finished thread"

    def cli_out(self, lin_to_prn):
        #print lin_to_prn, " <<"
        self.textedit.append(lin_to_prn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

