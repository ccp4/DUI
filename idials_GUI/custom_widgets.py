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
#from import_mult_opt import ParamWidget as imp_ops

class imp_ops(QWidget):
    def __init__(self):
        super(imp_ops, self).__init__()
        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(QLabel("               Import widget here"))
        self.setLayout(v_left_box)


class StepList(object):
    lst_lablel = ["import", "find_spots", "index", "refine", "integrate",]

    def __init__(self):
        self.lst_widg  = [imp_ops(), fnd_ops(), idx_ops(), ref_ops(), int_ops(),]
        self.lst_icons = [QIcon("resources/import.png"),
                          QIcon("resources/find_spots.png"),
                          QIcon("resources/index.png"),
                          QIcon("resources/refine.png"),
                          QIcon("resources/integrate.png"),
                          ]
    def __call__(self):
        return self.lst_lablel, self.lst_widg, self.lst_icons
