import numpy as np

#from PySide.QtGui import QImage, QLabel, QPixmap, QApplication
from PyQt4.QtGui import QImage, QLabel, QPixmap, QApplication
from dials_viewer_ext import rgb_img
from dials.array_family import flex

def wx_img_w_cpp(show_nums = True):

    n_col = 20
    n_row = 10

    wx_bmp_arr = rgb_img()
    flex_data_in = flex.double(flex.grid(n_row, n_col),15)
    flex_mask_in = flex.double(flex.grid(n_row, n_col),0)

    err_code = wx_bmp_arr.set_min_max(14.0, 16.0)

    palette = "black2white"

    if palette == "black2white":
        palette_num = 1
    elif palette == "white2black":
        palette_num = 2
    elif palette == "hot ascend":
        palette_num = 3
    else: # assuming "hot descend"
        palette_num = 4
    print "before c++"
    img_array_tmp = wx_bmp_arr.gen_bmp(flex_data_in, flex_mask_in, show_nums, palette_num)
    print "after c++"
    np_img_array = img_array_tmp.as_numpy_array()

    height = np.size(np_img_array[:, 0:1, 0:1])
    width = np.size( np_img_array[0:1, :, 0:1])

    img_array = np.zeros([height, width, 4], dtype=np.uint8)
    img_array[:,:,0:3] = np_img_array[:,:,0:3]
    print "end of np generator"

    return img_array


height = 300
width = 400

#building array
'''
arr_i = np.zeros([height, width, 4], dtype=np.uint8)
arr_i[20:100, 40:200,0] = 255
arr_i[30:150, 80:250,1] = 255
arr_i[40:200, 120:300,2] = 255
'''
arr_i = wx_img_w_cpp()


#arr_i = wx_img_w_cpp()
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

