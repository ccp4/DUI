'''
iDIALS mode higher level DUI QWidget

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
from idials_gui import IdialsInnerrWidget
from outputs_gui import outputs_widget

class CentreWidget( QWidget):
    def __init__(self, parent = None):
        super(CentreWidget, self).__init__(parent)

    def __call__(self, widget_buts = None, go_btn = None, param_widg = None):

        main_box = QVBoxLayout()

        #h_or_v_box = QVBoxLayout()
        h_or_v_box = QHBoxLayout()

        h_or_v_box.addWidget(widget_buts)
        h_or_v_box.addWidget(go_btn)
        main_box.addLayout(h_or_v_box)
        main_box.addWidget(param_widg)

        self.setLayout(main_box)
        self.show()


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()

        buttons_widget = QWidget()
        #buttons_widget.setStyleSheet("background-color: solid gray")
        buttons_widget.setStyleSheet("background-color: lightgray")
        v_left_box =  QHBoxLayout()
        self.step_param_widg =  QStackedWidget()
        my_lst = StepList(parent = self)
        label_lst, self.widg_lst, icon_lst, command_lst = my_lst()

        #My_style = Qt.ToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setWindowTitle('DUI / idials')

        self.btn_lst = []

        for pos, step_data in enumerate(label_lst):
            print "pos = ", pos
            new_btn = QToolButton(self)
            #new_btn.setText(step_data)
            new_btn.setToolTip(step_data)
            new_btn.setIcon(icon_lst[pos])
            new_btn.setIconSize(QSize(50,50))
            new_btn.par_wig = self.widg_lst[pos]
            new_btn.command = command_lst[pos]
            #new_btn.setToolButtonStyle(My_style)

            #new_btn.setFont(QFont("Monospace", 10, QFont.Bold))
            new_btn.clicked.connect(self.btn_clicked)

            v_left_box.addWidget(new_btn)
            self.step_param_widg.addWidget(new_btn.par_wig)
            self.btn_lst.append(new_btn)

        self.idials_widget = IdialsInnerrWidget(self)

        buttons_widget.setLayout(v_left_box)
        self._refrech_btn_look()

        multi_step_hbox = QSplitter()

        multi_step_hbox.addWidget(self.idials_widget)

        self.btn_go =  QPushButton('\n   Run  \n', self)
        self.btn_go.clicked.connect(self.idials_widget.run_clicked)

        centre_widget = CentreWidget(self)
        centre_widget(buttons_widget, self.btn_go, self.step_param_widg)

        multi_step_hbox.addWidget(centre_widget)

        img_view = outputs_widget(self)
        multi_step_hbox.addWidget(img_view)

        self.resize(1200, 900)
        self.setCentralWidget(multi_step_hbox)

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



