#!/usr/bin/python
import subprocess


def get_next_step(uni_step_obj):
    if( uni_step_obj.prev_step.lin_num == 0 ):
        return "import"

    elif(uni_step_obj.command == None):
        for pos, stp in enumerate(uni_step_obj.dials_com_lst[0:-1]):
            print "pos, stp: ", pos, stp
            try:
                if( stp == uni_step_obj.prev_step.command[0] ):
                    nxt_str = uni_step_obj.dials_com_lst[pos + 1]
                    print "returning ", nxt_str
                    return nxt_str

            except:
                pass

        return None

    else:
        for pos, stp in enumerate(uni_step_obj.dials_com_lst):
            print "pos, stp: ", pos, stp
            try:
                if( stp == uni_step_obj.command[0] ):
                    nxt_str = uni_step_obj.command[0]
                    print "returning ", nxt_str
                    return nxt_str

            except:
                pass

        return None


def build_command_lst(uni_step_obj, cmd_lst):

    to_re_use = '''
    dials.import ../*.cbf
    dials.find_spots datablock.json spotfinder.mp.nproc=4
    dials.index datablock.json strong.pickle

    opt:

    dials.refine_bravais_settings input.experiments=experiments.json input.reflections=indexed.pickle output.prefix=tst_prefix
    dials.reindex input.reflections=indexed.pickle input.experiments=tst_prefixbravais_setting_6.json change_of_basis_op=b-c,b+c,a output.experiments=tst_n_reindexed_experiments.json output.reflections=tst_n_reindexed_experiments.pickle

    "or"

    dials.refine_bravais_settings experiments.json indexed.pickle
    dials.reindex indexed.pickle change_of_basis_op=b-c,b+c,a bravais_setting_6.json
    .

    dials.refine reindexed_experiments.json reindexed_reflections.pickle
    dials.integrate integration.mp.nproc=4 refined_experiments.json refined.pickle
    '''

    #TODO make sure new step is compatible with previous
    cmd_lst_to_run = []
    cmd_lst_to_run.append("dials." + cmd_lst[0])
    for tmp_par in cmd_lst[1:]:
        cmd_lst_to_run.append(tmp_par)

    if( cmd_lst[0] == "import" ):
        uni_step_obj.json_file_out = str(uni_step_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + uni_step_obj.json_file_out
        cmd_lst_to_run.append(output_str)
        #TODO make sure import without arguments does NOT run

    elif( cmd_lst[0] == "find_spots" ):
        json_file_in = uni_step_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        cmd_lst_to_run.append(input_str)

        uni_step_obj.json_file_out = str(uni_step_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + uni_step_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        uni_step_obj.pickle_file_out = str(uni_step_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + uni_step_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

    elif( cmd_lst[0] == "index" ):
        json_file_in = uni_step_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        cmd_lst_to_run.append(input_str)

        pickle_file_in = uni_step_obj.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        uni_step_obj.json_file_out = str(uni_step_obj.lin_num) + "_experiments.json"
        output_str = "output.experiments=" + uni_step_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        uni_step_obj.pickle_file_out = str(uni_step_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + uni_step_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

        '''
    dials.refine_bravais_settings input.experiments=experiments.json input.reflections=indexed.pickle output.prefix=tst_prefix
    dials.reindex input.reflections=indexed.pickle input.experiments=tst_prefixbravais_setting_6.json change_of_basis_op=b-c,b+c,a output.experiments=tst_n_reindexed_experiments.json output.reflections=tst_n_reindexed_experiments.pickle
        '''
    elif( cmd_lst[0] == "refine_bravais_settings" ):
        json_file_in = uni_step_obj.prev_step.json_file_out
        input_str = "input.experiments=" + json_file_in
        cmd_lst_to_run.append(input_str)

        pickle_file_in = uni_step_obj.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        prefix_str = "lin_" + str(uni_step_obj.lin_num) + "_"
        uni_step_obj.prefix_out = prefix_str
        output_str = "output.prefix=" + uni_step_obj.prefix_out
        cmd_lst_to_run.append(output_str)

        uni_step_obj.json_file_out = prefix_str + "_bravais_summary.json"




        '''
        import json

        with open("lin_7_bravais_summary.json") as summary_file:
            j_obj = json.load(summary_file)
            #solution = max(map(int, j_obj.keys()))

        #change_of_basis_op = j_obj[str(solution)]['cb_op']
        change_of_basis_op = j_obj["2"]['cb_op']

        print "change_of_basis_op =", change_of_basis_op
        '''


    elif( cmd_lst[0] == "refine" or cmd_lst[0] == "integrate" ):
        json_file_in = uni_step_obj.prev_step.json_file_out
        input_str = "input.experiments=" + json_file_in
        cmd_lst_to_run.append(input_str)

        pickle_file_in = uni_step_obj.prev_step.pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        cmd_lst_to_run.append(input_str)

        uni_step_obj.json_file_out = str(uni_step_obj.lin_num) + "_experiments.json"
        output_str = "output.experiments=" + uni_step_obj.json_file_out
        cmd_lst_to_run.append(output_str)

        uni_step_obj.pickle_file_out = str(uni_step_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + uni_step_obj.pickle_file_out
        cmd_lst_to_run.append(output_str)

    elif( cmd_lst[0] == "export" ):
        cmd_lst_to_run.append(uni_step_obj.prev_step.json_file_out)
        cmd_lst_to_run.append(uni_step_obj.prev_step.pickle_file_out)

        file_out = str(uni_step_obj.lin_num) + "_integrated.mtz"
        output_str = "mtz.hklout=" + file_out
        cmd_lst_to_run.append(output_str)

    return cmd_lst_to_run

def generate_report(uni_step_obj):
    rep_out = None
    try:
        if( uni_step_obj.command[0] in uni_step_obj.dials_com_lst[1:-1] ):
            current_lin = uni_step_obj.lin_num
            refl_inp = uni_step_obj.pickle_file_out
            deps_outp = "output.external_dependencies=local"
            htm_fil = str(current_lin) + "_report.html"
            html_outp = "output.html=" + htm_fil
            if( uni_step_obj.command[0] == "find_spots" ):
                rep_cmd = ["dials.report", refl_inp, deps_outp, html_outp]

            else:
                exp_inp = uni_step_obj.json_file_out
                rep_cmd = ["dials.report", exp_inp, refl_inp, deps_outp, html_outp]

            print "rep_cmd =", rep_cmd

            try:
                gen_rep_proc = subprocess.Popen(rep_cmd)
                gen_rep_proc.wait()
                rep_out = uni_step_obj.work_dir + "/" + htm_fil
                print "generated report at: ", rep_out

            except:
                rep_out = None
                print "Someting went wrong in report level 2"

        else:
            print "NO report needed for this step"
            rep_out = None

    except:
        rep_out = None
        print "Someting went wrong in report level 1"

    return rep_out

class DialsCommand(object):
    def __init__(self):
        print "creating new DialsCommand (obj)"

    def __call__(self, lst_cmd_to_run = None, ref_to_class = None):
        try:
            print "\n << running >>", lst_cmd_to_run
            my_process = subprocess.Popen(lst_cmd_to_run,
                                          stdout = subprocess.PIPE,
                                          stderr = subprocess.STDOUT,
                                          bufsize = 1)

            for line in iter(my_process.stdout.readline, b''):
                single_line = line[0:len(line)-1]
                try:
                    ref_to_class.emit_print_signal(single_line)

                except:
                    print single_line

            my_process.wait()
            my_process.stdout.close()
            if( my_process.poll() == 0 ):
                local_success = True

            else:
                local_success = False

        except:
            local_success = False
            print "\n FAIL call"

        return local_success


def print_list(lst, curr):
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
        self.tree_print(my_runner.current)
        print "---------------------" + self.max_indent * self.ind_lin


    def add_tree(self, step = None, indent = None):
        if( step.success == True ):
            stp_prn = " S "

        elif( step.success == False ):
            stp_prn = " F "

        else:
            stp_prn = " N "

        str_lin_num = "{0:3}".format(int(step.lin_num))

        stp_prn += str_lin_num + self.ind_spc * indent + "   \___"
        try:
            stp_prn += str(step.command[0])

        except:
            stp_prn += "None"

        self.str_lst.append([stp_prn, indent, int(step.lin_num)])
        try:
            for line in step.next_step_list:
                new_indent = indent + 1
                self.add_tree(step = line, indent = new_indent)

        except:
            new_indent = int(new_indent)
            if( new_indent > self.max_indent ):
                self.max_indent = new_indent


    def tree_print(self, curr):
        self.tree_dat = []
        for tmp_lst in self.str_lst:
            self.tree_dat.append(tmp_lst)

        for pos, loc_lst in enumerate(self.tree_dat):
            if(pos > 0):
                if( loc_lst[1] < self.tree_dat[pos - 1][1] ):
                    for up_pos in xrange(pos - 1, 0, -1):
                        pos_in_str = loc_lst[1] * len(self.ind_spc) + 9
                        left_side = self.tree_dat[up_pos][0][0:pos_in_str]
                        right_side = self.tree_dat[up_pos][0][pos_in_str + 1:]
                        if( self.tree_dat[up_pos][1] > loc_lst[1] ):
                            self.tree_dat[up_pos][0] = left_side + "|" + right_side

                        elif( self.tree_dat[up_pos][1] == loc_lst[1] ):
                            break

            if( loc_lst[2] == curr ):
                lng = len(self.ind_spc) * self.max_indent + 22
                lng_lft = lng - len(self.tree_dat[pos][0])
                str_here = lng_lft * " "
                self.tree_dat[pos][0] += str_here + "   <<< here "

        for prn_str in self.tree_dat:
            print prn_str[0]

