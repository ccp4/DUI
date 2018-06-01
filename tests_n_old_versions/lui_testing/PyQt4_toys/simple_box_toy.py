#from subprocess import call as shell_func
import subprocess
import sys
#'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
'''
from PySide.QtGui import *
from PySide.QtCore import *
'''
class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.btn1 = QPushButton('\n\n     Click ME    \n\n', self)
        self.btn1.clicked.connect(self.B_clicked1)


        vbox = QVBoxLayout()
        vbox.addWidget(self.btn1)



        bg_box = QVBoxLayout(self)
        bg_box.addLayout(vbox)



        self.setGeometry(1200, 200, 450, 350)
        self.setLayout(bg_box)
        self.setWindowTitle('Shell dialog')
        self.show()


    def paintEvent(self, event):

        p = QPainter()
        p.begin(self)
        p.drawLine(1,1,500,500)
        p.end()


    def B_clicked1(self):
        print "B_clicked1"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
