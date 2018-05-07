import os

mini_path = "../../../../dui_test/X4_wide/xia2_run/DEFAULT/NATIVE/SWEEP1/"
lst_dir = os.listdir(mini_path)
lst_file = []
for n_dir in lst_dir:
    mini_lst_file = os.listdir(mini_path + "/" + n_dir)
    for n_file in mini_lst_file:
        if(n_file[-3:] == "log"):
            lst_file.append(n_file)

for n_file in lst_file:
    print n_file


