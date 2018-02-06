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
'''
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
'''

class OuterCaller(QWidget):
    def __init__(self):
        super(OuterCaller, self).__init__()

        v_box = QHBoxLayout()
        v_box.addWidget(QLabel("\n Click >> \n"))

        my_but = QPushButton("Start QProcess")
        my_but.clicked.connect(self.run_my_proc)
        v_box.addWidget(my_but)

        #self.qProcess = MyQProcess()
        #self.qProcess.setProcessChannelMode(QProcess.MergedChannels);

        self.setLayout(v_box)
        self.show()

    def run_my_proc(self):
        #self.qProcess.start("./sec_interval.sh")
        #self.qProcess.start("dials.reciprocal_lattice_viewer /scratch/dui/dui_test/only_20_img_X4_wide/aaaa/dials_files/6_reflections.pickle /scratch/dui/dui_test/only_20_img_X4_wide/aaaa/dials_files/6_experiments.json")

        p = subprocess.Popen(["dials.reciprocal_lattice_viewer /scratch/dui/dui_test/only_20_img_X4_wide/aaaa/dials_files/6_reflections.pickle /scratch/dui/dui_test/only_20_img_X4_wide/aaaa/dials_files/6_experiments.json"],
                            shell = True,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.STDOUT,
                            bufsize = 1)

        print "after subprocess"

        for line in iter(p.stdout.readline, b''):
            single_line = line[0:len(line)-1]
            print single_line

if __name__ == '__main__':

    app   = QApplication(sys.argv)

    my_widg = OuterCaller()
    my_widg.show()


    sys.exit(app.exec_())


