
import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyThread (QThread):

    def __init__(self):
        print "MyThread.__init__()"

    def run():
        socket = QTcpSocket()

        # something here

        self.exec_()


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        self.textedit = QTextEdit()
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.textedit)

        main_box = QHBoxLayout()
        main_box.addWidget(scrollArea)
        self.setLayout(main_box)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

