from subprocess import call as shell_func
import sys
#from PySide import QtGui

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        hbox = QtGui.QVBoxLayout(self)

        self.btn1 = QtGui.QPushButton('    import    ', self)
        hbox.addWidget(self.btn1)
        self.btn1.clicked.connect(self.B_clicked1)

        self.btn2 = QtGui.QPushButton(' find_spots ', self)
        hbox.addWidget(self.btn2)
        self.btn2.clicked.connect(self.B_clicked2)

        self.btn3 = QtGui.QPushButton('    index     ', self)
        hbox.addWidget(self.btn3)
        self.btn3.clicked.connect(self.B_clicked3)

        self.lin_txt = QtGui.QLineEdit(self)
        hbox.addWidget(self.lin_txt)

        self.btn_go = QtGui.QPushButton('      Go      ', self)
        hbox.addWidget(self.btn_go)
        self.btn_go.clicked.connect(self.B_go_clicked)



        self.setLayout(hbox)
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
