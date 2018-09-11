from dials.util.options import OptionParser

def get_phil_par(path_to_file):
    print "path_to_file =", path_to_file
    parser = OptionParser(phil = phil_scope)
    params, options = parser.parse_args(show_diff_phil=False)

if(__name__ == "__main__"):
    get_phil_par("/something/here")
