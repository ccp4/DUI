from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import sys

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.super_parent = self

        main_box = QHBoxLayout()
        main_box.addWidget(QLabel("DIALS command: "))

        self.cmd_edit = QLineEdit()
        self.cmd_edit.editingFinished.connect(self.cmd_entr)

        main_box.addWidget(self.cmd_edit)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

    def cmd_entr(self):
        new_cmd = self.cmd_edit.text()
        print "command entered:", new_cmd

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

