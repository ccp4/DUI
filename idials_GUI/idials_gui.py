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
        print "item_clicked"
        item = self.tmp_model.itemFromIndex(it_index)


        if item.idials_node.success == True:
            print "item.idials_node.index =", item.idials_node.index
            self.super_parent.goto(item.idials_node.index)
        else:
            print "cannot jump to failed step"
            self.super_parent.goto(item.idials_node.parent.index)

class IdialsOuterWidget( QWidget):
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
        super(IdialsOuterWidget, self).__init__()

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
        self.btn_go.clicked.connect(self.run_clicked)
        midl_hbox.addWidget(self.btn_go)

        self.btn_nxt =  QPushButton('\n  Next \n', self)
        self.btn_nxt.clicked.connect(self.nxt_clicked)
        midl_hbox.addWidget(self.btn_nxt)

        big_vbox.addLayout(midl_hbox)

        self.setLayout(big_vbox)
        self.setWindowTitle('Shell dialog')
        self.show()



    def _set_current_mode(self):

        print "...current.mode =", self.controller.get_current().name
        self.next_cmd = self.controller.get_current().name
        self.controller.set_mode(self.next_cmd)


    def goto(self, idx):
        print "goto: ", idx

        self.controller.goto(idx)
        self._set_current_mode()
        self._update_tree()


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


    def change_mode(self, new_mode):
        print "change_mode(self)"

        self.next_cmd = new_mode
        self.controller.set_mode(self.next_cmd)
        self._update_tree()


    def _update_tree(self):

        history = self.controller.get_history()
        print "history =", history

        current = self.controller.get_current()
        dir_current = '''
        ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__',
        '__hash__', '__init__', '__iter__', '__module__', '__new__', '__reduce__',
        '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
        '__weakref__', 'applied', 'as_dict', 'children', 'description', 'directory', 'experiments',
        'from_dict', 'index', 'name', 'output', 'parameters', 'parent', 'reflections', 'report',
        'success', 'workspace']
        '''
        #print "dir(current) =", dir(current)
        print "current.success =", current.success

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
    ex = IdialsOuterWidget()
    sys.exit(app.exec_())


