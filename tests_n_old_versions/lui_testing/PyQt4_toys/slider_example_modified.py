#!/usr/bin/env python

from PyQt4 import QtCore, QtGui

class SlidersGroup(QtGui.QGroupBox):

    valueChanged = QtCore.pyqtSignal(int)

    def __init__(self, title, parent=None):
        super(SlidersGroup, self).__init__(title, parent)

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


class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.horizontalSliders = SlidersGroup("Horizontal")

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.horizontalSliders)
        self.setLayout(layout)
        self.setWindowTitle("Sliders")


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
