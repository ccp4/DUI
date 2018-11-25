'''
DUI's code generator from phil parameters

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


# FIXME Copied from dials.index.py. This is needed here because scipy needs to
# be imported before cctbx otherwise there will be a segmentation fault. This
# should be fixed in dials.index so that we don't need to import here.

try:
  # try importing scipy.linalg before any cctbx modules, otherwise we
  # sometimes get a segmentation fault/core dump if it is imported after
  # scipy.linalg is a dependency of sklearn.cluster.DBSCAN
  import scipy.linalg # import dependency

except ImportError, e:
  pass


from PyQt4.QtGui import *
from PyQt4.QtCore import *

from dials.command_line.find_spots import phil_scope
#from dials.command_line.refine_bravais_settings import phil_scope

import sys

class ScopeData(object):
    '''
    class conceived to store only data related to the scope Phil object
    '''
    pass


class tree_2_lineal(object):

    '''
    Recursively navigates the Phil objects in a way that the final
    self.lst_obj is a lineal list without ramifications, this final list
    will be used later to generate a dynamic GUI
    '''

    def __init__(self, phl_obj):
        self.lst_obj = []
        self.deep_in_rec(phl_obj)

    def __call__(self):
        return self.lst_obj

    def deep_in_rec(self, phl_obj):

        for single_obj in phl_obj:
            if(single_obj.is_definition):
                self.lst_obj.append(single_obj)

            elif(single_obj.is_scope):
                if(single_obj.name != "output"):
                    scope_info = ScopeData()
                    scope_info.name = str(single_obj.name)
                    scope_info.f_path = str(single_obj.full_path())
                    scope_info.i_m_scope = True

                    #print "scope_info.f_path =", scope_info.f_path
                    scope_info.indent = scope_info.f_path.count('.')
                    #print "scope_info.f_path.count('.') =", scope_info.indent

                    self.lst_obj.append(scope_info)
                    self.deep_in_rec(single_obj.objects)

                else:
                    print "The \"", single_obj.name, "\" set of parameters is automatically handled by idials"
                    #pass

            else:
                print "\n _____________ <<< WARNING neither definition or scope\n"
                #pass


class PhilWidget( QWidget):
    item_changed = pyqtSignal(str, str)
    def __init__(self, phl_obj, parent = None):   #TODO fix the order of this two parameters
        super(PhilWidget, self).__init__(parent)
        #self.param_widget_parent = parent.param_widget_parent

        #self.win_pal = QPalette()
        #self.win_pal.setColor(QPalette.Window, QColor(125, 125, 125, 1))
        ##self.win_pal.setColor(QPalette.Background, Qt.white)
        #self.setAutoFillBackground(True)
        #self.setPalette(self.win_pal)
        #
        ##std_bkgr = self.palette().color(self.backgroundRole())
        #
        #self.plt_scp = QPalette()
        #self.plt_scp.setColor(QPalette.WindowText, QColor(85, 85, 85, 255))
        ##self.plt_scp.setColor(QPalette.Background, std_bkgr)
        #
        #self.plt_obj = QPalette()
        #self.plt_obj.setColor(QPalette.WindowText, Qt.black)
        ##self.plt_obj.setColor(QPalette.Background, std_bkgr)
        #
        #
        #self.plt_fnd = QPalette()
        #self.plt_fnd.setColor(QPalette.WindowText, QColor(0, 0, 255, 255))
        #self.plt_fnd.setColor(QPalette.Background, QColor(255, 255, 0, 255))

        self.bg_box = QVBoxLayout(self)


        lst_obj = tree_2_lineal(phl_obj.objects)
        lst_phil_obj = lst_obj()

        self.phil_list2gui(lst_phil_obj)

        self.setLayout(self.bg_box)
        self.show()

    def user_searching(self, value):

        for nm, labl_obj in enumerate(self.lst_label_widg):
            #labl_obj.setPalette(labl_obj.style_orign)
            labl_obj.setStyleSheet(labl_obj.style_orign)

        if(len(value) > 1):
            print "user searching for:", value
            pos_str = None
            print "len =", len(value)

            for nm, labl_obj in enumerate(self.lst_label_widg):
                labl_text = labl_obj.text()
                if(value in labl_text):
                    #labl_obj.setPalette(self.plt_fnd)
                    labl_obj.setStyleSheet("color: rgba(0, 155, 255, 255);"
                                           "background-color: yellow;")

                    print "pos_str =", nm

            #TODO make sure this keeps colours of grayed state


    def phil_list2gui(self, lst_phil_obj):

        sys_font = QFont()
        sys_font_point_size =  sys_font.pointSize()

        inde_step = 4

        self.lst_label_widg = []
        self.lst_var_widg = []

        non_added_lst = []

        for nm, obj in enumerate(lst_phil_obj):

            if(str(type(obj))[-11:-2] == "ScopeData"):
                tmp_str = " " * int(obj.indent * inde_step) + str(obj.name)
                #print tmp_str
                tmp_widg = QLabel(tmp_str)
                tmp_widg.setAutoFillBackground(True)
                #tmp_widg.setPalette(self.plt_scp)
                tmp_widg.setFont(QFont("Monospace", sys_font_point_size, QFont.Bold))
                tmp_widg.style_orign = "color: rgba(85, 85, 85, 255)"
                tmp_widg.setStyleSheet(tmp_widg.style_orign)

                self.bg_box.addWidget(tmp_widg)

                tmp_widg.test_flag = "Yes"

                self.lst_label_widg.append(tmp_widg)

            else:

                tmp_h_box = QHBoxLayout()

                indent = str(obj.full_path()).count('.')
                tmp_str = " " * indent * inde_step + str(obj.name)
                tmp_label  = QLabel(tmp_str)
                tmp_label.setAutoFillBackground(True)
                #tmp_label.setPalette(self.plt_obj)
                tmp_label.style_orign = "color: rgba(0, 0, 0, 255)"
                tmp_label.setStyleSheet(tmp_label.style_orign)
                tmp_label.setFont(QFont("Monospace", sys_font_point_size))

                tmp_h_box.addWidget(tmp_label)

                self.lst_label_widg.append(tmp_label)

                if(obj.type.phil_type == 'float'  or
                   obj.type.phil_type == 'int'    or
                   obj.type.phil_type == 'bool'   or
                   obj.type.phil_type == 'choice'):


                    if(obj.type.phil_type == 'float' or
                       obj.type.phil_type == 'int' ):

                        if(obj.type.phil_type == 'float'):
                            par_min = 0.0
                            par_max = 5000.0
                            tmp_widg = QDoubleSpinBox()
                            tmp_widg.setDecimals(3)

                        elif(obj.type.phil_type == 'int'):
                            par_min = 0
                            par_max = 5000
                            tmp_widg = QSpinBox()

                        if(obj.type.phil_type == 'int' or obj.type.phil_type == 'float'):
                            tmp_widg.str_defl = None
                            tmp_widg.setRange(par_min, par_max)
                            if(str(obj.extract()) == 'Auto' or str(obj.extract()) == 'None'):
                                par_def = str(obj.extract())
                                tmp_widg.setSpecialValueText(par_def)
                                tmp_widg.str_defl = par_def

                            else:
                                par_def = obj.extract()
                                if(float(par_def) != 0.0 and obj.type.phil_type == 'float' ):
                                    par_max = abs(par_def * 100.0)
                                    tmp_widg.setSingleStep(abs(par_def /10))

                                tmp_widg.setValue(par_def)

                            tmp_str += "                          " + str(obj.extract())

                        tmp_widg.tmp_lst = None

                        if(obj.type.phil_type == 'int' or obj.type.phil_type == 'float'):
                            tmp_widg.valueChanged.connect(self.spnbox_changed)

                        else:
                            tmp_widg.textChanged.connect(self.spnbox_changed)

                    elif(obj.type.phil_type == 'bool'):

                        tmp_widg = QComboBox()

                        tmp_widg.tmp_lst=[]
                        tmp_widg.tmp_lst.append("True")
                        tmp_widg.tmp_lst.append("False")

                        for lst_itm in tmp_widg.tmp_lst:
                            tmp_widg.addItem(lst_itm)

                        if(str(obj.extract()) == "False"):
                            tmp_widg.setCurrentIndex(1)
                            tmp_str += "                          False"

                        elif(str(obj.extract()) == "True"):
                            tmp_str += "                          True"

                        else:
                            tmp_str = None

                        tmp_widg.currentIndexChanged.connect(self.combobox_changed)

                    elif(obj.type.phil_type == 'choice'):
                        #remember to ask david about the issue here
                        before_patch = '''
                        tmp_widg = QComboBox()

                        tmp_widg.tmp_lst=[]
                        pos = 0
                        found_choise = False
                        for num, opt in enumerate(obj.words):
                            opt = str(opt)
                            if(opt[0] == "*"):
                                found_choise = True
                                opt = opt[1:]
                                pos = num
                                tmp_str += "                          " + opt

                            tmp_widg.tmp_lst.append(opt)

                        for lst_itm in tmp_widg.tmp_lst:
                            tmp_widg.addItem(lst_itm)

                        tmp_widg.setCurrentIndex(pos)
                        tmp_widg.currentIndexChanged.connect(self.combobox_changed)

                        if(found_choise == False):
                            tmp_str = None
                            non_added_lst.append(str(obj.full_path()))
                        '''
                        # begins pathed version
                        tmp_widg = QComboBox()

                        tmp_widg.tmp_lst=[]
                        pos = 0
                        found_choise = False
                        for num, opt in enumerate(obj.words):
                            opt = str(opt)
                            if(opt[0] == "*"):
                                found_choise = True
                                opt = opt[1:]
                                pos = num
                                tmp_str += "                          " + opt

                            tmp_widg.tmp_lst.append(opt)

                        if(found_choise == False):
                            tmp_str += "                          " + str(obj.extract())

                        for lst_itm in tmp_widg.tmp_lst:
                            tmp_widg.addItem(lst_itm)

                        tmp_widg.setCurrentIndex(pos)
                        tmp_widg.currentIndexChanged.connect(self.combobox_changed)

                        # ends pathed version

                else:
                    tmp_widg = QLineEdit()
                    tmp_widg.setText("")
                    tmp_widg.str_defl = None
                    tmp_widg.textChanged.connect(self.spnbox_changed)
                    #tmp_widg.tmp_lst = None
                    tmp_str += "                          " + str(obj.extract())

                if(tmp_str != None):
                    tmp_widg.local_path = str(obj.full_path())
                    #tmp_h_box.addStretch()
                    tmp_h_box.addWidget(tmp_widg)
                    self.lst_var_widg.append(tmp_widg)
                    self.bg_box.addLayout(tmp_h_box)


        #debugging = '''
        print "\n\n Non added parameters:"
        for lin_to_print in non_added_lst:
            print lin_to_print

        print "\n\n"
        #'''

    def spnbox_changed(self, value):
        sender = self.sender()
        if(sender.str_defl != None and float(value) == 0.0):
            str_value = sender.str_defl

        else:
            str_value = str(value)

        print "sender =", sender
        print "spnbox_changed to:",
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print "local_path =", str_path

        #self.param_widget_parent.update_lin_txt(str_path, str_value)
        self.item_changed.emit(str_path, str_value)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path

        #self.param_widget_parent.update_lin_txt(str_path, str_value)
        self.item_changed.emit(str_path, str_value)


class TstTmpWidget( QWidget):
    def __init__(self, phl_obj = None, parent = None):
        super(TstTmpWidget, self).__init__(parent)
        #self.param_widget_parent = self
        inner_widget = PhilWidget(phl_obj, self) #TODO fix the order of this two parameters
        inner_widget.item_changed.connect(self.update_lin_txt)

        my_box = QVBoxLayout()
        my_box.addWidget(inner_widget)
        self.setLayout(my_box)
        self.show()

    def update_lin_txt(self, new_path, new_value):
        print "new_path =", new_path
        print "new_value =", new_value
        print "from update_lin_txt(self) in TstTmpWidget"


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = TstTmpWidget(phil_scope)
    sys.exit(app.exec_())

