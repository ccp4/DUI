import sys
import time
import subprocess

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

class MyQProcess(QProcess):

    str_print_signal = pyqtSignal(str)

    def __init__(self):
        super(MyQProcess, self).__init__()
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.setProcessChannelMode(QProcess.MergedChannels)
        self.started.connect(self.on_start)
        self.finished.connect(self.on_finish)

    def on_start(self):
        print "\n on_start \n"

    def on_finish(self):
        print "\n on_finish \n"

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        self.str_print_signal.emit(single_line)


class MyObject(QObject):

    str_print_signal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyObject, self).__init__()
        self.qProcess = MyQProcess()
        self.qProcess.str_print_signal.connect(self.prn_lin)

    def launch(self):
        print "Hi from QThread(run)"
        self.qProcess.start("./sec_interval.sh")

    def prn_lin(self, single_line):
        self.str_print_signal.emit(single_line)


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        self.my_obj = MyObject()
        #self.my_obj.finished.connect(self.tell_finished)
        main_box = QHBoxLayout()


        self.my_obj.str_print_signal.connect(self.cli_out)

        self.textedit = QTextEdit()
        main_box.addWidget(self.textedit)

        self.pushbutton = QPushButton('Click Me')
        main_box.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.start_thread)

        self.setLayout(main_box)
        self.show()

    def start_thread(self):
        print "Staring thread"
        self.my_obj.launch()

    def tell_finished(self):
        print "finished thread"

    def cli_out(self, lin_to_prn):
        #print lin_to_prn, " <<"
        self.textedit.append(lin_to_prn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

