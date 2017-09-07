import json
import os

tmp_off = '''
self.prev_step = prev_step
self.dials_comand = DialsCommand()
self.work_dir = os.getcwd()
'''

elem = {
        "lin_num": 0,
        "next_step_list": None,
        "command_lst": [None],
        "success": None,
        "pickle_file_out": None,
        "json_file_out": None,
        "phil_file_out": None,
        "report_out": None,
        "prev_step_lin_num": -1,
        "work_dir": os.getcwd()
       }

if(__name__ == "__main__"):
    print elem

    with open('data.json', 'w') as outfile:
        json.dump(elem, outfile)


