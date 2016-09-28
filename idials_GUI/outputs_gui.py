'''
Users info outputs widget for DUI

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

from python_qt_bind import GuiBinding
if GuiBinding.pyhon_binding == "PyQt4":
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *
    print "   <<<   using PyQt4"

else:
    #asuming GuiBinding.pyhon_binding == "PySide"
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtWebKit import *
    print "using PySide"

from img_viewer.image_viewer_w_opengl import MyImgWin

class WebTab(QWidget):

    def __init__(self):
        super(WebTab, self).__init__()

        print " QWebSettings.JavascriptEnabled =",  QWebSettings.JavascriptEnabled

        QWebSettings.JavascriptEnabled = True

        self.web =  QWebView()

        #self.web.load(QUrl("file:///home/luiso/dui/dui_test/only_9_img/dui_idials_GUI_tst_09/dials-1/8_refine/report.html"))
        self.web.load(QUrl("file:///home/luiso/dui/dui_test/only_9_img/dui_idials_GUI_tst_09/dials-1/8_refine/report.html"))

        hbox = QHBoxLayout()
        hbox.addWidget(self.web)

        #self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def update_page(self, new_path):
        print "update_page(", new_path, ")"
        new_path = "file://" + new_path
        print "new_path:", new_path
        self.web.load(QUrl(new_path))


class outputs_widget( QWidget):

    #item_changed = pyqtSignal()
    def __init__(self, phl_obj, parent = None):
        super(outputs_widget, self).__init__(parent)
        #self.super_parent = parent

        my_box = QVBoxLayout()
        v_splitter = QSplitter()

        v_splitter.setOrientation(Qt.Vertical)

        self.img_view = MyImgWin()
        self.web_view = WebTab()

        v_splitter.addWidget(self.img_view)
        v_splitter.addWidget(self.web_view)
        my_box.addWidget(v_splitter)

        self.setLayout(my_box)
        self.show()

