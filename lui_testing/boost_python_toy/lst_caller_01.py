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
        return 10

img_select = dumy_class()

def ini_reflection_table(pckl_file_path = None):
    if( pckl_file_path != None ):

        print "[pickle file] =", pckl_file_path
        table = flex.reflection_table.from_pickle(pckl_file_path)
        print "table =", table
        local_bbox = table[5]['bbox']
        print "local_bbox =", local_bbox
        print "len(table) = ", len(table)

        n_refs = len(table)

        bbox_col = map(list, table["bbox"])
        a = lst_ext.arange_list(bbox_col)
        #print "a =", a

        # in the image viewer, the img_select variable is par of the class
        n_imgs = img_select.maximum()

        flat_data_lst = []
        if( n_imgs > 0 ):


            #old_stable_way = '''
            firts_time = time_now()

            for img_num in xrange(n_imgs):
                tmp_lst = []
                flat_data_lst.append(tmp_lst)

            for i in xrange(n_refs):
                local_bbox = table[i]['bbox']
                z_boud = local_bbox[4:6]
                x_ini = local_bbox[0]
                y_ini = local_bbox[2]
                width = local_bbox[1] - local_bbox[0]
                height = local_bbox[3] - local_bbox[2]

                try:
                    local_hkl = str(table[i]['miller_index'])

                except:
                    local_hkl = None

                for idx in xrange( int(z_boud[0]), int(z_boud[1]) ):
                    reflection_data = flat_data()
                    reflection_data.box = [x_ini, y_ini, width, height]

                    reflection_data.hkl = local_hkl

                    flat_data_lst[idx].append(reflection_data)

            print "\n building flat_data_lst (diff time) =", time_now() - firts_time, "\n"
            #'''
    else:
        flat_data_lst = [None]


if( __name__ == "__main__" ):
    lst_data = ini_reflection_table("/home/luiso/dui/dui_test/only_9_img/dui_idials_tst_05/dials-1/3_index/reflections.pickle")

