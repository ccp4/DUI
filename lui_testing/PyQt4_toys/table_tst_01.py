import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MyPopup(QWidget):
    def __init__(self, parent = None):
        super(MyPopup, self).__init__(parent)

        my_table = QTableWidget(5, 6, self)
        my_table.cellClicked.connect(self.usr_clic)

        vbox = QVBoxLayout()
        vbox.addWidget(my_table)
        self.setLayout(vbox)
        self.show()

    def usr_clic(self, row, column):
        print "row, column =", row, column


#Alternatively, tables can be constructed without a given size and resized later:
'''
tableWidget = QTableWidget()
tableWidget.setRowCount(10)
tableWidget.setColumnCount(5)
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyPopup()
    widget.show()
    sys.exit(app.exec_())

