#!/usr/bin/env python

#from PySide import QtCore, QtGui
from PyQt4 import QtCore, QtGui

to_test = '''
PySide.QtGui.QTableView.selectRow(row)
PySide.QtGui.QTableView.setHorizontalHeader(header)

'''

def MyData():
    data_list = [
    ('22', '3.7617', '1.730', '0.612/0.862',  '9000', 'cP', ' 44.48,  44.48,  44.48  90.00  90.00   90.00', ' 87986','           a,b,c'),
    ('21', '3.7617', '1.712', '0.655/0.661',  '9000', 'hR', ' 63.24,  63.24,  77.18  90.00  90.00  120.00', '267338','  -a+b,a+c,a+b-c'),
    ('20', '3.7617', '1.648', '0.612/0.614',  '9000', 'hR', ' 63.15,  63.15,  78.55  90.00  90.00  120.00', '271257',' -b+c,a+b,-a+b+c'),
    ('19', '3.7616', '1.672', '0.643/0.650',  '9000', 'hR', ' 62.30,  62.30,  77.17  90.00  90.00  120.00', '259357','   a-c,b+c,a-b+c'),
    ('18', '3.7616', '1.660', '0.653/0.653',  '9000', 'hR', ' 62.38,  62.38,  75.57  90.00  90.00  120.00', '254645','  b-c,-a+c,a+b+c'),
    ('17', '3.7617', '1.708', '0.631/0.851',  '9000', 'tP', ' 44.55,  44.55,  44.77  90.00  90.00   90.00', ' 88854','           c,a,b'),
    ('16', '3.7617', '1.708', '0.616/0.851',  '9000', 'oC', ' 63.04,  62.81,  44.67  90.00  90.00   90.00', '176861','      -a+c,a+c,b'),
    ('15', '3.7616', '1.625', '0.651/0.651',  '9000', 'mC', ' 62.08,  61.86,  44.22  90.00  90.98   90.00', '169783','       a+c,a-c,b'),
    ('14', '3.7617', '1.632', '0.616/0.616',  '9000', 'mC', ' 63.91,  63.19,  45.13  90.00  89.23   90.00', '182231','      -a+c,a+c,b'),
    ('13', '3.6202', '1.470', '0.639/0.862',  '9000', 'tP', ' 43.00,  43.00,  43.95  90.00  90.00   90.00', ' 81264','           a,b,c'),
    ('12', '3.6202', '1.449', '0.651/0.862',  '9000', 'oC', ' 61.60,  60.68,  44.01  90.00  90.00   90.00', '164520','       a-b,a+b,c'),
    ('11', '3.6199', '1.421', '0.679/0.679',  '9000', 'mC', ' 60.70,  61.72,  44.01  90.00  90.31   90.00', '164865','      a+b,-a+b,c'),
    ('10', '3.6202', '1.425', '0.651/0.651',  '9000', 'mC', ' 61.75,  60.79,  44.15  90.00  90.50   90.00', '165714','       a-b,a+b,c'),
    (' 9', '0.1576', '0.171', '0.832/0.848',  '9000', 'tP', ' 42.41,  42.41,  39.76  90.00  90.00   90.00', ' 71506','           b,c,a'),
    (' 8', '0.1576', '0.172', '0.832/0.923',  '9000', 'oC', ' 60.00,  60.04,  39.78  90.00  90.00   90.00', '143304','       b-c,b+c,a'),
    (' 7', '0.1576', '0.163', '0.860/0.860',  '9000', 'mC', ' 60.05,  60.05,  39.82  90.00  90.13   90.00', '143580','       b-c,b+c,a'),
    (' 6', '0.1482', '0.167', '0.923/0.923',  '9000', 'mC', ' 60.01,  59.99,  39.75  90.00  89.91   90.00', '143090','      b+c,-b+c,a'),
    (' 5', '0.0795', '0.160', '0.832/0.862',  '9000', 'oP', ' 39.76,  42.34,  42.45  90.00  90.00   90.00', ' 71480','           a,b,c'),
    (' 4', '0.0790', '0.161', '0.862/0.862',  '9000', 'mP', ' 39.76,  42.46,  42.34  90.00  89.99   90.00', ' 71482','        -a,-c,-b'),
    (' 3', '0.0795', '0.158', '0.832/0.832',  '9000', 'mP', ' 42.37,  39.79,  42.48  90.00  89.96   90.00', ' 71614','        -b,-a,-c'),
    (' 2', '0.0249', '0.155', '0.851/0.851',  '9000', 'mP', ' 39.77,  42.37,  42.47  90.00  89.90   90.00', ' 71572','           a,b,c'),
    (' 1', '0.0000', '0.155', '        -/-',  '9000', 'aP', ' 39.77,  42.37,  42.47  89.98  89.91   89.98', ' 71553','           a,b,c'),
    ]

    return data_list



class MyTable(QtGui.QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.cellClicked.connect(self.usr_clic)

    def usr_clic(self, row, col):
        print "cellClicked at: ", row, col

    def setContent(self, data_content):
        n_row = len(data_content)
        print "n_row =", n_row
        n_col = len(data_content[0])
        print "n_col =", n_col

        self.setRowCount(n_row)
        self.setColumnCount(n_col)

        #self.setItem(2, 3, QtGui.QTableWidgetItem("Hi there"))

        for row, row_cont in enumerate(data_content):
            for col, col_cont in enumerate(row_cont):
                self.setItem(row, col, QtGui.QTableWidgetItem(col_cont))

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

    import sys
    app = QtGui.QApplication(sys.argv)

    dat = MyData()

    widg = MainWidget()
    widg.dataIn(dat)

    sys.exit(app.exec_())
