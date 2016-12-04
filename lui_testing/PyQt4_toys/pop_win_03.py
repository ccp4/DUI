import sys
#from PyQt4.Qt import *

from PySide.QtCore import *
from PySide.QtGui import *

example = '''
class MyDialog(QDialog):
    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
'''
class MyPopup(QWidget):
    def __init__(self, parent = None):
        super(MyPopup, self).__init__(parent)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)

    def closeEvent(self, event):
        print "<< closeEvent ( from QWidget) >>"


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.btn1 = QPushButton("Click me", self.cw)
        self.btn1.setGeometry(QRect(0, 0, 100, 30))
        self.connect(self.btn1, SIGNAL("clicked()"), self.doit)
        self.w = None

    def doit(self):
        print "Opening a new popup window"
        self.w = MyPopup()
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.show()

    def closeEvent(self, event):
        print "<< closeEvent ( from QMainWindow) >>"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
