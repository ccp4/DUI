#!/usr/bin/python
import os
import sys
import pickle
from cli_utils import print_list, TreeShow, DialsCommand, \
     generate_report, build_command_lst, get_next_step

class UniStep(object):
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
        self.next_step_list = None
        self.prev_step = prev_step
        self.command_lst = [None]
        self.success = None
        self.pickle_file_out = None
        self.json_file_out = None
        self.phil_file_out = None
        self.report_out = None
        self.dials_comand = DialsCommand()

        self.work_dir = os.getcwd()


    def __call__(self, cmd_lst, ref_to_class):
        self.command_lst = cmd_lst
        if( cmd_lst[0] == "fail" ):
            #testing virtual failed step
            print "\n intentionally FAILED for testing \n"
            self.success = False

        else:
            if( cmd_lst[0] in self.dials_com_lst ):
                self.build_command(cmd_lst)
                self.success = self.dials_comand( lst_cmd_to_run = self.cmd_lst_to_run,
                                                 ref_to_class = ref_to_class)

                if( self.success == True ):
                    #print "#generate_report(self)"
                    self.report_out = generate_report(self)

            else:
                print "NOT dials command"
                self.success = False

    def build_command(self, cmd_lst):

        self.cmd_lst_to_run = build_command_lst(self, cmd_lst)
        print "\n cmd_lst_to_run =", self.cmd_lst_to_run, "\n"

    def get_next_step(self):
        return get_next_step(self)

class Runner(object):

    ctrl_com_lst = ["goto", "fail", "slist","reset"]
    def __init__(self):
        root_node = UniStep(prev_step = None)
        root_node.success = True
        root_node.command_lst = ["Root"]
        self.step_list = [root_node]
        self.bigger_lin = 0
        self.current = self.bigger_lin
        self.create_step(root_node)

    def run(self, command_str, ref_to_class, mk_nxt = True):

        cmd_lst = command_str.split()
        if( cmd_lst[0] == "goto" ):
            self.goto(int(cmd_lst[1]))

        elif( cmd_lst[0] == "slist" ):
            self.slist()

        elif( cmd_lst[0] == "mkchi" ):
            self.create_step(self.step_list[self.current])

        elif( cmd_lst[0] == "mksib" ):
            self.goto_prev()
            print "forking"
            self.create_step(self.step_list[self.current])

        else:
            if( self.step_list[self.current].success == True ):
                self.goto_prev()
                print "forking"
                self.create_step(self.step_list[self.current])

            self.step_list[self.current](cmd_lst, ref_to_class)
            if( self.step_list[self.current].success == True and mk_nxt == True):
                self.create_step(self.step_list[self.current])

            else:
                print "failed step"

    def create_step(self, prev_step):
        new_step = UniStep(prev_step = prev_step)
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        try:
            if( prev_step.next_step_list == None ):
                prev_step.next_step_list = [new_step]
                print "converting None in [new_step]"

            else:
                prev_step.next_step_list.append(new_step)
                print "appending step"

        except:
            print "failed to append to previous step"

        self.step_list.append(new_step)
        self.goto(self.bigger_lin)

    def goto_prev(self):
        try:
            self.goto(self.step_list[self.current].prev_step.lin_num)

        except:
            print "can NOT fork <None> node "

    def goto(self, new_lin):
        self.current = new_lin

    def get_html_report(self):
        if( self.step_list[self.current].success == True ):
            html_rep = self.step_list[self.current].report_out

        else:
            try:
                html_rep = self.step_list[self.current].prev_step.report_out

            except:
                html_rep = None

        return html_rep

    def get_datablock_path(self):

        tmp_cur = self.step_list[self.current]
        path_to_json = None

        while True:
            if( tmp_cur.command_lst == [None] ):
                tmp_cur = tmp_cur.prev_step

            elif( tmp_cur.success == True and tmp_cur.command_lst[0] == "import" ):
                path_to_json = tmp_cur.json_file_out
                break

            elif( tmp_cur.command_lst[0] == "Root" or tmp_cur.success == False ):
                break

            else:
                tmp_cur = tmp_cur.prev_step


        return path_to_json

    def get_reflections_path(self):
        tmp_cur = self.step_list[self.current]
        if( tmp_cur.command_lst == [None] ):
           tmp_cur = tmp_cur.prev_step

        if( tmp_cur.command_lst[0] == "Root" or
             tmp_cur.command_lst[0] == "import" or
             tmp_cur.success == False ):

            path_to_pickle = None

        try:
            path_to_pickle = tmp_cur.pickle_file_out

        except:
            path_to_pickle = None
            print "no pickle file available"

        return path_to_pickle

    def get_next_from_here(self):
        return self.step_list[self.current].get_next_step()

    def slist(self):
        print "printing in steps list mode: \n"
        print_list(self.step_list, self.current)

if( __name__ == "__main__"):
    tree_output = TreeShow()

    try:
        with open ('bkp.pickle', 'rb') as bkp_in:
            uni_controler = pickle.load(bkp_in)

    except:
        uni_controler = Runner()

    tree_output(uni_controler)

    command = ""
    while( command.strip() != 'exit' and command.strip() != 'quit' ):
        try:
            inp_str = "lin [" + str(uni_controler.current) + "] >>> "
            command = str(raw_input(inp_str))
            if( command == "" ):
                print "converting empty line in self.slist()"
                command = "slist"

        except:
            print " ... interrupting"
            sys.exit(0)

        uni_controler.run(command, None, mk_nxt = True)
        tree_output(uni_controler)
        nxt_str = uni_controler.get_next_from_here()
        print "\n next to run:\n ", nxt_str

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(uni_controler, bkp_out)

