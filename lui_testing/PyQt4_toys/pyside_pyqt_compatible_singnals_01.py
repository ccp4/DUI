from subprocess import call as shell_func
import sys

PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''

#PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
pyqtSignal = Signal
print "using PySide"
#'''

class MainWidget( QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.btn_go_01 =  QPushButton('\n      Go 01  \n', self)
        self.btn_go_01.clicked.connect(self.clickeado)

        self.btn_go_02 =  QPushButton('\n      Go 02  \n', self)
        self.btn_go_02.clicked.connect(self.clickeado)

        hbox =  QHBoxLayout()

        hbox.addWidget(self.btn_go_01)
        hbox.addWidget(self.btn_go_02)

        self.setLayout(hbox)
        self.show()



        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def clickeado(self, num = 5):
        sender = self.sender()
        print "sender =", sender

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
