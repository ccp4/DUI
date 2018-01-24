def right_side_from_single(in_str_tmp, dir_path):
    out_str = dir_path + in_str_tmp
    for pos, single_char in reversed(list(enumerate(in_str_tmp))):
        if(single_char == "."):
            ext_pos_sep = pos

    left_sd_name = in_str_tmp[:ext_pos_sep]
    ext_name = in_str_tmp[ext_pos_sep:]
    if(ext_name == ".h5"):
        print "found h5 file"
        out_str = left_sd_name
        out_str = out_str + ext_name
        tail_size = 0

    else:
        out_str = left_sd_name

        max_tail_size = int(len(in_str_tmp) / 3)
        for tail_size in xrange(max_tail_size):
            prev_str = out_str
            pos_to_replase = len(out_str) - tail_size - 1
            for num_char in '0123456789':
                if out_str[pos_to_replase] == num_char:
                    out_str = out_str[:pos_to_replase] + '#' + out_str[pos_to_replase + 1:]

            if(prev_str == out_str):
                break

        out_str = out_str + ext_name

    return out_str, tail_size

def get_run_str(str_lst):
    selected_file_path = str(str_lst[0])
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

    dir_name = selected_file_path[:dir_pos_sep]
    print "dir_name =", dir_name

    #TODO test if the next << if >> is actually needed
    if(dir_name[0:3] == "(u\'"):
        print "dir_name[0:3] == \"(u\'\""
        dir_name = dir_name[3:]

    templ_str_tmp = selected_file_path[dir_pos_sep:]
    templ_r_side, bak_pos = right_side_from_single(templ_str_tmp, dir_name)
    print "templ_r_side, bak_pos =", templ_r_side, bak_pos

if(__name__ == "__main__"):

    str_lst_ux = ['/scratch/dui/dui_code/mini_idials_w_GUI/dynamic_reindex_gui.pyc',
                  '/scratch/dui/dui_code/mini_idials_w_GUI/params_live_gui_generator.pyc']

    str_lst_wd = ['c:\scratch\dui\dui_code\mini_idials_w_GUI\dynamic_reindex_gui.pyc',
                  'c:\scratch\dui\dui_code\mini_idials_w_GUI\params_live_gui_generator.pyc']

    str_lst_single = ['/scratch/dui/dui_code/mini_idials_w_GUI/dynamic_reindex_gui.pyc']

    str_to_run = get_run_str(str_lst_single)



