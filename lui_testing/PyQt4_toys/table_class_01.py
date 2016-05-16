#!/usr/bin/env python

from PySide import QtCore, QtGui
#from PyQt4 import QtCore, QtGui

class ApplicationsTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ApplicationsTab, self).__init__(parent)

        localLayout = QtGui.QVBoxLayout()

        tableWidget = QtGui.QTableWidget(5, 4, self)
        localLayout.addWidget( tableWidget  )

        self.setLayout(localLayout)
        self.show()

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    tab = ApplicationsTab()
    sys.exit(app.exec_())
