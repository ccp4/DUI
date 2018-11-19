from subprocess import call as shell_func
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class inner_widg1( QWidget):

    goClicked = pyqtSignal()
    txt_changed = pyqtSignal(str)

    def __init__(self, parent):
        super(inner_widg1, self).__init__()
        self.parent_widget = parent

        self.line_ed1 = QLineEdit()
        self.line_ed1.setText("")
        self.line_ed1.textChanged.connect(self.line1_txt_changed)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.line_ed1)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setLayout(bg_box)
        self.show()

    def line1_txt_changed(self):
        new_str = str(self.line_ed1.text())
        self.txt_changed.emit(new_str)


class inner_widg2( QWidget):

    goClicked = pyqtSignal()
    txt_changed = pyqtSignal(str)

    def __init__(self, parent):
        super(inner_widg2, self).__init__()
        self.parent_widget = parent

        self.line_ed2 = QLineEdit()
        self.line_ed2.setText("")
        self.line_ed2.textChanged.connect(self.line2_txt_changed)

        hbox =  QHBoxLayout()
        hbox.addWidget(self.line_ed2)

        bg_box =  QVBoxLayout(self)
        bg_box.addLayout(hbox)

        self.setLayout(bg_box)
        self.show()

    def line2_txt_changed(self):
        new_str = str(self.line_ed2.text())
        self.txt_changed.emit(new_str)


class MainWidget( QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        self.in_widg1 = inner_widg1(self)
        self.in_widg1.txt_changed.connect(self.on_txt_changed)

        self.in_widg2 = inner_widg2(self)
        self.in_widg2.txt_changed.connect(self.on_txt_changed)
        hbox =  QHBoxLayout()

        hbox.addWidget(self.in_widg1)
        hbox.addWidget(self.in_widg2)

        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

    def on_txt_changed(self, txt):
        print "new_str =", txt

        self.in_widg1.line_ed1.setText(txt)
        self.in_widg2.line_ed2.setText(txt)

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())

