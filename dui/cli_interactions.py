'''
import subprocess
import sys
'''

import os

from resources.python_qt_bind import GuiBinding
gui_lib = GuiBinding()
print "using ", gui_lib.pyhon_binding
qt_tool = gui_lib.pyhon_binding

if( qt_tool == "PyQt4" ):
    from PyQt4 import QtCore, QtGui, QtWebKit

else:
    from PySide import QtCore, QtGui, QtWebKit



class TextBrows(QtGui.QTextBrowser):
    def __init__(self):
        super(TextBrows, self).__init__()
        #self.multi_line_txt = QtGui.QTextBrowser()
        #self.multi_line_txt.setMaximumHeight(724)
        #self.multi_line_txt.setMinimumHeight(24)

class ImgTab( QtGui.QWidget):

    def __init__(self):
        super(ImgTab, self).__init__()

        self.web = QtWebKit.QWebView()

        my_dui_path = os.environ["DUI_PATH"]
        print "my_dui_path =", my_dui_path
        tmp_path = my_dui_path[0:len(my_dui_path) - 12]
        print "tmp_path =", tmp_path
        self.html_path = tmp_path + "/dui/xia2-report.html"
        print "self.html_path =", self.html_path


        #self.web.load(QtCore.QUrl("file:///home/lui/dui_code/trunk/dui/xia2-report.html"))
        self.web.load(QtCore.QUrl(self.html_path))


        hbox =  QtGui.QHBoxLayout()
        hbox.addWidget(self.web)

        #self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()
