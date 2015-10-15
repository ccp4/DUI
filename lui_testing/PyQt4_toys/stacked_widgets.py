#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui


class ConfigurationPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ConfigurationPage, self).__init__(parent)

        configGroup = QtGui.QGroupBox("Box 01")
        configLayout = QtGui.QVBoxLayout()



        lin_txt =  QtGui.QLineEdit(self)
        configLayout.addWidget(lin_txt)

        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class UpdatePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpdatePage, self).__init__(parent)

        updateGroup = QtGui.QGroupBox("Box 02")
        systemCheckBox = QtGui.QCheckBox("Check 01")

        updateLayout = QtGui.QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateGroup.setLayout(updateLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(updateGroup)

        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class QueryPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(QueryPage, self).__init__(parent)

        startQueryButton = QtGui.QPushButton("Bttn tst")
        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(startQueryButton)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)


class MyMainDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyMainDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        #self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        #self.contentsWidget.setIconSize(QtCore.QSize(96, 84))
        #self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtGui.QStackedWidget()
        self.pagesWidget.addWidget(ConfigurationPage())
        self.pagesWidget.addWidget(UpdatePage())
        self.pagesWidget.addWidget(QueryPage())

        Go_button = QtGui.QPushButton(" \n\n    Go    \n\n")

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        Go_button.clicked.connect(self.onGoBtn)

        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch(1)
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

    def createIcons(self):
        page_01_button = QtGui.QListWidgetItem(self.contentsWidget)
        #page_01_button.setIcon(QtGui.QIcon(':/images/config.png'))
        page_01_button.setText("Page n 1")
        page_01_button.setTextAlignment(QtCore.Qt.AlignHCenter)
        page_01_button.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        page_02_button = QtGui.QListWidgetItem(self.contentsWidget)
        #page_02_button.setIcon(QtGui.QIcon(':/images/update.png'))
        page_02_button.setText("Page n 2")
        page_02_button.setTextAlignment(QtCore.Qt.AlignHCenter)
        page_02_button.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        page_03_button = QtGui.QListWidgetItem(self.contentsWidget)
        #page_03_button.setIcon(QtGui.QIcon(':/images/query.png'))
        page_03_button.setText("Page n 3")
        page_03_button.setTextAlignment(QtCore.Qt.AlignHCenter)
        page_03_button.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)


    def onGoBtn(self, event):
        print "Go pressed"


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = MyMainDialog()
    sys.exit(dialog.exec_())
