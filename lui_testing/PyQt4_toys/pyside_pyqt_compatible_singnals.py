from subprocess import call as shell_func
import sys

PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#Signal = pyqtSignal
print "using PyQt4"
#'''

#PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
pyqtSignal = Signal
print "using PySide"
#'''

class inner_widg( QWidget):
    goClicked = pyqtSignal()
    def __init__(self, parent):
        super(inner_widg, self).__init__()

        self.btn_go =  QPushButton('\n      Go   \n', self)
        #self.btn_go.clicked.connect(self.B_go_clicked)
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

        self.inner_btn = inner_widg(self)
        hbox =  QHBoxLayout()
        hbox.addWidget(self.inner_btn)
        self.inner_btn.goClicked.connect(self.to_be_caled_from_son_widg)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def to_be_caled_from_son_widg(self):
        print "from parent parent_widget"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
