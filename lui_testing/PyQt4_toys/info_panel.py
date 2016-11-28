from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class CrystalData(object):
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.spg_group = None


class InstrumentData(object):
    def __init__(self):
        self.r1 = None
        self.r2 = None
        self.r3 = None
        self.xb = None
        self.yb = None
        self.dd = None

def update_crystal(experiments_path):

    dat = CrystalData()

    try:

        from dxtbx.model.experiment.experiment_list import ExperimentListFactory
        experiments = ExperimentListFactory.from_json_file(
                      experiments_path, check_format=False)

        print "len(experiments)", len(experiments)

        exp = experiments[0]
        unit_cell = exp.crystal.get_unit_cell()
        dat.a, dat.b, dat.c, dat.alpha, dat.beta, dat.gamma = unit_cell.parameters()

    except:
        print "Unable to find cell data"

    return dat


def update_intrument(exp_dat):
    exp_dat.r1 = 90.02
    exp_dat.r2 = 89.8
    exp_dat.r3 = 91.4
    exp_dat.xb = 1588
    exp_dat.yb = 1466
    exp_dat.dd = 2135


def update_data_label(data_label, data_info):
    if( data_info == None ):
        data_label.setText("   -      ")
        data_label.setStyleSheet("background-color: white")

    else:
        rnd_nm = round(data_info, ndigits=4)
        data_label.setText(str(rnd_nm))
        data_label.setStyleSheet("background-color: white")


class InfoWidget( QWidget):
    def __init__(self, parent = None):
        super(InfoWidget, self).__init__()

        cell_group =  QGroupBox(" Crystal Cell ")

        empty_str = "__________"

        cell_v_layout = QVBoxLayout()

        a_label = QLabel("   a ")
        b_label = QLabel("   b ")
        c_label = QLabel("   c ")
        cell_label_d_layout = QHBoxLayout()
        cell_label_d_layout.addWidget(a_label)
        cell_label_d_layout.addWidget(b_label)
        cell_label_d_layout.addWidget(c_label)
        cell_v_layout.addLayout(cell_label_d_layout)

        self.a_data = QLabel(empty_str)
        self.b_data = QLabel(empty_str)
        self.c_data = QLabel(empty_str)
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(self.a_data)
        cell_data_layout.addWidget(self.b_data)
        cell_data_layout.addWidget(self.c_data)
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

        self.alpha_data = QLabel(empty_str)
        self.beta_data = QLabel(empty_str)
        self.gamma_data = QLabel(empty_str)
        cell_data_layout = QHBoxLayout()
        cell_data_layout.addWidget(self.alpha_data)
        cell_data_layout.addWidget(self.beta_data)
        cell_data_layout.addWidget(self.gamma_data)
        cell_v_layout.addLayout(cell_data_layout)

        cell_group.setLayout(cell_v_layout)

        orien_group =  QGroupBox(" Crystal Orientation ")

        r_v_layout = QVBoxLayout()
        umatr_label = QLabel("      U matrix    ")


        orien_group.setLayout(r_v_layout)


        beam_group =  QGroupBox(" Bean / Source ")

        bm_v_layout = QVBoxLayout()

        xb_label = QLabel("  X Beam ")
        yb_label = QLabel("  Y Beam ")

        bm_label_a_layout = QHBoxLayout()
        bm_label_a_layout.addWidget(xb_label)
        bm_label_a_layout.addWidget(yb_label)

        bm_v_layout.addLayout(bm_label_a_layout)

        self.xb_data = QLabel(empty_str)
        self.yb_data = QLabel(empty_str)
        bm_data_layout = QHBoxLayout()
        bm_data_layout.addWidget(self.xb_data)
        bm_data_layout.addWidget(self.yb_data)
        bm_v_layout.addLayout(bm_data_layout)

        bm_v_layout.addWidget(QLabel("  "))
        d_dist_label = QLabel("  Detector Distance ")
        bm_v_layout.addWidget(d_dist_label)
        self.d_dist_data = QLabel(empty_str)
        bm_v_layout.addWidget(self.d_dist_data)
        bm_v_layout.addWidget(QLabel("  "))

        beam_group.setLayout(bm_v_layout)

        self.expm_data = InstrumentData()

        my_box = QVBoxLayout()
        my_box.addWidget(cell_group)
        my_box.addWidget(orien_group)
        my_box.addWidget(beam_group)

        #next 3 lines and connections will be removed when this goes to the main GUI
        update_data = QPushButton(self)
        update_data.clicked.connect(self.btn_clicked)
        my_box.addWidget(update_data)

        self.setLayout(my_box)
        self.show()

    def btn_clicked(self):
        self.update_data()

    def update_data(self):

        self.crys_data = update_crystal(
        "/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/3_index/experiments.json")

        update_intrument(self.expm_data)

        update_data_label(self.a_data, self.crys_data.a)
        update_data_label(self.b_data, self.crys_data.b)
        update_data_label(self.c_data, self.crys_data.c)

        update_data_label(self.alpha_data, self.crys_data.alpha)
        update_data_label(self.beta_data , self.crys_data.beta)
        update_data_label(self.gamma_data, self.crys_data.gamma)

        update_data_label(self.r1_data, self.expm_data.r1)
        update_data_label(self.r2_data, self.expm_data.r2)
        update_data_label(self.r3_data, self.expm_data.r3)
        update_data_label(self.xb_data, self.expm_data.xb)
        update_data_label(self.yb_data, self.expm_data.yb)
        update_data_label(self.d_dist_data, self.expm_data.dd)


if( __name__ == "__main__" ):

    app =  QApplication(sys.argv)
    ex = InfoWidget()
    sys.exit(app.exec_())
