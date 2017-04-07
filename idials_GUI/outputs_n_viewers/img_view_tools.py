
'''
iDIALS GUI's image viewer tools

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import numpy as np

from dials_viewer_ext import rgb_img
from dials.array_family import flex

def py_find_closer_hkl_func(x_mouse_scaled, y_mouse_scaled, flat_data_lst):
    #print"\n Using Python search for closer reflection \n"
    dst_squared = 999999.0
    hkl_result = None
    slice_result = None
    for j, img_flat_data in enumerate(flat_data_lst):
        for i, reflection in enumerate(img_flat_data):
            x = float(reflection[0]) + float(reflection[2]) / 2.0
            y = float(reflection[1]) + float(reflection[3]) / 2.0

            tmp_dst_squared = (x - x_mouse_scaled) ** 2.0 + (y - y_mouse_scaled) ** 2.0

            if( tmp_dst_squared < dst_squared ):
                hkl_result = i
                slice_result = j
                dst_squared = tmp_dst_squared

    return hkl_result, slice_result

def py_list_arange_func(bbox_lst, hkl_lst, n_imgs):

    img_lst = []
    for time in xrange(n_imgs):
        img_lst.append([])

    for i, ref_box in enumerate(bbox_lst):
        x_ini = ref_box[0]
        y_ini = ref_box[2]
        width = ref_box[1] - ref_box[0]
        height = ref_box[3] - ref_box[2]

        box_dat = []
        box_dat.append(x_ini)
        box_dat.append(y_ini)
        box_dat.append(width)
        box_dat.append(height)

        if( len(hkl_lst) <= 1 ):
            local_hkl = ""
            box_dat.append(local_hkl)

        else:
            local_hkl = hkl_lst[i]
            if(local_hkl == "(0, 0, 0)"):
                local_hkl = "NOT indexed"

            box_dat.append(local_hkl)

        for idx in xrange(ref_box[4], ref_box[5]):
            img_lst[idx].append(box_dat);

    return img_lst

try:
    import lst_ext
    find_closer_hkl = lst_ext.find_closer_hkl_func
    lst_arrange = lst_ext.arrange_list
    print "running C++ lst_ext"

except:
    find_closer_hkl = py_find_closer_hkl_func
    lst_arrange = py_list_arange_func
    print "running Python replacements of lst_ext C++ Module"

def find_hkl_near(x_mouse_scaled, y_mouse_scaled, flat_data_lst):

    hkl_result, slice_result = find_closer_hkl(x_mouse_scaled, y_mouse_scaled, flat_data_lst)
    if hkl_result == -1 :
        hkl_result, slice_result = None

    return hkl_result, slice_result


def lst_arange(bbox_lst, hkl_lst, n_imgs):
    return lst_arrange(bbox_lst, hkl_lst, n_imgs)


class img_w_cpp(object):
    def __init__(self):
        self.wx_bmp_arr = rgb_img()

    def __call__(self, flex_data_in, flex_mask_in, show_nums = False,
                 i_min = -3.0, i_max = 200.0, palette = "hot ascend"):

        err_code = self.wx_bmp_arr.set_min_max(i_min, i_max)

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


class build_qimg(object):
    def __init__(self):
        self.arr_img = img_w_cpp()

    def __call__ (self, img_flex, palette_in, min_i, max_i):
        flex_2d_data = img_flex.as_double()
        flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = min_i, i_max = max_i, palette = palette_in)

        q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

        return q_img


