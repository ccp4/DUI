'''
DUI's utilities for interactions with shell commands

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.




import os
from subprocess import call as shell_func

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


class CmdLine(QtGui.QTextBrowser):

    '''
    This class emulates QtGui.QLineEdit but with several lines
    here will be contained the commands that DUI will run
    '''

    def __init__(self):
        super(CmdLine, self).__init__()
        print "\n\n CmdLine(ready) \n\n "

        # QtGui.QSizePolicy.Fixed
        self.setSizePolicy( QtGui.QSizePolicy.Minimum , QtGui.QSizePolicy.Maximum )

    def set_text(self, lin_str):
        self.clear()
        self.append(lin_str)
        self.current_line = lin_str

    def get_text(self):
        return self.current_line


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



class ImgWidg(QtGui.QWidget):
    def __init__(self, parent = None, img_path_lst = None):
        super(ImgWidg, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        bg_box =  QtGui.QHBoxLayout(self)
        img_path = self.super_parent.w_dir + "/spot_find_output/analysis/strong/" + "spots_per_image.png"

        #/home/lui/dui_testind_w_imgs/only_10_img/New_04/analysis/strong

        #img_path = "/home/lui/dui_code/lui_testing/PyQt4_toys/img_layouts/" + "centroid_diff_x.png"
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

        self.imageWidg = ImgWidg(self.super_parent, lst_img)
        self.setWidget(self.imageWidg)
        self.show()






class HtmlWidg( QtGui.QWidget):

    def __init__(self, parent = None):
        super(HtmlWidg, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        self.hbox =  QtGui.QHBoxLayout()
        self.web = QtWebKit.QWebView()

        my_path = self.super_parent.w_dir
        self.html_path = "file://" + my_path + "/dials-report.html"

        self.web.load(QtCore.QUrl(self.html_path))
        self.hbox.addWidget(self.web)

        self.setLayout(self.hbox)
        self.show()

class HtmlTab( QtGui.QWidget ):
    def __init__(self, parent = None):
        super(HtmlTab, self).__init__()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog



    def update_me(self):
        print "\n updating HTML \n"
        self.my_box =  QtGui.QHBoxLayout()
        self.html_widg = HtmlWidg(self.super_parent)
        self.my_box.addWidget(self.html_widg)
        self.setLayout(self.my_box)
        self.show()
        print "\n Done updating HTML \n"


