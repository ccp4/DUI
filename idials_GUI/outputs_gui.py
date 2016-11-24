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
from dynamic_reindex_gui import MyReindexOpts



class CrystalData(object):
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.spg_group = None


class InstrumentData(object):
    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.r3 = None
        self.xb = None
        self.yb = None
        self.dd = None

def update_crystal(experiments_path):

    dat = CrystalData()

    try:

        from dxtbx.model.experiment.experiment_list import ExperimentListFactory
        experiments = ExperimentListFactory.from_json_file(
                      experiments_path, check_format=False)

        print "len(experiments)", len(experiments)

        exp = experiments[0]
        unit_cell = exp.crystal.get_unit_cell()
        dat.a, dat.b, dat.c, dat.alpha, dat.beta, dat.gamma = unit_cell.parameters()

    except:
        print "Unable to find cell data"

    return dat


def update_intrument():
    exp_dat = InstrumentData()

    return exp_dat


def update_data_label(data_label, data_info):
    if( data_info == None ):
        data_label.setText("   -      ")
        data_label.setStyleSheet("background-color: white")

    else:
        rnd_nm = round(data_info, ndigits=4)
        data_label.setText(str(rnd_nm))
        data_label.setStyleSheet("background-color: white")


class InfoWidget( QWidget):
    def __init__(self, parent = None):
        super(InfoWidget, self).__init__()

        cell_group =  QGroupBox(" Crystal Cell ")

        empty_str = "__________"

        cell_v_layout = QVBoxLayout()

        a_label = QLabel("   a ")
        b_label = QLabel("   b ")
        c_label = QLabel("   c ")
        cell_label_d_layout = QHBoxLayout()
        cell_label_d_layout.addWidget(a_label)
        cell_label_d_layout.addWidget(b_label)
        cell_label_d_layout.addWidget(c_label)
        cell_v_layout.addLayout(cell_label_d_layout)

        self.a_data = QLabel(empty_str)
        self.b_data = QLabel(empty_str)
        self.c_data = QLabel(empty_str)
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(self.a_data)
        cell_data_layout.addWidget(self.b_data)
        cell_data_layout.addWidget(self.c_data)
        cell_v_layout.addLayout(cell_data_layout)
        cell_v_layout.addWidget(QLabel("  "))

        alpha_label = QLabel("  alpha ")
        beta_label = QLabel("   beta ")
        gamma_label = QLabel("  gamma ")
        cell_label_a_layout = QHBoxLayout()
        cell_label_a_layout.addWidget(alpha_label)
        cell_label_a_layout.addWidget(beta_label)
        cell_label_a_layout.addWidget(gamma_label)
        cell_v_layout.addLayout(cell_label_a_layout)

        self.alpha_data = QLabel(empty_str)
        self.beta_data = QLabel(empty_str)
        self.gamma_data = QLabel(empty_str)
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(self.alpha_data)
        cell_data_layout.addWidget(self.beta_data)
        cell_data_layout.addWidget(self.gamma_data)
        cell_v_layout.addLayout(cell_data_layout)

        cell_group.setLayout(cell_v_layout)

        orien_group =  QGroupBox(" Crystal Orientation ")

        r_v_layout = QVBoxLayout()
        r1_label = QLabel("  R 1 ")
        r2_label = QLabel("  R 2 ")
        r3_label = QLabel("  R 3 ")

        r_label_a_layout = QHBoxLayout()
        r_label_a_layout.addWidget(r1_label)
        r_label_a_layout.addWidget(r2_label)
        r_label_a_layout.addWidget(r3_label)

        r_v_layout.addLayout(r_label_a_layout)

        self.r1_data = QLabel(empty_str)
        self.r2_data = QLabel(empty_str)
        self.r3_data = QLabel(empty_str)
        r_data_layout = QHBoxLayout()
        r_data_layout.addWidget(self.r1_data)
        r_data_layout.addWidget(self.r2_data)
        r_data_layout.addWidget(self.r3_data)
        r_v_layout.addLayout(r_data_layout)
        orien_group.setLayout(r_v_layout)


        beam_group =  QGroupBox(" Bean / Source ")

        bm_v_layout = QVBoxLayout()

        xb_label = QLabel("  X Beam ")
        yb_label = QLabel("  Y Beam ")

        bm_label_a_layout = QHBoxLayout()
        bm_label_a_layout.addWidget(xb_label)
        bm_label_a_layout.addWidget(yb_label)

        bm_v_layout.addLayout(bm_label_a_layout)

        self.xb_data = QLabel(empty_str)
        self.yb_data = QLabel(empty_str)
        bm_data_layout = QHBoxLayout()
        bm_data_layout.addWidget(self.xb_data)
        bm_data_layout.addWidget(self.yb_data)
        bm_v_layout.addLayout(bm_data_layout)

        bm_v_layout.addWidget(QLabel("  "))
        d_dist_label = QLabel("  Detector Distance ")
        bm_v_layout.addWidget(d_dist_label)
        self.d_dist_data = QLabel(empty_str)
        bm_v_layout.addWidget(self.d_dist_data)
        bm_v_layout.addWidget(QLabel("  "))

        beam_group.setLayout(bm_v_layout)

        my_box = QVBoxLayout()
        my_box.addWidget(cell_group)
        my_box.addWidget(orien_group)
        my_box.addWidget(beam_group)

        #next 3 lines and connections will be removed when this goes to the main GUI
        update_data = QPushButton(self)
        update_data.clicked.connect(self.btn_clicked)
        my_box.addWidget(update_data)

        self.setLayout(my_box)
        self.show()

    def btn_clicked(self):
        self.update_data()

    def update_data(self, exp_json_path = None):

        #self.crys_data = update_crystal(
        #"/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/3_index/experiments.json")

        self.crys_data = update_crystal(exp_json_path)

        self.expm_data = update_intrument()
        self.expm_data = InstrumentData()

        update_data_label(self.a_data, self.crys_data.a)
        update_data_label(self.b_data, self.crys_data.b)
        update_data_label(self.c_data, self.crys_data.c)

        update_data_label(self.alpha_data, self.crys_data.alpha)
        update_data_label(self.beta_data , self.crys_data.beta)
        update_data_label(self.gamma_data, self.crys_data.gamma)

        update_data_label(self.r1_data, self.expm_data.r1)
        update_data_label(self.r2_data, self.expm_data.r2)
        update_data_label(self.r3_data, self.expm_data.r3)
        update_data_label(self.xb_data, self.expm_data.xb)
        update_data_label(self.yb_data, self.expm_data.yb)
        update_data_label(self.d_dist_data, self.expm_data.dd)



class TextOut( QTextBrowser):
    def __init__(self, parent = None):
        super(TextOut, self).__init__(parent)
        self.set_black_font()
        self.content_lst = []

    def set_black_font(self):
        self.setCurrentFont( QFont("Monospace"))
        self.setTextColor( QColor("black"))

    def set_green_font(self):
        self.setCurrentFont( QFont("Monospace"))
        self.setTextColor( QColor("green"))

    def set_red_font(self):
        self.setCurrentFont( QFont("Monospace"))
        self.setTextColor( QColor("red"))

    def append_black(self, to_print):
        self.moveCursor(QTextCursor.End)
        self.set_black_font()
        self.append(to_print)
        self.content_lst.append(to_print)

    def append_green(self, to_print):
        self.moveCursor(QTextCursor.End)
        self.set_green_font()
        self.append(to_print)
        self.content_lst = []

    def append_red(self, to_print):
        self.moveCursor(QTextCursor.End)
        self.set_red_font()
        self.append(to_print)

    def get_full_output_lst(self):
        return self.content_lst


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

