import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MyDialog(QDialog):
    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
        labl1 = QLabel("\n\n Hi QDialog \n\n")

        vbox = QVBoxLayout()
        vbox.addWidget(labl1)
        self.setLayout(vbox)
        self.setModal(True)
        self.show()

    def closeEvent(self, event):
        print "from << closeEvent  (QDialog) >>"

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

    def closeEvent(self, event):
        print "from << closeEvent  (QMainWindow) >>"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())


