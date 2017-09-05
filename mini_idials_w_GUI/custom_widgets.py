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
                                   RefineSimplerParamTab, IntegrateSimplerParamTab

from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index
from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate
from dials.command_line.export import phil_scope as phil_scope_export

def template_right_side_build(in_str_tmp, dir_path):

    #print "in_str_tmp =", in_str_tmp
    #print "dir_path =", dir_path

    out_str = in_str_tmp + dir_path
    lst_files = os.listdir(str(dir_path))

    #for i, e in reversed(list(enumerate(a))):
    #for pos, single_char in enumerate(in_str_tmp):
    for pos, single_char in reversed(list(enumerate(in_str_tmp))):
        if(single_char == "."):
            pos_sep = pos

    left_sd_name = in_str_tmp[:pos_sep]
    print "\n left_sd_name =", left_sd_name, "\n"

    ext_name = in_str_tmp[pos_sep:]
    print "\n ext_name =", ext_name, "\n"


    out_str = left_sd_name

    max_tail_size = int(len(in_str_tmp) / 3)
    print "\n max_tail_size =", max_tail_size, "\n"
    for tail_size in xrange(max_tail_size):
        #print "tail_size =", tail_size
        prev_str = out_str
        pos_to_replase = len(out_str) - tail_size - 1
        #print "pos_to_replase =", pos_to_replase
        for num_char in '0123456789':
            if out_str[pos_to_replase] == num_char:
                out_str = out_str[:pos_to_replase] + '#' + out_str[pos_to_replase + 1:]

        #print "new out_str =", out_str
        if(prev_str == out_str):
            #print "found non num char"
            break

    out_str = out_str + ext_name
    return out_str


def template_from_lst_build(in_str_lst):
    print "in_str_lst =", in_str_lst
    str_lst = []
    for single_qstring in in_str_lst:
        str_lst.append(str(single_qstring))

    print "str_lst =", str_lst

    out_str = ""
    for pos in xrange(len(str_lst[0])):
        all_equal = True
        single_char = str_lst[0][pos]
        for single_string in str_lst:
            if(single_string[pos] != single_char):
                all_equal = False

        if(all_equal == True):
            out_str = out_str + single_char

        else:
            out_str = out_str + "#"

    print "out_str =", out_str

    return out_str


class FileOrDir(QFileDialog):
    def __init__(self, parent = None):
        super(FileOrDir, self).__init__(parent = None)
        get_wor_dir = os.getcwd()
        self.setDirectory(str(get_wor_dir))
        self.setFileMode(QFileDialog.Directory)


class ImportPage(QWidget):

    '''
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    '''

    def __init__(self, parent = None):
        super(ImportPage, self).__init__(parent = None)
        #self.super_parent = parent.super_parent # reference across the hole GUI to MyMainDialog

        template_grp =  QGroupBox("Import Template ")
        template_vbox =  QHBoxLayout()
        self.templ_lin =   QLineEdit(self)
        self.templ_lin.setText("template = ?")
        template_vbox.addWidget(self.templ_lin)
        template_grp.setLayout(template_vbox)

        mainLayout =  QVBoxLayout()
        #mainLayout.addWidget(import_path_group)
        mainLayout.addWidget(template_grp)

        big_layout =  QHBoxLayout()
        big_layout.addLayout(mainLayout)

        self.setLayout(big_layout)
        self.show()

        #TODO remove next commented stuff if appliable
        #self.done_import = False

    def __call__(self):
        print "from __call__   << import page >>"
        if(str(self.templ_lin.text()) == "template = ?"):
            self.find_my_img_dir()


        #TODO remove next commented stuff if appliable
        Deprecated = '''
        if(self.done_import == False):
            self.find_my_img_dir()
            print "( self.done_import == False )"
        '''

    def find_my_img_dir(self, event = None):

        selector = FileOrDir(self)
        #selected_file_path = str(selector.getOpenFileName(self, "Open IMG Dir"))
        lst_file_path = selector.getOpenFileNames(self, "Open IMG Dir")
        #getOpenFileNamesAndFilter

        print "[ file path selected ] =", lst_file_path
        print "len(lst_file_path) =", len(lst_file_path)

        for single_string in lst_file_path:
            print "single_string =", single_string

        if(lst_file_path and len(lst_file_path) == 1):
            selected_file_path = str(lst_file_path[0])

            print "\n selected_file_path =", selected_file_path, "\n"
            print "type(selected_file_path) =", type(selected_file_path)

            for pos, single_char in enumerate(selected_file_path):
                if(single_char == "/" or single_char == "\\"):
                    pos_sep = pos

            dir_name = selected_file_path[:pos_sep]
            if(dir_name[0:3] == "(u\'"):
                print "dir_name[0:3] == \"(u\'\""
                dir_name = dir_name[3:]

            print "dir_name(final) =", dir_name

            templ_str_tmp = selected_file_path[pos_sep:]
            #print "templ_str_tmp =", templ_str_tmp

            templ_r_side = template_right_side_build(templ_str_tmp, dir_name)

            templ_str_final = dir_name + templ_r_side
            self.templ_lin.setText(templ_str_final)

        elif(len(lst_file_path) > 1):
            print "time to handle multiple files selected"
            templ_str_final = template_from_lst_build(lst_file_path)
            print "templ_str_final =", templ_str_final
            self.templ_lin.setText(templ_str_final)

        else:
            print "Failed to pick dir"

        #print "\ncalling:\n self.super_parent.idials_widget.failed == None\n"
        #self.super_parent.idials_widget.failed = None



class ParamAdvancedWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamAdvancedWidget, self).__init__()

        #self.super_parent = parent.super_parent
        #self.param_widget_parent = parent.param_widget_parent

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
        print "par_str =", par_str
        pair = string2pair(par_str)
        print "pair =", pair
        lst_pair.append(pair)

    return lst_pair

class ParamMainWidget( QWidget):
    #str_param_signal = pyqtSignal(str)
    def __init__(self, phl_obj = None, simp_widg = None, parent = None, upper_label = None):
        super(ParamMainWidget, self).__init__()

        self.command_lst = [None]
        self.lst_pair = []

        try:
            #self.super_parent = parent.super_parent
            self.my_phl_obj = phl_obj
            self.simp_widg_in = simp_widg
        except:
            print "\n\n\n something went wrong here wiht the phil object \n\n\n"



        #self.param_widget_parent = self

        self._vbox = QVBoxLayout()

        self.build_param_widget()

        self.reset_btn = QPushButton("Reset to Default", self)
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
        self.sipler_widget = self.simp_widg_in(parent = self) #TODO make sure you need to do: parent = self

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

        #self.super_parent.reset_param()


        try:
            self.sipler_widget.set_max_nproc()
            print "\n Tunning nproc to maximum \n"

        except:
            print "\n This step runs as fas as it can with nproc = 1 \n"


    def update_advanced_widget(self, str_path, str_value):

        for bg_widg in(self.advanced_widget.scrollable_widget.lst_wgs ,
                       self.sipler_widget.lst_wgs):
            for widg in bg_widg:
                if(widg.local_path == str_path):
                    if(widg.tmp_lst == None):
                        try:
                            num_val = float(str_value)
                            widg.setValue(num_val)

                        except:
                            print "\n\n Type Mismatch while searching for twin parameter \n\n"

                    else:
                        for pos, val in enumerate(widg.tmp_lst):
                            if(val == str_value):
                                print "found val, v=", val
                                widg.setCurrentIndex(pos)

    def update_lin_txt(self, str_path, str_value):

        print "self.command_lst =", self.command_lst

        cmd_to_run = str_path + "=" + str_value
        print "adjusting parameter: {", cmd_to_run,"}"
        self.update_advanced_widget(str_path, str_value)

        self.lst_pair = update_lst_pair(self.lst_pair, str_path, str_value)
        print "self.lst_pair =", self.lst_pair
        self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)

        print "self.command_lst =", self.command_lst, "\n"
        print "running update_lin_txt from: custom_widgets.py"


    def update_param(self, lst_in):
        self.reset_par()
        print "self.command_lst =", self.command_lst
        print "lst_in =", lst_in
        if(len(lst_in) > 1):
            new_lst_pair = buils_lst_pair(lst_in)
            print "new_lst_pair =", new_lst_pair
            self.lst_pair = new_lst_pair
            print "self.lst_pair =", self.lst_pair
            self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)

            for pair in self.lst_pair:
                self.update_advanced_widget(pair[0], pair[1])
        else:
            self.lst_pair = []
            self.command_lst = [self.command_lst[0]]

class TmpImportWidget(QLabel):
    def __init__(self):
        super(TmpImportWidget, self).__init__()
        self.setText("TMP \n Import Widget")
        self.command_lst = ["import", "../*.cbf"]
        self.show()

    def update_param(self, dummy_cmd_lst = None):
        print "\n Nothing to update here \n"



class ParamWidget(QWidget):
    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        self.my_label = label_str

        inner_widgs = {
                       "find_spots": [phil_scope_find_spots , FindspotsSimplerParameterTab ],
                       "index"     : [phil_scope_index      , IndexSimplerParamTab         ],
                       "refine"    : [phil_scope_refine     , RefineSimplerParamTab        ],
                       "integrate" : [phil_scope_integrate  , IntegrateSimplerParamTab     ],
                        }

        if(label_str == "import"):
            old_test_way = '''
            self.my_widget = QLabel("TMP \n Import Widget")
            self.my_widget.command_lst = ["import", "../*.cbf"]
            '''
            self.my_widget = TmpImportWidget()

        else:
            #self.command = [label_str]

            self.my_widget = ParamMainWidget(phl_obj = inner_widgs[label_str][0],
                                             simp_widg = inner_widgs[label_str][1],
                                             parent = self, upper_label = label_str)

            self.my_widget.command_lst = [label_str]

        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(self.my_widget)

        self.setLayout(v_left_box)
        self.show()

    def update_param(self, curr_step):
        print "curr_step.command_lst = ", curr_step.command_lst
        self.my_widget.update_param(curr_step.command_lst)


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = ParamWidget("find_spots")
    sys.exit(app.exec_())


