from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import sys

class MyQProcess(QProcess):
    def __init__(self, parent = None):
        super(MyQProcess, self).__init__()
        self.run_stat = False
        self.started.connect(self.local_start)
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.readyReadStandardError.connect(self.readStdError)
        self.finished.connect(self.local_finished)

    def local_start(self):
        self.run_stat = True

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        print ">>: ", single_line

    def readStdError(self):
        line_string = str(self.readAllStandardError())
        single_line = line_string[0:len(line_string) - 1]
        print "<< err : ", single_line

    def local_finished(self):
        self.run_stat = False
        print "\n ended \n"

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        main_box = QHBoxLayout()
        main_box.addWidget(QLabel("DIALS command: "))


        try:
            self.qProcess  = MyQProcess(self)
            #self.qProcess.setProcessChannelMode(QProcess.SeparateChannels);
            print "MyQProcess() ready"
        except:
            print "Failed to create MyQProcess()"

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

        self.qProcess.start("../PyQt4_toys/sec_interval.sh")



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())


