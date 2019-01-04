"""
Containers for widgets related to each step

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
import sys

from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import phil_scope as phil_scope_index
from dials.command_line.refine_bravais_settings import (
    phil_scope as phil_scope_r_b_settings,
)
from dials.command_line.refine import phil_scope as phil_scope_refine
from dials.command_line.integrate import phil_scope as phil_scope_integrate
from dials.command_line.symmetry import phil_scope as phil_scope_symetry
from dials.command_line.scale import phil_scope as phil_scope_scale

# from dials.command_line.export import phil_scope as phil_scope_export

from .gui_utils import get_import_run_string, get_main_path
from .params_live_gui_generator import PhilWidget
from .simpler_param_widgets import (
    FindspotsSimplerParameterTab,
    IndexSimplerParamTab,
    RefineBravaiSimplerParamTab,
    RefineSimplerParamTab,
    IntegrateSimplerParamTab,
    SymmetrySimplerParamTab,
    ScaleSimplerParamTab,
)
from .qt import (
    QApplication,
    QCheckBox,
    QColor,
    QFileDialog,
    QFont,
    QHBoxLayout,
    QIcon,
    QLabel,
    QLineEdit,
    QPalette,
    QPushButton,
    QScrollArea,
    QSize,
    QSpinBox,
    QTabWidget,
    QTimer,
    QVBoxLayout,
    QWidget,
    Signal,
)
from six.moves import range

logger = logging.getLogger(__name__)


class ExportPage(QWidget):

    update_command_lst_low_level = Signal(list)

    """
    This stacked widget basically helps the user to export by
    generating an MTZ file, there is no auto-generated GUI
    form Phil parameters in use withing this widget.
    """

    def __init__(self, parent=None):
        super(ExportPage, self).__init__(parent=None)

        main_v_box = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel(str("Export"))
        step_label.setFont(label_font)

        out_file_label = QLabel(str("mtz output name:"))

        self.simple_lin = QLineEdit(self)
        self.simple_lin.textChanged.connect(self.update_command)

        self.check_scale = QCheckBox("Output Scaled Intensities")
        self.check_scale.setChecked(False)
        self.check_scale.stateChanged.connect(self.update_command)

        main_v_box.addWidget(step_label)
        main_v_box.addWidget(out_file_label)
        main_v_box.addWidget(self.simple_lin)
        main_v_box.addWidget(self.check_scale)

        main_v_box.addStretch()
        self.setLayout(main_v_box)
        # self.show()

        self.simple_lin.setText("integrated.mtz")

    def update_command(self):
        self.command_lst = ["export"]

        param1_com = str(self.simple_lin.text())
        logger.debug("param1_com = %s", param1_com)

        self.command_lst.append("mtz.hklout=" + param1_com)

        if self.check_scale.checkState():
            param2_com = "intensity=scale"
            logger.debug("param2_com = %s", param2_com)

            self.command_lst.append(param2_com)

        self.update_command_lst_low_level.emit(self.command_lst)
        logger.debug("self.command_lst = %s", self.command_lst)

        for lin_prn in self.command_lst:
            logger.debug("lin_prn = %s", lin_prn)

    def gray_me_out(self):
        self.simple_lin.setEnabled(False)

    def activate_me(self):
        self.simple_lin.setEnabled(True)

    def reset_par(self):
        logger.debug(" Not supposed to reset export page")


class ImportPage(QWidget):

    update_command_lst_low_level = Signal(list)

    """
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    """

    def __init__(self, parent=None):
        super(ImportPage, self).__init__(parent=None)

        main_v_box = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel(str("Import"))
        step_label.setFont(label_font)

        self.simple_lin = QLineEdit(self)
        self.simple_lin.setText(" ? ")
        self.simple_lin.textChanged.connect(self.update_command)

        self.x_spn_bx = QSpinBox()
        self.x_spn_bx.setMaximum(99999)
        self.x_spn_bx.setSpecialValueText("Auto")
        # self.x_spn_bx.setValue(6.0)
        self.y_spn_bx = QSpinBox()
        self.y_spn_bx.setMaximum(99999)
        self.y_spn_bx.setSpecialValueText("Auto")

        # self.y_spn_bx.setValue(6.0)
        self.x_spn_bx.valueChanged.connect(self.x_beam_changed)
        self.y_spn_bx.valueChanged.connect(self.y_beam_changed)

        self.chk_invert = QCheckBox("Invert Rotation Axis")
        self.chk_invert.setChecked(False)
        self.chk_invert.stateChanged.connect(self.inv_rota_changed)

        self.opn_fil_btn = QPushButton(" \n Select File(s) \n ")

        main_path = get_main_path()
        logger.debug("main_path = %s", main_path)
        self.opn_fil_btn.setIcon(QIcon(main_path + "/resources/import.png"))
        self.opn_fil_btn.setIconSize(QSize(80, 48))

        main_v_box.addWidget(step_label)
        main_v_box.addWidget(self.opn_fil_btn)
        main_v_box.addWidget(self.simple_lin)
        self.b_cetre_label = QLabel("\n\n Beam Centre")
        main_v_box.addWidget(self.b_cetre_label)
        cent_hbox = QHBoxLayout()
        self.x_label = QLabel("    X: ")
        cent_hbox.addWidget(self.x_label)
        cent_hbox.addWidget(self.x_spn_bx)
        self.y_label = QLabel("    Y: ")
        cent_hbox.addWidget(self.y_label)
        cent_hbox.addWidget(self.y_spn_bx)
        #    cent_hbox.addWidget(QLabel(" \n "))
        cent_hbox.addStretch()
        main_v_box.addLayout(cent_hbox)
        main_v_box.addWidget(self.chk_invert)
        main_v_box.addStretch()

        self.opn_fil_btn.clicked.connect(self.open_files)

        self.cmd_list = []
        self.x_beam, self.y_beam = 0.0, 0.0
        self.path_file_str = ""
        self.second_half = ""
        self.third_half = ""

        self.defa_dir = str(os.getcwd())
        self.setLayout(main_v_box)
        # self.show()

    def inv_rota_changed(self):
        logger.debug("self.chk_invert.checkState(): %s", self.chk_invert.checkState())
        if self.chk_invert.checkState():
            self.third_half = "invert_rotation_axis=True"

        else:
            self.third_half = ""

        self.put_str_lin()

    def x_beam_changed(self, value):
        self.x_beam = value
        logger.debug("New Beam pos(X) = %s", self.x_beam)
        self.build_second_half()

    def y_beam_changed(self, value):
        self.y_beam = value
        logger.debug("New Beam pos(Y) = %s", self.y_beam)
        self.build_second_half()

    def build_second_half(self):
        logger.debug("%s %s", self.x_beam, self.y_beam)
        if self.x_beam != 0.0 and self.y_beam != 0.0:
            self.second_half = (
                "slow_fast_beam_centre=" + str(self.y_beam) + "," + str(self.x_beam)
            )

        else:
            self.second_half = ""

        self.put_str_lin()

    def open_files(self):
        lst_file_path = QFileDialog.getOpenFileNames(
            self, "Open File(s)", self.defa_dir, "All Files (*.*)"
        )

        if len(lst_file_path) > 0:
            new_dir, new_command = get_import_run_string(lst_file_path)
            self.path_file_str = new_command
            self.defa_dir = new_dir
            self.put_str_lin()

    def put_str_lin(self):
        self.cmd_list = [
            self.path_file_str,
            self.second_half.lstrip(),
            self.third_half.lstrip(),
        ]
        txt_lin = " ".join(self.cmd_list).rstrip()
        while "  " in txt_lin:
            txt_lin = txt_lin.replace("  ", " ")

        self.simple_lin.setText(txt_lin)

        logger.debug("self.simple_lin.setText:<<" + txt_lin + ">>")

    def get_arg_obj(self, sys_arg_in):
        logger.debug("sys_arg_in = %s", sys_arg_in)
        if sys_arg_in.template is not None:
            str_arg = str(sys_arg_in.template)
            self.simple_lin.setText(str_arg)

    def update_command(self):
        logger.debug("action_simple")
        self.command_lst = ["import"]
        param_com = str(self.simple_lin.text())
        logger.debug("param_com = %s", param_com)

        cmd_lst = param_com.split(" ")
        logger.debug("cmd_lst = %s", cmd_lst)

        for single_com in cmd_lst:
            self.command_lst.append(single_com)

        self.update_command_lst_low_level.emit(self.command_lst)
        logger.debug("self.command_lst = %s", self.command_lst)

        logger.debug("\n loop print \n")

        for lin_prn in self.command_lst:
            logger.debug("lin_prn = %s", lin_prn)

    def gray_me_out(self):
        self.simple_lin.setEnabled(False)
        self.opn_fil_btn.setEnabled(False)
        self.x_spn_bx.setEnabled(False)
        self.y_spn_bx.setEnabled(False)
        self.x_label.setEnabled(False)
        self.y_label.setEnabled(False)
        self.b_cetre_label.setEnabled(False)
        self.chk_invert.setEnabled(False)

    def activate_me(self):
        self.simple_lin.setEnabled(True)
        self.opn_fil_btn.setEnabled(True)
        self.y_spn_bx.setEnabled(True)
        self.x_spn_bx.setEnabled(True)
        self.x_label.setEnabled(True)
        self.y_label.setEnabled(True)
        self.b_cetre_label.setEnabled(True)
        self.chk_invert.setEnabled(True)


class ParamAdvancedWidget(QWidget):
    def __init__(self, phl_obj=None, parent=None):
        super(ParamAdvancedWidget, self).__init__()

        self.scrollable_widget = PhilWidget(phl_obj, parent=self)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        vbox = QVBoxLayout()

        search_label = QLabel("search:")
        search_edit = QLineEdit("type search here")
        search_edit.textChanged.connect(self.scrollable_widget.user_searching)

        hbox = QHBoxLayout()
        hbox.addWidget(search_label)
        hbox.addWidget(search_edit)
        vbox.addLayout(hbox)

        vbox.addWidget(scrollArea)
        self.setLayout(vbox)
        # self.show()


def update_lst_pair(lst_ini, str_path, str_value):
    new_lst = []
    found = False
    for pos, pair in enumerate(lst_ini):
        if pair[0] == str_path:
            new_pair = [str_path, str_value]
            found = True
        else:
            new_pair = pair

        new_lst.append(new_pair)

    if not found:
        new_lst.append([str_path, str_value])

    return new_lst


def pair2string(str_path, str_value):
    str_out = str(str_path) + "=" + str(str_value)
    return str_out


def build_lst_str(cmd_0, lst_pair):
    lst_str = [cmd_0]
    for pair in lst_pair:
        str_cmd = pair2string(pair[0], pair[1])
        if pair[1] != "":
            lst_str.append(str_cmd)

    return lst_str


def string2pair(str_in):
    pair = None
    for pos, single_char in enumerate(str_in):
        if single_char == "=":
            pair = [str_in[0:pos], str_in[pos + 1 :]]
            return pair


def buils_lst_pair(lst_in):
    lst_pair = []
    for par_str in lst_in[1 : len(lst_in)]:
        logger.debug("par_str = %s", par_str)
        pair = string2pair(par_str)
        logger.debug("pair = %s", pair)
        lst_pair.append(pair)

    return lst_pair


class ParamMainWidget(QWidget):

    update_command_lst_low_level = Signal(list)

    def __init__(self, phl_obj=None, simp_widg=None, parent=None, upper_label=None):
        super(ParamMainWidget, self).__init__()

        self.command_lst = [None]
        self.lst_pair = []

        try:
            self.my_phl_obj = phl_obj
            self.simp_widg_in = simp_widg
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("\n\n\n something went wrong here wiht the phil object \n\n\n")

        self.build_param_widget()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        self.step_label = QLabel(str(upper_label))
        self.step_label.setFont(label_font)

        self._vbox = QVBoxLayout()
        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)

        self.setLayout(self._vbox)
        # self.show()

    def build_param_widget(self):
        self.dual_level_tab = QTabWidget()
        self.simpler_widget = self.simp_widg_in()
        self.advanced_widget = ParamAdvancedWidget(phl_obj=self.my_phl_obj, parent=self)
        self.advanced_widget.scrollable_widget.item_changed.connect(self.update_lin_txt)

        try:
            self.simpler_widget.item_changed.connect(self.update_advanced_widget)
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("found self.simpler_widget without << item_changed >> signal")

        try:
            self.simpler_widget.item_to_remove.connect(self.remove_one_par)
        except AttributeError:
            # simpler_widget has no item_to_remove
            logger.debug(
                "found self.simpler_widget without << item_to_remove >> signal"
            )

        self.reset_btn = self.simpler_widget.inner_reset_btn
        self.dual_level_tab.addTab(self.simpler_widget, "Simple")
        self.dual_level_tab.addTab(self.advanced_widget, "Advanced")
        self.reset_btn.clicked.connect(self.reset_par)

    def reset_par(self):
        logger.debug("Reseting")

        for i in reversed(list(range(self._vbox.count()))):
            widgetToRemove = self._vbox.itemAt(i).widget()
            self._vbox.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        self.build_param_widget()

        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)

        logger.debug("<< inner >>self.command_lst = %s", self.command_lst)
        self.command_lst = [self.command_lst[0]]
        self.lst_pair = []
        logger.debug("<< inner >>self.command_lst = %s", self.command_lst)

        self.update_command_lst_low_level.emit(self.command_lst)

        try:
            max_nproc = self.simpler_widget.set_max_nproc()
            if max_nproc > 1:
                logger.debug("\n time to raise nproc to: %s %s", max_nproc, " \n")
                self.raise_nproc_str = (
                    str(self.simpler_widget.box_nproc.local_path) + "=" + str(max_nproc)
                )
                QTimer.singleShot(1000, self.raise_nproc_to_max)
                logger.debug("tst 03")
        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.error("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.debug("\n This step runs as fast as it can with nproc = 1 \n")

    def raise_nproc_to_max(self):
        found_nproc = False
        for single_par in self.command_lst:
            if "mp.nproc" in single_par:
                found_nproc = True

        if not found_nproc:
            self.command_lst.append(self.raise_nproc_str)
            self.update_command_lst_low_level.emit(self.command_lst)

    def update_advanced_widget(self, str_path, str_value):

        for bg_widg in (
            self.advanced_widget.scrollable_widget.lst_var_widg,
            self.simpler_widget.lst_var_widg,
        ):
            for widg in bg_widg:
                try:
                    if widg.local_path == str_path:
                        if not hasattr(widg, "tmp_lst") or widg.tmp_lst is None:
                            try:
                                num_val = float(str_value)
                                widg.setValue(num_val)
                            except ValueError:
                                try:
                                    str_val = str(str_value)
                                    widg.setText(str_val)
                                    logger.debug(
                                        "widg.local_path = %s", widg.local_path
                                    )

                                except BaseException as e:
                                    # We don't want to catch bare exceptions but don't
                                    # know what this was supposed to catch. Log it.
                                    logger.error(
                                        "Caught unknown exception type %s: %s",
                                        type(e).__name__,
                                        e,
                                    )
                                    logger.debug(
                                        "Type mismatch searching for twin parameter"
                                    )

                        else:
                            for pos, val in enumerate(widg.tmp_lst):
                                if val == str_value:
                                    try:
                                        logger.debug("found val, v= %s", val)
                                        widg.setCurrentIndex(pos)
                                    except BaseException as e:
                                        # We don't want to catch bare exceptions but
                                        # dont know what this was supposed to catch.
                                        logger.error("Caught unknown exception: %s", e)
                                        logger.debug("failed to:")
                                        logger.debug("widg.setCurrentIndex(pos)")

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )

        logger.debug("finished update_advanced_widget")

    def update_simpler_widget(self, str_path, str_value):

        logger.debug(
            "update_simpler_widget( %s %s %s %s", str_path, ", ", str_value, ")"
        )

        for widg in self.simpler_widget.lst_var_widg:
            try:
                if widg.local_path == str_path:
                    logger.debug("found << widg.local_path == str_path >> ")
                    try:
                        num_val = float(str_value)
                        widg.setValue(num_val)
                    except ValueError:
                        try:
                            for pos, val in enumerate(widg.tmp_lst):
                                if val == str_value:
                                    logger.debug("found val, v= %s", val)
                                    widg.setCurrentIndex(pos)
                        except BaseException as e:
                            # We don't want to catch bare exceptions but don't know
                            # what this was supposed to catch. Log it.
                            logger.error(
                                "Caught unknown exception type %s: %s",
                                type(e).__name__,
                                e,
                            )
                            logger.debug(
                                "\n\n Type Mismatch in simpler_param_widgets \n\n"
                            )
            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.error(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("skip label_str")

    def update_lin_txt(self, str_path, str_value):
        # cmd_to_run = str_path + "=" + str_value
        self.update_advanced_widget(str_path, str_value)
        self.update_simpler_widget(str_path, str_value)

        self.lst_pair = update_lst_pair(self.lst_pair, str_path, str_value)
        self.command_lst = build_lst_str(self.command_lst[0], self.lst_pair)
        self.update_command_lst_low_level.emit(self.command_lst)

    def update_param_w_lst(self, lst_in, do_reset=True):

        logger.debug("update_param_w_lst(self,  %s)", lst_in)
        if do_reset:
            self.reset_par()

        logger.debug("_________________ after reset_par")
        if len(lst_in) > 1:
            logger.debug("restoring advanced widgets")
            self.lst_pair = buils_lst_pair(lst_in)
            logger.debug("lst_pair done")
            self.command_lst = build_lst_str(lst_in[0], self.lst_pair)
            logger.debug("looping thru params")
            for pair in self.lst_pair:
                self.update_advanced_widget(pair[0], pair[1])

        else:
            logger.debug("updating with no parameters")
            self.lst_pair = []
            self.command_lst = lst_in
            logger.debug("")

        logger.debug("after update widgets")

    def remove_one_par(self, path_str):
        logger.debug("\n removing: %s %s", path_str, "parameter \n")
        nxt_lst = []
        for single_param in self.command_lst:
            if str(path_str) in single_param:
                logger.debug("found:  %s", single_param)

            else:
                nxt_lst.append(str(single_param))

        self.update_param_w_lst(nxt_lst, do_reset=False)

    def gray_me_out(self):
        self.reset_btn.setEnabled(False)
        palt_gray = QPalette()
        palt_gray.setColor(QPalette.WindowText, QColor(88, 88, 88, 88))
        for bg_widg in (
            self.advanced_widget.scrollable_widget.lst_var_widg,
            self.advanced_widget.scrollable_widget.lst_label_widg,
            self.simpler_widget.lst_var_widg,
        ):

            for widg in bg_widg:
                widg.setStyleSheet("color: rgba(88, 88, 88, 88)")

                try:
                    widg.setEnabled(False)
                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    pass

    def activate_me(self):
        self.reset_btn.setEnabled(True)
        for bg_widg in (
            self.advanced_widget.scrollable_widget.lst_var_widg,
            self.advanced_widget.scrollable_widget.lst_label_widg,
            self.simpler_widget.lst_var_widg,
        ):

            for widg in bg_widg:

                widg.setStyleSheet("color: rgba(0, 0, 0, 255)")
                try:
                    widg.setStyleSheet(widg.style_orign)
                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    pass

                try:
                    widg.setEnabled(True)
                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.error(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    pass


class ParamWidget(QWidget):

    update_command_lst_medium_level = Signal(list)

    def __init__(self, label_str):
        super(ParamWidget, self).__init__()
        self.my_label = label_str

        inner_widgs = {
            "find_spots": [phil_scope_find_spots, FindspotsSimplerParameterTab],
            "index": [phil_scope_index, IndexSimplerParamTab],
            "refine_bravais_settings": [
                phil_scope_r_b_settings,
                RefineBravaiSimplerParamTab,
            ],
            "refine": [phil_scope_refine, RefineSimplerParamTab],
            "integrate": [phil_scope_integrate, IntegrateSimplerParamTab],
            "symmetry": [phil_scope_symetry, SymmetrySimplerParamTab],
            "scale": [phil_scope_scale, ScaleSimplerParamTab],
        }

        if label_str == "import":
            self.my_widget = ImportPage()

        elif label_str == "export":
            self.my_widget = ExportPage()

        else:
            self.my_widget = ParamMainWidget(
                phl_obj=inner_widgs[label_str][0],
                simp_widg=inner_widgs[label_str][1],
                parent=self,
                upper_label=label_str,
            )

        self.my_widget.command_lst = [label_str]

        self.my_widget.update_command_lst_low_level.connect(self.update_parent_lst)

        v_left_box = QVBoxLayout()
        v_left_box.addWidget(self.my_widget)
        self.setLayout(v_left_box)
        # self.show()

    def update_param(self, curr_step):

        logger.debug("update_param( %s %s", curr_step.command_lst, ")")
        self.my_widget.update_param_w_lst(curr_step.command_lst)

    def update_parent_lst(self, command_lst):
        self.update_command_lst_medium_level.emit(command_lst)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ex = ParamWidget("find_spots")
    # ex = ParamWidget("integrate")
    # ex = ParamWidget("import")
    # ex = ParamWidget("index")
    # ex = ParamWidget("refine")
    # ex = ParamWidget("integrate")
    # ex = ParamWidget("symmetry")
    # ex = ParamWidget("scale")
    ex = ParamWidget("export")
    sys.exit(app.exec_())
