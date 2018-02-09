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

        run_but = QPushButton("run QProcess")
        run_but.clicked.connect(self.run_my_proc)
        vbox.addWidget(run_but)

        kl_but = QPushButton("Kill QProcess")
        kl_but.clicked.connect(self.kill_my_proc)
        vbox.addWidget(kl_but)

#        self.setFocus.connect(self.run_my_proc)

        self.setLayout(vbox)
        self.setModal(True)

    def run_my_proc(self):

        lst_cmd_to_run = [
                     "dials.reciprocal_lattice_viewer",
                     "../../../../dui_test/X4_wide/reuse_area/dials_files/3_reflections.pickle",
                     "../../../../dui_test/X4_wide/reuse_area/dials_files/3_experiments.json"
                     ]

        my_process = subprocess.Popen(lst_cmd_to_run,
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.STDOUT,
                                      bufsize = 1)

        self.my_pid = my_process.pid
        print "self.my_pid =", self.my_pid


        print "Just Launched >>> \n"

        for line in iter(my_process.stdout.readline, b''):
            single_line = line[0:len(line)-1]
            print single_line

        print "\n<<< After Ended"


    def kill_my_proc(self):
        print "self.kill_my_proc"



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
        self.diag.exec_()
        print dir(self.diag)


if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.show()

    sys.exit(app.exec_())


