import sys
from PySide.QtGui import *
from PySide.QtCore import *

class MyThread (QThread):

    def run(self):
        print "Hi from QThread(run)"

        #self.exec_() #complains "QThread: Destroyed while thread is still running"

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        main_box = QHBoxLayout()

        self.textedit = QTextEdit()
        main_box.addWidget(self.textedit)

        self.pushbutton = QPushButton('Click Me')
        main_box.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.start_thread)

        self.setLayout(main_box)
        self.show()

    def start_thread(self):
        thr = MyThread(self)
        thr.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

