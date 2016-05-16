#!/usr/bin/env python

from PySide import QtCore, QtGui, QtSql
#from PyQt4 import QtCore, QtGui, QtSql

class MyModel(QtSql.QSqlTableModel):
    def __init__(self, parent):
        super(MyModel, self).__init__()
        print "Hi there"


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    model = MyModel(app)

    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle("Table Model")
    view.show()

    sys.exit(app.exec_())
