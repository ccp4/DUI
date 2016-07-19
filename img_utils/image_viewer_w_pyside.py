import sys
from dxtbx.datablock import DataBlockFactory
from data_2_img import img_w_cpp
from dials.array_family import flex

from PySide.QtGui import *
from PySide.QtCore import *

import numpy as np

class MyDynamicLabel(QLabel):
    def __init__(self, q_img = None):
        super(MyDynamicLabel, self).__init__()

        pix = QPixmap.fromImage(q_img)

        self.setPixmap(pix)


class MyImgWin(QWidget):

    def __init__(self, my_array_double = None):
        super(MyImgWin, self).__init__()


        flex_2d_mask = flex.double(flex.grid(800, 900),0)

        flex_2d_data = my_array_double[1:2, 0:800, 0:900]
        flex_2d_data.reshape(flex.grid(800, 900))

        arr_i = img_w_cpp()
        arr_i = arr_i(flex_2d_data, flex_2d_mask)


        q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

        imageLabel = MyDynamicLabel(q_img)

        scrollArea = QScrollArea()
        scrollArea.setWidget(imageLabel)

        main_box = QHBoxLayout()

        multi_control_box = QVBoxLayout()

        label_test = QLabel(" <<< Test 01 >>>")
        multi_control_box.addWidget(label_test)

        real_time_slider = QSlider()
        real_time_slider.setRange(0, 9)
        real_time_slider.setOrientation(Qt.Horizontal)
        real_time_slider.sliderMoved.connect(self.onSliderMove)
        multi_control_box.addWidget(real_time_slider)

        main_box.addLayout(multi_control_box)

        main_box.addWidget(scrollArea)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Image inside scrollable')
        self.show()
        self.setLayout(main_box)

    def onSliderMove(self, position = None):
        print "position =", position
        print "onSliderMove"


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



