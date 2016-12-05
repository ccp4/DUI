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

import sys
from python_qt_bind import *
from img_viewer.img_viewer import MyImgWin
from dynamic_reindex_gui import MyReindexOpts
from dxtbx.model.experiment.experiment_list import ExperimentListFactory
from dials.array_family import flex

class CrystalData(object):
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.spg_group = None

        self.b11 = None
        self.b12 = None
        self.b13 = None
        self.b21 = None
        self.b22 = None
        self.b23 = None
        self.b31 = None
        self.b32 = None
        self.b33 = None


class InstrumentData(object):
    def __init__(self):
        self.u11 = None
        self.u12 = None
        self.u13 = None
        self.u21 = None
        self.u22 = None
        self.u23 = None
        self.u31 = None
        self.u32 = None
        self.u33 = None

        self.xb = None
        self.yb = None
        self.dd = None


        self.w_lambda =None

class ReflectionsData(object):
    def __init__(self):
        self.n_strng = None
        self.n_index = None
        self.n_refnd = None
        self.n_integ_sum = None
        self.n_integ_prf = None

def update_reflections(reflections_path):

    dat = ReflectionsData()

    try:
        refl_tabl = flex.reflection_table.from_pickle(reflections_path)
        dat.n_strng = refl_tabl.get_flags(refl_tabl.flags.strong).count(True)
        print "dat.n_strng =", dat.n_strng
        dat.n_index = refl_tabl.get_flags(refl_tabl.flags.indexed).count(True)
        print "dat.n_index =", dat.n_index
        dat.n_refnd = refl_tabl.get_flags(refl_tabl.flags.used_in_refinement).count(True)
        print "dat.n_refnd =", dat.n_refnd
        dat.n_integ_sum = refl_tabl.get_flags(refl_tabl.flags.integrated_sum).count(True)
        print "dat.n_integ_sum =", dat.n_integ_sum
        dat.n_integ_prf = refl_tabl.get_flags(refl_tabl.flags.integrated_prf).count(True)
        print "dat.n_integ_prf =", dat.n_integ_prf

    except:
        print "failed"

    return dat

def update_crystal(experiments_path):

    dat = CrystalData()

    try:
        experiments = ExperimentListFactory.from_json_file(
                      experiments_path, check_format=False)

        print "len(experiments)", len(experiments)

        exp = experiments[0]
        unit_cell = exp.crystal.get_unit_cell()
        dat.a, dat.b, dat.c, dat.alpha, dat.beta, dat.gamma = unit_cell.parameters()
        b_mat = exp.crystal.get_B()
        dat.b11, dat.b12, dat.b13, dat.b21, dat.b22, dat.b23, dat.b31, dat.b32, dat.b33 = b_mat.elems

    except:
        print "Unable to find cell data"

    return dat


def update_instrument(experiments_path):

    dat = InstrumentData()
    print "\n\n Hi \n\n"
    '''

    try:
        experiments = ExperimentListFactory.from_json_file(
                      experiments_path, check_format=False)

        print "len(experiments)", len(experiments)

        exp = experiments[0]
        u_mat = exp.crystal.get_U()

        dat.w_lambda = exp.beam.get_wavelength()

        dat.u11, dat.u12, dat.u13, dat.u21, dat.u22, dat.u23, dat.u31, dat.u32, dat.u33 = u_mat.elems

        #TODO find the right way to find Distance
        for expt in experiments:
            for panel in expt.detector:
                print 'Origin:', panel.get_origin()
                dat.dd = panel.get_distance()
                print 'Distance (mm)', dat.dd
            try:
                # does the beam intersect with the panel?
                dat.xb, dat.yb = panel.get_beam_centre(expt.beam.get_s0())
            except:
                print"RuntimeError, e:"
    '''
    experiments = ExperimentListFactory.from_json_file(
                  experiments_path, check_format=False)

    print "len(experiments)", len(experiments)

    exp = experiments[0]

    dat.w_lambda = exp.beam.get_wavelength()
    u_mat = exp.crystal.get_U()
    dat.u11, dat.u12, dat.u13, dat.u21, dat.u22, dat.u23, dat.u31, dat.u32, dat.u33 = u_mat.elems

    # assume details for the panel the beam intersects are the same for the whole detector
    pnl_beam_intersects = exp.detector.get_ray_intersection(exp.beam.get_s0())[0]
    pnl = exp.detector[pnl_beam_intersects]
    dist = pnl.get_distance()
    npanels = len(exp.detector)
    px_size = pnl.get_pixel_size()
    gain = pnl.get_gain()
    max_res = exp.detector.get_max_resolution(exp.beam.get_s0())

    print dir(pnl)

    print "pnl_beam_intersects             ", pnl_beam_intersects
    print "dist                            ", dist
    print "npanels                         ", npanels
    print "px_size                         ", px_size
    print "gain                            ", gain
    print "max_res                         ", max_res

    dat.dd = dist
    #dat.xb, dat.yb =


    # todo get scan data
    print exp.scan.get_image_range()
    print exp.scan.get_oscillation()
    # is this next line right? check what dials.show does
    print max(exp.scan.get_exposure_times())
    #print set(exp.scan.get_exposure_times())




    '''
    except:
        print "Unable to find instrument"
    '''

    return dat


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

        #self.super_parent = parent.super_parent

        empty_str = "__________"

        beam_group =  QGroupBox(" Beam ")

        bm_v_layout = QVBoxLayout()

        xb_label = QLabel("  X (mm) ")
        yb_label = QLabel("  Y (mm) ")

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
        w_lambda_label = QLabel("  Wavelength ang...")
        bm_v_layout.addWidget(w_lambda_label)
        self.w_lambda_data = QLabel(empty_str)
        bm_v_layout.addWidget(self.w_lambda_data)
        bm_v_layout.addWidget(QLabel("  "))

        #TODO find the angstrom symbol

        beam_group.setLayout(bm_v_layout)



        cell_group =  QGroupBox(" Crystal Cell ")


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
        cell_v_layout.addWidget(QLabel("  "))

        u_v_layout = QVBoxLayout()
        u_v_layout.addWidget(QLabel("  U matrix    "))

        u1n_data_layout = QHBoxLayout()
        self.u11_data = QLabel(empty_str)
        self.u12_data = QLabel(empty_str)
        self.u13_data = QLabel(empty_str)
        u1n_data_layout.addWidget(self.u11_data)
        u1n_data_layout.addWidget(self.u12_data)
        u1n_data_layout.addWidget(self.u13_data)

        u2n_data_layout = QHBoxLayout()
        self.u21_data = QLabel(empty_str)
        self.u22_data = QLabel(empty_str)
        self.u23_data = QLabel(empty_str)
        u2n_data_layout.addWidget(self.u21_data)
        u2n_data_layout.addWidget(self.u22_data)
        u2n_data_layout.addWidget(self.u23_data)

        u3n_data_layout = QHBoxLayout()
        self.u31_data = QLabel(empty_str)
        self.u32_data = QLabel(empty_str)
        self.u33_data = QLabel(empty_str)
        u3n_data_layout.addWidget(self.u31_data)
        u3n_data_layout.addWidget(self.u32_data)
        u3n_data_layout.addWidget(self.u33_data)


        u_v_layout.addLayout(u1n_data_layout)
        u_v_layout.addWidget(QLabel("  "))
        u_v_layout.addLayout(u2n_data_layout)
        u_v_layout.addWidget(QLabel("  "))
        u_v_layout.addLayout(u3n_data_layout)
        u_v_layout.addWidget(QLabel("  "))
        #u_mat_group.setLayout(u_v_layout)


        crys_v_layout = QVBoxLayout()

        crys_v_layout.addLayout(cell_v_layout)
        crys_v_layout.addLayout(u_v_layout)

        cell_group.setLayout(crys_v_layout)


        scan_group =  QGroupBox("          Scan       ")

        self.scan_data_01 = QLabel(empty_str)
        self.scan_data_02 = QLabel(empty_str)
        self.scan_data_03 = QLabel(empty_str)
        self.scan_data_04 = QLabel(empty_str)
        self.scan_data_05 = QLabel(empty_str)
        self.scan_data_06 = QLabel(empty_str)

        scan_v_layout = QVBoxLayout()
        scan_v_layout.addWidget(self.scan_data_01)
        scan_v_layout.addWidget(self.scan_data_02)
        scan_v_layout.addWidget(self.scan_data_03)
        scan_v_layout.addWidget(self.scan_data_04)
        scan_v_layout.addWidget(self.scan_data_05)
        scan_v_layout.addWidget(self.scan_data_06)
        scan_group.setLayout(scan_v_layout)

        detec_group =  QGroupBox("      Detector    ")
        detec_v_layout = QVBoxLayout()

        detec_v_layout.addWidget(QLabel("  "))
        d_dist_label = QLabel(" Sample - Detector \n       Distance ")
        detec_v_layout.addWidget(d_dist_label)
        self.d_dist_data = QLabel(empty_str)
        detec_v_layout.addWidget(self.d_dist_data)

        detec_v_layout.addWidget(QLabel("  "))
        n_pans_label = QLabel(" Number of panels ")
        detec_v_layout.addWidget(n_pans_label)
        self.n_pans_data = QLabel(empty_str)
        detec_v_layout.addWidget(self.n_pans_data)
        detec_v_layout.addWidget(QLabel("  "))

        detec_v_layout.addWidget(QLabel("  "))
        pix_size_label = QLabel(" Pixel size ")
        detec_v_layout.addWidget(pix_size_label)

        px_h_layout = QHBoxLayout()

        px_x_v_layout = QVBoxLayout()
        x_px_size_label = QLabel(" X(mm)")
        self.x_px_size_data = QLabel(empty_str)
        px_x_v_layout.addWidget(x_px_size_label)
        px_x_v_layout.addWidget(self.x_px_size_data)

        px_y_v_layout = QVBoxLayout()
        y_px_size_label = QLabel(" Y(mm)")
        self.y_px_size_data = QLabel(empty_str)
        px_y_v_layout.addWidget(y_px_size_label)
        px_y_v_layout.addWidget(self.y_px_size_data)

        px_h_layout.addLayout(px_x_v_layout)
        px_h_layout.addLayout(px_y_v_layout)

        detec_v_layout.addLayout(px_h_layout)


        detec_v_layout.addWidget(QLabel("  "))
        gain_label = QLabel(" Gain ")
        detec_v_layout.addWidget(gain_label)
        self.gain_data = QLabel(empty_str)
        detec_v_layout.addWidget(self.gain_data)


        detec_v_layout.addWidget(QLabel("  "))
        max_res_label = QLabel(" Max resolution ")
        detec_v_layout.addWidget(max_res_label)
        self.max_res_data = QLabel(empty_str)
        detec_v_layout.addWidget(self.max_res_data)




        detec_group.setLayout(detec_v_layout)

        inner_main_box = QHBoxLayout()
        inner_main_box.addWidget(beam_group)
        inner_main_box.addWidget(cell_group)
        #inner_main_box.addWidget(u_mat_group)
        inner_main_box.addWidget(scan_group)
        inner_main_box.addWidget(detec_group)

        my_main_box = QVBoxLayout()
        my_main_box.addLayout(inner_main_box)
        my_main_box.addStretch()

        #uncomment the next line only for debugging purpose
        #self.update_data()

        self.setLayout(my_main_box)
        self.show()

    def update_data(self, exp_json_path = None, refl_pikl_path = None):

        print "\nrefl_pikl_path =", refl_pikl_path,"\n"

        self.crys_data = update_crystal(exp_json_path)
        self.reflection_data = update_reflections(refl_pikl_path)
        self.expm_data = update_instrument(exp_json_path)

        update_data_label(self.a_data, self.crys_data.a)
        update_data_label(self.b_data, self.crys_data.b)
        update_data_label(self.c_data, self.crys_data.c)

        update_data_label(self.alpha_data, self.crys_data.alpha)
        update_data_label(self.beta_data , self.crys_data.beta)
        update_data_label(self.gamma_data, self.crys_data.gamma)

        update_data_label(self.u11_data, self.expm_data.u11)
        update_data_label(self.u12_data, self.expm_data.u12)
        update_data_label(self.u13_data, self.expm_data.u13)
        update_data_label(self.u21_data, self.expm_data.u21)
        update_data_label(self.u22_data, self.expm_data.u22)
        update_data_label(self.u23_data, self.expm_data.u23)
        update_data_label(self.u31_data, self.expm_data.u31)
        update_data_label(self.u32_data, self.expm_data.u32)
        update_data_label(self.u33_data, self.expm_data.u33)

        update_data_label(self.xb_data, self.expm_data.xb)
        update_data_label(self.yb_data, self.expm_data.yb)
        update_data_label(self.w_lambda_data, self.expm_data.w_lambda)

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


        self.my_tabs.addTab(self.img_view, "Image View")

        self.my_tabs.addTab(self.in_txt_out, "Log View")
        self.my_tabs.addTab(self.web_view, "Report View")


        if( self.super_parent.embedded_reindex == False ):
            #TODO make sure consistent the way to use the "super_parent" reference in the next line
            self.reindex_tool = MyReindexOpts(parent)
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


if( __name__ == "__main__" ):

    app =  QApplication(sys.argv)
    ex = InfoWidget()
    sys.exit(app.exec_())
