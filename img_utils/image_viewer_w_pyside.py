import sys
from dxtbx.datablock import DataBlockFactory
from data_2_img import wx_img_w_cpp
from dials.array_family import flex
from PyQt4.QtGui import QImage, QLabel, QPixmap, QApplication
import numpy as np

if __name__ == '__main__':

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
    print "dir(my_array) =", dir(my_array)
    print "type(my_array_double) =", type(my_array_double)
    print "type(my_array) =", type(my_array)


    flex_2d_data = flex.double(flex.grid(500, 250),0)
    flex_2d_mask = flex.double(flex.grid(500, 250),0)

    print "type(flex_2d_data) =", type(flex_2d_data)
    print "type(flex_2d_mask) =", type(flex_2d_mask)

    flex_2d_data = my_array_double[:,:,0]

    arr_i = wx_img_w_cpp(flex_2d_data, flex_2d_mask)

    #converting to QImage
    print "before QImage generator"
    q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                   np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)
    print "after QImage generator"

    #building app with IMG
    app = QApplication([])
    pix = QPixmap.fromImage(q_img)
    lbl = QLabel()
    lbl.setPixmap(pix)
    lbl.show()

    app.exec_()

