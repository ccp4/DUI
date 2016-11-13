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

        self.img = None
        self.setMouseTracking(True)
        self.show()

        self.my_scale = 1.0

        self.img_width = 247
        self.img_height = 253
        self.resize(self.img_width * self.my_scale, self.img_height * self.my_scale)

        self.p_h_svar = self.my_parent.my_scrollable.horizontalScrollBar
        self.p_v_svar = self.my_parent.my_scrollable.verticalScrollBar

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            self.x_pos, self.y_pos = event.x(), event.y()

        elif event.buttons() == Qt.LeftButton:
            dx = event.x() - self.x_pos
            dy = event.y() - self.y_pos
            self.move_scrollbar(scrollBar = self.p_h_svar(), dst = dx)
            self.move_scrollbar(scrollBar = self.p_v_svar(), dst = dy)

        elif event.buttons() == Qt.RightButton:
            print "Right click drag"

    def wheelEvent(self, event):

        old_x = event.x()
        print "old_x =", old_x
        h_scr_bar = float(self.p_h_svar().value())
        print "h_scr_bar =", h_scr_bar

        old_y = event.y()
        print "old_y =", old_y
        v_scr_bar = float(self.p_v_svar().value())
        print "v_scr_bar =", v_scr_bar

        print "self.my_scale =", self.my_scale, "\n"

        if( event.delta() > 0 ):
            scale_factor = 1.1

        else:
            scale_factor = 0.9

        self.my_scale *= scale_factor
        h_new_pbar_pos = int(h_scr_bar * scale_factor)
        v_new_pbar_pos = int(v_scr_bar * scale_factor)

        self.rec = QRect(0, 0, self.img_width * self.my_scale, self.img_height * self.my_scale)
        self.update()

        self.move_scrollbar(scrollBar = self.p_h_svar(), new_pos = h_new_pbar_pos)
        self.move_scrollbar(scrollBar = self.p_v_svar(), new_pos = v_new_pbar_pos)


    def move_scrollbar(self, scrollBar = None, dst = None, new_pos = None):
        if( dst != None ):
            old_val = scrollBar.value()
            scrollBar.setValue(old_val - dst)

        if( new_pos != None ):
            scrollBar.setValue(new_pos)

    def set_img_pix(self, q_img = None):

        self.img = q_img

        self.img_width = q_img.width()
        self.img_height = q_img.height()
        self.rec = QRect(0, 0, self.img_width * self.my_scale,
                         self.img_height * self.my_scale)

        #replace <<update>> with <<paintEvent>> when [self] inherits from QGLWidget
        #self.paintEvent(None)

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

    def __call__ (self, img_flex, palette_in, min_i, max_i):
        flex_2d_data = img_flex.as_double()
        flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = min_i, i_max = max_i, palette = palette_in)

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

        self.img_select = QComboBox()
        self.my_scrollable = QScrollArea()
        self.my_painter = ImgPainter(self)
        self.my_scrollable.setWidget(self.my_painter)

        self.i_min = -3
        min_edit = QLineEdit()
        max_min_validator = QIntValidator(-5, 9995, self)
        min_edit.setValidator(max_min_validator)
        min_edit.setText(str(self.i_min))
        min_edit.textChanged.connect(self.min_changed_by_user)

        self.i_max = 100
        max_edit = QLineEdit()
        max_edit.setValidator(max_min_validator)
        max_edit.setText(str(self.i_max))
        max_edit.textChanged.connect(self.max_changed_by_user)

        palette_select = QComboBox()

        self.palette_lst = ["hot ascend", "hot descend", "black2white", "white2black"]
        self.palette = self.palette_lst[0]
        for plt in self.palette_lst:
            palette_select.addItem(plt)

        palette_select.currentIndexChanged.connect(self.palette_changed_by_user)


        self.img_num = 0
        self.current_qimg = build_qimg()

        if( json_file_path == None ):
            print "\n\n no datablock given \n\n"
            n_of_imgs = 1

        else:
            self.ini_datablock(json_file_path)

        self.img_select.setCurrentIndex(0)
        self.img_select.currentIndexChanged.connect(self.img_changed_by_user)

        btn_first =  QPushButton(' I< ')
        btn_first.clicked.connect(self.btn_first_clicked)
        btn_rev =  QPushButton(' << ')
        btn_rev.clicked.connect(self.btn_rev_clicked)
        btn_prev = QPushButton('  < ')
        btn_prev.clicked.connect(self.btn_prev_clicked)
        btn_next =  QPushButton(' >  ')
        btn_next.clicked.connect(self.btn_next_clicked)
        btn_ffw =  QPushButton(' >> ')
        btn_ffw.clicked.connect(self.btn_ffw_clicked)
        btn_last = QPushButton('  >I ')
        btn_last.clicked.connect(self.btn_last_clicked)

        top_box.addStretch()

        top_box.addWidget(QLabel("I min"))
        top_box.addWidget(min_edit)
        top_box.addWidget(QLabel("I max"))
        top_box.addWidget(max_edit)
        top_box.addWidget(palette_select)

        top_box.addWidget(btn_first)
        top_box.addWidget(btn_rev)
        top_box.addWidget(btn_prev)
        top_box.addWidget(self.img_select)
        top_box.addWidget(btn_next)
        top_box.addWidget(btn_ffw)
        top_box.addWidget(btn_last)

        my_box.addLayout(top_box)



        my_box.addWidget(self.my_scrollable)

        self.setLayout(my_box)
        self.show()


    def ini_datablock(self, json_file_path):

        datablocks = DataBlockFactory.from_json_file(json_file_path)
        #TODO check length of datablock for safety

        db = datablocks[0]
        self.my_sweep = db.extract_sweeps()[0]
        self.img_select.clear()
        print"\n self.my_sweep.get_array_range() =", self.my_sweep.get_array_range()
        print "self.my_sweep.get_array_range() =", self.my_sweep.get_array_range()
        print "self.my_sweep.get_image_size() =", self.my_sweep.get_image_size()
        n_of_imgs = len(self.my_sweep.indices())
        print "n_of_imgs =", n_of_imgs

        self.img_select.setMaxCount(n_of_imgs)
        for num in xrange(n_of_imgs):
            labl = "img#" + str(num + 1)
            self.img_select.addItem(labl)

        self.set_img()

    def set_img(self):

        print "New self.img_num =", self.img_num

        firts_time = time_now()
        self.img_arr = self.my_sweep.get_raw_data(self.img_num)[0]
        self.my_painter.set_img_pix(self.current_qimg(self.img_arr, self.palette, self.i_min, self.i_max))
        print "diff time =", time_now() - firts_time, "\n"

    def min_changed_by_user(self, value):
        try:
            self.i_min = int(value)
        except:
            self.i_min = 0
        self.set_img()

    def max_changed_by_user(self, value):
        try:
            self.i_max = int(value)
        except:
            self.i_max = 0
        self.set_img()

    def palette_changed_by_user(self, new_palette_num):
        self.palette = self.palette_lst[new_palette_num]
        self.set_img()


    def btn_first_clicked(self):
        self.img_num = 0
        self.img_select.setCurrentIndex(self.img_num)

    def btn_rev_clicked(self):
        self.img_num -= 10
        if( self.img_num < 0 ):
            self.img_num = 0
        self.img_select.setCurrentIndex(self.img_num)

    def btn_prev_clicked(self):
        self.img_num -= 1
        if( self.img_num < 0 ):
            self.img_num = 0
        self.img_select.setCurrentIndex(self.img_num)

    def btn_next_clicked(self):
        self.img_num += 1
        if( self.img_num >= self.img_select.maxCount() ):
            self.img_num = self.img_select.maxCount() - 1
        self.img_select.setCurrentIndex(self.img_num)

    def btn_ffw_clicked(self):
        self.img_num += 10
        if( self.img_num >= self.img_select.maxCount() ):
            self.img_num = self.img_select.maxCount() - 1
        self.img_select.setCurrentIndex(self.img_num)

    def btn_last_clicked(self):
        self.img_num = self.img_select.maxCount() - 1
        self.img_select.setCurrentIndex(self.img_num)

    def img_changed_by_user(self, value):
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

