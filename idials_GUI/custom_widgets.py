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


from python_qt_bind import *

import os, sys
from dynamic_reindex_gui import MyReindexOpts

from params_live_gui_generator import PhilWidget

from simpler_param_widgets import IndexSimplerParamTab

from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index

#from dials.command_line.refine_bravais_settings import phil_scope as phil_scope_refine_br_st

from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate

try:
    from dials.command_line.export import phil_scope as phil_scope_export
except:
    from dials.command_line.export_mtz import phil_scope as phil_scope_export

def template_right_side_build(in_str_tmp, dir_path):

    #print "in_str_tmp =", in_str_tmp
    #print "dir_path =", dir_path

    out_str = in_str_tmp + dir_path
    lst_files = os.listdir(str(dir_path))

    #for i, e in reversed(list(enumerate(a))):
    #for pos, single_char in enumerate(in_str_tmp):
    for pos, single_char in reversed(list(enumerate(in_str_tmp))):
        if( single_char == "." ):
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
        if( prev_str == out_str ):
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
            if( single_string[pos] != single_char ):
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

        print "before setFileMode"
        self.setFileMode(QFileDialog.Directory)
        print "after setFileMode"




class ImportPage(QWidget):

    '''
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    '''

    # FIXME when the user enters a path without images dials fails to import
    # but does not raises an error consequently there is no red output in the GUI

    # FIXME study the file:
    # Dxtbx/sweep_filenames.py

    def __init__(self, parent = None):
        super(ImportPage, self).__init__(parent = None)
        self.super_parent = parent.super_parent # reference across the hole GUI to MyMainDialog

        import_path_group =  QGroupBox("Experiment IMG Directory")
        import_path_layout =  QVBoxLayout()

        import_path_button =  QPushButton(" \n    Find Images      . \n")
        import_path_button.clicked.connect(self.find_my_img_dir)
        import_path_group.setLayout(import_path_layout)

        import_path_layout.addWidget(import_path_button)

        template_grp =  QGroupBox("Template ")
        template_vbox =  QHBoxLayout()
        self.templ_lin =   QLineEdit(self)
        self.templ_lin.setText("Generated Template =")
        template_vbox.addWidget(self.templ_lin)
        template_grp.setLayout(template_vbox)

        mainLayout =  QVBoxLayout()
        mainLayout.addWidget(import_path_group)
        mainLayout.addWidget(template_grp)

        big_layout =  QHBoxLayout()
        big_layout.addLayout(mainLayout)

        self.setLayout(big_layout)
        self.show()

        self.success_stat = False


    def __call__(self):
        print "from __call__   << import page >>"

        if( self.success_stat == False ):
            self.find_my_img_dir()
            print "( self.success_stat == False )  == False"

    def find_my_img_dir(self, event = None):

        selector = FileOrDir(self)
        #selected_file_path = str(selector.getOpenFileName(self, "Open IMG Dir"))
        lst_file_path = selector.getOpenFileNames(self, "Open IMG Dir")
        #getOpenFileNamesAndFilter

        print "[ file path selected ] =", lst_file_path
        print "len(lst_file_path) =", len(lst_file_path)

        for single_string in lst_file_path:
            print "single_string =", single_string

        if( lst_file_path and len(lst_file_path) == 1 ):
            selected_file_path = str(lst_file_path[0])

            print "\n selected_file_path =", selected_file_path, "\n"
            print "type(selected_file_path) =", type(selected_file_path)

            for pos, single_char in enumerate(selected_file_path):
                if( single_char == "/" or single_char == "\\" ):
                    pos_sep = pos

            dir_name = selected_file_path[:pos_sep]
            if( dir_name[0:3] == "(u\'" ):
                print "dir_name[0:3] == \"(u\'\""
                dir_name = dir_name[3:]

            print "dir_name(final) =", dir_name

            templ_str_tmp = selected_file_path[pos_sep:]
            #print "templ_str_tmp =", templ_str_tmp

            templ_r_side = template_right_side_build(templ_str_tmp, dir_name)

            templ_str_final = dir_name + templ_r_side
            self.templ_lin.setText(templ_str_final)

        elif( len(lst_file_path) > 1 ):
            print "time to handle multiple files selected"
            templ_str_final = template_from_lst_build(lst_file_path)
            print "templ_str_final =", templ_str_final
            self.templ_lin.setText(templ_str_final)

        else:
            print "Failed to pick dir"


class ParamSiplerWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamSiplerWidget, self).__init__()

        vbox =  QVBoxLayout()
        dummy_label = QLabel("dummy test")
        vbox.addWidget(dummy_label)
        self.setLayout(vbox)
        self.show()


class ParamAdvancedWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamAdvancedWidget, self).__init__()

        self.param_widget_paret = parent.param_widget_paret
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





class ParamMainWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamMainWidget, self).__init__()
        if parent == None:
            self.super_parent = self
            my_phl_obj = phil_scope_find_spots

        else:
            self.super_parent = parent.super_parent
            my_phl_obj = phl_obj

        self.param_widget_paret = self

        hbox = QHBoxLayout()

        level_tab = QTabWidget()

        self.sipler_widget = IndexSimplerParamTab(parent = self)
        self.advanced_widget = ParamAdvancedWidget(phl_obj = my_phl_obj, parent = self)

        level_tab.addTab(self.sipler_widget, "Simple Editor")
        level_tab.addTab(self.advanced_widget, "Advanced Editor")

        hbox.addWidget(level_tab)

        self.setLayout(hbox)
        self.show()

    def update_lin_txt(self, str_path, str_value):
        cmd_to_run = str_path + "=" + str_value
        print "running command = {", cmd_to_run,"}"
        self.super_parent.param_changed(cmd_to_run)
        print "\n\n YES \n\n"

class StepList(object):

    lst_lablel = [
                  " import",
                  "find spots",
                  "index",
                  "refine bravais settings",
                  "refine",
                  "integrate"
                  ]

    lst_commands = [
                    "import",
                    "find_spots",
                    "index",
                    "refine_bravais_settings",
                    "refine",
                    "integrate"
                   ]

    def __init__(self, parent = None):
        self.super_parent = parent
        self.lst_widg  = [
                          ImportPage(parent = self),
                          ParamMainWidget(phl_obj = phil_scope_find_spots, parent = self),
                          ParamMainWidget(phl_obj = phil_scope_index, parent = self),
                          MyReindexOpts(parent = self),
                          ParamMainWidget(phl_obj = phil_scope_refine, parent = self),
                          ParamMainWidget(phl_obj = phil_scope_integrate, parent = self)
                         ]

        idials_path = os.environ["IDIALS_PATH"]
        print "idials_path =", idials_path

        lst_icons_path = []

        lst_icons_path.append(str(idials_path + "/resources/import.png"))
        lst_icons_path.append(str(idials_path + "/resources/find_spots.png"))
        lst_icons_path.append(str(idials_path + "/resources/index.png"))
        lst_icons_path.append(str(idials_path + "/resources/reindex.png"))
        lst_icons_path.append(str(idials_path + "/resources/refine.png"))
        lst_icons_path.append(str(idials_path + "/resources/integrate.png"))

        self.lst_icons = []
        for my_icon_path in lst_icons_path:
            self.lst_icons.append(QIcon(my_icon_path))
            print "attempting to append:", my_icon_path

    def __call__(self):
        return self.lst_lablel, self.lst_widg, self.lst_icons, self.lst_commands


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = ParamMainWidget()
    #ex = importOuterWidget()
    sys.exit(app.exec_())


