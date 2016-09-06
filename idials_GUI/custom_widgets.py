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
import os

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
    lst_lablel = [
                  "import",
                  "find spots",
                  "index",
                  "refine \n bravais \n settings",
                  "reindex",
                  "refine",
                  "integrate"
                  ]
    lst_commands = [
                    "import",
                    "find_spots",
                    "index",
                    "refine_bravais_settings",
                    "reindex",
                    "refine",
                    "integrate"
                   ]
    line_to_add_in_the_future = '''
                    "export",
    '''
    def __init__(self):
        self.lst_widg  = [imp_ops(), fnd_ops(), idx_ops(), ref_ops(), idx_ops(), ref_ops(), int_ops()]

        #TODO make the path of this icons available project wise

        my_dui_path = os.environ["DUI_PATH"]
        print "my_dui_path =", my_dui_path
        #dials_logo_path = my_dui_path + "/../dui/resources/DIALS_Logo_icon_ish.png"


        self.lst_icons = [QIcon("resources/import.png"),
                          QIcon("resources/find_spots.png"),
                          QIcon("resources/index.png"),

                          QIcon("resources/refine_v_sets.png"),
                          QIcon("resources/reindex.png"),

                          QIcon("resources/refine.png"),
                          QIcon("resources/integrate.png")
                          ]
    def __call__(self):
        return self.lst_lablel, self.lst_widg, self.lst_icons, self.lst_commands
