
def get_run_str(in_str_lst):

    print "in_str_lst =", in_str_lst

    selected_file_path = str(in_str_lst[0])
    fnd_sep = False
    sep_chr = None
    for pos, single_char in enumerate(selected_file_path):
        if(single_char == "/" or single_char == "\\"):
            dir_pos_sep = pos

            if(fnd_sep == True and sep_chr != single_char):
                print "inconsistent dir separator"
                return None

            fnd_sep = True
            sep_chr = single_char

    if(fnd_sep == False):
        print "Failed to find dir path"
        return None

    dir_path = selected_file_path[:dir_pos_sep]

    #TODO test if the next << if >> is actually needed
    if(dir_path[0:3] == "(u\'"):
        print "dir_path[0:3] == \"(u\'\""
        dir_path = dir_path[3:]

    templ_r_side = selected_file_path[dir_pos_sep:]

    for pos, single_char in reversed(list(enumerate(templ_r_side))):
        if(single_char == "."):
            ext_pos_sep = pos

    left_sd_name = templ_r_side[:ext_pos_sep]
    ext_name = templ_r_side[ext_pos_sep:]
    if(ext_name == ".h5"):
        print "found h5 file"
        file_name = left_sd_name
        file_name = file_name + ext_name
        tail_size = 0

    else:
        file_name = left_sd_name

        max_tail_size = int(len(templ_r_side) / 3)
        for tail_size in xrange(max_tail_size):
            prev_str = file_name
            pos_to_replase = len(file_name) - tail_size - 1
            for num_char in '0123456789':
                if file_name[pos_to_replase] == num_char:
                    file_name = file_name[:pos_to_replase] + '#' + file_name[pos_to_replase + 1:]

            if(prev_str == file_name):
                break

        file_name = file_name + ext_name

    if(in_str_lst and len(in_str_lst) == 1):
        out_str = dir_path + file_name
        img_range = None

    else:
        str_lst = []
        for single_qstring in in_str_lst:
            str_lst.append(str(single_qstring))

        out_str = ""
        pos_last_num = 0

        for pos in xrange(len(str_lst[0])):
            all_equal = True
            single_char = str_lst[0][pos]
            for single_string in str_lst:
                try:
                    if(single_string[pos] != single_char):
                        all_equal = False
                except:
                    all_equal =False

            if(all_equal == True):
                out_str = out_str + single_char

            else:
                out_str = out_str + "#"
                pos_last_num = pos

        pos_last_num +=1

        print "pos_last_num =", pos_last_num

        if(pos_last_num > 1):
            lst_num_str = []
            try:

                for single_string in str_lst:
                    lst_num_str.append(int(single_string[pos_last_num-tail_size:
                                                         pos_last_num]))

                print "lst_num_str =", lst_num_str
                img_range = [min(lst_num_str), max(lst_num_str)]

            except:
                print "something went wrong with the range thing 01"
                img_range = None

        else:
            print "something went wrong with the range thing 02"
            img_range = None


    print "out_str( template mode ) =", out_str

    new_cmd = ""
    for single_char in out_str:

        if(single_char != "#"):
            new_cmd += single_char

        elif(prev_char != "#"):
            new_cmd += "*"

        prev_char = single_char

    out_str = new_cmd
    print "img_range =", img_range

    if(img_range != None):
        out_str += " image_range=" + str(img_range[0]) + "," + str(img_range[1])

    print "out_str( * mode ) =", out_str, "\n"

    return out_str

if(__name__ == "__main__"):

    str_lst_ux = ['/scratch/dui/dui_code/mini_idials_w_GUI/dynamic_reindex_gui.pyc',
                  '/scratch/dui/dui_code/mini_idials_w_GUI/params_live_gui_generator.pyc']

    str_lst_wd = ['c:\scratch\dui\dui_code\mini_idials_w_GUI\dynamic_reindex_gui.pyc',
                  'c:\scratch\dui\dui_code\mini_idials_w_GUI\params_live_gui_generator.pyc']

    str_lst_single = ['/scratch/dui/dui_code/mini_idials_w_GUI/dynamic_reindex_gui.pyc']

    str_lst_single_real = ['/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0004.cbf']

    str_lst_real = ['/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0004.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0005.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0006.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0007.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0008.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0009.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0010.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0011.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0012.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0013.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0014.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0015.cbf']

    str_lst_trick = ['/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0004.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0005.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0006.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0007.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0012.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0013.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0014.cbf',
                    '/scratch/dui/dui_test/only_20_img_X4_wide/X4_wide_M1S4_2_0015.cbf']


    img_range = get_run_str(str_lst_ux)
    img_range = get_run_str(str_lst_wd)
    img_range = get_run_str(str_lst_single)
    img_range = get_run_str(str_lst_single_real)
    img_range = get_run_str(str_lst_real)
    img_range = get_run_str(str_lst_trick)



