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
                                  IntegrateSimplerParamTab

from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index

from dials.command_line.refine_bravais_settings import phil_scope as phil_scope_r_b_settings

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

class ImportPage(QWidget):

    update_command_lst = pyqtSignal(list)

    '''
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    '''

    def __init__(self, parent = None):
        super(ImportPage, self).__init__(parent = None)

        template_grp =  QGroupBox(" Import from File(s) ")
        template_vbox =  QVBoxLayout()
        self.templ_lin =   QLineEdit(self)
        self.templ_lin.setText(" ? ")
        opn_fil_btn = QPushButton("\n Select File(s)\n")

        template_vbox.addWidget(self.templ_lin)
        template_vbox.addWidget(opn_fil_btn)

        template_grp.setLayout(template_vbox)

        to_maybe_remove = '''
        dir_grp =  QGroupBox(" Import from Dir ")
        dir_vbox =  QVBoxLayout()
        self.dir_lin =   QLineEdit(self)
        self.dir_lin.setText(" ? ")
        opn_dir_btn = QPushButton("\n open Dir\n")
        dir_vbox.addWidget(self.dir_lin)
        dir_vbox.addWidget(opn_dir_btn)
        dir_grp.setLayout(dir_vbox)
        '''

        big_layout =  QVBoxLayout()
        big_layout.addWidget(template_grp)

        to_maybe_remove = '''
        big_layout.addWidget(QLabel("\n\n                                 Or \n\n"))
        big_layout.addWidget(dir_grp)
        '''

        opn_fil_btn.clicked.connect(self.open_files)
        self.templ_lin.textChanged.connect(self.intro_file_changed)

        to_maybe_remove = '''
        opn_dir_btn.clicked.connect(self.open_dir)
        self.dir_lin.textChanged.connect(self.intro_dir_changed)
        '''

        self.setLayout(big_layout)
        self.show()

    def get_arg_obj(self, sys_arg_in):
        print "\n sys_arg_in =", sys_arg_in, "\n"
        if(sys_arg_in.template != None):
            self.templ_lin.setText(str(sys_arg_in.template))

        to_maybe_remove = '''
        elif(sys_arg_in.directory != None):
            self.dir_lin.setText(str(sys_arg_in.directory))
        '''


    def intro_file_changed(self, value):
        print "txt(value) =", value
        str_path = "template="
        str_value = str(value)

        my_cmd = str_path + str_value
        self.command_lst = ["import", my_cmd]
        self.update_command_lst.emit(self.command_lst)

        to_maybe_remove = '''
    def intro_dir_changed(self, value):
        print "txt(value) =", value
        str_path = "directory="
        str_value = str(value)

        my_cmd = str_path + str_value
        self.command_lst = ["import", my_cmd]

    def open_dir(self):
        print "open_dir"
        file_dialog = QFileDialog()
        get_wor_dir = str(os.getcwd())

        end_dir =  QFileDialog.getExistingDirectory(self, "Open Dir",
                                                      get_wor_dir)

        print "end_dir =", end_dir
        self.dir_lin.setText(end_dir)
        '''

    def open_files(self):
        print "from open_files  << import page >>"
        get_wor_dir = str(os.getcwd())

        lst_file_path =  QFileDialog.getOpenFileNames(self, "Open File(s)",
                                                      get_wor_dir,
                                                      "All Files (*.*)")

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

    def gray_me_out(self):
        pass

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
        #print "par_str =", par_str
        pair = string2pair(par_str)
        #print "pair =", pair
        lst_pair.append(pair)

    return lst_pair

class ParamMainWidget( QWidget):

    update_command_lst = pyqtSignal(list)

    def __init__(self, phl_obj = None, simp_widg = None, parent = None, upper_label = None):
        super(ParamMainWidget, self).__init__()

        self.command_lst = [None]
        self.lst_pair = []

        try:
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

        #self.sipler_widget = self.simp_widg_in(parent = self) #TODO make sure you need to do: parent = self
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

        try:
            self.sipler_widget.set_max_nproc()
            print "\n Tunning nproc to maximum \n"

        except:
            print "\n This step runs as fas as it can with nproc = 1 \n"


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
                                print "\n\n Type Mismatch while searching for twin parameter \n\n"

                        else:
                            for pos, val in enumerate(widg.tmp_lst):
                                if(val == str_value):
                                    print "found val, v=", val
                                    widg.setCurrentIndex(pos)

                except:
                    pass

    def update_lin_txt(self, str_path, str_value):
        cmd_to_run = str_path + "=" + str_value
        self.update_advanced_widget(str_path, str_value)
        self.lst_pair = update_lst_pair(self.lst_pair, str_path, str_value)
        self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)
        self.update_command_lst.emit(self.command_lst)

    def update_param(self, lst_in):
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
        palt_gray = QPalette()
        palt_gray.setColor(QPalette.WindowText, QColor(88, 88, 88, 88))

        for bg_widg in(self.advanced_widget.scrollable_widget.lst_var_widg ,
                       self.advanced_widget.scrollable_widget.lst_label_widg,
                       self.sipler_widget.lst_var_widg):

            for widg in bg_widg:

                print "type(widg) =", type(widg)

                widg.setStyleSheet("color: rgba(88, 88, 88, 88)")
                #widg.setPalette(palt_gray)

                try:
                    widg.setReadOnly(True)

                except:
                    pass


    def activate_me(self):
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
                    widg.setReadOnly(False)

                except:
                    pass


class ParamWidget(QWidget):

    update_command_lst = pyqtSignal(list)

    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        self.my_label = label_str

        inner_widgs = {
                       "find_spots":              [phil_scope_find_spots   , FindspotsSimplerParameterTab ],
                       "index"     :              [phil_scope_index        , IndexSimplerParamTab         ],
                       "refine_bravais_settings": [phil_scope_r_b_settings , RefineBravaiSimplerParamTab  ],
                       "refine"    :              [phil_scope_refine       , RefineSimplerParamTab        ],
                       "integrate" :              [phil_scope_integrate    , IntegrateSimplerParamTab     ],
                        }

        if(label_str == "import"):
            #self.my_widget = TmpImportWidget()
            self.my_widget = ImportPage()


        else:
            self.my_widget = ParamMainWidget(phl_obj = inner_widgs[label_str][0],
                                             simp_widg = inner_widgs[label_str][1],
                                             parent = self, upper_label = label_str)

        self.my_widget.command_lst = [label_str]

        self.my_widget.update_command_lst.connect(self.update_parent_lst)

        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(self.my_widget)
        self.setLayout(v_left_box)
        self.show()

    def update_param(self, curr_step):
        self.my_widget.update_param(curr_step.command_lst)

    def update_parent_lst(self, command_lst):
        self.update_command_lst.emit(command_lst)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    #ex = ParamWidget("find_spots")
    ex = ParamWidget("import")
    sys.exit(app.exec_())


