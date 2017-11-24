import json



def print_someting(experiments_argv):

    from dxtbx.model.experiment.experiment_list import ExperimentListFactory
    experiments = ExperimentListFactory.from_json_file(
                  experiments_argv, check_format=False)

    print "len(experiments)", len(experiments)
    print experiments[0]

    for exp in experiments:
        print "\n exp =", exp
        #print "dir(exp) =", dir(exp), "\n"

        #print "dir(exp.crystal) =", dir(exp.crystal)

        print "exp.crystal.get_space_group =", exp.crystal.get_space_group()
        print "exp.crystal.get_unit_cell =", exp.crystal.get_unit_cell()

        #detc = exp.detector
        #scan = exp.scan
        #prof = exp.profile
        gonio = exp.goniometer

        #print "\n\n dir(detc) =", dir(detc)
        #print "\n\n dir(scan) =", dir(scan)
        #print "\n\n dir(prof) =", dir(prof)

        print "\n dir(gonio) =", dir(gonio), "\n"

        '''
        print "gonio.get_fixed_rotation() =", gonio.get_fixed_rotation()
        print "gonio.get_rotation_axis() =", gonio.get_rotation_axis()
        print "gonio.get_rotation_axis_datum() =", gonio.get_rotation_axis_datum()
        print "gonio.get_setting_rotation() =", gonio.get_setting_rotation()
        '''

        #get_U().elems


        print "\nexp.crystal.get_U() =\n", exp.crystal.get_U().elems
        print "\nexp.crystal.get_A() =\n", exp.crystal.get_A().elems
        print "\nexp.crystal.get_B() =\n", exp.crystal.get_B().elems


    print "Pass 01"

    '''
    for exp in experiments:

        crystal = exp.crystal
        scan = exp.scan

        scan_pts = range(crystal.num_scan_points)
        phi = [scan.get_angle_from_array_index(t) for t in scan_pts]
        Umats = [crystal.get_U_at_scan_point(t) for t in scan_pts]

        #if self._relative_to_static_orientation:
        #asuming previous if as True:
        # factor out static U
        Uinv = crystal.get_U().inverse()
        Umats = [U*Uinv for U in Umats]

        print "Umats =", Umats
        print "Uinv =", Uinv

        # NB e3 and e1 definitions for the crystal are swapped compared
        # with those used inside the solve_r3_rotation_for_angles_given_axes
        # method

    print "Pass 02 \n\n##################################################################################\n\n"
    '''



if( __name__ == "__main__" ):

    #with datablock.json it fails badly
    #data ='/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/1_import/datablock.json'


    data ='/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_04/dials-1/3_index/experiments.json'
    print_someting(data)

    data ='/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_04/dials-1/6_refine/experiments.json'
    print_someting(data)
