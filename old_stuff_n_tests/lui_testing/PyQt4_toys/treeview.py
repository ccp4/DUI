from PySide.QtGui import *
from PySide.QtCore import *
import sys

app = QApplication(sys.argv)
# Our main window will be a QTreeView
tree = QTreeView()
tree.setWindowTitle('Example List')
tree.setMinimumSize(600, 400)

model = QStandardItemModel(tree)

lst_nums = [
    'Uno',
    'Dos',
    'Tres',
    'Cuatro',
    'Cinco'
]

for num, elem_num in enumerate(lst_nums):

    item = QStandardItem(elem_num)
    for n_num in xrange(num):
        tst_new_item_01 = QStandardItem(str(n_num))
        item.appendRow(tst_new_item_01)

    model.appendRow(item)

tree.setModel(model)
tree.show()
sys.exit(app.exec_())
