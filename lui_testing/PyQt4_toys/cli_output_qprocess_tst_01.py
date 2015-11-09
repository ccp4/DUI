from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MyQProcess(QProcess):
  def __init__(self):

    QProcess.__init__(self)

    self.edit  = QTextEdit()
    self.edit.setWindowTitle("QTextEdit Standard Output Redirection")
    self.edit.show()

  def readStdOutput(self):
    self.edit.append(QString(self.readAllStandardOutput()))



def main():
    app   = QApplication(sys.argv)
    qProcess  = MyQProcess()

    qProcess.setProcessChannelMode(QProcess.MergedChannels);

    qProcess.start("ls -al")

    print "running"


    qProcess.readStdOutput()


    return app.exec_()

if __name__ == '__main__':
    main()


