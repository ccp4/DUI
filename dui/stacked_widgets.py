#!/usr/bin/env python

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


from python_qt_bind import GuiBinding
gui_lib = GuiBinding()
print "using ", gui_lib.pyhon_binding
qt_tool = gui_lib.pyhon_binding

if( qt_tool == "PyQt4" ):
    from PyQt4 import QtCore, QtGui, QtWebKit

else:
    from PySide import QtCore, QtGui, QtWebKit

import os

class ImportPage(QtGui.QWidget):
    # FIXME when the user enters a path without images dials fails to import
    # but does not raises an error consequently there is no red output in the GUI
    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent)
        self.super_parent = parent

        self.w_dir_str = os.getcwd()
        self.cmd_lin_default = "dials.import ~/put/your/path/here"
        self.button_label = "Import"

        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/import.png"

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
        self.w_dir_lin.setText(self.w_dir_str)
        w_dir_layout.addWidget(self.w_dir_lin)
        w_dir_button = QtGui.QPushButton(" \n    Change Working Dir    . \n")
        w_dir_button.clicked.connect(self.change_w_dir)
        w_dir_layout.addWidget(w_dir_button)
        w_dir_group.setLayout(w_dir_layout)

        self.log_json_txt = QtGui.QTextBrowser()
        #self.log_json_txt.setMaximumHeight(724)
        #self.log_json_txt.setMinimumHeight(24)

        self.log_json_txt.setTextColor(QtGui.QColor("black"))

        self.auto_next_check = QtGui.QCheckBox("Enable auto-Next Feature")
        self.auto_next_check.stateChanged.connect(self.changed_auto_next)
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(import_path_group)
        mainLayout.addWidget(w_dir_group)
        mainLayout.addWidget(self.log_json_txt)
        mainLayout.addStretch(1)
        mainLayout.addWidget(self.auto_next_check)

        self.setLayout(mainLayout)


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
        dir_name = QtGui.QFileDialog.getExistingDirectory(self, "Change Working Dir")
        print "[dir path found] =", dir_name

        if( dir_name ):
            print "dir_name(final) =", dir_name
            self.w_dir_str = dir_name
            os.chdir(self.w_dir_str)
            self.w_dir_lin.setText(self.w_dir_str)

        else:
            print "Failed to pick dir"


class FindspotsSimplerParameterTab(QtGui.QWidget):
    def __init__(self, parent = None):
        super(FindspotsSimplerParameterTab, self).__init__(parent)
        self.super_parent = parent


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


        self.setLayout(localLayout)


    def spnbox_changed(self, value):
        sender = self.sender()
        str_value = str(value)
        print value
        print "local_path =",
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value)
        self.super_parent.update_lin_txt(sender.local_path, value)


class FindspotsParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from find_spots_mult_opt import ParamMainWidget
        super(FindspotsParameterWidget, self).__init__(parent)
        self.super_parent = parent

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = FindspotsSimplerParameterTab(self.super_parent)
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(default_tab, "Simple")
        tabWidget.addTab(param_widg, "Advanced")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/find_spots.png"


class IndexSimplerParamTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(IndexSimplerParamTab, self).__init__(parent)
        self.super_parent = parent

        hbox_lay_scan_varying_117 =  QtGui.QHBoxLayout()
        label_scan_varying_117 = QtGui.QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying_117.addWidget(label_scan_varying_117)

        box_scan_varying_117 = QtGui.QComboBox()
        box_scan_varying_117.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_117.tmp_lst=[]
        box_scan_varying_117.tmp_lst.append("True")
        box_scan_varying_117.tmp_lst.append("False")
        for lst_itm in box_scan_varying_117.tmp_lst:
            box_scan_varying_117.addItem(lst_itm)
        box_scan_varying_117.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_117.addWidget(box_scan_varying_117)

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
        localLayout.addLayout(hbox_lay_scan_varying_117)

        localLayout.addLayout(hbox_method)
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

class IndexParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from index_mult_opt import ParamMainWidget
        super(IndexParameterWidget, self).__init__(parent)
        self.super_parent = parent

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = IndexSimplerParamTab(self.super_parent)

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(default_tab, "Simple")
        tabWidget.addTab(param_widg, "Advanced")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "Index"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/index.png"


class RefineSimplerParamTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RefineSimplerParamTab, self).__init__(parent)
        self.super_parent = parent

        hbox_lay_scan_varying_117 =  QtGui.QHBoxLayout()
        label_scan_varying_117 = QtGui.QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying_117.addWidget(label_scan_varying_117)

        box_scan_varying_117 = QtGui.QComboBox()
        box_scan_varying_117.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_117.tmp_lst=[]
        box_scan_varying_117.tmp_lst.append("True")
        box_scan_varying_117.tmp_lst.append("False")
        for lst_itm in box_scan_varying_117.tmp_lst:
            box_scan_varying_117.addItem(lst_itm)
        box_scan_varying_117.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_117.addWidget(box_scan_varying_117)

        self.setLayout(hbox_lay_scan_varying_117)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value)

class RefineParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from refine_mult_opt import ParamMainWidget
        super(RefineParameterWidget, self).__init__(parent)
        self.super_parent = parent

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = RefineSimplerParamTab(self.super_parent)

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(default_tab, "Simple")

        tabWidget.addTab(param_widg, "Advanced")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "Refine"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/refine.png"


class IntegrateSimplerParamTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(IntegrateSimplerParamTab, self).__init__(parent)
        localLayout = QtGui.QVBoxLayout()
        self.super_parent = parent

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


class IntegrateParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from integrate_mult_opt import ParamMainWidget
        super(IntegrateParameterWidget, self).__init__(parent)
        self.super_parent = parent

        param_widg = ParamMainWidget(self.super_parent)
        default_tab = IntegrateSimplerParamTab(self.super_parent)

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(default_tab, "Simple")
        tabWidget.addTab(param_widg, "Advanced")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.integrate refined_experiments.json refined.pickle"
        self.button_label = "Integrate"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/integrate.png"


class ExportParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from export_mult_opt import ParamMainWidget
        super(ExportParameterWidget, self).__init__(parent)
        self.super_parent = parent

        param_widg = ParamMainWidget(self.super_parent)


        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.export integrated.pickle refined_experiments.json"
        self.button_label = "Export mtz"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/export.png"



class MainWindow(QtGui.QMainWindow):

  def __init__(self, parent=None):

    # Call the parent constructor
    super(MainWindow, self).__init__(parent)

    # Create the parameter window widget
    params = FindspotsParameterWidget(self)
    #params = IndexParameterWidget()
    #params = RefineParameterWidget()
    #params = IntegrateParameterWidget()
    #params = ExportParameterWidget()

    # Create the window layout
    layout = QtGui.QVBoxLayout()
    layout.addWidget(params)

    # Setup the window contents
    window = QtGui.QWidget()
    window.setLayout(layout)
    self.setCentralWidget(window)

if __name__ == '__main__':
  import sys

  # Create the application
  app = QtGui.QApplication(sys.argv)

  # Create the main window
  window = MainWindow()
  window.resize(800, 600)
  window.show()

  # Execute the application
  sys.exit(app.exec_())

