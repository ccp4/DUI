from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from outputs_n_viewers.web_page_view import WebTab
from outputs_n_viewers.img_viewer import MyImgWin

import sys
import pickle
from cli_utils import TreeShow
from m_idials import Runner
from gui_utils import CliOutView
import subprocess

class MyThread (QThread):

    str_print_signal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyThread, self).__init__()

    def __call__(self, cmd_to_run, ref_to_controler):
        self.cmd_to_run = cmd_to_run
        self.ref_to_controler = ref_to_controler
        self.start()

    def run(self):
        self.ref_to_controler.run(command = self.cmd_to_run, ref_to_class = self)

    def emit_print_signal(self, str_lin):
        #print str_lin, "... Yes"
        self.str_print_signal.emit(str_lin)


class TreeNavWidget(QTreeView):
    def __init__(self, parent = None):
        super(TreeNavWidget, self).__init__()
        print "TreeNavWidget(__init__)"

    def update_me(self, root_node, lst_path_idx):
        self.lst_idx = lst_path_idx

        print self.lst_idx

        self.std_mod = QStandardItemModel(self)
        self.recursive_node(root_node, self.std_mod)

        self.std_mod.setHorizontalHeaderLabels(["History Tree"])
        self.setModel(self.std_mod)
        self.expandAll()

    def recursive_node(self, root_node, item_in):

        #for child_node in root_node.children:
        try:
            for child_node in root_node.next_step_list:
                try:
                    child_node_name = str(child_node.command[0])
                except:
                    child_node_name = "None"

                try:
                    child_node_tip = str(child_node.command[1:])
                except:
                    child_node_tip = "None"

                new_item = QStandardItem(child_node_name)
                new_item.setToolTip(child_node_tip)
                new_item.idials_node = child_node
                #new_item.success = child_node.success

                if( self.lst_idx == child_node.lin_num ):
                    new_item.setBackground(Qt.blue)
                    new_item.setForeground(Qt.white)

                else:
                    new_item.setBackground(Qt.white)
                    new_item.setForeground(Qt.blue)

                new_item.setEditable(False)      # not letting the user edit it

                self.recursive_node(child_node, new_item)
                item_in.appendRow(new_item)

        except:
            print "end of node"

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()

        try:
            with open ('bkp.pickle', 'rb') as bkp_in:
                self.uni_controler = pickle.load(bkp_in)

        except:
            self.uni_controler = Runner()

        self.cli_tree_output = TreeShow()
        self.cli_tree_output(self.uni_controler)

        main_box = QVBoxLayout()

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)

        self.tree_out =TreeNavWidget()
        self.tree_out.clicked[QModelIndex].connect(self.item_clicked)
        self.tree_out.update_me(self.uni_controler.step_list[0], self.uni_controler.current)

        h_main_splitter.addWidget(self.tree_out)

        self.cli_out = CliOutView()
        self.web_view = WebTab()
        self.img_view = MyImgWin("1_datablock.json")

        self.my_tabs = QTabWidget()
        self.my_tabs.addTab(self.img_view, "Image View")
        self.my_tabs.addTab(self.cli_out, "CLI OutPut")
        self.my_tabs.addTab(self.web_view, "Report View")

        h_main_splitter.addWidget(self.my_tabs)

        main_box.addWidget(h_main_splitter)

        self.custom_thread = MyThread()
        self.custom_thread.finished.connect(self.update_after_finished)
        self.custom_thread.str_print_signal.connect(self.cli_out.add_txt)

        self.cmd_edit = QLineEdit()
        self.cmd_edit.editingFinished.connect(self.cmd_entr)

        main_box.addWidget(QLabel("DIALS command: "))
        main_box.addWidget(self.cmd_edit)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

    def cmd_entr(self, command_overwrite = None):
        if( command_overwrite == None ):
            new_cmd = str(self.cmd_edit.text())

        else:
            new_cmd = command_overwrite

        print "command entered:", new_cmd
        if( new_cmd == "" ):
            new_cmd = "slist"

        self.custom_thread(new_cmd, self.uni_controler)

    def update_after_finished(self):

        self.cmd_edit.setText("")
        self.cli_tree_output(self.uni_controler)
        #self.web_view.update_page("/scratch/dui/dui_test/only_20_img_X4_wide/dui_tst_02/dials-2/6_refine/report.html")
        self.web_view.update_page("/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_05/dials-1/5_reindex/report.html")
        self.tree_out.update_me(self.uni_controler.step_list[0], self.uni_controler.current)

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(self.uni_controler, bkp_out)

    def item_clicked(self, it_index):
        print "TreeNavWidget(item_clicked)"
        item = self.tree_out.std_mod.itemFromIndex(it_index)
        lin_num = item.idials_node.lin_num
        print "clicked item lin_num (self.tree_out.std_mod) =", lin_num
        cmd_ovr = "goto " + str(lin_num)
        self.cmd_entr(cmd_ovr)


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

