def template_right_side_build(in_str_tmp, dir_path):

    print "in_str_tmp =", in_str_tmp
    print "dir_path =", dir_path

    out_str = dir_path + in_str_tmp
    #lst_files = os.listdir(str(dir_path))     #<<< test comment

    for pos, single_char in reversed(list(enumerate(in_str_tmp))):
        if(single_char == "."):
            pos_sep = pos

    left_sd_name = in_str_tmp[:pos_sep]
    print "\n left_sd_name =", left_sd_name, "\n"

    ext_name = in_str_tmp[pos_sep:]
    print "\n ext_name =", ext_name, "\n"

    if(ext_name == ".h5"):
        print "found h5 file"

    else:
        out_str = left_sd_name

        max_tail_size = int(len(in_str_tmp) / 3)
        print "\n max_tail_size =", max_tail_size, "\n"
        for tail_size in xrange(max_tail_size):
            prev_str = out_str
            pos_to_replase = len(out_str) - tail_size - 1
            for num_char in '0123456789':
                if out_str[pos_to_replase] == num_char:
                    out_str = out_str[:pos_to_replase] + '#' + out_str[pos_to_replase + 1:]

            if(prev_str == out_str):
                #print "found non num char"
                break

        out_str = out_str + ext_name

    return out_str

if(__name__ == "__main__"):

    #str_out = template_right_side_build(in_str_tmp = "th_8_2_0001.cbf",
    #                                    dir_path = "/scratch/dui/dui_test/only_9_img")

    str_out = template_right_side_build(in_str_tmp = "collect_1_master.h5",
                                        dir_path = "/dls/mx-scratch/gw56/Eiger/Soleil2/h5/")

    print "str_out =", str_out

