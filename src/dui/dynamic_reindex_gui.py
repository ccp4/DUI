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
import re
from pathlib import Path
from typing import List

from dui.cli_utils import sys_arg
from dui.qt import (
    QApplication,
    QColor,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSize,
    QSizePolicy,
    QStyle,
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


def _calculate_table_size(table: QTableWidget, maximum_rows: int = 10) -> QSize:
    """Calculate the fixed size to show a whole table, up to a maximum row count"""
    calculated_width = (
        table.horizontalHeader().length() + table.verticalHeader().width()
    )
    # If more than the maximum rows, we need to account for a scrollbar
    if table.rowCount() > maximum_rows:
        calculated_width += (
            QApplication.instance().style().pixelMetric(QStyle.PM_ScrollBarExtent)
        )
    calculated_height = (
        min(
            table.rowHeight(0) * maximum_rows + table.horizontalHeader().height(),
            table.verticalHeader().length() + table.horizontalHeader().height(),
        )
        + 2
    )
    return QSize(calculated_width, calculated_height)


def ops_list_from_json(json_path: Path) -> List:
    """Extract a summary of bravais settings solutions from a summary file"""
    if json_path is None:
        return None

    json_data = json.loads(json_path.read_text())

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


def extract_chiral_header(node_id: int, json_summary_file: Path) -> str:
    """
    Extract the symmetry header text for the reindex table

    Args:
        node_id: The node number of the refine_bravais_settings step
        json_summary_file: The path to the json summary file

    Returns:
        The symmetry header text
    """

    bravais_logfile = (
        json_summary_file.parent / f"{node_id}_refine_bravais_settings.log"
    )
    logger.debug("refine_bravais_settings logfile: %s", bravais_logfile)
    if not bravais_logfile.is_file():
        logger.error("Could not find bravais settings logfile: %s", bravais_logfile)
        return ""

    match = re.search(
        r"(Chiral space groups(?:.|\n)*?)\n.*?---",
        bravais_logfile.read_text(),
        re.MULTILINE,
    )
    if not match:
        logger.error("Could not read summary from bravais log %s", bravais_logfile)
        return ""

    return match.group(1)


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

    def load_data(self, json_path: Path = None):

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

        if self.solution is not None:
            self.selectRow(self.solution - 1)


class MyReindexOpts(QDialog):
    def __init__(
        self, parent, summary_json: str, bravais_node_id: int, show_cancel: bool = False
    ):
        """
        Create a reindex dialog.

        Args:
            parent: The parent window for the dialog
            summary_json: Name of the summary.json for a step
            bravais_node_id:
                The node number of the refine_bravais_settings step.
                Used to locate the log file for the symmetry header.
            show_cancel: Show a cancel button on the dialog
        """
        super().__init__(parent)
        self.setWindowTitle("Re-index to solution")
        self.solution = None
        self.show_cancel = show_cancel

        json_path = Path(sys_arg.directory) / "dui_files" / summary_json
        header_text = extract_chiral_header(bravais_node_id, json_path)

        self.table = ReindexTable(self)
        self.table.doubleClicked.connect(self.accept)
        self.table.load_data(json_path)

        recomd_str = "Select a bravais lattice to enforce\n"
        if self.table.recommended_solution:
            recomd_str += (
                f"(best guess solution = row {self.table.recommended_solution})"
            )
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
        vbox.addWidget(self.table)
        vbox.addLayout(bot_box)
        self.setLayout(vbox)

        # Attempt to set table to exact size required
        self.table.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.resizeColumnsToContents()
        self.table.setFixedSize(_calculate_table_size(self.table))

    def accept(self):
        """The user confirmed selection of an item."""
        self.solution = self.table.solution
        logger.debug("Selected solution %s", self.solution)
        super().accept()
