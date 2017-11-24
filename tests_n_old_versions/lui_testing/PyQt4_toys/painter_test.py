
from PySide import QtCore, QtGui


class AnalogClock(QtGui.QWidget):

    hourColor = QtGui.QColor(127, 0, 127)


    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        self.setWindowTitle("Painter test")
        self.resize(200, 200)

    def paintEvent(self, event):


        img_paint = QtGui.QPainter()
        img_paint.begin(self)

        img = QtGui.QImage("tux_n_chrome.png")
        Pmap = QtGui.QPixmap.fromImage(img)

        img_paint.drawPixmap(1, 1, Pmap)


        img_paint.end()



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())
