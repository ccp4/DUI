import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import time
from dials.util.idials import Controller

class StdOut(QObject):

    write_signal = pyqtSignal(str)

    def write(self,string):
        self.write_signal.emit(string)

    def flush(self):
        pass

class MyThread (QThread):

    def set_controler(self, controller):
        self.to_run = controller
        self.handler = StdOut()
    def run(self):
        self.to_run.goto(1)
        self.to_run.set_mode("find_spots")



        self.to_run.run(stdout=self.handler, stderr=self.handler).wait()

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

        self.controller = Controller(".")
        self.thrd = MyThread(self)#, self.controller)
        self.thrd.set_controler(self.controller)
        self.thrd.handler.write_signal.connect(self.append_text)
        self.thrd.finished.connect(self.tell_finished)

        self.setLayout(main_box)
        self.show()

    def start_thread(self):
        self.thrd.start()
        self.textedit.insertPlainText("\nstart_thread\n")

    def tell_finished(self):
        print "finished thread"
        self.textedit.insertPlainText("\nfinished\n")

    def append_text(self,text):
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText( text )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

