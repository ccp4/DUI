#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Image inside scrollable')
        self.show()

        imageLabel = QtGui.QLabel()
        image = QtGui.QImage("tux_n_chrome.png")
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

        scrollArea = QtGui.QScrollArea()
        scrollArea.setWidget(imageLabel)

        main_box = QtGui.QHBoxLayout()
        main_box.addWidget(scrollArea)
        self.setLayout(main_box)

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

