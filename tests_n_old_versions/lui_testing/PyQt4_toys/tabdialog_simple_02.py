#!/usr/bin/env python

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TabDialog(QDialog):
    def __init__(self, parent=None):
        super(TabDialog, self).__init__()

        tabWidget = QTabWidget()
        tabWidget.addTab(PermissionsTab(), "Tab 1")
        tabWidget.addTab(ApplicationsTab(), "tab 2")

        tabWidget.currentChanged.connect(self.tab_changed)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)
        self.setWindowTitle("2 Tabs Dialog")

    def tab_changed(self, num):
        print "tab changed to:", num

class PermissionsTab(QWidget):
    def __init__(self, parent=None):
        super(PermissionsTab, self).__init__()

        readable = QCheckBox("CheckBox")
        localLayout = QVBoxLayout()
        localLayout.addWidget(readable)
        self.setLayout(localLayout)

class ApplicationsTab(QWidget):
    def __init__(self, parent=None):
        super(ApplicationsTab, self).__init__()

        topLabel = QLabel("label text")
        localLayout = QVBoxLayout()
        localLayout.addWidget(topLabel)
        self.setLayout(localLayout)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    tabdialog = TabDialog()
    sys.exit(tabdialog.exec_())
