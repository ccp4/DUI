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
from typing import List, Tuple

from dui.cli_utils import sys_arg
from dui.qt import (
    QColor,
    QDialog,
    QFont,
    QHBoxLayout,
    QLabel,
    QPushButton,
    Qt,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    Signal,
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


def header_text_from_node(lin_num: int, j_path: str) -> Tuple[str, int]:
    """
    Extract the symmetry header text for the reindex table

    Args:
        lin_num: The node number of the refine_bravais_settings step
        j_path: The path to the json summary file

    Returns:
        Tuple containing:
            header: The symmetry header text
            num_lines: The number of lines in this header text
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
    n_of_lines = 0
    for pos1, single_lin1 in enumerate(all_lines):
        logger.debug("pos1, single_lin1: %s, %s", pos1, single_lin1)
        # if str(single_lin1[0:19]) == "Chiral space groups":
        if "Chiral space groups" in single_lin1:

            start_block = pos1
            logger.debug("start_block = %s", start_block)

            for pos2, single_lin2 in enumerate(all_lines[start_block:]):
                n_of_lines += 1
                if "----" in single_lin2:
                    end_block = pos2 + start_block
                    logger.debug("end_block = %s", end_block)
                    break

            break

    logger.debug("start_block, end_block = %s %s", start_block, end_block)

    for single_lin in all_lines[start_block:end_block]:
        multi_lin_txt += single_lin

    return multi_lin_txt, n_of_lines


class ReindexTable(QTableWidget):
    opt_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cellClicked.connect(self.opt_clicked)

        self.v_sliderBar = self.verticalScrollBar()
        self.h_sliderBar = self.horizontalScrollBar()

        self.tmp_sel = None

        sys_font = QFont()
        self.sys_font_point_size = sys_font.pointSize()
        # self.show()

    def opt_clicked(self, row, col):
        logger.info("Solution clicked = %s", row + 1)
        # p_h_svar = self.horizontalScrollBar().value()
        # p_v_svar = self.verticalScrollBar().value()

        v_sliderValue = self.v_sliderBar.value()
        h_sliderValue = self.h_sliderBar.value()

        self.del_opts_lst()
        self.add_opts_lst(lst_labels=self.list_labl, selected_pos=row)

        self.v_sliderBar.setValue(v_sliderValue)
        self.h_sliderBar.setValue(h_sliderValue)

        self.opt_pick(row)

    def ok_clicked(self):
        self.opt_pick(self.tmp_sel)

    def opt_pick(self, row):

        if self.tmp_sel == row:
            logger.debug("\n selecting opt: %s %s", row + 1, "\n")
            self.opt_signal.emit(row)

        self.tmp_sel = row

    def find_best_solu(self):
        bst_sol = -1
        for row, row_cont in enumerate(self.list_labl):
            if row_cont[self.rec_col] == " Y":
                if row > bst_sol:
                    bst_sol = row

        logger.debug("bst_sol =  %s", bst_sol)

        return bst_sol

    def add_opts_lst(self, lst_labels=None, json_path=None, selected_pos=None):

        if lst_labels is None:
            logger.debug("json_path = %s", json_path)
            self.list_labl = ops_list_from_json(json_path)

        n_row = len(self.list_labl)
        logger.debug("n_row = %s", n_row)
        n_col = len(self.list_labl[0])
        logger.debug("n_col = %s", n_col)

        self.setRowCount(n_row)
        self.setColumnCount(n_col - 1)

        header_label_lst = [
            "max δ",
            "rmsd",
            " min cc",
            "max cc",
            "latt",
            "  a ",
            "  b ",
            "  c ",
            " α ",
            " β ",
            " γ ",
            "Ok",
        ]

        self.setHorizontalHeaderLabels(header_label_lst)

        self.rec_col = None

        for row, row_cont in enumerate(self.list_labl):
            for col, col_cont in enumerate(row_cont[1:]):
                item = QTableWidgetItem(col_cont)
                item.setFlags(Qt.ItemIsEnabled)
                if col_cont == " Y":
                    item.setBackground(QColor(Qt.green).lighter())
                    item.setForeground(Qt.black)

                    self.rec_col = col + 1

                elif col_cont == " N":
                    item.setBackground(QColor(Qt.red).lighter())
                    item.setForeground(Qt.black)

                else:
                    if row == selected_pos:
                        item.setBackground(Qt.blue)
                        item.setForeground(Qt.yellow)

                    else:
                        if float(row) / 2.0 == int(float(row) / 2.0):
                            item.setBackground(QColor(50, 50, 50, 50))

                        else:
                            item.setBackground(Qt.white)

                        item.setForeground(Qt.black)

                item.setFont(
                    QFont("Monospace", self.sys_font_point_size)
                )  # , QFont.Bold))
                self.setItem(row, col, item)

        self.resizeColumnsToContents()

    def del_opts_lst(self):

        logger.debug("del_opts_lst")
        self.clear()
        self.setRowCount(1)
        self.setColumnCount(1)


class MyReindexOpts(QDialog):
    def __init__(self, parent, summary_json: str, node_id: int):
        """
        Create a reindex dialog.

        Args:
            parent: The parent window for the dialog
            summary_json: Path to the summary.json for a step
            node_id:
                The node number of the refine_bravais_settings step.
                Used to locate the log file for the symmetry header.
        """
        super().__init__(parent)
        self.setWindowTitle("Reindex")
        self.row = -1
        self._set_ref(summary_json, node_id)

    def _set_ref(self, in_json_path: str, lin_num: int):
        """
        Set the reference data for the settings table.

        Args:
            in_json_path: Path to the summary.json for a step
            lin_num: The node number of the refine_bravais_settings step
        """
        my_box = QVBoxLayout()
        self.my_inner_table = ReindexTable(self)
        self.my_inner_table.opt_signal.connect(self._select_row)

        cwd_path = os.path.join(sys_arg.directory, "dui_files")
        full_json_path = os.path.join(cwd_path, in_json_path)

        self.my_inner_table.add_opts_lst(json_path=full_json_path)

        if self.my_inner_table.rec_col is not None:
            my_solu = self.my_inner_table.find_best_solu()
            self.my_inner_table.opt_clicked(my_solu, 0)

        recomd_str = "Select a bravais lattice to enforce: \n"
        try:
            recomd_str += "(best guess solution = row {})".format(
                self.my_inner_table.tmp_sel + 1
            )

        except BaseException as e:
            # Since we don't know exactly what this was supposed to be
            # - AttributeError? We don't know how to cleanly catch
            logger.error("Unknown exception catch caught. Was: %s", e)
            recomd_str += "(no best solution could be automatically determined)"

        bot_box = QHBoxLayout()
        bot_box.addWidget(QLabel(recomd_str))
        bot_box.addStretch()
        ok_but = QPushButton("     OK      ")
        ok_but.clicked.connect(self.my_inner_table.ok_clicked)
        bot_box.addWidget(ok_but)
        header_text, v_header_size = header_text_from_node(lin_num, full_json_path)
        my_box.addWidget(QLabel(header_text))
        my_box.addWidget(self.my_inner_table)
        my_box.addLayout(bot_box)

        self.setLayout(my_box)

        n_col = self.my_inner_table.columnCount()
        tot_width = 80
        for col in range(n_col):
            loc_width = self.my_inner_table.columnWidth(col)
            tot_width += loc_width

        n_row = self.my_inner_table.rowCount()
        row_height = self.my_inner_table.rowHeight(1)
        tot_heght = int((float(n_row)) * float(row_height))
        tot_heght += int((float(v_header_size + 2)) * float(row_height * 0.62))

        self.resize(tot_width, tot_heght)

    def _select_row(self, row: int):
        """A row in the reindex table has been firmly selected"""
        logger.debug("Selected row %s", row)
        self.row = row
        self.accept()
