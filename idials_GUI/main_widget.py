import sys

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
def get_my_step_lst():
    return [
            "import",
            "find_spots",
            "index",
            "refine",
            "integrate",
           ]

class ParamWidget(QWidget):
    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(QLabel(label_str))

        self.setLayout(v_left_box)

class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()

        v_left_box =  QVBoxLayout()
        self.step_param_widg =  QStackedWidget()

        for step_name in get_my_step_lst():
            new_btn = QPushButton(step_name, self)
            new_btn.par_wig = ParamWidget(step_name)
            new_btn.clicked.connect(self.btn_clicked)
            v_left_box.addWidget(new_btn)

            self.step_param_widg.addWidget(new_btn.par_wig)

        multi_step_hbox = QHBoxLayout()
        multi_step_hbox.addLayout(v_left_box)
        multi_step_hbox.addWidget(self.step_param_widg)

        self.setLayout(multi_step_hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def btn_clicked(self):
        my_sender = self.sender()
        self.step_param_widg.setCurrentWidget(my_sender.par_wig)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

