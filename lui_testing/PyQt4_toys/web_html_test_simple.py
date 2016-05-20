#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, QtWebKit
#from PySide import QtCore, QtGui, QtWebKit

import sys

class ImgTab( QtGui.QWidget):

    def __init__(self):
        super(ImgTab, self).__init__()

        print "QtWebKit.QWebSettings.JavascriptEnabled =", QtWebKit.QWebSettings.JavascriptEnabled

        QtWebKit.QWebSettings.JavascriptEnabled = True

        self.web = QtWebKit.QWebView()
        #print "dir(self.web) =", dir(self.web)

        #self.web.load(QtCore.QUrl("http://google.co.uk"))
        self.web.load(QtCore.QUrl("file:///home/luiso/dui/dui_test/test_nproc_eq_8/dials-report.html"))
        hbox =  QtGui.QHBoxLayout()
        hbox.addWidget(self.web)

        #self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ImgTab()
    sys.exit(app.exec_())




bare_html_engine = '''
app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://google.co.uk"))

#web.load(QUrl("file:///home/dev/a_tour_of_dartlang/A_Tour_of_the_Dart_Language__Dart_Up_and_Running__Dart.html"))
web.show()

sys.exit(app.exec_())
'''
