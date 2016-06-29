from dials.util.idials import Controller
import sys

#PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''

PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
print "using PySide"
#'''

class TreeNavWidget(QTreeView):
    #TODO >> try: QTreeWidget
    def __init__(self, parent = None):
        self.super_parent = parent
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
            new_item.idx = child_node.index

            if new_item.idx == self.lst_idx[-1]:
                new_item.setBackground(Qt.blue)
                new_item.setForeground(Qt.white)
            elif new_item.idx in self.lst_idx:
                new_item.setBackground(Qt.cyan)

            new_item.setEditable(False)      # not letting the user edit it

            self.recursive_node(child_node, new_item)
            item_in.appendRow(new_item)


    def item_clicked(self, it_index):
        print "item_clicked"
        item = self.tmp_model.itemFromIndex(it_index)
        print "item.idx =", item.idx
        self.super_parent.goto(item.idx)
        print "Tst"

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

        self.controller = Controller(".")
        self.next_cmd = "import"

        big_vbox =  QVBoxLayout()

        self.tree_nav = TreeNavWidget(self)

        big_vbox.addWidget(self.tree_nav)

        midl_hbox =  QHBoxLayout()

        self.btn_prv =  QPushButton('\n  Prev \n', self)
        self.btn_prv.clicked.connect(self.prv_clicked)
        midl_hbox.addWidget(self.btn_prv)

        self.btn_go =  QPushButton('\n   Run  \n', self)
        self.btn_go.clicked.connect(self.go_clicked)
        midl_hbox.addWidget(self.btn_go)

        self.btn_nxt =  QPushButton('\n  Next \n', self)
        self.btn_nxt.clicked.connect(self.nxt_clicked)
        midl_hbox.addWidget(self.btn_nxt)

        big_vbox.addLayout(midl_hbox)

        self.setLayout(big_vbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def goto(self, idx):
        print "goto: ", idx
        self.controller.goto(idx)
        print "...current.mode =", self.controller.get_current().name
        self._update_tree()


    def go_clicked(self):
        print "go_clicked(self)"
        print "Running ", self.next_cmd

        self.controller.set_mode(self.next_cmd)

        if( self.controller.get_mode() == "import" ):
            self.controller.set_parameters("template=../X4_wide_M1S4_2_####.cbf", short_syntax=True)
            #self.controller.set_parameters("template=../th_8_2_####.cbf", short_syntax=True)

        self.controller.run(stdout=sys.stdout, stderr=sys.stderr).wait()
        self._update_tree()

    def nxt_clicked(self):
        print "nxt_clicked(self)"
        last_mod = self.controller.get_current().name
        for pos, cmd in enumerate(self.lst_commands):
            if( cmd == last_mod ):
                self.next_cmd = self.lst_commands[pos + 1]

        self.controller.set_mode(self.next_cmd)
        self._update_tree()

    def prv_clicked(self):
        print "prv_clicked(self)"

        current = self.controller.get_current()
        previous = current.parent

        self.controller.goto(previous.index)
        self._update_tree()


    def _update_tree(self):

        history = self.controller.get_history()
        print "history =", history

        current = self.controller.get_current()

        lst_path_idx = [current.index]
        lst_path_cmd = [current.name]

        while current.index > 0:
            previous = current.parent

            lst_path_idx.insert(0, previous.index)
            lst_path_cmd.insert(0, previous.name)

            current = previous

        self.tree_nav.update_me(current, lst_path_idx)

        print
        print " Ready to run >>", self.controller.get_mode()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())


