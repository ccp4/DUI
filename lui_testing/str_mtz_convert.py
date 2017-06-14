def build_mtz_str(str_in):
    str_out = str_in
    last_fwsl = -1
    last_point = len(str_out)
    print "len(str_out) = ", last_point

    for pos, singe_shar in enumerate(str_in):
        if( singe_shar == "/" ):
            last_fwsl = pos

        if( singe_shar == "." ):
            last_point = pos

        if( singe_shar == "#" ):
            str_out = str_out[:pos] + "n" + str_out[pos + 1:]

    print "last_point = ", last_point
    print "last_fwsl = ", last_fwsl
    print "str_out(1) =", str_out

    str_out = str_out[last_fwsl + 1:last_point]

    print "str_out(2) =", str_out

    return str_out




if( __name__ == "__main__" ):
    template_str = "/scratch/dui/dui_test/only_10_img/th_8_2_####.cbf"
    mtz_name = build_mtz_str(template_str)
    print "mtz_name =", mtz_name
