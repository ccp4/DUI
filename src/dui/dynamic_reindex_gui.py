"""
Reindex table popup GUI

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

import json
import logging
import sys
import os

try:
    from cli_utils import sys_arg

    from qt import (
        QApplication,
        QColor,
        QFont,
        QHBoxLayout,
        QLabel,
        QMainWindow,
        QPushButton,
        Qt,
        QTableWidget,
        QTableWidgetItem,
        QVBoxLayout,
        QWidget,
        Signal,
    )

except ImportError:
    from .cli_utils import sys_arg

    from .qt import (
        QApplication,
        QColor,
        QFont,
        QHBoxLayout,
        QLabel,
        QMainWindow,
        QPushButton,
        Qt,
        QTableWidget,
        QTableWidgetItem,
        QVBoxLayout,
        QWidget,
        Signal,
    )


from six.moves import range

logger = logging.getLogger(__name__)

copied_from_SymmetryExpert_d_py = """
lattice_to_spacegroup_number = {'aP':1, 'mP':3, 'mC':5, 'oP':16, 'oC':20,
                                'oF':22, 'oI':23, 'tP':75, 'tI':79,'hP':143,
                                'hR':146, 'cP':195, 'cF':196, 'cI':197}
"""


def choice_if_decimal(num_in):

    str_f = "{:6.2f}".format(num_in)
    if str_f[-3:] == ".00":
        str_out = str_f[0:-3]

    else:
        str_out = str_f

    return str_out


def ops_list_from_json(json_path=None):
    if json_path is None:
        return None

    with open(json_path) as json_file:
        json_data = json.load(json_file)

    lst_ops = []
    for key, value in json_data.iteritems():
        recommended_str = "  "
        for inner_key in value:
            if inner_key == "rmsd":
                rmsd_val = value["rmsd"]
                rmsd_str = " {:7.2}".format(rmsd_val)

            elif inner_key == "min_cc":
                min_cc_val = value["min_cc"]
                min_cc_str = " {:7.2}".format(min_cc_val)

                if "Non" in min_cc_str:
                    min_cc_str = "    - "

                # TODO the format here is not always giving the same with

                # TODO think about someting like:
                #   "aa = list(round(i, ndigits=6) for i in aa)"

            elif inner_key == "max_cc":
                max_cc_val = value["max_cc"]
                max_cc_str = " {:7.2}".format(max_cc_val)

                if "Non" in max_cc_str:
                    max_cc_str = "    - "

                # print "__________________________________________
                # type(max_cc_val) =", type(max_cc_val)
                # TODO the format here is not always giving the same with

                # TODO think about someting like:
                #   "aa = list(round(i, ndigits=6) for i in aa)"

            elif inner_key == "bravais":
                bravais_val = value["bravais"]
                bravais_str = " " + str(bravais_val).ljust(3)

            elif inner_key == "max_angular_difference":
                angular_diff_val = value["max_angular_difference"]
                angular_diff_str = " {:7.2} ".format(angular_diff_val)

            elif inner_key == "correlation_coefficients":
                # corr_coeff_val = value["correlation_coefficients"]
                # corr_coeff_str = str(corr_coeff_val)
                pass

            elif inner_key == "unit_cell":
                unit_cell_val = value["unit_cell"]
                uc_d = unit_cell_val[0:3]
                uc_a = unit_cell_val[3:6]
                unit_cell_str_a = "{:6.1f}".format(uc_d[0])
                unit_cell_str_b = "{:6.1f}".format(uc_d[1])
                unit_cell_str_c = "{:6.1f}".format(uc_d[2])

                unit_cell_str_apl = choice_if_decimal(uc_a[0])
                unit_cell_str_bet = choice_if_decimal(uc_a[1])
                unit_cell_str_gam = choice_if_decimal(uc_a[2])

            elif inner_key == "recommended":
                recommended_val = value["recommended"]
                if recommended_val:
                    recommended_str = " Y"
                else:
                    recommended_str = " N"

            else:
                logger.debug("Fell off end of key list with inner_key=%s", inner_key)

        single_lin_lst = [
            int(key),
            angular_diff_str,
            rmsd_str,
            min_cc_str,
            max_cc_str,
            bravais_str,
            unit_cell_str_a,
            unit_cell_str_b,
            unit_cell_str_c,
            unit_cell_str_apl,
            unit_cell_str_bet,
            unit_cell_str_gam,
            recommended_str,
        ]

        lst_ops.append(single_lin_lst)

    sorted_lst_ops = sorted(lst_ops)
    return sorted_lst_ops


def heather_text_from_lin(lin_num, j_path):

    dir_path_end = j_path.find("lin_")
    dir_path = j_path[0:dir_path_end]
    lin_num_str = str(lin_num)
    my_file_path = dir_path + lin_num_str + "_refine_bravais_settings.log"

    logger.debug("my_file_path: ", my_file_path)

    myfile = open(my_file_path, "r")
    all_lines = myfile.readlines()
    myfile.close()

    logger.debug("len(all_lines):", len(all_lines))

    multi_lin_txt = ""
    n_of_lines = 0
    for pos1, single_lin1 in enumerate(all_lines):
        logger.debug("pos1, single_lin1:", pos1, single_lin1)
        if str(single_lin1[0:19]) == "Chiral space groups":
            start_block = pos1
            logger.debug("start_block = %s", start_block)

            for pos2, single_lin2 in enumerate(all_lines[start_block:]):
                n_of_lines += 1
                if str(single_lin2[1:5]) == "----":
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
        super(ReindexTable, self).__init__(parent)

        self.cellClicked.connect(self.opt_clicked)

        self.v_sliderBar = self.verticalScrollBar()
        self.h_sliderBar = self.horizontalScrollBar()

        self.tmp_sel = None

        sys_font = QFont()
        self.sys_font_point_size = sys_font.pointSize()
        # self.show()

    def opt_clicked(self, row, col):
        print("Solution clicked = %s", row + 1)
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

        alpha_str = " " + u"\u03B1" + " "
        beta_str = " " + u"\u03B2" + " "
        gamma_str = " " + u"\u03B3" + " "

        low_delta_str = u"\u03B4"
        delta_max_str = "max " + low_delta_str

        header_label_lst = [
            delta_max_str,
            "rmsd",
            " min cc",
            "max cc",
            "latt",
            "  a ",
            "  b ",
            "  c ",
            alpha_str,
            beta_str,
            gamma_str,
            "Ok",
        ]

        self.setHorizontalHeaderLabels(header_label_lst)

        self.rec_col = None

        for row, row_cont in enumerate(self.list_labl):
            for col, col_cont in enumerate(row_cont[1:]):
                item = QTableWidgetItem(col_cont)
                item.setFlags(Qt.ItemIsEnabled)
                if col_cont == " Y":
                    item.setBackground(Qt.green)
                    item.setForeground(Qt.black)

                    self.rec_col = col + 1

                elif col_cont == " N":
                    item.setBackground(Qt.red)
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


class MyReindexOpts(QWidget):
    def __init__(self, parent=None):
        super(MyReindexOpts, self).__init__(parent)
        self.setWindowTitle("Reindex")

    def set_ref(self, in_json_path, lin_num):
        my_box = QVBoxLayout()
        self.my_inner_table = ReindexTable(self)

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
        heather_text, v_heather_size = heather_text_from_lin(lin_num, full_json_path)
        my_box.addWidget(QLabel(heather_text))
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
        tot_heght += int((float(v_heather_size + 2)) * float(row_height * 0.62))

        self.resize(tot_width, tot_heght)
        # self.adjustSize()
        self.show()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.btn1 = QPushButton("Click me", self)

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("A1"))
        vbox.addWidget(self.btn1)
        vbox.addWidget(QLabel("B2"))

        self.btn1.clicked.connect(self.doit)
        self.my_pop = None

        self.main_widget = QWidget(self)
        self.main_widget.setLayout(vbox)
        self.setCentralWidget(self.main_widget)

    def doit(self):
        logger.debug("Opening a new popup window")
        self.my_pop = MyReindexOpts()
        self.my_pop.set_ref(
            in_json_path="/tmp/dui2run/dui_files/lin_4_bravais_summary.json", lin_num=4
        )
        # in_json_path="/tmp/dui_run/dui_files/lin_4_bravais_summary.json"

    def opt_picked(self, opt_num):
        logger.debug("\n from dynamic_reindex_gui.py MainWindow")
        logger.debug("opt_num = %s %s", opt_num, "\n")

    def closeEvent(self, event):
        logger.debug("<< closeEvent ( from QMainWindow) >>")
        if self.my_pop is not None:
            self.my_pop.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()
    app.exec_()
