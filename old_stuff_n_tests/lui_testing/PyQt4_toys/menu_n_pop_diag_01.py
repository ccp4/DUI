import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        fileMenu.addAction("Modal", self.openModal)
        fileMenu.addAction("Modeles", self.openModeles)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menubar')
        self.show()

    def openModal(self):
        print "open Modal Dialog"

        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog',
            'Enter your name:')

        if ok:
            print "self.le.setText(str(", text, "))"

    def openModeles(self):
        print "open Modeles Dialog"


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

