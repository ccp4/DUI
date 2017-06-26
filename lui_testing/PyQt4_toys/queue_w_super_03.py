import sys
from Queue import Queue
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import subprocess

class run_something(object):
    def __init__(self):
        self.cmd_to_run = "./sec_interval.sh"

    def __call__(self):

        print "before subprocess"
        p = subprocess.Popen([self.cmd_to_run],
                             stdout = subprocess.PIPE,
                             stderr = subprocess.STDOUT,
                             bufsize = 1)
        print "after subprocess"

        for line in iter(p.stdout.readline, b''):
            single_line = line[0:len(line)-1]
            print single_line

        p.wait()
        p.stdout.close()

        print "after ...close()"

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

    def __init__(self, queue):
        super(MyReceiver, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            text = self.queue.get()
            self.mysignal.emit(text)

# An example QObject (to be run in a QThread) which outputs information with print
class LongRunningThing(QObject):
    def __init__(self):
        super(LongRunningThing, self).__init__()
        self.to_run = run_something()

    def run(self):
        self.to_run()

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()

        queue = Queue()
        sys.stdout = WriteStream(queue)
        outer_thread = QThread()
        my_receiver = MyReceiver(queue)
        my_receiver.mysignal.connect(self.append_text)
        my_receiver.moveToThread(outer_thread)
        outer_thread.started.connect(my_receiver.run)
        outer_thread.start()

        self.layout = QVBoxLayout(self)
        self.textedit = QTextEdit()
        self.button_run = QPushButton('start long running thread')
        self.button_run.clicked.connect(self.start_thread)
        self.layout.addWidget(self.textedit)
        self.layout.addWidget(self.button_run)

        self.button_console = QPushButton('print to console')
        self.button_console.clicked.connect(self.print_to_console)
        self.layout.addWidget(self.button_console)


    def append_text(self,text):
        self.textedit.moveCursor(QTextCursor.End)
        self.textedit.insertPlainText( text )

    def start_thread(self):
        self.thread_2 = QThread()
        self.long_running_thing = LongRunningThing()
        self.long_running_thing.moveToThread(self.thread_2)
        self.thread_2.started.connect(self.long_running_thing.run)
        self.thread_2.start()

    def print_to_console(self):
        print "printing AAAAAAAAAAAA"


if( __name__ == "__main__" ):

    # Create QApplication and QWidget
    qapp = QApplication(sys.argv)
    app = MyApp()
    app.show()

    qapp.exec_()
