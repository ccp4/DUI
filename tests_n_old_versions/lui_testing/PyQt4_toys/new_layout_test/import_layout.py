#from subprocess import call as shell_func
import subprocess
import sys, os
#'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
'''
from PySide.QtGui import *
from PySide.QtCore import *
'''

class OverideButtonWidget(QWidget):
    def __init__(self):
        super(OverideButtonWidget, self).__init__()
        self.overide_button = QPushButton(" \n Overide Parameter \n ")
        m_vbox = QVBoxLayout()
        m_vbox.addStretch()

        l_hbox = QHBoxLayout()
        l_hbox.addWidget(self.overide_button)
        l_hbox.addStretch()

        m_vbox.addLayout(l_hbox)

        self.setLayout(m_vbox)

class ChangeParameter(QWidget):
    def __init__(self):
        super(ChangeParameter, self).__init__()
        m_vbox = QVBoxLayout()
        m_vbox.addStretch()
        x_widg = QDoubleSpinBox()
        x_widg.setDecimals(3)
        y_widg = QDoubleSpinBox()
        y_widg.setDecimals(3)

        v_hbox1 = QHBoxLayout()
        v_hbox1.addWidget(QLabel("X beam Centre"))
        v_hbox1.addWidget(x_widg)
        m_vbox.addLayout(v_hbox1)

        v_hbox2 = QHBoxLayout()
        v_hbox2.addWidget(QLabel("Y beam Centre"))
        v_hbox2.addWidget(y_widg)
        m_vbox.addLayout(v_hbox2)

        self.ChangeWidgetButton = QPushButton(" \n back to simple \n ")

        l_hbox = QHBoxLayout()
        l_hbox.addWidget(self.ChangeWidgetButton)
        l_hbox.addStretch()

        m_vbox.addLayout(l_hbox)

        self.setLayout(m_vbox)


class ImportPage(QWidget):
    def __init__(self):
        super(ImportPage, self).__init__()

        template_vbox = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size =  label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel(str("Import"))
        step_label.setFont(label_font)

        self.simple_lin =   QLineEdit(self)
        self.simple_lin.setText(" ? ")
        self.simple_lin.textChanged.connect(self.update_command)

        self.opn_fil_btn = QPushButton(" \n Select File(s) \n ")
        tmp_hbox = QHBoxLayout()
        tmp_hbox.addStretch()
        tmp_hbox.addWidget(self.opn_fil_btn)


        self.par_widg = ChangeParameter()

        template_vbox.addWidget(step_label)
        template_vbox.addLayout(tmp_hbox)
        template_vbox.addStretch()

        self.my_stackedWidget =  QStackedWidget()
        self.overide_button_widget = OverideButtonWidget()
        self.my_stackedWidget.addWidget(self.overide_button_widget)
        self.my_stackedWidget.addWidget(self.par_widg)

        template_vbox.addWidget(self.my_stackedWidget)

        self.par_widg.ChangeWidgetButton.clicked.connect(self.set_overide_button)
        self.overide_button_widget.overide_button.clicked.connect(self.set_par_widg)

        template_vbox.addWidget(self.simple_lin)

        self.opn_fil_btn.clicked.connect(self.open_files)

        #self.templ_cmd = ""
        #self.expli_templ = True
        self.defa_dir = str(os.getcwd())
        self.setLayout(template_vbox)
        self.show()

    def set_overide_button(self):
        print "set_overide_button"
        self.my_stackedWidget.setCurrentWidget(self.overide_button_widget)

    def set_par_widg(self):
        print "set_par_widg"
        self.my_stackedWidget.setCurrentWidget(self.par_widg)

    def open_files(self):
        print "open_files clicked"
        self.simple_lin.setText("something here")

    def update_command(self):
        print "update_command emited"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImportPage()
    sys.exit(app.exec_())
