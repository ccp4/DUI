"""
DUI's command simple stacked widgets

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
import sys

import libtbx.introspection

from dui.qt import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QRegExp,
    QRegExpValidator,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    Signal,
)

logger = logging.getLogger(__name__)


def _get_all_direct_layout_widget_children(parent):
    """Walk a widget tree and get all non-QLayout direct children

    Args:
        parent(QLayout): The layout to walk

    Returns:
        (List[QWidget]): Any widgets directly attached to layouts in this
    """
    children = []
    if isinstance(parent, QLayout):
        for child in [parent.itemAt(i) for i in range(parent.count())]:
            children.extend(_get_all_direct_layout_widget_children(child))

    elif hasattr(parent, "widget"):
        if parent.widget():
            children.append(parent.widget())

    return children


class ResetButton(QPushButton):
    """QPushButton with default text."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("Reset to default")


class DefaultComboBox(QComboBox):
    """A ComboBox initialised with a list of items and keeps track of which one
    is default"""

    def __init__(self, local_path, items, default_index=0):
        super().__init__()
        self.local_path = local_path
        self.tmp_lst = items
        self.default_index = default_index
        for item in items:
            self.addItem(item)

        self.setCurrentIndex(self.default_index)


class SimpleParamTab(QWidget):
    """Base class shared by all simple parameter tabs"""

    item_changed = Signal(str, str)
    item_to_remove = Signal(str)

    def spnbox_finished(self):
        sender = self.sender()
        value = sender.value()
        str_path = str(sender.local_path)
        if sender.specialValueText() and value == sender.minimum():
            self.item_to_remove.emit(str_path)
        else:
            str_value = str(value)
            self.item_changed.emit(str_path, str_value)

    def combobox_changed(self, value):

        sender = self.sender()
        str_value = str(sender.tmp_lst[value])
        str_path = str(sender.local_path)

        if sender.currentIndex() == sender.default_index:
            self.item_to_remove.emit(str_path)
        else:
            self.item_changed.emit(str_path, str_value)


class FindspotsSimplerParameterTab(SimpleParamTab):
    """
    This widget is the tool for tunning the simpler and most common parameters
    in the spot-finder, this widget is the first to appear once the button
    "Find Sots" at the left side of the GUI is clicked
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.param_widget_parent = parent.param_widget_parent
        # TODO thinks about making "None equivalent to 1"
        xds_gain_label = QLabel("Gain")
        xds_gain_spn_bx = QDoubleSpinBox()
        xds_gain_spn_bx.local_path = "spotfinder.threshold.dispersion.gain"
        xds_gain_spn_bx.setSpecialValueText("None")
        xds_gain_spn_bx.setValue(1.0)
        xds_gain_spn_bx.editingFinished.connect(self.spnbox_finished)

        xds_sigma_background_label = QLabel("Sigma background")
        xds_sigma_background_spn_bx = QDoubleSpinBox()
        xds_sigma_background_spn_bx.setValue(6.0)
        xds_sigma_background_spn_bx.local_path = (
            "spotfinder.threshold.dispersion.sigma_background"
        )
        xds_sigma_background_spn_bx.editingFinished.connect(self.spnbox_finished)

        xds_sigma_strong_label = QLabel("Sigma strong")
        xds_sigma_strong_spn_bx = QDoubleSpinBox()
        xds_sigma_strong_spn_bx.setValue(3.0)
        xds_sigma_strong_spn_bx.local_path = (
            "spotfinder.threshold.dispersion.sigma_strong"
        )
        xds_sigma_strong_spn_bx.editingFinished.connect(self.spnbox_finished)

        xds_global_threshold_label = QLabel("Global threshold")
        xds_global_threshold_spn_bx = QDoubleSpinBox()
        xds_global_threshold_spn_bx.setMaximum(9999.99)
        xds_global_threshold_spn_bx.local_path = (
            "spotfinder.threshold.dispersion.global_threshold"
        )
        xds_global_threshold_spn_bx.editingFinished.connect(self.spnbox_finished)

        localLayout = QVBoxLayout()

        xds_gain_hb = QHBoxLayout()
        xds_gain_hb.addWidget(xds_gain_label)
        xds_gain_hb.addWidget(xds_gain_spn_bx)
        localLayout.addLayout(xds_gain_hb)

        xds_sigma_background_hb = QHBoxLayout()
        xds_sigma_background_hb.addWidget(xds_sigma_background_label)
        xds_sigma_background_hb.addWidget(xds_sigma_background_spn_bx)
        localLayout.addLayout(xds_sigma_background_hb)

        xds_sigma_strong_hb = QHBoxLayout()
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_label)
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_spn_bx)
        localLayout.addLayout(xds_sigma_strong_hb)

        xds_global_threshold_hb = QHBoxLayout()
        xds_global_threshold_hb.addWidget(xds_global_threshold_label)
        xds_global_threshold_hb.addWidget(xds_global_threshold_spn_bx)
        localLayout.addLayout(xds_global_threshold_hb)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = _get_all_direct_layout_widget_children(localLayout)


class IndexSimplerParamTab(SimpleParamTab):
    """
    This widget is the tool for tunning the simpler and most common parameters
    in the indexer, this widget is the first to appear once the button
    "Index" at the left side of the GUI is clicked
    """

    def __init__(self, phl_obj=None, parent=None):
        super().__init__(parent)

        # self.param_widget_parent = parent.param_widget_parent
        # indexing_method_check = QCheckBox("indexing.method")

        hbox_method = QHBoxLayout()
        label_method_62 = QLabel("Indexing method")
        hbox_method.addWidget(label_method_62)
        box_method_62 = DefaultComboBox(
            "indexing.method",
            ["fft3d", "fft1d", "real_space_grid_search", "low_res_spot_match"],
        )
        box_method_62.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(box_method_62)

        max_cell_label = QLabel("Max cell")
        max_cell_spn_bx = QDoubleSpinBox()
        max_cell_spn_bx.setSingleStep(5.0)
        max_cell_spn_bx.local_path = "indexing.max_cell"
        max_cell_spn_bx.setSpecialValueText("Auto")
        max_cell_spn_bx.editingFinished.connect(self.spnbox_finished)

        space_group_label = QLabel("Space group")
        space_group_line = QLineEdit()
        # Simple validator to allow only characters in H-M symbols
        regex = QRegExp(r"[ABCPIFR][0-9a-d\-/:nmHR]+")
        validatorHM = QRegExpValidator(regex)
        space_group_line.setValidator(validatorHM)
        space_group_line.local_path = "indexing.known_symmetry.space_group"
        space_group_line.editingFinished.connect(self.line_changed)

        unit_cell_label = QLabel("Unit cell")
        unit_cell_line = QLineEdit()
        regex = QRegExp(r"[0-9\., ]+")
        validatorUC = QRegExpValidator(regex)
        unit_cell_line.setValidator(validatorUC)
        unit_cell_line.local_path = "indexing.known_symmetry.unit_cell"
        unit_cell_line.editingFinished.connect(self.line_changed)

        localLayout = QVBoxLayout()

        localLayout.addLayout(hbox_method)

        qf = QFormLayout()
        qf.addRow(max_cell_label, max_cell_spn_bx)
        qf.addRow(space_group_label, space_group_line)
        qf.addRow(unit_cell_label, unit_cell_line)
        localLayout.addLayout(qf)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = _get_all_direct_layout_widget_children(localLayout)

    def line_changed(self):
        sender = self.sender()
        str_value = sender.text()
        str_path = str(sender.local_path)

        self.item_changed.emit(str_path, str_value)


# >>>>>>> old master
# class RefineBravaiSimplerParamTab(QWidget):


class RefineBravaiSimplerParamTab(SimpleParamTab):
    def __init__(self, parent=None):
        super().__init__(parent)

        localLayout = QVBoxLayout()
        hbox_lay_outlier_algorithm = QHBoxLayout()
        label_outlier_algorithm = QLabel("Outlier rejection algorithm")

        hbox_lay_outlier_algorithm.addWidget(label_outlier_algorithm)
        box_outlier_algorithm = DefaultComboBox(
            "refinement.reflections.outlier.algorithm",
            ["null", "Auto", "mcd", "tukey", "sauter_poon"],
            default_index=1,
        )
        box_outlier_algorithm.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_outlier_algorithm.addWidget(box_outlier_algorithm)
        localLayout.addLayout(hbox_lay_outlier_algorithm)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = []
        self.lst_var_widg.append(box_outlier_algorithm)
        self.lst_var_widg.append(label_outlier_algorithm)


class RefineSimplerParamTab(SimpleParamTab):
    """
    This widget is the tool for tunning the simpler and most common parameters
    in the refiner, this widget is the first to appear once the button
    "Refine" at the left side of the GUI is clicked
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.param_widget_parent = parent.param_widget_parent
        localLayout = QVBoxLayout()

        hbox_lay_scan_varying = QHBoxLayout()

        label_scan_varying = QLabel("Scan varying refinement")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = DefaultComboBox(
            "refinement.parameterisation.scan_varying",
            ["True", "False", "Auto"],
            default_index=2,
        )
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)
        localLayout.addLayout(hbox_lay_scan_varying)

        ###########################################################################

        hbox_lay_outlier_algorithm = QHBoxLayout()
        label_outlier_algorithm = QLabel("Outlier rejection algorithm")

        hbox_lay_outlier_algorithm.addWidget(label_outlier_algorithm)
        box_outlier_algorithm = DefaultComboBox(
            "refinement.reflections.outlier.algorithm",
            ["null", "Auto", "mcd", "tukey", "sauter_poon"],
            default_index=1,
        )
        box_outlier_algorithm.currentIndexChanged.connect(self.combobox_changed)

        hbox_lay_outlier_algorithm.addWidget(box_outlier_algorithm)
        localLayout.addLayout(hbox_lay_outlier_algorithm)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = []
        self.lst_var_widg.append(box_scan_varying)
        self.lst_var_widg.append(label_scan_varying)

        # self.lst_var_widg.append(box_beam_fix)
        # self.lst_var_widg.append(label_beam_fix)

        # self.lst_var_widg.append(box_crystal_fix)
        # self.lst_var_widg.append(label_crystal_fix)

        # self.lst_var_widg.append(box_detector_fix)
        # self.lst_var_widg.append(label_detector_fix)

        # self.lst_var_widg.append(box_goniometer_fix)
        # self.lst_var_widg.append(label_goniometer_fix)

        self.lst_var_widg.append(box_outlier_algorithm)
        self.lst_var_widg.append(label_outlier_algorithm)


class IntegrateSimplerParamTab(SimpleParamTab):
    """
    This widget is the tool for tunning the simpler and most common parameters
    in the integrate algorithm, this widget is the first to appear once the button
    "Integrate" at the left side of the GUI is clicked
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.param_widget_parent = parent.param_widget_parent

        localLayout = QVBoxLayout()
        PrFit_lay_out = QHBoxLayout()
        label_PrFit = QLabel("Use profile fitting")
        PrFit_lay_out.addWidget(label_PrFit)

        PrFit_comb_bx = DefaultComboBox(
            "integration.profile.fitting", ["True", "False", "Auto"]
        )
        PrFit_comb_bx.currentIndexChanged.connect(self.combobox_changed)

        PrFit_lay_out.addWidget(PrFit_comb_bx)
        localLayout.addLayout(PrFit_lay_out)

        hbox_lay_algorithm_53 = QHBoxLayout()
        label_algorithm_53 = QLabel("Background algorithm")
        hbox_lay_algorithm_53.addWidget(label_algorithm_53)

        box_algorithm_53 = DefaultComboBox(
            "integration.background.algorithm",
            ["simple", "null", "median", "gmodel", "glm"],
            default_index=4,
        )
        box_algorithm_53.currentIndexChanged.connect(self.combobox_changed)

        hbox_lay_algorithm_53.addWidget(box_algorithm_53)
        localLayout.addLayout(hbox_lay_algorithm_53)

        hbox_d_min = QHBoxLayout()
        label_d_min = QLabel("High resolution limit")
        hbox_d_min.addWidget(label_d_min)
        d_min_spn_bx = QDoubleSpinBox()
        d_min_spn_bx.local_path = "prediction.d_min"
        d_min_spn_bx.setSpecialValueText("None")
        d_min_spn_bx.setValue(0.0)
        hbox_d_min.addWidget(d_min_spn_bx)
        d_min_spn_bx.editingFinished.connect(self.spnbox_finished)
        localLayout.addLayout(hbox_d_min)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = _get_all_direct_layout_widget_children(localLayout)



class SymmetrySimplerParamTab(SimpleParamTab):
    """
    This widget is the tool for tunning the simpler and most common parameters
    in the symmetry command, this widget is the first to appear once the button
    "Symmetry" at the left side of the GUI is clicked
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        hbox_d_min = QHBoxLayout()
        localLayout = QVBoxLayout()
        label_d_min = QLabel("High resolution limit")

        hbox_d_min.addWidget(label_d_min)

        d_min_spn_bx = QDoubleSpinBox()
        d_min_spn_bx.local_path = "d_min"
        d_min_spn_bx.setSpecialValueText("Auto")
        d_min_spn_bx.setValue(0.0)
        hbox_d_min.addWidget(d_min_spn_bx)

        d_min_spn_bx.editingFinished.connect(self.spnbox_finished)

        localLayout.addLayout(hbox_d_min)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = []
        self.lst_var_widg.append(d_min_spn_bx)
        self.lst_var_widg.append(label_d_min)


class ScaleSimplerParamTab(SimpleParamTab):

    """
    This widget is the tool for tunning the simpler and most common parameters
    in the scale command, this widget is the first to appear once the button
    "Scale" at the left side of the GUI is clicked
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        localLayout = QVBoxLayout()

        hbox_lay_mod = QHBoxLayout()
        label_mod = QLabel("Model")

        hbox_lay_mod.addWidget(label_mod)
        box_mod = DefaultComboBox("model", ["physical", "array", "KB"])
        box_mod.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_mod.addWidget(box_mod)

        hbox_lay_wgh_opt_err = QHBoxLayout()
        label_wgh_opt_err = QLabel("Error optimisation model")

        hbox_lay_wgh_opt_err.addWidget(label_wgh_opt_err)
        box_wgh_opt_err = DefaultComboBox(
            "weighting.error_model.error_model", ["basic", "None"]
        )
        box_wgh_opt_err.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_wgh_opt_err.addWidget(box_wgh_opt_err)
        """
        weighting {
          error_model {
            error_model = *basic None
        """

        hbox_d_min = QHBoxLayout()
        d_min_label = QLabel("High resolution limit")
        d_min_spn_bx = QDoubleSpinBox()
        d_min_spn_bx.local_path = "cut_data.d_min"
        d_min_spn_bx.setSpecialValueText("None")
        d_min_spn_bx.setValue(0.0)
        hbox_d_min.addWidget(d_min_label)
        hbox_d_min.addWidget(d_min_spn_bx)

        d_min_spn_bx.editingFinished.connect(self.spnbox_finished)

        localLayout.addLayout(hbox_lay_mod)
        localLayout.addLayout(hbox_lay_wgh_opt_err)
        localLayout.addLayout(hbox_d_min)

        self.inner_reset_btn = ResetButton()
        localLayout.addWidget(self.inner_reset_btn)
        localLayout.addStretch()

        self.setLayout(localLayout)

        self.lst_var_widg = []
        self.lst_var_widg.append(box_mod)
        self.lst_var_widg.append(label_mod)
        self.lst_var_widg.append(box_wgh_opt_err)
        self.lst_var_widg.append(label_wgh_opt_err)
        self.lst_var_widg.append(d_min_spn_bx)
        self.lst_var_widg.append(d_min_label)


class TmpTstWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.param_widget_parent = self

        my_widget = RefineSimplerParamTab(self)
        # my_widget = FindspotsSimplerParameterTab(self)
        # my_widget = SymmetrySimplerParamTab(self)
        # my_widget = ScaleSimplerParamTab(self)

        my_box = QVBoxLayout()
        my_box.addWidget(my_widget)
        self.setLayout(my_box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TmpTstWidget()
    ex.show()
    sys.exit(app.exec_())
