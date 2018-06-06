#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Window(QWidget):

    valueChanged = pyqtSignal(int)

    def __init__(self):
        super(Window, self).__init__()

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMinimum(20)
        self.slider1.setMaximum(60)
        self.slider1.valueChanged[int].connect(self.print_value1)

        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMinimum(20)
        self.slider2.setMaximum(60)
        self.slider2.valueChanged[int].connect(self.print_value2)

        slidersLayout = QVBoxLayout()
        slidersLayout.addWidget(self.slider1)
        slidersLayout.addWidget(self.slider2)
        self.setLayout(slidersLayout)

    def print_value1(self, value):
        print "value1 =", value

        if(self.slider2.sliderPosition() > value):
            self.slider2.setValue(value)

    def print_value2(self, value):
        print "value2 =", value
        if(self.slider1.sliderPosition() < value):
            self.slider1.setValue(value)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
