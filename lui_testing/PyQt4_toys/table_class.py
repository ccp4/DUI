#!/usr/bin/env python

#from PySide import QtCore, QtGui, QtSql
from PyQt4 import QtCore, QtGui, QtSql

def createView(title, model):
    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    model = QtSql.QSqlTableModel()
    view1 = createView("Table Model", model)
    view1.show()

    sys.exit(app.exec_())
