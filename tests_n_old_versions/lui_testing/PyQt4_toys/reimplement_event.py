#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
copied and hacked from ZetCode PyQt4 tutorial

hacks by Luiso

"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        # I still don't understand, when or where is the binding done?
        # who calls this function?
        # but this this piece of code works and it does widgets closes
        # when Esc is pressed

        if e.key() == QtCore.Qt.Key_Escape:
            print "Key_Escape pressed"
            self.close()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
