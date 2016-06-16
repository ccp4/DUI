import sys

#PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''

PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "using PySide"
#'''
from find_spots_mult_opt import ParamMainWidget as fnd_ops
from index_mult_opt import ParamMainWidget as idx_ops
from refine_mult_opt import ParamMainWidget as ref_ops
from integrate_mult_opt import ParamMainWidget as int_ops

class StepList(object):
    lst_lablel = [
            "import",
            "find_spots",
            "index",
            "refine",
            "integrate",
            ]

    def __init__(self):
        self.lst_widg  = [
              None,
              fnd_ops(),
              idx_ops(),
              ref_ops(),
              int_ops(),
              ]

    def __call__(self):
        return self.lst_lablel, self.lst_widg


class ParamWidget(QWidget):
    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(QLabel(label_str))

        self.setLayout(v_left_box)

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()

        v_left_box =  QVBoxLayout()
        self.step_param_widg =  QStackedWidget()
        my_lst = StepList()
        label_lst, widg_lst = my_lst()
        for pos, step_data in enumerate(label_lst):
            new_btn = QPushButton(step_data, self)
            if( widg_lst[pos] == None ):
                new_btn.par_wig = ParamWidget(step_data)
            else:
                new_btn.par_wig = widg_lst[pos]

            new_btn.clicked.connect(self.btn_clicked)
            v_left_box.addWidget(new_btn)

            self.step_param_widg.addWidget(new_btn.par_wig)

        multi_step_hbox = QHBoxLayout()
        multi_step_hbox.addLayout(v_left_box)
        multi_step_hbox.addWidget(self.step_param_widg)

        self.setLayout(multi_step_hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def btn_clicked(self):
        my_sender = self.sender()
        self.step_param_widg.setCurrentWidget(my_sender.par_wig)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

