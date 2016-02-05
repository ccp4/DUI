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

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui

from phil_param_widget_builder import ParameterWidget
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
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"

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
        self.log_json_txt.setCurrentFont(QtGui.QFont("Monospace"))
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

    def find_my_img_dir(self, event):
        selected_file_path = QtGui.QFileDialog.getOpenFileName(self, "Open IMG Dir")
        print "[file path found] =", selected_file_path

        if( selected_file_path ):
            for pos, single_char in enumerate(selected_file_path):
                if( single_char == "/" or single_char == "\\" ):
                    pos_sep = pos

            dir_name = selected_file_path[:pos_sep]
            print "dir_name(final) =", dir_name
            self.lin_import_path.setText(dir_name)
            self.cmd_lin_default = "dials.import "+ dir_name
            print "CLI =", self.cmd_lin_default

        else:
            print "Failed to pick dir"
            self.cmd_lin_default = " "

        self.super_parent.gui_line_edit.setText(self.cmd_lin_default)


    def change_w_dir(self, event):
        dir_name = QtGui.QFileDialog.getExistingDirectory(self, "Change Working Dir")
        print "[dir path found] =", dir_name

        if( dir_name ):
            print "dir_name(final) =", dir_name
            self.w_dir_str = dir_name
            os.chdir(self.w_dir_str)
            self.w_dir_lin.setText(self.w_dir_str)

        else:
            print "Failed to pick dir"




class FindspotstParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from find_spots_mult_opt import ParamMainWidget
        super(FindspotstParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParamMainWidget()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"




class IndexParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from index_mult_opt import ParamMainWidget
        super(IndexParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParamMainWidget()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "Index"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"



class SimplerParamTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SimplerParamTab, self).__init__(parent)
        scan_varying_check = QtGui.QCheckBox("scan_varying")
        use_all_refl_check = QtGui.QCheckBox("use_all_reflections")
        localLayout = QtGui.QVBoxLayout()
        localLayout.addWidget(scan_varying_check)
        localLayout.addWidget(use_all_refl_check)
        self.setLayout(localLayout)


class RefineParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from refine_mult_opt import ParamMainWidget
        super(RefineParameterWidget, self).__init__(parent)
        self.super_parent = parent

        param_widg = ParamMainWidget()
        default_tab = SimplerParamTab()

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(default_tab, "Tab 1")

        tabWidget.addTab(param_widg, "tab 2")


        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "Refine"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"


class IntegrateParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from integrate_mult_opt import ParamMainWidget
        super(IntegrateParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParamMainWidget()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.integrate refined_experiments.json refined.pickle"
        self.button_label = "Integrate"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"


class ExportParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        try:
            from dials.command_line.export import phil_scope
        except:
            from dials.command_line.export_mtz import phil_scope

        super(ExportParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)
        self.cmd_lin_default = "dials.export integrated.pickle refined_experiments.json"
        old_ver = '''
        self.cmd_lin_default = "dials.export experiments.json integrated.pickle hklout=integrated.mtz"
        '''
        self.button_label = "Export mtx"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"


class MainWindow(QtGui.QMainWindow):

  def __init__(self, parent=None):

    # Call the parent constructor
    super(MainWindow, self).__init__(parent)

    # Create the parameter window widget
    params = FindspotstParameterWidget(self)
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

  def update_lin_txt(self):
    print "from tmp parent.update_lin_txt"

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

