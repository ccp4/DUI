#from subprocess import call as shell_func
import subprocess
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        percentSpinBox = QDoubleSpinBox()
        percentSpinBox.setRange(0, 1000)
        percentSpinBox.setSingleStep(10)
        percentSpinBox.setSuffix("%")
        percentSpinBox.setSpecialValueText(str("Automatic"))

        vbox = QVBoxLayout()
        vbox.addWidget(percentSpinBox)

        self.setGeometry(1200, 200, 450, 350)
        self.setLayout(vbox)
        self.setWindowTitle('Shell dialog')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
