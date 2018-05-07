import os

def read_from_log(file_in):
    print "\n Reading from file:", n_file

    with open(file_in) as myfile:
        all_lines = myfile.readlines()

    myfile.close()

    for single_line in all_lines:
        print single_line,


mini_path = "../../../../dui_test/X4_wide/xia2_run/DEFAULT/NATIVE/SWEEP1/"
lst_dir = os.listdir(mini_path)
lst_file = []
for n_dir in lst_dir:
    mini_lst_file = os.listdir(mini_path + n_dir)
    for n_file in mini_lst_file:
        if(n_file[-3:] == "log"):
            n_file = mini_path + n_dir + "/" + n_file
            lst_file.append(n_file)

for n_file in lst_file:
    #print "n_file =", n_file
    read_from_log(n_file)



