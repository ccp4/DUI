import sys
from Queue import Queue
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import subprocess

class run_something(object):
    def __init__(self):
        self.cmd_to_run = "./sec_interval.sh"

    def __call__(self):

        my_process = subprocess.Popen([self.cmd_to_run])
        my_process.wait()

        if( my_process.poll() == 0 ):
            self.success = True

        else:
            self.success = False

        print "self.success =", self.success


# The new Stream Object which replaces the default stream associated with sys.stdout
# This object just puts data in a queue!
class WriteStream(object):
    def __init__(self,queue):
        self.queue = queue

    def write(self, text):
        self.queue.put(text)

# A QObject (to be run in a QThread) which sits waiting for data to come through a Queue.Queue().
# It blocks until data is available, and one it has got something from the queue, it sends
# it to the "MainThread" by emitting a Qt Signal

class MyReceiver(QObject):
    mysignal = pyqtSignal(str)

    def __init__(self,queue ):
        super(MyReceiver, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            text = self.queue.get()
            self.mysignal.emit(text)

# An example QObject (to be run in a QThread) which outputs information with print
class Running_iDIALS_stuff(QThread):
    def __init__(self):
        super(Running_iDIALS_stuff, self).__init__()
        self.to_run = run_something()

    def run(self):

        self.to_run()

        print "QThread"



# An Example application QWidget containing the textedit to redirect stdout to
class MyApp(QWidget):
    def __init__(self ):
        super(MyApp, self).__init__()

        # start moved stuff
        # Create Queue and redirect sys.stdout to this queue
        tmp_queue = Queue()
        sys.stdout = WriteStream(tmp_queue)

        # Create thread that will listen on the other end of the queue, and send the text to the textedit in our application
        self.outher_thread = QThread()
        my_receiver = MyReceiver(tmp_queue)
        my_receiver.mysignal.connect(self.append_text)
        my_receiver.moveToThread(self.outher_thread)
        self.outher_thread.started.connect(my_receiver.run)
        self.outher_thread.start()
        #end moved stuff

        self.layout = QVBoxLayout(self)
        self.textedit = QTextEdit()
        self.button = QPushButton('start long running thread')
        self.button.clicked.connect(self.start_thread)
        self.layout.addWidget(self.textedit)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        self.show()

    def append_text(self,text):
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText( text )

    def start_thread(self):
        self.thread = QThread()
        self.idials_thread = Running_iDIALS_stuff()
        self.idials_thread.moveToThread(self.thread)
        self.thread.started.connect(self.idials_thread.run)
        self.thread.start()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
