'''
iDIALS QWidget

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from dials.util.idials import Controller
import sys
from Queue import Queue
from python_qt_bind import *

class TreeNavWidget(QTreeView):
    def __init__(self, parent = None):
        self.my_parent = parent
        super(TreeNavWidget, self).__init__()
        self.clicked[QModelIndex].connect(self.item_clicked)

    def update_me(self, root_node, lst_path_idx):
        self.lst_idx = lst_path_idx

        print self.lst_idx

        self.tmp_model = QStandardItemModel(self)

        self.recursive_node(root_node, self.tmp_model)

        self.tmp_model.setHorizontalHeaderLabels(["History Tree"])
        self.setModel(self.tmp_model)
        self.expandAll()

    def recursive_node(self, root_node, item_in):

        for child_node in root_node.children:
            new_item = QStandardItem(str(child_node.name))

            new_item.idials_node = child_node

            new_item.idx = child_node.index
            new_item.success = child_node.success

            if new_item.idials_node.index == self.lst_idx[-1]:
                new_item.setBackground(Qt.blue)
                new_item.setForeground(Qt.white)
            elif new_item.idials_node.index in self.lst_idx:
                new_item.setBackground(Qt.white)
                new_item.setForeground(Qt.blue)
            elif new_item.idials_node.success == True:
                new_item.setBackground(Qt.white)
                new_item.setForeground(Qt.black)
            else:
                new_item.setBackground(Qt.white)
                new_item.setForeground(Qt.gray)

            new_item.setEditable(False)      # not letting the user edit it

            self.recursive_node(child_node, new_item)
            item_in.appendRow(new_item)


    def item_clicked(self, it_index):
        print "self.my_parent.super_parent.running =", self.my_parent.super_parent.running
        if( self.my_parent.super_parent.running == False ):
            print "_____________________________________________________ <<< item_clicked"
            item = self.tmp_model.itemFromIndex(it_index)

            if item.idials_node.success == True:
                print "item.idials_node.index =", item.idials_node.index
                index_to_jump = item.idials_node.index

            else:
                print "cannot jump to failed step"
                index_to_jump = item.idials_node.parent.index

            self.my_parent.goto(index_to_jump)

class TextOut( QTextBrowser):
    def __init__(self, parent = None):
        super(TextOut, self).__init__(parent)
        self.set_black_font()
        self.content_lst = []

    def set_black_font(self):
        self.setCurrentFont( QFont("Monospace"))
        self.setTextColor( QColor("black"))

    def set_green_font(self):
        self.setCurrentFont( QFont("Monospace"))
        self.setTextColor( QColor("green"))

    def set_red_font(self):
        self.setCurrentFont( QFont("Monospace"))
        self.setTextColor( QColor("red"))

    def append_black(self, to_print):
        self.moveCursor(QTextCursor.End)
        self.set_black_font()
        self.append(to_print)
        self.content_lst.append(to_print)

    def append_green(self, to_print):
        self.moveCursor(QTextCursor.End)
        self.set_green_font()
        self.append(to_print)
        self.content_lst = []

    def append_red(self, to_print):
        self.moveCursor(QTextCursor.End)
        self.set_red_font()
        self.append(to_print)

    def get_full_output_lst(self):
        return self.content_lst

class IdialsOuterWidget( QWidget):
    def __init__(self, parent = None):
        super(IdialsOuterWidget, self).__init__(parent)

        my_inner_widget = IdialsInnerrWidget(self)
        my_inner_widget.rtime_txt_on = True
        self.running = False

        vbox =  QVBoxLayout()
        vbox.addWidget(my_inner_widget)

        big_vbox =  QVBoxLayout()

        midl_hbox =  QHBoxLayout()


        self.btn_prv =  QPushButton('\n  Prev \n', self)
        self.btn_prv.clicked.connect(my_inner_widget.prv_clicked)
        midl_hbox.addWidget(self.btn_prv)

        self.btn_nxt =  QPushButton('\n  Next \n', self)
        self.btn_nxt.clicked.connect(my_inner_widget.nxt_clicked)
        midl_hbox.addWidget(self.btn_nxt)

        self.btn_go =  QPushButton('\n   Run  \n', self)
        self.btn_go.clicked.connect(my_inner_widget.run_clicked)

        big_vbox.addLayout(midl_hbox)
        big_vbox.addWidget(self.btn_go)



        self.txt_out = TextOut()
        vbox.addWidget(self.txt_out)
        vbox.addLayout(big_vbox)

        self.setLayout(vbox)
        self.setWindowTitle('iDIALS dialog')
        self.show()

    def jump(self, cmd_name = None, new_url = None):
        print "\n MainWidget swishing to", cmd_name, "\n\n"
        self.txt_out.append_green("something green")

    def update_report(self, report_path):
        print "\n MainWidget update report with:", report_path

    def start_pbar_motion(self):
        self.running = True
        print "\n\n<<<                                                     start_pbar_motion\n\n"

    def update_pbar_text(self, trim_cor_text):
        print "\n update_pbar_text <<<", trim_cor_text, ">>>"

    def end_pbar_motion(self):
        print "\n\n<<<                                                     end_pbar_motion\n\n"
        self.running = False

class StdOut(QObject):

    write_signal = pyqtSignal(str)

    def write(self,string):
        self.write_signal.emit(string)

    def flush(self):
        pass

class MyThread (QThread):

    def set_controler(self, controller):
        self.to_run = controller
        self.handler = StdOut()

    def run(self):
        self.to_run.run(stdout=self.handler, stderr=self.handler).wait()


class IdialsInnerrWidget( QWidget):
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

    def __init__(self, parent = None, dials_logo = None):
        super(IdialsInnerrWidget, self).__init__(parent)
        self.super_parent = parent
        self.controller = Controller(".")
        self.next_cmd = "import"

        big_vbox =  QVBoxLayout()

        self.tree_nav = TreeNavWidget(self)
        big_vbox.addWidget(self.tree_nav)

        self.thrd = MyThread(self)#, self.controller)
        self.thrd.set_controler(self.controller)
        self.thrd.handler.write_signal.connect(self.append_text)
        self.thrd.started.connect(self.started_thread)
        self.thrd.finished.connect(self.finished_thread)

        self.setLayout(big_vbox)
        self.show()

    def _set_current_mode(self):

        print "...current.mode =", self.controller.get_current().name
        self.next_cmd = self.controller.get_current().name
        self.controller.set_mode(self.next_cmd)

    def goto(self, idx):
        print "goto: ", idx

        self.controller.goto(idx)
        #self._set_current_mode()
        self._update_tree()
        try:
            html_rep = self.controller.get_report()
        except:
            html_rep = None

        self.super_parent.jump(self.next_cmd, html_rep)

    def prv_clicked(self):
        print "prv_clicked(self)"

        current = self.controller.get_current()
        previous = current.parent

        self.controller.goto(previous.index)
        self._set_current_mode()
        self._update_tree()

    def run_clicked(self):
        print "run_clicked(self)"
        print "Running ", self.next_cmd

        self.controller.set_mode(self.next_cmd)

        if( self.controller.get_mode() == "import" ):
            tmpl_str = "template=" + str(self.super_parent.widg_lst[0].templ_lin.text())
            print "tmpl_str =", tmpl_str, "\n\n"
            self.change_parameter(tmpl_str)

        self.thrd.start()

    def append_text(self,text):
        trim_cor_text = text[0:len(text) - 1]
        self.super_parent.txt_out.append_green(trim_cor_text)

        if( self.rtime_txt_on == True ):
            self.super_parent.update_pbar_text(trim_cor_text)


    def started_thread(self):
        self.super_parent.start_pbar_motion()

    def finished_thread(self):

        print "\n\n Here \n\n"
        self._update_tree()
        self.super_parent.end_pbar_motion()

        to_reuse_later = '''
        print "self.controller.get_current().datablock =", str(self.controller.get_current().datablock)
        print "self.controller.get_current().description =", str(self.controller.get_current().description)
        print "self.controller.get_current().directory =", str(self.controller.get_current().directory)
        print "self.controller.get_current().output =", str(self.controller.get_current().output)
        print "self.controller.get_current().workspace =", str(self.controller.get_current().workspace)
        '''


    def nxt_clicked(self):
        print "nxt_clicked(self)"
        last_mod = self.controller.get_current().name
        for pos, cmd in enumerate(self.lst_commands):
            if( cmd == last_mod ):
                self.next_cmd = self.lst_commands[pos + 1]

        self.controller.set_mode(self.next_cmd)
        self._update_tree()


    def change_mode(self, new_mode):
        print "change_mode(self)"
        self.next_cmd = new_mode
        self.controller.set_mode(self.next_cmd)
        self._update_tree()

    def change_parameter(self, par_str):
        self.controller.set_parameters(par_str, short_syntax=True)

    def _update_tree(self):

        history = self.controller.get_history()
        print "history =", history

        current = self.controller.get_current()
        print "current.success =", current.success

        lst_path_idx = [current.index]
        lst_path_cmd = [current.name]

        while current.index > 0:
            previous = current.parent

            lst_path_idx.insert(0, previous.index)
            lst_path_cmd.insert(0, previous.name)

            current = previous

        self.tree_nav.update_me(current, lst_path_idx)

        updt_str = " Click the Dials icon to run >> " + self.controller.get_mode()
        print updt_str
        self.super_parent.update_pbar_text(updt_str)

def dummy_reminder():

    #print "dir(self.idials_widget.controller) =", dir(self.idials_widget.controller)
    dir_controler = '''
    ['get_command_tree', 'get_current', 'get_history', 'get_mode', 'get_models', 'get_parameters', 'get_report'
    , 'get_summary', 'goto', 'lock', 'mode_list', 'redo_parameters', 'reset_parameters', 'run', 'set_mode'
    , 'set_parameters', 'state', 'state_filename', 'undo_parameters']
    '''
    #print "mode_list =", self.idials_widget.controller.mode_list
    #print "get_models=", self.idials_widget.controller.get_models()

    curr = self.idials_widget.controller.get_current()
    dir_curr = '''
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
    '__iter__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    '__str__', '__subclasshook__', '__weakref__', 'applied', 'as_dict', 'children', 'description', 'directory',
    'experiments', 'from_dict', 'index', 'name', 'output', 'parameters', 'parent', 'reflections', 'report',
    'success', 'workspace']
    '''
    curr_mode = self.idials_widget.controller.get_mode()
    print "curr_mode =", curr_mode
    #curr_loc = self.idials_widget.controller.lock
    #print "dir(curr_loc) =", dir(curr_loc)

    print "curr.children =", curr.children
    print "curr.parent =", curr.parent

    print "curr.workspace =", curr.workspace
    #find allowed_parents

    #print "dir(self.idials_widget.controller) =", dir(self.idials_widget.controller)
    dir_controler = '''
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', 'get_command_tree', 'get_current', 'get_history', 'get_mode', 'get_models', 'get_parameters',
    'get_report', 'get_summary', 'goto', 'lock', 'mode_list', 'redo_parameters', 'reset_parameters', 'run', 'set_mode',
    'set_parameters', 'state', 'state_filename', 'undo_parameters']
    '''
    print "self.idials_widget.controller.state =", self.idials_widget.controller.state

    curr_state = self.idials_widget.controller.state
    dir_curr_state = '''
    ['CommandClass', 'Memento', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
    '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    '__str__', '__subclasshook__', '__weakref__', 'as_dict', 'command_tree', 'counter', 'current', 'dump', 'from_dict', 'goto',
    'load', 'mode', 'parameters', 'run', 'workspace']
    '''
    print "curr_state.mode =", curr_state.mode

    curr_run = self.idials_widget.controller
    print dir(curr_run)



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = IdialsOuterWidget()
    sys.exit(app.exec_())




