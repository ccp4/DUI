from PySide.QtGui import *
from PySide.QtCore import *
import sys

# Create a Qt application
app = QApplication(sys.argv)

# Our main window will be a QTreeView
tree = QTreeView()
tree.setWindowTitle('Example List')
tree.setMinimumSize(600, 400)

model = QStandardItemModel(tree)

foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]

for num, food in enumerate(foods):

    tst_new_item = QStandardItem(str(num))

    item = QStandardItem(food)
    item.appendRow(tst_new_item)
    model.appendRow(item)

# Apply the model to the tree view
tree.setModel(model)

# Show the window and run the app
tree.show()
#app.exec_()
sys.exit(app.exec_())
