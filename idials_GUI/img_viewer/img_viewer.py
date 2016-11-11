import sys, os
import numpy as np
from dxtbx.datablock import DataBlockFactory
from dials.array_family import flex
from dials_viewer_ext import rgb_img
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from time import time as time_now


class img_w_cpp(object):
    def __init__(self):
        self.wx_bmp_arr = rgb_img()

    def __call__(self, flex_data_in, flex_mask_in, show_nums = False,
                 i_min = -3.0, i_max = 200.0, palette = "hot ascend"):

        err_code = self.wx_bmp_arr.set_min_max(i_min, i_max)

        if palette == "black2white":
            palette_num = 1
        elif palette == "white2black":
            palette_num = 2
        elif palette == "hot ascend":
            palette_num = 3
        else: # assuming "hot descend"
            palette_num = 4

        img_array_tmp = self.wx_bmp_arr.gen_bmp(flex_data_in, flex_mask_in, show_nums, palette_num)

        np_img_array = img_array_tmp.as_numpy_array()

        height = np.size(np_img_array[:, 0:1, 0:1])
        width = np.size( np_img_array[0:1, :, 0:1])

        img_array = np.zeros([height, width, 4], dtype=np.uint8)

        #for some strange reason PyQt4 needs to use RGB as BGR
        img_array[:,:,0:1] = np_img_array[:,:,2:3]
        img_array[:,:,1:2] = np_img_array[:,:,1:2]
        img_array[:,:,2:3] = np_img_array[:,:,0:1]

        return img_array



class ImgPainter(QWidget):

    def __init__(self, parent = None):
        super(ImgPainter, self).__init__()

        self.my_parent = parent

        #self.setFixedSize(2550, 2400)


        self.img = None
        self.setMouseTracking(True)
        self.show()

        self.my_scale = 1.0

        self.img_width = 2463
        self.img_height = 2527

        self.rec = QRect(0, 0, self.img_width * self.my_scale, self.img_height * self.my_scale)
        self.resize(self.img_width * self.my_scale, self.img_height * self.my_scale)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            self.x_pos, self.y_pos = event.x(), event.y()

        elif event.buttons() == Qt.LeftButton:
            dx = event.x() - self.x_pos
            dy = event.y() - self.y_pos
            self.adjustScrollBar(self.my_parent.my_scrollable.horizontalScrollBar(), dx)
            self.adjustScrollBar(self.my_parent.my_scrollable.verticalScrollBar(), dy)

        elif event.buttons() == Qt.RightButton:
            print "Right click drag"

    def wheelEvent(self, event):
        #print "wheelEvent()"
        #print "event.delta() =", event.delta()

        if( event.delta() > 0 ):
            #print "Up"
            self.my_scale = self.my_scale + 0.1

        elif( event.delta() < 0 ):
            #print "Down"
            self.my_scale = self.my_scale - 0.1

        self.rec = QRect(0, 0, self.img_width * self.my_scale, self.img_height * self.my_scale)
        self.update()


    def adjustScrollBar(self, scrollBar, delta):

        old_val = scrollBar.value()
        scrollBar.setValue(old_val - delta)


    def set_img_pix(self, q_img = None):

        self.img = q_img
        #self.setFixedSize(2550, 2400)
        #self.resize(self.img.size())


        #print "self.img.size() =", self.img.size()

        #print "dir(self.img)", dir(self.img)

        # the next two choices need to be taken depending on the
        # rendering back end

        # Use paintEvent when [self] inherits from QGLWidget
        #self.paintEvent(None)

        #Use "update" when [self] inherits from QWidget
        self.update()
        #in future consider *self.repaint()* for the video thing or instead of *self.update()*

    def paintEvent(self, event):
        if( self.img == None ):
            return

        else:
            self.resize(self.img_width * self.my_scale, self.img_height * self.my_scale)
            img_paint = QPainter()
            img_paint.begin(self)
            img_paint.drawImage(self.rec, self.img)
            img_paint.end()


class build_qimg(object):
    def __init__(self):
        self.arr_img = img_w_cpp()

    def __call__ (self, img_flex, palette):
        flex_2d_data = img_flex.as_double()
        flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = 0.0, i_max = 100, palette = palette)

        q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

        return q_img


class MyImgWin(QWidget):
    def __init__(self, json_file_path = None):
        super(MyImgWin, self).__init__()
        my_box = QVBoxLayout()
        top_box = QHBoxLayout()
        left_top_box = QVBoxLayout()
        right_top_box = QVBoxLayout()

        self.my_painter = ImgPainter(self)
        self.img_select = QComboBox()

        self.palette_lst = ["hot ascend", "hot descend", "black2white", "white2black"]
        self.palette = self.palette_lst[0]
        self.img_num = 0
        self.current_qimg = build_qimg()

        if( json_file_path == None ):
            print "\n\n no datablock given \n\n"
            n_of_imgs = 1

        else:
            self.ini_datablock(json_file_path)

        self.img_select.setCurrentIndex(0)
        self.img_select.currentIndexChanged.connect(self.img_changed_by_user)

        palette_select = QComboBox()

        for plt in self.palette_lst:
            palette_select.addItem(plt)

        palette_select.currentIndexChanged.connect(self.palette_changed_by_user)

        left_top_box.addWidget(palette_select)
        top_box.addLayout(left_top_box)

        right_top_box.addWidget(self.img_select)
        top_box.addLayout(right_top_box)

        my_box.addLayout(top_box)

        self.my_scrollable = QScrollArea()
        self.my_scrollable.setWidget(self.my_painter)

        my_box.addWidget(self.my_scrollable)

        self.setLayout(my_box)
        self.show()


    def ini_datablock(self, json_file_path):

        datablocks = DataBlockFactory.from_json_file(json_file_path)
        #TODO check length of datablock

        db = datablocks[0]
        self.my_sweep = db.extract_sweeps()[0]
        self.img_select.clear()

        print "self.my_sweep.get_array_range() =", self.my_sweep.get_array_range()
        print "self.my_sweep.get_image_size() =", self.my_sweep.get_image_size()

        n_of_imgs = self.my_sweep.get_array_range()[1]
        print "n_of_imgs =", n_of_imgs

        for num in xrange(n_of_imgs):
            labl = "image number:" + str(num)
            self.img_select.addItem(labl)


        self.set_img()

    def set_img(self):
        firts_time = time_now()
        self.img_arr = self.my_sweep.get_raw_data(self.img_num)[0]
        self.my_painter.set_img_pix(self.current_qimg(self.img_arr, self.palette))
        print "diff time =", time_now() - firts_time, "\n"

    def palette_changed_by_user(self, new_palette_num):
        self.palette = self.palette_lst[new_palette_num]
        self.set_img()

    def img_changed_by_user(self, value):
        sender = self.sender()
        self.img_num = value
        self.set_img()


if( __name__ == "__main__" ):

    app = QApplication(sys.argv)
    print "sys.argv =", sys.argv
    if( len(sys.argv) > 1 ):
        img_path = sys.argv[1]
    else:
        img_path = None

    print "img_path =", img_path

    diag = MyImgWin(img_path)
    sys.exit(app.exec_())
    app.exec_()

