'''
Containers for widgets related to each step

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

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os, sys

from params_live_gui_generator import PhilWidget
from simpler_param_widgets import FindspotsSimplerParameterTab, IndexSimplerParamTab, \
                                  RefineBravaiSimplerParamTab, RefineSimplerParamTab, \
                                  IntegrateSimplerParamTab, SymmetrySimplerParamTab, \
                                  ScaleSimplerParamTab#, ExportSimplerParamTab

from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index

from dials.command_line.refine_bravais_settings import phil_scope as phil_scope_r_b_settings

from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate
from dials.command_line.symmetry import phil_scope as phil_scope_symetry
from dials.command_line.scale import phil_scope as phil_scope_scale
from dials.command_line.export import phil_scope as phil_scope_export

from gui_utils import get_import_run_string, get_main_path


class ExportPage(QWidget):

    update_command_lst_low_level = pyqtSignal(list)

    '''
    This stacked widget basically helps the user to export by
    generating an MTZ file, there is no auto-generated GUI
    form Phil parameters in use withing this widget.
    '''

    def __init__(self, parent = None):
        super(ExportPage, self).__init__(parent = None)

        template_vbox =  QVBoxLayout()

        label_font = QFont()
        sys_font_point_size =  label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel(str("Export"))
        step_label.setFont(label_font)

        out_file_label = QLabel(str("mtz output name:"))

        self.simple_lin = QLineEdit(self)
        self.simple_lin.setText("integrated.mtz")
        self.simple_lin.textChanged.connect(self.update_command)

        template_vbox.addWidget(step_label)
        template_vbox.addWidget(out_file_label)
        template_vbox.addWidget(self.simple_lin)
        #template_vbox.addStretch()

        self.setLayout(template_vbox)
        self.show()

    def update_command(self):
        self.command_lst = ["export"]
        param_com = str(self.simple_lin.text())
        print "param_com =", param_com

        self.command_lst.append("mtz.hklout=" + param_com)

        self.update_command_lst_low_level.emit(self.command_lst)
        print "self.command_lst =", self.command_lst

        for lin_prn in self.command_lst:
            print "lin_prn =", lin_prn

    def gray_me_out(self):
        self.simple_lin.setEnabled(False)

    def activate_me(self):
        self.simple_lin.setEnabled(True)


class ImportPage(QWidget):

    update_command_lst_low_level = pyqtSignal(list)

    '''
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    '''

    def __init__(self, parent = None):
        super(ImportPage, self).__init__(parent = None)

        template_vbox =  QVBoxLayout()

        label_font = QFont()
        sys_font_point_size =  label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel(str("Import"))
        step_label.setFont(label_font)

        self.simple_lin =   QLineEdit(self)
        self.simple_lin.setText(" ? ")
        self.simple_lin.textChanged.connect(self.update_command)

        self.opn_fil_btn = QPushButton(" \n Select File(s) \n ")

        #######################################################################
        main_path = get_main_path()
        print "main_path =", main_path
        self.opn_fil_btn.setIcon(QIcon(main_path + "/resources/import.png"))
        self.opn_fil_btn.setIconSize(QSize(80, 48))

        #######################################################################

        tmp_hbox = QHBoxLayout()
        tmp_hbox.addWidget(self.opn_fil_btn)

        template_vbox.addWidget(step_label)
        template_vbox.addLayout(tmp_hbox)
        template_vbox.addWidget(self.simple_lin)
        #template_vbox.addStretch()

        self.opn_fil_btn.clicked.connect(self.open_files)

        #self.templ_cmd = ""
        #self.expli_templ = True
        self.defa_dir = str(os.getcwd())
        self.setLayout(template_vbox)
        self.show()

    def gray_me_out(self):
        self.simple_lin.setEnabled(False)
        self.opn_fil_btn.setEnabled(False)

    def activate_me(self):
        self.simple_lin.setEnabled(True)
        self.opn_fil_btn.setEnabled(True)

    def open_files(self):
        lst_file_path =  QFileDialog.getOpenFileNames(self, "Open File(s)",
                                                      self.defa_dir,
                                                      "All Files (*.*)")

        if(len(lst_file_path) > 0):
            new_dir, new_command = get_import_run_string(lst_file_path)

            self.simple_lin.setText(new_command)
            self.defa_dir = new_dir

    def get_arg_obj(self, sys_arg_in):
        print "sys_arg_in =", sys_arg_in
        if(sys_arg_in.template != None):
            str_arg = str(sys_arg_in.template)
            self.simple_lin.setText(str_arg)

    def update_command(self):
        print "action_simple"
        self.command_lst = ["import"]
        param_com = str(self.simple_lin.text())
        print "param_com =", param_com

        cmd_lst = param_com.split(" ")
        print "cmd_lst =", cmd_lst

        for single_com in cmd_lst:
            '''
            new_single_com = single_com.encode('utf_8')
            print "new_single_com =", new_single_com
            print "single_com =", single_com
            self.command_lst.append(new_single_com.decode('unicode_escape'))
            '''
            self.command_lst.append(single_com)

        self.update_command_lst_low_level.emit(self.command_lst)
        print "self.command_lst =", self.command_lst

        print "\n loop print \n"

        for lin_prn in self.command_lst:
            print "lin_prn =", lin_prn


class ParamAdvancedWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamAdvancedWidget, self).__init__()

        self.scrollable_widget = PhilWidget(phl_obj, parent = self)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        vbox =  QVBoxLayout()

        search_label = QLabel("search:")
        search_edit = QLineEdit("type search here")
        search_edit.textChanged.connect(self.scrollable_widget.user_searching)


        hbox = QHBoxLayout()
        hbox.addWidget(search_label)
        hbox.addWidget(search_edit)
        vbox.addLayout(hbox)

        vbox.addWidget(scrollArea)
        self.setLayout(vbox)
        self.show()


def update_lst_pair(lst_ini, str_path, str_value):
    new_lst = []
    found = False
    for pos, pair in enumerate(lst_ini):
        if(pair[0] == str_path):
            new_pair = [str_path, str_value]
            found = True

        else:
            new_pair = pair

        new_lst.append(new_pair)

    if(found == False):
        new_lst.append([str_path, str_value])

    return new_lst


def pair2string(str_path, str_value):
    str_out = str(str_path) + "=" + str(str_value)
    return str_out


def build_lst_str(cmd_0, lst_pair):
    lst_str = [cmd_0]
    for pair in lst_pair:
        str_cmd = pair2string(pair[0], pair[1])
        if(pair[1] != ""):
            lst_str.append(str_cmd)

    return lst_str


def string2pair(str_in):
    pair = None
    for pos, single_char in enumerate(str_in):
        if(single_char == "="):
            eq_pos = pos
            pair = [str_in[0:pos], str_in[pos+1:]]
            return pair


def buils_lst_pair(lst_in):
    lst_pair = []
    for par_str in lst_in[1:len(lst_in)]:
        #print "par_str =", par_str
        pair = string2pair(par_str)
        #print "pair =", pair
        lst_pair.append(pair)

    return lst_pair

class ResetButton(QPushButton):
    def __init__(self, parent = None):
        super(ResetButton, self).__init__()
        self.setContentsMargins(-5,-1,-5,-1)

        my_label = QLabel("Reset to Default")
        v_box = QVBoxLayout()
        v_box.addWidget(my_label)
        self.setLayout(v_box)
        self.show()


class ParamMainWidget( QWidget):

    update_command_lst_low_level = pyqtSignal(list)

    def __init__(self, phl_obj = None, simp_widg = None, parent = None, upper_label = None):
        super(ParamMainWidget, self).__init__()

        self.command_lst = [None]
        self.lst_pair = []

        try:
            self.my_phl_obj = phl_obj
            self.simp_widg_in = simp_widg
        except:
            print "\n\n\n something went wrong here wiht the phil object \n\n\n"

        self._vbox = QVBoxLayout()

        self.build_param_widget()

        #self.reset_btn = QPushButton("\n Reset to Default \n", self)
        self.reset_btn = ResetButton()

        self.reset_btn.clicked.connect(self.reset_par)

        label_font = QFont()
        sys_font_point_size =  label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        self.step_label = QLabel(str(upper_label))
        self.step_label.setFont(label_font)

        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)
        self._vbox.addWidget(self.reset_btn)

        self.setLayout(self._vbox)
        self.show()

    def build_param_widget(self):
        self.dual_level_tab = QTabWidget()
        self.sipler_widget = self.simp_widg_in()
        self.advanced_widget = ParamAdvancedWidget(phl_obj = self.my_phl_obj, parent = self)
        self.advanced_widget.scrollable_widget.item_changed.connect(self.update_lin_txt)

        try:
            self.sipler_widget.item_changed.connect(self.update_advanced_widget)

        except:
            print "found self.sipler_widget without << item_changed >> signal"

        self.dual_level_tab.addTab(self.sipler_widget, "Simple")
        self.dual_level_tab.addTab(self.advanced_widget, "Advanced")

    def reset_par(self):
        print "Reseting"

        for i in reversed(range(self._vbox.count())):
            widgetToRemove = self._vbox.itemAt( i ).widget()
            self._vbox.removeWidget( widgetToRemove )
            widgetToRemove.setParent( None )

        self.build_param_widget()

        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)
        self._vbox.addWidget(self.reset_btn)


        print "<< inner >>self.command_lst =", self.command_lst
        self.command_lst = [self.command_lst[0]]
        self.lst_pair = []
        print "<< inner >>self.command_lst =", self.command_lst

        self.update_command_lst_low_level.emit(self.command_lst)

        try:
            max_nproc = self.sipler_widget.set_max_nproc()
            if(max_nproc > 1):
                print "\n time to raise nproc to:", max_nproc, " \n"
                self.raise_nproc_str = str(self.sipler_widget.box_nproc.local_path) + "=" + str(max_nproc)
                QTimer.singleShot(1000, self.raise_nproc_to_max)
                print "tst 03"

        except:
            print "\n This step runs as fast as it can with nproc = 1 \n"

    def raise_nproc_to_max(self):
        found_nproc = False
        for single_par in self.command_lst:
            if("mp.nproc" in single_par):
                found_nproc = True

        if(found_nproc == False):
            self.command_lst.append(self.raise_nproc_str)
            self.update_command_lst_low_level.emit(self.command_lst)

    def update_advanced_widget(self, str_path, str_value):

        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.sipler_widget.lst_var_widg):
            for widg in bg_widg:
                try:
                    if(widg.local_path == str_path):
                        if(widg.tmp_lst == None):
                            try:
                                num_val = float(str_value)
                                widg.setValue(num_val)

                            except:
                                try:
                                    str_val = str(str_value)
                                    widg.setText(str_val)
                                    print "widg.local_path =", widg.local_path

                                except:
                                    print "\n\n Type Mismatch while searching for twin parameter \n\n"

                        else:
                            for pos, val in enumerate(widg.tmp_lst):
                                if(val == str_value):
                                    print "found val, v=", val
                                    widg.setCurrentIndex(pos)

                except:
                    pass




    def update_simpler_widget(self, str_path, str_value):

        print "update_simpler_widget(", str_path, ", ", str_value, ")"

        for widg in self.sipler_widget.lst_var_widg:
            try:
                if(widg.local_path == str_path):
                    print "found << widg.local_path == str_path >> "

                    try:
                        num_val = float(str_value)
                        widg.setValue(num_val)

                    except:
                        try:
                            for pos, val in enumerate(widg.tmp_lst):
                                if(val == str_value):
                                    print "found val, v=", val
                                    widg.setCurrentIndex(pos)

                        except:
                            print "\n\n Type Mismatch in simpler_param_widgets \n\n"

            except:
                print "skip label_str"

    def update_lin_txt(self, str_path, str_value):
        cmd_to_run = str_path + "=" + str_value
        self.update_advanced_widget(str_path, str_value)
        self.update_simpler_widget(str_path, str_value)

        self.lst_pair = update_lst_pair(self.lst_pair, str_path, str_value)
        self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)
        self.update_command_lst_low_level.emit(self.command_lst)

    def update_param_w_lst(self, lst_in):

        print "update_param_w_lst(self, ", lst_in, ")"

        self.reset_par()
        if(len(lst_in) > 1):
            new_lst_pair = buils_lst_pair(lst_in)
            self.lst_pair = new_lst_pair
            self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)

            for pair in self.lst_pair:
                self.update_advanced_widget(pair[0], pair[1])
        else:
            self.lst_pair = []
            self.command_lst = [self.command_lst[0]]

    def gray_me_out(self):
        self.reset_btn.setEnabled(False)
        palt_gray = QPalette()
        palt_gray.setColor(QPalette.WindowText, QColor(88, 88, 88, 88))
        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.advanced_widget.scrollable_widget.lst_label_widg,
                       self.sipler_widget.lst_var_widg):

            for widg in bg_widg:
                widg.setStyleSheet("color: rgba(88, 88, 88, 88)")

                try:
                    widg.setEnabled(False)

                except:
                    pass

    def activate_me(self):
        self.reset_btn.setEnabled(True)
        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.advanced_widget.scrollable_widget.lst_label_widg,
                       self.sipler_widget.lst_var_widg):

            for widg in bg_widg:

                widg.setStyleSheet("color: rgba(0, 0, 0, 255)")
                try:
                    widg.setStyleSheet(widg.style_orign)
                except:
                    pass

                try:
                    widg.setEnabled(True)

                except:
                    pass


class ParamWidget(QWidget):

    update_command_lst_medium_level = pyqtSignal(list)

    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        self.my_label = label_str

        inner_widgs = {
                       "find_spots":              [phil_scope_find_spots   , FindspotsSimplerParameterTab ],
                       "index"     :              [phil_scope_index        , IndexSimplerParamTab         ],
                       "refine_bravais_settings": [phil_scope_r_b_settings , RefineBravaiSimplerParamTab  ],
                       "refine"    :              [phil_scope_refine       , RefineSimplerParamTab        ],
                       "integrate" :              [phil_scope_integrate    , IntegrateSimplerParamTab     ],
                       "symmetry"  :              [phil_scope_symetry      , SymmetrySimplerParamTab      ],
                       "scale"     :              [phil_scope_scale        , ScaleSimplerParamTab         ]
                        }

        if(label_str == "import"):
            self.my_widget = ImportPage()

        elif(label_str == "export"):
            self.my_widget = ExportPage()

        else:
            self.my_widget = ParamMainWidget(phl_obj = inner_widgs[label_str][0],
                                             simp_widg = inner_widgs[label_str][1],
                                             parent = self, upper_label = label_str)

        self.my_widget.command_lst = [label_str]

        self.my_widget.update_command_lst_low_level.connect(self.update_parent_lst)

        v_left_box =  QVBoxLayout()
        self.my_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        v_left_box.addWidget(self.my_widget)
        self.setLayout(v_left_box)
        self.show()

    def update_param(self, curr_step):

        print "update_param(", curr_step.command_lst, ")"
        self.my_widget.update_param_w_lst(curr_step.command_lst)

    def update_parent_lst(self, command_lst):
        self.update_command_lst_medium_level.emit(command_lst)


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    #ex = ParamWidget("find_spots")
    #ex = ParamWidget("integrate")
    #ex = ParamWidget("import")
    #ex = ParamWidget("index")
    #ex = ParamWidget("refine")
    #ex = ParamWidget("integrate")
    #ex = ParamWidget("symmetry")
    #ex = ParamWidget("scale")
    ex = ParamWidget("export")
    sys.exit(app.exec_())

