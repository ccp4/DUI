from PyQt4 import QtGui, QtCore
import sys

class InnerWidg(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InnerWidg, self).__init__(parent)
        pushbutton = QtGui.QPushButton('Popup Button')
        menu = QtGui.QMenu()
        menu.addAction('This is Action 1', self.Action1)
        menu.addAction('This is Action 2', self.Action2)
        pushbutton.setMenu(menu)

        vbox =  QtGui.QVBoxLayout()
        vbox.addWidget(pushbutton)

        self.setLayout(vbox)
        self.show()

    def Action1(self):
        print 'You selected Action 1'

    def Action2(self):
        print 'You selected Action 2'

class MainWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        only_widg = InnerWidg(self)
        self.setCentralWidget(only_widg)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main = MainWidget()
    main.show()
    app.exec_()
