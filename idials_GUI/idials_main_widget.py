import sys

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


from custom_widgets import StepList
from idials_gui import IdialsOuterWidget

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()

        buttons_widget = QWidget()
        #buttons_widget.setStyleSheet("background-color: solid gray")
        buttons_widget.setStyleSheet("background-color: lightgray")
        v_left_box =  QHBoxLayout()
        self.step_param_widg =  QStackedWidget()
        my_lst = StepList()
        label_lst, self.widg_lst, icon_lst, command_lst = my_lst()

        #My_style = Qt.ToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setWindowTitle('DUI / idials')

        self.btn_lst = []

        for pos, step_data in enumerate(label_lst):

            print "pos = ", pos

            new_btn = QToolButton(self)
            #new_btn.setText(step_data)
            new_btn.setIcon(icon_lst[pos])
            new_btn.setIconSize(QSize(90,90))
            new_btn.par_wig = self.widg_lst[pos]
            new_btn.command = command_lst[pos]
            #new_btn.setToolButtonStyle(My_style)

            #new_btn.setFont(QFont("Monospace", 10, QFont.Bold))
            new_btn.clicked.connect(self.btn_clicked)

            v_left_box.addWidget(new_btn)
            self.step_param_widg.addWidget(new_btn.par_wig)
            self.btn_lst.append(new_btn)

        self.idials_widget = IdialsOuterWidget(self)

        buttons_widget.setLayout(v_left_box)
        self._refrech_btn_look()

        multi_step_hbox = QHBoxLayout()

        multi_step_hbox.addWidget(self.idials_widget)

        control_vbox = QVBoxLayout()
        control_vbox.addWidget(buttons_widget)
        control_vbox.addWidget(self.step_param_widg)
        multi_step_hbox.addLayout(control_vbox)


        main_widget = QWidget()
        main_widget.setLayout(multi_step_hbox)
        self.resize(1200, 900)
        self.setCentralWidget(main_widget)

        self.show()

    def btn_clicked(self):
        my_sender = self.sender()
        self.step_param_widg.setCurrentWidget(my_sender.par_wig)
        self._refrech_btn_look()
        my_sender.setStyleSheet("background-color: lightblue")

        self.idials_widget.change_mode(my_sender.command)


    def _refrech_btn_look(self):
        for btn in self.btn_lst:
            btn.setStyleSheet("background-color: lightgray")

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())



