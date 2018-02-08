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
import subprocess, sys

class OuterCaller(QWidget):
    def __init__(self):
        super(OuterCaller, self).__init__()

        v_box = QHBoxLayout()
        v_box.addWidget(QLabel("\n Click >> \n"))

        my_but = QPushButton("Start QProcess")
        my_but.clicked.connect(self.run_my_proc)
        v_box.addWidget(my_but)

        dum_but = QPushButton("dummy button")
        dum_but.clicked.connect(self.run_dum_prn)
        v_box.addWidget(dum_but)

        self.setLayout(v_box)
        self.show()

    def run_dum_prn(self):
        print "[self.run_dum_prn] =", self.run_dum_prn

    def run_my_proc(self):
        self.setEnabled(False)
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

        '''
Constant    Description
Qt.NonModal The window is not modal and does not block input to other windows.
Qt.WindowModal  The window is modal to a single window hierarchy and blocks input to its parent window, all grandparent windows, and all siblings of its parent and grandparent windows.
Qt.ApplicationModal The window is modal to the application and blocks input to all windows.
        '''


        print "Just Launched --> \n"
        for line in iter(my_process.stdout.readline, b''):
            single_line = line[0:len(line)-1]
            print single_line

        print "\n<-- After Ended"

        self.setEnabled(True)

if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.show()


    sys.exit(app.exec_())


