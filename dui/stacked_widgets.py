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

from cli_interactions import ImgTab, TextBrows, HtmlTab

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
        self.button_label = "Import"

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

        #self.log_json_txt = QtGui.QTextBrowser()
        #self.log_json_txt.setTextColor(QtGui.QColor("black"))

        self.auto_next_check = QtGui.QCheckBox("Enable auto-Next Feature")
        self.auto_next_check.stateChanged.connect(self.changed_auto_next)
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(import_path_group)
        mainLayout.addWidget(w_dir_group)

        imageLabel = QtGui.QLabel()
        dials_logo_path = my_dui_path + "/../dui/resources/DIALS_Logo_scaled.png"
        #dials_logo_path = my_dui_path + "/../dui/resources/DIALS_Logo.png"
        image = QtGui.QImage(dials_logo_path)
        imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        mainLayout.addWidget(imageLabel)
        #imageLabel.setScaledContents(True)


        #mainLayout.addWidget(self.log_json_txt)
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

        self.super_parent.gui_line_edit.setText(self.cmd_lin_default)


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

    def add_tabs(self, simpler_par_widget = None, advanced_par_widget = None):

        ltabWidget = QtGui.QTabWidget()

        if( simpler_par_widget != None ):
            default_tab = simpler_par_widget
            ltabWidget.addTab(default_tab, "Simple")

        if( advanced_par_widget != None ):
            param_widg = advanced_par_widget
            ltabWidget.addTab(param_widg, "Advanced")

        rtabWidget = QtGui.QTabWidget()
        self.multi_line_txt = TextBrows()
        self.report_out_widg = HtmlTab()
        self.analyse_out_img = ImgTab(self.super_parent)

        rtabWidget.addTab(self.multi_line_txt, "Shell Log")
        rtabWidget.addTab(self.report_out_widg, "HTML output")
        rtabWidget.addTab(self.analyse_out_img, "Graphic Reports")

        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(ltabWidget)
        mainLayout.addWidget(rtabWidget)
        self.setLayout(mainLayout)


class FindspotsSimplerParameterTab(QtGui.QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the spot-finder, this widget is the first to appear once the button
    "Find Sots" at the left side of the GUI is clicked

    '''
    def __init__(self, parent = None):
        super(FindspotsSimplerParameterTab, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog


        xds_gain_label = QtGui.QLabel("spotfinder.threshold.xds.gain")
        xds_gain_spn_bx = QtGui.QDoubleSpinBox()
        xds_gain_spn_bx.local_path = "spotfinder.threshold.xds.gain"
        xds_gain_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_kernel_size_label_x = QtGui.QLabel("spotfinder.threshold.xds.kernel_size(X)")
        xds_kernel_size_spn_bx_x = QtGui.QSpinBox()
        xds_kernel_size_spn_bx_x.local_path = "spotfinder.threshold.xds.kernel_size(X)"
        xds_kernel_size_spn_bx_x.valueChanged.connect(self.spnbox_changed)

        xds_kernel_size_label_y = QtGui.QLabel("spotfinder.threshold.xds.kernel_size(Y)")
        xds_kernel_size_spn_bx_y = QtGui.QSpinBox()
        xds_kernel_size_spn_bx_y.local_path = "spotfinder.threshold.xds.kernel_size(Y)"
        xds_kernel_size_spn_bx_y.valueChanged.connect(self.spnbox_changed)

        xds_sigma_background_label = QtGui.QLabel("spotfinder.threshold.xds.sigma_background")
        xds_sigma_background_spn_bx = QtGui.QDoubleSpinBox()
        xds_sigma_background_spn_bx.local_path = "spotfinder.threshold.xds.sigma_background"
        xds_sigma_background_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_sigma_strong_label = QtGui.QLabel("spotfinder.threshold.xds.sigma_strong")
        xds_sigma_strong_spn_bx = QtGui.QDoubleSpinBox()
        xds_sigma_strong_spn_bx.local_path = "spotfinder.threshold.xds.sigma_strong"
        xds_sigma_strong_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_global_threshold_label = QtGui.QLabel("spotfinder.threshold.xds.global_threshold")
        xds_global_threshold_spn_bx = QtGui.QDoubleSpinBox()
        xds_global_threshold_spn_bx.local_path = "spotfinder.threshold.xds.global_threshold"
        xds_global_threshold_spn_bx.valueChanged.connect(self.spnbox_changed)

        localLayout = QtGui.QVBoxLayout()

        xds_gain_hb = QtGui.QHBoxLayout()
        xds_gain_hb.addWidget(xds_gain_label)
        xds_gain_hb.addWidget(xds_gain_spn_bx)
        localLayout.addLayout(xds_gain_hb)

        xds_kernel_size_hb_x = QtGui.QHBoxLayout()
        xds_kernel_size_hb_x.addWidget(xds_kernel_size_label_x)
        xds_kernel_size_hb_x.addWidget(xds_kernel_size_spn_bx_x)
        localLayout.addLayout(xds_kernel_size_hb_x)

        xds_kernel_size_hb_y = QtGui.QHBoxLayout()
        xds_kernel_size_hb_y.addWidget(xds_kernel_size_label_y)
        xds_kernel_size_hb_y.addWidget(xds_kernel_size_spn_bx_y)
        localLayout.addLayout(xds_kernel_size_hb_y)


        xds_sigma_background_hb = QtGui.QHBoxLayout()
        xds_sigma_background_hb.addWidget(xds_sigma_background_label)
        xds_sigma_background_hb.addWidget(xds_sigma_background_spn_bx)
        localLayout.addLayout(xds_sigma_background_hb)

        xds_sigma_strong_hb = QtGui.QHBoxLayout()
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_label)
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_spn_bx)
        localLayout.addLayout(xds_sigma_strong_hb)

        xds_global_threshold_hb = QtGui.QHBoxLayout()
        xds_global_threshold_hb.addWidget(xds_global_threshold_label)
        xds_global_threshold_hb.addWidget(xds_global_threshold_spn_bx)
        localLayout.addLayout(xds_global_threshold_hb)
        localLayout.addStretch(1)

        self.setLayout(localLayout)


    def spnbox_changed(self, value):
        sender = self.sender()
        str_value = str(value)
        print value
        print "local_path =",
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value)
        self.super_parent.update_lin_txt(sender.local_path, value)


class FindspotsParameterWidget(GenericParameterWidget):
    def __init__(self, parent=None):
        from resources.find_spots_mult_opt import ParamMainWidget
        super(FindspotsParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = FindspotsSimplerParameterTab(self.super_parent)
        self.add_tabs(simpler_par_widget = default_tab, advanced_par_widget = param_widg)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/find_spots.png"



class IndexSimplerParamTab(QtGui.QWidget):


    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the indexer, this widget is the first to appear once the button
    "Index" at the left side of the GUI is clicked

    '''

    def __init__(self, parent=None):
        super(IndexSimplerParamTab, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        hbox_lay_scan_varying =  QtGui.QHBoxLayout()
        label_scan_varying = QtGui.QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QtGui.QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)

        indexing_method_check = QtGui.QCheckBox("indexing.method")
        hbox_method =  QtGui.QHBoxLayout()
        label_method_62 = QtGui.QLabel("indexing.method")
        hbox_method.addWidget(label_method_62)
        box_method_62 = QtGui.QComboBox()
        box_method_62.tmp_lst=[]
        box_method_62.local_path = "indexing.method"
        box_method_62.tmp_lst.append("*fft3d")
        box_method_62.tmp_lst.append("fft1d")
        box_method_62.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_62.tmp_lst:
            box_method_62.addItem(lst_itm)
        box_method_62.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(box_method_62)

        localLayout = QtGui.QVBoxLayout()
        localLayout.addLayout(hbox_lay_scan_varying)

        localLayout.addLayout(hbox_method)

        localLayout.addStretch(1)

        self.setLayout(localLayout)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value)

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

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = IndexSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = default_tab, advanced_par_widget = param_widg)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "Index"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/index.png"


class RefineSimplerParamTab(QtGui.QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the refiner, this widget is the first to appear once the button
    "Refine" at the left side of the GUI is clicked
    '''

    def __init__(self, parent=None):
        super(RefineSimplerParamTab, self).__init__(parent)

        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        hbox_lay_scan_varying =  QtGui.QHBoxLayout()
        localLayout = QtGui.QVBoxLayout()
        label_scan_varying = QtGui.QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QtGui.QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)
        localLayout.addLayout(hbox_lay_scan_varying)
        localLayout.addStretch(1)
        self.setLayout(localLayout)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value)

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

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = RefineSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = default_tab, advanced_par_widget = param_widg)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "Refine"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/refine.png"


class IntegrateSimplerParamTab(QtGui.QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the integrate algorithm, this widget is the first to appear once the button
    "Integrate" at the left side of the GUI is clicked

    '''
    def __init__(self, parent=None):
        super(IntegrateSimplerParamTab, self).__init__(parent)
        localLayout = QtGui.QVBoxLayout()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        PrFit_lay_out =  QtGui.QHBoxLayout()
        label_PrFit = QtGui.QLabel("integration.profile.fitting")
        PrFit_lay_out.addWidget(label_PrFit)

        PrFit_comb_bx = QtGui.QComboBox()
        PrFit_comb_bx.local_path = "integration.profile.fitting"
        PrFit_comb_bx.tmp_lst=[]
        PrFit_comb_bx.tmp_lst.append("True")
        PrFit_comb_bx.tmp_lst.append("False")

        for lst_itm in PrFit_comb_bx.tmp_lst:
            PrFit_comb_bx.addItem(lst_itm)
        PrFit_comb_bx.currentIndexChanged.connect(self.combobox_changed)
        PrFit_lay_out.addWidget(PrFit_comb_bx)
        localLayout.addLayout(PrFit_lay_out)

        hbox_lay_algorithm_53 =  QtGui.QHBoxLayout()
        label_algorithm_53 = QtGui.QLabel("integration.background.algorithm")
        hbox_lay_algorithm_53.addWidget(label_algorithm_53)

        box_algorithm_53 = QtGui.QComboBox()
        box_algorithm_53.local_path = "integration.background.algorithm"
        box_algorithm_53.tmp_lst=[]
        box_algorithm_53.tmp_lst.append("simple")
        box_algorithm_53.tmp_lst.append("null")
        box_algorithm_53.tmp_lst.append("*glm")
        box_algorithm_53.tmp_lst.append("const_d")
        for lst_itm in box_algorithm_53.tmp_lst:
            box_algorithm_53.addItem(lst_itm)
        box_algorithm_53.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_53.addWidget(box_algorithm_53)
        localLayout.addLayout(hbox_lay_algorithm_53)
        localLayout.addStretch(1)
        self.setLayout(localLayout)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value)


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

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = IntegrateSimplerParamTab(self.super_parent)
        self.add_tabs(simpler_par_widget = default_tab, advanced_par_widget = param_widg)


        self.cmd_lin_default = "dials.integrate refined_experiments.json refined.pickle"
        self.button_label = "Integrate"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/integrate.png"


class ExportSimplerParameterWidget(QtGui.QWidget):
    '''
    This widget like the import one has no multiple tabs, but it does have
    auto generated code on it
    '''

    def __init__(self, parent=None):
        from resources.export_mult_opt import ParamMainWidget
        super(ExportSimplerParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog


        hbox_lay_hklout_6 = QtGui.QHBoxLayout()
        label_hklout_6 = QtGui.QLabel("    hklout")

        label_hklout_6.setFont(QtGui.QFont("Monospace"))
        hbox_lay_hklout_6.addWidget(label_hklout_6)

        box_hklout_6 = QtGui.QLineEdit()
        box_hklout_6.local_path = "mtz.hklout"
        #box_hklout_6.textChanged.connect(self.spnbox_changed)

        hbox_lay_hklout_6.addWidget(box_hklout_6)
        bg_box = QtGui.QVBoxLayout()
        bg_box.addLayout(hbox_lay_hklout_6)

        PrFit_lay_out =  QtGui.QHBoxLayout()
        label_PrFit = QtGui.QLabel("integration.profile.fitting")
        PrFit_lay_out.addWidget(label_PrFit)
        PrFit_comb_bx = QtGui.QComboBox()
        PrFit_comb_bx.local_path = "integration.profile.fitting"
        PrFit_comb_bx.tmp_lst=[]
        PrFit_comb_bx.tmp_lst.append("True")
        PrFit_comb_bx.tmp_lst.append("False")

        for lst_itm in PrFit_comb_bx.tmp_lst:
            PrFit_comb_bx.addItem(lst_itm)
        #PrFit_comb_bx.currentIndexChanged.connect(self.combobox_changed)
        PrFit_lay_out.addWidget(PrFit_comb_bx)



        bg_box.addLayout(PrFit_lay_out)

        bg_box.addStretch()

        self.setLayout(bg_box)





class ExportParameterWidget(GenericParameterWidget):
    '''
    This widget like the import one has no multiple tabs, but it does have
    auto generated code on it
    '''

    def __init__(self, parent=None):
        from resources.export_mult_opt import ParamMainWidget
        super(ExportParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = ExportSimplerParameterWidget(self.super_parent)
        self.add_tabs(simpler_par_widget = default_tab, advanced_par_widget = param_widg)



        self.cmd_lin_default = "dials.export integrated.pickle refined_experiments.json"
        self.button_label = "Export mtz"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/resources/export.png"

        To_run_pointless_n_aimless__simplest_case = '''

        pointless < pointless.dat | tee pointless.log
        aimless < aimless.dat | tee aimless.log

        where pointless.dat contains:
        HKLIN integrated.mtz
        HKLOUT unscaled.mtz

        And aimless.dat contains:
        HKLIN unscaled.mtz
        HKLOUT scaled.mtz
        '''


