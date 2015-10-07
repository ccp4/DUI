from PyQt4.QtGui import *
from PyQt4.QtCore import *
from subprocess import call as shell_func

class step(object):
    def __init__(self):
        self.Bttlabel = "\n\n     CLI command    \n\n"
        self.default_action = "dials.some_command"


class InnerBox( QWidget):

    def __init__(self):
        super(InnerBox, self).__init__()
        self.initUI()

    def initUI(self):
        pixmap =  QPixmap("/home/lui/Pictures/dials_logo01.png")
        #pixmap =  QPixmap("/home/dev/Downloads/tux2_w_dart_logo.png")
        lbl =  QLabel(self)
        lbl.setPixmap(pixmap)

        scrollArea =  QScrollArea()
        scrollArea.setWidget(lbl)
        btn_tmp = QPushButton("test", self)

        main_box =  QHBoxLayout()
        main_box.addWidget(btn_tmp)
        #main_box.addStretch(1)
        main_box.addWidget(scrollArea)

        self.setLayout(main_box)


class MainWidget( QWidget):

    def __init__(self, steps_in):
        super(MainWidget, self).__init__()
        self.initUI(steps_in)

    def initUI(self, steps_in):
        self.gui_button_steps = steps_in
        self.btn_lst = []
        for step in self.gui_button_steps:
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



        in_box = InnerBox()
        top_box.addWidget(in_box)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.lin_txt)
        hbox.addWidget(self.btn_go)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(top_box)

        bg_box.addLayout(hbox)

        self.setGeometry(100, 200, 1150, 850)
        self.setLayout(bg_box)
        self.setWindowTitle('Shell dialog')
        self.show()


    def B_clicked_any(self):
        btn_sender = self.sender()

        for pos, btn  in enumerate(self.btn_lst):
            if( btn == btn_sender ):
                self.lin_txt.setText(str(self.gui_button_steps[pos].default_action))


    def B_go_clicked(self):
        shell_str = str(self.lin_txt.text())
        shell_func(shell_str, shell=True)
        print"\n Ok \n"
        self.lin_txt.setText(str(""))
