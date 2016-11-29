from PyQt4 import QtGui, QtCore
import sys

################################################################

class Layers(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Layers, self).__init__(parent)

class LayersMenu(QtGui.QMenu):

    def __init__(self, parent=None):
        super(LayersMenu, self).__init__(parent=parent)
        self.setStyleSheet('QMenu {'
                           '    border: 1px solid #ccc;'
                           '    background-color: #fbfbfb;'
                           '    border-radius: 4px;'
                           '    min-width: 400px;'
                           '}')
        layout = QtGui.QVBoxLayout(self)
        self.layers = Layers()
        layout.addWidget(self.layers)

    def sizeHint(self):
        return self.layers.sizeHint()

################################################################


class InnerWidg(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InnerWidg, self).__init__(parent)
        pushbutton = QtGui.QPushButton('Popup Button')
        menu = QtGui.QMenu()
        menu.addAction('This is Action 1', self.Action1)
        menu.addAction('This is Action 2', self.Action2)
        pushbutton.setMenu(LayersMenu())

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
