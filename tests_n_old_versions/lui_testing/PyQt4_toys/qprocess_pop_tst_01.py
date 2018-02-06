#gpl = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "wprks with PyQt4"
#'''
py_side = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "works with PySide"
#'''

import sys

class MyQProcess(QProcess):
    def __init__(self):
        super(MyQProcess, self).__init__()

        self.started.connect(self.on_start)
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.finished.connect(self.on_finish)

    def on_start(self):
        print "on_start"

    def on_finish(self):
        print "on_finish"

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        print ">>", single_line

if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = QWidget()
    my_widg.setWindowTitle("QTextEdit Standard Output Redirection")
    my_widg.show()

    qProcess  = MyQProcess()
    qProcess.setProcessChannelMode(QProcess.MergedChannels);
    qProcess.start("./sec_interval.sh")

    sys.exit(app.exec_())


