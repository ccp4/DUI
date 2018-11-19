from subprocess import call as shell_func
import sys

#from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *



class inner_widg( QWidget):

    goClicked = pyqtSignal()
    txt_changed = pyqtSignal(str)

    def __init__(self, parent):
        super(inner_widg, self).__init__()
        self.parent_widget = parent

        self.btn_go =  QPushButton('\n     Go   \n', self)
        self.btn_go.clicked.connect(self.goClicked)


        self.line_ed = QLineEdit()
        self.line_ed.setText("")
        self.line_ed.textChanged.connect(self.line_txt_changed)


        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)
        hbox.addWidget(self.line_ed)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setLayout(bg_box)
        self.show()


    def line_txt_changed(self):
        print "ed"
        new_str = str(self.line_ed.text())
        self.txt_changed.emit(new_str)

class MainWidget( QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.btn_go = inner_widg(self)
        self.btn_go.goClicked.connect(self.onGoClicked)
        self.btn_go.txt_changed.connect(self.on_txt_changed)
        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def onGoClicked(self):
        print"\n Ok    from parent_widg \n"

    def on_txt_changed(self, txt):
        print "new_str =", txt

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

