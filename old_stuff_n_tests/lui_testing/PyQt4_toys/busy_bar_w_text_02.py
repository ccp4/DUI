from PySide import QtGui, QtCore
import sys



class MyProgressBar(QtGui.QProgressBar):

    def __init__(self, parent):
        super(MyProgressBar,self).__init__()
        self.setRange(0, 0)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self._text = None

    def setText(self, text):
        self._text = text

    def text(self):
        return self._text



class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.pbar = MyProgressBar(self)
        self.pbar.setText('finding resource...')

        self.btn = QtGui.QPushButton('Start', self)
        self.btn.clicked.connect(self.doAction)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.btn)
        hbox.addWidget(self.pbar)
        self.setLayout(hbox)

        self.setWindowTitle('QtGui.QProgressBar')
        self.show()


    def doAction(self):
        self.pbar.setText("working")



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

