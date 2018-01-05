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

        self.busy_state = False

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
        if(self.busy_state == False):
            self.busy_state = True

            self.pbar.setText("working")
            self.pbar.start_motion()
            self.setCursor(QtCore.Qt.BusyCursor)

        else:
            self.busy_state = False

            self.pbar.setText("Stoped")
            self.pbar.end_motion()
            self.setCursor(QtCore.Qt.ArrowCursor)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

