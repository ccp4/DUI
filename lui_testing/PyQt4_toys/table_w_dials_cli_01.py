#!/usr/bin/env python

from PySide import QtCore, QtGui
#from PyQt4 import QtCore, QtGui

to_test = '''
PySide.QtGui.QTableView.selectRow(row)
PySide.QtGui.QTableView.setHorizontalHeader(header)

'''

class MyTable(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)

    def setContent(self, data_content):
        n_row = len(data_content)
        print "n_row =", n_row
        n_col = 1
        print "n_col =", n_col

        self.setRowCount(n_row)
        self.setColumnCount(n_col)

        for row, row_cont in enumerate(data_content):
            self.setItem(row, 0, QtGui.QTableWidgetItem(row_cont))

class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

    def dataIn(self, my_data_lst):

        localLayout = QtGui.QVBoxLayout()

        tableWidget = MyTable()
        tableWidget.setContent(my_data_lst)

        localLayout.addWidget( tableWidget  )

        self.setLayout(localLayout)
        self.show()

if __name__ == '__main__':


    import subprocess
    import sys


    print "before subprocess"
    p = subprocess.Popen("dials.refine_bravais_settings experiments.json indexed.pickle",
                         stdout = subprocess.PIPE, bufsize = 1, shell = True)
    print "after subprocess"

    lst_output_ln = []

    for line in iter(p.stdout.readline, b''):
        single_line = line[0:len(line)-1]
        lst_output_ln.append(single_line)

    p.stdout.close()
    p.wait()

    print "after stdout.close()"

    for local_line in lst_output_ln:
        print local_line

    app = QtGui.QApplication(sys.argv)

    widg = MainWidget()
    widg.dataIn(lst_output_ln)

    sys.exit(app.exec_())
