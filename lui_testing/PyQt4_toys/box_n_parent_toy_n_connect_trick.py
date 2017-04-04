import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class inner_widg( QWidget):
    def __init__(self, parent):
        super(inner_widg, self).__init__()
        self.parent_widget = parent

        self.btn_go =  QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.parent_widget.to_be_caled_from_son_widg)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.btn_go)
        self.setLayout(hbox)
        self.show()

class MainWidget( QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()

        self.inner_btn = inner_widg(self)
        hbox =  QHBoxLayout()
        hbox.addWidget(self.inner_btn)

        self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def to_be_caled_from_son_widg(self):
        print "from parent parent_widget"

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
