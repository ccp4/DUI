#!/usr/bin/python
import os
import sys
import pickle
from cli_utils import print_list, TreeShow, DialsCommand, \
     generate_report, build_command_lst

class UniStep(object):
    dials_com_lst = [
    'import',
    'find_spots',
    'index',
    'refine',
    'integrate',
    'export',
    ]

    def __init__(self, prev_step = None):
        self.lin_num = 0
        self.next_step_list = None
        self.prev_step = prev_step
        self.command = None
        self.success = None
        self.pickle_file_out = None
        self.json_file_out = None
        self.phil_file_out = None
        self.report_out = None
        self.dials_comand = DialsCommand()

        self.work_dir = os.getcwd()


    def __call__(self, cmd_lst, ref_to_class):
        if( cmd_lst[0] == "fail" ):
            #testing virtual failed step
            print "\n intentionally FAILED for testing \n"
            self.command = cmd_lst
            self.success = False

        else:
            self.command = cmd_lst

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

class Runner(object):

    ctrl_com_lst = ["goto", "fail", "slist","reset"]
    def __init__(self):
        root_node = UniStep(prev_step = None)
        root_node.success = True
        root_node.command = ["Root"]
        self.step_list = [root_node]
        self.bigger_lin = 0
        self.current = self.bigger_lin
        self.create_step(root_node)

    def run(self, command, ref_to_class):

        cmd_lst = command.split()
        if( cmd_lst[0] == "goto" ):
            self.goto(int(cmd_lst[1]))

        elif( cmd_lst[0] == "slist" ):
            self.slist()

        else:
            if( self.step_list[self.current].success == True ):
                self.goto_prev()
                self.create_step(self.step_list[self.current])

            self.step_list[self.current](cmd_lst, ref_to_class)
            if( self.step_list[self.current].success == True ):
                self.create_step(self.step_list[self.current])

            else:
                print "failed step"

    def create_step(self, prev_step):
        new_step = UniStep(prev_step = prev_step)
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        try:
            if( self.step_list[self.current].next_step_list == None ):
                self.step_list[self.current].next_step_list = [new_step]

            else:
                self.step_list[self.current].next_step_list.append(new_step)

        except:
            print "failed to append to previous step"


        self.step_list.append(new_step)
        self.goto(self.bigger_lin)

    def goto_prev(self):
        print "forking"
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

        uni_controler.run(command, None)
        tree_output(uni_controler)

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(uni_controler, bkp_out)
