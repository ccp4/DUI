#gpl = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "wprks with PyQt4"
#'''
py_side = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "works with PySide"
#'''
import subprocess
import sys
import psutil

from time import sleep

def kill_w_child(pid_num):
    print "attempting to kill pid #:", pid_num
    parent_proc = psutil.Process(pid_num)
    for child in parent_proc.children(recursive=True):  # or parent_proc.children() for recursive=False
        child.kill()

    parent_proc.kill()


class MyThread (QThread):

    def __init__(self, parent = None):
        super(MyThread, self).__init__()

    def run(self):
        print "Hi from QThread(run)  ___________________ Before Loop"
        my_proc = psutil.Process(self.pid_to_see)
        while(my_proc.status() == 'running' or my_proc.status() == 'sleeping'):
            print "my_proc.status() =", my_proc.status()


        print "my_proc.status() =", my_proc.status()

        print "_________________________________________ Loop ended"

    def get_pid(self, pid_in):
        self.pid_to_see = pid_in



class MyDialog(QDialog):
    def __init__(self, parent = None):
        super(MyDialog, self).__init__()

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("\n Hi QDialog \n"))

        kl_but = QPushButton("Kill QProcess")
        kl_but.clicked.connect(self.kill_my_proc)
        vbox.addWidget(kl_but)

        self.setLayout(vbox)
        self.setModal(True)

    def run_my_proc(self):

        lst_cmd_to_run = [
                     "dials.reciprocal_lattice_viewer",
                     "../../../../dui_test/X4_wide/reuse_area/dials_files/3_reflections.pickle",
                     "../../../../dui_test/X4_wide/reuse_area/dials_files/3_experiments.json"
                     ]
        self.my_process = subprocess.Popen(lst_cmd_to_run)
        self.proc_pid = self.my_process.pid


        ############################################### Test Ini
        self.thrd = MyThread()
        self.thrd.get_pid(self.proc_pid)
        self.thrd.finished.connect(self.child_closed)
        self.thrd.start()
        ############################################### Test End


        self.exec_()

    def kill_my_proc(self):
        print "self.kill_my_proc"
        print "time to kill", self.proc_pid
        kill_w_child(self.proc_pid)
        self.done(0)

    def child_closed(self):
        print "after ...close()"
        self.kill_my_proc()


    def closeEvent(self, event):
        print "from << closeEvent  (QDialog) >>"


class OuterCaller(QWidget):
    def __init__(self):
        super(OuterCaller, self).__init__()

        v_box = QHBoxLayout()
        v_box.addWidget(QLabel("\n Click >> \n"))

        my_but = QPushButton("Start QProcess")
        my_but.clicked.connect(self.run_my_dialg)
        v_box.addWidget(my_but)

        self.diag = MyDialog()

        self.setLayout(v_box)
        self.show()

    def run_my_dialg(self):
        self.diag.run_my_proc()


if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.show()

    sys.exit(app.exec_())


