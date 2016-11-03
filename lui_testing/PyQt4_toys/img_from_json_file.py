import sys, os
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


def build_qimg(img_flex):
    arr_img = img_w_cpp()

    flex_2d_data = img_flex.as_double()
    #flex_2d_data = self.block_3d_flex[img_slice:img_slice + 1, 0:2500, 0:2400]
    #flex_2d_data.reshape(flex.grid(2500, 2400))

    flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)

    arr_i = arr_img(flex_2d_data, flex_2d_mask, i_min = -3.0, i_max = 500)

    q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                   np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)


if( __name__ == "__main__" ):

    datablocks = DataBlockFactory.from_json_file("/home/luiso/dui/dui_test/X4_wide/test_02/dials-1/1_import/datablock.json")
    print "datablocks[0] =", datablocks[0]
    db=datablocks[0]

    sw=db.extract_sweeps()[0]

    print "sw.get_raw_data(0) =", sw.get_raw_data(0)
    print "sw.get_raw_data(1) =", sw.get_raw_data(1)
    print "sw.get_raw_data(2) =", sw.get_raw_data(2)

    im1=sw.get_raw_data(0)[0]

    print "im1.all() =", im1.all()

