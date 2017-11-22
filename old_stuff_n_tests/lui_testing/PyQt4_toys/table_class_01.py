#!/usr/bin/env python

from PySide import QtCore, QtGui
#from PyQt4 import QtCore, QtGui

to_test = '''
PySide.QtGui.QTableView.selectRow(row)
PySide.QtGui.QTableView.setHorizontalHeader(header)



'''

class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        localLayout = QtGui.QVBoxLayout()

        tableWidget = QtGui.QTableWidget()
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(5)
        tableWidget.setItem(2, 3, QtGui.QTableWidgetItem("Hi"))
        localLayout.addWidget( tableWidget  )

        self.setLayout(localLayout)
        self.show()

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    widg = MainWidget()
    sys.exit(app.exec_())
