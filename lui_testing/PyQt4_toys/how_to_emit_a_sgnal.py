#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
copied from ZetCode PyQt4 tutorial
and hacked by Luiso
"""

import sys
from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
    clickApp = QtCore.pyqtSignal()

class inner_widg(QtGui.QWidget):

    def __init__(self):
        super(inner_widg, self).__init__()

        self.btn_go =  QtGui.QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.btn_go)


        self.c = Communicate()
        self.c.clickApp.connect(self.cliqueado)


        bg_box = QtGui.QVBoxLayout(self)
        bg_box.addLayout(hbox)
        self.setLayout(bg_box)
        self.show()

    def B_go_clicked(self):
        print"\n Ok    from inner_widg \n"

    def cliqueado(self):
        self.c.clickApp.emit()
        print "from cliqueado(self, event)"


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        my_wg = inner_widg()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(my_wg)

        main_widget = QtGui.QWidget()
        main_widget.setLayout(mainLayout)
        self.setCentralWidget(main_widget)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()


    def tst_func(self):
        print "from tst_func"


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
