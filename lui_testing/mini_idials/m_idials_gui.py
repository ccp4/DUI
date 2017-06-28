from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import sys
import pickle
from cli_utils import TreeShow
from m_idials import Runner
from gui_utils import MyQProcess
import subprocess


class DialsCommandGUI(QObject):

    mysignal = pyqtSignal(str)

    def __init__(self):
        super(DialsCommandGUI, self).__init__()
        print "creating new DialsCommand (PyQt4 obj)"


    def __call__(self, lst_cmd_to_run):
        try:

            print "before subprocess"
            my_process = subprocess.Popen(lst_cmd_to_run,
                                            stdout = subprocess.PIPE,
                                            stderr = subprocess.STDOUT,
                                            bufsize = 1)
            print "after subprocess"

            for line in iter(my_process.stdout.readline, b''):
                single_line = line[0:len(line)-1]
                print single_line
                self.mysignal.emit(single_line)

            my_process.wait()
            my_process.stdout.close()
            print "after ...close()"
            if( my_process.poll() == 0 ):
                local_success = True

            else:
                local_success = False

        except:
            local_success = False
            print "\n FAIL call"

        return local_success


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.super_parent = self
        self.cli_tree_output = TreeShow()


        #try:
        #    with open ('bkp.pickle', 'rb') as bkp_in:
        #        self.uni_controler = pickle.load(bkp_in)
        #
        #except:


        gui_runner = DialsCommandGUI()
        self.uni_controler = Runner(gui_runner)


        self.cli_tree_output(self.uni_controler)

        main_box = QHBoxLayout()
        main_box.addWidget(QLabel("DIALS command: "))

        self.cmd_edit = QLineEdit()
        self.cmd_edit.editingFinished.connect(self.cmd_entr)

        main_box.addWidget(self.cmd_edit)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

    def cmd_entr(self):
        new_cmd = str(self.cmd_edit.text())
        print "command entered:", new_cmd
        if( new_cmd == "" ):
            new_cmd = "slist"

        self.uni_controler.run(new_cmd)
        self.cmd_edit.setText("")
        self.cli_tree_output(self.uni_controler)

        #with open('bkp.pickle', 'wb') as bkp_out:
        #    pickle.dump(self.uni_controler, bkp_out)



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

