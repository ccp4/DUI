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
        #self.setProcessChannelMode(QProcess.MergedChannels)
        self.readyReadStandardError.connect(self.readErrOutput)

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        self.str_print_signal.emit(single_line)

    def readErrOutput(self):
        print "some ERROR"


class MyObject(QObject):

    str_print_signal = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, parent = None):
        super(MyObject, self).__init__()
        self.qProcess = MyQProcess()
        self.qProcess.str_print_signal.connect(self.prn_lin)
        self.qProcess.started.connect(self.on_start)
        self.qProcess.finished.connect(self.on_finish)

    def launch(self):
        print "Hi from QObject(run)"
        self.qProcess.start("./sec_interval.sh")
        #self.qProcess.start("dials.index")

    def prn_lin(self, single_line):
        self.str_print_signal.emit(single_line)

    def on_start(self):
        print "\n on_start \n"

    def on_finish(self):
        print "\n on_finish \n"
        self.finished.emit()


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        self.my_obj = MyObject()
        self.my_obj.finished.connect(self.tell_finished)
        self.my_obj.str_print_signal.connect(self.cli_out)

        main_box = QHBoxLayout()

        self.textedit = QTextEdit()
        main_box.addWidget(self.textedit)

        self.pushbutton = QPushButton('Click Me')
        main_box.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.start_thread)

        self.setLayout(main_box)
        self.show()

    def start_thread(self):
        print "Staring QObject & QProcess"
        self.my_obj.launch()

    def tell_finished(self):
        print "Finished QObject & QProcess"

    def cli_out(self, lin_to_prn):
        self.textedit.append(lin_to_prn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

