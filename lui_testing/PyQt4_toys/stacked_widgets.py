#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui

from subprocess import call as shell_func
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

        self.button_label = "dials.import ~/data/th_8_2_0*"

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

        self.button_label = "dials.find_spots datablock.json"

        super(SpotFindPage, self).__init__(parent)

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

        self.button_label = "dials.index datablock.json strong.pickle"

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class MyMainDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyMainDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(96, 84))
        self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtGui.QStackedWidget()
        self.widget_list = []
        self.widget_list.append(ImportPage())
        self.widget_list.append(SpotFindPage())
        self.widget_list.append(IndexPage())

        for widg in self.widget_list:
            self.pagesWidget.addWidget(widg)

        Go_button = QtGui.QPushButton(" \n\n    Go    \n\n")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        Go_button.clicked.connect(self.onGoBtn)

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtGui.QHBoxLayout()

        self.lin_txt =  QtGui.QLineEdit(self)
        buttonsLayout.addWidget(self.lin_txt)

        buttonsLayout.addWidget(Go_button)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle("Main GUI")

    def changePage(self, current, previous):
        if not current:
            current = previous
        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

        idx = self.pagesWidget.currentIndex()
        cli_str = self.widget_list[idx].button_label

        try:
            self.lin_txt.setText(str(cli_str))
        except:
            pass

    def createIcons(self):
        for page_text in ["Page n 1","Page n 2","Page n 3"]:
            page_n_button = QtGui.QListWidgetItem(self.contentsWidget)
            #page_n_button.setIcon(QtGui.QIcon(':/images/config.png'))
            page_n_button.setText(page_text)
            page_n_button.setTextAlignment(QtCore.Qt.AlignHCenter)
            page_n_button.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)


    def onGoBtn(self, event):
        print "Go pressed"
        shell_str = str(self.lin_txt.text())
        shell_func(shell_str, shell=True)
        print"\n Ok \n"
        self.lin_txt.setText(str(""))


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = MyMainDialog()
    sys.exit(dialog.exec_())
