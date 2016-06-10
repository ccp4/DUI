import sys

PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''

#PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "using PySide"
#'''
def get_my_step_lst():
    return [
            "import",
            "find_spots",
            "index",
            "refine",
            "integrate",
           ]

class ParamWidget(QWidget):
    lst_commands = get_my_step_lst()
    def __init__(self):
        super(ParamWidget, self).__init__()
        hbox =  QVBoxLayout()
        for step_name in self.lst_commands:
            hbox.addWidget(QLabel(step_name))

        self.setLayout(hbox)
        self.show()

class MainWidget(QWidget):
    lst_commands = get_my_step_lst()

    def __init__(self):
        super(MainWidget, self).__init__()

        self.btn_lst = []
        hbox =  QVBoxLayout()
        for step_name in self.lst_commands:
            new_btn = QPushButton(step_name, self)
            new_btn.clicked.connect(self.btn_clicked)
            hbox.addWidget(new_btn)
            self.btn_lst.append(new_btn)

        pw = ParamWidget()
        hbox.addWidget(pw)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def btn_clicked(self):
        print "btn_clicked"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

