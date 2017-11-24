import json
import os

tmp_off = '''
self.prev_step = prev_step
self.dials_comand = DialsCommand()
self.work_dir = os.getcwd()
'''
def get_new_elem(num = -1):
    elem = {
            "lin_num": 0,
            "next_step_list": None,
            "command_lst": [None],
            "success": None,
            "pickle_file_out": None,
            "json_file_out": None,
            "phil_file_out": None,
            "report_out": None,
            "prev_step_lin_num": num,
            "work_dir": os.getcwd()
        }
    return elem

if(__name__ == "__main__"):

    lst_data = []
    for num in xrange(5):
        new_elem = get_new_elem(num)
        lst_data.append(new_elem)

    print "\n lst_data:\n", lst_data, "\n"

    with open('data.json', 'w') as outfile:
        json.dump(lst_data, outfile)
        #json.dump(dict(elem), outfile)

    print

    with open('data.json') as data_file:
        new_data = json.load(data_file)

    print "\n new_data:\n", new_data
    print "type(new_data) =", type(new_data)
    print "len(new_data) =", len(new_data)
    print "new_data[1][\"work_dir\"] =", new_data[1]["work_dir"]

    print



