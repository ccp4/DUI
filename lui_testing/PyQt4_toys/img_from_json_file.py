import sys, os
import numpy as np
from dxtbx.datablock import DataBlockFactory
from dials.array_family import flex
from dials_viewer_ext import rgb_img
from PyQt4.QtGui import *
from PyQt4.QtCore import *

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



class ScrollableImg(QScrollArea):
    def __init__(self, parent = None):
        super(ScrollableImg, self).__init__()
        self.setWidget(parent)


class ImgPainter(QWidget):

    def __init__(self):
        super(ImgPainter, self).__init__()
        self.setFixedSize(2550, 2400)
        #self.pix = None
        self.img = None
        self.show()

    def set_img_pix(self, q_img = None):

        #self.pix = QPixmap.fromImage(q_img)
        self.img = q_img
        # the next two choices need to be taken depending on the
        # rendering back end

        # Use paintEvent when [self] inherits from QGLWidget
        #self.paintEvent(None)

        #Use "update" when [self] inherits from QWidget
        self.update()

        #in future consider *self.repaint()* for the video thing or instead of *self.update()*


    def paintEvent(self, event):
        if( self.img == None ):
            print "self.img = None"
            return

        else:
            img_paint = QPainter()
            img_paint.begin(self)
            img_paint.drawImage(0, 0, self.img)
            img_paint.end()


def build_qimg(img_flex, palette):
    arr_img = img_w_cpp()

    #TODO remember that the previous line needs to run only once


    flex_2d_data = img_flex.as_double()
    flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
    arr_i = arr_img(flex_2d_data, flex_2d_mask, i_min = 0.0, i_max = 100, palette = palette)

    q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                   np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

    return q_img



class BigWidget(QWidget):
    def __init__(self):
        super(BigWidget, self).__init__()
        my_box = QVBoxLayout()
        top_box = QHBoxLayout()
        left_top_box = QVBoxLayout()
        right_top_box = QVBoxLayout()

        self.my_painter = ImgPainter()

        #json_file_path = "/home/luiso/dui/dui_test/only_9_img/dui_idials_tst_04/dials-1/1_import/datablock.json"
        json_file_path = "/home/luiso/dui/dui_test/X4_wide/test_02/dials-1/1_import/datablock.json"
        #json_file_path = "/home/lui/dui/dui_test/X4_wide/tst01/datablock.json"

        datablocks = DataBlockFactory.from_json_file(json_file_path)
        db = datablocks[0]
        self.my_sweep = db.extract_sweeps()[0]

        print "self.my_sweep.get_array_range() =", self.my_sweep.get_array_range()
        print "self.my_sweep.get_image_size() =", self.my_sweep.get_image_size()

        n_of_imgs = self.my_sweep.get_array_range()[1]
        print "n_of_imgs =", n_of_imgs

        self.set_img_num(0, "hot ascend")
        self.my_painter.set_img_pix(self.current_qimg )

        my_scrollable = ScrollableImg(self.my_painter)


        img_select = QComboBox()

        for num in xrange(n_of_imgs):
            labl = "image number:" + str(num)
            img_select.addItem(labl)

        img_select.setCurrentIndex(0)
        img_select.currentIndexChanged.connect(self.img_changed_by_user)

        palette_select = QComboBox()

        self.palette_lst = ["hot ascend", "hot descend", "black2white", "white2black"]
        for plt in self.palette_lst:
            palette_select.addItem(plt)

        palette_select.currentIndexChanged.connect(self.palette_changed_by_user)

        left_top_box.addWidget(palette_select)
        top_box.addLayout(left_top_box)

        right_top_box.addWidget(img_select)
        top_box.addLayout(right_top_box)

        my_box.addLayout(top_box)
        my_box.addWidget(my_scrollable)

        self.setLayout(my_box)
        self.show()

    def set_img_num(self, img_n, palette):
        self.img_arr = self.my_sweep.get_raw_data(img_n)[0]
        print "self.img_arr.all() =", self.img_arr.all()
        self.current_qimg  = build_qimg(self.img_arr, palette)

    def palette_changed_by_user(self, new_palette_num):
        print "palette_num =", new_palette_num
        print "palette =", self.palette_lst[new_palette_num]
        self.current_qimg  = build_qimg(self.img_arr, self.palette_lst[new_palette_num])
        self.my_painter.set_img_pix(self.current_qimg)


    def img_changed_by_user(self, value):
        sender = self.sender()
        print "Num =", value

        self.set_img_num(value, "hot ascend")
        self.my_painter.set_img_pix(self.current_qimg)


if( __name__ == "__main__" ):

    app = QApplication(sys.argv)
    ex = BigWidget()
    sys.exit(app.exec_())


    old_example = '''
    datablocks = DataBlockFactory.from_json_file("/home/luiso/dui/dui_test/X4_wide/test_02/dials-1/1_import/datablock.json")
    print "datablocks[0] =", datablocks[0]
    db=datablocks[0]

    sw=db.extract_sweeps()[0]

    print "sw.get_raw_data(0) =", sw.get_raw_data(0)
    print "sw.get_raw_data(1) =", sw.get_raw_data(1)
    print "sw.get_raw_data(2) =", sw.get_raw_data(2)

    img_arr=sw.get_raw_data(0)[0]

    print "img_arr.all() =", img_arr.all()

    app = QApplication(sys.argv)
    ex = ImgPainter()

    q_img = build_qimg(img_arr)

    ex.set_img_pix(q_img)
    '''
