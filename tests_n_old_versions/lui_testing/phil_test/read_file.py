'''
from dials.util.options import OptionParser
import libtbx.load_env
'''

import libtbx.phil

class ScopeData(object):
    '''
    class conceived to store only data related to the scope Phil object
    '''
    pass

class tree_2_lineal(object):

    '''
    Recursively navigates the Phil objects in a way that the final
    self.lst_obj is a lineal list without ramifications
    '''

    def __init__(self, phl_obj):
        self.lst_obj = []
        self.deep_in_rec(phl_obj)

    def __call__(self):
        return self.lst_obj

    def deep_in_rec(self, phl_obj):

        for single_obj in phl_obj:
            if( single_obj.is_definition ):
                self.lst_obj.append(single_obj)

            elif( single_obj.is_scope ):
                scope_info = ScopeData()
                scope_info.is_definition = False
                self.lst_obj.append(scope_info)
                self.deep_in_rec(single_obj.objects)

            else:
                print "\n\n _____________ <<< WARNING neither definition or scope\n\n"


def get_phil_par(path_to_file):

    print "path_to_file =", path_to_file
    obj = libtbx.phil.parse(file_name=path_to_file)
    print "type(obj) =", type(obj)
    print "obj =", obj
    lst_obj = tree_2_lineal(obj.objects)
    multipl_phil_lst = lst_obj()

    for obj in multipl_phil_lst:
        if(obj.is_definition):
            str_par = str(obj.full_path()) + "="
            str_val = ''
            for nm, single_val in enumerate(obj.extract()):
                if(nm > 0):
                    str_val += ","
                str_val += str(single_val)

            str_par += str_val

            print str_par

if(__name__ == "__main__"):
    get_phil_par("/scratch/dui/dui_test/only_20_img_X4_wide/dui_files/find_spots.phil")

