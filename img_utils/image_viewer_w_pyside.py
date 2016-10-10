import sys
from dxtbx.datablock import DataBlockFactory
from data_2_img import img_w_cpp
from dials.array_family import flex

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtOpenGL import QGLWidget


try:
    from OpenGL import GL
except:
    print "Failed to import OpenGL"

import numpy as np

from time import time as tm_now


class ImgPainter(QWidget):

    def __init__(self):
        super(ImgPainter, self).__init__()
        self.setFixedSize(2550, 2400)
        self.pix = None

    def set_img_pix(self, q_img = None):

        self.pix = QPixmap.fromImage(q_img)

        # the next two choices need to be taken depending on the
        # rendering back end

        # Use paintEvent when [self] inherits from QGLWidget
        #self.paintEvent(None)

        #Use "update" when [self] inherits from QWidget
        self.update()



        #consider self.repaint() for the video thing
        #self.repaint()


    def paintEvent(self, event):

        if( self.pix == None ):
            print "self.pix = None"
            return

        else:
            img_paint = QPainter()
            img_paint.begin(self)
            img_paint.drawPixmap(0, 0, self.pix)
            img_paint.end()


class ScrollableImg(QScrollArea):
    def __init__(self, parent = None):
        super(ScrollableImg, self).__init__()
        self.setWidget(parent)


class MyImgWin(QWidget):

    def __init__(self, my_array_double = None):
        super(MyImgWin, self).__init__()

        self.block_3d_flex = my_array_double
        self.arr_img = img_w_cpp()
        self.img_painter = ImgPainter()
        self.img_pos = 0
        self.imax = 30
        self.new_img()

        main_box = QVBoxLayout()

        label_img_num = QLabel(" <<< IMG Num >>>")
        main_box.addWidget(label_img_num)

        img_num_slider = QSlider()
        img_num_slider.setRange(0, 8)
        img_num_slider.setOrientation(Qt.Horizontal)
        img_num_slider.sliderMoved.connect(self.onImgSliderMove)
        main_box.addWidget(img_num_slider)


        label_imax = QLabel(" <<< I Max >>>")
        main_box.addWidget(label_imax)

        imax_slider = QSlider()
        imax_slider.setRange(0, 1000)
        imax_slider.setOrientation(Qt.Horizontal)
        imax_slider.sliderMoved.connect(self.onMaxiSliderMove)
        main_box.addWidget(imax_slider)

        scrollArea = ScrollableImg(self.img_painter)
        main_box.addWidget(scrollArea)

        self.setLayout(main_box)
        self.setWindowTitle('Image view test')
        self.show()

    def new_img(self):
        self.set_my_img()
        self.update()

    def set_my_img(self):

        tm_start = tm_now()

        flex_2d_mask = flex.double(flex.grid(2500, 2400),0)
        img_slice = self.img_pos

        flex_2d_data = self.block_3d_flex[img_slice:img_slice + 1, 0:2500, 0:2400]
        flex_2d_data.reshape(flex.grid(2500, 2400))

        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = -3.0, i_max = self.imax)

        q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

        self.img_painter.set_img_pix(q_img)
        print "dif_time[set_img_pix(q_img)] =", tm_now() - tm_start


    def onImgSliderMove(self, position = None):
        self.img_pos = position
        self.new_img()

    def onMaxiSliderMove(self, position = None):
        self.imax = position
        self.new_img()


if __name__ == '__main__':

    app = QApplication([])

    json_name = str(sys.argv[1])
    print "json_name =", json_name

    datablocks = DataBlockFactory.from_json_file(json_name)

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

    #type(first_data) = <class 'dxtbx.imageset.ImageSweep'>

    print "Trying to_array()"
    my_array = first_data.to_array()
    print "Done to_array()"
    print "type(my_array) =", type(my_array)
    print "_____________________________ TST"

    my_array_double = my_array.as_double()

    ex = MyImgWin(my_array_double)
    sys.exit(app.exec_())


    app.exec_()



