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

    def set_app_root(self, root_ref):
        self.my_app = root_ref

    def run_dum_prn(self):
        print "[self.run_dum_prn] =", self.run_dum_prn

    def run_my_proc(self):
        self.setEnabled(False)
        lst_cmd_to_run = [
                          "dials.reciprocal_lattice_viewer",
                          "../../../../dui_test/X4_wide/reuse_area/dials_files/3_reflections.pickle",
                          "../../../../dui_test/X4_wide/reuse_area/dials_files/3_experiments.json"
                         ]

        for num_of_tim in xrange(10):
            self.my_app.processEvents()

        subprocess.call(lst_cmd_to_run)
        #'''

        self.setEnabled(True)

if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.set_app_root(app)


    sys.exit(app.exec_())


