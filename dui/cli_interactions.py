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


class MyQProcess(QtCore.QProcess):
    def __init__(self, parent):
        super(MyQProcess, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.run_stat = False
        self.started.connect(self.local_start)
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.readyReadStandardError.connect(self.readStdError)
        self.finished.connect(self.local_finished)

    def local_start(self):
        self.super_parent.on_started()
        self.go_btn_txt = "  Running "
        self.run_stat = True

        self.my_timer = QtCore.QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(300)

    def on_timeout(self):
        self.go_btn_txt = self.go_btn_txt[1:] + self.go_btn_txt[:1]
        self.super_parent.update_go_txt(self.go_btn_txt)

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        self.super_parent.append_line(single_line)

    def readStdError(self):
        line_string = str(self.readAllStandardError())
        self.super_parent.append_line(line_string, err_out = True)

    def local_finished(self):
        self.super_parent.on_finished()
        self.my_timer.stop()
        self.run_stat = False

class TextBrows(QtGui.QTextBrowser):
    def __init__(self):
        super(TextBrows, self).__init__()
        self.set_black_font()

    def set_black_font(self):
        self.setCurrentFont(QtGui.QFont("Monospace"))
        self.setTextColor(QtGui.QColor("black"))

    def set_green_font(self):
        self.setCurrentFont(QtGui.QFont("Monospace"))
        self.setTextColor(QtGui.QColor("green"))

    def set_red_font(self):
        self.setCurrentFont(QtGui.QFont("Monospace"))
        self.setTextColor(QtGui.QColor("red"))

    def append_black(self, to_print):
        self.set_black_font()
        self.append(to_print)

    def append_green(self, to_print):
        self.set_green_font()
        self.append(to_print)

    def append_red(self, to_print):
        self.set_red_font()
        self.append(to_print)


old_html_thing = '''
class ImgTab( QtGui.QWidget):

    def __init__(self):
        super(ImgTab, self).__init__()

        hbox =  QtGui.QHBoxLayout()


        self.web = QtWebKit.QWebView()
        my_dui_path = os.environ["DUI_PATH"]
        print "my_dui_path =", my_dui_path
        tmp_path = my_dui_path[0:len(my_dui_path) - 12]
        print "tmp_path =", tmp_path
        self.html_path = tmp_path + "/dui/xia2-report.html"
        print "self.html_path =", self.html_path
        #self.web.load(QtCore.QUrl("file:///home/lui/dui_code/trunk/dui/xia2-report.html"))
        self.web.load(QtCore.QUrl(self.html_path))
        hbox.addWidget(self.web)


        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()
#'''

class ImgTab(QtGui.QWidget):

    def __init__(self):
        super(ImgTab, self).__init__()
        #self.setGeometry(300, 300, 250, 150)


        imageLabel = QtGui.QLabel()
        image = QtGui.QImage("/home/lui/dui_code/lui_testing/PyQt4_toys/tux_n_chrome.png")

        print "Hi from ImgTab"

        imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

        scrollArea = QtGui.QScrollArea()
        scrollArea.setWidget(imageLabel)

        main_box = QtGui.QHBoxLayout()
        main_box.addWidget(scrollArea)
        self.setLayout(main_box)
        self.show()



