from PySide import QtCore, QtGui
import numpy as np


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

    return my_array_double


class MyScroll(QtGui.QScrollArea):

    def __init__(self, parent = None):
        super(MyScroll, self).__init__()

        self.imageLabel = QtGui.QLabel()
        '''
        width = 200
        height = 200
        data = np.random.randint(0,256,size=(width,height,3)).astype(np.uint8)

        img = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
        for x in xrange(width):
            for y in xrange(height):
                img.setPixel(x, y, QtGui.QColor(*data[x][y]).rgb())

        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(img))
        '''
        self.setWidget(self.imageLabel)
        self.show()


    def update_me(self):
        print "update_me(self)"

        self.setWidget(self.imageLabel)
        self.show()


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

    def B_go_clicked(self):
        print "B_go_clicked(self)"
        self.scrollArea.update_me()

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    frame = ImgTab()
    sys.exit(app.exec_())


