import os

def read_from_log(file_in):

    with open(file_in) as myfile:
        all_lines = myfile.readlines()

    myfile.close()
    print "\n\n             _____________________________________Reading from file:", n_file

    print "len(", file_in, ") =", len(all_lines)

    max_len = len(all_lines)
    if(max_len > 45):
        max_len = 45

    for single_line in all_lines[0:max_len]:
        print single_line,
    print "\n\n"

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



