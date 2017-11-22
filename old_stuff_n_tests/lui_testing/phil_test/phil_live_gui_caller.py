
from phil_live_gui_generator import PhilWidget
import sys


'''
from python_qt_bind import GuiBinding
gui_lib = GuiBinding()
print "using ", gui_lib.pyhon_binding
qt_tool = gui_lib.pyhon_binding
'''
#TODO uncomment previous code and make it work
#qt_tool = "PyQt4"
qt_tool = "PySide"

if( qt_tool == "PyQt4" ):
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    print "using PyQt4"

else:
    from PySide.QtGui import *
    from PySide.QtCore import *
    pyqtSignal = Signal
    print "using PySide"


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
        self.setWindowTitle('Phil dialog')
        self.show()

    def update_lin_txt(self, str_path, str_value):
        print "running {", str_path, "=", str_value,"}"

if __name__ == '__main__':

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

    app =  QApplication(sys.argv)
    ex = ParamMainWidget(lst_phl_obj[0])

    sys.exit(app.exec_())
