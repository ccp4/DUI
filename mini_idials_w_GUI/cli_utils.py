#!/usr/bin/python
'''
mini_idials navigation tree utilities

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

import subprocess
import json
import os


def prn_lst_lst_cmd(last_idials_node):
    cur_nod = last_idials_node
    lst_simpl_cmd = []
    lst_full_cmd = []

    while True:
        if(cur_nod.command_lst == ["Root"] or cur_nod.lin_num == 0):
            break

        l_n = str(cur_nod.lin_num)
        lst_simpl_cmd.append("command_lst[" + l_n + "] = " + str(cur_nod.command_lst))
        lst_full_cmd.append("full_cmd_lst[" + l_n + "] = " + str(cur_nod.dials_comand.full_cmd_lst))

        cur_nod = cur_nod.prev_step

    for prn_lin in reversed(lst_simpl_cmd):
        print prn_lin

    print "\n"

    for prn_lin in reversed(lst_full_cmd):
        print prn_lin

    print "\n\n"


def get_next_step(node_obj):
    if(node_obj.lin_num == 0):
        return "import"

    else:
        for pos, stp in enumerate(node_obj.dials_com_lst[0:-1]):
            if(stp == node_obj.command_lst[0]):
                nxt_str = node_obj.dials_com_lst[pos + 1]
                return nxt_str

    print "\n\n Defaulting to << None >> in automatic << get_next_step >> \n\n"
    return None

def build_command_lst(node_obj, cmd_lst):

    #TODO make sure new step is compatible with previous
    cmd_lst_to_run = []
    cmd_lst_to_run.append("dials." + cmd_lst[0])
    if(cmd_lst[0] != "reindex"):
        for tmp_par in cmd_lst[1:]:
            cmd_lst_to_run.append(tmp_par)

    if(cmd_lst[0] == "import"):
        node_obj.json_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + node_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.debug_log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".debug.log"
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.import', 'template=/home/lui/ccp4/dui_test/only_9_img/X4_wide_M1S4_2_####.cbf',
                         'output.datablock=dials_files/1_datablock.json',
                         'output.log=dials_files/1_import.log',
                         'output.debug_log=dials_files/1_import_debug.log'
                         ] )
        '''
        #TODO make sure import without arguments does NOT run

    elif(cmd_lst[0] == "find_spots"):
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        cmd_lst_to_run.append(input_str)

        node_obj.json_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + node_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.pickle_file_out = "dials_files" + os.sep + str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.debug_log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".debug.log"
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.find_spots', 'spotfinder.mp.nproc=4',
                         'input.datablock=dials_files/1_datablock.json',
                         'output.datablock=dials_files/2_datablock.json',
                         'output.reflections=dials_files/2_reflections.pickle',
                         'output.log=dials_files/2_find_spots.log',
                         'output.debug_log=dials_files/2_find_spots_debug.log'
                         ] )
        '''

    elif(cmd_lst[0] == "index"):
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        cmd_lst_to_run.append(input_str)

        pickle_file_in = node_obj.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        node_obj.json_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_experiments.json"
        output_str = "output.experiments=" + node_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.pickle_file_out = "dials_files" + os.sep + str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.debug_log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".debug.log"
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.index',
                         'input.datablock=dials_files/2_datablock.json',
                         'input.reflections=dials_files/2_reflections.pickle',
                         'output.experiments=dials_files/3_experiments.json',
                         'output.reflections=dials_files/3_reflections.pickle',
                         'output.log=dials_files/3_index.log',
                         'output.debug_log=dials_files/3_index_debug.log'
                         ] )
        '''

    elif(cmd_lst[0] == "refine_bravais_settings"):
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.experiments=" + json_file_in
        cmd_lst_to_run.append(input_str)

        pickle_file_in = node_obj.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        prefix_str = "lin_" + str(node_obj.lin_num) + "_"
        node_obj.prefix_out = prefix_str
        output_str = "output.prefix=" + node_obj.prefix_out
        cmd_lst_to_run.append(output_str)
        cmd_lst_to_run.append("output.directory=dials_files")
        node_obj.json_file_out = "dials_files" + os.sep +  prefix_str + "bravais_summary.json"

        node_obj.log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.debug_log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".debug.log"
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.refine_bravais_settings',
                         'input.experiments=dials_files/3_experiments.json',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'output.prefix=lin_4_',
                         'output.directory=dials_files',
                         'output.log=dials_files/4_refine_bravais_settings.log',
                         'output.debug_log=dials_files/4_refine_bravais_settings_debug.log'
                         ] )
        '''
    elif(cmd_lst[0] == "reindex"):
        try:
            if(cmd_lst[1][0:9] == "solution="):
                sol_num = int(cmd_lst[1][9:])
            else:
                sol_num = 1
        except:
            sol_num = 1

        pickle_file_in = node_obj.prev_step.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        json_file_tmp = node_obj.prev_step.json_file_out
        with open(json_file_tmp) as summary_file:
            j_obj = json.load(summary_file)
        change_of_basis_op = j_obj[str(sol_num)]['cb_op']

        input_str = "change_of_basis_op=" + str(change_of_basis_op)
        cmd_lst_to_run.append(input_str)

        node_obj.json_file_out = "dials_files" + os.sep +  node_obj.prev_step.prefix_out + "bravais_setting_" + str(sol_num) + ".json"

        node_obj.pickle_file_out = "dials_files" + os.sep + str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.reindex',
                         'input.reflections=dials_files/3_reflections.pickle',
                         'change_of_basis_op=a,b,c',
                         'output.reflections=dials_files/5_reflections.pickle'
                         ] )
        '''

    elif(cmd_lst[0] == "refine" or cmd_lst[0] == "integrate"):
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.experiments=" + json_file_in
        cmd_lst_to_run.append(input_str)

        pickle_file_in = node_obj.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        node_obj.json_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_experiments.json"
        output_str = "output.experiments=" + node_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.pickle_file_out = "dials_files" + os.sep + str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

        if(cmd_lst[0] == "integrate"):
            cmd_lst_to_run.append("output.phil=dials_files/" + str(node_obj.lin_num) + "_integrate.phil")

        node_obj.log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.debug_log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".debug.log"
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.refine',
                         'input.experiments=dials_files/lin_4_bravais_setting_9.json',
                         'input.reflections=dials_files/5_reflections.pickle',
                         'output.experiments=dials_files/6_experiments.json',
                         'output.reflections=dials_files/6_reflections.pickle',
                         'output.log=dials_files/6_refine.log',
                         'output.debug_log=dials_files/6_refine_debug.log'
                         ] )
        '''
        now = '''
                        ['dials.refine',
                         'input.experiments=dials_files/lin_4_dials_files/bravais_setting_9.json',
                         'input.reflections=dials_files/5_reflections.pickle',
                         'output.experiments=dials_files/6_experiments.json',
                         'output.reflections=dials_files/6_reflections.pickle']

        '''

    elif(cmd_lst[0] == "export"):
        cmd_lst_to_run.append(node_obj.prev_step.json_file_out)
        cmd_lst_to_run.append(node_obj.prev_step.pickle_file_out)

        node_obj.log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        cmd_lst_to_run.append(output_str)

        node_obj.debug_log_file_out = "dials_files" + os.sep +  str(node_obj.lin_num) + "_" + cmd_lst[0] + ".debug.log"
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        cmd_lst_to_run.append(output_str)

        '''
    full_cmd_lst.append(['dials.export', 'mtz.hklout=hkl_out.mtz',
                         'dials_files/7_experiments.json',
                         'dials_files/7_reflections.pickle',
                         'output.log=dials_files/8_export.log',
                         'output.debug_log=dials_files/8_export_debug.log'
                         ] )
        '''

    return cmd_lst_to_run

def generate_report(node_obj):
    rep_out = None

    if(node_obj.command_lst[0] in node_obj.dials_com_lst[1:-1]):
        current_lin = node_obj.lin_num
        refl_inp = node_obj.pickle_file_out
        deps_outp = "output.external_dependencies=local"
        htm_fil = "dials_files" + os.sep + str(current_lin) + "_report.html"
        html_outp = "output.html=" + htm_fil
        if(node_obj.command_lst[0] == "find_spots"):
            rep_cmd = ["dials.report", refl_inp, deps_outp, html_outp]

        else:
            exp_inp = node_obj.json_file_out
            rep_cmd = ["dials.report", exp_inp, refl_inp, deps_outp, html_outp]

        print "rep_cmd =", rep_cmd

        try:
            gen_rep_proc = subprocess.Popen(rep_cmd)
            gen_rep_proc.wait()
            rep_out = node_obj.work_dir + "/" + htm_fil
            print "generated report at: ", rep_out

        except:
            rep_out = None
            print "Someting went wrong in report level 2"

    else:
        print "NO report needed for this step"
        rep_out = None

    return rep_out

class DialsCommand(object):
    def __init__(self):
        print "creating new DialsCommand (obj)"
        self.full_cmd_lst = None

    def __call__(self, lst_cmd_to_run = None, ref_to_class = None):
        try:
            print "\n [[ running >> \n"
            single_string = ""

            for lin_to_prn in lst_cmd_to_run:
                print lin_to_prn

                single_string += lin_to_prn
                single_string += " "

            print "\n<<<"

            my_process = subprocess.Popen(single_string,
                                        shell = True,
                                        stdout = subprocess.PIPE,
                                        stderr = subprocess.STDOUT,
                                        bufsize = 1)



            '''
            for lin_to_prn in lst_cmd_to_run:
                print lin_to_prn

            print "\n<<<"

            my_process = subprocess.Popen(lst_cmd_to_run,
                                            stdout = subprocess.PIPE,
                                            stderr = subprocess.STDOUT,
                                            bufsize = 1)
            '''

            self.my_pid = my_process.pid

            print "process PID =", self.my_pid

            for line in iter(my_process.stdout.readline, b''):
                single_line = line[0:len(line)-1]
                try:
                    ref_to_class.emit_print_signal(single_line)

                except:
                    print single_line

            print "Done print loop"

            my_process.wait()
            my_process.stdout.close()
            if(my_process.poll() == 0):
                local_success = True

            else:
                local_success = False

                #TODO handle error outputs
                try:
                    ref_to_class.emit_fail_signal()

                except:
                    print Failed

            print "Done all step"

        except Exception as my_err:
            print "error =", my_err, "\n"
            local_success = False
            print "\n FAIL call"

        self.full_cmd_lst = lst_cmd_to_run
        return local_success

def print_list(lst, curr):
    print "__________________________listing:"
    for uni in lst:
        stp_str = str(uni.lin_num) + " " + str(uni.success) + " comm: " + str(uni.command_lst)

        try:
            stp_str += " prev: " + str(uni.prev_step.lin_num)

        except:
            stp_str += " prev: None"

        stp_str += " nxt: "
        if(len(uni.next_step_list) > 0):
            for nxt_uni in uni.next_step_list:
                stp_str += "  " + str(nxt_uni.lin_num)

        else:
            stp_str += "empty"

        if(curr == uni.lin_num):
            stp_str += "                           <<< here I am <<<"

        print stp_str

class TreeShow(object):
    def __init__(self):
        self.ind_spc = "      "
        self.ind_lin = "------"

    def __call__(self, my_runner):
        print
        print "status "
        print " |  lin num "
        print " |   |  command "
        print " |   |   | "
        print "------------------"
        self.max_indent = 0
        self.str_lst = []
        self.add_tree(step = my_runner.step_list[0], indent = 0)
        self.tree_print(my_runner.current_line)
        print "---------------------" + self.max_indent * self.ind_lin


    def add_tree(self, step = None, indent = None):
        if(step.success == True):
            stp_prn = " S "

        elif(step.success == False):
            stp_prn = " F "

        else:
            stp_prn = " N "

        str_lin_num = "{0:3}".format(int(step.lin_num))

        stp_prn += str_lin_num + self.ind_spc * indent + "   \___"
        stp_prn += str(step.command_lst[0])

        self.str_lst.append([stp_prn, indent, int(step.lin_num)])
        new_indent = indent
        if(len(step.next_step_list) > 0):
            for line in step.next_step_list:
                new_indent = indent + 1
                self.add_tree(step = line, indent = new_indent)

        else:
            new_indent = int(new_indent)
            if(new_indent > self.max_indent):
                self.max_indent = new_indent

    def tree_print(self, curr):
        self.tree_dat = []
        for tmp_lst in self.str_lst:
            self.tree_dat.append(tmp_lst)

        for pos, loc_lst in enumerate(self.tree_dat):
            if(pos > 0):
                if(loc_lst[1] < self.tree_dat[pos - 1][1]):
                    for up_pos in xrange(pos - 1, 0, -1):
                        pos_in_str = loc_lst[1] * len(self.ind_spc) + 9
                        left_side = self.tree_dat[up_pos][0][0:pos_in_str]
                        right_side = self.tree_dat[up_pos][0][pos_in_str + 1:]
                        if(self.tree_dat[up_pos][1] > loc_lst[1]):
                            self.tree_dat[up_pos][0] = left_side + "|" + right_side

                        elif(self.tree_dat[up_pos][1] == loc_lst[1]):
                            break

            if(loc_lst[2] == curr):
                lng = len(self.ind_spc) * self.max_indent + 22
                lng_lft = lng - len(self.tree_dat[pos][0])
                str_here = lng_lft * " "
                self.tree_dat[pos][0] += str_here + "   <<< here "

        for prn_str in self.tree_dat:
            print prn_str[0]

