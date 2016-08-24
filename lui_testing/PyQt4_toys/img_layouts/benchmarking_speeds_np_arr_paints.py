from PySide import QtCore, QtGui
import numpy as np
from dxtbx.datablock import DataBlockFactory
from dials.array_family import flex
import sys

sys.path.append("../../..")
from img_utils.data_2_img import img_w_cpp

def get_3d_flex_array():
    json_file_path = str("../../dummy_unversioned_data/datablock.json")
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


class MyScroll(QtGui.QScrollArea):

    def __init__(self, parent = None):
        super(MyScroll, self).__init__()
        img = QtGui.QImage(2500, 2400, QtGui.QImage.Format_RGB32)
        self.imageLabel = QtGui.QLabel()
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(img))
        self.arr_data = get_3d_flex_array()
        self.setWidget(self.imageLabel)
        self.show()
        self.arr_img = img_w_cpp()
        self.slice_pos = 0

    def update_me(self):

        print "_____________________________________________________________ self.slice_pos =", self.slice_pos

        flex_2d_mask = flex.double(flex.grid(2500, 2400),0)
        flex_2d_data = self.arr_data[self.slice_pos:self.slice_pos + 1, 0:2500, 0:2400]
        flex_2d_data.reshape(flex.grid(2500, 2400))
        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = -3.0, i_max = 500)
        q_img = QtGui.QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QtGui.QImage.Format_RGB32)

        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(q_img))
        self.setWidget(self.imageLabel)
        self.show()

        self.slice_pos += 1
        if self.slice_pos >= self.arr_data.all()[0] :
            self.slice_pos = 0

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
        self.update()

    def B_go_clicked(self):
        print "B_go_clicked(self)"

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.scrollArea.update_me)
        timer.start(1)


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    frame = ImgTab()
    sys.exit(app.exec_())


