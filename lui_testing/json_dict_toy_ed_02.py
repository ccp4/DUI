import json

def get_list(data):
    print "type(data) =", type(data)
    for key in data.keys():
        print "key =", key
        print "<<key>> = <<" , key , ">>"


    print "_______________________________ end key loop \n\n\n"

    '''
    for col in data['beam']:
        print "col =", col

    print "_______________________________"
    '''

    for val in data.items():

        print "\n\n_____________________________________________________"
        print "val =", val
        print "_____________________________________________________"

        for iner_val in val:
            print "iner_val=", iner_val
            '''
            for iner__iner_val in iner_val:

                print "iner__iner_val =", iner__iner_val
                print "<<<"
            '''

if( __name__ == "__main__" ):

    #input_file=open('/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/1_import/datablock.json', 'r')
    #input_file=open('/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/3_index/experiments.json', 'r')
    input_file=open('/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_03/dials-1/5_refine/experiments.json', 'r')
    data = json.load(input_file)

    get_list(data)
