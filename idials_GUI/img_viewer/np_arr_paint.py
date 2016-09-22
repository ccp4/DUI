from PySide.QtCore import *
from PySide.QtGui import *

import numpy as np
from dxtbx.datablock import DataBlockFactory
from dials.array_family import flex
import sys
from time import time as time_now

from data_2_img import img_w_cpp

def get_3d_flex_array():
    json_file_path = str("dials-1/1_import/datablock.json")
    print "json_file_path =", json_file_path

    datablocks = DataBlockFactory.from_json_file(json_file_path)

    if len(datablocks) > 0:
        assert(len(datablocks) == 1)
        imagesets = datablocks[0].extract_imagesets()
        crystals = None
        print "len(datablocks) > 0"

    else:
        raise RuntimeError("No imageset could be constructed")

    print "len(imagesets) =", len(imagesets)
    print "type(imagesets) =", type(imagesets)
    first_data = imagesets[0]
    print "type(first_data) =", type(first_data)
    my_array = first_data.to_array()
    print "type(my_array) =", type(my_array)
    my_array_double = my_array.as_double()

    print "my_array_double.all() =", my_array_double.all()

    return my_array_double


class MyScroll( QScrollArea):

    my_time = time_now()

    def __init__(self, parent = None):
        super(MyScroll, self).__init__()

        self.imageLabel =  QLabel()
        tmp_img =  QImage("../../../dui/resources/DIALS_Logo_scaled.png")
        self.imageLabel.setPixmap( QPixmap.fromImage(tmp_img))

        self.arr_data = get_3d_flex_array()
        self.img_w = self.arr_data.all()[1]
        self.img_h = self.arr_data.all()[2]
        self.flex_2d_mask = flex.double(flex.grid(self.img_w, self.img_h),0)

        print "self.img_w, self.img_h =", self.img_w, self.img_h

        self.setWidget(self.imageLabel)
        self.show()
        self.arr_img = img_w_cpp()
        self.slice_pos = 0

        self.setWidgetResizable(True)

    def update_me(self):

        flex_2d_data = self.arr_data[self.slice_pos:self.slice_pos + 1, 0:self.img_w, 0:self.img_h]
        flex_2d_data.reshape(flex.grid(self.img_w, self.img_h))
        arr_i = self.arr_img(flex_2d_data, self.flex_2d_mask, i_min = -3.0, i_max = 500)
        q_img =  QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]),  QImage.Format_RGB32)

        self.imageLabel.setPixmap( QPixmap.fromImage(q_img))
        self.setWidget(self.imageLabel)
        self.update()
        #self.show()

        #print "self.slice_pos=", self.slice_pos
        dif_time = time_now() - self.my_time
        self.my_time = time_now()
        #print "time spent=", dif_time


        self.slice_pos += 1
        if self.slice_pos >= self.arr_data.all()[0] :
            self.slice_pos = 0

class ImgTab( QWidget):

    def __init__(self, parent = None):
        super(ImgTab, self).__init__()

        self.scrollArea = MyScroll(self)
        main_box =  QVBoxLayout()

        btn_play =  QPushButton('\n   Play Video  \n', self)
        btn_play.clicked.connect(self.B_play_clicked)

        btn_stop =  QPushButton('\n   Stop Video  \n', self)
        btn_stop.clicked.connect(self.B_stop_clicked)

        hbox = QHBoxLayout()

        hbox.addWidget(btn_play)
        hbox.addWidget(btn_stop)

        main_box.addLayout(hbox)
        main_box.addWidget(self.scrollArea)

        self.setLayout(main_box)
        self.show()
        self.update()

    def B_play_clicked(self):
        print "B_play_clicked(self)"

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.scrollArea.update_me)
        self.timer.start(1)

    def B_stop_clicked(self):
        print "B_stop_clicked(self)"

        #print "dir(self.timer) =", dir(self.timer)
        self.timer.stop()
        


if __name__ == '__main__':

    import sys
    app =  QApplication(sys.argv)
    frame = ImgTab()
    sys.exit(app.exec_())



