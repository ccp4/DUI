gpl = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "wprks with PyQt4"
#'''
#py_side = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "works with PySide"
#'''

import sys

class MyQProcess(QProcess):
    def __init__(self):
        super(MyQProcess, self).__init__()
        #Create an instance variable here (of type QTextEdit)
        self.edit  = QTextEdit()
        self.edit.setWindowTitle("QTextEdit Standard Output Redirection")
        self.edit.show()
        self.readyReadStandardOutput.connect(self.readStdOutput)

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        self.edit.append(single_line)

def main():

    app   = QApplication(sys.argv)

    qProcess  = MyQProcess()
    qProcess.setProcessChannelMode(QProcess.MergedChannels);
    qProcess.start("./sec_interval.sh")

    return app.exec_()

if __name__ == '__main__':
    main()


