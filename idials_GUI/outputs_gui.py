
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

from img_viewer.np_arr_paint import ImgTab

class outputs_widget( QWidget):
    #item_changed = pyqtSignal()
    def __init__(self, phl_obj, parent = None):
        super(outputs_widget, self).__init__(parent)
        #self.super_parent = parent
        vbox = QVBoxLayout()

        img_view = ImgTab()
        vbox.addWidget(img_view)
        self.setLayout(vbox)
        self.show()


