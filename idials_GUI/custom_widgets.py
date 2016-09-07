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

#from import_mult_opt import ParamWidget as imp_ops
from find_spots_mult_opt import ParamMainWidget as fnd_ops
from index_mult_opt import ParamMainWidget as idx_ops
from refine_mult_opt import ParamMainWidget as ref_ops
from integrate_mult_opt import ParamMainWidget as int_ops
from idials_stacked_widgets import TableSelectWidget


class imp_ops(QWidget):
    def __init__(self):
        super(imp_ops, self).__init__()
        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(QLabel("               Import widget here"))
        self.setLayout(v_left_box)


class StepList(object):
    lst_lablel = [
                  "                 import",
                  "             find spots",
                  "                  index",
                  "refine bravais settings",
                  "                reindex",
                  "                 refine",
                  "              integrate",
                  "                 export"
                  ]

    lst_commands = [
                    "import",
                    "find_spots",
                    "index",
                    "refine_bravais_settings",
                    "reindex",
                    "refine",
                    "integrate",
                    "export"
                   ]

    def __init__(self):
        self.lst_widg  = [
                          imp_ops(),
                          fnd_ops(),
                          idx_ops(),
                          TableSelectWidget(),
                          idx_ops(),
                          ref_ops(),
                          int_ops(),
                          imp_ops()
                          ]

        idials_path = os.environ["IDIALS_PATH"]
        print "idials_path =", idials_path

        lst_icons_path = []

        lst_icons_path.append(str(idials_path + "/resources/import.png"))
        lst_icons_path.append(str(idials_path + "/resources/find_spots.png"))
        lst_icons_path.append(str(idials_path + "/resources/index.png"))
        lst_icons_path.append(str(idials_path + "/resources/refine_v_sets.png"))
        lst_icons_path.append(str(idials_path + "/resources/reindex.png"))
        lst_icons_path.append(str(idials_path + "/resources/refine.png"))
        lst_icons_path.append(str(idials_path + "/resources/integrate.png"))
        lst_icons_path.append(str(idials_path + "/resources/export.png"))

        self.lst_icons = []
        for my_icon_path in lst_icons_path:
            self.lst_icons.append(QIcon(my_icon_path))
            print "attempting to append:", my_icon_path

    def __call__(self):
        return self.lst_lablel, self.lst_widg, self.lst_icons, self.lst_commands
