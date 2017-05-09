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

from python_qt_bind import *

from dials.command_line.find_spots import phil_scope
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
            if( single_obj.is_definition ):
                self.lst_obj.append(single_obj)

            elif( single_obj.is_scope ):
                if( single_obj.name != "output" ):
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
    item_changed = pyqtSignal()
    def __init__(self, phl_obj, parent = None):   #TODO fix the order of this two parameters
        super(PhilWidget, self).__init__(parent)
        self.param_widget_parent = parent.param_widget_parent

        self.super_parent = parent.super_parent
        #self.super_parent = self.param_widget_parent.super_parent

        self.win_pal = QPalette()
        self.win_pal.setColor(QPalette.Window, QColor(125, 125, 125, 1))
        #self.win_pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(self.win_pal)

        #std_bkgr = self.palette().color(self.backgroundRole())

        self.plt_scp = QPalette()
        self.plt_scp.setColor(QPalette.WindowText, QColor(85, 85, 85, 255))
        #self.plt_scp.setColor(QPalette.Background, std_bkgr)

        self.plt_obj = QPalette()
        self.plt_obj.setColor(QPalette.WindowText, Qt.black)
        #self.plt_obj.setColor(QPalette.Background, std_bkgr)

        self.bg_box = QVBoxLayout(self)

        self.plt_fnd = QPalette()
        self.plt_fnd.setColor(QPalette.WindowText, QColor(0, 0, 255, 255))
        self.plt_fnd.setColor(QPalette.Background, QColor(255, 255, 0, 255))



        lst_obj = tree_2_lineal(phl_obj.objects)
        lst_phil_obj = lst_obj()

        self.phil_list2gui(lst_phil_obj)

        self.setLayout(self.bg_box)
        self.show()

    def user_searching(self, value):

        for nm, labl_obj in enumerate(self.lst_widg):
            labl_obj.setPalette(labl_obj.palette_orig)

        if( len(value) > 1 ):
            print "user searching for:", value
            pos_str = None
            print "len =", len(value)

            for nm, labl_obj in enumerate(self.lst_widg):
                labl_text = labl_obj.text()
                if( value in labl_text ):
                    labl_obj.setPalette(self.plt_fnd)
                    print "pos_str =", nm


    def phil_list2gui(self, lst_phil_obj):

        sys_font = QFont()
        sys_font_point_size =  sys_font.pointSize()
        print "sys_font_point_size =", sys_font_point_size

        if( self.super_parent.embedded_reindex ):
            inde_step = 7
        else:
            inde_step = 2

        #lst_widg = self.lst_phil_obj
        self.lst_widg = []
        something_else = False
        self.lst_wgs = []

        print "\n"

        for nm, obj in enumerate(lst_phil_obj):

            if( str(type(obj))[-11:-2] == "ScopeData"):
                tmp_str = " " * int(obj.indent * inde_step) + str(obj.name)
                print tmp_str
                tmp_widg = QLabel(tmp_str)
                tmp_widg.setAutoFillBackground(True)
                tmp_widg.setPalette(self.plt_scp)
                tmp_widg.setFont(QFont("Monospace", sys_font_point_size, QFont.Bold))
                self.bg_box.addWidget(tmp_widg)
                tmp_widg.palette_orig = self.plt_scp

                self.lst_widg.append(tmp_widg)

            else:
                multiple_index = False

                if(obj.type.phil_type == 'float' or
                   obj.type.phil_type == 'int'   or
                   obj.type.phil_type == 'str'   or
                   obj.type.phil_type == 'bool'  or
                   obj.type.phil_type == 'choice' ):

                    tmp_h_box = QHBoxLayout()

                    indent = str(obj.full_path()).count('.')
                    tmp_str = " " * indent * inde_step + str(obj.name)
                    tmp_label  = QLabel(tmp_str)
                    tmp_label.setAutoFillBackground(True)
                    tmp_label.setPalette(self.plt_obj)
                    tmp_label.setFont(QFont("Monospace", sys_font_point_size))

                    tmp_h_box.addWidget(tmp_label)
                    tmp_label.palette_orig = self.plt_obj
                    self.lst_widg.append(tmp_label)

                    something_else = False
                    if(obj.type.phil_type == 'float' or
                       obj.type.phil_type == 'int'   or
                       obj.type.phil_type == 'str'     ):

                        if( obj.type.phil_type == 'float' ):
                            tmp_widg = QDoubleSpinBox()

                        elif( obj.type.phil_type == 'int' ):
                            tmp_widg = QSpinBox()

                        elif( obj.type.phil_type == 'str' ):
                            tmp_widg = QLineEdit()

                        if( obj.type.phil_type == 'int' or obj.type.phil_type == 'float'  ):

                            if( str(obj.extract()) == 'Auto' or str(obj.extract()) == 'None'):
                                #TODO fix the libtbx.AutoType in double Phil parameter"
                                tmp_str = None

                            else:
                                tmp_widg.setValue(obj.extract())
                                tmp_str += "                          " + str(obj.extract())


                        tmp_widg.local_path = str(obj.full_path())
                        tmp_widg.tmp_lst = None

                        if( obj.type.phil_type == 'int' or obj.type.phil_type == 'float' ):
                            tmp_widg.valueChanged.connect(self.spnbox_changed)
                        else:
                            tmp_widg.textChanged.connect(self.spnbox_changed)

                    elif( obj.type.phil_type == 'bool' ):

                        tmp_widg = QComboBox()

                        tmp_widg.local_path = str(obj.full_path())
                        tmp_widg.tmp_lst=[]
                        tmp_widg.tmp_lst.append("True")
                        tmp_widg.tmp_lst.append("False")

                        for lst_itm in tmp_widg.tmp_lst:
                            tmp_widg.addItem(lst_itm)

                        if( str(obj.extract()) == "False" ):
                            tmp_widg.setCurrentIndex(1)
                            tmp_str += "                          False"

                        else:
                            tmp_str += "                          True"

                        tmp_widg.currentIndexChanged.connect(self.combobox_changed)

                    elif( obj.type.phil_type == 'choice' ):

                        tmp_widg = QComboBox()
                        tmp_widg.local_path = str(obj.full_path())
                        tmp_widg.tmp_lst=[]
                        pos = 0
                        for num, opt in enumerate(obj.words):
                            opt = str(opt)
                            if( opt[0] == "*" ):
                                opt = opt[1:]
                                pos = num
                                tmp_str += "                          " + opt

                            tmp_widg.tmp_lst.append(opt)

                        for lst_itm in tmp_widg.tmp_lst:
                            tmp_widg.addItem(lst_itm)

                        tmp_widg.setCurrentIndex(pos)
                        tmp_widg.currentIndexChanged.connect(self.combobox_changed)


                    tmp_disabled = '''

                elif( obj.type.phil_type == 'ints' or obj.type.phil_type == 'floats' ):

                    if( obj.type.size_min >= 2 and obj.type.size_max <= 6 and
                        obj.type.size_max == obj.type.size_min and obj.type.size_max != None ):
                        tmp_h_box_lst = []
                        tmp_label_lst = []
                        multi_widg_lst = []
                        indent = str(obj.full_path()).count('.')

                        for indx in range(obj.type.size_max):

                            new_labl = QLabel(" " * indent * inde_step + str(obj.name)
                                              + "[" + str(indx + 1) + "]")

                            new_labl.setPalette(self.plt_obj)
                            new_labl.setFont(QFont("Monospace", sys_font_point_size))
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
                    '''

                else:
                    debugging = '''
                    print
                    print "_____________________ << WARNING find something ELSE"
                    print "_____________________ << full_path =", obj.full_path()
                    print "_____________________ << obj.type.phil_type =", obj.type.phil_type
                    print "_____________________ << obj.type =", obj.type
                    print
                    '''
                    something_else = True

                if( something_else == False ):
                    if(multiple_index == False):
                        if(tmp_str != None):
                            tmp_h_box.addWidget(tmp_widg)
                            self.bg_box.addLayout(tmp_h_box)
                            self.lst_wgs.append(tmp_widg)
                            print tmp_str

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
        self.param_widget_parent.update_lin_txt(str_path, str_value)


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.param_widget_parent.update_lin_txt(str_path, str_value)


class TstTmpWidget( QWidget):

    item_changed = pyqtSignal() #TODO check if this line is needed

    def __init__(self, phl_obj = None, parent = None):
        super(TstTmpWidget, self).__init__(parent)
        self.param_widget_parent = self
        self.super_parent = self
        self.embedded_reindex = False
        inner_widget = PhilWidget(phl_obj, self) #TODO fix the order of this two parameters


        my_box = QVBoxLayout()
        my_box.addWidget(inner_widget)
        self.setLayout(my_box)
        self.show()

    def update_lin_txt(self, new_path, new_value):
        print "new_path =", new_path
        print "new_value =", new_value
        print "from update_lin_txt(self)"


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = TstTmpWidget(phil_scope)
    sys.exit(app.exec_())




