#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from subprocess import call as shell_func

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


class uni_step(object):
    example = '''
    dials.import ../*.cbf
    dials.find_spots datablock.json
    dials.index datablock.json strong.pickle
    dials.refine experiments.json indexed.pickle
    dials.integrate refined_experiments.json refined.pickle
    dials.export integrated_experiments.json integrated.pickle

    dials.import ../*.cbf output.datablock=test_02.json

    dials.find_spots input.datablock=datablock.json    \
     output.reflections=reflections_tst_01.pickle

    dials.index input.datablock=datablock.json input.reflections=reflections_tst_01.pickle \
     output.experiments=experiments_tst_01.json output.reflections=indexed_tst_01.pickle

    dials.refine input.experiments=experiments_tst_01.json input.reflections=indexed_tst_01.pickle \
     output.experiments=refined_experiment_tst_01.json output.reflections=refined_tst_01.pickle

    dials.integrate input.experiments=refined_experiment_tst_01.json input.reflections=refined_tst_01.pickle \
     output.experiments=integrated_experiments_tst_01.json output.reflections=integrated_refletions_tst_01.pickle

    dials.export integrated_experiments_tst_01.json integrated_refletions_tst_01.pickle

    '''

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


        print "\n self.cmd_lst_to_run =", self.cmd_lst_to_run, "\n"

class runner(object):

    ctrl_com_lst = ["goto", "fail", "slist","reset"]
    def __init__(self):
        self.step_list = [uni_step(None)]
        self.bigger_lin = 0
        self.current = self.bigger_lin

    def run(self, command):

        cmd_lst = command.split()
        if( cmd_lst[0] == "goto" ):
            self.goto(int(cmd_lst[1]))

        elif( cmd_lst[0] == "slist" ):
            self.slist()

        else:
            if( self.step_list[self.current].success != False ):
                if( self.step_list[self.current].success == True ):
                    self.goto_prev()
                    self.create_step(self.step_list[self.current])

                self.step_list[self.current](cmd_lst)
                if( self.step_list[self.current].success == True ):
                    self.create_step(self.step_list[self.current])

                else:
                    print "failed step"

            else:
                print "cannot run from failed step"

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

if( __name__ == "__main__"):
    uni_controler = runner()

    command = ""
    while command.strip() != 'exit':
        # printing new list of steps
        #prin_lst(uni_controler.step_list, uni_controler.current)

        # showing showing tree
        print "________ showing steps tree:"
        show_tree(step = uni_controler.step_list[0], curr = uni_controler.current, indent = 1)

        try:
            command = str(raw_input(">>> "))

        except:
            print "tweak key pressed ... quitting"
            sys.exit(0)

        uni_controler.run(command)

