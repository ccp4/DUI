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
    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        v_left_box =  QVBoxLayout()
        v_left_box.addWidget(QLabel(label_str))

        self.setLayout(v_left_box)
        self.show()

class MainWidget(QWidget):
    lst_commands = get_my_step_lst()

    def __init__(self):
        super(MainWidget, self).__init__()

        self.btn_lst = []
        v_left_box =  QVBoxLayout()
        for step_name in self.lst_commands:
            new_btn = QPushButton(step_name, self)
            new_btn.clicked.connect(self.btn_clicked)
            v_left_box.addWidget(new_btn)
            self.btn_lst.append(new_btn)

        stackedWidget =  QStackedWidget()

        for step_name in self.lst_commands:
            param_widg = ParamWidget(step_name)
            stackedWidget.addWidget(param_widg)

        bing_h_box = QHBoxLayout()
        bing_h_box.addLayout(v_left_box)
        bing_h_box.addWidget(stackedWidget)


        '''
        firstPageWidget =  QWidget()
        secondPageWidget =  QWidget()
        thirdPageWidget =  QWidget()

        stackedWidget =  QStackedWidget()
        stackedWidget.addWidget(firstPageWidget)
        stackedWidget.addWidget(secondPageWidget)
        stackedWidget.addWidget(thirdPageWidget)

        layout =  QVBoxLayout()
        layout.addWidget(stackedWidget)
        setLayout(layout)
        '''

        self.setLayout(bing_h_box)
        self.setWindowTitle('Shell dialog')
        self.show()

    def btn_clicked(self):
        print "btn_clicked"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

