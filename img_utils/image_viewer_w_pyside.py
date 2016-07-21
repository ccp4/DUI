import sys
from dxtbx.datablock import DataBlockFactory
from data_2_img import img_w_cpp
from dials.array_family import flex

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtOpenGL import QGLWidget
from OpenGL import GL

import numpy as np

class ImgPainter(QGLWidget):

    def __init__(self):
        super(ImgPainter, self).__init__()
        self.setFixedSize(950, 850)
        self.pix = None

    def set_img_pix(self, q_img = None):
        self.pix = QPixmap.fromImage(q_img)
        self.paintEvent(None)

    def paintEvent(self, event):

        if( self.pix == None ):
            return
        else:

            img_paint = QPainter()
            img_paint.begin(self)
            img_paint.drawPixmap(1, 1, self.pix)
            img_paint.end()


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
        multi_control_box = QVBoxLayout()

        label_img_num = QLabel(" <<< IMG Num >>>")
        multi_control_box.addWidget(label_img_num)

        img_num_slider = QSlider()
        img_num_slider.setRange(0, 8)
        img_num_slider.setOrientation(Qt.Horizontal)
        img_num_slider.sliderMoved.connect(self.onImgSliderMove)
        multi_control_box.addWidget(img_num_slider)


        label_imax = QLabel(" <<< I Max >>>")
        multi_control_box.addWidget(label_imax)

        imax_slider = QSlider()
        imax_slider.setRange(0, 1000)
        imax_slider.setOrientation(Qt.Horizontal)
        imax_slider.sliderMoved.connect(self.onMaxiSliderMove)
        multi_control_box.addWidget(imax_slider)


        main_box.addLayout(multi_control_box)
        main_box.addWidget(self.img_painter)


        self.setLayout(main_box)

        self.setGeometry(300, 300, 1200, 950)
        self.setWindowTitle('Image view test')
        self.show()

    def new_img(self):
        self.set_my_img()
        self.update()

    def set_my_img(self):

        flex_2d_mask = flex.double(flex.grid(800, 900),0)
        img_slice = self.img_pos

        flex_2d_data = self.block_3d_flex[img_slice:img_slice + 1, 400:1200, 300:1200]
        flex_2d_data.reshape(flex.grid(800, 900))

        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = -3.0, i_max = self.imax)

        q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

        self.img_painter.set_img_pix(q_img)


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

    my_array_double = my_array.as_double()

    ex = MyImgWin(my_array_double)
    sys.exit(app.exec_())


    app.exec_()



