#!/usr/bin/python
"""
mini_idials navigation tree utilities

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
"""
from __future__ import absolute_import, division, print_function

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import json
import logging
import os
import subprocess

import libtbx.phil
from six.moves import range

logger = logging.getLogger(__name__)


class SysArgvData(object):
    """
    Some data related to how the GUI gets launched from CLI
    """

    template = None
    directory = str(os.getcwd())


sys_arg = SysArgvData()


def prn_lst_lst_cmd(last_idials_node):
    cur_nod = last_idials_node
    lst_simpl_cmd = []
    lst_full_cmd = []

    while True:
        if cur_nod.ll_command_lst[0] == ["Root"] or cur_nod.lin_num == 0:
            break

        # TODO make a loop thru the list of posible commands
        l_n = str(cur_nod.lin_num)
        lst_simpl_cmd.append(
            "command_lst[" + l_n + "] = " + str(cur_nod.ll_command_lst[0])
        )
        for one_cmd in reversed(cur_nod.dials_command.full_cmd_lst):
            lst_full_cmd.append(one_cmd)

        cur_nod = cur_nod.prev_step

    for prn_lin in reversed(lst_simpl_cmd):
        logger.debug(prn_lin)

    sh_cmd_lst = []
    for prn_lin in reversed(lst_full_cmd):
        str_cmd = ""
        for cmd_par in prn_lin:
            str_cmd += " " + cmd_par

        sh_cmd_lst.append(str_cmd)

    print("All commands to get here:\n___________________________")
    for prn_lin in sh_cmd_lst:
        print(prn_lin)

    print("___________________________\n")


def get_next_step(node_obj):
    if node_obj.lin_num == 0:
        return "import"

    else:
        for pos, stp in enumerate(node_obj.dials_com_lst[0:-1]):
            if stp == node_obj.ll_command_lst[0][0]:
                nxt_str = node_obj.dials_com_lst[pos + 1]
                return nxt_str

    return None


class ScopeData(object):
    """
    class conceived to store only data related to the scope Phil object
    """

    pass


class tree_2_lineal(object):

    """
    Recursively navigates the Phil objects in a way that the final
    self.lst_obj is a lineal list without ramifications
    """

    def __init__(self, phl_obj):
        self.lst_obj = []
        self.deep_in_rec(phl_obj)

    def __call__(self):
        return self.lst_obj

    def deep_in_rec(self, phl_obj):

        for single_obj in phl_obj:
            if single_obj.is_definition:
                self.lst_obj.append(single_obj)

            elif single_obj.is_scope:
                scope_info = ScopeData()
                scope_info.is_definition = False
                self.lst_obj.append(scope_info)
                self.deep_in_rec(single_obj.objects)

            else:
                logger.debug(
                    "\n\n _____________ <<< WARNING neither definition or scope\n\n"
                )


def get_phil_par(path_to_file):

    logger.debug("path_to_file = %s", path_to_file)
    p_obj = libtbx.phil.parse(
        input_string=None,
        source_info=None,
        file_name=path_to_file,
        converter_registry=None,
        process_includes=False,
    )
    logger.debug("p_obj = %s", p_obj)
    lst_obj = tree_2_lineal(p_obj.objects)
    multipl_phil_lst = lst_obj()

    lst_str_commands = []

    for obj in multipl_phil_lst:
        if obj.is_definition:
            try:
                str_par = str(obj.full_path()) + "="
                str_val = ""
                obj_ext = obj.extract()
                logger.debug("obj_ext = %s", obj_ext)
                if type(obj_ext) is list:
                    for nm, single_val in enumerate(obj_ext):
                        if nm > 0:
                            str_val += ","

                        str_val += str(single_val)

                else:
                    str_val = str(obj_ext)

                str_par += str_val

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.debug(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("\n\n failed to get obj & par \n\n")

            lst_str_commands.append(str_par)

    logger.debug("\n lst_str_commands = %s", lst_str_commands)
    return lst_str_commands


def build_command_lst(node_obj, cmd_lst):

    # TODO make sure new step is compatible with previous

    cmd_lst_to_run = []

    lst_inner = []
    cmd_lst_ini = cmd_lst[0][0]

    lst_inner.append("dials." + cmd_lst_ini)
    if cmd_lst_ini != "reindex":
        for tmp_par in cmd_lst[0][1:]:
            lst_inner.append(tmp_par)

    run_path = sys_arg.directory + os.sep + "dui_files"

    if cmd_lst_ini == "import":
        node_obj.json_file_out = str(node_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + node_obj.json_file_out
        lst_inner.append(output_str)
        node_obj.log_file_out = str(node_obj.lin_num) + "_" + cmd_lst_ini + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        lst_inner.append(output_str)
        node_obj.debug_log_file_out = (
            str(node_obj.lin_num) + "_" + cmd_lst_ini + ".debug.log"
        )
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        lst_inner.append(output_str)
        #####################################################################
        # TODO make sure import without arguments does NOT run
        #####################################################################

    elif cmd_lst_ini == "find_spots":
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        lst_inner.append(input_str)
        node_obj.json_file_out = str(node_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + node_obj.json_file_out
        lst_inner.append(output_str)
        node_obj.refl_pickle_file_out = str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.refl_pickle_file_out
        lst_inner.append(output_str)
        node_obj.log_file_out = str(node_obj.lin_num) + "_" + cmd_lst_ini + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        lst_inner.append(output_str)
        node_obj.debug_log_file_out = (
            str(node_obj.lin_num) + "_" + cmd_lst_ini + ".debug.log"
        )
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        lst_inner.append(output_str)

    elif cmd_lst_ini == "index":
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        lst_inner.append(input_str)

        pickle_file_in = node_obj.prev_step.refl_pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        lst_inner.append(input_str)
        node_obj.json_file_out = str(node_obj.lin_num) + "_experiments.json"
        output_str = "output.experiments=" + node_obj.json_file_out
        lst_inner.append(output_str)
        node_obj.refl_pickle_file_out = str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.refl_pickle_file_out
        lst_inner.append(output_str)
        node_obj.log_file_out = str(node_obj.lin_num) + "_" + cmd_lst_ini + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        lst_inner.append(output_str)
        node_obj.debug_log_file_out = (
            str(node_obj.lin_num) + "_" + cmd_lst_ini + ".debug.log"
        )
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        lst_inner.append(output_str)

    elif cmd_lst_ini == "refine_bravais_settings":
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.experiments=" + json_file_in
        lst_inner.append(input_str)

        pickle_file_in = node_obj.prev_step.refl_pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        lst_inner.append(input_str)

        prefix_str = "lin_" + str(node_obj.lin_num) + "_"
        node_obj.prefix_out = prefix_str
        output_str = "output.prefix=" + node_obj.prefix_out
        lst_inner.append(output_str)

        node_obj.json_file_out = prefix_str + "bravais_summary.json"

        node_obj.log_file_out = str(node_obj.lin_num) + "_" + cmd_lst_ini + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        lst_inner.append(output_str)

        node_obj.debug_log_file_out = (
            str(node_obj.lin_num) + "_" + cmd_lst_ini + ".debug.log"
        )
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        lst_inner.append(output_str)

    elif cmd_lst_ini == "reindex":

        try:
            sol_str = str(cmd_lst[0][1])
            if sol_str[0:9] == "solution=":
                sol_num = int(sol_str[9:])

            else:
                print("\nDEFAULT  to sol_num = 1 \n")
                sol_num = 1

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            print("\n reindex \n exeption:", e, "type:", type(e))

            # getting to exeption: list index out of range
            # type: <type 'exceptions.IndexError'>

            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            sol_num = 1

        pickle_file_in = node_obj.prev_step.prev_step.refl_pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        lst_inner.append(input_str)

        json_file_tmp = node_obj.prev_step.json_file_out
        with open(run_path + os.sep + json_file_tmp) as summary_file:
            j_obj = json.load(summary_file)
        change_of_basis_op = j_obj[str(sol_num)]["cb_op"]

        input_str = "change_of_basis_op=" + str(change_of_basis_op)
        lst_inner.append(input_str)

        node_obj.json_file_out = (
            node_obj.prev_step.prefix_out + "bravais_setting_" + str(sol_num) + ".json"
        )

        node_obj.refl_pickle_file_out = str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.refl_pickle_file_out
        lst_inner.append(output_str)

    elif (
        cmd_lst_ini == "refine"
        or cmd_lst_ini == "integrate"
        or cmd_lst_ini == "scale"
        or cmd_lst_ini == "symmetry"
    ):

        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.experiments=" + json_file_in
        lst_inner.append(input_str)
        pickle_file_in = node_obj.prev_step.refl_pickle_file_out
        input_str = "input.reflections=" + pickle_file_in
        lst_inner.append(input_str)
        node_obj.json_file_out = str(node_obj.lin_num) + "_experiments.json"
        output_str = "output.experiments=" + node_obj.json_file_out
        lst_inner.append(output_str)
        node_obj.refl_pickle_file_out = str(node_obj.lin_num) + "_reflections.pickle"
        output_str = "output.reflections=" + node_obj.refl_pickle_file_out
        lst_inner.append(output_str)

        if cmd_lst_ini == "integrate":
            lst_inner.append("output.phil=" + str(node_obj.lin_num) + "_integrate.phil")

        node_obj.log_file_out = str(node_obj.lin_num) + "_" + cmd_lst_ini + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        lst_inner.append(output_str)

        node_obj.debug_log_file_out = (
            str(node_obj.lin_num) + "_" + cmd_lst_ini + ".debug.log"
        )

        if cmd_lst_ini == "scale":
            output_str = "output.debug.log=" + node_obj.debug_log_file_out

        else:
            output_str = "output.debug_log=" + node_obj.debug_log_file_out

        lst_inner.append(output_str)

        if cmd_lst_ini == "symmetry":

            node_obj.json_sym_out = (
                str(node_obj.lin_num) + "_" + cmd_lst_ini + ".symmetry.json"
            )
            output_str = "output.json=" + node_obj.json_sym_out
            lst_inner.append(output_str)

    elif cmd_lst_ini == "export":
        lst_inner.append(node_obj.prev_step.json_file_out)
        lst_inner.append(node_obj.prev_step.refl_pickle_file_out)
        node_obj.log_file_out = str(node_obj.lin_num) + "_" + cmd_lst_ini + ".log"
        output_str = "output.log=" + node_obj.log_file_out
        lst_inner.append(output_str)
        node_obj.debug_log_file_out = (
            str(node_obj.lin_num) + "_" + cmd_lst_ini + ".debug.log"
        )
        output_str = "output.debug_log=" + node_obj.debug_log_file_out
        lst_inner.append(output_str)

    elif cmd_lst_ini == "generate_mask":
        lst_inner1 = list(lst_inner)
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        lst_inner1.append(input_str)

        # TODO add this info to node_obj
        mask_file = str(node_obj.lin_num) + "_mask.pickle"
        lst_inner1.append("output.mask=" + mask_file)

        node_obj.json_file_out = str(node_obj.lin_num) + "_datablock.json"

        lst_inner = [
            "dials.apply_mask",
            "input.datablock=" + json_file_in,
            "input.mask=" + mask_file,
            "output.datablock=" + node_obj.json_file_out,
        ]
        cmd_lst_to_run.append(lst_inner1)

    elif cmd_lst_ini == "modify_geometry":
        lst_inner1 = list(lst_inner)
        json_file_in = node_obj.prev_step.json_file_out
        input_str = "input.datablock=" + json_file_in
        lst_inner.append(input_str)

        node_obj.json_file_out = str(node_obj.lin_num) + "_datablock.json"
        output_str = "output.datablock=" + node_obj.json_file_out
        lst_inner.append(output_str)


        print("\n modify_geometry \n")
        '''
        dials.modify_geometry input.datablock=1_datablock.json \
        geometry.detector.slow_fast_beam_centre=350,350 \
        output.datablock=2_datablock.json

        #################################################################
        '''


    cmd_lst_to_run.append(lst_inner)


    #print("\n\n test:", cmd_lst_to_run, "\n")

    return cmd_lst_to_run


def build_mask_command_lst(mask_itm_lst):

    to_run1 = ["generate_mask"]

    for item in mask_itm_lst:
        if item[0] == "rect":
            to_run1.append(
                "untrusted.rectangle="
                + str(item[1])
                + ","
                + str(item[2])
                + ","
                + str(item[3])
                + ","
                + str(item[4])
            )

        elif item[0] == "circ":
            to_run1.append(
                "untrusted.circle="
                + str(item[1])
                + ","
                + str(item[2])
                + ","
                + str(item[3])
            )

    to_run2 = ["apply_mask ..."]

    return [to_run1, to_run2]


def generate_predict(node_obj):
    pre_out = None
    cwd_path = os.path.join(sys_arg.directory, "dui_files")
    if node_obj.ll_command_lst[0][0] in node_obj.dials_com_lst[2:-1]:
        try:
            logger.debug("running predictions START")
            current_lin = node_obj.lin_num
            exp_inp = node_obj.json_file_out
            pre_fil = str(current_lin) + "_predict.pickle"
            pred_outp = " output=" + pre_fil
            pred_cmd = "dials.predict " + str(exp_inp) + pred_outp
            logger.debug("predict command:  %s %s", pred_cmd, "\n\n")

            gen_pred_proc = subprocess.Popen(pred_cmd, shell=True, cwd=cwd_path)
            gen_pred_proc.wait()

            tst_path = os.path.join(cwd_path, pre_fil)
            if os.path.exists(tst_path):
                logger.debug("\ngenerated predictions at:  %s %s", tst_path, "\n")
                pre_out = pre_fil

            else:
                logger.debug("\n path to predictions NOT generated")
                pre_out = None

            logger.debug("running predictions END")

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("Failed adding path to predictions")
            pre_out = None

    return pre_out


def generate_report(node_obj):

    rep_out = None

    if node_obj.ll_command_lst[0][0] in node_obj.dials_com_lst[1:-1]:
        logger.debug("running report START")
        current_lin = node_obj.lin_num
        refl_inp = node_obj.refl_pickle_file_out
        deps_outp = "output.external_dependencies=local"
        htm_fil = str(current_lin) + "_report.html"
        html_outp = "output.html=" + htm_fil
        if node_obj.ll_command_lst[0][0] == "find_spots":
            rep_cmd = "dials.report " + refl_inp + " " + deps_outp + " " + html_outp

        else:
            exp_inp = node_obj.json_file_out
            rep_cmd = (
                "dials.report "
                + str(exp_inp)
                + " "
                + str(refl_inp)
                + " "
                + deps_outp
                + " "
                + html_outp
            )

        logger.debug("rep_cmd = %s", rep_cmd)

        try:
            cwd_path = os.path.join(sys_arg.directory, "dui_files")
            gen_rep_proc = subprocess.Popen(rep_cmd, shell=True, cwd=cwd_path)
            gen_rep_proc.wait()

            rep_out = htm_fil
            logger.debug("generated report at:  %s", rep_out)

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            rep_out = None
            logger.debug("Someting went wrong in report level 2")

        logger.debug("running report END")

    else:
        logger.debug("NO report needed for this step")
        rep_out = None

    return rep_out


class DialsCommand(object):
    def __init__(self):
        logger.debug("creating new DialsCommand (obj)")
        self.full_cmd_lst = None

        os_name = os.name
        logger.debug("\n Running process on  %s %s", os_name, "\n\n")
        if os_name == "nt":
            self.use_shell = True

        else:
            self.use_shell = False

    def __call__(self, lst_cmd_to_run=None, ref_to_class=None):
        self.full_cmd_lst = []

        self.tmp_std_all = []
        for lst_single in lst_cmd_to_run:
            try:
                single_string = ""

                for lin_to_prn in lst_single:
                    logger.debug(lin_to_prn)

                    single_string += lin_to_prn
                    single_string += " "

                if self.use_shell:
                    run_cmd = single_string

                else:
                    run_cmd = lst_single

                cwd_path = os.path.join(sys_arg.directory, "dui_files")

                print("\nRunning:", run_cmd, "\n")

                my_process = subprocess.Popen(
                    run_cmd,
                    shell=self.use_shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    bufsize=1,
                    cwd=cwd_path,
                )
                self.my_pid = my_process.pid
                for line in iter(my_process.stdout.readline, b""):
                    single_line = line[0 : len(line) - 1]
                    # print(">>: ", single_line)
                    self.tmp_std_all.append(single_line)
                    try:
                        ref_to_class.emit_print_signal(single_line)

                    except AttributeError:
                        print(">>: ", single_line)

                my_process.wait()
                my_process.stdout.close()
                if my_process.poll() == 0:
                    local_success = True

                else:
                    local_success = False
                    # TODO handle error outputs
                    print("\n __________________ Failed ______________________ \n")
                    try:
                        ref_to_class.emit_fail_signal()
                        return False

                    except BaseException as e:
                        # We don't want to catch bare exceptions but don't know
                        # what this was supposed to catch. Log it.
                        logger.debug(
                            "Caught unknown exception type %s: %s", type(e).__name__, e
                        )
                        return False

                logger.debug("Done all step")

            except Exception as my_err:
                logger.debug("error = %s %s", my_err, "\n")
                local_success = False
                logger.debug("\n FAIL call")

            self.full_cmd_lst.append(lst_single)

        return local_success


def print_list(lst, curr):
    print("__________________________listing:")
    for uni in lst:
        # TODO loopthru all commands, in "both" lists
        stp_str = (
            str(uni.lin_num)
            + " "
            + str(uni.success)
            + " comm: "
            + str(uni.ll_command_lst[0])
        )

        try:
            stp_str += " prev: " + str(uni.prev_step.lin_num)
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            stp_str += " prev: None"

        stp_str += " nxt: "
        if len(uni.next_step_list) > 0:
            for nxt_uni in uni.next_step_list:
                stp_str += "  " + str(nxt_uni.lin_num)
        else:
            stp_str += "empty"

        if curr == uni.lin_num:
            stp_str += "                           <<< here I am <<<"

        print(stp_str)


class TreeShow(object):
    def __init__(self):
        self.ind_spc = "      "
        self.ind_lin = "------"

    def __call__(self, my_runner):

        #print("\n\n TreeShow debug \n my_runner.step_list:\n")
        #print_list(my_runner.step_list, my_runner.current_line)
        print("\n")

        print("")
        print("status ")
        print(" |  lin num ")
        print(" |   |  command ")
        print(" |   |   | ")
        print("------------------")
        self.max_indent = 0
        self.str_lst = []
        self.add_tree(step=my_runner.step_list[0], indent=0)
        self.tree_print(my_runner.current_line)
        # TODO maybe here goes a print print function instead of logger ...
        print("---------------------" + self.max_indent * self.ind_lin)

    def add_tree(self, step=None, indent=None):
        if step.success is True:
            stp_prn = " S "
        elif step.success is False:
            stp_prn = " F "
        else:
            stp_prn = " N "

        str_lin_num = "{0:3}".format(int(step.lin_num))

        stp_prn += str_lin_num + self.ind_spc * indent + r"   \___"
        stp_prn += str(step.ll_command_lst[0][0])

        self.str_lst.append([stp_prn, indent, int(step.lin_num)])
        new_indent = indent
        if len(step.next_step_list) > 0:
            for line in step.next_step_list:
                new_indent = indent + 1
                self.add_tree(step=line, indent=new_indent)

        else:
            new_indent = int(new_indent)
            if new_indent > self.max_indent:
                self.max_indent = new_indent

    def tree_print(self, curr):
        self.tree_dat = []
        for tmp_lst in self.str_lst:
            self.tree_dat.append(tmp_lst)

        for pos, loc_lst in enumerate(self.tree_dat):
            if pos > 0:
                if loc_lst[1] < self.tree_dat[pos - 1][1]:
                    for up_pos in range(pos - 1, 0, -1):
                        pos_in_str = loc_lst[1] * len(self.ind_spc) + 9
                        left_side = self.tree_dat[up_pos][0][0:pos_in_str]
                        right_side = self.tree_dat[up_pos][0][pos_in_str + 1 :]
                        if self.tree_dat[up_pos][1] > loc_lst[1]:
                            self.tree_dat[up_pos][0] = left_side + "|" + right_side

                        elif self.tree_dat[up_pos][1] == loc_lst[1]:
                            break

            if loc_lst[2] == curr:
                lng = len(self.ind_spc) * self.max_indent + 22
                lng_lft = lng - len(self.tree_dat[pos][0])
                str_here = lng_lft * " "
                self.tree_dat[pos][0] += str_here + "   <<< here "

        for prn_str in self.tree_dat:
            print(prn_str[0])
