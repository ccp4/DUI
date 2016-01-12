#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui


class TabDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TabDialog, self).__init__(parent)

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(PermissionsTab(), "Tab 1")
        tabWidget.addTab(ApplicationsTab(), "tab 2")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)
        self.setWindowTitle("2 Tabs Dialog")

class PermissionsTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PermissionsTab, self).__init__(parent)
        readable = QtGui.QCheckBox("CheckBox")
        localLayout = QtGui.QVBoxLayout()
        localLayout.addWidget(readable)
        self.setLayout(localLayout)

class ApplicationsTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ApplicationsTab, self).__init__(parent)
        topLabel = QtGui.QLabel("label text")
        localLayout = QtGui.QVBoxLayout()
        localLayout.addWidget(topLabel)
        self.setLayout(localLayout)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    tabdialog = TabDialog()
    sys.exit(tabdialog.exec_())
