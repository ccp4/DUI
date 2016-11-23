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

from python_qt_bind import *

from img_viewer.img_viewer import MyImgWin
from idials_gui import TextOut
from dynamic_reindex_gui import MyReindexOpts


class WebTab(QWidget):

    def __init__(self):
        super(WebTab, self).__init__()

        print " QWebSettings.JavascriptEnabled =",  QWebSettings.JavascriptEnabled

        QWebSettings.JavascriptEnabled = True

        self.web =  QWebView()
        print "\n\n No need to load HTML file yet\n\n"

        hbox = QHBoxLayout()
        hbox.addWidget(self.web)

        #self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.show()

    def update_page(self, new_path):
        print "update_page(", new_path, ")"
        new_path = "file://" + new_path
        print "new_path:", new_path
        self.web.load(QUrl(new_path))


class outputs_widget( QWidget):
    def __init__(self, parent = None):
        super(outputs_widget, self).__init__()
        self.super_parent = parent

        #FIXME remember the upper case convention with class names

        my_box = QVBoxLayout()
        self.my_tabs = QTabWidget()

        #self.img_view = MyImgWin("/home/luiso/dui/dui_test/only_9_img/dui_idials_tst_01/dials-1/1_import/datablock.json")
        self.img_view = MyImgWin()

        self.web_view = WebTab()
        self.in_txt_out = TextOut()
        self.reindex_tool = MyReindexOpts(self)

        self.my_tabs.addTab(self.img_view, "Image View")

        self.my_tabs.addTab(self.in_txt_out, "Log View")
        self.my_tabs.addTab(self.web_view, "Report View")
        self.my_tabs.addTab(self.reindex_tool, "Re-index table")

        my_box.addWidget(self.my_tabs)

        self.pref_tab_pos = self.img_view
        self.set_pref_tab()


        self.my_tabs.currentChanged.connect(self.tab_changed)


        self.setLayout(my_box)
        self.show()


    def tab_changed(self):
        new_widg = self.my_tabs.currentWidget()
        if( new_widg != self.reindex_tool ):
            print "should update self.pref_tab_pos"
            self.pref_tab_pos = new_widg

    def set_reindex_tab(self):
        self.pref_tab_pos = self.my_tabs.currentWidget()
        self.my_tabs.setCurrentWidget(self.reindex_tool)

    def set_pref_tab(self):
        self.my_tabs.setCurrentWidget(self.pref_tab_pos)

