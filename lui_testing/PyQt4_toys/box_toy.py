from subprocess import call as shell_func
import sys

#from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Example( QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn_go =  QPushButton('\n      Go      \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setGeometry(100, 200, 1150, 850)
        self.setLayout(bg_box)
        self.setWindowTitle('Shell dialog')
        self.show()


    def B_go_clicked(self):
        print"\n Ok \n"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
