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

from dials.command_line.refine_bravais_settings import phil_scope as phil_scope_refine_br_st

from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate

try:
    from dials.command_line.export import phil_scope as phil_scope_export
except:
    from dials.command_line.export_mtz import phil_scope as phil_scope_export

class ImportPage(QWidget):

    '''
    This stacked widget basically helps the user to browse the input images
    path and the working directory, there is no auto-generated code in use
    withing this widget and there is no multiple tabs like the other stacked
    widgets.
    '''

    # FIXME when the user enters a path without images dials fails to import
    # but does not raises an error consequently there is no red output in the GUI

    # FIXME study the file:
    # Dxtbx/sweep_filenames.py

    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent)
        #self.super_parent = parent # reference across the hole GUI to MyMainDialog

        #self.super_parent.w_dir = os.getcwd()
        self.w_dir = os.getcwd()

        self.cmd_lin_default = "dials.import ~/put/your/path/here"

        import_path_group =  QGroupBox("Experiment IMG Directory")
        import_path_layout =  QHBoxLayout()

        self.lin_import_path =   QLineEdit(self)
        import_path_layout.addWidget(self.lin_import_path)
        import_path_button =  QPushButton(" \n    Find experiment Dir            . \n")
        import_path_button.clicked.connect(self.find_my_img_dir)
        import_path_layout.addWidget(import_path_button)
        import_path_group.setLayout(import_path_layout)

        w_dir_group =  QGroupBox("Working Directory")
        w_dir_layout =  QHBoxLayout()
        self.w_dir_lin =   QLineEdit(self)
        self.w_dir_lin.setText("/some/w_diw/here")
        #self.w_dir_lin.setText(self.super_parent.w_dir)
        w_dir_layout.addWidget(self.w_dir_lin)
        w_dir_button =  QPushButton(" \n    Change Working Dir    . \n")
        w_dir_button.clicked.connect(self.change_w_dir)
        w_dir_layout.addWidget(w_dir_button)
        w_dir_group.setLayout(w_dir_layout)


        mainLayout =  QVBoxLayout()
        mainLayout.addWidget(import_path_group)
        mainLayout.addWidget(w_dir_group)

        idials_path = os.environ["IDIALS_PATH"]

        imageLabel =  QLabel()
        dials_logo_path = str(idials_path + "/resources/DIALS_Logo_smaller_centred.png")

        image =  QImage(dials_logo_path)
        imageLabel.setPixmap( QPixmap.fromImage(image))
        mainLayout.addWidget(imageLabel)
        #imageLabel.setScaledContents(True)


        big_layout =  QHBoxLayout()
        big_layout.addLayout(mainLayout)

        '''
        self.multi_line_txt = TextBrows()
        big_layout.addWidget(self.multi_line_txt)
        '''

        self.setLayout(big_layout)
        #self.show()


    def find_my_img_dir(self, event = None):
        selected_file_path = str( QFileDialog.getOpenFileName(self, "Open IMG Dir"))
        print "[file path found] =", selected_file_path

        if( selected_file_path ):
            for pos, single_char in enumerate(selected_file_path):
                if( single_char == "/" or single_char == "\\" ):
                    pos_sep = pos

            dir_name = selected_file_path[:pos_sep]
            if( dir_name[0:3] == "(u\'" ):
                print "dir_name[0:3] == \"(u\'\""
                dir_name = dir_name[3:]

            print "dir_name(final) =", dir_name
            self.lin_import_path.setText(dir_name)
            #self.cmd_lin_default = "dials.import "+ dir_name
            print "CLI =", self.cmd_lin_default

        else:
            print "Failed to pick dir"
            self.cmd_lin_default = " "

        #self.super_parent.gui_line_edit.set_text(self.cmd_lin_default)


    def change_w_dir(self, event = None):
        dir_name = str( QFileDialog.getExistingDirectory(self, "Change Working Dir"))
        print "[dir path found] =", dir_name

        if( dir_name ):
            old_way = '''
            self.super_parent.w_dir = dir_name
            os.chdir(self.super_parent.w_dir)
            self.w_dir_lin.setText(self.super_parent.w_dir)
            print "dir_name(w_dir) =", self.super_parent.w_dir
            '''

            self.w_dir = dir_name
            os.chdir(self.w_dir)
            self.w_dir_lin.setText(self.w_dir)
            print "dir_name(w_dir) =", self.w_dir

        else:
            print "Failed to pick dir"






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
                  #"                reindex",
                  "                 refine",
                  "              integrate"
                  #,"                 export"
                  ]

    lst_commands = [
                    "import",
                    "find_spots",
                    "index",
                    "refine_bravais_settings",
                    #"reindex",
                    "refine",
                    "integrate"
                    #,"export"
                   ]

    def __init__(self):
        self.lst_widg  = [
                          ImportPage(),
                          ParamMainWidget(phil_scope_find_spots),
                          ParamMainWidget(phil_scope_index),
                          ParamMainWidget(phil_scope_refine_br_st),
                          #imp_ops("                reindex"),
                          ParamMainWidget(phil_scope_refine),
                          ParamMainWidget(phil_scope_integrate)
                          #,ParamMainWidget(phil_scope_export)
                         ]

        idials_path = os.environ["IDIALS_PATH"]
        print "idials_path =", idials_path

        lst_icons_path = []

        lst_icons_path.append(str(idials_path + "/resources/import.png"))
        lst_icons_path.append(str(idials_path + "/resources/find_spots.png"))
        lst_icons_path.append(str(idials_path + "/resources/index.png"))
        #lst_icons_path.append(str(idials_path + "/resources/refine_v_sets.png"))
        lst_icons_path.append(str(idials_path + "/resources/reindex.png"))
        lst_icons_path.append(str(idials_path + "/resources/refine.png"))
        lst_icons_path.append(str(idials_path + "/resources/integrate.png"))
        #lst_icons_path.append(str(idials_path + "/resources/export.png"))

        self.lst_icons = []
        for my_icon_path in lst_icons_path:
            self.lst_icons.append(QIcon(my_icon_path))
            print "attempting to append:", my_icon_path

    def __call__(self):
        return self.lst_lablel, self.lst_widg, self.lst_icons, self.lst_commands
