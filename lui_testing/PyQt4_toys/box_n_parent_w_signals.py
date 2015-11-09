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
        self.btn_go =  QPushButton('\n     Go   \n', self)
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

    def onGoClicked(self):
        print"\n Ok    from parent_widg \n"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())



'''

class A(QGroupBox):
    def __init__(self, parent=None):
        super(A, self).__init__(parent)
        self.button1= QPushButton('bt1')
        self.button1.show()

class B(QGroupBox):
    def __init__(self, parent=None):
        super(B, self).__init__(parent)
        self.line2 = QLineEdit()
        self.line2.show()

        self.connect(self.okButton, QtCore.SIGNAL("clicked()"),
                     self, QtCore.SLOT("accept()"))

ob1 = A()
ob2 = B()



Yes, create a method in object B that's
tied to a signal in object A. Note how connect is called (this is just an example):

    self.connect(self.okButton, QtCore.SIGNAL("clicked()"),
                 self, QtCore.SLOT("accept()"))

The third argument is the object with the slot, and the fourth the slot name.
The sending and receiving objects can definitely be different.


'''
