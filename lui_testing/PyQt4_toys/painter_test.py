
from PySide import QtCore, QtGui


class AnalogClock(QtGui.QWidget):

    hourColor = QtGui.QColor(127, 0, 127)


    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)

        self.setWindowTitle("Painter test")
        self.resize(200, 200)

    def paintEvent(self, event):


        p = QtGui.QPainter()
        p.begin(self)
        p.drawLine(1,1,500,500)
        p.end()



if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())
