'''
libtbx.phil.parse(
    file_name=file_name,
    converter_registry=None,
    process_includes=co.process_includes)
'''

from dials.util.options import OptionParser
import libtbx.load_env
import libtbx.phil
def get_phil_par(path_to_file):

    print "path_to_file =", path_to_file
    obj = libtbx.phil.parse(file_name=path_to_file)
    print "type(obj) =", type(obj)
    print "obj =", obj

if(__name__ == "__main__"):
    get_phil_par("/scratch/dui/dui_test/only_20_img_X4_wide/dui_files/find_spots.phil")
