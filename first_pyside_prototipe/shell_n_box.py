from subprocess import call as shell_func
import sys

from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn1 = QtGui.QPushButton('\n\n     import    \n\n', self)
        self.btn1.clicked.connect(self.B_clicked1)

        self.btn2 = QtGui.QPushButton('\n\n find_spots \n\n', self)
        self.btn2.clicked.connect(self.B_clicked2)

        self.btn3 = QtGui.QPushButton('\n\n    index     \n\n', self)
        self.btn3.clicked.connect(self.B_clicked3)

        self.lin_txt = QtGui.QLineEdit(self)
        self.btn_go = QtGui.QPushButton('\n      Go      \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        top_box = QtGui.QHBoxLayout()
        top_box.addLayout(vbox)
        top_box.addStretch(1)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.lin_txt)
        hbox.addWidget(self.btn_go)

        bg_box = QtGui.QVBoxLayout(self)
        bg_box.addLayout(top_box)
        bg_box.addStretch(1)
        bg_box.addLayout(hbox)

        self.setGeometry(100, 200, 1150, 850)
        self.setLayout(bg_box)
        self.setWindowTitle('Shell dialog')
        self.show()


    def B_clicked1(self):
        self.lin_txt.setText(str("dials.import"))

    def B_clicked2(self):
        self.lin_txt.setText(str("dials.find_spots"))

    def B_clicked3(self):
        self.lin_txt.setText(str("dials.index"))

    def B_go_clicked(self):
        shell_str = str(self.lin_txt.text())
        shell_func(shell_str, shell=True)
        self.lin_txt.setText(str(""))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
