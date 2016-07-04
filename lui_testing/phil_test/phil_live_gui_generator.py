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


qt_tool = "PyQt4"

#self.src_code_1 = []
import sys

if( qt_tool == "PyQt4" ):
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    print "using PyQt4"

else:
    from PySide.QtGui import *
    from PySide.QtCore import *
    pyqtSignal = Signal
    print "using PySide"




class ScopeData(object):
    '''
    class conceived to store only data related to the scope Phil object
    '''
    pass

class tree_2_lineal(object):

    '''
    Recursively navigates the Phil objects in a way that the final
    self.lst_obj is a lineal list without ramifications, this final list
    will be used by phil_list_2_disc() to generate runnable code
    '''

    def __init__(self, phl_obj):
        self.lst_obj = []
        self.deep_in_rec(phl_obj)

    def __call__(self):
        return self.lst_obj

    def deep_in_rec(self, phl_obj):

        for single_obj in phl_obj:
            if( single_obj.is_definition):
                self.lst_obj.append(single_obj)

            elif( single_obj.is_scope ):
                #print "scope.name = ", single_obj.name
                scope_info = ScopeData()
                scope_info.name = str(single_obj.name)
                scope_info.f_path = str(single_obj.full_path())

                #print "scope_info.f_path =", scope_info.f_path
                scope_info.indent = scope_info.f_path.count('.')
                #print "scope_info.f_path.count('.') =", scope_info.indent

                self.lst_obj.append(scope_info)
                self.deep_in_rec(single_obj.objects)

            else:
                print "\n\n _____________ <<< WARNING neither definition or scope\n\n"


class inner_widg( QWidget):
    item_changed = pyqtSignal()
    def __init__(self, lst_obj, qt_tool = "PyQt4", parent = None):
        super(inner_widg, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.plt_scp = QPalette()
        self.plt_scp.setColor(QPalette.Foreground, QColor(85, 85, 85, 255))
        self.plt_obj = QPalette()
        self.plt_obj.setColor(QPalette.Foreground,Qt.black)
        self.bg_box = QVBoxLayout(self)

        self.phil_list2gui(lst_obj, qt_tool)

        self.setLayout(self.bg_box)
        self.show()

        print "Done 02"


    def phil_list2gui(self, lst_obj, qt_tool):

        lst_widg = lst_obj
        for nm, obj in enumerate(lst_obj):

            if( str(type(obj)) == "<class '__main__.ScopeData'>" ):
                lst_widg[nm] = QLabel(" " * int(obj.indent * 4) + str(obj.name))
                lst_widg[nm].setPalette(self.plt_scp)
                lst_widg[nm].setFont(QFont("Monospace", 10, QFont.Bold))
                self.bg_box.addWidget(lst_widg[nm])





            else:
                multiple_index = False
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
                            #tmp_h_box_str = "hbox_lay_" + str(obj.name) + "_" + str(nm) + "_" + str(indx)
                            tmp_h_box_lst.append(QHBoxLayout())

                            tmp_label_lst.append(QLabel(" " * indent * 4 + str(obj.name) + "[" + str(indx + 1) + "]"))
                            tmp_label_lst[indx].setPalette(self.plt_obj)
                            tmp_label_lst[indx].setFont(QFont("Monospace", 10))

                            tmp_h_box_lst[indx].addWidget(tmp_label_lst[indx])

                            if(obj.type.phil_type == 'ints'):
                                new_widg = QSpinBox()

                            elif( obj.type.phil_type == 'floats' ):
                                new_widg = QDoubleSpinBox()

                            multi_widg_lst.append(new_widg)
                            multi_widg_lst[indx].local_path = str(obj.full_path())
                            multi_widg_lst[indx].valueChanged.connect(self.spnbox_changed)

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
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = False)
        self.super_parent.update_lin_txt(sender.local_path, value)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = False)

class ParamMainWidget( QWidget):
    def __init__(self, lst_obj, qt_tool = "PyQt4", parent = None):
        super(ParamMainWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.scrollable_widget = inner_widg( lst_obj, qt_tool, parent = self.super_parent)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        hbox =  QHBoxLayout()
        hbox.addWidget(scrollArea)
        self.setLayout(hbox)
        self.setWindowTitle('Phil dialog')
        self.show()

    def to_be_caled_from_son_widg(self):
        print "from parent parent_widget"

if __name__ == '__main__':

    '''
    from python_qt_bind import GuiBinding
    gui_lib = GuiBinding()
    print "using ", gui_lib.pyhon_binding
    qt_tool = gui_lib.pyhon_binding
    '''
    #TODO uncomment previous code and make it work
    qt_tool = "PyQt4"



    lst_phl_obj = []

    from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
    lst_phl_obj.append(phil_scope_find_spots)
    from dials.command_line.index import phil_scope as phil_scope_index
    lst_phl_obj.append(phil_scope_index)
    from dials.command_line.refine import phil_scope as phil_scope_refine
    lst_phl_obj.append(phil_scope_refine)
    from dials.command_line.integrate import phil_scope as phil_scope_integrate
    lst_phl_obj.append(phil_scope_integrate)

    try:
        from dials.command_line.export import phil_scope as phil_scope_export
    except:
        from dials.command_line.export_mtz import phil_scope as phil_scope_export

    lst_phl_obj.append(phil_scope_export)



    lst_pos = 0

    lst_phl_obj[lst_pos]= tree_2_lineal(lst_phl_obj[lst_pos].objects)

    app =  QApplication(sys.argv)
    ex = ParamMainWidget(lst_phl_obj[lst_pos](), qt_tool)
    sys.exit(app.exec_())




