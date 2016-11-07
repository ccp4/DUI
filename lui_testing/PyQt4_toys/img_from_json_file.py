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

    def __call__(self, flex_data_in, flex_mask_in, show_nums = False, i_min = -3.0, i_max = 200.0):

        err_code = self.wx_bmp_arr.set_min_max(i_min, i_max)
        #err_code = self.wx_bmp_arr.set_min_max(0.0, 1500.0)

        palette = "hot ascend"
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


def build_qimg(img_flex):
    arr_img = img_w_cpp()

    flex_2d_data = img_flex.as_double()
    flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
    arr_i = arr_img(flex_2d_data, flex_2d_mask, i_min = -3.0, i_max = 500)

    q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                   np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

    return q_img



class BigWidget(QWidget):
    def __init__(self):
        super(BigWidget, self).__init__()
        my_box = QVBoxLayout()
        self.my_painter = ImgPainter()

        json_file_path = "/home/luiso/dui/dui_test/X4_wide/test_02/dials-1/1_import/datablock.json"
        #json_file_path = "/home/lui/dui/dui_test/X4_wide/tst01/datablock.json"
        datablocks = DataBlockFactory.from_json_file(json_file_path)

        print "datablocks[0] =", datablocks[0]
        db = datablocks[0]
        self.my_sweep = db.extract_sweeps()[0]

        self.set_img_num(0)
        self.my_painter.set_img_pix(self.current_qimg )

        my_scrollable = ScrollableImg(self.my_painter)
        my_box.addWidget(my_scrollable)

        img_select = QComboBox()
        img_select.tmp_lst=[]
        for num in xrange(90):
            labl = "image number:" + str(num)
            img_select.tmp_lst.append(labl)

        for lst_itm in img_select.tmp_lst:
            img_select.addItem(lst_itm)

        img_select.setCurrentIndex(0)
        img_select.currentIndexChanged.connect(self.combobox_changed)
        my_box.addWidget(img_select)

        self.setLayout(my_box)
        self.show()

    def set_img_num(self, n_of_img):
        img_arr = self.my_sweep.get_raw_data(n_of_img)[0]
        print "img_arr.all() =", img_arr.all()
        self.current_qimg  = build_qimg(img_arr)

    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "Num =", value
        self.set_img_num(value)
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
