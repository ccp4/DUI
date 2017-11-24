from PySide.QtGui import *
from PySide.QtCore import *
import sys

# Create a Qt application
app = QApplication(sys.argv)

# Our main window will be a QListView
list = QListView()
list.setWindowTitle('Example List')
list.setMinimumSize(600, 400)

# Create an empty model for the list's data
model = QStandardItemModel(list)

# Add some textual items
foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]

for food in foods:
    # create an item with a caption
    item = QStandardItem(food)

    # add a checkbox to it
    item.setCheckable(True)

    # Add the item to the model
    model.appendRow(item)

# Apply the model to the list view
list.setModel(model)

# Show the window and run the app
list.show()
#app.exec_()
sys.exit(app.exec_())
