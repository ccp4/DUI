from subprocess import call as shell_func
import sys

#from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class step(object):
    def __init__(self):
        self.Bttlabel = "\n\n     CLI command    \n\n"
        self.action = "dials.some_command"


steps = []

import_step = step()
import_step.Bttlabel = "\n\n     import    \n\n"
import_step.action = "dials.import ~/data/th_8_2_0*"
steps.append(import_step)

find_step = step()
find_step.Bttlabel = "\n\n     find spots    \n\n"
find_step.action = "dials.find_spots datablock.json"
steps.append(find_step)

index_step = step()
index_step.Bttlabel = "\n\n     index    \n\n"
index_step.action = "dials.index datablock.json strong.pickle"
steps.append(index_step)

refine_step = step()
refine_step.Bttlabel = "\n\n     refine    \n\n"
refine_step.action = "dials.refine experiments.json indexed.pickle"
steps.append(refine_step)

integrate_step = step()
integrate_step.Bttlabel = "\n\n     integrate    \n\n"
integrate_step.action = "dials.integrate refined_experiments.json refined.pickle"
steps.append(integrate_step)

export_step = step()
export_step.Bttlabel = "\n\n     export    \n\n"
export_step.action = "dials.export integrated.pickle integrated.h5"
steps.append(export_step)


class Example( QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn_lst = []
        for step in steps:
            btn_tmp = QPushButton(step.Bttlabel, self)
            btn_tmp.clicked.connect(self.B_clicked_any)

            self.btn_lst.append(btn_tmp)

        self.lin_txt =  QLineEdit(self)
        self.btn_go =  QPushButton('\n      Go      \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        vbox =  QVBoxLayout()
        for btn in self.btn_lst:
            vbox.addWidget(btn)

        top_box =  QHBoxLayout()
        top_box.addLayout(vbox)
        top_box.addStretch(1)

        pixmap =  QPixmap("/home/lui/Pictures/dials_logo01.png")

        lbl =  QLabel(self)
        lbl.setPixmap(pixmap)

        scrollArea =  QScrollArea()
        scrollArea.setWidget(lbl)

        top_box.addWidget(scrollArea)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.lin_txt)
        hbox.addWidget(self.btn_go)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(top_box)
        #bg_box.addStretch(1)
        bg_box.addLayout(hbox)

        self.setGeometry(100, 200, 1150, 850)
        self.setLayout(bg_box)
        self.setWindowTitle('Shell dialog')
        self.show()


    def B_clicked_any(self):
        btn_sender = self.sender()

        for pos, btn  in enumerate(self.btn_lst):
            if( btn == btn_sender ):
                self.lin_txt.setText(str(steps[pos].action))


    def B_go_clicked(self):
        shell_str = str(self.lin_txt.text())
        shell_func(shell_str, shell=True)
        print"\n Ok \n"
        self.lin_txt.setText(str(""))

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

