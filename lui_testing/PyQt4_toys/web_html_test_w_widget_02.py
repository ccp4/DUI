#!/usr/bin/env python
import sys
#from PySide import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui, QtWebKit

class WebWidget( QtWebKit.QWebView):

    def __init__(self):
        super(WebWidget, self).__init__()

        self.load(QtCore.QUrl("file:///scratch/dui/dui_test/X4_wide/dui_idials_test_01/dials-1/3_index/report.html"))
        #self.load(QtCore.QUrl("http://google.co.uk"))

class MainWidget( QtGui.QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()

        hbox =  QtGui.QHBoxLayout()

        self.btn_go = QtGui.QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)
        hbox.addWidget(self.btn_go)
        self.web = WebWidget()
        hbox.addWidget(self.web)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def B_go_clicked(self):
        print"\n go clicked \n"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

