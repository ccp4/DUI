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
    def __init__(self, parent = None):
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




first_attempt_w_png_files = '''
class ImgTab(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ImgTab, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog


        self.imageLabel = QtGui.QLabel()
        self.image = QtGui.QImage("/home/lui/dui_code/lui_testing/PyQt4_toys/tux_n_chrome.png")
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.image))

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidget(self.imageLabel)

        main_box = QtGui.QHBoxLayout()
        main_box.addWidget(self.scrollArea)
        self.setLayout(main_box)
        self.show()


    def update_img(self):

        #try:
        print "dir_name(w_dir) =", self.super_parent.w_dir
        print "self.super_parent.w_dir =", self.super_parent.w_dir
        img_path = self.super_parent.w_dir + "/output/analysis/centroid/" + "centroid_diff_x.png"
        print "img_path =", img_path

        self.imageLabel = QtGui.QLabel(img_path)
        self.image = QtGui.QImage()
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.image))

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setWidget(self.imageLabel)

        print "img updated internally"
        self.super_parent.update()
        self.super_parent.repaint()
        #self.refresh()


        #except:
        #    print "NON existent self.super_parent.w_dir Var"


        #pop_viewers_layout = QtGui.QHBoxLayout()
        #pop_viewers_layout.addWidget(pop_ref_view_but)
        #pop_viewers_layout.addWidget(pop_but)
        #right_side_layout = QtGui.QVBoxLayout()
        #
        #right_side_layout.addLayout(pop_viewers_layout)
        #horizontalLayout.addLayout(right_side_layout)
        #'''


class ImgWidg(QtGui.QWidget):
    def __init__(self, parent = None, img_path_lst = None):
        super(ImgWidg, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        bg_box =  QtGui.QHBoxLayout(self)
        #img_path = self.super_parent.w_dir + "/output/analysis/centroid/" + "centroid_diff_x.png"
        img_path = "/home/lui/dui_code/lui_testing/PyQt4_toys/img_layouts/" + "centroid_diff_x.png"
        img_path_lst = [img_path]
        print "img_path_lst[0] =", img_path_lst[0]

        for single_img_path in img_path_lst:

            imageLabel = QtGui.QLabel()
            image = QtGui.QImage(single_img_path)
            imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

            bg_box.addWidget(imageLabel)

        self.setLayout(bg_box)
        self.show()


class ImgTab(QtGui.QScrollArea):

    def __init__(self, parent = None, lst_img = None):
        super(ImgTab, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.imageWidg = ImgWidg(self.super_parent, lst_img)
        self.setWidget(self.imageWidg)
        self.show()

    def update_me(self, lst_img = None):
        print "update_me(self)"

        self.imageWidg = ImgWidg(self, lst_img)
        self.setWidget(self.imageWidg)
        self.show()


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
