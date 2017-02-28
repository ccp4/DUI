from dials.array_family import flex
from time import time as time_now

import lst_ext

'''
after converting to C++ this should go a LOT faster than:
building flat_data_lst (diff time) = 0.0659489631653
'''
class flat_data(object):
    box = None
    hkl = None

class dumy_class(object):
    def maximum(self):
        return 589

img_select = dumy_class()

def ini_reflection_table(pckl_file_path = None):
    if( pckl_file_path != None ):


        table = flex.reflection_table.from_pickle(pckl_file_path)
        local_bbox = table[5]['bbox']

        n_refs = len(table)
        bbox_col = map(list, table["bbox"])
        try:
            hkl_col = map(str, table["miller_index"])
            print hkl_col[0]
            print hkl_col[n_refs - 1]

        except:
            hkl_col = []



        # in the image viewer, the img_select variable is part of the class
        n_imgs = img_select.maximum()
        print "\n\n\n"

        #print "a =", a

        flat_data_lst = []
        if( n_imgs > 0 ):

            firts_time = time_now()
            a = lst_ext.arange_list(bbox_col, hkl_col, n_imgs)


            print a
            print "\n building flat_data_lst (diff time) =", time_now() - firts_time, "\n"

    else:
        flat_data_lst = [None]



if( __name__ == "__main__" ):
    lst_data = ini_reflection_table("/home/luiso/dui/dui_test/only_9_img/dui_idials_tst_05/dials-1/3_index/reflections.pickle")
    #lst_data = ini_reflection_table("/home/luiso/dui/dui_test/th_9_3_0588/dui_idials_tst_06/dials-1/7_integrate/reflections.pickle")
    #lst_data = ini_reflection_table("/home/luiso/dui/dui_test/only_9_img/dui_idials_tst_05/dials-1/2_find_spots/reflections.pickle")
