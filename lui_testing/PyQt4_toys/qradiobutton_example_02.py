from PyQt4 import QtGui, QtCore
import sys
class PopMenu(QtGui.QMenu):
    def __init__(self, parent=None):
        super(PopMenu, self).__init__(parent)

        self.rb_group = QtGui.QButtonGroup()
        self.rb_group_box = QtGui.QGroupBox()
        self.rb_group_box_layout = QtGui.QVBoxLayout()
        self.rb_group_box.setLayout(self.rb_group_box_layout)

        self.rb_01 = QtGui.QRadioButton("Show all HKLs")
        self.rb_group.addButton(self.rb_01)
        self.rb_01.clicked.connect(self.Action1)
        self.rb_group_box_layout.addWidget(self.rb_01)

        self.rb_02 = QtGui.QRadioButton("Show Only Nearest HKL")
        self.rb_group.addButton(self.rb_02)
        self.rb_02.clicked.connect(self.Action2)
        self.rb_group_box_layout.addWidget(self.rb_02)

        self.rb_03 = QtGui.QRadioButton("No HKL shown")
        self.rb_group.addButton(self.rb_03)
        self.rb_03.clicked.connect(self.Action3)
        self.rb_group_box_layout.addWidget(self.rb_03)


        layout= QtGui.QVBoxLayout()
        layout.addWidget(self.rb_group_box)
        self.setLayout(layout)

    def Action1(self):
        print "buttn 1"

    def Action2(self):
        print "buttn 2"

    def Action3(self):
        print "buttn 3"


class InnerWidg(QtGui.QWidget):
    def __init__(self, parent=None):
        super(InnerWidg, self).__init__(parent)
        pushbutton = QtGui.QPushButton("Popup Button")
        pushbutton.setMenu(PopMenu())

        vbox =  QtGui.QVBoxLayout()
        vbox.addWidget(pushbutton)

        self.setLayout(vbox)
        self.show()


class MainWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        only_widg = InnerWidg(self)
        self.setCentralWidget(only_widg)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWidget()
    main.show()
    app.exec_()
