#!/usr/bin/env python
import sys
#from PySide import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui, QtWebKit

class inner_widg( QtGui.QWidget):

    def __init__(self, parent):
        super(inner_widg, self).__init__()
        self.parent_widget = parent

        self.btn_go = QtGui.QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        hbox =  QtGui.QHBoxLayout()
        hbox.addWidget(self.btn_go)

        bg_box =  QtGui.QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setLayout(bg_box)
        self.show()

    def B_go_clicked(self):
        print"\n Ok    from inner_widg \n"
        self.parent_widget.to_be_caled_from_son_widg(4)

class WebWidget( QtWebKit.QWebView):

    def __init__(self):
        super(WebWidget, self).__init__()

        self.load(QtCore.QUrl("file:///scratch/dui/dui_test/X4_wide/dui_idials_test_01/dials-1/3_index/report.html"))
        #self.load(QtCore.QUrl("http://google.co.uk"))

class MainWidget( QtGui.QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.btn_go = inner_widg(self)

        hbox =  QtGui.QHBoxLayout()
        hbox.addWidget(self.btn_go)
        self.web = WebWidget()
        hbox.addWidget(self.web)

        self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def to_be_caled_from_son_widg(self, n):
        print "n =", n
        print "from parent parent_widget"

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

