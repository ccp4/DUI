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

from python_qt_bind import *

class TreeNavWidget(QTreeView):
    #TODO >> try: QTreeWidget
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
        print "item_clicked"
        item = self.tmp_model.itemFromIndex(it_index)


        if item.idials_node.success == True:
            print "item.idials_node.index =", item.idials_node.index
            index_to_jump = item.idials_node.index

        else:
            print "cannot jump to failed step"
            index_to_jump = item.idials_node.parent.index


        self.my_parent.goto(index_to_jump)

class IdialsOuterWidget( QWidget):
    def __init__(self, parent = None):
        super(IdialsOuterWidget, self).__init__(parent)

        my_inner_widget = IdialsInnerrWidget(self)
        vbox =  QVBoxLayout()
        vbox.addWidget(my_inner_widget)

        big_vbox =  QVBoxLayout()

        midl_hbox =  QHBoxLayout()

        self.btn_prv =  QPushButton('\n  Prev \n', self)
        self.btn_prv.clicked.connect(my_inner_widget.prv_clicked)
        midl_hbox.addWidget(self.btn_prv)


        self.btn_go =  QPushButton('\n   Run  \n', self)
        self.btn_go.clicked.connect(my_inner_widget.run_clicked)
        midl_hbox.addWidget(self.btn_go)

        self.btn_nxt =  QPushButton('\n  Next \n', self)
        self.btn_nxt.clicked.connect(my_inner_widget.nxt_clicked)
        midl_hbox.addWidget(self.btn_nxt)

        big_vbox.addLayout(midl_hbox)

        vbox.addLayout(big_vbox)

        self.setLayout(vbox)
        self.setWindowTitle('iDIALS dialog')
        self.show()

    def jump(self, cmd_name = None, new_url = None):
        print "\n MainWidget swishing to", cmd_name, "\n\n"

    def update_report(self, report_path):
        print "\n MainWidget update report with:", report_path


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

    def __init__(self, parent = None):
        super(IdialsInnerrWidget, self).__init__(parent)
        self.super_parent = parent
        self.controller = Controller(".")
        self.next_cmd = "import"

        big_vbox =  QVBoxLayout()

        self.tree_nav = TreeNavWidget(self)
        big_vbox.addWidget(self.tree_nav)

        self.setLayout(big_vbox)
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

        #Telling super parent to jump and to update URL
        self.super_parent.jump(self.next_cmd, self.controller.get_report())

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

            dir_path = self.super_parent.widg_lst[0].lin_import_path.text()
            #tmpl_str = "template=" + dir_path + "/*.cbf"
            tmpl_str = "template=" + dir_path +"/X4_wide_M1S4_2_####.cbf"
            print "dir_path =", dir_path
            print "tmpl_str =", tmpl_str

            self.controller.set_parameters(tmpl_str, short_syntax=True)

        self.controller.run(stdout=sys.stdout, stderr=sys.stderr).wait()
        self._update_tree()
        #print "dir(self.controller)", dir(self.controller)
        print "self.controller.get_report()", self.controller.get_report()
        self.super_parent.update_report(self.controller.get_report())

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


