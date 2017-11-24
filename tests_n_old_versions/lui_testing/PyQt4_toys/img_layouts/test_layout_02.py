
from PySide import QtCore, QtGui


class ImgWidg(QtGui.QWidget):
    def __init__(self, parent = None, img_path_lst = None):
        super(ImgWidg, self).__init__()

        bg_box =  QtGui.QVBoxLayout(self)
        for single_img_path in img_path_lst:

            imageLabel = QtGui.QLabel()
            image = QtGui.QImage(single_img_path)
            imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))

            bg_box.addWidget(imageLabel)

        self.setLayout(bg_box)
        self.show()


class MyScroll(QtGui.QScrollArea):

    def __init__(self, parent = None, lst_img = None):
        super(MyScroll, self).__init__()

        self.imageWidg = ImgWidg(self, lst_img)
        self.setWidget(self.imageWidg)
        self.show()

    def update_me(self, lst_img = None):
        print "update_me(self)"

        self.imageWidg = ImgWidg(self, lst_img)
        self.setWidget(self.imageWidg)
        self.show()


class ImgTab(QtGui.QWidget):

    def __init__(self, parent = None):
        super(ImgTab, self).__init__()


        self.lst_tmp1 = ["centroid_diff_x.png", "centroid_diff_z.png", "centroid_rmsd_vs_phi.png"]
        self.lst_tmp2 = ["centroid_xz_residuals.png", "centroid_diff_hist.png", "centroid_diff_y.png"]
        self.lst_tmp3 = ["centroid_mean_diff_vs_phi.png", "centroid_xy_residuals.png"]
        self.lst_tmp4 = ["centroid_zy_residuals.png"]

        self.scrollArea = MyScroll(self, self.lst_tmp1)
        main_box = QtGui.QVBoxLayout()
        self.btn_go = QtGui.QPushButton('\n      Go   \n', self)
        self.btn_go.clicked.connect(self.B_go_clicked)

        main_box.addWidget(self.btn_go)
        main_box.addWidget(self.scrollArea)

        self.setLayout(main_box)
        self.show()

    def B_go_clicked(self):

        print "B_go_clicked(self)"
        self.scrollArea.update_me(self.lst_tmp2)




if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    frame = ImgTab()
    sys.exit(app.exec_())
