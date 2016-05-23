#!/usr/bin/env python

#from PySide import QtCore, QtGui
from PyQt4 import QtCore, QtGui

to_test = '''
PySide.QtGui.QTableView.selectRow(row)
PySide.QtGui.QTableView.setHorizontalHeader(header)
'''

def get_lst_output_ln():
    lst_ln = []
    lst_ln.append("DIALS 1.2.2-g62d8f5d-release                                                                                         ")
    lst_ln.append("The following parameters have been modified:                                                                         ")
    lst_ln.append("                                                                                                                     ")
    lst_ln.append("input {                                                                                                              ")
    lst_ln.append("  experiments = experiments.json                                                                                     ")
    lst_ln.append("  reflections = indexed.pickle                                                                                       ")
    lst_ln.append("}                                                                                                                    ")
    lst_ln.append("                                                                                                                     ")
    lst_ln.append("---------------------------------------------------------------------------------------------------------------------")
    lst_ln.append("Solution Metric fit  rmsd  min/max cc #spots lattice                                 unit_cell volume           cb_op")
    lst_ln.append("---------------------------------------------------------------------------------------------------------------------")
    lst_ln.append("      22     3.7617 1.730 0.612/0.862   9000      cP  44.48  44.48  44.48  90.00  90.00  90.00  87986           a,b,c")
    lst_ln.append("      21     3.7617 1.712 0.655/0.661   9000      hR  63.24  63.24  77.18  90.00  90.00 120.00 267338  -a+b,a+c,a+b-c")
    lst_ln.append("      20     3.7617 1.648 0.612/0.614   9000      hR  63.15  63.15  78.55  90.00  90.00 120.00 271257 -b+c,a+b,-a+b+c")
    lst_ln.append("      19     3.7616 1.672 0.643/0.650   9000      hR  62.30  62.30  77.17  90.00  90.00 120.00 259357   a-c,b+c,a-b+c")
    lst_ln.append("      18     3.7616 1.660 0.653/0.653   9000      hR  62.38  62.38  75.57  90.00  90.00 120.00 254645  b-c,-a+c,a+b+c")
    lst_ln.append("      17     3.7617 1.708 0.631/0.851   9000      tP  44.55  44.55  44.77  90.00  90.00  90.00  88854           c,a,b")
    lst_ln.append("      16     3.7617 1.708 0.616/0.851   9000      oC  63.04  62.81  44.67  90.00  90.00  90.00 176861      -a+c,a+c,b")
    lst_ln.append("      15     3.7616 1.625 0.651/0.651   9000      mC  62.08  61.86  44.22  90.00  90.98  90.00 169783       a+c,a-c,b")
    lst_ln.append("      14     3.7617 1.632 0.616/0.616   9000      mC  63.91  63.19  45.13  90.00  89.23  90.00 182231      -a+c,a+c,b")
    lst_ln.append("      13     3.6202 1.470 0.639/0.862   9000      tP  43.00  43.00  43.95  90.00  90.00  90.00  81264           a,b,c")
    lst_ln.append("      12     3.6202 1.449 0.651/0.862   9000      oC  61.60  60.68  44.01  90.00  90.00  90.00 164520       a-b,a+b,c")
    lst_ln.append("      11     3.6199 1.421 0.679/0.679   9000      mC  60.70  61.72  44.01  90.00  90.31  90.00 164865      a+b,-a+b,c")
    lst_ln.append("      10     3.6202 1.425 0.651/0.651   9000      mC  61.75  60.79  44.15  90.00  90.50  90.00 165714       a-b,a+b,c")
    lst_ln.append("       9     0.1576 0.171 0.832/0.848   9000      tP  42.41  42.41  39.76  90.00  90.00  90.00  71506           b,c,a")
    lst_ln.append("       8     0.1576 0.172 0.832/0.923   9000      oC  60.00  60.04  39.78  90.00  90.00  90.00 143304       b-c,b+c,a")
    lst_ln.append("       7     0.1576 0.163 0.860/0.860   9000      mC  60.05  60.05  39.82  90.00  90.13  90.00 143580       b-c,b+c,a")
    lst_ln.append("       6     0.1482 0.167 0.923/0.923   9000      mC  60.01  59.99  39.75  90.00  89.91  90.00 143090      b+c,-b+c,a")
    lst_ln.append("       5     0.0795 0.160 0.832/0.862   9000      oP  39.76  42.34  42.45  90.00  90.00  90.00  71480           a,b,c")
    lst_ln.append("       4     0.0790 0.161 0.862/0.862   9000      mP  39.76  42.46  42.34  90.00  89.99  90.00  71482        -a,-c,-b")
    lst_ln.append("       3     0.0795 0.158 0.832/0.832   9000      mP  42.37  39.79  42.48  90.00  89.96  90.00  71614        -b,-a,-c")
    lst_ln.append("       2     0.0249 0.155 0.851/0.851   9000      mP  39.77  42.37  42.47  90.00  89.90  90.00  71572           a,b,c")
    lst_ln.append("       1     0.0000 0.155         -/-   9000      aP  39.77  42.37  42.47  89.98  89.91  89.98  71553           a,b,c")
    lst_ln.append("---------------------------------------------------------------------------------------------------------------------")
    lst_ln.append("                                                                                                                     ")
    lst_ln.append("usr+sys time: 1.10 seconds                                                                                           ")
    lst_ln.append("wall clock time: 8.10 seconds                                                                                        ")
    return lst_ln




class TextLine(QtGui.QLineEdit):
    def __init__(self, my_content = None):
        super(TextLine, self).__init__()
        self.setReadOnly(True)
        self.setText(my_content)

class GenericData(object):
    pass

class BuildTable(object):
    def __init__(self, my_data_lst):

        div_n_1 = False
        div_n_2 = False
        div_n_3 = False

        opt_lst = []

        for ln in my_data_lst:
            if( ln[0:5] == "-----" ):
                if( div_n_1 == False ):
                    div_n_1 = True

                elif( div_n_2 == False ):
                    div_n_2 = True

                elif( div_n_3 == False ):
                    div_n_3 = True
                    print "end of MyTable"

                else:
                    print "ERROR to many dividers"

            if( div_n_1 == True and div_n_2 == False and ln[0:5] != "-----" ):
                print "Label =", ln
                label = ln

            elif( div_n_2 == True and div_n_3 == False and ln[0:5] != "-----" ):
                #print "Line to eDD =", ln
                opt_lst.append(ln)

        self.data = GenericData()
        self.data.label = label
        self.data.multline_opt = opt_lst

    def get_table(self):
        return self.data


class TableSelectWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TableSelectWidget, self).__init__(parent)

    def dataIn(self, my_data_lst):
        data_table = BuildTable(my_data_lst)
        data_table = data_table.get_table()

        table_line_layout = QtGui.QVBoxLayout()

        self.line_txt_lst = []
        for i, line_wgt in enumerate(data_table.multline_opt):
            single_line_layout = QtGui.QHBoxLayout()
            line_txt = TextLine(line_wgt)
            self.line_txt_lst.append(line_txt)
            single_line_layout.addWidget(line_txt)
            select_button = QtGui.QPushButton("Select")
            single_line_layout.addWidget(select_button)
            table_line_layout.addLayout(single_line_layout)
            select_button.opt_num = i
            select_button.clicked.connect(self.click_select)

        self.setLayout(table_line_layout)
        self.show()

    def click_select(self, event):
        my_sender = self.sender()
        self.user_opt = my_sender.opt_num
        print "opt_num =", self.user_opt

        for line_txt in self.line_txt_lst:
            line_txt.deselect()

        self.line_txt_lst[self.user_opt].setSelection(1,260)


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)

    dat = get_lst_output_ln()

    widg = TableSelectWidget()
    widg.dataIn(dat)

    sys.exit(app.exec_())
