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
        my_process = subprocess.Popen(lst_cmd_to_run)
        self.my_pid = my_process.pid
        self.exec_()


    def kill_my_proc(self):
        print "self.kill_my_proc"
        print "time to kill", self.my_pid



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
        #self.diag.exec_()


if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.show()

    sys.exit(app.exec_())


