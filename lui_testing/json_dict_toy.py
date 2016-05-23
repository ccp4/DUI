import json



def get_list(data):
    for key in data.keys():
        print "key =", key
        print "<<key>> = <<" , key , ">>"
        if key == "13" :
            print
            print "key 13"
            print


    print "_______________________________"

    for col in data['2']:
        print "col =", col

    print "_______________________________"

    for val in data.items():
        print "_______________________________"
        for iner_val in val:
            for iner__iner_val in iner_val:

                print "iner__iner_val =", iner__iner_val
                print "<<<"





if( __name__ == "__main__" ):

    input_file=open('bravais_summary.json', 'r')
    data = json.load(input_file)

    get_list(data)
