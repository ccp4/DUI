from PySide import QtGui
import numpy as np
import pyqtgraph as pg

## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

## Define a top-level widget to hold everything
w = QtGui.QWidget()

## Create some widgets to be placed inside
btn = QtGui.QPushButton('press me')
text = QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()


arr_i = np.arange(400 * 400).reshape(400, 400)

imv = pg.ImageView()
#imv.show()
imv.setImage(arr_i)

plot = pg.PlotWidget()




## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(btn, 0, 0)   # button goes in upper-left
layout.addWidget(text, 1, 0)   # text edit goes in middle-left
layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
#layout.addWidget(plot, 0, 1, 3, 1)  # plot goes on right side, spanning 3 rows
layout.addWidget(imv, 0, 1, 3, 1)
## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()
