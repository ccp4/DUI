#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui

from subprocess import call as shell_func

import os

'''

    import_step = step()
    import_step.Bttlabel = "\n\n     import    \n\n"
    import_step.default_action = "dials.import ~/data/th_8_2_0*"
    import_step.InnerBox = btn__img_ibox()
    steps.append(import_step)

    find_step = step()
    find_step.Bttlabel = "\n\n     find spots    \n\n"
    find_step.default_action = "dials.find_spots datablock.json"
    find_step.InnerBox = EmptyInnerBox()
    steps.append(find_step)

    index_step = step()
    index_step.Bttlabel = "\n\n     index    \n\n"
    index_step.default_action = "dials.index datablock.json strong.pickle"
    index_step.InnerBox = btn__img_ibox()
    steps.append(index_step)

    refine_step = step()
    refine_step.Bttlabel = "\n\n     refine    \n\n"
    refine_step.default_action = "dials.refine experiments.json indexed.pickle"
    refine_step.InnerBox = EmptyInnerBox()
    steps.append(refine_step)

    integrate_step = step()
    integrate_step.Bttlabel = "\n\n     integrate    \n\n"
    integrate_step.default_action = "dials.integrate refined_experiments.json refined.pickle"
    integrate_step.InnerBox = btn__img_ibox()
    steps.append(integrate_step)

    export_step = step()
    export_step.Bttlabel = "\n\n     export    \n\n"
    export_step.default_action = "dials.export integrated.pickle integrated.h5"
    export_step.InnerBox = EmptyInnerBox()
    steps.append(export_step)


'''
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

