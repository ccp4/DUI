from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import sys
import pickle
from cli_utils import TreeShow
from m_idials import Runner
from gui_utils import MyQProcess
import subprocess


class DialsCommandGUI(object):
    def __init__(self):
        print "creating new DialsCommand (PyQt4 obj)"

        #try:
        self.qProcess  = MyQProcess(self)
        self.qProcess.setProcessChannelMode(QProcess.SeparateChannels)
        print "MyQProcess() ready"
        #except:
        #    print "Failed to create MyQProcess()"

    def __call__(self, lst_cmd_to_run):
        #try:

        cmd_nam = lst_cmd_to_run[0]
        cmd_par = lst_cmd_to_run[1:]
        self.qProcess.start(cmd_nam, cmd_par)
        local_success = True
        self.qProcess.waitForFinished()
        self.qProcess.close()
        '''
        print "\n << running >>", lst_cmd_to_run, "from GUI class"
        my_process = subprocess.Popen(lst_cmd_to_run)
        my_process.wait()
        if( my_process.poll() == 0 ):
            local_success = True

        else:
            local_success = False
        '''

        '''
        except:
            local_success = False
            print "\n FAIL call"
        '''

        return local_success


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.super_parent = self
        self.cli_tree_output = TreeShow()
        '''
        try:
            with open ('bkp.pickle', 'rb') as bkp_in:
                self.uni_controler = pickle.load(bkp_in)

        except:
        '''
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

        self.uni_controler.run(new_cmd)
        self.cmd_edit.setText("")
        self.cli_tree_output(self.uni_controler)
        '''
        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(self.uni_controler, bkp_out)
        '''



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

