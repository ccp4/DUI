from PyQt4 import QtGui, QtCore
import sys
class PopMenu(QtGui.QMenu):
    def __init__(self, parent=None):
        super(PopMenu, self).__init__(parent)

        self.buttonadd = QtGui.QPushButton("Perform")
        self.rb_group = QtGui.QButtonGroup()
        self.rb_group_box = QtGui.QGroupBox()
        self.rb_group_box_layout = QtGui.QVBoxLayout()
        self.rb_group_box.setLayout(self.rb_group_box_layout)
        self.rb_hull = QtGui.QRadioButton("Hull")
        self.rb_group.addButton(self.rb_hull)
        self.rb_group_box_layout.addWidget(self.rb_hull)
        self.rb_minkowski = QtGui.QRadioButton("Minkowski")
        self.rb_group.addButton(self.rb_minkowski)
        self.rb_group_box_layout.addWidget(self.rb_minkowski)

        layouth=QtGui.QHBoxLayout()
        layouth.addWidget(self.buttonadd)
        layout= QtGui.QVBoxLayout()
        layout.addLayout(layouth)
        layout.addWidget(self.rb_group_box)
        self.setLayout(layout)



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
