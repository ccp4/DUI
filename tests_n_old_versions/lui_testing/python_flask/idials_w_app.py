#!/usr/bin/python
'''
DUI's management of CLI commands and navigation tree

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import os
import sys
import pickle
from cli_utils import print_list, TreeShow, DialsCommand, sys_arg, \
     generate_report, build_command_lst, get_next_step, generate_predict

from flask import Flask, render_template, request

class CommandNode(object):
    dials_com_lst = [
    'import',
    'find_spots',
    'index',
    'refine_bravais_settings',
    'reindex',
    'refine',
    'integrate',
    'export',
    ]

    def __init__(self, prev_step = None):
        self.lin_num = 0
        self.next_step_list = []
        self.prev_step = prev_step
        self.command_lst = [None]
        self.success = None
        self.refl_pickle_file_out = None
        self.json_file_out = None
        self.phil_file_out = None
        self.log_file_out = None
        self.debug_log_file_out = None
        self.report_out = None
        self.predict_pickle_out = None
        self.err_file_out = None

        self.dials_command = DialsCommand()
        #self.work_dir = os.getcwd()

    def __call__(self, cmd_lst, ref_to_class):
        self.command_lst = cmd_lst
        if(cmd_lst[0] == "fail"):
            #testing virtual failed step
            print "\n intentionally FAILED for testing \n"
            self.success = False

        else:
            if(cmd_lst[0] in self.dials_com_lst):
                self.build_command(cmd_lst)
                self.success = self.dials_command( lst_cmd_to_run = self.cmd_lst_to_run,
                                                 ref_to_class = ref_to_class)

                if(self.success == True):
                    self.report_out = generate_report(self)
                    self.predict_pickle_out = generate_predict(self)

            else:
                print "NOT dials command"
                self.success = False

    def edit_list(self, cmd_lst):
        self.command_lst = cmd_lst

    def build_command(self, cmd_lst):
        self.cmd_lst_to_run = build_command_lst(self, cmd_lst)
        print "\n cmd_lst_to_run =", self.cmd_lst_to_run, "\n"

    def get_next_step(self):
        return get_next_step(self)


class Runner(object):

    def __init__(self):
        root_node = CommandNode(prev_step = None)
        root_node.success = True
        root_node.command_lst = ["Root"]
        self.step_list = [root_node]
        self.bigger_lin = 0
        self.current_line = self.bigger_lin
        self.make_next = True
        self.create_step(root_node)

        print "root_node.lin_num =", root_node.lin_num
        #self.current_node = root_node

    def run(self, command, ref_to_class):

        #TODO verify the step actually runs and give the proper output files

        if(type(command) is str):
            cmd_lst = command.split()
        else:
            cmd_lst = command

        if(cmd_lst[0] == "goto"):
            self.goto(int(cmd_lst[1]))

        elif(cmd_lst[0] == "slist"):
            self.slist()

        elif(cmd_lst[0] == "clean"):
            self.clean()

        elif(cmd_lst[0] == "mkchi"):
            self.create_step(self.current_node)

        elif(cmd_lst[0] == "mksib"):
            old_command_lst = self.current_node.command_lst
            self.goto_prev()
            print "forking"
            self.create_step(self.current_node)
            self.current_node.edit_list(old_command_lst)

        else:
            if(self.current_node.success == True):
                self.goto_prev()
                print "forking"
                self.create_step(self.current_node)

            self.current_node(cmd_lst, ref_to_class)
            if(self.current_node.success == True and self.make_next == True):
                self.create_step(self.current_node)

            else:
                print "failed step"

    def clean(self):
        print "\n Cleaning"
        print "self.current_line =", self.current_line

        lst_to_rm = []

        for node in self.step_list:
            if( node != self.current_node and
                node.success == None and (
                self.make_next == False or
                len(node.prev_step.next_step_list) > 1 ) ):
                lst_to_rm.append(node)

        for node in lst_to_rm:
            node.prev_step.next_step_list.remove(node)
            self.step_list.remove(node)

        print "self.current_line =", self.current_line, "\n"

    def create_step(self, prev_step):
        new_step = CommandNode(prev_step = prev_step)
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        prev_step.next_step_list.append(new_step)
        self.step_list.append(new_step)
        self.goto(self.bigger_lin)

    def goto_prev(self):
        try:
            self.goto(self.current_node.prev_step.lin_num)

        except:
            print "can NOT fork <None> node "

    def goto(self, new_lin):
        self.current_line = new_lin

        for node in self.step_list:
            if(node.lin_num == self.current_line):
                self.current_node = node

    def get_current_node():
        return self.current_node

    def get_html_report(self):

        try:
            html_rep = self.current_node.report_out

        except:
            html_rep = None


        old_style = '''
        if(self.current_node.success == True):
            html_rep = self.current_node.report_out

        else:
            try:
                html_rep = self.current_node.prev_step.report_out

            except:
                html_rep = None
        '''

        return html_rep

    def get_datablock_path(self):

        tmp_cur = self.current_node
        path_to_json = None

        while True:
            if(tmp_cur.command_lst == [None]):
                tmp_cur = tmp_cur.prev_step

            elif(tmp_cur.success == True and tmp_cur.command_lst[0] == "import"):
                path_to_json = tmp_cur.json_file_out
                break

            elif(tmp_cur.command_lst[0] == "Root" or tmp_cur.success == False):
                break

            else:
                tmp_cur = tmp_cur.prev_step

        return path_to_json

    def get_log_path(self):

        path_to_log = None

        try:
            path_to_log = self.current_node.log_file_out

        except:
            print "failed to retrieve log path"

        return path_to_log

    def get_experiment_path(self):
        path_to_json = None
        tmp_cur = self.current_node
        if(tmp_cur.command_lst == [None]):
           tmp_cur = tmp_cur.prev_step

        if(tmp_cur.command_lst[0] != "Root" and
          tmp_cur.command_lst[0] != "import" and
          tmp_cur.command_lst[0] != "find_spots" and
          tmp_cur.success == True):

            try:
                path_to_json = tmp_cur.json_file_out

            except:
                print "no experimet json file available"

        return path_to_json

    def get_reflections_path(self):
        tmp_cur = self.current_node
        if(tmp_cur.command_lst == [None]):
            tmp_cur = tmp_cur.prev_step

        if(tmp_cur.command_lst[0] == "Root" or
                tmp_cur.command_lst[0] == "import" or
                tmp_cur.success != True):

            return None, None

        ref_pkl = None
        pre_pkl = None

        try:
            ref_pkl = tmp_cur.refl_pickle_file_out
            pre_pkl = tmp_cur.predict_pickle_out

        except:
            print "no pickle file available"

        return ref_pkl, pre_pkl

    def get_next_from_here(self):
        return self.current_node.get_next_step()

    def slist(self):
        print "printing in steps list mode: \n"
        print_list(self.step_list, self.current_line)

def main_loop(i_runner, o_tree):
    command = ""
    while(command.strip() != 'exit' and command.strip() != 'quit'):
        try:
            inp_str = "lin [" + str(i_runner.current_line) + "] >>> "
            command = str(raw_input(inp_str))
            if(command == ""):
                print "converting empty line in self.slist()"
                command = "slist"

        except:
            print " ... interrupting"
            sys.exit(0)

        i_runner.run(command, None)
        o_tree(i_runner)

        with open(storage_path + "/dui_files/bkp.pickle", "wb") as bkp_out:
            pickle.dump(i_runner, bkp_out)

'''

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    str_out = ""
    if request.method == 'POST':
        print request.form
        str_entered = request.form['command']
        str_out = (str_entered + "\n\n") * 15
        print "\n", str_entered, "\n"

    return render_template("index.html", out_put = str_out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

'''


if(__name__ == "__main__"):
    tree_output = TreeShow()
    make_next_in = True
    print "Running in << automatic >> mode ..."
    storage_path = sys_arg.directory

    try:
        with open (storage_path + "/dui_files/bkp.pickle", "rb") as bkp_in:
            idials_runner = pickle.load(bkp_in)

    except Exception as e:
        print "str(e) =", str(e)
        print "e.message =", e.message
        idials_runner = Runner()

        try:
            import shutil
            shutil.rmtree(storage_path + "/dui_files")

        except:
            print "failed to do \"shutil.rmtree(\"/dui_files\")\""

        os.mkdir(storage_path + "/dui_files")

    idials_runner.make_next = make_next_in
    tree_output(idials_runner)
    main_loop(i_runner = idials_runner, o_tree = tree_output)


