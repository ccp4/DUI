from subprocess import call as shell_func
import sys

#from PyQt4 import QtGui, QtCore

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example( QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        self.btn1 =  QPushButton('\n\n     import    \n\n', self)
        self.btn1.clicked.connect(self.B_clicked1)

        self.btn2 =  QPushButton('\n\n find_spots \n\n', self)
        self.btn2.clicked.connect(self.B_clicked2)

        self.btn3 =  QPushButton('\n\n    index     \n\n', self)
        self.btn3.clicked.connect(self.B_clicked3)

        self.lin_txt =  QLineEdit(self)
        self.btn_go =  QPushButton('\n      Go      \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        vbox =  QVBoxLayout()
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        top_box =  QHBoxLayout()
        top_box.addLayout(vbox)
        #top_box.addStretch(1)

        pixmap =  QPixmap("../../../Pictures/crouton_powered_01.jpg")

        '''
        pixmap  =  QPixmap(QSize(400,400))
        painter =  QPainter(pixmap)
        gradient =  QLinearGradient(QPointF(pixmap.rect().topLeft()),
                       QPointF(pixmap.rect().bottomLeft()))

        gradient.setColorAt(0,    Qt.blue)
        gradient.setColorAt(0.4,  Qt.cyan)
        gradient.setColorAt(1,    Qt.green)

        brush   =  QBrush(gradient)
        painter.fillRect(  QRectF(0, 0, 400, 400), brush)
        painter.drawText(  QRectF(0, 0, 400, 400),  Qt.AlignCenter,
                  "This is an image created with QPainter and QPixmap")
        '''

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
    app =  QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

