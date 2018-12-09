"""
DUI's utilities

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

import logging
import os
import subprocess
import sys

import psutil

from .cli_utils import get_next_step, sys_arg, get_phil_par
from .qt import (
    QApplication,
    QDialog,
    QFont,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QSize,
    QSizePolicy,
    QStandardItem,
    QStandardItemModel,
    QStyleFactory,
    Qt,
    QT5,
    QTextEdit,
    QThread,
    QTreeView,
    QVBoxLayout,
    QWidget,
    Signal,
)

logger = logging.getLogger(__name__)


def try_find_prev_mask_pickle(cur_nod):
    pickle_path = None
    my_node = cur_nod
    while pickle_path is None:
        my_node = my_node.prev_step
        try:
            if my_node.command_lst[0] == "find_spots":
                logger.debug("found find_spots")
                for command in my_node.command_lst:
                    if command.startswith("spotfinder.lookup.mask="):
                        logger.debug("Found mask.pickle")
                        logger.debug(my_node.command_lst)
                        pickle_path = command[23:]
                        logger.debug("\n my_path = %s %s", pickle_path, "\n")
                        if os.path.isfile(pickle_path):
                            logger.debug("file is still there")

                        else:
                            logger.debug("file no longer there")
                            pickle_path = None
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("not getting there")
            return None

    return pickle_path


def kill_w_child(pid_num):
    """Kills a process and it's entire child process tree.

    Args:
        pid_num (int): The PID of the parent process to kill
    """
    logger.debug("attempting to kill pid #: %s", pid_num)
    try:
        parent_proc = psutil.Process(pid_num)
        for child in parent_proc.children(
            recursive=True
        ):  # or parent_proc.children() for recursive=False
            child.kill()

        parent_proc.kill()

    except Exception as e:
        logger.debug("\n\n failed to kill process(es): %s", e)


def get_main_path():
    return str(os.path.dirname(os.path.abspath(__file__)))


def get_import_run_string(in_str_lst):
    """???UNCERTAIN ON BEHAVIOUR???
    Appears to calculate the dials.import filename, image_range string

    Args:
        in_str_lst ([str]): List of files to open

    Returns:
        (Tuple[str,str]):
            dir_path, import_string where dir_path is the location of the
            data, and import_string is the string containing parts to pass
            to dials.import.
    """
    logger.debug("in_str_lst = %s", in_str_lst)

    selected_file_path = str(in_str_lst[0])
    logger.debug("selected_file_path = %s", selected_file_path)

    fnd_sep = False
    sep_chr = None
    for pos, single_char in enumerate(selected_file_path):
        if single_char == "/" or single_char == "\\":
            dir_pos_sep = pos

            if fnd_sep and sep_chr != single_char:
                logger.debug("inconsistent dir separator")
                return None

            fnd_sep = True
            sep_chr = single_char

    if not fnd_sep:
        logger.debug("Failed to find dir path")
        return None

    dir_path = selected_file_path[:dir_pos_sep]
    # Check to see if this is identical to dirname
    if dir_path != os.path.dirname(selected_file_path):
        logger.warning(
            "Validation: get_import_run_string '%s' != '%s'",
            dir_path,
            os.path.dirname(selected_file_path),
        )

    # TODO test if the next << if >> is actually needed
    if dir_path[0:3] == "(u'":
        logger.debug('dir_path[0:3] == "(u\'"')
        dir_path = dir_path[3:]

    templ_r_side = selected_file_path[dir_pos_sep:]

    for pos, single_char in reversed(list(enumerate(templ_r_side))):
        if single_char == ".":
            ext_pos_sep = pos

    left_sd_name = templ_r_side[:ext_pos_sep]
    ext_name = templ_r_side[ext_pos_sep:]
    if ext_name == ".h5" or ext_name == ".nxs":
        logger.debug("found h5 or nxs file")
        file_name = left_sd_name
        file_name = file_name + ext_name
        tail_size = 0

    else:
        file_name = left_sd_name

        max_tail_size = int(len(templ_r_side) / 3)
        for tail_size in xrange(max_tail_size):
            prev_str = file_name
            pos_to_replase = len(file_name) - tail_size - 1
            for num_char in "0123456789":
                if file_name[pos_to_replase] == num_char:
                    file_name = (
                        file_name[:pos_to_replase]
                        + "#"
                        + file_name[pos_to_replase + 1 :]
                    )

            if prev_str == file_name:
                break

        file_name = file_name + ext_name

    if in_str_lst and len(in_str_lst) == 1:
        out_str = dir_path + file_name
        img_range = None

    else:
        str_lst = []
        for single_qstring in in_str_lst:
            str_lst.append(str(single_qstring))

        out_str = ""
        pos_last_num = 0

        for pos in xrange(len(str_lst[0])):
            all_equal = True
            single_char = str_lst[0][pos]
            for single_string in str_lst:
                try:
                    if single_string[pos] != single_char:
                        all_equal = False
                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error("Caught unknown exception type: %s", e)
                    all_equal = False

            if all_equal:
                out_str = out_str + single_char

            else:
                out_str = out_str + "#"
                pos_last_num = pos

        pos_last_num += 1

        logger.debug("pos_last_num = %s", pos_last_num)

        if pos_last_num > 1:
            lst_num_str = []
            try:

                for single_string in str_lst:
                    lst_num_str.append(
                        int(single_string[pos_last_num - tail_size : pos_last_num])
                    )

                logger.debug("lst_num_str = %s", lst_num_str)
                img_range = [min(lst_num_str), max(lst_num_str)]

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.error("Caught unknown exception type: %s", e)
                logger.debug("something went wrong with the range thing 01")
                img_range = None
        else:
            logger.debug("something went wrong with the range thing 02")
            img_range = None

    logger.debug("out_str( template mode ) = %s", out_str)

    new_cmd = ""
    for single_char in out_str:

        if single_char != "#":
            new_cmd += single_char

        elif prev_char != "#":
            new_cmd += "*"

        prev_char = single_char

    out_str = new_cmd
    logger.debug("img_range = %s", img_range)

    if img_range is not None:
        out_str += " image_range=" + str(img_range[0]) + "," + str(img_range[1])

    logger.debug("out_str( * mode ) = %s %s", out_str, "\n")
    logger.debug("dir_path = %s", dir_path)

    return dir_path, out_str


def build_label(com_nam):

    label_connects = {
        "import": "import",
        "find_spots": "find  ",
        "index": "index",
        "refine_bravais_settings": "lattice",
        "refine": "refine",
        "integrate": "integrate",
        "symmetry": "symmetry",
        "scale": "scale",
        "export": "export",
    }

    return "\n" * 2 + label_connects[com_nam]


def build_ttip(com_nam):

    tip_connects = {
        "import": " dials.import ...",
        "find_spots": " dials.find_spots ...",
        "index": " dials.index ...",
        "refine_bravais_settings": " dials.refine_bravais_settings\n"
        + "         + \n"
        + " dials.reindex ...",
        "refine": " dials.refine ...",
        "integrate": " dials.integrate ...",
        "symmetry": " dials.symmetry ...",
        "scale": " dials.scale ...",
        "export": " dials.export ...",
    }

    return tip_connects[com_nam]


def build_command_tip(command_lst):
    if command_lst == [None]:
        str_tip = "?"

    else:
        str_tip = "dials." + str(command_lst[0])
        for new_cmd in command_lst[1:]:
            str_tip += "\n  " + str(new_cmd)

    return str_tip


def update_info(main_obj):

    main_obj.cli_tree_output(main_obj.idials_runner)
    main_obj.cur_html = main_obj.idials_runner.get_html_report()

    if main_obj.view_tab_num == 2:
        main_obj.web_view.update_page(main_obj.cur_html)

    new_log = main_obj.idials_runner.get_log_path()

    tmp_curr = main_obj.idials_runner.current_node

    main_obj.cli_out.clear()
    main_obj.cli_out.make_green()
    main_obj.cur_log = new_log
    main_obj.cli_out.refresh_txt(main_obj.cur_log, tmp_curr)

    new_img_json = main_obj.idials_runner.get_datablock_path()
    new_ref_pikl = main_obj.idials_runner.get_reflections_path()

    if main_obj.view_tab_num == 0:

        if main_obj.cur_json != new_img_json:
            main_obj.cur_json = new_img_json
            # TODO check if next line should run ALLWAYS
            main_obj.img_view.contrast_initiated = False
            main_obj.img_view.ini_datablock(main_obj.cur_json)

        if main_obj.cur_pick != new_ref_pikl:
            main_obj.cur_pick = new_ref_pikl
            main_obj.img_view.ini_reflection_table(main_obj.cur_pick)

    if tmp_curr.success is None:
        tmp_curr = tmp_curr.prev_step

    uni_json = tmp_curr.json_file_out

    main_obj.info_widget.update_data(
        exp_json_path=uni_json, refl_pikl_path=new_ref_pikl
    )

    main_obj.img_view.update_exp(main_obj.info_widget.all_data.ref2exp)

    main_obj.ext_view.update_data(new_pick=new_ref_pikl, new_json=uni_json)

    try:
        xb = main_obj.info_widget.all_data.xb / main_obj.info_widget.all_data.x_px_size
        yb = main_obj.info_widget.all_data.yb / main_obj.info_widget.all_data.y_px_size

    except BaseException as e:
        # We don't want to catch bare exceptions but don't know
        # what this was supposed to catch. Log it.
        logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
        xb, yb = None, None

    main_obj.img_view.update_beam_centre(xb, yb)


def update_pbar_msg(main_obj):
    tmp_curr = main_obj.idials_runner.current_node
    txt = str(tmp_curr.command_lst[0])

    if tmp_curr.success is False:
        txt = "click << Retry >> or navigate backwards in the tree"
    elif txt == "refine_bravais_settings" and tmp_curr.success:
        txt = "click << Retry >> or navigate elsewhere in the tree"
    elif txt == "reindex" and tmp_curr.success is None:
        txt = "click the blue row to run reindex"
    elif tmp_curr.success is None:
        if tmp_curr.lin_num == 1:
            logger.debug("tmp_curr.lin_num == 1")
            current_widget = main_obj.centre_par_widget.step_param_widg.currentWidget()
            templ_text = current_widget.my_widget.simple_lin.text()
            logger.debug("templ_text = %s", templ_text)
            if templ_text == " ? ":
                txt = "click << Select File(s) >> or edit input line "
            else:
                txt = "click dials icon to run import"
        else:
            txt = "click dials icon to run " + txt
    else:
        nxt_cmd = get_next_step(tmp_curr)

        if nxt_cmd is None:
            txt = "Done"
        else:
            lab_nxt_cmd = get_lab_txt(nxt_cmd)
            txt = "click <<" + lab_nxt_cmd + ">> to go ahead, or click << Retry >>"

    main_obj.txt_bar.setText(txt)
    logger.debug("update_pbar_msg = %s", txt)


def get_lab_txt(com_nam):

    cmd_to_labl = {
        "import": " import ",
        "find_spots": " find ",
        "index": " index ",
        "refine_bravais_settings": " lattice ",
        "refine": " refine ",
        "integrate": " integrate",
        "symmetry": " symmetry",
        "scale": " scale",
        "export": " export",
    }

    new_com_nam = cmd_to_labl[com_nam]

    return new_com_nam


class MyQButton(QPushButton):
    def __init__(self, text="", parent=None):
        super(MyQButton, self).__init__()
        self.setContentsMargins(-5, -1, -5, -1)

    def intro_content(self, my_text, my_icon, my_tool_tip):

        self.setIcon(my_icon)
        self.setIconSize(QSize(31, 30))

        self.setToolTip(my_tool_tip)

        btn_txt = build_label(my_text)

        v_box = QVBoxLayout()
        v_box.insertSpacing(1, 4)

        h_box_space = QHBoxLayout()
        h_box_space.insertSpacing(1, 62)
        v_box.addLayout(h_box_space)

        h_box_label = QHBoxLayout()
        h_box_label.addStretch()

        my_font = QFont()
        sys_font_point_size = my_font.pointSize()
        my_font.setPointSize(sys_font_point_size - 2)

        my_label = QLabel(btn_txt)
        my_label.setMargin(1)
        my_label.setFont(my_font)

        h_box_label.addWidget(my_label)
        h_box_label.addStretch()

        v_box.addLayout(h_box_label)
        self.cmd_n1 = my_text
        self.setLayout(v_box)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.show()


class TreeNavWidget(QTreeView):
    def __init__(self, parent=None):
        super(TreeNavWidget, self).__init__()
        logger.debug("TreeNavWidget(__init__)")
        self.setSortingEnabled(False)
        self.setAnimated(True)
        self.setIndentation(10)

        header_view = self.header()
        if QT5:
            header_view.setSectionResizeMode(QHeaderView.ResizeToContents)
        else:
            header_view.setResizeMode(QHeaderView.ResizeToContents)
        header_view.setStretchLastSection(True)

    def update_me(self, root_node, lst_path_idx):
        self.lst_idx = lst_path_idx

        logger.debug(self.lst_idx)

        self.std_mod = QStandardItemModel(self)
        self.recursive_node(root_node, self.std_mod)

        self.std_mod.setHorizontalHeaderLabels([" History Tree "])
        self.setModel(self.std_mod)

        # self.update()
        self.expandAll()

    def recursive_node(self, root_node, item_in):
        if len(root_node.next_step_list) > 0:
            for child_node in root_node.next_step_list:
                if child_node.command_lst != [None]:
                    child_node_name = str(child_node.command_lst[0])
                elif child_node.success is None:
                    child_node_name = "* None *"
                else:
                    child_node_name = " ? None ? "

                try:
                    child_node_tip = build_command_tip(child_node.command_lst)
                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    child_node_tip = "None"

                new_item = QStandardItem(child_node_name)
                new_item.setToolTip(child_node_tip)
                new_item.idials_node = child_node

                if self.lst_idx == child_node.lin_num:
                    new_item.setBackground(Qt.blue)
                    if child_node.success is None:
                        new_item.setForeground(Qt.green)
                    elif child_node.success is True:
                        new_item.setForeground(Qt.white)
                    elif child_node.success is False:
                        new_item.setForeground(Qt.red)
                else:
                    new_item.setBackground(Qt.white)
                    if child_node.success is None:
                        new_item.setForeground(Qt.green)
                    elif child_node.success is True:
                        new_item.setForeground(Qt.blue)
                    elif child_node.success is False:
                        new_item.setForeground(Qt.red)

                new_item.setEditable(False)  # not letting the user edit it

                self.recursive_node(child_node, new_item)
                item_in.appendRow(new_item)


class ViewerThread(QThread):
    """Tracks the lifetime of a subprocess

    Args:
        process (subprocess.Popen): The process to track
    """

    def __init__(self, process):
        super(ViewerThread, self).__init__()
        self.process = process

    def run(self):
        logger.debug("Hi from QThread(run)  ___________________<<< Before Loop >>>")

        self.process.wait()

        logger.debug("_________________________________________>>> Loop ended <<<")


class ExternalProcDialog(QDialog):
    """Create a pop-up modal dialog to wait for an external process

    Args:
        parent (QWidget): The parent for the dialog. Passed to QDialog.

    Attributes:
        outputFileFound (Signal):
            A named output file was found. Signal is called with a list
            of full paths to the output files.
    """

    outputFileFound = Signal(list)

    def __init__(self, parent=None):
        super(ExternalProcDialog, self).__init__(parent)

        vbox = QVBoxLayout()
        label = QLabel(
            (
                "Running a pop-up viewer ...\n\n"
                "remember to close the viewer before\n"
                "performing any other task"
            )
        )
        label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label)

        kl_but = QPushButton("Close pop-up viewer")
        kl_but.clicked.connect(self.kill_my_proc)
        vbox.addWidget(kl_but)

        self.setLayout(vbox)
        self.setFixedSize(self.sizeHint())
        self.setModal(True)
        self.setWindowTitle("External Tool")

        self.my_process = None
        self.check_for = []

    def run_my_proc(self, command, json_path, pickle_path, check_for=None):
        """Run a process.

        Args:
            command (str):      The command to run
            json_path (str):
                Path to the JSON file to pass in as first argument
            pickle_path (Sequence[Optional[str]]):
                An additional path to a pickle to pass in as an argument.
                Currently, all except the first argument is ignored.
            check_for (Sequence[str]):
                Files to look for. Anything named here will be removed
                before running, and a outputFileFound signal sent after
                running with a list of full paths to each file found.
        """

        # assert isinstance(json_path, basestring)
        # # This function previously had strings as default parameters
        # # but appears to only accept Indexable lists of strings. Make
        # # sure we never try to use strings
        # assert not isinstance(pickle_path, basestring)
        # # Since we ignore everything after [0] assert they are None
        # assert all(x is None for x in pickle_path[1:])
        # # Only one process running from each class
        # assert self.my_process is None

        # Build the command
        cmd_to_run = [command, str(json_path)]
        first_pikl_path = pickle_path[0]
        if first_pikl_path is not None:
            cmd_to_run.append(str(first_pikl_path))

        # Save the working directory
        self.cwd_path = os.path.join(sys_arg.directory, "dui_files")

        self.check_for = check_for or []
        # Store metadata about the files if they exist, to check if they changed
        self.check_file_status = {}
        for check_file in self.check_for:
            full_path = os.path.join(self.cwd_path, check_file)
            if os.path.exists(full_path):
                logger.debug("File %s exists - collecting metadata", full_path)
                self.check_file_status[check_file] = os.stat(full_path)

        logger.debug("\n running Popen>>>\n   " + " ".join(cmd_to_run) + "\n<<<")
        self.my_process = subprocess.Popen(args=cmd_to_run, cwd=self.cwd_path)
        logger.debug("Running PID {}".format(self.my_process.pid))

        # Track the process status in a separate thread
        self.thrd = ViewerThread(self.my_process)
        self.thrd.finished.connect(self.child_closed)
        self.thrd.start()

        # Show this dialog
        self.exec_()

    def kill_my_proc(self):
        """Kill the subprocess early"""
        logger.debug("self.kill_my_proc")
        kill_w_child(self.my_process.pid)
        self.my_process = None
        self._check_for_output_files()
        self.done(0)

    def child_closed(self):
        """The child process has closed by itself"""
        logger.debug("after ...close()")
        self.my_process = None
        self._check_for_output_files()
        # Just close ourself
        self.done(0)

    def closeEvent(self, event):
        """User has clicked 'close' window decorator on dialog box"""
        logger.debug("from << closeEvent  (QDialog) >>")
        self._check_for_output_files()
        self.kill_my_proc()

    def _check_for_output_files(self):
        """Send out any signals about created or changed output files"""
        found_checks = []
        for filename in self.check_for:
            full_path = os.path.join(self.cwd_path, filename)
            if filename in self.check_file_status:
                # If this file existed, see if it has changed
                try:
                    new_stat = os.stat(full_path)
                    old_stat = self.check_file_status[filename]
                    if (new_stat.st_mtime, new_stat.st_size) != (
                        old_stat.st_mtime,
                        old_stat.st_size,
                    ):
                        logger.info(
                            "Size/mtime of %s has changed - reading as new file",
                            filename,
                        )
                        found_checks.append(full_path)
                except OSError as e:
                    logger.warning(
                        "OSError (%s) trying to stat file that previously existed", e
                    )
            elif os.path.isfile(full_path):
                # The file didn't exist before - definitely new!
                logger.debug("Found output file {}".format(filename))
                found_checks.append(full_path)

        if found_checks:
            self.outputFileFound.emit(found_checks)


class OuterCaller(QWidget):

    pass_parmam_lst = Signal(list)

    def __init__(self):
        super(OuterCaller, self).__init__()

        v_box = QVBoxLayout()

        recip_lat_but = QPushButton("\n Open Reciprocal Lattice Viewer \n")
        recip_lat_but.clicked.connect(self.run_recip_dialg)
        v_box.addWidget(recip_lat_but)

        img_but = QPushButton("\n Open Image Viewer \n")
        img_but.clicked.connect(self.run_img_dialg)
        v_box.addWidget(img_but)

        self.diag = ExternalProcDialog(parent=self.window())
        self.diag.outputFileFound.connect(self.check_for_phil)
        self.setLayout(v_box)
        self.show()

    def update_data(self, new_pick=None, new_json=None):
        self.my_pick = new_pick
        self.my_json = new_json

    def run_recip_dialg(self):
        self.diag.run_my_proc(
            "dials.reciprocal_lattice_viewer",
            json_path=self.my_json,
            pickle_path=self.my_pick,
        )

    def run_img_dialg(self):
        self.diag.run_my_proc(
            "dials.image_viewer",
            json_path=self.my_json,
            pickle_path=self.my_pick,
            check_for=["find_spots.phil", "mask.pickle"],
        )

    def check_for_phil(self, output_files):
        """Slot function triggered by new files created by external process"""
        logger.debug("Output files: %s", output_files)

        for filename in output_files:
            if filename.endswith("find_spots.phil"):
                logger.debug("Reading spotfinding settings: %s %s", filename, "\n")
                lst_params = get_phil_par(filename)
                logger.debug("Emitting %s", repr(lst_params))
                self.pass_parmam_lst.emit(lst_params)
            elif filename.endswith("mask.pickle"):
                logger.debug("Found mask; emitting")
                # As a quick hack, broadcast lookup.mask and rewrite in catch
                phil_parms = ["lookup.mask={}".format(filename)]
                self.pass_parmam_lst.emit(phil_parms)
            else:
                logger.debug("Not sure how to handle %s", filename)


class CliOutView(QTextEdit):
    def __init__(self, app=None):
        super(CliOutView, self).__init__()
        self.setFont(QFont("Monospace", 10, QFont.Bold))
        self.make_green()

    def add_txt(self, str_to_print):
        try:
            ed_str = str(str_to_print).rstrip()
            self.append(ed_str)
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("unwritable char << %s %s", str_to_print, ">>")

    def make_red(self):
        logger.debug("turning log fonts to RED")
        style_orign = "color: rgba(220, 0, 0, 255)"
        self.setStyleSheet(style_orign)

    def make_green(self):
        logger.debug("turning log fonts to GREEN")
        style_orign = "color: rgba(0, 125, 0, 255)"
        self.setStyleSheet(style_orign)

    def make_blue(self):
        logger.debug("turning log fonts to BLUE")
        style_orign = "color: rgba(0, 0, 125, 255)"
        self.setStyleSheet(style_orign)

    def refresh_txt(self, path_to_log, curr_step=None):
        success = curr_step.success

        if success is True:
            self.make_blue()
        elif success is False:
            self.make_red()
            path_to_log = curr_step.err_file_out
        else:
            self.make_green()

        logger.debug(" path_to_log = %s", path_to_log)

        try:
            fil_obj = open(path_to_log, "r")
            lst_lin = fil_obj.readlines()
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("Failed to read log file")
            lst_lin = ["Ready to Run:"]
            self.make_green()

        self.clear()
        logger.debug("success = %s %s", success, "refresh_txt")

        for lin in lst_lin:
            self.add_txt(lin)


class Text_w_Bar(QProgressBar):
    def __init__(self, parent=None):
        super(Text_w_Bar, self).__init__()
        self.setAlignment(Qt.AlignCenter)
        self._text = ""
        logger.debug("test setStyle(QStyleFactory.create())")
        try:
            self.setStyle(QStyleFactory.create("cleanlooks"))
            # self.setStyle(QStyleFactory.create("Plastique"))
            # self.setStyle(QStyleFactory.create("cde"))
            # self.setStyle(QStyleFactory.create("motif"))
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("Failed to setStyle()")

    def setText(self, text):
        if len(text) > 2:
            self._text = text
            self.repaint()

    def text(self):
        return self._text

    def start_motion(self):
        logger.debug("starting motion")
        self.setRange(0, 0)

    def end_motion(self):
        self.setRange(0, 1)
        logger.debug("ending motion")


class MainWidget(QMainWindow):
    """
    This is a test GUI only used by the developer
    the user should NEVER see this code running
    """

    def __init__(self):
        super(MainWidget, self).__init__()
        main_box = QVBoxLayout()
        main_box.addWidget(QLabel("Test dummy GUI"))

        self.tst_view = CliOutView(app=app)
        main_box.addWidget(self.tst_view)
        self.txt_bar = Text_w_Bar()
        main_box.addWidget(self.txt_bar)

        btn1 = QPushButton("\n Do \n", self)
        btn1.clicked.connect(self.btn_1_clicked)
        main_box.addWidget(btn1)

        btn2 = QPushButton("\n Stop \n", self)
        btn2.clicked.connect(self.btn_2_clicked)
        main_box.addWidget(btn2)

        btn3 = QPushButton("\n refresh text \n", self)
        btn3.clicked.connect(self.btn_3_clicked)
        main_box.addWidget(btn3)

        self.n = 1

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)
        self.show()

    def btn_1_clicked(self):
        self.txt_bar.start_motion()
        self.n += 5
        my_text = str(self.n) + "aaaaa bbbbbb a ccccccccc a" + str(self.n * self.n)
        self.tst_view.add_txt(my_text)
        self.txt_bar.setText(my_text)

    def btn_2_clicked(self):
        my_text = " Done "
        self.tst_view.add_txt(my_text)
        self.txt_bar.setText(my_text)
        self.txt_bar.end_motion()

    def btn_3_clicked(self):
        # TODO update this path
        self.tst_view.refresh_txt(
            "../../dui_test/X4_wide/reuse_area/dials_files/2_find_spots.log"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
