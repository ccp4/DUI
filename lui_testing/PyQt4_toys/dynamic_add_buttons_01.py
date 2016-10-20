from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Main( QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)

        self.addButton =  QPushButton('button to add 3 QPushButtons')
        self.addButton.clicked.connect(self.addWidget)

        self.delButton =  QPushButton('button to remove one QPushButton')
        self.delButton.clicked.connect(self.delWidget)

        self.scrollLayout = QVBoxLayout()
        self.scrollLayout.setMargin(0)
        self.scrollLayout.setContentsMargins(QMargins(0,0,0,0))
        self.scrollLayout.setSpacing(0)

        self.scrollWidget =  QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        self.scrollArea =  QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.mainLayout =  QVBoxLayout()
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.delButton)
        self.mainLayout.addWidget(self.scrollArea)

        self.centralWidget =  QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.centralWidget)

    def delWidget(self):
        print "delWidget"

    def addWidget(self):
        lst_ops = []
        for lin in xrange(3):
            labl = str("op #" + str(lin) + "Pick me")
            new_op = QPushButton(labl)
            self.scrollLayout.addWidget(new_op)
            lst_ops.append(new_op)



if __name__ == "__main__":

    app =  QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()

