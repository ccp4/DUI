"""
DUI's most central gidgets

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


import logging
import pickle
import re
import time
import traceback
from pathlib import Path
from typing import List

from ._version import __version__
from .cli_utils import TreeShow, build_mask_command_lst, prn_lst_lst_cmd, sys_arg
from .custom_widgets import BeamCentrPage, MaskPage, ParamWidget
from .dynamic_reindex_gui import MyReindexOpts
from .gui_utils import (
    ACTIONS,
    CliOutView,
    MyActionButton,
    OuterCaller,
    Text_w_Bar,
    TreeNavWidget,
    get_main_path,
    kill_w_child,
    try_find_prev_mask_pickle,
    update_manifest,
    update_info,
    update_pbar_msg,
)
from .m_idials import Runner
from .outputs_gui import InfoWidget
from .outputs_n_viewers.img_view_tools import ProgBarBox
from .outputs_n_viewers.img_viewer import MyImgWin
from .outputs_n_viewers.web_page_view import WebTab
from .qt import (
    QDialog,
    QHBoxLayout,
    QIcon,
    QMainWindow,
    QModelIndex,
    QPushButton,
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


class CheckStatusThread(QThread):
    start_busy_box = Signal()
    end_busy_box = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def __call__(self, ref_to_controler):
        self.ref_to_controler = ref_to_controler
        self.start()

    def run(self):
        prev_stat = None
        while True:
            gen_info_stat = self.ref_to_controler.current_node.info_generating
            time.sleep(0.25)

            if prev_stat is None and gen_info_stat is True:
                self.start_busy_box.emit()

            if gen_info_stat is False:
                self.end_busy_box.emit()
                break

            prev_stat = gen_info_stat

        time.sleep(0.1)


class CommandThread(QThread):

    str_print_signal = Signal(str)
    str_fail_signal = Signal()
    busy_box_on = Signal(str)
    busy_box_off = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def __call__(self, cmd_to_run: List[str], ref_to_controler: Runner):
        self.cmd_to_run = cmd_to_run
        self.ref_to_controler = ref_to_controler
        self.status_thread = CheckStatusThread()

        self.status_thread(self.ref_to_controler)
        self.status_thread.start_busy_box.connect(self.pop_busy_box)
        self.status_thread.end_busy_box.connect(self.close_busy_box)

        self.start()

    def run(self):
        self.ref_to_controler.run(command=self.cmd_to_run, ref_to_class=self)
        self.status_thread.wait()

    def emit_print_signal(self, str_lin):
        self.str_print_signal.emit(str_lin)

    def emit_fail_signal(self):
        self.str_fail_signal.emit()

    def pop_busy_box(self):
        logger.debug("emiting pop busy box signal")
        self.busy_box_on.emit("Getting Predictions or Report")

    def close_busy_box(self):
        logger.debug("emiting close busy box signal")
        self.busy_box_off.emit()


class ControlWidget(QWidget):
    """Primarily, the action button widget.

    Also holds as a property (but not in the QT hierarchy) the stage-parameter
    widgets.

    Attributes:
        step_param_widg (QStackedWidget):
            Physical collection widget that holds every possible parameter page.
        param_widgets (Dict[str, ParamWidget]):
            Mapping of action ID to physical widget to handle the parameter page.
        btn_lst (List[MyActionButton]):
            The actual action button instances. Each has a .pr_widg written
            by this class that points to the associated ParamWidget instance,
            and a .action property to point to the action it represents.
        user_changed (Signal[str]):
            A signal emitted when the user has requested a command change
    """

    user_changed = Signal(str)
    update_command_lst_high_level = Signal(list)
    finished_masking = Signal()
    finished_b_centr = Signal()
    click_mask = Signal()
    click_b_centr = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        top_box = QVBoxLayout()
        # top_box.setMargin(0)
        top_box.setContentsMargins(0, 0, 0, 0)

        self.step_param_widg = QStackedWidget()
        self.step_param_widg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.param_widgets = {}
        self.btn_lst = []

        # We only show action buttons for a subset of possible actions
        button_actions = [
            "import",  # Leave in for now - currently pages must be precreated
            "find_spots",
            "index",
            "refine_bravais_settings",
            "refine",
            "integrate",
            "symmetry",
            "scale",
            "export",
        ]

        for x in button_actions:
            action = ACTIONS[x]

            new_btn = MyActionButton(action, parent=self)
            new_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Don't add import to our button list for now - but other code
            # currently assumes the order of this list so we can't not add and
            # create the parameter pages here
            if action.id == "import":
                new_btn.hide()

            else:
                new_btn.clicked.connect(self._action_button_clicked)
                top_box.addWidget(new_btn)

            param_widg = ParamWidget(action.id)
            new_btn.pr_widg = param_widg
            self.step_param_widg.addWidget(param_widg)
            self.param_widgets[action.id] = param_widg
            param_widg.update_command_lst_medium_level.connect(self.update_parent_lst)
            self.btn_lst.append(new_btn)

            param_widg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.mask_page = MaskPage()
        self.mask_page.update_command_lst_medium_level.connect(
            self.singular_step_new_command
        )

        self.mask_page.mask_done.connect(self.done_masking)
        self.mask_page.mask_set.connect(self.set_mask)
        self.step_param_widg.addWidget(self.mask_page)

        self.b_centr_page = BeamCentrPage()
        self.b_centr_page.update_command_lst_medium_level.connect(
            self.singular_step_new_command
        )
        self.b_centr_page.b_centr_done.connect(self.done_b_centr)
        self.b_centr_page.b_centr_set.connect(self.set_b_centr)

        self.step_param_widg.addWidget(self.b_centr_page)

        self.setLayout(top_box)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def singular_step_new_command(self, command_lst):
        self.user_changed.emit(command_lst[0])
        self.update_command_lst_high_level.emit([command_lst])

    def done_masking(self):
        self.finished_masking.emit()

    def set_mask(self):
        self.click_mask.emit()

    def done_b_centr(self):
        self.finished_b_centr.emit()

    def set_b_centr(self):
        self.click_b_centr.emit()

    def update_parent_lst(self, command_lst):
        self.update_command_lst_high_level.emit([command_lst])

    def pass_sys_arg_object_to_import(self, sys_arg_in):
        """Explicitly pass the system argument object to the import page"""
        self.param_widgets["import"].my_widget.set_arg_obj(sys_arg_in)

    def set_widget(self, nxt_cmd=None, curr_step=None):
        """Switch to a different action parameter page.

        Arguments:
            nxt_cmd (str):  Action ID for the page to switch to
            curr_step:      Metadata about the current page state
        """
        # Firstly try looking in the params widget lookup table
        if nxt_cmd in self.param_widgets:
            widget = self.param_widgets[nxt_cmd]
            self.step_param_widg.setCurrentWidget(widget)
            try:
                widget.update_param(curr_step)

            except AttributeError:
                logger.info("\n object has no attribute update_param \n")

        elif nxt_cmd == "reindex":
            # Reindex is a special step because it doesn't have it's own page
            logger.debug("Reindex mode")
            param_widget = self.param_widgets["refine_bravais_settings"]
            self.step_param_widg.setCurrentWidget(param_widget)

        elif nxt_cmd == "generate_mask":
            # Mask is a special step because it doesn't have it's own button
            logger.debug("Mask")
            self.mask_page.update_param(curr_step)
            self.step_param_widg.setCurrentWidget(self.mask_page)

        elif nxt_cmd == "modify_geometry":
            logger.info("\n modify_geometry \n")
            self.step_param_widg.setCurrentWidget(self.b_centr_page)

        else:
            logger.info("No action widget found in set_widget")
            logger.info("nxt_cmd = %s", nxt_cmd)

    def _action_button_clicked(self):
        "Slot: An action button was clicked"

        my_sender = self.sender()
        logger.debug("Action button clicked - %s", my_sender.action.id)

        # Switch to the pareter page for this action
        param_page = self.param_widgets[my_sender.action.id]
        self.step_param_widg.setCurrentWidget(param_page)

        # Appears to: Use my_label as a lookup of the action ID for this parameter page
        self.user_changed.emit(param_page.my_label)
        logger.debug(
            "my_label (action ID?) of parameter widget for clicked action: %s",
            param_page.my_label,
        )
        # TODO make sure is [[..label]] and not [..label]
        command_lst = [[str(param_page.my_label)]]
        self.update_command_lst_high_level.emit(command_lst)

        self.finished_masking.emit()
        self.finished_b_centr.emit()

    def gray_outs_all(self):
        """Disable all action buttons."""
        for btn in self.btn_lst:
            btn.setEnabled(False)

    def gray_outs_from_lst(self, lst_nxt):
        """
        Disable any action buttons not in a list.

        Arguments:
            lst_nxt (List[str]): List of action ID's to leave enabled
        """
        self.gray_outs_all()

        for btn in self.btn_lst:
            for cmd_str in lst_nxt:
                if btn.action.id == cmd_str:
                    btn.setEnabled(True)


class StopRunRetry(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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
        self.run_btn.setIconSize(QSize(50, 50))
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
        # self.show()


class DUIDataLoadingError(Exception):
    def __init__(self, original):
        self.original_traceback = original


def load_previous_state(dui_files_path):
    with open(dui_files_path / "bkp.pickle", "rb") as bkp_in:
        return pickle.load(bkp_in)


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        # Any child popup windows. Only bravais_table ATM
        self.reindex_dialog: MyReindexOpts = None
        self.storage_path = Path(sys_arg.directory)

        self.cli_tree_output = TreeShow()

        restoring_session = False

        # Load the previous state of DUI, if present
        dui_files_path = self.storage_path / "dui_files"

        if (dui_files_path / "bkp.pickle").is_file():
            try:
                self.idials_runner = load_previous_state(dui_files_path)
                self.cli_tree_output(self.idials_runner)

            except Exception as e:
                # Something went wrong - tell the user then close
                msg = traceback.format_exc()
                logger.error("ERROR LOADING PREVIOUS DATA:\n%s", msg)
                raise DUIDataLoadingError(msg) from e

            restoring_session = True
        else:
            self.idials_runner = Runner()
            self.cli_tree_output(self.idials_runner)

        self.cur_html = None
        self.cur_pick = None
        self.cur_json = None
        self.cur_log = None
        self.cur_cmd_name = "None"

        main_box = QVBoxLayout()

        self.centre_par_widget = ControlWidget()
        self.centre_par_widget.pass_sys_arg_object_to_import(sys_arg)
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

        # Splitters can only contain widgets, not layouts
        dummy_left_widget = QWidget()
        left_control_box.setContentsMargins(0, 0, 0, 0)
        dummy_left_widget.setLayout(left_control_box)

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)
        h_main_splitter.addWidget(dummy_left_widget)

        self.cli_out = CliOutView()
        self.web_view = WebTab()
        self.img_view = MyImgWin()
        self.ext_view = OuterCaller()
        self.info_widget = InfoWidget()

        self.output_info_tabs = QTabWidget()
        self.output_info_tabs.addTab(self.img_view, "Image")
        self.output_info_tabs.addTab(self.cli_out, "Log")
        self.output_info_tabs.addTab(self.web_view, "Report")
        self.output_info_tabs.addTab(self.ext_view, "Tools")
        self.output_info_tabs.addTab(self.info_widget, "Experiment")

        self.view_tab_num = 0
        self.output_info_tabs.currentChanged.connect(self.tab_changed)

        self.img_view.mask_applied.connect(self.pop_mask_list)
        self.img_view.predic_changed.connect(self.tab_changed)
        self.img_view.bc_applied.connect(self.pop_b_centr_coord)

        self.img_view.new_pars_applied.connect(self.pass_parmams)

        # self.ext_view.pass_parmam_lst.connect(self.pass_parmams)

        self.centre_par_widget.finished_masking.connect(self.img_view.unchec_my_mask)
        self.centre_par_widget.click_mask.connect(self.img_view.chec_my_mask)
        self.centre_par_widget.finished_b_centr.connect(self.img_view.unchec_b_centr)
        self.centre_par_widget.click_b_centr.connect(self.img_view.chec_b_centr)

        h_main_splitter.addWidget(self.output_info_tabs)

        main_box.addWidget(h_main_splitter)

        self.txt_bar = Text_w_Bar()
        main_box.addWidget(self.txt_bar)

        self.connect_all()

        self.custom_thread = CommandThread()
        self.custom_thread.finished.connect(self.update_after_finished)
        self.custom_thread.str_fail_signal.connect(self.after_failed)
        self.custom_thread.str_print_signal.connect(self.cli_out.add_txt)
        self.custom_thread.str_print_signal.connect(self.txt_bar.setText)

        self.custom_thread.busy_box_on.connect(self.pop_busy_box)
        self.custom_thread.busy_box_off.connect(self.close_busy_box)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

        self.setWindowTitle(f"CCP4 DUI - {__version__}: {dui_files_path}")
        self.setWindowIcon(QIcon(self.stop_run_retry.dials_logo_path))

        # Variable supresses showing the reindex GUI if on reindex step
        self.just_reindexed = False
        self.user_stoped = False
        self.reconnect_when_ready()

        if restoring_session:
            self.restore_gui_after_load()

    def pop_mask_list(self, mask_itm_lst):

        tmp_cmd_lst = build_mask_command_lst(mask_itm_lst)

        self.centre_par_widget.mask_page.set_par(tmp_cmd_lst)
        self.centre_par_widget.step_param_widg.setCurrentWidget(
            self.centre_par_widget.mask_page
        )

    def pop_b_centr_coord(self, new_b_centr):
        logger.info("New b_centr = %s", new_b_centr)
        self.centre_par_widget.b_centr_page.set_par(new_b_centr)
        self.centre_par_widget.step_param_widg.setCurrentWidget(
            self.centre_par_widget.b_centr_page
        )

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
            my_widget.activate_me(cur_nod=self.idials_runner.current_node)

        else:
            if self.idials_runner.current_node.ll_command_lst[0][0] not in (
                "export",
                "merge",
            ):
                self.stop_run_retry.repeat_btn.setEnabled(True)

            my_widget.gray_me_out()

        if self.idials_runner.current_node.ll_command_lst[0][0] == "reindex":
            self.stop_run_retry.run_btn.setEnabled(False)
            self.stop_run_retry.repeat_btn.setEnabled(False)

        self.check_gray_outs()
        self.user_stoped = False
        self.update_nav_tree()

    def chouse_if_predict_or_report(self):
        if (
            self.idials_runner.current_node.ll_command_lst[0][0]
            != "refine_bravais_settings"
        ):
            if self.view_tab_num == 0 and self.img_view.rad_but_pre_hkl.checkState():
                self.pop_busy_box(text_in_bar="Generating Predictions")
                self.idials_runner.current_node.gen_repr_n_pred(to_run="predict")
                self.close_busy_box()

            elif self.view_tab_num == 2:
                """
                ##########################################################################
                tmp_bar = ProgBarBox(min_val=0, max_val=10, text=text_in_bar)
                tmp_bar(5)
                tmp_bar.ended()
                ################################################################################
                """

                tmp_bar = ProgBarBox(min_val=0, max_val=10, text="Generating Report")
                tmp_bar(5)
                self.idials_runner.current_node.gen_repr_n_pred(to_run="report")
                tmp_bar.ended()

    def tab_changed(self, num=0):
        self.view_tab_num = num
        self.chouse_if_predict_or_report()

        update_info(self)

    def pass_parmams(self, cmd_lst):
        """(We've been passed a parameter by the external tool signal)"""

        current_parameter_widget = (
            self.centre_par_widget.step_param_widg.currentWidget()
        )
        action_name = current_parameter_widget.my_widget.command_lst[0][0]

        if (
            action_name == "find_spots"
            and self.idials_runner.current_node.success is None
        ):

            gain = cmd_lst[0]
            size = cmd_lst[1]
            nsig_b = cmd_lst[2]
            nsig_s = cmd_lst[3]
            global_threshold = cmd_lst[4]
            min_count = cmd_lst[5]

            full_command = [
                "find_spots",
                "spotfinder.threshold.dispersion.gain=" + str(gain),
                "spotfinder.threshold.dispersion.kernel_size="
                + str(size[0])
                + ","
                + str(size[1]),
                "spotfinder.threshold.dispersion.sigma_background=" + str(nsig_b),
                "spotfinder.threshold.dispersion.sigma_strong=" + str(nsig_s),
                "spotfinder.threshold.dispersion.min_local=" + str(min_count),
                "spotfinder.threshold.dispersion.global_threshold="
                + str(global_threshold),
            ]

            current_parameter_widget.my_widget.update_param_w_lst(full_command)

        else:
            logger.debug("No need to feed back params")
            """
            logger.info(
                "my_widget_now.my_widget.command_lst = %s",
                current_parameter_widget.my_widget.command_lst,
            )
            """

    def update_low_level_command_lst(self, command_lst):
        self.idials_runner.current_node.ll_command_lst = command_lst
        self.reconnect_when_ready()

    def cmd_changed_by_user(self, my_label):
        logger.debug("cmd_changed_by_user()")
        tmp_curr = self.idials_runner.current_node
        if tmp_curr.success is True:
            self.cmd_exe(["mkchi"])
            self.idials_runner.current_node.ll_command_lst = [[str(my_label)]]
            self.centre_par_widget.step_param_widg.currentWidget().my_widget.reset_par()

            path_to_mask_pickle = None
            if self.idials_runner.current_node.ll_command_lst[0][0] == "integrate":
                logger.debug("Running: try_find_prev_mask_pickle")
                path_to_mask_pickle = try_find_prev_mask_pickle(
                    self.idials_runner.current_node
                )
                if path_to_mask_pickle is not None:
                    self.pass_parmams(["lookup.mask=" + path_to_mask_pickle])

            self.cmd_exe(["clean"])

        elif tmp_curr.success is None:
            self.idials_runner.current_node.ll_command_lst[0] = [str(my_label)]
            self.reconnect_when_ready()

    def cmd_changed_by_any(self):
        tmp_curr_widg = self.centre_par_widget.step_param_widg.currentWidget()
        self.cur_cmd_name = tmp_curr_widg.my_widget.command_lst[0][0]
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

        self.img_view.draw_img_img()

        cmd_tmp = (
            self.centre_par_widget.step_param_widg.currentWidget().my_widget.command_lst
        )
        self.cmd_launch(cmd_tmp)

    def cmd_exe(self, new_cmd):
        # Running NOT in parallel
        update_info(self)
        self.idials_runner.run(command=new_cmd, ref_to_class=None)
        self.check_reindex_pop()
        self.reconnect_when_ready()

    def cmd_launch(self, new_cmd):
        # Ensure output directory for log files exists
        (self.storage_path / "dui_files").mkdir(exist_ok=True)

        # Running WITH threading
        self.cli_out.clear()
        self.cli_out.make_green()
        self.txt_bar.start_motion()
        self.txt_bar.setText("Running")
        self.disconnect_while_running()
        self.custom_thread(new_cmd, self.idials_runner)

    def update_after_finished(self):
        self.chouse_if_predict_or_report()
        update_info(self)

        self.txt_bar.end_motion()
        self.just_reindexed = False

        tmp_curr = self.idials_runner.current_node

        prn_lst_lst_cmd(tmp_curr)

        if (
            tmp_curr.ll_command_lst[0][0] == "refine_bravais_settings"
            and tmp_curr.success is True
        ):
            self.idials_runner.run(command=["mkchi"], ref_to_class=None)
            self.idials_runner.current_node.ll_command_lst = [["reindex"]]

        elif tmp_curr.ll_command_lst[0][0] == "reindex" and tmp_curr.success is True:

            # Supress opening of the reindex popup next time
            self.just_reindexed = True

        elif (
            tmp_curr.ll_command_lst[0][0] in ("export", "merge")
            and tmp_curr.success is True
        ):
            update_manifest(tmp_curr)

        self.check_reindex_pop()
        self.check_gray_outs()
        self.reconnect_when_ready()

        if (
            tmp_curr.ll_command_lst[0][0] == "generate_mask"
            and tmp_curr.success is True
        ):
            self.img_view.my_painter.reset_mask_tool(None)

        elif (
            tmp_curr.ll_command_lst[0][0] == "modify_geometry"
            and tmp_curr.success is True
        ):
            self.img_view.my_painter.reset_bc_tool(None)

        with open(self.storage_path / "dui_files" / "bkp.pickle", "wb") as bkp_out:
            pickle.dump(self.idials_runner, bkp_out)

    def pop_busy_box(self, text_in_bar):
        # logger.info(f"OPENING busy pop bar with the text: {text_in_bar}")
        if (
            self.idials_runner.current_node.ll_command_lst[0][0]
            != "refine_bravais_settings"
        ):
            self.my_bar = ProgBarBox(min_val=0, max_val=10, text=text_in_bar)
            self.my_bar(5)

    def close_busy_box(self):
        if hasattr(self, "my_bar"):
            logger.info("closing busy pop bar")
            self.my_bar.ended()

    def check_gray_outs(self):
        tmp_curr = self.idials_runner.current_node
        if tmp_curr.success is not True:
            tmp_curr = tmp_curr.prev_step

        # TODO fix "generate_mask" and "modify_geometry" : it should be the same as the previous step

        # This dictionary defines which tasks can be performed at each step and
        # which should be grayed out
        cmd_connects = {
            "Root": ["import"],
            "import": ["find_spots"],
            "find_spots": ["index"],
            "index": ["refine_bravais_settings", "refine", "integrate"],
            "refine_bravais_settings": [None],
            "reindex": ["refine", "integrate", "index"],
            "refine": [
                "refine_bravais_settings",
                "refine",
                "integrate",
                "index",
            ],
            "integrate": ["symmetry", "scale", "export", "index", "export"],
            "symmetry": ["refine_bravais_settings", "scale", "export"],
            "scale": ["refine_bravais_settings", "symmetry", "export"],
            "export": [None],
            "merge": [None],
            "generate_mask": ["find_spots"],
            "modify_geometry": ["find_spots"],
            "None": [None],
        }

        lst_nxt = cmd_connects[str(tmp_curr.ll_command_lst[0][0])]
        self.centre_par_widget.gray_outs_from_lst(lst_nxt)

    def check_reindex_pop(self, allow_cancel=False):
        # Always either close popup or open new one when calling this
        node = self.idials_runner.current_node
        command = node.ll_command_lst[0]
        logger.debug(
            "check_reindex_pop: just_reindexed: %s, command: %s",
            self.just_reindexed,
            command,
        )
        if command[0] == "reindex" and not self.just_reindexed:
            # Find if one of the command arguments was a previous solution
            solution_argument = [x for x in command if "solution=" in x]
            prev_solution = None
            if solution_argument:
                prev_solution = int(
                    re.match(r"solution=(\d+)", solution_argument[-1]).group(1)
                )
                logger.debug("Found previous solution: %s", prev_solution)

            logger.debug("Redetermining reindex decision")
            self.reindex_dialog = MyReindexOpts(
                parent=self,
                summary_json=node.prev_step.json_file_out,
                bravais_node_id=node.prev_step.lin_num,
                show_cancel=allow_cancel,
                solution=prev_solution,
            )
            self.reindex_dialog.finished.connect(self.reindex_dialog_finished)
            self.reindex_dialog.open()

        # Either we closed, or opened - can do so next time also
        self.just_reindexed = False

    def update_nav_tree(self):
        self.tree_out.update_me(
            self.idials_runner.step_list[0], self.idials_runner.current_line
        )
        update_pbar_msg(self)
        self.img_view.my_painter.repaint()

    def after_failed(self):
        logger.info("\n FAILED STEP:")
        self.update_nav_tree()
        self.txt_bar.end_motion()

        curr_step = self.idials_runner.current_node

        for err_lin in curr_step.dials_command.tmp_std_all:
            logger.debug(err_lin)

        err_log_file_out = (
            self.storage_path / "dui_files" / f"{curr_step.lin_num}_err_out.log"
        )

        logger.info("\n ERROR \n err_log_file_out = %s", err_log_file_out)

        fil_obj = open(err_log_file_out, "wt")
        for err_lin in curr_step.dials_command.tmp_std_all:
            fil_obj.write(err_lin)
            fil_obj.write("\n")

        fil_obj.close()
        self.idials_runner.current_node.err_file_out = err_log_file_out

    def reindex_dialog_finished(self, result: int):
        """Process the results from a reindex dialog closing."""
        # Grab the result and discard the dialog
        reindex_index = self.reindex_dialog.solution
        self.reindex_dialog = None

        if result == QDialog.DialogCode.Rejected:
            return

        logger.debug("Chose reindex solution %s", reindex_index)

        # Reindex to this solution
        node = self.idials_runner.current_node
        reindex_command = ["reindex", f"solution={reindex_index}"]
        if node.ll_command_lst[0] != reindex_command or node.success is None:
            self.cmd_launch([reindex_command])
        else:
            logger.info("Reindex would result in no change. Skipping.")

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
                logger.info(
                    " Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.info("\n Tst A1 \n")

            item = self.tree_out.std_mod.itemFromIndex(it_index)
            prn_lst_lst_cmd(item.idials_node)
            lin_num = item.idials_node.lin_num
            cmd_ovr = "goto " + str(lin_num)

            # Suppress reindex gui for cmd_exe - we will try explicitly
            self.just_reindexed = True
            self.cmd_exe(cmd_ovr)

            self.centre_par_widget.set_widget(
                nxt_cmd=item.idials_node.ll_command_lst[0][0],
                curr_step=self.idials_runner.current_node,
            )

            # Always want to show if clicking a new reindex node
            self.just_reindexed = False
            self.check_reindex_pop(allow_cancel=True)

            self.chouse_if_predict_or_report()
            update_info(self)

            self.check_gray_outs()
            self.reconnect_when_ready()

            self.centre_par_widget.update_command_lst_high_level.connect(
                self.update_low_level_command_lst
            )

    def restore_gui_after_load(self):
        """Restore the GUI state after first loading dui"""

        lin_num = self.idials_runner.current_node.lin_num
        logger.debug("doing goto:  %s", lin_num)
        cmd_ovr = "goto " + str(lin_num)
        # cmd_exe calls check_reindex_pop - prevent displaying reindex gui on load
        self.just_reindexed = True
        self.cmd_exe(cmd_ovr)

        self.centre_par_widget.set_widget(
            nxt_cmd=self.idials_runner.current_node.ll_command_lst[0][0],
            curr_step=self.idials_runner.current_node,
        )

        # Called this explicitly to implicitly cause the popup to to close
        # - we never want to do this now because want to prevent popup opening
        # self.check_reindex_pop()

        self.chouse_if_predict_or_report()
        update_info(self)
        self.check_gray_outs()
        self.reconnect_when_ready()

        # We want to show the dialog next time... probably
        self.just_reindexed = False

        logger.info("\n ... recovering from previous run of GUI \n")

    def closeEvent(self, event):
        if self.reindex_dialog:
            self.reindex_dialog.close()
