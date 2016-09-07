'''
DUI's command line control stacked widgets

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




# FIXME Copied from dials.index.py. This is needed here because scipy needs to
# be imported before cctbx otherwise there will be a segmentation fault. This
# should be fixed in dials.index so that we don't need to import here.
try:
  # try importing scipy.linalg before any cctbx modules, otherwise we
  # sometimes get a segmentation fault/core dump if it is imported after
  # scipy.linalg is a dependency of sklearn.cluster.DBSCAN
  import scipy.linalg # import dependency
except ImportError, e:
  pass

'''
from resources.python_qt_bind import GuiBinding
gui_lib = GuiBinding()
print "using ", gui_lib.pyhon_binding
qt_tool = gui_lib.pyhon_binding
'''
qt_tool = "PyQt4"

if( qt_tool == "PyQt4" ):
    from PyQt4 import QtCore, QtGui, QtWebKit

else:
    from PySide import QtCore, QtGui, QtWebKit

import os
'''
from simpler_param_stacked_widgets import FindspotsSimplerParameterTab, \
                                          IndexSimplerParamTab,         \
                                          RefineSimplerParamTab,        \
                                          IntegrateSimplerParamTab,     \
                                          ExportSimplerParameterWidget


from cli_interactions import ImgTab, TextBrows, HtmlTab
from subprocess import call as shell_func

class ImportPage(QtGui.QWidget):


    # FIXME when the user enters a path without images dials fails to import
    # but does not raises an error consequently there is no red output in the GUI

    # FIXME consider something like:
    # dials.import template=/my/path/to/my/data/th_8_2_####.cbf
    # instead of:
    # dials.import /my/path/to/my/data/
    # as the generated line to run

    # And study the file:
    # Dxtbx/sweep_filenames.py

    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        self.super_parent.w_dir = os.getcwd()
        self.cmd_lin_default = "dials.import ~/put/your/path/here"
        self.button_label = "   Import      "

        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/import.png"

        import_path_group = QtGui.QGroupBox("Experiment IMG Directory")
        import_path_layout = QtGui.QHBoxLayout()

        self.lin_import_path =  QtGui.QLineEdit(self)
        import_path_layout.addWidget(self.lin_import_path)
        import_path_button = QtGui.QPushButton(" \n    Find experiment Dir            . \n")
        import_path_button.clicked.connect(self.find_my_img_dir)
        import_path_layout.addWidget(import_path_button)
        import_path_group.setLayout(import_path_layout)

        w_dir_group = QtGui.QGroupBox("Working Directory")
        w_dir_layout = QtGui.QHBoxLayout()
        self.w_dir_lin =  QtGui.QLineEdit(self)
        self.w_dir_lin.setText(self.super_parent.w_dir)
        w_dir_layout.addWidget(self.w_dir_lin)
        w_dir_button = QtGui.QPushButton(" \n    Change Working Dir    . \n")
        w_dir_button.clicked.connect(self.change_w_dir)
        w_dir_layout.addWidget(w_dir_button)
        w_dir_group.setLayout(w_dir_layout)


        self.auto_next_check = QtGui.QCheckBox("Enable auto-Next Feature")
        self.auto_next_check.stateChanged.connect(self.changed_auto_next)
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(import_path_group)
        mainLayout.addWidget(w_dir_group)


        imageLabel = QtGui.QLabel()
        #dials_logo_path = my_dui_path + "/../dui/resources/DIALS_Logo_scaled.png"
        dials_logo_path = my_dui_path + "/../dui/resources/DIALS_Logo_smaller_centred.png"

        #dials_logo_path = my_dui_path + "/../dui/resources/DIALS_Logo.png"
        image = QtGui.QImage(dials_logo_path)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        mainLayout.addWidget(imageLabel)
        #imageLabel.setScaledContents(True)


        #mainLayout.addStretch(1)
        mainLayout.addWidget(self.auto_next_check)



        big_layout = QtGui.QHBoxLayout()
        big_layout.addLayout(mainLayout)

        self.multi_line_txt = TextBrows()
        big_layout.addWidget(self.multi_line_txt)



        self.setLayout(big_layout)


    def changed_auto_next(self):
        print "changed_auto_next"
        self.update_auto_next_flag()

    def update_auto_next_flag(self):
        print "self.auto_next_check.checkState() =", self.auto_next_check.checkState()
        state = self.auto_next_check.checkState()
        if( state == 0 ):
            self.auto_next_flag = "unchecked"
        else:
            self.auto_next_flag = "checked"

    def find_my_img_dir(self, event = None):
        selected_file_path = str(QtGui.QFileDialog.getOpenFileName(self, "Open IMG Dir"))
        print "[file path found] =", selected_file_path

        if( selected_file_path ):
            for pos, single_char in enumerate(selected_file_path):
                if( single_char == "/" or single_char == "\\" ):
                    pos_sep = pos

            dir_name = selected_file_path[:pos_sep]
            if( dir_name[0:3] == "(u\'" ):
                print "dir_name[0:3] == \"(u\'\""
                dir_name = dir_name[3:]

            print "dir_name(final) =", dir_name
            self.lin_import_path.setText(dir_name)
            self.cmd_lin_default = "dials.import "+ dir_name
            print "CLI =", self.cmd_lin_default

        else:
            print "Failed to pick dir"
            self.cmd_lin_default = " "

        #self.super_parent.gui_line_edit.setText(self.cmd_lin_default)
        self.super_parent.gui_line_edit.set_text(self.cmd_lin_default)

    def change_w_dir(self, event = None):
        dir_name = str(QtGui.QFileDialog.getExistingDirectory(self, "Change Working Dir"))
        print "[dir path found] =", dir_name

        if( dir_name ):
            self.super_parent.w_dir = dir_name
            os.chdir(self.super_parent.w_dir)
            self.w_dir_lin.setText(self.super_parent.w_dir)
            print "dir_name(w_dir) =", self.super_parent.w_dir

        else:
            print "Failed to pick dir"


class GenericParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(GenericParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

    def add_tabs(self, simpler_par_widget = None, advanced_par_widget = None):

        ltabWidget = QtGui.QTabWidget()

        if( simpler_par_widget != None ):
            self.simple_par_tab = simpler_par_widget
            ltabWidget.addTab(self.simple_par_tab, "Simple")

        if( advanced_par_widget != None ):
            self.advance_par_tab = advanced_par_widget
            ltabWidget.addTab(self.advance_par_tab, "Advanced")

        rtabWidget = QtGui.QTabWidget()
        self.multi_line_txt = TextBrows()
        self.report_out_widg = HtmlTab(self.super_parent)
        self.analyse_out_img = ImgTab(self.super_parent)

        rtabWidget.addTab(self.multi_line_txt, "Log")
        rtabWidget.addTab(self.report_out_widg, "HTML output")
        rtabWidget.addTab(self.analyse_out_img, "Graphic Reports")

        splitter_layout = QtGui.QSplitter()
        splitter_layout.addWidget(ltabWidget)
        splitter_layout.addWidget(rtabWidget)
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(splitter_layout)
        self.setLayout(mainLayout)
        self.cmd_lin_extra = None

    def update_parms(self, from_simple):
        if( from_simple == True ):
            self.simple_par_tab.update_a_param()
        else:
            self.advance_par_tab.update_a_param()


    def run_extra_code(self):

        if( self.second_go_flag == True and self.cmd_lin_extra != None ):
            my_cmd = self.cmd_lin_extra
            print "\n running ", my_cmd, "\n"
            self.super_parent.update_lin_txt(new_line = my_cmd )
            self.super_parent.onGoBtn(event = True)
            self.second_go_flag = False
            return False

        else:
            return True


class FindspotsParameterWidget(GenericParameterWidget):
    def __init__(self, parent = None):
        from resources.find_spots_mult_opt import ParamMainWidget
        super(FindspotsParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

        self.advance_par_tab = ParamMainWidget(self.super_parent)
        self.simple_par_tab = FindspotsSimplerParameterTab(self.super_parent)
        self.add_tabs(simpler_par_widget = self.simple_par_tab,
                      advanced_par_widget = self.advance_par_tab)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots   "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/find_spots.png"
        self.cmd_lin_extra = "dials.report output.external_dependencies=local strong.pickle"
        #self.cmd_lin_extra = "dials.analyse_output output.directory=spot_find_output strong.pickle"


class IndexParameterWidget(GenericParameterWidget):

    def __init__(self, parent=None):
        from resources.index_mult_opt import ParamMainWidget
        super(IndexParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

        self.advance_par_tab = ParamMainWidget(self.super_parent)
        self.simple_par_tab = IndexSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = self.simple_par_tab,
                      advanced_par_widget = self.advance_par_tab)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "    Index       "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/index.png"

        self.cmd_lin_extra = "dials.report output.external_dependencies=local indexed.pickle"

        #self.cmd_lin_extra = "dials.analyse_output output.directory=index_output indexed.pickle"


def get_lst_output_ln(txt_brows):
    lst_ln_raw = txt_brows.get_full_output_lst()

    lst_ln = []

    for raw_block in lst_ln_raw:
        zero_pos = 0
        for xpos, single_char in enumerate(raw_block):
            if( single_char == "\n" ):
                print "xpos =", xpos
                str_to_add = raw_block[zero_pos:xpos]
                zero_pos = xpos
                lst_ln.append(str_to_add)



    return lst_ln


class TextLine(QtGui.QLineEdit):
    def __init__(self, my_content = None):
        super(TextLine, self).__init__()
        self.setReadOnly(True)
        self.setText(my_content)
        self.setFont(QtGui.QFont("Monospace"))

'''
class GenericData(object):
    pass


class BuildTable(object):
    def __init__(self, my_data_lst):

        div_n_1 = False
        div_n_2 = False
        div_n_3 = False

        opt_lst = []

        for ln in my_data_lst:
            if( ln[1:6] == "-----" ):
                if( div_n_1 == False ):
                    div_n_1 = True

                elif( div_n_2 == False ):
                    div_n_2 = True

                elif( div_n_3 == False ):
                    div_n_3 = True
                    print "end of MyTable"

                else:
                    print "ERROR to many dividers"

            if( div_n_1 == True and div_n_2 == False and ln[1:6] != "-----" ):
                #print "Label =", ln
                label = ln

            elif( div_n_2 == True and div_n_3 == False and ln[1:6] != "-----" ):
                print "Line to eDD =<<<", ln, ">>>"
                opt_lst.append(ln)

        self.data = GenericData()
        self.data.label = label
        self.data.multline_opt = opt_lst

    def get_table(self):
        return self.data


class TableSelectWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TableSelectWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        print "Hi tst"

    def dataIn(self, my_data_lst):
        data_table = BuildTable(my_data_lst)
        data_table = data_table.get_table()

        table_line_layout = QtGui.QVBoxLayout()

        label_str = data_table.label
        top_label = QtGui.QLabel(label_str)
        top_label.setFont(QtGui.QFont("Monospace"))

        table_line_layout.addWidget(top_label)

        self.line_txt_lst = []
        for i, line_wgt in enumerate(data_table.multline_opt):
            single_line_layout = QtGui.QHBoxLayout()
            line_txt = TextLine(line_wgt)
            self.line_txt_lst.append(line_txt)
            single_line_layout.addWidget(line_txt)
            select_button = QtGui.QPushButton("Select")
            single_line_layout.addWidget(select_button)
            table_line_layout.addLayout(single_line_layout)
            select_button.opt_num = i
            select_button.clicked.connect(self.click_select)

        self.setLayout(table_line_layout)
        self.show()

    def click_select(self):
        my_sender = self.sender()
        self.user_opt = my_sender.opt_num
        print "opt_num =", self.user_opt

        for line_txt in self.line_txt_lst:
            line_txt.deselect()

        self.line_txt_lst[self.user_opt].setSelection(1,180)

        full_lin = str(self.line_txt_lst[self.user_opt].text())
        for i_spc in xrange(len(full_lin)-2, 1, -1):

            if( full_lin[i_spc:i_spc + 1] == " " ):
                bas_op_str = full_lin[i_spc + 1:len(full_lin)]
                break


        str_to_run = "dials.reindex indexed.pickle change_of_basis_op=" + bas_op_str
        self.super_parent.gui_line_edit.set_text(str(str_to_run))


'''

class ReIndexWidget(QtGui.QWidget):

    #TODO review if my_dui_path var can be used more globally

    def __init__(self, parent=None):
        super(ReIndexWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        self.cmd_lin_default = "dials.refine_bravais_settings experiments.json indexed.pickle"
        self.button_label = "    ReIndex  "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/reindex.png"


        rtabWidget = QtGui.QTabWidget()
        self.multi_line_txt = TextBrows()

        self.reindex_tab = TableSelectWidget(self.super_parent)

        rtabWidget.addTab(self.reindex_tab, "Reindex ")
        rtabWidget.addTab(self.multi_line_txt, "Log")

        big_layout = QtGui.QHBoxLayout()

        big_layout.addWidget(rtabWidget)
        self.setLayout(big_layout)

    def run_extra_code(self):

        dat = get_lst_output_ln(self.multi_line_txt)
        self.reindex_tab.dataIn(dat)

class RefineParameterWidget(GenericParameterWidget):

    def __init__(self, parent=None):
        from resources.refine_mult_opt import ParamMainWidget
        super(RefineParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

        self.advance_par_tab = ParamMainWidget(self.super_parent)
        self.simple_par_tab = RefineSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = self.simple_par_tab,
                      advanced_par_widget = self.advance_par_tab)

        self.cmd_lin_default = "dials.refine experiments.json reindexed_reflections.pickle"
        self.button_label = "    Refine      "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/refine.png"

        self.cmd_lin_extra = "dials.report output.external_dependencies=local refined.pickle"

        #self.cmd_lin_extra = "dials.analyse_output output.directory=refine_output refined.pickle"


class IntegrateParameterWidget(GenericParameterWidget):

    def __init__(self, parent=None):
        from resources.integrate_mult_opt import ParamMainWidget
        super(IntegrateParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

        self.advance_par_tab = ParamMainWidget(self.super_parent)
        self.simple_par_tab = IntegrateSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = self.simple_par_tab,
                      advanced_par_widget = self.advance_par_tab)


        self.cmd_lin_default = "dials.integrate refined_experiments.json refined.pickle"
        self.button_label = " Integrate    "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/integrate.png"

        self.cmd_lin_extra = "dials.report output.external_dependencies=local integrated.pickle"

        #self.cmd_lin_extra = "dials.analyse_output output.directory=integrate_output integrated.pickle"

class ExportParameterWidget(GenericParameterWidget):


    def __init__(self, parent=None):
        from resources.export_mult_opt import ParamMainWidget
        super(ExportParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

        self.advance_par_tab = ParamMainWidget(self.super_parent)
        self.simple_par_tab = ExportSimplerParameterWidget(self.super_parent)
        self.add_tabs(simpler_par_widget = self.simple_par_tab,
                      advanced_par_widget = self.advance_par_tab)

        self.cmd_lin_default = "dials.export integrated.pickle refined_experiments.json"
        self.button_label = "Export mtz   "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/export.png"

        self.cmd_lin_extra = ["pointless < pointless.dat | tee pointless.log",
                              "aimless < aimless.dat | tee aimless.log"]

    def run_extra_code(self):

        if( self.second_go_flag == True and self.cmd_lin_extra != None ):

            print "self.simple_par_tab.run_pointless_check.checkState() =", \
                   self.simple_par_tab.run_pointless_check.checkState()

            print "self.simple_par_tab.run_aimless_check.checkState() =", \
                   self.simple_par_tab.run_aimless_check.checkState()

            if( self.simple_par_tab.run_pointless_check.checkState() == 2 ):
                try:
                    p_file = open("pointless.dat", "w")
                    p_file.write("HKLIN hklout.mtz\n")
                    p_file.write("HKLOUT unscaled.mtz\n")
                    p_file.close()

                    my_cmd = "pointless < pointless.dat | tee pointless.log"
                    shell_func(my_cmd, shell=True)

                except:
                    print "WARNING something went wrong attempting to run pointless"

            if( self.simple_par_tab.run_aimless_check.checkState() == 2 ):
                try:
                    a_file = open("aimless.dat", "w")
                    a_file.write("HKLIN unscaled.mtz\n")
                    a_file.write("HKLOUT scaled.mtz\n")
                    a_file.close()

                    my_cmd = "aimless < aimless.dat | tee aimless.log"
                    shell_func(my_cmd, shell=True)

                except:
                    print "WARNING something went wrong attempting to run aimless"


        self.second_go_flag = False




        #flag to tell the caller (main_dui) if HTML view should be updated
        return False


'''
