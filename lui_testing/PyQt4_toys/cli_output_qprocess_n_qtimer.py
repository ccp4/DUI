gpl = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "testing with PyQt4"
#'''
#py_side = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "testing with PySide"
#'''

import sys

class MyQProcess(QProcess):
    def __init__(self):
        super(MyQProcess, self).__init__()
        #Create an instance variable here (of type QTextEdit)
        self.edit  = QTextEdit()
        self.edit.setWindowTitle("QTextEdit Standard Output Redirection")
        self.edit.show()
        self.started.connect(self.on_start)
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.finished.connect(self.on_finish)

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        self.edit.append(single_line)

    def on_start(self):
        print "on_start"
        self.my_timer = QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(500)

    def on_finish(self):
        print "on_finish"
        self.my_timer.stop()

    def on_timeout(self):
        print "on_timeout"

def main():

    app   = QApplication(sys.argv)

    qProcess  = MyQProcess()
    print "after MyQProcess.__init__()"
    qProcess.setProcessChannelMode(QProcess.MergedChannels);
    print "after (setProcessChannelMode(QProcess.MergedChannels)"
    qProcess.start("./sec_interval.sh")

    return app.exec_()

if __name__ == '__main__':
    main()


