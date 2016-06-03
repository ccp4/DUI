from dials.util.idials import Controller
import sys

linear_example_from_JMP = '''
controller = Controller(".")
controller.set_mode("import")
controller.set_parameters("template=../X4_wide_M1S4_2_####.cbf", short_syntax=True)
controller.run()

controller.set_mode("find_spots")
controller.run()
'''

PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''

#PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "using PySide"
#'''

class MainWidget( QWidget):
    lst_commands = [
                    "import",
                    "find_spots",
                    "index",
                    "refine_bravais_settings",
                    "reindex",
                    "refine",
                    "integrate",
                    "export"
                   ]


    def __init__(self):
        super(MainWidget, self).__init__()

        self.lst_exe_pos = 0
        self.controller = Controller(".")
        self.next_cmd = "import"

        self.btn_prv =  QPushButton('\n  Prev \n', self)
        self.btn_prv.clicked.connect(self.prv_clicked)

        self.btn_go =  QPushButton('\n    Go  \n', self)
        self.btn_go.clicked.connect(self.go_clicked)

        self.btn_nxt =  QPushButton('\n  Next \n', self)
        self.btn_nxt.clicked.connect(self.nxt_clicked)

        hbox =  QHBoxLayout()

        hbox.addWidget(self.btn_prv)
        hbox.addWidget(self.btn_go)
        hbox.addWidget(self.btn_nxt)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def go_clicked(self):
        print "go_clicked(self)"

        self.controller.set_mode(self.next_cmd)

        if( self.controller.get_mode() == "import" ):
            self.controller.set_parameters("template=../X4_wide_M1S4_2_####.cbf", short_syntax=True)
            #self.controller.set_parameters("template=../th_8_2_####.cbf", short_syntax=True)

        self.controller.run(stdout=sys.stdout, stderr=sys.stderr).wait()

        self._update_after_run()

        last_mod = self.controller.get_mode()
        print "last_mod =", last_mod

        for pos, cmd in enumerate(self.lst_commands):
            print "pos =", pos, "  cmd =", cmd
            if( cmd == last_mod ):
                self.next_cmd = self.lst_commands[pos + 1]

        if( self.next_cmd == None ):
            self.next_cmd = "import"

        self.controller.set_mode(self.next_cmd)



    def nxt_clicked(self):
        print "nxt_clicked(self)"
        self.lst_exe_pos += 1

        if( self.lst_exe_pos > len(self.lst_commands) - 1 ):
            self.lst_exe_pos = len(self.lst_commands) - 1

        print "self.lst_exe_pos =", self.lst_exe_pos

    def prv_clicked(self):
        print "prv_clicked(self)"

        self.controller.goto(self.curr_lin - 1)
        self._update_after_run()

        old_way = '''
        self.lst_exe_pos -= 1

        if( self.lst_exe_pos < 0 ):
            self.lst_exe_pos = 0

        print "self.lst_exe_pos =", self.lst_exe_pos
        '''


    def _update_after_run(self):

        history = self.controller.get_history()
        print "history =", history
        history_lines = history.split("\n")

        lst_line_number = []
        lst_hist_cmd = []
        lst_exec_stat = []
        for single_line in history_lines:
            print ">>>", single_line, "<<<"
            single_line = single_line.lstrip()
            lst_data = single_line.split(" ")
            if( len(lst_data) >=3 ):
                tmp_log = '''
                print "Data =>>>",
                for dt_prn in lst_data:
                    print dt_prn, ">>>",

                print "<<<end line"
                '''

                line_number = int(lst_data[0])
                exec_stats = lst_data[1]
                #print "lst_data[len(lst_data) - 1] =", lst_data[len(lst_data) - 1]

                if( lst_data[len(lst_data) - 1] == "(current)" ):
                    self.curr_lin = line_number
                    line_command = lst_data[len(lst_data) - 2]

                else:
                    line_command = lst_data[len(lst_data) - 1]

                lst_line_number.append(line_number)
                lst_hist_cmd.append(line_command)
                lst_exec_stat.append(exec_stats)

        print "________________________________________ List:"

        for n in xrange(len(lst_line_number)):
            print "[", n, "]: ", lst_line_number[n], " >> ", lst_hist_cmd[n], " >> ", lst_exec_stat[n]

        print "controller.get_current() =", self.controller.get_current()
        print "current line =", self.curr_lin
        print "controller.get_mode() =", self.controller.get_mode()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())


