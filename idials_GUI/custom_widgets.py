from python_qt_bind import GuiBinding

if GuiBinding.pyhon_binding == "PyQt4":
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    print "   <<<   using PyQt4"

else:
    from PySide.QtGui import *
    from PySide.QtCore import *
    print " <<< using PySide"

import os

from params_live_gui_generator import PhilWidget
from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index
from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate

try:
    from dials.command_line.export import phil_scope as phil_scope_export
except:
    from dials.command_line.export_mtz import phil_scope as phil_scope_export


class imp_ops(QWidget):
    def __init__(self, str_label = None):
        super(imp_ops, self).__init__()
        v_left_box =  QVBoxLayout()
        if( str_label == None ):
            str_label = "               Import widget here"

        v_left_box.addWidget(QLabel(str_label))
        self.setLayout(v_left_box)
        #self.show()

class ParamMainWidget( QWidget):
    def __init__(self, phl_obj):
        super(ParamMainWidget, self).__init__()
        #self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.scrollable_widget = PhilWidget(phl_obj, parent = self)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        hbox =  QHBoxLayout()
        hbox.addWidget(scrollArea)
        self.setLayout(hbox)
        self.show()

    def update_lin_txt(self, str_path, str_value):
        print "running {", str_path, "=", str_value,"}"


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
                          imp_ops("                 import"),
                          ParamMainWidget(phil_scope_find_spots),
                          ParamMainWidget(phil_scope_index),
                          imp_ops("refine bravais settings"),
                          imp_ops("                reindex"),
                          ParamMainWidget(phil_scope_refine),
                          ParamMainWidget(phil_scope_integrate),
                          ParamMainWidget(phil_scope_export)
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
