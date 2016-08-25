# -*- coding: utf-8 -*-
"""
Demonstrates very basic use of ImageItem to display image data inside a ViewBox.
"""


from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg
import pyqtgraph.ptime as ptime

from benchmarking_speeds_np_arr_paints import get_3d_flex_array

app = QtGui.QApplication([])

## Create window with GraphicsView widget
win = pg.GraphicsLayoutWidget()
win.show()  ## show widget alone in its own window
win.setWindowTitle('pyqtgraph example: ImageItem')
view = win.addViewBox()

## lock the aspect ratio so pixels are always square
view.setAspectLocked(True)

## Create image item
img = pg.ImageItem(border='w')
view.addItem(img)

## Set initial view bounds
view.setRange(QtCore.QRectF(0, 0, 2500, 2400))

## Create random image
#data = np.random.normal(size=(5, 2500, 2400), loc=1024, scale=64).astype(np.uint16)
#data = np.random.normal(size=(5, 2500, 2400)).astype(np.double)

arr_data = get_3d_flex_array()

print arr_data.all()

i = 0
updateTime = ptime.time()



def updateData():
    #global img, data, i, updateTime
    global img, arr_data, i, updateTime


    ## Display the data
    #img.setImage(data[i])

    all_1 = arr_data.all()[1]
    all_2 = arr_data.all()[2]
    flex_slice_2d = arr_data[i:i+1, 0:all_1, 0:all_2]

    np_slice = flex_slice_2d.as_numpy_array()
    img_np = np.zeros([all_1, all_2], dtype=np.double)
    img_np[:,:] = np_slice[0:1,:,:]

    img.setImage(img_np)

    i += 1
    if i >= arr_data.all()[0]:
        i = 0

    QtCore.QTimer.singleShot(1, updateData)
    now = ptime.time()

    dif_time = updateTime - now
    updateTime = now

    print "dif_time =", dif_time




updateData()

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
