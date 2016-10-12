#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide.QtGui import *
from PySide.QtCore import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        imageLabel = QLabel()
        image = QImage("tux_n_chrome.png")
        imageLabel.setPixmap( QPixmap.fromImage(image))

        scrollArea = QScrollArea()
        scrollArea.setWidget(imageLabel)

        main_box = QHBoxLayout()
        main_box.addWidget(scrollArea)
        self.setLayout(main_box)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

