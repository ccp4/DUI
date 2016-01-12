#!/usr/bin/env python

import sys

#from PySide import QtCore, QtGui, QtWebKit
from PyQt4 import QtCore, QtGui, QtWebKit

from subprocess import call as shell_func
import sys

class inner_widg( QtGui.QWidget):

    def __init__(self, parent):
        super(inner_widg, self).__init__()
        self.parent_widget = parent
        self.initUI()

    def initUI(self):
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


class MainWidget( QtGui.QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.btn_go = inner_widg(self)


        self.web = QtWebKit.QWebView()
        self.web.load(QtCore.QUrl("file:///home/lui/dui_code/trunk/dui/xia2-report.html"))


        hbox =  QtGui.QHBoxLayout()
        hbox.addWidget(self.btn_go)
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




bare_html_engine = '''
app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://google.co.uk"))

#web.load(QUrl("file:///home/dev/a_tour_of_dartlang/A_Tour_of_the_Dart_Language__Dart_Up_and_Running__Dart.html"))
web.show()

sys.exit(app.exec_())
'''
