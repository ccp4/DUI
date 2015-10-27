#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui
from stacked_widgets import ImportPage, FindspotstParameterWidget, IndexPage, RefineParameterWidget, IntegrateParameterWidget, ExportParameterWidget

from subprocess import call as shell_func
import os

class MyMainDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(96, 84))
        self.contentsWidget.setMovement(QtGui.QListView.Static)

        self.contentsWidget.setMaximumWidth(148)
        self.contentsWidget.setMinimumHeight(724)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtGui.QStackedWidget()
        self.widget_list = []
        self.widget_list.append(ImportPage())
        print "\n\n"
        self.widget_list.append(FindspotstParameterWidget())
        print "\n\n"
        self.widget_list.append(IndexPage())
        print "\n\n"
        self.widget_list.append(RefineParameterWidget())
        print "\n\n"
        self.widget_list.append(IntegrateParameterWidget())
        print "\n\n"
        self.widget_list.append(ExportParameterWidget())

        for widg in self.widget_list:
            self.pagesWidget.addWidget(widg)

        Go_button = QtGui.QPushButton(" \n\n    Go    \n\n")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        Go_button.clicked.connect(self.onGoBtn)

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        exec_layout = QtGui.QHBoxLayout()

        self.lin_txt =  QtGui.QLineEdit(self)
        exec_layout.addWidget(self.lin_txt)

        exec_layout.addWidget(Go_button)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(horizontalLayout)
        mainLayout.addStretch(1)
        mainLayout.addSpacing(12)
        mainLayout.addLayout(exec_layout)

        main_widget = QtGui.QWidget()
        main_widget.setLayout(mainLayout)
        self.resize(1200, 900)
        self.setCentralWidget(main_widget)


    def changePage(self, current, previous):
        if not current:
            current = previous
        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

        idx = self.pagesWidget.currentIndex()
        cli_str = self.widget_list[idx].cmd_lin_default

        try:
            self.lin_txt.setText(str(cli_str))
        except:
            pass

    def createIcons(self):

        for widget in self.widget_list:

            page_n_button = QtGui.QListWidgetItem(self.contentsWidget)
            page_n_button.setIcon(QtGui.QIcon(widget.logo_path))
            page_n_button.setText(widget.button_label)
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
    dialog.show()
    sys.exit(app.exec_())

