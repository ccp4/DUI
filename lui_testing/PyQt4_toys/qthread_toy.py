import sys
from PySide.QtGui import *
from PySide.QtCore import *
import time

class MyThread (QThread):

    def run(self):
        print "Hi from QThread(run)"
        for i in range(30):
            time.sleep(0.1)
            print i

        #self.exec_() #complains "QThread: Destroyed while thread is still running"

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Qthread Toy')

        self.thrd = MyThread(self)
        self.thrd.finished.connect(self.tell_finished)
        main_box = QHBoxLayout()

        self.textedit = QTextEdit()
        main_box.addWidget(self.textedit)

        self.pushbutton = QPushButton('Click Me')
        main_box.addWidget(self.pushbutton)
        self.pushbutton.clicked.connect(self.start_thread)

        self.setLayout(main_box)
        self.show()

    def start_thread(self):
        self.thrd.start()

    def tell_finished(self):
        print "finished thread"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

