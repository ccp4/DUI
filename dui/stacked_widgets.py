#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui

from subprocess import call as shell_func
import os

class ImportPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent)

        self.cmd_lin_default = "dials.import ~/data/th_8_2_0*"
        self.button_label = "Import"

        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"

        configGroup = QtGui.QGroupBox("Box 01")
        configLayout = QtGui.QVBoxLayout()



        lin_txt =  QtGui.QLineEdit(self)
        configLayout.addWidget(lin_txt)

        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class SpotFindPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SpotFindPage, self).__init__(parent)

        self.cmd_lin_default = "dials.find_spots datablock.json"
        self.button_label = "Find Spots"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"

        updateGroup = QtGui.QGroupBox("Box 02")
        systemCheckBox = QtGui.QCheckBox("Check 01")

        updateLayout = QtGui.QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateGroup.setLayout(updateLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(updateGroup)

        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class IndexPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(IndexPage, self).__init__(parent)

        self.cmd_lin_default = "dials.index datablock.json strong.pickle"
        self.button_label = "Index"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)



class RefinePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(RefinePage, self).__init__(parent)

        self.cmd_lin_default = "dials.refine experiments.json indexed.pickle"
        self.button_label = "Refine"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/dartlang_logo_small.png"

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class IntegratePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(IntegratePage, self).__init__(parent)

        self.cmd_lin_default = "dials.integrate refined_experiments.json refined.pickle"
        self.button_label = "Integrate"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/nuclear_dartlang_logo_small.png"

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class ExportPage(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ExportPage, self).__init__(parent)


        self.cmd_lin_default = "dials.export integrated.pickle integrated.h5"
        self.button_label = "Export"
        my_dui_path = os.environ["DUI_PATH"]
        self.logo_path = my_dui_path + "/../dui/bird_dartlang_logo_small.png"

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)



if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    #ex = ImportPage()
    #ex = SpotFindPage()
    #ex = IndexPage()
    #ex = RefinePage()
    ex = IntegratePage()
    #ex = ExportPage()

    ex.show()
    sys.exit(app.exec_())




