import sys

PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''

#PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "using PySide"
#'''

class MainWidget( QWidget):
    lst_commands = [
                    "import",
                    "find_spots",
                    "index",
                    "refine_bravais_settings",
                    "reindex",
                    "refine",
                    "integrate",
                    "export"
                   ]

    def __init__(self):
        super(MainWidget, self).__init__()

        self.btn_nxt =  QPushButton('\n  Next \n', self)
        #self.btn_nxt.clicked.connect(self.nxt_clicked)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_nxt)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

