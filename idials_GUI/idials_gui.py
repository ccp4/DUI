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



class TreeNavWidget(QTreeView):

    def __init__(self):
        super(TreeNavWidget, self).__init__()
        self.model = QStandardItemModel(self)

        tmp_item = QStandardItem("dummy element")
        self.model.appendRow(tmp_item)

        self.setModel(self.model)
        self.expandAll()
        self.clicked.connect(self.item_clicked)
        #print "self.model Dr =", dir(self.model)
        #self.model.itemChanged.connect(self.item_clicked)

    def update_me(self, root_node):
        self.tmp_model = QStandardItemModel(self)
        self.main_item = QStandardItem("1")

        dir_main_item = '''
        ['ItemType', 'Type', 'UserType', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__',
        '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
        '__lshift__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
        '__rlshift__', '__rrshift__', '__rshift__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
        'accessibleDescription', 'accessibleText', 'appendColumn', 'appendRow', 'appendRows', 'background',
        'checkState', 'child', 'clone', 'column', 'columnCount', 'data', 'emitDataChanged', 'flags', 'font',
        'foreground', 'hasChildren', 'icon', 'index', 'insertColumn', 'insertColumns', 'insertRow',
        'insertRows', 'isCheckable', 'isDragEnabled', 'isDropEnabled', 'isEditable', 'isEnabled',
        'isSelectable', 'isTristate', 'model', 'parent', 'read', 'removeColumn', 'removeColumns',
        'removeRow', 'removeRows', 'row', 'rowCount', 'setAccessibleDescription', 'setAccessibleText',
        'setBackground', 'setCheckState', 'setCheckable', 'setChild', 'setColumnCount', 'setData',
        'setDragEnabled', 'setDropEnabled', 'setEditable', 'setEnabled', 'setFlags', 'setFont',
        'setForeground', 'setIcon', 'setRowCount', 'setSelectable', 'setSizeHint', 'setStatusTip',
        'setText', 'setTextAlignment', 'setToolTip', 'setTristate', 'setWhatsThis', 'sizeHint', 'sortChildren',
        'statusTip', 'takeChild', 'takeColumn', 'takeRow', 'text', 'textAlignment', 'toolTip', 'type', 'whatsThis',
        'write']'''


        self.recursive_node(root_node, self.main_item)

        self.tmp_model.appendRow(self.main_item)
        self.update_model_tree()


    def recursive_node(self, root_node, item_in):

        for child_node in root_node.children:
            new_item = QStandardItem(str(child_node.name))

            new_item.idx = child_node.index  # testing
            new_item.setSelectable(True)     # testing

            new_item.setEditable(False)      # not letting the user edit it


            self.recursive_node(child_node, new_item)
            item_in.appendRow(new_item)


    def update_model_tree(self):

        self.setModel(self.tmp_model)
        self.expandAll()

    def item_clicked(self):

        print "item_clicked"
        #print "self.sender() =", self.sender()
        #print "dir(self.model.childEvent) =", dir(self.model.childEvent)

        print "self.senderSignalIndex() =", self.senderSignalIndex()
        #print "self.model.index ="

        dir_model_ = '''
        self.model Dr = ['__class__', '__delattr__', '__dict__', '__doc__', '__format__',
        '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__',
        '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'appendColumn',
        'appendRow', 'beginInsertColumns', 'beginInsertRows', 'beginMoveColumns', 'beginMoveRows',
        'beginRemoveColumns', 'beginRemoveRows', 'beginResetModel', 'blockSignals', 'buddy',
        'canFetchMore', 'changePersistentIndex', 'changePersistentIndexList', 'childEvent',
        'children', 'clear', 'columnCount', 'columnsAboutToBeInserted', 'columnsAboutToBeMoved',
        'columnsAboutToBeRemoved', 'columnsInserted', 'columnsMoved', 'columnsRemoved', 'connect',
        'connectNotify', 'createIndex', 'customEvent', 'data', 'dataChanged', 'decodeData', 'deleteLater',
        'destroyed', 'disconnect', 'disconnectNotify', 'dropMimeData', 'dumpObjectInfo', 'dumpObjectTree',
        'dynamicPropertyNames', 'emit', 'encodeData', 'endInsertColumns', 'endInsertRows', 'endMoveColumns',
        'endMoveRows', 'endRemoveColumns', 'endRemoveRows', 'endResetModel', 'event', 'eventFilter', 'fetchMore',
        'findChild', 'findChildren', 'findItems', 'flags', 'hasChildren', 'hasIndex', 'headerData', 'headerDataChanged',
        'horizontalHeaderItem', 'index', 'indexFromItem', 'inherits', 'insertColumn', 'insertColumns', 'insertRow',
        'insertRows', 'installEventFilter', 'invisibleRootItem', 'isWidgetType', 'item', 'itemChanged', 'itemData',
        'itemFromIndex', 'itemPrototype', 'killTimer', 'layoutAboutToBeChanged', 'layoutChanged', 'match',
        'metaObject', 'mimeData', 'mimeTypes', 'modelAboutToBeReset', 'modelReset', 'moveToThread',
        'objectName', 'parent', 'persistentIndexList', 'property', 'receivers', 'registerUserData',
        'removeColumn', 'removeColumns', 'removeEventFilter', 'removeRow', 'removeRows', 'reset',
        'resetInternalData', 'revert', 'roleNames', 'rowCount', 'rowsAboutToBeInserted', 'rowsAboutToBeMoved',
        'rowsAboutToBeRemoved', 'rowsInserted', 'rowsMoved', 'rowsRemoved', 'sender', 'senderSignalIndex',
        'setColumnCount', 'setData', 'setHeaderData', 'setHorizontalHeaderItem', 'setHorizontalHeaderLabels',
        'setItem', 'setItemData', 'setItemPrototype', 'setObjectName', 'setParent', 'setProperty', 'setRoleNames',
        'setRowCount', 'setSortRole', 'setSupportedDragActions', 'setVerticalHeaderItem', 'setVerticalHeaderLabels',
        'sibling', 'signalsBlocked', 'sort', 'sortRole', 'span', 'startTimer', 'staticMetaObject', 'submit',
        'supportedDragActions', 'supportedDropActions', 'takeColumn', 'takeHorizontalHeaderItem', 'takeItem',
        'takeRow', 'takeVerticalHeaderItem', 'thread', 'timerEvent', 'tr', 'trUtf8', 'verticalHeaderItem']
        '''


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

        self.tree_nav = TreeNavWidget()

        big_vbox.addWidget(self.tree_nav)

        self.btn_up =  QPushButton('\n    Up  \n', self)
        self.btn_up.clicked.connect(self.up_clicked)
        big_vbox.addWidget(self.btn_up)

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

        self.btn_dwn =  QPushButton('\n  Down \n', self)
        self.btn_dwn.clicked.connect(self.dwn_clicked)
        big_vbox.addWidget(self.btn_dwn)

        self.setLayout(big_vbox)
        self.setWindowTitle('Shell dialog')
        self.show()


    def up_clicked(self):
        print "up_clicked"
        print "self.curr_lin =", self.curr_lin
        self.controller.goto(self.lst_line_number[self.curr_lin - 2])
        print "...current.mode =", self.controller.get_current().name
        self._update_tree()

    def dwn_clicked(self):
        print "dw_clicked"
        print "self.curr_lin =", self.curr_lin
        self.controller.goto(self.lst_line_number[self.curr_lin])
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
        previous = current.parent
        print "current.index =", current.index
        print "previous.index =", previous.index

        self.lst_line_number = []

        for lst_num, single_line in enumerate(history.split("\n")):
            lst_data = single_line.lstrip().split(" ")

            if( len(lst_data) >=3 ):
                line_number = int(lst_data[0])
                self.lst_line_number.append(line_number)
                if( lst_data[len(lst_data) - 1] == "(current)" ):
                    self.curr_lin = lst_num

        self._update_gui_tree()
        print "self.curr_lin =", self.curr_lin
        print
        print " Ready to run >>", self.controller.get_mode()


    def _update_gui_tree(self):

        current = self.controller.get_current()

        lst_path_idx = [current.index]
        lst_path_cmd = [current.name]

        while current.index > 0:
            previous = current.parent

            lst_path_idx.insert(0, previous.index)
            lst_path_cmd.insert(0, previous.name)

            current = previous

        print "single_path(idx) =", lst_path_idx
        print "single_path(cmd) =", lst_path_cmd

        self.tree_nav.update_me(current)





if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())


