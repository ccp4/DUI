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
class ParamWidget(QWidget):
    def __init__(self):
        super(ParamWidget, self).__init__()
        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(QLabel("               Import widget here"))
        self.setLayout(v_left_box)
