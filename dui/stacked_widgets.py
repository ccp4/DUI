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


from resources.python_qt_bind import GuiBinding
gui_lib = GuiBinding()
print "using ", gui_lib.pyhon_binding
qt_tool = gui_lib.pyhon_binding

if( qt_tool == "PyQt4" ):
    from PyQt4 import QtCore, QtGui, QtWebKit

else:
    from PySide import QtCore, QtGui, QtWebKit

import os

from simpler_param_stacked_widgets import FindspotsSimplerParameterTab, \
                                          IndexSimplerParamTab,         \
                                          RefineSimplerParamTab,        \
                                          IntegrateSimplerParamTab,     \
                                          ExportSimplerParameterWidget

from cli_interactions import ImgTab, TextBrows, HtmlTab
from subprocess import call as shell_func

class ImportPage(QtGui.QWidget):

    '''
    This stacked widget basically helps the user to browse the input images
    path and the working directory, there is no auto-generated code in use
    withing this widget and there is no multiple tabs like the other stacked
    widgets.
    '''

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
    '''
    All dual tab parameter widgets should inherit from this one
    as they all look alike
    '''
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
    '''
    The duty of this widget is to contain 2 tabs with the 2
    levels of expertise and with different amounts of parameters
    to adjust in the indexing algorithm
    '''
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

'''
inserting example to be cut START _________________________________________________________
'''



def get_lst_output_ln():
    lst_ln = []
    lst_ln.append("DIALS 1.2.2-g62d8f5d-release                                                                                         ")
    lst_ln.append("The following parameters have been modified:                                                                         ")
    lst_ln.append("                                                                                                                     ")
    lst_ln.append("input {                                                                                                              ")
    lst_ln.append("  experiments = experiments.json                                                                                     ")
    lst_ln.append("  reflections = indexed.pickle                                                                                       ")
    lst_ln.append("}                                                                                                                    ")
    lst_ln.append("                                                                                                                     ")
    lst_ln.append("---------------------------------------------------------------------------------------------------------------------")
    lst_ln.append("Solution Metric fit  rmsd  min/max cc #spots lattice                                 unit_cell volume           cb_op")
    lst_ln.append("---------------------------------------------------------------------------------------------------------------------")
    lst_ln.append("      22     3.7617 1.730 0.612/0.862   9000      cP  44.48  44.48  44.48  90.00  90.00  90.00  87986           a,b,c")
    lst_ln.append("      21     3.7617 1.712 0.655/0.661   9000      hR  63.24  63.24  77.18  90.00  90.00 120.00 267338  -a+b,a+c,a+b-c")
    lst_ln.append("      20     3.7617 1.648 0.612/0.614   9000      hR  63.15  63.15  78.55  90.00  90.00 120.00 271257 -b+c,a+b,-a+b+c")
    lst_ln.append("      19     3.7616 1.672 0.643/0.650   9000      hR  62.30  62.30  77.17  90.00  90.00 120.00 259357   a-c,b+c,a-b+c")
    lst_ln.append("      18     3.7616 1.660 0.653/0.653   9000      hR  62.38  62.38  75.57  90.00  90.00 120.00 254645  b-c,-a+c,a+b+c")
    lst_ln.append("      17     3.7617 1.708 0.631/0.851   9000      tP  44.55  44.55  44.77  90.00  90.00  90.00  88854           c,a,b")
    lst_ln.append("      16     3.7617 1.708 0.616/0.851   9000      oC  63.04  62.81  44.67  90.00  90.00  90.00 176861      -a+c,a+c,b")
    lst_ln.append("      15     3.7616 1.625 0.651/0.651   9000      mC  62.08  61.86  44.22  90.00  90.98  90.00 169783       a+c,a-c,b")
    lst_ln.append("      14     3.7617 1.632 0.616/0.616   9000      mC  63.91  63.19  45.13  90.00  89.23  90.00 182231      -a+c,a+c,b")
    lst_ln.append("      13     3.6202 1.470 0.639/0.862   9000      tP  43.00  43.00  43.95  90.00  90.00  90.00  81264           a,b,c")
    lst_ln.append("      12     3.6202 1.449 0.651/0.862   9000      oC  61.60  60.68  44.01  90.00  90.00  90.00 164520       a-b,a+b,c")
    lst_ln.append("      11     3.6199 1.421 0.679/0.679   9000      mC  60.70  61.72  44.01  90.00  90.31  90.00 164865      a+b,-a+b,c")
    lst_ln.append("      10     3.6202 1.425 0.651/0.651   9000      mC  61.75  60.79  44.15  90.00  90.50  90.00 165714       a-b,a+b,c")
    lst_ln.append("       9     0.1576 0.171 0.832/0.848   9000      tP  42.41  42.41  39.76  90.00  90.00  90.00  71506           b,c,a")
    lst_ln.append("       8     0.1576 0.172 0.832/0.923   9000      oC  60.00  60.04  39.78  90.00  90.00  90.00 143304       b-c,b+c,a")
    lst_ln.append("       7     0.1576 0.163 0.860/0.860   9000      mC  60.05  60.05  39.82  90.00  90.13  90.00 143580       b-c,b+c,a")
    lst_ln.append("       6     0.1482 0.167 0.923/0.923   9000      mC  60.01  59.99  39.75  90.00  89.91  90.00 143090      b+c,-b+c,a")
    lst_ln.append("       5     0.0795 0.160 0.832/0.862   9000      oP  39.76  42.34  42.45  90.00  90.00  90.00  71480           a,b,c")
    lst_ln.append("       4     0.0790 0.161 0.862/0.862   9000      mP  39.76  42.46  42.34  90.00  89.99  90.00  71482        -a,-c,-b")
    lst_ln.append("       3     0.0795 0.158 0.832/0.832   9000      mP  42.37  39.79  42.48  90.00  89.96  90.00  71614        -b,-a,-c")
    lst_ln.append("       2     0.0249 0.155 0.851/0.851   9000      mP  39.77  42.37  42.47  90.00  89.90  90.00  71572           a,b,c")
    lst_ln.append("       1     0.0000 0.155         -/-   9000      aP  39.77  42.37  42.47  89.98  89.91  89.98  71553           a,b,c")
    lst_ln.append("---------------------------------------------------------------------------------------------------------------------")
    lst_ln.append("                                                                                                                     ")
    lst_ln.append("usr+sys time: 1.10 seconds                                                                                           ")
    lst_ln.append("wall clock time: 8.10 seconds                                                                                        ")
    return lst_ln




class TextLine(QtGui.QLineEdit):
    def __init__(self, my_content = None):
        super(TextLine, self).__init__()
        self.setReadOnly(True)
        self.setText(my_content)
        self.setFont(QtGui.QFont("Monospace"))
class GenericData(object):
    pass

class BuildTable(object):
    def __init__(self, my_data_lst):

        div_n_1 = False
        div_n_2 = False
        div_n_3 = False

        opt_lst = []

        for ln in my_data_lst:
            if( ln[0:5] == "-----" ):
                if( div_n_1 == False ):
                    div_n_1 = True

                elif( div_n_2 == False ):
                    div_n_2 = True

                elif( div_n_3 == False ):
                    div_n_3 = True
                    print "end of MyTable"

                else:
                    print "ERROR to many dividers"

            if( div_n_1 == True and div_n_2 == False and ln[0:5] != "-----" ):
                print "Label =", ln
                label = ln

            elif( div_n_2 == True and div_n_3 == False and ln[0:5] != "-----" ):
                #print "Line to eDD =", ln
                opt_lst.append(ln)

        self.data = GenericData()
        self.data.label = label
        self.data.multline_opt = opt_lst

    def get_table(self):
        return self.data


class TableSelectWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TableSelectWidget, self).__init__(parent)

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

        self.line_txt_lst[self.user_opt].setSelection(1,260)







'''
example to cut END _______________________________________________________________________
'''


class ReIndexWidget(QtGui.QWidget):

    #TODO review if my_dui_path var can be used more globally

    def __init__(self, parent=None):
        super(ReIndexWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        self.cmd_lin_default = "dials.refine_bravais_settings experiments.json indexed.pickle"
        self.button_label = "    ReIndex  "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/refine.png"



        rtabWidget = QtGui.QTabWidget()
        self.multi_line_txt = TextBrows()


        dat = get_lst_output_ln()
        reindex_tab = TableSelectWidget()
        reindex_tab.dataIn(dat)

        rtabWidget.addTab(self.multi_line_txt, "Log")
        rtabWidget.addTab(reindex_tab, "Reindex ")


        big_layout = QtGui.QHBoxLayout()
        '''
        self.multi_line_txt = TextBrows()
        big_layout.addWidget(self.multi_line_txt)
        '''
        big_layout.addWidget(rtabWidget)
        self.setLayout(big_layout)


class RefineParameterWidget(GenericParameterWidget):
    '''
    The duty of this widget is to contain 2 tabs with the 2
    levels of expertise and with different amounts of parameters
    to adjust in the refine algorithm
    '''
    def __init__(self, parent=None):
        from resources.refine_mult_opt import ParamMainWidget
        super(RefineParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.second_go_flag = True # flag to decide if should run go a second time

        self.advance_par_tab = ParamMainWidget(self.super_parent)
        self.simple_par_tab = RefineSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = self.simple_par_tab,
                      advanced_par_widget = self.advance_par_tab)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "    Refine      "
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/refine.png"

        self.cmd_lin_extra = "dials.report output.external_dependencies=local refined.pickle"

        #self.cmd_lin_extra = "dials.analyse_output output.directory=refine_output refined.pickle"


class IntegrateParameterWidget(GenericParameterWidget):
    '''
    The duty of this widget is to contain 2 tabs with the 2
    levels of expertise and with different amounts of parameters
    to adjust in the integration algorithm
    '''
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
    '''
    This widget like the import one has no multiple tabs, but it does have
    auto generated code on it
    '''

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



        to_try_to_fix_after_the_meeting = '''

        if( self.second_go_flag == True and self.cmd_lin_extra != None ):

            #preparing pointless.dat
            p_file = open("pointless.dat", "w")
            p_file.write("HKLIN hklout.mtz\n")
            p_file.write("HKLOUT unscaled.mtz\n")
            p_file.close()

            #running pointless from within the GUI
            pointless_cmd = "pointless HKLIN hklout.mtz HKLOUT unscaled.mtz"
            self.super_parent.update_lin_txt(new_line = pointless_cmd )
            self.super_parent.onGoBtn(event = True)
            self.second_go_flag = False



            self.super_parent.onGoBtn(event = False)
            self.second_go_flag = "next"

        elif( self.second_go_flag == "next" ):

            #preparing aimless.dat
            a_file = open("aimless.dat", "w")
            a_file.write("HKLIN unscaled.mtz\n")
            a_file.write("HKLOUT scaled.mtz\n")
            a_file.close()

            #running aimless from within the GUI
            self.super_parent.update_lin_txt(new_line = "aimless < aimless.dat" )
            self.super_parent.onGoBtn(event = True)
            self.second_go_flag = False

        else:
            print "Hi after running pointless and aimless"
        '''

        #flag to tell the caller (main_dui) if HTML view should be updated
        return False







