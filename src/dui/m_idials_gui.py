"""
DUI's most central gidgets

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
import pickle
import shutil

from .dynamic_reindex_gui import MyReindexOpts
from .cli_utils import TreeShow, prn_lst_lst_cmd, sys_arg
from .custom_widgets import ParamWidget
from .gui_utils import (
    CliOutView,
    Text_w_Bar,
    OuterCaller,
    # build_command_tip,
    update_info,
    update_pbar_msg,
    kill_w_child,
    TreeNavWidget,
    build_ttip,
    # build_label,
    MyQButton,
    get_main_path,
    try_find_prev_mask_pickle,
)
from .m_idials import Runner
from .outputs_n_viewers.web_page_view import WebTab
from .outputs_n_viewers.img_viewer import MyImgWin
from .outputs_gui import InfoWidget
from .qt import (
    QHBoxLayout,
    QIcon,
    QMainWindow,
    QModelIndex,
    QPushButton,
    QScrollArea,
    QSize,
    QSizePolicy,
    QSplitter,
    QStackedWidget,
    Qt,
    QTabWidget,
    QThread,
    QVBoxLayout,
    QWidget,
    Signal,
)

logger = logging.getLogger(__name__)

widg_name_list = [
    "import",
    "find_spots",
    "index",
    "refine_bravais_settings",
    "refine",
    "integrate",
    "symmetry",
    "scale",
    "export",
]


class CommandThread(QThread):

    str_print_signal = Signal(str)
    str_fail_signal = Signal()

    def __init__(self, parent=None):
        super(CommandThread, self).__init__()

    def __call__(self, cmd_to_run, ref_to_controler):
        self.cmd_to_run = cmd_to_run
        self.ref_to_controler = ref_to_controler
        self.start()

    def run(self):
        self.ref_to_controler.run(command=self.cmd_to_run, ref_to_class=self)

    def emit_print_signal(self, str_lin):
        self.str_print_signal.emit(str_lin)

    def emit_fail_signal(self):
        self.str_fail_signal.emit()


class ControlWidget(QWidget):

    user_changed = Signal(str)
    update_command_lst_high_level = Signal(list)

    def __init__(self, parent=None):
        super(ControlWidget, self).__init__()

        main_path = get_main_path()
        logger.debug("main_path = %s", main_path)

        lst_icons_path = []
        lst_icons_path.append(main_path + "/resources/import.png")
        lst_icons_path.append(main_path + "/resources/find_spots.png")
        lst_icons_path.append(main_path + "/resources/index.png")
        lst_icons_path.append(main_path + "/resources/reindex.png")
        lst_icons_path.append(main_path + "/resources/refine.png")
        lst_icons_path.append(main_path + "/resources/integrate.png")
        lst_icons_path.append(main_path + "/resources/symmetry.png")
        lst_icons_path.append(main_path + "/resources/scale.png")
        lst_icons_path.append(main_path + "/resources/export.png")

        lst_grayed_icons_path = []
        lst_grayed_icons_path.append(main_path + "/resources/import_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/find_spots_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/index_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/reindex_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/refine_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/integrate_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/symmetry_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/scale_grayed.png")
        lst_grayed_icons_path.append(main_path + "/resources/export_grayed.png")

        top_box = QVBoxLayout()
        top_box.setMargin(0)
        top_box.setContentsMargins(0, 0, 0, 0)

        self.step_param_widg = QStackedWidget()
        self.step_param_widg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.widg_lst = []
        self.btn_lst = []

        logger.debug("\n\n\n\n")

        lst_heights = []
        lst_widths = []

        for num, step_name in enumerate(widg_name_list):

            tmp_ico = QIcon()
            tmp_ico.addFile(lst_icons_path[num], mode=QIcon.Normal)
            tmp_ico.addFile(lst_grayed_icons_path[num], mode=QIcon.Disabled)

            ttip = build_ttip(step_name)

            new_btn = MyQButton(self)
            new_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            new_btn.intro_content(step_name, tmp_ico, ttip)

            if num > 0:
                new_btn.clicked.connect(self.btn_clicked)
                top_box.addWidget(new_btn)

            elif num == 0:
                new_btn.hide()

            param_widg = ParamWidget(step_name)
            new_btn.pr_widg = param_widg
            self.step_param_widg.addWidget(param_widg)
            self.widg_lst.append(param_widg)
            param_widg.update_command_lst_medium_level.connect(self.update_parent_lst)
            self.btn_lst.append(new_btn)

            param_widg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            lst_heights.append(param_widg.height())
            lst_widths.append(param_widg.width())

        logger.debug("lst_heights = %s", lst_heights)
        logger.debug("max(lst_heights) = %s", max(lst_heights))

        logger.debug("lst_widths = %s", lst_widths)
        logger.debug("max(lst_widths) = %s", max(lst_widths))

        self.setLayout(top_box)

        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.show()

        logger.debug("self.height = %s", self.height())
        logger.debug("self.width = %s", self.width())
        logger.debug("\n\n\n\n")

    def update_parent_lst(self, command_lst):
        self.update_command_lst_high_level.emit(command_lst)

    def get_arg_obj(self, sys_arg_in):
        self.widg_lst[0].my_widget.get_arg_obj(sys_arg_in)

    def set_widget(self, nxt_cmd=None, curr_step=None):

        found_label = False

        for widget in self.widg_lst:
            if widget.my_label == nxt_cmd:
                self.step_param_widg.setCurrentWidget(widget)
                found_label = True
                try:
                    widget.update_param(curr_step)
                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    logger.debug("\n Unable to update params\n")

        if not found_label and nxt_cmd == "reindex":
            logger.debug("assuming reindex mode")
            widget_now = self.widg_lst[3]
            self.step_param_widg.setCurrentWidget(widget_now)

    def btn_clicked(self):
        logger.debug("btn_clicked")
        my_sender = self.sender()
        self.step_param_widg.setCurrentWidget(my_sender.pr_widg)
        self.user_changed.emit(my_sender.pr_widg.my_label)

        logger.debug("my_sender.pr_widg.my_label = %s", my_sender.pr_widg.my_label)
        command_lst = [str(my_sender.pr_widg.my_label)]
        self.update_command_lst_high_level.emit(command_lst)

    def gray_outs_all(self):
        for btn in self.btn_lst:
            btn.setEnabled(False)

    def gray_outs_from_lst(self, lst_nxt):
        self.gray_outs_all()

        for btn in self.btn_lst:
            for cmd_str in lst_nxt:
                if btn.cmd_n1 == cmd_str:
                    btn.setEnabled(True)


class StopRunRetry(QWidget):
    def __init__(self, parent=None):
        super(StopRunRetry, self).__init__()

        main_path = get_main_path()

        ctrl_box = QHBoxLayout()

        self.repeat_btn = QPushButton("\n Retry \n", self)

        re_try_icon_path = str(main_path + "/resources/re_try.png")
        re_try_grayed_path = str(main_path + "/resources/re_try_grayed.png")
        tmp_ico = QIcon()
        tmp_ico.addFile(re_try_icon_path, mode=QIcon.Normal)
        tmp_ico.addFile(re_try_grayed_path, mode=QIcon.Disabled)

        self.repeat_btn.setIcon(tmp_ico)
        self.repeat_btn.setIconSize(QSize(50, 38))
        ctrl_box.addWidget(self.repeat_btn)

        self.run_btn = QPushButton("\n  Run  \n", self)
        self.dials_logo_path = str(
            main_path + "/resources/DIALS_Logo_smaller_centred.png"
        )
        dials_grayed_path = str(
            main_path + "/resources/DIALS_Logo_smaller_centred_grayed.png"
        )
        tmp_ico = QIcon()
        tmp_ico.addFile(self.dials_logo_path, mode=QIcon.Normal)
        tmp_ico.addFile(dials_grayed_path, mode=QIcon.Disabled)

        self.run_btn.setIcon(tmp_ico)
        self.run_btn.setIconSize(QSize(50, 38))
        ctrl_box.addWidget(self.run_btn)

        self.stop_btn = QPushButton("\n  Stop  \n", self)
        stop_logo_path = str(main_path + "/resources/stop.png")
        stop_grayed_path = str(main_path + "/resources/stop_grayed.png")
        tmp_ico = QIcon()
        tmp_ico.addFile(stop_logo_path, mode=QIcon.Normal)
        tmp_ico.addFile(stop_grayed_path, mode=QIcon.Disabled)
        self.stop_btn.setIcon(tmp_ico)
        self.stop_btn.setIconSize(QSize(50, 38))
        ctrl_box.addWidget(self.stop_btn)

        self.setLayout(ctrl_box)
        self.show()


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.storage_path = sys_arg.directory
        try:
            with open(self.storage_path + "/dui_files/bkp.pickle", "rb") as bkp_in:
                self.idials_runner = pickle.load(bkp_in)

            # TODO sometimes the following error appears
            # Attribute not found
            #   'module' object has no attribute 'CommandNode'

            refresh_gui = True

        except Exception as e:
            logger.debug("str(e) = %s", str(e))
            logger.debug("e.__doc__ = %s", e.__doc__)
            logger.debug("e.message = %s", e.message)
            self.idials_runner = Runner()

            try:
                shutil.rmtree(self.storage_path + "/dui_files")
            except OSError:
                logger.debug('failed to do "shutil.rmtree("/dui_files")"')

            os.mkdir(self.storage_path + "/dui_files")
            refresh_gui = False

        self.cli_tree_output = TreeShow()
        self.cli_tree_output(self.idials_runner)

        self.cur_html = None
        self.cur_pick = None
        self.cur_json = None
        self.cur_log = None
        self.cur_cmd_name = "None"

        main_box = QVBoxLayout()

        self.centre_par_widget = ControlWidget()
        self.centre_par_widget.get_arg_obj(sys_arg)
        self.stop_run_retry = StopRunRetry()
        self.tree_out = TreeNavWidget()

        left_control_box = QHBoxLayout()

        left_top_control_box = QVBoxLayout()
        left_top_control_box.addWidget(self.centre_par_widget)
        left_top_control_box.addStretch()
        left_control_box.addLayout(left_top_control_box)

        centre_control_box = QVBoxLayout()

        v_control_splitter = QSplitter()
        v_control_splitter.setOrientation(Qt.Vertical)
        v_control_splitter.addWidget(self.tree_out)
        v_control_splitter.addWidget(self.centre_par_widget.step_param_widg)

        centre_control_box.addWidget(v_control_splitter)
        centre_control_box.addWidget(self.stop_run_retry)
        left_control_box.addLayout(centre_control_box)

        dummy_left_widget = QWidget()
        dummy_h_layout = QHBoxLayout()
        dummy_h_layout.addLayout(left_control_box)
        dummy_left_widget.setLayout(dummy_h_layout)
        dummy_left_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)
        h_main_splitter.addWidget(dummy_left_widget)

        self.cli_out = CliOutView()
        self.web_view = WebTab()
        self.img_view = MyImgWin()
        self.ext_view = OuterCaller()

        self.output_info_tabs = QTabWidget()
        self.output_info_tabs.addTab(self.img_view, "Image View")
        self.output_info_tabs.addTab(self.cli_out, "Log Text")
        self.output_info_tabs.addTab(self.web_view, "Report View")
        self.output_info_tabs.addTab(self.ext_view, "External Tools")
        self.view_tab_num = 0
        self.output_info_tabs.currentChanged.connect(self.tab_changed)

        self.info_widget = InfoWidget()

        InfoScrollArea = QScrollArea()
        InfoScrollArea.setWidget(self.info_widget)

        v_info_splitter = QSplitter()
        v_info_splitter.setOrientation(Qt.Vertical)
        v_info_splitter.addWidget(self.output_info_tabs)
        v_info_splitter.addWidget(InfoScrollArea)

        h_main_splitter.addWidget(v_info_splitter)

        main_box.addWidget(h_main_splitter)

        self.txt_bar = Text_w_Bar()
        main_box.addWidget(self.txt_bar)

        self.connect_all()

        self.custom_thread = CommandThread()
        self.custom_thread.finished.connect(self.update_after_finished)
        self.custom_thread.str_fail_signal.connect(self.after_failed)
        self.custom_thread.str_print_signal.connect(self.cli_out.add_txt)
        self.custom_thread.str_print_signal.connect(self.txt_bar.setText)

        self.ext_view.pass_parmam_lst.connect(self.pass_parmams)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

        self.setWindowTitle("CCP4 DUI")
        self.setWindowIcon(QIcon(self.stop_run_retry.dials_logo_path))

        self.just_reindexed = False
        self.user_stoped = False
        self.reconnect_when_ready()

        self.my_pop = None

        if refresh_gui:
            self.refresh_my_gui()

    def connect_all(self):
        self.setCursor(Qt.ArrowCursor)
        self.tree_clickable = True
        self.tree_out.clicked[QModelIndex].connect(self.node_clicked)

        self.stop_run_retry.repeat_btn.clicked.connect(self.rep_clicked)
        self.stop_run_retry.run_btn.clicked.connect(self.run_clicked)
        self.stop_run_retry.stop_btn.clicked.connect(self.stop_clicked)

        self.centre_par_widget.user_changed.connect(self.cmd_changed_by_user)
        self.centre_par_widget.update_command_lst_high_level.connect(
            self.update_low_level_command_lst
        )
        self.centre_par_widget.step_param_widg.currentChanged.connect(
            self.cmd_changed_by_any
        )
        self.check_gray_outs()

    def disconnect_while_running(self):

        self.setCursor(Qt.BusyCursor)
        self.tree_clickable = False

        self.stop_run_retry.repeat_btn.setEnabled(False)
        self.stop_run_retry.run_btn.setEnabled(False)
        self.stop_run_retry.stop_btn.setEnabled(True)
        self.centre_par_widget.gray_outs_all()
        self.centre_par_widget.step_param_widg.currentWidget().my_widget.gray_me_out()

        self.user_stoped = False

    def reconnect_when_ready(self):

        self.setCursor(Qt.ArrowCursor)
        self.tree_clickable = True

        self.stop_run_retry.repeat_btn.setEnabled(False)
        self.stop_run_retry.stop_btn.setEnabled(False)
        self.stop_run_retry.run_btn.setEnabled(False)

        if self.user_stoped:
            self.idials_runner.current_node.success = None

        my_widget = self.centre_par_widget.step_param_widg.currentWidget().my_widget
        if self.idials_runner.current_node.success is None:
            self.stop_run_retry.run_btn.setEnabled(True)
            my_widget.activate_me()
        else:
            if self.idials_runner.current_node.command_lst[0] != "export":
                self.stop_run_retry.repeat_btn.setEnabled(True)
            my_widget.gray_me_out()

        if self.idials_runner.current_node.command_lst[0] == "reindex":
            self.stop_run_retry.run_btn.setEnabled(False)
            self.stop_run_retry.repeat_btn.setEnabled(False)

        self.check_gray_outs()
        self.user_stoped = False
        self.update_nav_tree()

    def tab_changed(self, num):
        self.view_tab_num = num
        update_info(self)

    def pass_parmams(self, cmd_lst):
        """(We've been passed a parameter by the external tool signal)"""

        logger.debug(
            "\n_________________________________________cmd_lst(pass_parmams) = %s %s",
            cmd_lst,
            "\n",
        )

        current_parameter_widget = (
            self.centre_par_widget.step_param_widg.currentWidget()
        )
        action_name = current_parameter_widget.my_widget.command_lst[0]
        if (
            action_name in ["find_spots", "integrate"]
            and self.idials_runner.current_node.success is None
        ):
            # As a quick hack to get things working, look for 'lookup.mask'
            # and if preset add a prefix phil-scope to it
            lookup_scope_name = {
                "find_spots": "spotfinder",
                "integrate": "integration",
            }[action_name]
            full_command = [action_name] + [
                lookup_scope_name + "." + x if x.startswith("lookup.mask=") else x
                for x in cmd_lst
            ]
            logger.debug("\n full_cmd_lst = %s", full_command)
            current_parameter_widget.my_widget.update_param_w_lst(full_command)
        else:
            logger.debug("No need to feed back params")
            logger.debug(
                "my_widget_now.my_widget.command_lst = %s",
                current_parameter_widget.my_widget.command_lst,
            )

    def update_low_level_command_lst(self, command_lst):
        logger.debug(
            "self.idials_runner.current_node.command_lst = %s",
            self.idials_runner.current_node.command_lst,
        )
        logger.debug("                                command_lst = %s", command_lst)

        self.idials_runner.current_node.command_lst = command_lst
        self.reconnect_when_ready()

    def cmd_changed_by_user(self, my_label):
        logger.debug("cmd_changed_by_user()")
        tmp_curr = self.idials_runner.current_node
        if tmp_curr.success is True:

            self.cmd_exe(["mkchi"])
            self.idials_runner.current_node.command_lst = [str(my_label)]
            logger.debug(
                "_________________________________________________________>>>> mkchi\n"
            )
            self.centre_par_widget.step_param_widg.currentWidget().my_widget.reset_par()

            path_to_mask_pickle = None
            if self.idials_runner.current_node.command_lst[0] == "integrate":
                logger.debug("Running: try_find_prev_mask_pickle")
                path_to_mask_pickle = try_find_prev_mask_pickle(
                    self.idials_runner.current_node
                )
                if path_to_mask_pickle is not None:
                    self.pass_parmams(["lookup.mask=" + path_to_mask_pickle])

            else:
                logger.debug(
                    "self.idials_runner.current_node.command_lst[0] = %s",
                    self.idials_runner.current_node.command_lst[0],
                )

            logger.debug("path_to_mask_pickle = %s", path_to_mask_pickle)
            logger.debug(
                "\n______________________________________________________mkchi <<<<<"
            )

            self.cmd_exe(["clean"])

        elif tmp_curr.success is None:
            self.idials_runner.current_node.command_lst = [str(my_label)]
            self.reconnect_when_ready()

    def cmd_changed_by_any(self):
        tmp_curr_widg = self.centre_par_widget.step_param_widg.currentWidget()
        self.cur_cmd_name = tmp_curr_widg.my_widget.command_lst[0]
        self.reconnect_when_ready()

    def rep_clicked(self):
        logger.debug("rep_clicked")
        self.cmd_exe(["mksib"])
        self.cmd_exe(["clean"])
        self.check_gray_outs()

    def stop_clicked(self):
        logger.debug("\n\n <<< Stop clicked >>> \n\n")
        # TODO fix spelling on << dials_command >>
        pr_to_kill = self.idials_runner.current_node.dials_command.my_pid
        logger.debug(
            "self.idials_runner.current_node.dials_command.my_pid = %s", pr_to_kill
        )
        self.user_stoped = True
        kill_w_child(pr_to_kill)

    def run_clicked(self):
        logger.debug("run_clicked")
        logger.debug(
            "...currentWidget(ref) = %s",
            self.centre_par_widget.step_param_widg.currentWidget(),
        )
        cmd_tmp = (
            self.centre_par_widget.step_param_widg.currentWidget().my_widget.command_lst
        )
        logger.debug("cmd_tmp = %s", cmd_tmp)
        self.cmd_launch(cmd_tmp)

    def cmd_exe(self, new_cmd):
        # Running NOT in parallel
        update_info(self)
        self.idials_runner.run(command=new_cmd, ref_to_class=None)
        self.check_reindex_pop()
        self.reconnect_when_ready()

    def cmd_launch(self, new_cmd):
        # Running WITH theading
        self.cli_out.clear()
        self.cli_out.make_green()
        self.txt_bar.start_motion()
        self.txt_bar.setText("Running")
        self.disconnect_while_running()

        self.custom_thread(new_cmd, self.idials_runner)

    def update_after_finished(self):
        update_info(self)

        self.txt_bar.end_motion()
        self.just_reindexed = False

        tmp_curr = self.idials_runner.current_node

        if (
            tmp_curr.command_lst[0] == "refine_bravais_settings"
            and tmp_curr.success is True
        ):

            self.idials_runner.run(command=["mkchi"], ref_to_class=None)

            self.idials_runner.current_node.command_lst[0] = "reindex"

        elif tmp_curr.command_lst[0] == "reindex" and tmp_curr.success is True:

            self.just_reindexed = True
            try:
                self.my_pop.close()
            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.error(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("no need to close reindex table")

        self.check_reindex_pop()
        self.check_gray_outs()
        self.reconnect_when_ready()

        with open(self.storage_path + "/dui_files/bkp.pickle", "wb") as bkp_out:
            pickle.dump(self.idials_runner, bkp_out)

    def check_gray_outs(self):
        tmp_curr = self.idials_runner.current_node
        if tmp_curr.success is not True:
            tmp_curr = tmp_curr.prev_step

        cmd_connects = {
            "Root": ["import"],
            "import": ["find_spots"],
            "find_spots": ["index"],
            "index": ["refine_bravais_settings", "refine", "integrate"],
            "refine_bravais_settings": [None],
            "reindex": ["refine", "integrate"],
            "refine": ["refine", "integrate"],
            "integrate": ["symmetry", "scale", "export"],
            "symmetry": ["scale", "export"],
            "scale": ["symmetry", "export"],
            "export": [None],
            "None": [None],
        }

        lst_nxt = cmd_connects[str(tmp_curr.command_lst[0])]
        self.centre_par_widget.gray_outs_from_lst(lst_nxt)

    def check_reindex_pop(self):
        tmp_curr = self.idials_runner.current_node
        if tmp_curr.command_lst[0] == "reindex" and not self.just_reindexed:

            try:
                self.my_pop = MyReindexOpts()
                self.my_pop.set_ref(
                    in_json_path=tmp_curr.prev_step.json_file_out,
                    lin_num=tmp_curr.prev_step.lin_num,
                )
                self.my_pop.my_inner_table.opt_signal.connect(self.opt_dobl_clicked)

            except Exception as my_err:
                logger.debug("str(my_err) = %s", str(my_err))
                logger.debug("my_err.__doc__ = %s", my_err.__doc__)
                logger.debug("my_err.message = %s", my_err.message)
                if str(my_err)[0:36] == "[Errno 2] No such file or directory:":
                    logger.debug("\n interrupted refine_bravais_settings \n")

            # TODO find an elegant way to interrupt and remove nodes

        else:
            try:
                self.my_pop.close()
            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.error(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("no need to close reindex table")

        self.just_reindexed = False

    def update_nav_tree(self):
        self.tree_out.update_me(
            self.idials_runner.step_list[0], self.idials_runner.current_line
        )

        update_pbar_msg(self)

    def after_failed(self):
        logger.debug("\n FAILED STEP:")
        self.update_nav_tree()
        self.txt_bar.end_motion()

        curr_step = self.idials_runner.current_node

        for err_lin in curr_step.dials_command.tmp_std_all:
            logger.debug(err_lin)

        logger.debug("curr_step.lin_num = %s", curr_step.lin_num)
        err_log_file_out = (
            self.storage_path
            + "/dui_files"
            + os.sep
            + str(curr_step.lin_num)
            + "_err_out.log"
        )
        logger.debug("err_log_file_out = %s %s", err_log_file_out, "\n")

        fil_obj = open(err_log_file_out, "w")
        for err_lin in curr_step.dials_command.tmp_std_all:
            fil_obj.write(err_lin)
            fil_obj.write("\n")

        fil_obj.close()
        self.idials_runner.current_node.err_file_out = err_log_file_out

    def opt_dobl_clicked(self, row):
        re_idx = row + 1
        logger.debug("Solution clicked = %s", re_idx)
        cmd_tmp = "reindex solution=" + str(re_idx)
        self.cmd_launch(cmd_tmp)

    def node_clicked(self, it_index):

        logger.debug("\n it_index = %s", it_index)
        logger.debug(" type(it_index) = %s", type(it_index))

        if self.tree_clickable:
            # TODO Think of a more robust way to "disconnect" ... next line
            try:
                self.centre_par_widget.update_command_lst_high_level.disconnect(
                    self.update_low_level_command_lst
                )
            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.error(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("<< update_low_level_command_lst >> already disconnected")

            logger.debug("TreeNavWidget(node_clicked)")
            item = self.tree_out.std_mod.itemFromIndex(it_index)
            prn_lst_lst_cmd(item.idials_node)
            lin_num = item.idials_node.lin_num
            logger.debug("clicked item lin_num (self.tree_out.std_mod) = %s", lin_num)
            cmd_ovr = "goto " + str(lin_num)
            self.cmd_exe(cmd_ovr)
            self.centre_par_widget.set_widget(
                nxt_cmd=item.idials_node.command_lst[0],
                curr_step=self.idials_runner.current_node,
            )

            self.check_reindex_pop()
            update_info(self)
            self.check_gray_outs()
            self.reconnect_when_ready()

            self.centre_par_widget.update_command_lst_high_level.connect(
                self.update_low_level_command_lst
            )

    def refresh_my_gui(self):

        prn_lst_lst_cmd(self.idials_runner.current_node)
        lin_num = self.idials_runner.current_node.lin_num
        logger.debug("doing goto:  %s", lin_num)
        cmd_ovr = "goto " + str(lin_num)
        self.cmd_exe(cmd_ovr)
        self.centre_par_widget.set_widget(
            nxt_cmd=self.idials_runner.current_node.command_lst[0],
            curr_step=self.idials_runner.current_node,
        )

        self.check_reindex_pop()
        update_info(self)
        self.check_gray_outs()
        self.reconnect_when_ready()

        logger.debug(
            "\n\n_________________________________________ ... refreshing GUI \n\n"
        )

    def closeEvent(self, event):
        if self.my_pop:
            self.my_pop.close()
