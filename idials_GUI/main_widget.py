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

from custom_widgets import StepList


class MainWidget(QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()

        v_left_box =  QVBoxLayout()
        self.step_param_widg =  QStackedWidget()
        my_lst = StepList()
        label_lst, widg_lst, icon_lst = my_lst()
        for pos, step_data in enumerate(label_lst):
            #new_btn = QToolButton(step_data, self)
            new_btn = QToolButton(self)
            My_style = Qt.ToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            new_btn.setToolButtonStyle(My_style)

            new_btn.setText(step_data)
            new_btn.setIcon(icon_lst[pos])
            new_btn.setIconSize(QSize(70,70))
            new_btn.par_wig = widg_lst[pos]
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



