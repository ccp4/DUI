
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
    from dials.command_line.find_spots import phil_scope
    from dials.command_line.refine_bravais_settings import phil_scope

    example = '''
    libtbx.phil.parse(
    input_string=input_string,
    source_info=source_info,
    file_name=file_name,
    converter_registry=converter_registry,
    process_includes=process_includes)

    input_string=None,
    source_info=None,
    file_name=None,
    converter_registry=None,
    process_includes=False
    '''

    print "path_to_file =", path_to_file
    #'''
    p_obj = libtbx.phil.parse(
            input_string=None,
            source_info=None,
            file_name=path_to_file,
            converter_registry=None,
            process_includes=False
            )
    #'''

    #p_obj = phil_scope
    print "type(p_obj) =", type(p_obj)
    print "p_obj =", p_obj
    lst_obj = tree_2_lineal(p_obj.objects)
    multipl_phil_lst = lst_obj()

    lst_str_commands = []

    for obj in multipl_phil_lst:
        if(obj.is_definition):
            try:
                str_par = str(obj.full_path()) + "="
                str_val = ''
                obj_ext = obj.extract()
                print "obj_ext =", obj_ext
                if(type(obj_ext) is list):
                    for nm, single_val in enumerate(obj_ext):
                        if(nm > 0):
                            str_val += ","

                        str_val += str(single_val)

                else:
                    str_val = str(obj_ext)

                str_par += str_val

            except:
                print "\n\n failed to get obj & par \n\n"

            lst_str_commands.append(str_par)

    return lst_str_commands

if(__name__ == "__main__"):
    #lst_par = get_phil_par("/scratch/dui/dui_test/only_20_img_X4_wide/dui_files/find_spots.phil")
    #lst_par = get_phil_par("/home/lui/ccp4/dui_test/only_20_imgs_X4_wide/dui_files/find_spots.phil")

    lst_par = get_phil_par("find_spots.phil")
    print "all commands =", lst_par

