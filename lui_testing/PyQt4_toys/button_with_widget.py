from PyQt4 import QtGui, QtCore
import sys
'''
class Layers(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Layers, self).__init__(parent)
'''
class LayersMenu(QtGui.QMenu):

    def __init__(self, parent=None):
        super(LayersMenu, self).__init__(parent)
        layout = QtGui.QVBoxLayout(self)
        #self.layers = Layers()
        layout.addWidget(QtGui.QPushButton("Action1"))
        layout.addWidget(QtGui.QPushButton("Action2"))
        self.setLayout(layout)

    def Action1(self):
        print 'You selected Action 1'

    def Action2(self):
        print 'You selected Action 2'

class InnerWidg(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InnerWidg, self).__init__(parent)
        pushbutton = QtGui.QPushButton('Popup Button')
        pushbutton.setMenu(LayersMenu())

        vbox =  QtGui.QVBoxLayout()
        vbox.addWidget(pushbutton)

        self.setLayout(vbox)
        self.show()

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
