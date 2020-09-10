"""
Reindex table popup GUI

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
from typing import List

from dui.cli_utils import sys_arg
from dui.qt import (
    QColor,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    Qt,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

logger = logging.getLogger(__name__)


def choice_if_decimal(num_in: float) -> str:
    """Remove the decimal places if zero"""

    str_f = f"{num_in:6.2f}"
    if str_f[-3:] == ".00":
        str_out = str_f[0:-3]
    else:
        str_out = str_f

    return str_out


def ops_list_from_json(json_path: str) -> List:
    """Extract a summary of bravais settings solutions from a summary file"""
    if json_path is None:
        return None

    with open(json_path) as json_file:
        json_data = json.load(json_file)

    operations = []

    for index, solution in json_data.items():
        angular_diff = f" {solution['max_angular_difference']:7.2}"
        rmsd = f" {solution['rmsd']:7.2}"
        bravais = f" {solution['bravais']:<3}"
        recommended = " Y" if solution["recommended"] else " N"

        edges, angles = solution["unit_cell"][:3], solution["unit_cell"][-3:]
        unit_cell_edges = [f"{edge:6.1f}" for edge in edges]
        unit_cell_angles = [choice_if_decimal(angle) for angle in angles]

        if solution["min_cc"] is not None:
            min_cc = f" {solution['min_cc']:7.2}"
        else:
            min_cc = "    - "
        if solution["max_cc"] is not None:
            max_cc = f" {solution['max_cc']:7.2}"
        else:
            max_cc = "    - "

        operations.append(
            [
                int(index),
                angular_diff,
                rmsd,
                min_cc,
                max_cc,
                bravais,
                *unit_cell_edges,
                *unit_cell_angles,
                recommended,
            ]
        )

    return sorted(operations)


def header_text_from_node(lin_num: int, j_path: str) -> str:
    """
    Extract the symmetry header text for the reindex table

    Args:
        lin_num: The node number of the refine_bravais_settings step
        j_path: The path to the json summary file

    Returns:
        The symmetry header text
    """

    dir_path_end = j_path.find("lin_")
    dir_path = j_path[0:dir_path_end]
    lin_num_str = str(lin_num)
    my_file_path = dir_path + lin_num_str + "_refine_bravais_settings.log"

    logger.debug("my_file_path: %s", my_file_path)

    myfile = open(my_file_path)
    all_lines = myfile.readlines()
    myfile.close()

    logger.debug("len(all_lines): %s", len(all_lines))

    multi_lin_txt = ""
    for pos1, single_lin1 in enumerate(all_lines):
        logger.debug("pos1, single_lin1: %s, %s", pos1, single_lin1)
        # if str(single_lin1[0:19]) == "Chiral space groups":
        if "Chiral space groups" in single_lin1:

            start_block = pos1
            logger.debug("start_block = %s", start_block)

            for pos2, single_lin2 in enumerate(all_lines[start_block:]):
                if "----" in single_lin2:
                    end_block = pos2 + start_block
                    logger.debug("end_block = %s", end_block)
                    break

            break

    logger.debug("start_block, end_block = %s %s", start_block, end_block)

    for single_lin in all_lines[start_block:end_block]:
        multi_lin_txt += single_lin

    return multi_lin_txt


class ReindexTable(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.solution = None
        self.recommended_solution = None

        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setAlternatingRowColors(True)

    def selectionChanged(self, selected, deselected):
        """Handle updating the selected solution"""
        super().selectionChanged(selected, deselected)
        rows = self.selectionModel().selectedRows()
        if rows:
            assert len(rows) == 1
            self.solution = rows[0].row() + 1
            logger.info("Updating solution to %s", self.solution)
        else:
            if not deselected:
                self.selectRow(0)
            else:
                # We don't want to allow this. Reselect
                logger.info(deselected.indexes()[0].row())
                self.selectRow(deselected.indexes()[0].row())
        assert len(rows) <= 1

    def find_best_solu(self):
        bst_sol = -1
        for row, row_cont in enumerate(self.list_labl):
            if row_cont[self.rec_col] == " Y":
                if row > bst_sol:
                    bst_sol = row

        logger.debug("bst_sol =  %s", bst_sol)

        return bst_sol

    def load_data(self, json_path=None):

        logger.debug("json_path = %s", json_path)

        data = ops_list_from_json(json_path)

        logger.debug("n_row = %s", len(data))
        logger.debug("n_col = %s", len(data[0]))

        self.setRowCount(len(data))
        # Don't count the solution number
        self.setColumnCount(len(data[0]) - 1)

        self.setHorizontalHeaderLabels(
            [
                "max δ",
                "rmsd",
                " min cc",
                "max cc",
                "latt",
                "a",
                "b",
                "c",
                "α",
                "β",
                "γ",
                "Ok",
            ]
        )

        last_recommendation = None
        for row, row_cont in enumerate(data):
            for col, col_value in enumerate(row_cont[1:]):
                item = QTableWidgetItem(col_value)
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                # TODO: Do we need monospace font here again? Just numbers though...
                # item.setFont(QFont("Monospace", self.sys_font_point_size))
                if col_value == " Y":
                    item.setBackground(QColor(Qt.green).lighter())
                    item.setFlags(Qt.ItemIsEnabled)
                    last_recommendation = row + 1
                elif col_value == " N":
                    item.setBackground(QColor(Qt.red).lighter())
                    item.setFlags(Qt.ItemIsEnabled)

                self.setItem(row, col, item)

        self.resizeColumnsToContents()

        self.recommended_solution = last_recommendation

        # If no solution given, default to the last recommendation
        if self.solution is None:
            self.solution = last_recommendation

        print("Solution", self.solution)
        if self.solution is not None:
            self.selectRow(self.solution - 1)


class MyReindexOpts(QDialog):
    def __init__(
        self, parent, summary_json: str, node_id: int, show_cancel: bool = False
    ):
        """
        Create a reindex dialog.

        Args:
            parent: The parent window for the dialog
            summary_json: Name of the summary.json for a step
            node_id:
                The node number of the refine_bravais_settings step.
                Used to locate the log file for the symmetry header.
            show_cancel: Show a cancel button on the dialog
        """
        super().__init__(parent)
        self.setWindowTitle("Reindex")
        self.solution = None
        self.show_cancel = show_cancel
        self._set_ref(summary_json, node_id)

    def _set_ref(self, in_json_path: str, lin_num: int):
        """
        Set the reference data for the settings table.

        Args:
            in_json_path: Name of the summary.json file for the bravais step
            lin_num: The node number of the refine_bravais_settings step
        """
        cwd_path = os.path.join(sys_arg.directory, "dui_files")
        full_json_path = os.path.join(cwd_path, in_json_path)

        header_text = header_text_from_node(lin_num, full_json_path)

        self.my_inner_table = ReindexTable(self)
        self.my_inner_table.doubleClicked.connect(self.accept)
        self.my_inner_table.load_data(full_json_path)

        recomd_str = "Select a bravais lattice to enforce\n"
        if self.my_inner_table.recommended_solution:
            recomd_str += f"(best guess solution = row {self.my_inner_table.recommended_solution})"
        else:
            recomd_str += "(no best solution could be automatically determined)"

        bot_box = QHBoxLayout()
        bot_box.addWidget(QLabel(recomd_str))
        bot_box.addStretch()
        if self.show_cancel:
            cancel_button = QPushButton("Cancel")
            cancel_button.clicked.connect(self.reject)
            bot_box.addWidget(cancel_button)
        ok_but = QPushButton("OK")
        ok_but.clicked.connect(self.accept)
        ok_but.setDefault(True)
        bot_box.addWidget(ok_but)

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel(header_text))
        vbox.addWidget(self.my_inner_table)
        vbox.addLayout(bot_box)
        self.setLayout(vbox)

        # Attempt to set table to exact size required
        self.my_inner_table.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.my_inner_table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.my_inner_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.my_inner_table.resizeColumnsToContents()
        self.my_inner_table.setFixedSize(
            self.my_inner_table.horizontalHeader().length()
            + self.my_inner_table.verticalHeader().width(),
            min(
                self.my_inner_table.rowHeight(0) * 10
                + self.my_inner_table.horizontalHeader().height(),
                self.my_inner_table.verticalHeader().length()
                + self.my_inner_table.horizontalHeader().height(),
            )
            + 2,
        )

    def accept(self):
        """The user confirmed selection of an item."""
        self.solution = self.my_inner_table.solution
        logger.debug("Selected solution %s", self.solution)
        super().accept()
