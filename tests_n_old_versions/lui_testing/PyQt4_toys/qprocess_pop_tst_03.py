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


class MyQProcess(QProcess):
    def __init__(self):
        super(MyQProcess, self).__init__()

        self.started.connect(self.on_start)
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.finished.connect(self.on_finish)

    def on_start(self):
        print "on_start"

    def on_finish(self):
        print "on_finish"

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        print ">>", single_line


class MyDialog(QDialog):
    def __init__(self, parent = None):
        super(MyDialog, self).__init__()


        self.qProcess = MyQProcess()
        self.qProcess.setProcessChannelMode(QProcess.MergedChannels);


        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("\n Hi QDialog \n"))

        kl_but = QPushButton("Kill QProcess")
        kl_but.clicked.connect(self.kill_my_proc)
        vbox.addWidget(kl_but)
        run_but = QPushButton("run QProcess")
        run_but.clicked.connect(self.run_my_proc)
        vbox.addWidget(run_but)

        self.setLayout(vbox)
        self.setModal(True)
        self.show()

    def run_my_proc(self):

        lst_cmd_to_run = "dials.reciprocal_lattice_viewer"
        lst_cmd_to_run += " ../../../../dui_test/X4_wide/reuse_area/dials_files/3_reflections.pickle"
        lst_cmd_to_run += " ../../../../dui_test/X4_wide/reuse_area/dials_files/3_experiments.json"

        self.qProcess.start(lst_cmd_to_run)
        #self.qProcess.start("./sec_interval.sh")




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

        self.setLayout(v_box)
        self.show()

    def set_root_ref(self, root_app):
        self.my_app = root_app

    def run_my_dialg(self):
        diag = MyDialog()
        self.my_app.processEvents()
        print "Here 1"
        diag.exec_()


if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.set_root_ref(app)
    my_widg.show()


    sys.exit(app.exec_())


