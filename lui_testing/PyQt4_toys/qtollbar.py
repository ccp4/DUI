#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
hacked copy of ZetCode PySide tutorial

This program creates a toolbar.

author: Jan Bodnar, modified by Luiso

"""

import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()


        exitAction = QtGui.QAction(QtGui.QIcon('tux_n_chrome.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.close)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Toolbar')
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
