from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class MyQProcess(QProcess):
    def __init__(self):
        #Call base class method
        QProcess.__init__(self)
        #Create an instance variable here (of type QTextEdit)
        self.edit  = QTextEdit()
        self.edit.setWindowTitle("QTextEdit Standard Output Redirection")
        self.edit.show()


    #Define Slot Here
    @pyqtSlot()
    def readStdOutput(self):
        self.edit.append(QString(self.readAllStandardOutput()))


def main():
    app   = QApplication(sys.argv)
    qProcess  = MyQProcess()

    qProcess.setProcessChannelMode(QProcess.MergedChannels);
    #qProcess.start("ldconfig -v")
    qProcess.start("./sec_interval.sh")

    QObject.connect(qProcess,SIGNAL("readyReadStandardOutput()"),qProcess,SLOT("readStdOutput()"));

    return app.exec_()

if __name__ == '__main__':
    main()


