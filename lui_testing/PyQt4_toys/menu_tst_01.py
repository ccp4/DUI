import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        fileMenu.addAction("&Open...", self.openFile, "Ctrl+O")
        fileMenu.addAction("E&xit", self.quit, "Ctrl+Q")

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')
        self.show()

    def openFile(self):
        print "openFile"

    def quit(self):
        print "quit"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

