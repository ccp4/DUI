#!/usr/bin/python
"""
DUI's management of CLI commands and navigation tree

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
"""

import logging
import os
import pickle
import shutil
import sys

from dui.cli_utils import (
    DialsCommand,
    TreeShow,
    build_command_lst,
    generate_predict,
    generate_report,
    get_next_step,
    sys_arg,
)

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


logger = logging.getLogger(__name__)


class CommandNode:
    dials_com_lst = [
        "import",
        "find_spots",
        "index",
        "refine_bravais_settings",
        "reindex",
        "refine",
        "integrate",
        "symmetry",
        "scale",
        "export",
        "generate_mask",
        "modify_geometry",
    ]

    def __init__(self, prev_step=None):
        self.lin_num = 0
        self.next_step_list = []
        self.prev_step = prev_step
        self.ll_command_lst = [[None]]
        self.success = None
        self.refl_pickle_file_out = None
        self.json_file_out = None
        self.phil_file_out = None
        self.log_file_out = None
        self.report_out = None
        self.predict_pickle_out = None
        self.err_file_out = None
        self.json_sym_out = None
        self.info_generating = None
        self.cmd_lst_to_run = [[None]]

        self.dials_command = DialsCommand()
        # self.work_dir = os.getcwd()

    def __call__(self, cmd_lst, ref_to_class):
        # logger.info(f"\n cmd_lst in = {cmd_lst}")
        self.ll_command_lst = list(cmd_lst)
        if cmd_lst == ["fail"]:
            # testing virtual failed step
            logger.debug("\n intentionally FAILED for testing \n")
            self.success = False

        else:
            if cmd_lst[0][0] in self.dials_com_lst:
                self.build_command(cmd_lst)
                self.success = self.dials_command(
                    lst_cmd_to_run=self.cmd_lst_to_run, ref_to_class=ref_to_class
                )
                if self.log_file_out is None:
                    logger.info("\n *** time to write ...log_file_out manually *** \n")

                    self.log_file_out = (
                        str(self.lin_num) + "_" + self.cmd_lst_to_run[0][0] + ".log"
                    )

                    cwd_path = os.path.join(sys_arg.directory, "dui_files")
                    file_path = os.path.join(cwd_path, self.log_file_out)

                    """
                    logger.info(f"..log_file_out = {file_path}")
                    logger.info(
                        "self.dials_command.tmp_std_all: {self.dials_command.tmp_std_all}",
                    )
                    """

                    fil_obj = open(file_path, "w")
                    for line_out in self.dials_command.tmp_std_all:
                        fil_obj.write(line_out)
                        fil_obj.write("\n")

                    fil_obj.close()

                logger.info("\n Done \n")
                # self.gen_repr_n_pred()

            else:
                logger.info("\n NOT dials command")
                logger.info("cmd_lst = %s", cmd_lst)
                self.success = False

        self.info_generating = False

    def gen_repr_n_pred(self, to_run=None):
        if (
            self.success is True
            and self.cmd_lst_to_run[0] != "dials.refine_bravais_settings"
        ):

            self.info_generating = True
            try:
                if to_run == "predict":
                    self.predict_pickle_out = generate_predict(self)

                elif to_run == "report":
                    self.report_out = generate_report(self)

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.debug(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("can NOT fork <None> node ")

        self.info_generating = False
        logger.info("\n _________________________________________gen_repr_n_pred\n")

    def edit_list(self, cmd_lst):
        self.ll_command_lst = cmd_lst

    def build_command(self, cmd_lst):
        self.cmd_lst_to_run = build_command_lst(self, cmd_lst)
        logger.info("cmd_lst_to_run(CommandNode) = %s", self.cmd_lst_to_run)

    def get_next_step(self):
        return get_next_step(self)


class Runner:
    def __init__(self):
        root_node = CommandNode(prev_step=None)
        root_node.success = True
        root_node.ll_command_lst = [["Root"]]
        self.step_list = [root_node]
        self.bigger_lin = 0
        self.current_line = self.bigger_lin
        self.create_step(root_node)

        logger.info("root_node.lin_num = %s", root_node.lin_num)
        # self.current_node = root_node

    def run(self, command, ref_to_class):
        if type(command) is str:
            cmd_lst = command.split()
        else:
            cmd_lst = command

        if cmd_lst[0] == "goto":
            logger.info("doing << goto >>")
            self.goto(int(cmd_lst[1]))

        elif cmd_lst == ["clean"]:
            self.clean()

        elif cmd_lst == ["mkchi"]:
            self.create_step(self.current_node)

        elif cmd_lst == ["mksib"]:
            old_command_lst = list(self.current_node.ll_command_lst)
            self.goto_prev()
            logger.info("forking")
            self.create_step(self.current_node)
            self.current_node.edit_list(old_command_lst)

        else:
            if self.current_node.success is True:
                self.goto_prev()
                logger.info("forking")
                self.create_step(self.current_node)

            self.current_node(cmd_lst, ref_to_class)
            if self.current_node.success is not True:
                logger.info("failed step")

    def clean(self):
        logger.debug("\n Cleaning")
        logger.debug("self.current_line = %s", self.current_line)

        lst_to_rm = []

        for node in self.step_list:
            if (
                node != self.current_node
                and node.success is None
                # TODO test further if the next line needs removing
                # and len(node.prev_step.next_step_list) > 1
            ):
                lst_to_rm.append(node)

        for node in lst_to_rm:
            node.prev_step.next_step_list.remove(node)
            self.step_list.remove(node)

        logger.debug("self.current_line = %s %s", self.current_line, "\n")

    def create_step(self, prev_step):
        new_step = CommandNode(prev_step=prev_step)
        self.bigger_lin += 1
        new_step.lin_num = self.bigger_lin
        prev_step.next_step_list.append(new_step)
        self.step_list.append(new_step)
        self.goto(self.bigger_lin)

    def goto_prev(self):
        try:
            self.goto(self.current_node.prev_step.lin_num)

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("can NOT fork <None> node ")

    def goto(self, new_lin):
        self.current_line = new_lin

        for node in self.step_list:
            if node.lin_num == self.current_line:
                self.current_node = node

    def get_current_node(self):
        return self.current_node

    def get_html_report(self):

        try:
            html_rep = self.current_node.report_out

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            html_rep = None

        return html_rep

    def get_datablock_path(self):

        tmp_cur = self.current_node
        path_to_json = None

        while True:
            if tmp_cur.ll_command_lst[0] == [None]:
                tmp_cur = tmp_cur.prev_step

            elif tmp_cur.success is True and tmp_cur.ll_command_lst[0][0] == "import":
                path_to_json = tmp_cur.json_file_out
                break

            elif tmp_cur.ll_command_lst[0][0] == "Root" or tmp_cur.success is False:
                break

            else:
                tmp_cur = tmp_cur.prev_step

        return path_to_json

    def get_log_path(self):

        path_to_log = None

        try:
            path_to_log = self.current_node.log_file_out

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch
            logger.info("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.info("failed to retrieve log path")

        return path_to_log

    def get_experiment_path(self):
        path_to_json = None
        tmp_cur = self.current_node
        if tmp_cur.ll_command_lst[0] == [None]:
            tmp_cur = tmp_cur.prev_step

        if (
            tmp_cur.ll_command_lst[0][0] != "Root"
            and tmp_cur.ll_command_lst[0][0] != "import"
            and tmp_cur.ll_command_lst[0][0] != "find_spots"
            and tmp_cur.success is True
        ):

            try:
                path_to_json = tmp_cur.json_file_out

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.debug(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("no experimet json file available")

        return path_to_json

    def get_reflections_path(self):
        tmp_cur = self.current_node
        if tmp_cur.ll_command_lst[0] == [None]:
            tmp_cur = tmp_cur.prev_step

        if (
            tmp_cur.ll_command_lst[0][0] == "Root"
            or tmp_cur.ll_command_lst[0][0] == "import"
            or tmp_cur.success is not True
        ):
            return None, None

        ref_pkl = None
        pre_pkl = None

        try:
            ref_pkl = tmp_cur.refl_pickle_file_out
            pre_pkl = tmp_cur.predict_pickle_out

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("no pickle file available")

        return ref_pkl, pre_pkl

    def get_next_from_here(self):
        return self.current_node.get_next_step()


if __name__ == "__main__" and __package__ is None:

    tree_output = TreeShow()
    storage_path = sys_arg.directory

    try:
        with open(storage_path + "/dui_files/bkp.pickle", "rb") as bkp_in:
            idials_runner = pickle.load(bkp_in)

        # TODO sometimes the following error appears
        # Attribute not found
        # 'module' object has no attribute 'CommandNode'

    except Exception as e:
        logger.info("%s: %s", type(e).__name__, e)
        idials_runner = Runner()
        try:
            shutil.rmtree(storage_path + "/dui_files")

        except OSError:
            logger.info('failed to do "shutil.rmtree("/dui_files")"')

        os.mkdir(storage_path + "/dui_files")

    tree_output(idials_runner)

    command = ""
    while command.strip() != "exit" and command.strip() != "quit":
        try:
            inp_str = "lin [" + str(idials_runner.current_line) + "] >>> "
            command = str(input(inp_str))

        except EOFError:
            logger.info("Caught << EOFError >>")
            logger.info(" ... interrupting")
            sys.exit(0)

        except BaseException as e:
            logger.info("Caught << some error >> %s", e)
            logger.info(" ... interrupting")
            sys.exit(1)

        logger.info("command = %s", command)
        if command[0:5] == "goto ":
            idials_runner.run(command.split(" "), None)
            tree_output(idials_runner)

        else:
            idials_runner.run([command.split(" ")], None)
            tree_output(idials_runner)

            idials_runner.run(["mkchi"], None)
            tree_output(idials_runner)

        with open(storage_path + "/dui_files/bkp.pickle", "wb") as bkp_out:
            pickle.dump(idials_runner, bkp_out)
