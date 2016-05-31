
from PySide import QtCore, QtGui

import numpy as np


class MyScroll(QtGui.QScrollArea):

    def __init__(self, parent = None):
        super(MyScroll, self).__init__()

        self.imageLabel = QtGui.QLabel()

        width = 100
        height = 100
        data = np.random.randint(0,256,size=(width,height,3)).astype(np.uint8)

        img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
        for x in xrange(width):
            for y in xrange(height):
                img.setPixel(x, y, QtGui.QColor(*data[x][y]).rgb())

        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(img))
        self.setWidget(self.imageLabel)
        self.show()


    def update_me(self, img_list = None):
        print "update_me(self)"
        self.imageLabel = QtGui.QLabel()
        self.image = QtGui.QImage("centroid_rmsd_vs_phi.png")
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.setWidget(self.imageLabel)
        self.show()


class ImgTab(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ImgTab, self).__init__()

        self.scrollArea = MyScroll(self)
        main_box = QtGui.QVBoxLayout()
        self.btn_go = QtGui.QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        main_box.addWidget(self.btn_go)
        main_box.addWidget(self.scrollArea)

        self.setLayout(main_box)
        self.show()

    def B_go_clicked(self):
        print "B_go_clicked(self)"
        self.scrollArea.update_me()

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    frame = ImgTab()
    sys.exit(app.exec_())
