'''
template for info panel
________________________________
crystal cell

a    b    c

alpha betha gahnma
________________________________
crystal orientation

R1           R2           R3
________________________________
bean / source

x - bean       y - bean

Detector distance

'''

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class CustomData(object):
    pass



class InfoWidget( QWidget):
    def __init__(self, parent = None):
        super(InfoWidget, self).__init__()

        cell_group =  QGroupBox(" Crystal Cell ")

        cell_v_layout = QVBoxLayout()

        #abc_label = QLabel("  a            b             c      ")
        a_label = QLabel("   a ")
        b_label = QLabel("   b ")
        c_label = QLabel("   c ")
        cell_label_layout = QHBoxLayout()
        cell_label_layout.addWidget(a_label)
        cell_label_layout.addWidget(b_label)
        cell_label_layout.addWidget(c_label)
        cell_v_layout.addLayout(cell_label_layout)
        #cell_v_layout.addWidget(abc_label)

        a_data = QLabel("    1   ")
        b_data = QLabel("    2   ")
        c_data = QLabel("    3   ")
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(a_data)
        cell_data_layout.addWidget(b_data)
        cell_data_layout.addWidget(c_data)
        cell_v_layout.addLayout(cell_data_layout)

        cell_group.setLayout(cell_v_layout)

        crys_data = CustomData()
        expm_data = CustomData()

        my_box = QVBoxLayout()
        my_box.addWidget(cell_group)
        self.setLayout(my_box)
        self.show()

if( __name__ == "__main__" ):

    app =  QApplication(sys.argv)
    ex = InfoWidget()
    sys.exit(app.exec_())
