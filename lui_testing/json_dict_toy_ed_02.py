import json



def print_someting(experiments_argv):

    from dxtbx.model.experiment.experiment_list import ExperimentListFactory
    experiments = ExperimentListFactory.from_json_file(
                  experiments_argv, check_format=False)

    print "len(experiments)", len(experiments)
    print experiments[0]

    for exp in experiments:
        print "\n\n exp =", exp
        print "dir(exp) =", dir(exp), "\n\n"

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
        print "\n\n dir(goni) =", dir(gonio)



    print "Pass"


if( __name__ == "__main__" ):

    #with datablock.json it fails badly
    #data ='/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/1_import/datablock.json'

    data ='/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/3_index/experiments.json'
    print_someting(data)
    '''
    data ='/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/5_refine/experiments.json'
    print_someting(data)
    '''

