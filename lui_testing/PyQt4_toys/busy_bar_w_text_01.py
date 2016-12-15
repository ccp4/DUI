from PySide import QtGui, QtCore

class MyProgressBar(QtGui.QProgressBar):


    def __init__(self):
        super(MyProgressBar,self).__init__()
        self.setRange(0, 0)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self._text = None

    def setText(self, text):
        self._text = text

    def text(self):
        return self._text

app = QtGui.QApplication([])

p = MyProgressBar()
p.setText('finding resource...')
p.show()

app.exec_()