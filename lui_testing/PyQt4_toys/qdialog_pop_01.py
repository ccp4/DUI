import sys

from PySide.QtCore import *
from PySide.QtGui import *

example = '''
class AnalogClock(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AnalogClock, self).__init__(parent)
'''

class MyDialog(QDialog):
    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
        labl1 = QLabel("\n\n Hi QDialog \n\n")
        self.show()


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        btn = QPushButton(" pres ME")
        btn.clicked.connect(self.createDialog)

        self.setCentralWidget(btn)
        self.show()

    def createDialog(self):
        my_dialog= MyDialog()
        my_dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())


