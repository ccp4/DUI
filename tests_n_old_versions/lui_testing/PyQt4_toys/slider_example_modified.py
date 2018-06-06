#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

class Window(QtGui.QWidget):

    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self):
        super(Window, self).__init__()

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)

        self.slider.setMinimum(20)
        self.slider.setMaximum(60)

        self.slider.valueChanged[int].connect(self.print_value)

        direction = QtGui.QBoxLayout.TopToBottom

        slidersLayout = QtGui.QBoxLayout(direction)
        slidersLayout.addWidget(self.slider)
        self.setLayout(slidersLayout)

    def print_value(self, value):
        print "value =", value


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
