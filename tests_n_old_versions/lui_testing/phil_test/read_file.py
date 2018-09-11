from dials.util.options import OptionParser

def get_phil_par(path_to_file):
    print "path_to_file =", path_to_file
    parser = OptionParser(file_name=path_to_file)
    params, options = parser.parse_args(show_diff_phil=False)

if(__name__ == "__main__"):
    get_phil_par("/scratch/dui/dui_test/only_20_img_X4_wide/dui_files/find_spots.phil")
