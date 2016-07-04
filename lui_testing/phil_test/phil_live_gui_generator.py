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
    def __init__(self, parent = None):
        super(inner_widg, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        palette_scope = QPalette()
        palette_scope.setColor(QPalette.Foreground, QColor(85, 85, 85, 255))
        palette_object = QPalette()
        palette_object.setColor(QPalette.Foreground,Qt.black)
        bg_box =  QVBoxLayout(self)


        self.setLayout(bg_box)
        self.show()

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
    def __init__(self, parent = None):
        super(ParamMainWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.scrollable_widget = inner_widg(self.super_parent)
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
    #TODO uncomment previous code
    qt_tool = "PyQt4"



    lst_phl_obj = []

    from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
    lst_phl_obj.append([phil_scope_find_spots, "find_spots_mult_opt"])
    tmp_off = '''
    from dials.command_line.index import phil_scope as phil_scope_index
    lst_phl_obj.append([phil_scope_index, "index_mult_opt"])
    from dials.command_line.refine import phil_scope as phil_scope_refine
    lst_phl_obj.append([phil_scope_refine, "refine_mult_opt"])
    from dials.command_line.integrate import phil_scope as phil_scope_integrate
    lst_phl_obj.append([phil_scope_integrate, "integrate_mult_opt"])

    try:
        from dials.command_line.export import phil_scope as phil_scope_export
    except:
        from dials.command_line.export_mtz import phil_scope as phil_scope_export

    lst_phl_obj.append([phil_scope_export, "export_mult_opt"])
    '''


    for phl_obj in lst_phl_obj:
        lst_obj = tree_2_lineal(phl_obj[0].objects)
        '''
        phil_list_2_disc(lst_obj(), phl_obj[1], qt_tool)
        #print phl_obj[0].show()
        '''


    app =  QApplication(sys.argv)
    ex = ParamMainWidget()
    sys.exit(app.exec_())




