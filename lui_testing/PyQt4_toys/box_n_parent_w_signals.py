from subprocess import call as shell_func
import sys

#from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *



class inner_widg( QWidget):

    goClicked = pyqtSignal()

    def __init__(self, parent):
        super(inner_widg, self).__init__()
        self.parent_widget = parent
        self.initUI()

    def initUI(self):
        self.btn_go =  QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.goClicked)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setLayout(bg_box)
        self.show()

class MainWidget( QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn_go = inner_widg(self)
        self.btn_go.goClicked.connect(self.onGoClicked)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)

        self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()
    def to_be_caled_from_son_widg(self, n):
        print "n =", n

        print "from parent parent_widget"
    def onGoClicked(self):
        print"\n Ok    from inner_widg \n"
        self.to_be_caled_from_son_widg(4)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
