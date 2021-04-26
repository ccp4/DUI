"""
Containers for widgets related to each step

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
import os
import shlex
import sys
from typing import List

import libtbx.phil
from dials.command_line.find_spots import phil_scope as phil_scope_find_spots
from dials.command_line.index import working_phil as phil_scope_index
from dials.command_line.integrate import phil_scope as phil_scope_integrate
from dials.command_line.refine import working_phil as phil_scope_refine
from dials.command_line.refine_bravais_settings import (
    phil_scope as phil_scope_r_b_settings,
)

from dui.cli_utils import sys_arg
from dui.gui_utils import escaped_join, get_import_run_string, get_main_path
from dui.params_live_gui_generator import PhilWidget
from dui.qt import (
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
from dui.simpler_param_widgets import (
    FindspotsSimplerParameterTab,
    IndexSimplerParamTab,
    IntegrateSimplerParamTab,
    RefineBravaiSimplerParamTab,
    RefineSimplerParamTab,
    ScaleSimplerParamTab,
    SymmetrySimplerParamTab,
    ResetButton,
)

# HACK - CCP4 7.69 both scale and symmetry are broken - so make sure DUI
# still runs. This isn't generally robust but solves this specifically
try:
    from dials.command_line.symmetry import phil_scope as phil_scope_symetry
except ImportError:
    phil_scope_symetry = libtbx.phil.parse("")

try:
    from dials.command_line.scale import phil_scope as phil_scope_scale
except ImportError:
    phil_scope_scale = libtbx.phil.parse("")

logger = logging.getLogger(__name__)


class BeamCentrPage(QWidget):
    update_command_lst_medium_level = Signal(list)

    """
    This stacked widget appears when the user wants
    to set manually the beam center, there is no
    auto-generated GUI form Phil parameters in use
    withing this widget.
    """

    b_centr_done = Signal()
    b_centr_set = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        main_v_box = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel("Modify Geometry")
        step_label.setFont(label_font)

        self.data_bc_label = QLabel("empty Data ... for now")

        main_v_box.addWidget(step_label)
        main_v_box.addStretch()
        main_v_box.addWidget(self.data_bc_label)
        main_v_box.addStretch()

        self.setLayout(main_v_box)
        self.command_lst = [["modify_geometry"]]

        self.show()
        self.my_widget = self

    def gray_me_out(self):
        # self.something.setEnabled(False)
        self.b_centr_done.emit()
        logger.info("gray_me_out(BeamCentrPage)")

    def update_param(self, curr_step):
        logger.info("update_param(BeamCentrPage)")
        logger.info("curr_step.ll_command_lst: %s", curr_step.ll_command_lst)

    def activate_me(self, cur_nod=None):
        self.b_centr_set.emit()

    def reset_par(self):
        logger.info("reset_par(BeamCentrPage)")

    def set_par(self, lst_par):
        logger.info("set_par(BeamCentrPage) %s", lst_par)

        self.data_bc_label.setText(
            "New beam centre:\n ("
            + str(lst_par[0])
            + ", "
            + str(lst_par[1])
            + ") pixels"
        )

        ml_lst_par = [
            "modify_geometry",
            "geometry.detector.slow_fast_beam_centre="
            + str(lst_par[1])
            + ","
            + str(lst_par[0]),
        ]

        self.command_lst = [ml_lst_par]
        self.update_command_lst_medium_level.emit(ml_lst_par)


class InnerMask(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.outher_box = QVBoxLayout()
        self.list_widg = QVBoxLayout()
        self.list_widg.addWidget(QLabel("empty List ... for now"))
        self.outher_box.addStretch()
        self.outher_box.addLayout(self.list_widg)
        self.outher_box.addStretch()
        self.setLayout(self.outher_box)
        self.show()

    def update_cmd_lst(self, lst_par):

        for i in reversed(range(self.list_widg.count())):
            widgetToRemove = self.list_widg.itemAt(i).widget()
            self.list_widg.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        for singl_com in lst_par[0]:
            new_widg = QLabel(str(singl_com))
            self.list_widg.addWidget(new_widg)


class MaskPage(QWidget):

    update_command_lst_medium_level = Signal(list)
    mask_done = Signal()
    mask_set = Signal()

    """
    This stacked widget appears when the user wants to
    do (...) apply_mask, there is no auto-generated GUI
    form Phil parameters in use withing this widget.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        main_v_box = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel("Apply Mask")
        step_label.setFont(label_font)

        self.my_scroll_area = QScrollArea()
        self.my_scroll_area.setWidgetResizable(True)
        self.my_inner_widget = InnerMask(self)
        self.my_scroll_area.setWidget(self.my_inner_widget)

        main_v_box.addWidget(step_label)
        main_v_box.addWidget(self.my_scroll_area)

        self.setLayout(main_v_box)

        self.my_widget = self
        self.show()

    def gray_me_out(self):
        # self.something.setEnabled(False)
        logger.info("gray_me_out(MaskPage)")
        self.mask_done.emit()

    def update_param(self, curr_step):
        logger.info("update_param(MaskPage)")
        self.update_widget_dat(curr_step.ll_command_lst)

    def activate_me(self, cur_nod):
        self.update_widget_dat(cur_nod.ll_command_lst)
        self.mask_set.emit()

    def reset_par(self):
        logger.info("reset_par(MaskPage)")
        self.command_lst = [["generate_mask"]]

    def set_par(self, lst_par):
        # logger.info(f"set_par(MaskPage) {lst_par}")
        self.update_widget_dat(lst_par)
        self.update_command_lst_medium_level.emit(lst_par[0])

    def update_widget_dat(self, lst_par):
        self.my_inner_widget.update_cmd_lst(lst_par)
        self.command_lst = lst_par


class ExportPage(QWidget):

    update_command_lst_low_level = Signal(list)

    """
    This stacked widget basically helps the user to export by
    generating an MTZ file, there is no auto-generated GUI
    form Phil parameters in use withing this widget.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        main_v_box = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel("Export")
        step_label.setFont(label_font)

        out_file_label = QLabel("mtz output name:")

        self.simple_lin = QLineEdit(self)
        self.simple_lin.textChanged.connect(self.update_command)

        self.check_scale = QCheckBox("Output Scaled Intensities")
        self.check_scale.setChecked(False)
        self.check_scale.stateChanged.connect(self.update_command)

        self.warning_label = QLabel(" ")
        self.warning_label.setWordWrap(True)

        main_v_box.addWidget(step_label)
        main_v_box.addWidget(out_file_label)
        main_v_box.addWidget(self.simple_lin)
        main_v_box.addWidget(self.check_scale)
        main_v_box.addStretch()
        main_v_box.addWidget(self.warning_label)
        main_v_box.addStretch()
        self.setLayout(main_v_box)
        self.fist_time = False
        # self.show()

        self.simple_lin.setText("integrated.mtz")

    def update_command(self):
        self.command_lst = [["export"]]

        param1_com = str(self.simple_lin.text())
        self.command_lst[0].append("mtz.hklout=" + param1_com)

        if self.check_scale.checkState():
            param2_com = "intensity=scale"
            self.command_lst[0].append(param2_com)

        self.update_command_lst_low_level.emit(self.command_lst[0])
        self.check_repeated_file()

    def check_repeated_file(self):
        param1_com = str(self.simple_lin.text())
        cwd_path = os.path.join(sys_arg.directory, "dui_files")
        mtz_file_path = os.path.join(cwd_path, param1_com)
        if os.path.isfile(mtz_file_path):
            txt_warning = "Warning, file: " + param1_com + " already exists"
            self.warning_label.setText(txt_warning)
            self.warning_label.setStyleSheet("color: rgba(255, 55, 55, 255)")
            """
            self.warning_label.setStyleSheet(
                        "color: rgba(255, 55, 55, 255);" "background-color: yellow;"
                    )
            """
        else:
            self.warning_label.setText(" ")
            self.warning_label.setStyleSheet("color: rgba(0, 155, 255, 255)")

    def gray_me_out(self):
        self.simple_lin.setEnabled(False)
        self.check_scale.setEnabled(False)

        self.fist_time = False

    def activate_me(self, cur_nod=None):
        self.simple_lin.setEnabled(True)
        self.check_scale.setEnabled(True)
        if self.fist_time is False:
            self.fist_time = True
            self.simple_lin.setText("integrated.mtz")
            self.check_scale.setChecked(False)
            my_node = cur_nod
            found_scale = False
            for iters in range(5):
                try:
                    if my_node.ll_command_lst[0][0] == "scale":
                        found_scale = True
                        break

                except AttributeError as at_err:
                    logger.info("found %s in for loop - not to worry", at_err)

                my_node = my_node.prev_step

            if found_scale is True:
                self.simple_lin.setText("scaled.mtz")
                self.check_scale.setChecked(True)

        self.check_repeated_file()

    def reset_par(self):
        logger.info("command_lst(ExportPage.reset_par) = %s", self.command_lst)
        logger.info(" Not supposed to reset export page")


class ImportPage(QWidget):

    update_command_lst_low_level = Signal(list)

    """
    This stacked widget basically helps the user to browse the input images
    path, there is no auto-generated GUI form Phil parameters in use withing
    this widget.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        main_v_box = QVBoxLayout()

        label_font = QFont()
        sys_font_point_size = label_font.pointSize()
        label_font.setPointSize(sys_font_point_size + 2)
        step_label = QLabel("Import")
        step_label.setFont(label_font)

        self.simple_lin = QLineEdit(self)
        self.simple_lin.textChanged.connect(self.update_command)

        self.start_image = QSpinBox()
        self.start_image.setMinimum(-1)
        self.start_image.setSpecialValueText(" ")
        self.start_image.valueChanged.connect(self.start_image_changed)
        self.end_image = QSpinBox()
        self.end_image.setMinimum(-1)
        self.end_image.setSpecialValueText(" ")
        self.end_image.valueChanged.connect(self.end_image_changed)

        self.x_spn_bx = QSpinBox()
        self.x_spn_bx.setMaximum(99999)
        self.x_spn_bx.setSpecialValueText(" ")
        self.y_spn_bx = QSpinBox()
        self.y_spn_bx.setMaximum(99999)
        self.y_spn_bx.setSpecialValueText(" ")

        self.x_spn_bx.valueChanged.connect(self.x_beam_changed)
        self.y_spn_bx.valueChanged.connect(self.y_beam_changed)

        self.chk_invert = QCheckBox("Invert rotation axis")
        self.chk_invert.stateChanged.connect(self.inv_rota_changed)

        self.opn_fil_btn = QPushButton(" \n Select file(s) \n ")

        main_path = get_main_path()

        self.opn_fil_btn.setIconSize(QSize(80, 48))

        main_v_box.addWidget(step_label)
        main_v_box.addWidget(self.opn_fil_btn)
        main_v_box.addWidget(self.simple_lin)

        self.image_range = [-1, -1]
        self.image_range_label = QLabel("\n\n Image range")
        main_v_box.addWidget(self.image_range_label)
        image_range_hbox = QHBoxLayout()
        self.start_label = QLabel("    Start: ")
        image_range_hbox.addWidget(self.start_label)
        image_range_hbox.addWidget(self.start_image)
        self.end_label = QLabel("    End: ")
        image_range_hbox.addWidget(self.end_label)
        image_range_hbox.addWidget(self.end_image)
        image_range_hbox.addStretch()
        main_v_box.addLayout(image_range_hbox)

        self.b_cetre_label = QLabel("\n Beam centre")
        main_v_box.addWidget(self.b_cetre_label)
        cent_hbox = QHBoxLayout()
        self.x_label = QLabel("    X: ")
        cent_hbox.addWidget(self.x_label)
        cent_hbox.addWidget(self.x_spn_bx)
        self.y_label = QLabel("    Y: ")
        cent_hbox.addWidget(self.y_label)
        cent_hbox.addWidget(self.y_spn_bx)

        cent_hbox.addStretch()
        main_v_box.addLayout(cent_hbox)

        main_v_box.addWidget(self.chk_invert)

        self.reset_button = ResetButton()
        main_v_box.addWidget(self.reset_button)
        self.reset_button.clicked.connect(self.reset_par)

        main_v_box.addStretch()

        self.opn_fil_btn.clicked.connect(self.open_files)

        self.defa_dir = str(os.getcwd())
        self.setLayout(main_v_box)
        # self.show()
        self.reset_par()

    def reset_par(self):
        logger.info("reset_par(ImportPage)")
        self.cmd_list = []
        self.simple_lin.setText("")
        self.start_image.setValue(-1)
        self.end_image.setValue(-1)
        self.x_spn_bx.setValue(0.0)
        self.y_spn_bx.setValue(0.0)
        self.chk_invert.setChecked(False)

        self.image_range = [-1, -1]
        self.x_beam, self.y_beam = 0.0, 0.0
        self.path_file_str = ""
        self.second_half = ""
        self.third_half = ""

    def update_param_w_lst(self, lst_in: List[str]) -> None:
        """
        Refresh the widget with parameters by re-reading a command list.

        Args:
            lst_in: A command list
        """

        self.reset_par()
        logger.info("update_param_w_lst(ImportPage) lst: %s", lst_in)

        input_params = []
        for singl_com in lst_in[1:]:
            if singl_com == "invert_rotation_axis=True":
                self.chk_invert.setChecked(True)
            elif singl_com.startswith("slow_fast_beam_centre="):
                yb_xb_str = singl_com[22:]
                yb_str, xb_str = yb_xb_str.split(",")
                yb = float(yb_str)
                xb = float(xb_str)
                self.y_spn_bx.setValue(yb)
                self.x_spn_bx.setValue(xb)
            elif singl_com.startswith("image_range="):
                image_range_str = singl_com[12:]
                start, end = image_range_str.split(",")
                start = int(start)
                end = int(end)
                self.start_image.setValue(start)
                self.end_image.setValue(end)
            else:
                input_params.append(singl_com)

        self.path_file_str = escaped_join(input_params)
        self.put_str_lin()

    def inv_rota_changed(self):
        if self.chk_invert.checkState():
            self.third_half = "invert_rotation_axis=True"

        else:
            self.third_half = ""

        self.put_str_lin()

    def x_beam_changed(self, value):
        self.x_beam = value
        self.build_second_half()

    def y_beam_changed(self, value):
        self.y_beam = value
        self.build_second_half()

    def start_image_changed(self, value):
        self.image_range[0] = value
        if self.image_range[1] != -1:
            self.build_second_half()

    def end_image_changed(self, value):
        self.image_range[1] = value
        if self.image_range[0] != -1:
            self.build_second_half()

    def build_second_half(self):
        second_half = []
        if self.x_beam != 0.0 and self.y_beam != 0.0:
            second_half.append(
                "slow_fast_beam_centre=" + str(self.y_beam) + "," + str(self.x_beam)
            )
        if all(e > -1 for e in self.image_range) and self.image_range[1] >= self.image_range[0]:

            second_half.append(
                f"image_range={self.image_range[0]},{self.image_range[1]}"
            )
        self.second_half = " ".join(second_half)
        self.put_str_lin()

    def open_files(self):

        lst_file_path, _ = QFileDialog.getOpenFileNames(
            self, "Open File(s)", self.defa_dir, "All Files (*.*)"
        )

        if len(lst_file_path) > 0:
            self.reset_par()
            new_dir, new_command = get_import_run_string(lst_file_path)
            # logger.info(f"\n new_dir= {new_dir} >>")
            # logger.info(f"\n new_command = {new_command} >>")
            self.path_file_str = new_command
            self.defa_dir = new_dir
            self.put_str_lin()

    def put_str_lin(self):
        print(f"self.path_file_str = {self.path_file_str} >>")
        if not self.path_file_str:
            self.simple_lin.setText("")
        self.cmd_list = [
            self.path_file_str,
            self.second_half.lstrip(),
            self.third_half.lstrip(),
        ]
        txt_lin = " ".join(self.cmd_list).rstrip()
        while "  " in txt_lin:
            txt_lin = txt_lin.replace("  ", " ")

        self.simple_lin.setText(txt_lin)

    def set_arg_obj(self, sys_arg_in):
        """Pass the system argument object to handle launch arguments."""
        if sys_arg_in.template is not None:
            str_arg = str(sys_arg_in.template)
            self.simple_lin.setText(str_arg)

    def update_command(self):
        """Update self.command_lst from the Text widget contents"""
        command = ["import"] + shlex.split(self.simple_lin.text())

        self.command_lst = [command]
        self.update_command_lst_low_level.emit(command)

    def gray_me_out(self):
        self.simple_lin.setEnabled(False)
        self.opn_fil_btn.setEnabled(False)
        self.x_spn_bx.setEnabled(False)
        self.y_spn_bx.setEnabled(False)
        self.x_label.setEnabled(False)
        self.y_label.setEnabled(False)
        self.b_cetre_label.setEnabled(False)
        self.chk_invert.setEnabled(False)

    def activate_me(self, cur_nod=None):
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
        super().__init__(parent)

        self.scrollable_widget = PhilWidget(phl_obj, parent=self)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        vbox = QVBoxLayout()

        search_label = QLabel("Search:")
        search_edit = QLineEdit()
        search_edit.setPlaceholderText("Type search here")
        search_edit.textChanged.connect(self.scrollable_widget.user_searching)
        self.search_next_button = QPushButton("Find next")
        self.search_next_button.setEnabled(False)

        hbox = QHBoxLayout()
        hbox.addWidget(search_label)
        hbox.addWidget(search_edit)
        hbox.addWidget(self.search_next_button)
        self.search_next_button.clicked.connect(self.scrollable_widget.find_next)
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
        pair = string2pair(par_str)
        lst_pair.append(pair)

    return lst_pair


class ParamMainWidget(QWidget):

    update_command_lst_low_level = Signal(list)

    def __init__(self, phl_obj=None, simp_widg=None, parent=None, upper_label=None):
        super().__init__(parent)

        self.command_lst = [[None]]
        self.lst_pair = []

        try:
            self.my_phl_obj = phl_obj
            self.simp_widg_in = simp_widg

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.info("Caught unknown exception %s: %s", type(e).__name__, e)
            logger.info("\n\n\n something went wrong here wiht the phil object \n\n\n")

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
            logger.info("Caught unknown exception %s: %s", type(e).__name__, e)
            logger.info("found self.simpler_widget without << item_changed >> signal")

        try:
            self.simpler_widget.item_to_remove.connect(self.remove_one_par)

        except AttributeError:
            pass

        self.reset_btn = self.simpler_widget.inner_reset_btn
        self.dual_level_tab.addTab(self.simpler_widget, "Simple")
        self.dual_level_tab.addTab(self.advanced_widget, "Advanced")
        self.reset_btn.clicked.connect(self.reset_par)

    def reset_par(self):

        for i in reversed(list(range(self._vbox.count()))):
            widgetToRemove = self._vbox.itemAt(i).widget()
            self._vbox.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)

        self.build_param_widget()

        self._vbox.addWidget(self.step_label)
        self._vbox.addWidget(self.dual_level_tab)

        self.command_lst[0] = [self.command_lst[0][0]]
        self.lst_pair = []

        self.update_command_lst_low_level.emit(self.command_lst[0])

        try:
            max_nproc = self.simpler_widget.set_max_nproc()
            if max_nproc > 1:
                self.raise_nproc_str = (
                    str(self.simpler_widget.box_nproc.local_path) + "=" + str(max_nproc)
                )
                QTimer.singleShot(1000, self.raise_nproc_to_max)

        except AttributeError:
            pass

    def raise_nproc_to_max(self):
        found_nproc = False
        for single_par in self.command_lst[0]:
            if "mp.nproc" in single_par:
                found_nproc = True

        if not found_nproc:
            self.command_lst[0].append(self.raise_nproc_str)
            self.update_command_lst_low_level.emit(self.command_lst[0])

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

                            except BaseException:
                                try:
                                    str_val = str(str_value)
                                    widg.setText(str_val)
                                    logger.debug(
                                        "widg.local_path = %s", widg.local_path
                                    )

                                except BaseException as ee:
                                    logger.info("ee = %s", ee)

                        else:
                            for pos, val in enumerate(widg.tmp_lst):
                                if val == str_value:
                                    try:
                                        widg.setCurrentIndex(pos)
                                    except BaseException as e:
                                        # We don't want to catch bare exceptions but
                                        # dont know what this was supposed to catch.
                                        logger.info(
                                            "Caught unknown exception #5 type: %s", e
                                        )
                                        logger.info("failed to:")
                                        logger.info("widg.setCurrentIndex(pos)")

                except AttributeError:
                    pass

    def update_simpler_widget(self, str_path, str_value):
        for widg in self.simpler_widget.lst_var_widg:
            try:
                if widg.local_path == str_path:
                    logger.debug("found << widg.local_path == str_path >> ")
                    try:
                        num_val = float(str_value)
                        widg.setValue(num_val)

                    except ValueError:
                        for pos, val in enumerate(widg.tmp_lst):
                            if val == str_value:
                                logger.info("found val v= %s", val)
                                widg.setCurrentIndex(pos)

            except AttributeError:
                pass

    def update_lin_txt(self, str_path, str_value):
        # cmd_to_run = str_path + "=" + str_value
        self.update_advanced_widget(str_path, str_value)
        self.update_simpler_widget(str_path, str_value)

        self.lst_pair = update_lst_pair(self.lst_pair, str_path, str_value)
        self.command_lst[0] = build_lst_str(self.command_lst[0][0], self.lst_pair)
        self.update_command_lst_low_level.emit(self.command_lst[0])

    def update_param_w_lst(self, lst_in, do_reset=True):

        if do_reset:
            self.reset_par()

        if len(lst_in) > 1:
            self.lst_pair = buils_lst_pair(lst_in)
            self.command_lst[0] = build_lst_str(lst_in[0], self.lst_pair)
            for pair in self.lst_pair:
                self.update_advanced_widget(pair[0], pair[1])

        else:
            self.lst_pair = []
            self.command_lst[0] = lst_in

    def remove_one_par(self, path_str):
        nxt_lst = []
        for single_param in self.command_lst[0]:
            if str(path_str) in single_param:
                pass

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
                    logger.info(
                        "Caught unknown exception #9 type %s: %s", type(e).__name__, e
                    )
                    pass

    def activate_me(self, cur_nod=None):
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

                except AttributeError:
                    pass

                try:
                    widg.setEnabled(True)

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.info(
                        "Caught unknown exception #11 type %s: %s", type(e).__name__, e
                    )


class ParamWidget(QWidget):

    update_command_lst_medium_level = Signal(list)

    def __init__(self, label_str):
        super().__init__()
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

        self.my_widget.command_lst = [[label_str]]

        self.my_widget.update_command_lst_low_level.connect(self.update_parent_lst)

        v_left_box = QVBoxLayout()
        v_left_box.addWidget(self.my_widget)
        self.setLayout(v_left_box)

        # comment next line to avoid ugly pops at launch
        # self.show()

    def update_param(self, curr_step):
        self.my_widget.update_param_w_lst(curr_step.ll_command_lst[0])

    def update_parent_lst(self, command_lst):
        self.update_command_lst_medium_level.emit(command_lst)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # ex = ParamWidget("import")
    # ex = ParamWidget("find_spots")
    # ex = ParamWidget("index")
    # ex = ParamWidget("refine")
    # ex = ParamWidget("integrate")
    # ex = ParamWidget("symmetry")
    ex = ParamWidget("scale")  # someting hapen with the Advanced parameters
    # ex = ParamWidget("export")

    ex.show()

    sys.exit(app.exec_())
