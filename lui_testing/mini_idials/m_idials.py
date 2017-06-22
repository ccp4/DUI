#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from subprocess import call as shell_func

class uni_step(object):
    dials_com_lst = [
    'import',
    'find_spots',
    'index',
    'refine',
    'integrate',
    'export',
    ]

    def __init__(self, prev_step):
        self.lin_num = 0
        self.next_step_list = None
        self.prev_step = prev_step
        self.command = None
        self.success = None
        self.pickle_file_out = None
        self.json_file_out = None
        self.phil_file_out = None

    def __call__(self, cmd_lst):
        if( cmd_lst[0] == "fail" ):
            #testing virtual failed step
            print "\n intentionally FAILED for testing \n"
            self.command = cmd_lst
            self.success = False

        else:
            print "____________________________________\n << running >>", cmd_lst
            self.command = cmd_lst

            if( cmd_lst[0] in self.dials_com_lst ):
                self.build_command(cmd_lst)
                shell_func(self.cmd_lst_to_run)
                self.success = True

            else:
                print "NOT dials command"
                self.success = False

    def build_command(self, cmd_lst):
        self.cmd_lst_to_run = []
        self.cmd_lst_to_run.append("dials." + cmd_lst[0])
        for tmp_par in cmd_lst[1:]:
            self.cmd_lst_to_run.append(tmp_par)

        if( cmd_lst[0] == "import" ):
            self.json_file_out = str(self.lin_num) + "_datablock.json"
            output_str = "output.datablock=" + self.json_file_out
            self.cmd_lst_to_run.append(output_str)

        elif( cmd_lst[0] == "find_spots" ):
            json_file_in = self.prev_step.json_file_out
            input_str = "input.datablock=" + json_file_in
            self.cmd_lst_to_run.append(input_str)

            self.json_file_out = str(self.lin_num) + "_datablock.json"
            output_str = "output.datablock=" + self.json_file_out
            self.cmd_lst_to_run.append(output_str)

            self.pickle_file_out = str(self.lin_num) + "_reflections.pickle"
            output_str = "output.reflections=" + self.pickle_file_out
            self.cmd_lst_to_run.append(output_str)

        elif( cmd_lst[0] == "index" ):
            json_file_in = self.prev_step.json_file_out
            input_str = "input.datablock=" + json_file_in
            self.cmd_lst_to_run.append(input_str)

            pickle_file_in = self.prev_step.pickle_file_out
            input_str = "input.reflections=" + pickle_file_in
            self.cmd_lst_to_run.append(input_str)

            self.json_file_out = str(self.lin_num) + "_experiments.json"
            output_str = "output.experiments=" + self.json_file_out
            self.cmd_lst_to_run.append(output_str)

            self.pickle_file_out = str(self.lin_num) + "_reflections.pickle"
            output_str = "output.reflections=" + self.pickle_file_out
            self.cmd_lst_to_run.append(output_str)

        elif( cmd_lst[0] == "refine" or cmd_lst[0] == "integrate" ):
            json_file_in = self.prev_step.json_file_out
            input_str = "input.experiments=" + json_file_in
            self.cmd_lst_to_run.append(input_str)

            pickle_file_in = self.prev_step.pickle_file_out
            input_str = "input.reflections=" + pickle_file_in
            self.cmd_lst_to_run.append(input_str)

            self.json_file_out = str(self.lin_num) + "_experiments.json"
            output_str = "output.experiments=" + self.json_file_out
            self.cmd_lst_to_run.append(output_str)

            self.pickle_file_out = str(self.lin_num) + "_reflections.pickle"
            output_str = "output.reflections=" + self.pickle_file_out
            self.cmd_lst_to_run.append(output_str)

        elif( cmd_lst[0] == "export" ):
            self.cmd_lst_to_run.append(self.prev_step.json_file_out)
            self.cmd_lst_to_run.append(self.prev_step.pickle_file_out)

            file_out = str(self.lin_num) + "_integrated.mtz"
            output_str = "mtz.hklout=" + file_out
            self.cmd_lst_to_run.append(output_str)

        print "\n self.cmd_lst_to_run =", self.cmd_lst_to_run, "\n"

class runner(object):

    ctrl_com_lst = ["goto", "fail", "slist","reset"]
    def __init__(self):

        root_node = uni_step(None)
        root_node.success = True
        root_node.command = ["Root"]
        self.step_list = [root_node]
        self.bigger_lin = 0
        self.current = self.bigger_lin
        self.create_step(root_node)

    def run(self, command):

        cmd_lst = command.split()
        if( cmd_lst[0] == "goto" ):
            self.goto(int(cmd_lst[1]))

        elif( cmd_lst[0] == "slist" ):
            self.slist()

        else:
            if( self.step_list[self.current].success == True ):
                self.goto_prev()
                self.create_step(self.step_list[self.current])

            self.step_list[self.current](cmd_lst)
            if( self.step_list[self.current].success == True ):
                self.create_step(self.step_list[self.current])

            else:
                print "failed step"


    def create_step(self, prev_step):
        new_step = uni_step(prev_step)
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

    def slist(self):
        print "printing in steps list mode: \n"
        prin_lst(self.step_list, self.current)

def prin_lst(lst, curr):
    print "__________________________listing:"
    for uni in lst:
        stp_str = str(uni.lin_num) + " comm: " + str(uni.command)

        try:
            stp_str += " prev: " + str(uni.prev_step.lin_num)

        except:
            stp_str += " prev: None"

        stp_str += " nxt: "
        try:
            for nxt_uni in uni.next_step_list:

                stp_str += "  " + str(nxt_uni.lin_num)

        except:
            stp_str += "empty"

        if( curr == uni.lin_num ):
            stp_str += "                           <<< here I am <<<"

        print stp_str

def show_tree(step = None, curr = None, indent = 1):
    if( step.success == True ):
        stp_prn = " T "

    elif( step.success == False ):
        stp_prn = " F "

    else:
        stp_prn = " N "

    str_lin_num = "{:3}".format(step.lin_num)

    stp_prn += str_lin_num + "     " * indent + " └──"
    try:
        stp_prn += str(step.command[0])

    except:
        stp_prn += "None"

    if( step.lin_num == curr ):
        stp_prn += "            <<< here "

    print stp_prn
    try:
        for line in step.next_step_list:
            show_tree(step = line, curr = curr, indent = indent + 1)

    except:
        #print "last indent =", indent
        pass


class tree_show(object):

    def __init__(self):
        print "__init__"

    def __call__(self, step_in = None, current_in = None):
        print "\nsuccess, lin num,  nav tree:\n"
        show_tree(step = step_in, curr = current_in, indent = 1)


if( __name__ == "__main__"):
    uni_controler = runner()
    tree_output = tree_show()

    command = ""
    while command.strip() != 'exit':
        tree_output(step_in = uni_controler.step_list[0],
                    current_in = uni_controler.current)

        try:
            inp_str = "\nlin [" + str(uni_controler.current) + "] >>> "
            command = str(raw_input(inp_str))

        except:
            print " ... interrupting"
            sys.exit(0)

        if( command == "" ):
            print "converting empty line in self.slist()"
            command = "slist"

        uni_controler.run(command)
