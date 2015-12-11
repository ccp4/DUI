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

from subprocess import call as shell_func
import os

class ImportPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent)

        self.super_parent = parent

        self.cmd_lin_default = "dials.import ~/put/your/path/here"
        self.button_label = "Import"

        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"

        configGroup = QtGui.QGroupBox("Experiment IMG Directory")
        configLayout = QtGui.QHBoxLayout()

        self.lin_txt =  QtGui.QLineEdit(self)
        configLayout.addWidget(self.lin_txt)
        dir_but = QtGui.QPushButton(" \n    Find experiment dir            . \n")
        dir_but.clicked.connect(self.find_my_dir)
        configLayout.addWidget(dir_but)
        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def find_my_dir(self, event):
        dir_name = QtGui.QFileDialog.getOpenFileName(self, "Open IMG Dir")
        print "[file path found] =", dir_name
        if dir_name:
            to_try_to_fix_later = '''
            for pos, single_char in enumerate(dir_name):
                print "single_char =", single_char
                print "pos =", pos
                if( single_char == "." ):
                    pos_dot = pos

            print "pos_dot =", pos_dot
            print "[char in pos_dot] =", dir_name[pos_dot]

            found_non_number = False
            for pos in range(pos_dot - 1,0,-1):
                print "pos =", pos
                print "dir_name[pos] =", dir_name[pos]
                if( dir_name[pos] != "0" and dir_name[pos] != "1" and
                    dir_name[pos] != "2" and dir_name[pos] != "3" and
                    dir_name[pos] != "4" and dir_name[pos] != "5" and
                    dir_name[pos] != "6" and dir_name[pos] != "7" and
                    dir_name[pos] != "8" and dir_name[pos] != "9" ):

                    found_non_number = True
                    pos_non_num = pos
                    print "should exit for loop here"
                    break

            if( found_non_number ):
                #dir_name = dir_name[:pos_non_num] + "*" + dir_name[pos_dot:]
                dir_name = dir_name[:pos_non_num + 1] + "*"
            print "final dir_name =", dir_name
        '''
        if( dir_name ):
            for pos, single_char in enumerate(dir_name):
                print "single_char =", single_char
                print "pos =", pos
                if( single_char == "/" or single_char == "\\" ):
                    pos_sep = pos
            dir_name = dir_name[:pos_sep]
            print "dir_name(final) =", dir_name
            self.lin_txt.setText(dir_name)
            self.cmd_lin_default = "dials.import "+ dir_name
            print "CLI =", self.cmd_lin_default

        else:
            print "Failed to pick dir"
            self.cmd_lin_default = " "

        self.super_parent.gui_line_edit.setText(self.cmd_lin_default)


class FindspotstParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.find_spots import phil_scope
        super(FindspotstParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"


class IndexParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.index import phil_scope
        super(IndexParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "Index"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"



class RefineParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.refine import phil_scope
        super(RefineParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(param_widg)
        self.setLayout(mainLayout)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "Refine"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"


class IntegrateParameterWidget(QtGui.QWidget):

    def __init__(self, parent=None):
        from dials.command_line.integrate import phil_scope
        super(IntegrateParameterWidget, self).__init__(parent)

        self.super_parent = parent
        param_widg = ParameterWidget(self.super_parent, phil_scope)

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

        self.cmd_lin_default = "dials.export experiments.json integrated.pickle hklout=integrated.mtz"
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

