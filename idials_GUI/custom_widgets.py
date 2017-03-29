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

from params_live_gui_generator import PhilWidget
from simpler_param_widgets import IndexSimplerParamTab, FindspotsSimplerParameterTab, \
                                   RefineSimplerParamTab, IntegrateSimplerParamTab

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
        get_wor_dir = os.getcwd()
        self.setDirectory(str(get_wor_dir))
        self.setFileMode(QFileDialog.Directory)


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

        self.super_parent.check_next()


class ParamAdvancedWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(ParamAdvancedWidget, self).__init__()
        self.super_parent = parent.super_parent
        self.param_widget_parent = parent.param_widget_parent
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
    def __init__(self, phl_obj = None, simp_widg = None, parent = None, upper_label = None):
        super(ParamMainWidget, self).__init__()

        #TODO remove this << if >> and run directly the
        # second shoice

        testing_off = '''
        if parent == None:
            self.super_parent = self
            my_phl_obj = phil_scope_index
            simp_widg = IndexSimplerParamTab

        else:

        '''
        try:
            self.super_parent = parent.super_parent
            my_phl_obj = phl_obj
        except:
            print "\n\n\n something went wrong here \n\n\n"



        self.param_widget_parent = self

        hbox = QVBoxLayout()

        level_tab = QTabWidget()

        self.sipler_widget = simp_widg(parent = self)
        self.advanced_widget = ParamAdvancedWidget(phl_obj = my_phl_obj, parent = self)

        level_tab.addTab(self.sipler_widget, "Simple")
        level_tab.addTab(self.advanced_widget, "Advanced")

        label_font = QFont()
        sys_font_point_size =  label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel(str(upper_label))
        step_label.setFont(label_font)

        hbox.addWidget(step_label)
        hbox.addWidget(level_tab)


        self.setLayout(hbox)
        self.show()

    def update_advanced_widget(self, str_path, str_value):

        for bg_widg in(self.advanced_widget.scrollable_widget.lst_wgs ,
                       self.sipler_widget.lst_wgs):
            for widg in bg_widg:
                if( widg.local_path == str_path ):
                    if( widg.tmp_lst == None ):
                        print "Number widget"
                        num_val = float(str_value)
                        widg.setValue(num_val)

                    else:
                        for pos, val in enumerate(widg.tmp_lst):
                            if( val == str_value ):
                                print "found val, v=", val
                                widg.setCurrentIndex(pos)

    def update_lin_txt(self, str_path, str_value):

        cmd_to_run = str_path + "=" + str_value
        print "adjusting parameter: {", cmd_to_run,"}"


        #TODO in a future will no longer be needed to check
        # because this should be running only from inside
        # the big GUI
        if( self.super_parent == self ):
            print"\n self.super_parent == self \n"

        else:
            print"\n self.super_parent != self \n"
            try:
                self.super_parent.param_changed(cmd_to_run)

            except:
                print "Not ready to change parameter yet"

        self.update_advanced_widget(str_path, str_value)


class StepList(object):

    lst_lablel = [
                  " import",
                  "find spots",
                  "index",
                  #"refine bravais settings",
                  "refine",
                  "integrate"
                  ]

    my_command_lst = [
                    "import",
                    "find_spots",
                    "index",
                    #"refine_bravais_settings",
                    "refine",
                    "integrate"
                   ]

    def __init__(self, parent = None):
        self.super_parent = parent
        self.list_of_widgets  = [
              ImportPage(parent = self),
              ParamMainWidget(phl_obj = phil_scope_find_spots, simp_widg = FindspotsSimplerParameterTab,
                              parent = self, upper_label = "Find Spots"),
              ParamMainWidget(phl_obj = phil_scope_index, simp_widg = IndexSimplerParamTab,
                              parent = self, upper_label = "Index"),
              ParamMainWidget(phl_obj = phil_scope_refine, simp_widg = RefineSimplerParamTab,
                              parent = self, upper_label = "Refine"),
              ParamMainWidget(phl_obj = phil_scope_integrate, simp_widg = IntegrateSimplerParamTab,
                              parent = self, upper_label = "Integrate")
                                 ]

        idials_gui_path = os.environ["IDIALS_GUI_PATH"]
        print "idials_gui_path =", idials_gui_path

        lst_icons_path = []

        lst_icons_path.append(str(idials_gui_path + "/resources/import.png"))
        lst_icons_path.append(str(idials_gui_path + "/resources/find_spots.png"))
        lst_icons_path.append(str(idials_gui_path + "/resources/index.png"))
        lst_icons_path.append(str(idials_gui_path + "/resources/refine.png"))
        lst_icons_path.append(str(idials_gui_path + "/resources/integrate.png"))

        self.lst_icons = []
        for my_icon_path in lst_icons_path:
            self.lst_icons.append(QIcon(my_icon_path))
            print "attempting to append:", my_icon_path

    def __call__(self):
        return self.lst_lablel, self.list_of_widgets, self.lst_icons, self.my_command_lst



class TmpTestWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(TmpTestWidget, self).__init__()
        self.super_parent = self
        self.embedded_reindex = self
        my_widget = ParamMainWidget(phl_obj = phil_scope_find_spots, simp_widg = FindspotsSimplerParameterTab,
                             parent = self, upper_label = "Find Spots")
        vbox = QVBoxLayout()
        vbox.addWidget(my_widget)
        self.setLayout(vbox)
        self.show()

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = TmpTestWidget()
    sys.exit(app.exec_())


