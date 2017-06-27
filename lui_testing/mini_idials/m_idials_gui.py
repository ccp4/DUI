from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import sys
import pickle
from cli_utils import TreeShow
from m_idials import Runner

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.super_parent = self

        ###############################################################################################


        self.cli_tree_output = TreeShow()

        try:
            with open ('bkp.pickle', 'rb') as bkp_in:
                self.uni_controler = pickle.load(bkp_in)

        except:
            self.uni_controler = Runner()

        self.cli_tree_output(self.uni_controler)

        ###############################################################################################

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
        self.cli_tree_output(self.uni_controler)

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(self.uni_controler, bkp_out)



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())



'''

if( __name__ == "__main__"):
    tree_output = TreeShow()

    try:
        with open ('bkp.pickle', 'rb') as bkp_in:
            uni_controler = pickle.load(bkp_in)

    except:
        uni_controler = Runner()

    tree_output(uni_controler)

    command = ""
    while( command.strip() != 'exit' and command.strip() != 'quit' ):
        try:
            inp_str = "lin [" + str(uni_controler.current) + "] >>> "
            command = str(raw_input(inp_str))
            if( command == "" ):
                print "converting empty line in self.slist()"
                command = "slist"

        except:
            print " ... interrupting"
            sys.exit(0)

        uni_controler.run(command)
        tree_output(uni_controler)

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(uni_controler, bkp_out)


'''
