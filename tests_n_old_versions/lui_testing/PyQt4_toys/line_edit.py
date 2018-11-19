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

        self.btn_go =  QPushButton('\n     Go   \n', self)
        self.btn_go.clicked.connect(self.goClicked)


        tmp_widg = QLineEdit()
        tmp_widg.setText("")
        tmp_widg.textChanged.connect(self.line_txt_changed)


        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)
        hbox.addWidget(tmp_widg)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setLayout(bg_box)
        self.show()


    def line_txt_changed(self):
        print "ed"

class MainWidget( QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.btn_go = inner_widg(self)
        self.btn_go.goClicked.connect(self.onGoClicked)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def onGoClicked(self):
        print"\n Ok    from parent_widg \n"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

