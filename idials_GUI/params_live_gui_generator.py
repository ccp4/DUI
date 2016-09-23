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

from python_qt_bind import GuiBinding
if GuiBinding.pyhon_binding == "PyQt4":
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    print "   <<<   using PyQt4"

else:
    #asuming GuiBinding.pyhon_binding == "PySide"
    from PySide.QtGui import *
    from PySide.QtCore import *
    print "using PySide"
    pyqtSignal = Signal


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
            if( single_obj.is_definition ):
                self.lst_obj.append(single_obj)

            elif( single_obj.is_scope ):
                #print "scope.name = ", single_obj.name
                scope_info = ScopeData()
                scope_info.name = str(single_obj.name)
                scope_info.f_path = str(single_obj.full_path())
                scope_info.soy_scope = True

                #print "scope_info.f_path =", scope_info.f_path
                scope_info.indent = scope_info.f_path.count('.')
                #print "scope_info.f_path.count('.') =", scope_info.indent

                self.lst_obj.append(scope_info)
                self.deep_in_rec(single_obj.objects)

            else:
                print "\n\n _____________ <<< WARNING neither definition or scope\n\n"


class PhilWidget( QWidget):
    item_changed = pyqtSignal()
    def __init__(self, phl_obj, parent = None):
        super(PhilWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.plt_scp = QPalette()
        self.plt_scp.setColor(QPalette.Foreground, QColor(85, 85, 85, 255))
        self.plt_obj = QPalette()
        self.plt_obj.setColor(QPalette.Foreground,Qt.black)
        self.bg_box = QVBoxLayout(self)

        lst_obj = tree_2_lineal(phl_obj.objects)
        multipl_phil_lst = lst_obj()

        self.phil_list2gui(multipl_phil_lst)

        self.setLayout(self.bg_box)
        self.show()


    def phil_list2gui(self, lst_obj):

        lst_widg = lst_obj

        for nm, obj in enumerate(lst_obj):

            if( str(type(obj))[-11:-2] == "ScopeData"):
                lst_widg[nm] = QLabel(" " * int(obj.indent * 4) + str(obj.name))
                lst_widg[nm].setPalette(self.plt_scp)
                lst_widg[nm].setFont(QFont("Monospace", 10, QFont.Bold))
                self.bg_box.addWidget(lst_widg[nm])

            else:
                multiple_index = False

                #print "dir(obj) =", dir(obj)

                if(obj.type.phil_type == 'float' or
                   obj.type.phil_type == 'int'   or
                   obj.type.phil_type == 'str'   or
                   obj.type.phil_type == 'bool'  or
                   obj.type.phil_type == 'choice' ):

                    tmp_h_box = QHBoxLayout()

                    indent = str(obj.full_path()).count('.')
                    tmp_label  = QLabel(" " * indent * 4 + str(obj.name))
                    tmp_label.setPalette(self.plt_obj)
                    tmp_label.setFont(QFont("Monospace", 10))

                    tmp_h_box.addWidget(tmp_label)

                    something_else = False
                    if(obj.type.phil_type == 'float' or
                       obj.type.phil_type == 'int'   or
                       obj.type.phil_type == 'str'     ):

                        if( obj.type.phil_type == 'float' ):
                            lst_widg[nm] = QDoubleSpinBox()

                        elif( obj.type.phil_type == 'int' ):
                            lst_widg[nm] = QSpinBox()

                        elif( obj.type.phil_type == 'str' ):
                            lst_widg[nm] = QLineEdit()

                        if( obj.type.phil_type == 'int' or obj.type.phil_type == 'float'  ):

                            if( str(obj.extract()) == 'Auto' or str(obj.extract()) == 'None'):
                                print "TODO fix the libtbx.AutoType in double Phil parameter"

                            else:
                                lst_widg[nm].setValue(obj.extract())

                        lst_widg[nm].local_path = str(obj.full_path())

                        if( obj.type.phil_type == 'int' or obj.type.phil_type == 'float' ):
                            lst_widg[nm].valueChanged.connect(self.spnbox_changed)
                        else:
                            lst_widg[nm].textChanged.connect(self.spnbox_changed)

                    elif( obj.type.phil_type == 'bool' ):

                        lst_widg[nm] = QComboBox()

                        lst_widg[nm].local_path = str(obj.full_path())
                        lst_widg[nm].tmp_lst=[]
                        lst_widg[nm].tmp_lst.append("True")
                        lst_widg[nm].tmp_lst.append("False")

                        for lst_itm in lst_widg[nm].tmp_lst:
                            lst_widg[nm].addItem(lst_itm)

                        if( str(obj.extract()) == "False" ):
                            lst_widg[nm].setCurrentIndex(1)

                        lst_widg[nm].currentIndexChanged.connect(self.combobox_changed)

                    elif( obj.type.phil_type == 'choice' ):

                        lst_widg[nm] = QComboBox()
                        lst_widg[nm].local_path = str(obj.full_path())
                        lst_widg[nm].tmp_lst=[]
                        pos = 0
                        for num, opt in enumerate(obj.words):
                            opt = str(opt)
                            if( opt[0] == "*" ):
                                opt = opt[1:]
                                pos = num

                            lst_widg[nm].tmp_lst.append(opt)

                        for lst_itm in lst_widg[nm].tmp_lst:
                            lst_widg[nm].addItem(lst_itm)

                        lst_widg[nm].setCurrentIndex(pos)
                        lst_widg[nm].currentIndexChanged.connect(self.combobox_changed)

                elif( obj.type.phil_type == 'ints' or obj.type.phil_type == 'floats' ):

                    if( obj.type.size_min >= 2 and obj.type.size_max <= 6 and
                        obj.type.size_max == obj.type.size_min and obj.type.size_max != None ):
                        tmp_h_box_lst = []
                        tmp_label_lst = []
                        multi_widg_lst = []
                        indent = str(obj.full_path()).count('.')

                        for indx in range(obj.type.size_max):

                            new_labl = QLabel(" " * indent * 4 + str(obj.name)
                                              + "[" + str(indx + 1) + "]")

                            new_labl.setPalette(self.plt_obj)
                            new_labl.setFont(QFont("Monospace", 10))
                            tmp_label_lst.append(new_labl)


                            new_hbox = QHBoxLayout()
                            new_hbox.addWidget(tmp_label_lst[indx])
                            tmp_h_box_lst.append(new_hbox)

                            if(obj.type.phil_type == 'ints'):
                                new_widg = QSpinBox()

                            elif( obj.type.phil_type == 'floats' ):
                                new_widg = QDoubleSpinBox()

                            new_widg.local_path = str(obj.full_path())
                            new_widg.valueChanged.connect(self.spnbox_changed)
                            multi_widg_lst.append(new_widg)

                        multiple_index = True

                    else:
                        something_else = True

                else:

                    print
                    print "_____________________ << WARNING find something ELSE"
                    print "_____________________ << full_path =", obj.full_path()
                    print "_____________________ << obj.type.phil_type =", obj.type.phil_type
                    print "_____________________ << obj.type =", obj.type
                    print
                    something_else = True

                if( something_else == False ):
                    if(multiple_index == False):
                        tmp_h_box.addWidget(lst_widg[nm])
                        self.bg_box.addLayout(tmp_h_box)

                    else:
                        for indx in range(obj.type.size_max):
                            tmp_h_box_lst[indx].addWidget(multi_widg_lst[indx])
                            self.bg_box.addLayout(tmp_h_box_lst[indx])

    def spnbox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "spnbox_changed to:",
        str_value = str(value)
        print value
        print "local_path =",
        str_path = str(sender.local_path)
        print "local_path =", str_path

        self.super_parent.update_lin_txt(str_path, str_value)
        #self.super_parent.update_lin_txt(sender.local_path, value)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value)

