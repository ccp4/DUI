
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class CustomData(object):
    pass



class InfoWidget( QWidget):
    def __init__(self, parent = None):
        super(InfoWidget, self).__init__()

        cell_group =  QGroupBox(" Crystal Cell ")

        empty_str = "__________0"

        cell_v_layout = QVBoxLayout()

        a_label = QLabel("   a ")
        b_label = QLabel("   b ")
        c_label = QLabel("   c ")
        cell_label_d_layout = QHBoxLayout()
        cell_label_d_layout.addWidget(a_label)
        cell_label_d_layout.addWidget(b_label)
        cell_label_d_layout.addWidget(c_label)
        cell_v_layout.addLayout(cell_label_d_layout)

        a_data = QLabel(empty_str)
        b_data = QLabel(empty_str)
        c_data = QLabel(empty_str)
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(a_data)
        cell_data_layout.addWidget(b_data)
        cell_data_layout.addWidget(c_data)
        cell_v_layout.addLayout(cell_data_layout)
        cell_v_layout.addWidget(QLabel("  "))

        alpha_label = QLabel("  alpha ")
        beta_label = QLabel("   beta ")
        gamma_label = QLabel("  gamma ")
        cell_label_a_layout = QHBoxLayout()
        cell_label_a_layout.addWidget(alpha_label)
        cell_label_a_layout.addWidget(beta_label)
        cell_label_a_layout.addWidget(gamma_label)
        cell_v_layout.addLayout(cell_label_a_layout)

        alpha_data = QLabel(empty_str)
        beta_data = QLabel(empty_str)
        gamma_data = QLabel(empty_str)
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(alpha_data)
        cell_data_layout.addWidget(beta_data)
        cell_data_layout.addWidget(gamma_data)
        cell_v_layout.addLayout(cell_data_layout)

        cell_group.setLayout(cell_v_layout)

        orien_group =  QGroupBox(" Crystal Orientation ")

        r_v_layout = QVBoxLayout()
        r1_label = QLabel("  R 1 ")
        r2_label = QLabel("  R 2 ")
        r3_label = QLabel("  R 3 ")

        r_label_a_layout = QHBoxLayout()
        r_label_a_layout.addWidget(r1_label)
        r_label_a_layout.addWidget(r2_label)
        r_label_a_layout.addWidget(r3_label)

        r_v_layout.addLayout(r_label_a_layout)

        r1_data = QLabel(empty_str)
        r2_data = QLabel(empty_str)
        r3_data = QLabel(empty_str)
        r_data_layout = QHBoxLayout()
        r_data_layout.addWidget(r1_data)
        r_data_layout.addWidget(r2_data)
        r_data_layout.addWidget(r3_data)
        r_v_layout.addLayout(r_data_layout)
        orien_group.setLayout(r_v_layout)


        beam_group =  QGroupBox(" Bean / Source ")

        bm_v_layout = QVBoxLayout()

        xb_label = QLabel("  X Beam ")
        yb_label = QLabel("  Y Beam ")

        bm_label_a_layout = QHBoxLayout()
        bm_label_a_layout.addWidget(xb_label)
        bm_label_a_layout.addWidget(yb_label)

        bm_v_layout.addLayout(bm_label_a_layout)

        xb_data = QLabel(empty_str)
        yb_data = QLabel(empty_str)
        bm_data_layout = QHBoxLayout()
        bm_data_layout.addWidget(xb_data)
        bm_data_layout.addWidget(yb_data)
        bm_v_layout.addLayout(bm_data_layout)

        bm_v_layout.addWidget(QLabel("  "))
        d_dist_label = QLabel("  Detector Distance ")
        bm_v_layout.addWidget(d_dist_label)
        d_dist_data = QLabel(empty_str)
        bm_v_layout.addWidget(yb_data)
        bm_v_layout.addWidget(QLabel("  "))

        beam_group.setLayout(bm_v_layout)

        crys_data = CustomData()
        expm_data = CustomData()

        my_box = QVBoxLayout()
        my_box.addWidget(cell_group)
        my_box.addWidget(orien_group)
        my_box.addWidget(beam_group)

        self.setLayout(my_box)
        self.show()

'''

template for info panel
________________________________
crystal cell

a    b    c

alpha beta gamma
________________________________
crystal orientation

R1           R2           R3
________________________________
bean / source

x - bean       y - bean

Detector distance

'''


if( __name__ == "__main__" ):

    app =  QApplication(sys.argv)
    ex = InfoWidget()
    sys.exit(app.exec_())
