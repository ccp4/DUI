#!/usr/bin/env python
import sys
#from PySide import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui, QtWebKit

class WebWidget( QtWebKit.QWebView):

    def __init__(self):
        super(WebWidget, self).__init__()

        self.load(QtCore.QUrl("file:///scratch/dui/dui_test/X4_wide/dui_idials_test_01/dials-1/3_index/report.html"))
        #self.load(QtCore.QUrl("http://google.co.uk"))
        self.selectionChanged.connect(self.selection_changed)

    def selection_changed(self):
        print "\n self.selection_changed "

    def some_action(self):
        print "\n self.some_action "

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
        self.setWindowTitle('web View test')
        self.show()

    def B_go_clicked(self):
        print"\n go clicked "
        self.web.some_action()
        self.web.selectionChanged(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

