from PySide import QtGui, QtCore
import sys



class Text_w_Bar(QtGui.QProgressBar):
    def __init__(self, parent = None):
        super(Text_w_Bar,self).__init__()
        self.setAlignment(QtCore.Qt.AlignCenter)
        self._text = ""

    def setText(self, text):
        self._text = text
        self.repaint()

    def text(self):
        return self._text

    def start_motion(self):
        print "starting motion"
        self.setRange(0, 0)

    def end_motion(self):
        self.setRange(0, 1)
        print "ending motion"


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.pbar = Text_w_Bar(self)
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
        self.pbar.start_motion()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

