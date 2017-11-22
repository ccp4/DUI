#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSql
#from PyQt4 import QtCore, QtGui, QtSql


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    model = QtSql.QSqlTableModel()

    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle("Table Model")
    view.show()

    sys.exit(app.exec_())
