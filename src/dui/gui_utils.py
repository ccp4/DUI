"""
DUI's utilities

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
"""
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
import re
import shutil
import subprocess
import sys
from collections import OrderedDict, namedtuple
from pathlib import Path
from typing import Iterable, List, Tuple

import psutil
from dxtbx.sequence_filenames import template_regex, template_regex_from_list

from .cli_utils import get_next_step, sys_arg
from .m_idials import generate_report
from .qt import (
    QDialog,
    QFont,
    QFontDatabase,
    QHeaderView,
    QIcon,
    QLabel,
    QProgressBar,
    QPushButton,
    QSize,
    QSizePolicy,
    QStandardItem,
    QStandardItemModel,
    QStyleFactory,
    Qt,
    QTextEdit,
    QThread,
    QToolButton,
    QTreeView,
    QVBoxLayout,
    QWidget,
    Signal,
)

logger = logging.getLogger(__name__)

# Basic tuple to store information about actions
ActionInformation = namedtuple(
    "ActionInformation", ["id", "label", "tooltip", "icon", "icon_disabled"]
)


def escaped_join(args: Iterable[str]) -> str:
    """Join a list of strings, escaping spaces if necessary"""
    return " ".join(x.replace(" ", r"\ ") for x in args)


# Basic implementation of a simple actions lookup table - not a perfect solution
# but allows partial refactoring to centralised previously scattered info
ACTIONS = OrderedDict(
    [
        (x.id, x)
        for x in [
            ActionInformation(
                id="import",
                label="import",
                tooltip="dials.import ...",
                icon="resources/import.png",
                icon_disabled="resources/import_grayed.png",
            ),
            ActionInformation(
                id="find_spots",
                label="find",
                tooltip="dials.find_spots ...",
                icon="resources/find_spots.png",
                icon_disabled="resources/find_spots_grayed.png",
            ),
            ActionInformation(
                id="index",
                label="index",
                tooltip="dials.index ...",
                icon="resources/index.png",
                icon_disabled="resources/index_grayed.png",
            ),
            ActionInformation(
                id="refine_bravais_settings",
                label="lattice",
                tooltip=" dials.refine_bravais_settings\n     +\ndials.reindex ...",
                icon="resources/reindex.png",
                icon_disabled="resources/reindex_grayed.png",
            ),
            ActionInformation(
                id="refine",
                label="refine",
                tooltip="dials.refine ...",
                icon="resources/refine.png",
                icon_disabled="resources/refine_grayed.png",
            ),
            ActionInformation(
                id="integrate",
                label="integrate",
                tooltip="dials.integrate ...",
                icon="resources/integrate.png",
                icon_disabled="resources/integrate_grayed.png",
            ),
            ActionInformation(
                id="symmetry",
                label="symmetry",
                tooltip="dials.symmetry ...",
                icon="resources/symmetry.png",
                icon_disabled="resources/symmetry_grayed.png",
            ),
            ActionInformation(
                id="scale",
                label="scale",
                tooltip="dials.scale ...",
                icon="resources/scale.png",
                icon_disabled="resources/scale_grayed.png",
            ),
            ActionInformation(
                id="export",
                label="export",
                tooltip="dials.export ...",
                icon="resources/export.png",
                icon_disabled="resources/export_grayed.png",
            ),
        ]
    ]
)


def update_manifest(export_node):
    """Update or create manifest.json, which contains information about exported
    MTZ files for use by calling software such as ccp4i2 and CCP4 Cloud"""

    manifest_path = os.path.join(sys_arg.directory, "dui_files", "manifest.json")

    # Read or set up the manifest dictionary
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path) as f:
                manifest = json.load(f)
        except json.decoder.JSONDecodeError:
            pass
    else:
        manifest = {}

    # Identify the MTZ file and type
    mtz_path = None
    mtz_type = "integrated"
    for parm in export_node.ll_command_lst[0]:
        logger.info(parm)
        if parm.startswith("mtz.hklout=") or parm.startswith("output.mtz="):
            mtz_path = os.path.realpath(parm.split("=")[1])
        elif parm == "intensity=scale":
            mtz_type = "scaled"
    if export_node.ll_command_lst[0][0] == "merge":
        mtz_type = "merged"

    # Get a path for the DIALS report for the previous step (if it already
    # exists this will return the existing path)
    report_out = os.path.realpath(generate_report(export_node.prev_step))

    # Add to the manifest and write it out
    manifest[mtz_path] = {"type": mtz_type, "report": report_out}
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=4)

    return


def try_find_prev_mask_pickle(cur_nod):
    pickle_path = None
    my_node = cur_nod
    while pickle_path is None:
        my_node = my_node.prev_step
        try:
            if my_node.ll_command_lst[0][0] == "find_spots":
                logger.debug("found find_spots")
                for command in my_node.ll_command_lst[0]:
                    if command.startswith("spotfinder.lookup.mask="):
                        logger.debug("Found mask.pickle")
                        logger.debug(my_node.ll_command_lst[0])
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
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("not getting there")
            return None

    return pickle_path


# Public domain code by anatoly techtonik <techtonik@gmail.com>
# from https://gist.github.com/4368898
def find_executable(executable, path=None):
    """Find if 'executable' can be run. Looks for it in 'path'
    (string that lists directories separated by 'os.pathsep';
    defaults to os.environ['PATH']). Checks for all executable
    extensions. Returns full path or None if no command is found.
    """
    if path is None:
        path = os.environ["PATH"]
    paths = path.split(os.pathsep)
    extlist = [""]
    if sys.platform == "win32":
        pathext = os.environ["PATHEXT"].lower().split(os.pathsep)
        (base, ext) = os.path.splitext(executable)
        if ext.lower() not in pathext:
            extlist = pathext

    for ext in extlist:
        execname = executable + ext
        if os.path.isfile(execname):
            return execname

        else:
            for p in paths:
                f = os.path.join(p, execname)
                if os.path.isfile(f):
                    return f

    else:
        return None


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
    """Get the path of the root of the DUI package"""
    return str(os.path.dirname(os.path.abspath(__file__)))


def get_package_path(path):
    """Get the absolute path of something under the DUI package"""
    return os.path.join(get_main_path(), path)


def get_import_run_string(in_str_lst: List[str]) -> Tuple[str, str]:
    """
    Calculate the dials.import filename and image_range parameters.

    Args:
        in_str_lst: List of files to open

    Returns:
        Tuple containing
            dir_path (str):
                The location of the data. Note: This only appears to
                be used for re-opening the data dialog?
            import_string (str):
                The string containing parts to pass to dials.import.
                This could be of the forms:
                    '/some/path/single_file_0002.cbf'
                    '/some/path/images_master.nxs'
                    '/some/path/filename_*.cbf'
                    '/some/path/filename_*.cbf image_range=1,100'
                but in other cases may include several filenames. Spaces
                within filenames will be escaped, so that shlex.split
                can recover the initial list.
    """
    logger.debug("Converting string for import: %s", in_str_lst)

    if len(in_str_lst) == 1:
        template, index = template_regex(in_str_lst[0])
        indices = [index]

    else:
        try:
            template, indices = template_regex_from_list(in_str_lst)

        except (AssertionError, TypeError):
            template = None
            indices = None

    if template is None:
        # Unable to collapse?? Just pass through all filenames as <name>
        # and trust dials to process
        return os.path.dirname(in_str_lst[0]), escaped_join(in_str_lst)

    dirname = os.path.dirname(template)

    # We're currently using wildcards, so continue with this by
    # replacing the template placeholder for now.
    out_str = escaped_join([re.sub("#+", "*", template)])

    # Do we have a restricted image range?
    image_range = None
    if len(indices) > 1:
        min_image_range = min(indices)
        max_image_range = max(indices)
        image_range = (min_image_range, max_image_range)

        # Warn if things were missing - this may be perfectly normal
        if not set(indices) == set(range(min_image_range, max_image_range + 1)):
            logger.warning("Non-continuous image range selected - output may be wrong")
            logger.info(indices)
            logger.info(sorted(set(range(min_image_range, max_image_range + 1))))

    if image_range is not None:
        out_str += " image_range={},{}".format(*image_range)

    logger.debug("Filename template output = %s", out_str)
    logger.debug("Filename template dir =    %s", dirname)

    return dirname, out_str


def build_command_tip(command_lst):
    """Build a tooltip with information about what was actually run"""
    if command_lst == [None]:
        str_tip = "?"

    else:
        str_tip = "dials." + str(command_lst[0][0])
        if len(command_lst[0]) > 1:
            for new_cmd in command_lst[0][1:]:
                str_tip += "\n  " + str(new_cmd)

    return str_tip


def join_path(file_in):
    cwd_path = os.path.join(sys_arg.directory, "dui_files")
    if file_in is not None:
        full_path = os.path.join(cwd_path, file_in)

    else:
        full_path = None

    return full_path


def update_info(main_obj):

    main_obj.cli_tree_output(main_obj.idials_runner)
    main_obj.cur_html = main_obj.idials_runner.get_html_report()

    if main_obj.view_tab_num == 2:
        main_obj.web_view.update_page(join_path(main_obj.cur_html))

    new_log = main_obj.idials_runner.get_log_path()

    tmp_curr = main_obj.idials_runner.current_node

    main_obj.cli_out.clear()
    main_obj.cli_out.make_green()
    main_obj.cur_log = new_log
    main_obj.cli_out.refresh_txt(join_path(main_obj.cur_log), tmp_curr)

    new_img_json = main_obj.idials_runner.get_datablock_path()
    new_ref_pikl = main_obj.idials_runner.get_reflections_path()

    if main_obj.view_tab_num == 0:

        if main_obj.cur_json != new_img_json:
            main_obj.cur_json = new_img_json
            # TODO check if next line should run ALLWAYS
            main_obj.img_view.contrast_initiated = False
            logger.info("before ini_datablock")
            main_obj.img_view.ini_datablock(main_obj.cur_json)
            logger.info("after ini_datablock")

        if main_obj.cur_pick != new_ref_pikl:
            main_obj.cur_pick = new_ref_pikl
            main_obj.img_view.set_reflection_table(
                [join_path(main_obj.cur_pick[0]), join_path(main_obj.cur_pick[1])]
            )

    if tmp_curr.success is None:
        tmp_curr = tmp_curr.prev_step

    main_obj.info_widget.update_data(
        exp_json_path=join_path(tmp_curr.json_file_out),
        refl_pikl_path=[join_path(new_ref_pikl[0]), join_path(new_ref_pikl[1])],
    )

    main_obj.img_view.update_exp(main_obj.info_widget.all_data.ref2exp)

    main_obj.ext_view.update_data(
        new_pick=[join_path(new_ref_pikl[0]), join_path(new_ref_pikl[1])],
        new_json=join_path(tmp_curr.json_file_out),
    )

    main_obj.img_view.update_painter_info(main_obj.info_widget.all_data)


def update_pbar_msg(main_obj):
    tmp_curr = main_obj.idials_runner.current_node
    txt = str(tmp_curr.ll_command_lst[0][0])

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

        try:
            if nxt_cmd is None:
                txt = "Done"

            else:
                lab_nxt_cmd = ACTIONS[nxt_cmd].label
                txt = "click <<" + lab_nxt_cmd + ">> to go ahead, or click << Retry >>"

        except KeyError:
            txt = "Done"

    # main_obj.txt_bar.setText(txt)
    main_obj.txt_bar.setText(" \n ")
    # logger.info(txt)


class MyActionButton(QToolButton):
    def __init__(self, action, parent=None):
        super().__init__(parent=parent)

        self.action = action

        # Load the icon for this action
        tmp_ico = QIcon()
        # TODO(nick): Switch to proper package resource loading?
        main_path = get_main_path()
        tmp_ico.addFile(os.path.join(main_path, action.icon), mode=QIcon.Normal)
        tmp_ico.addFile(
            os.path.join(main_path, action.icon_disabled), mode=QIcon.Disabled
        )

        self.setIcon(tmp_ico)
        self.setIconSize(QSize(31, 30))

        self.setToolTip(action.tooltip)
        self.setText(action.label)

        sys_font = QFont()
        small_font_size = sys_font.pointSize() - 2

        self.setFont(QFont("Helvetica", small_font_size, QFont.Light))
        # self.setFont(QFont("Monospace", small_font_size, QFont.Bold))

        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


class TreeNavWidget(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        logger.debug("TreeNavWidget(__init__)")
        self.setSortingEnabled(False)
        self.setAnimated(True)
        self.setIndentation(18)

        header_view = self.header()
        header_view.setSectionResizeMode(QHeaderView.ResizeToContents)
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
                if child_node.ll_command_lst[0] != [None]:
                    # child_node_name = str(child_node.ll_command_lst)
                    child_node_name = str(child_node.ll_command_lst[0][0])

                elif child_node.success is None:
                    child_node_name = "* None *"

                else:
                    child_node_name = " ? None ? "

                try:
                    child_node_tip = build_command_tip(child_node.ll_command_lst)

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.debug(
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
        super().__init__()
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
        super().__init__(parent)

        vbox = QVBoxLayout()
        label = QLabel(
            "Running a pop-up viewer ...\n\n"
            "remember to close the viewer before\n"
            "performing any other task"
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

    def run_my_proc(self, command, json_path, pickle_path):
        """Run a process.

        Args:
            command (str):      The command to run
            json_path (str):
                Path to the JSON file to pass in as first argument
            pickle_path (Sequence[Optional[str]]):
                An additional path to a pickle to pass in as an argument.
                Currently, all except the first argument is ignored.
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
        cmd_to_run = [find_executable(command), str(json_path)]
        logger.debug("Resolving %s as %s", command, cmd_to_run[0])

        first_pikl_path = pickle_path[0]
        if first_pikl_path is not None:
            cmd_to_run.append(str(first_pikl_path))

        # Save the working directory
        self.cwd_path = os.path.join(sys_arg.directory, "dui_files")

        logger.debug("\n running Popen>>>\n   %s\n<<<", " ".join(cmd_to_run))
        self.my_process = subprocess.Popen(args=cmd_to_run, cwd=self.cwd_path)
        logger.debug("Running PID %s", self.my_process.pid)

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
        self.done(0)

    def child_closed(self):
        """The child process has closed by itself"""
        logger.debug("after ...close()")
        self.my_process = None
        # Just close ourself
        self.done(0)

    def closeEvent(self, event):
        """User has clicked 'close' window decorator on dialog box"""
        logger.debug("from << closeEvent  (QDialog) >>")
        self.kill_my_proc()


class OuterCaller(QWidget):
    def __init__(self):
        super().__init__()

        v_box = QVBoxLayout()

        recip_lat_but = QPushButton("\n Open reciprocal lattice viewer \n")
        recip_lat_but.clicked.connect(self.run_recip_dialg)
        v_box.addWidget(recip_lat_but)

        img_but = QPushButton("\n Open image viewer \n")
        img_but.clicked.connect(self.run_img_dialg)
        v_box.addWidget(img_but)

        self.diag = ExternalProcDialog(parent=self.window())
        self.setLayout(v_box)
        # self.show()

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
            "dials.image_viewer", json_path=self.my_json, pickle_path=self.my_pick
        )


class CliOutView(QTextEdit):
    def __init__(self, app=None):
        super().__init__()
        self.setFont(QFontDatabase.systemFont(QFontDatabase.FixedFont))

        self.make_green()

    def add_txt(self, str_to_print):
        try:
            ed_str = str(str_to_print).rstrip()
            self.append(ed_str)
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
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

        if path_to_log and Path(path_to_log).is_file():
            fil_obj = open(path_to_log)
            lst_lin = fil_obj.readlines()
        else:
            logger.debug("No log file")
            lst_lin = ["Ready to Run:"]
            self.make_green()

        self.clear()
        logger.debug("success = %s %s", success, "refresh_txt")

        for lin in lst_lin:
            self.add_txt(lin)


class Text_w_Bar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
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
            logger.debug("Caught unknown exception type %s: %s", type(e).__name__, e)
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


def loading_error_dialog(message):
    """Create an error message about loading in a dialog box."""
    # If pre-building:
    # from dui.resources.error_loading_dialog import Ui_LoadErrorDialog

    # dialog_filename = get_package_path("resources/error_loading_dialog.ui")
    # Ui_LoadErrorDialog, _ = loadUiType(dialog_filename)
    # Use compiled class while pyside2-uic is broken in CCP4
    from .error_loading_dialog import Ui_LoadErrorDialog

    dialog = QDialog()
    errwidget = Ui_LoadErrorDialog()
    errwidget.setupUi(dialog)
    errwidget.errorMessage.setPlainText(message)
    return dialog
