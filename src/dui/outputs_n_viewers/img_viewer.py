"""
iDIALS GUI's image viewer

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
import sys
import os

from dials.array_family import flex

from dials.algorithms.image.threshold import (
    DispersionThresholdDebug,
    DispersionExtendedThresholdDebug,
)

from dxtbx.model.experiment_list import ExperimentListFactory

import numpy as np

try:
    sys.path.append("../")
    from dui.cli_utils import sys_arg
    from dui.gui_utils import get_main_path
    from dui.outputs_n_viewers.img_view_tools import (
        panel_data_as_double,
        build_qimg,
        draw_palette_label,
        find_hkl_near,
        list_arrange,
        list_p_arrange,
    )
    from dui.qt import (
        QApplication,
        QButtonGroup,
        QCheckBox,
        QColor,
        QComboBox,
        QDoubleSpinBox,
        QFont,
        QGroupBox,
        QHBoxLayout,
        QIcon,
        QIntValidator,
        QLabel,
        QLineEdit,
        QMenu,
        QPainter,
        QPen,
        QPixmap,
        QImage,
        QPoint,
        QPointF,
        QPushButton,
        QRadioButton,
        QRect,
        QRectF,
        QScrollArea,
        QSlider,
        QSpinBox,
        Qt,
        QTimer,
        QVBoxLayout,
        QWidget,
        Signal,
    )
except ImportError:
    from ..cli_utils import sys_arg
    from ..gui_utils import get_main_path
    from .img_view_tools import (
        panel_data_as_double,
        build_qimg,
        draw_palette_label,
        find_hkl_near,
        list_arrange,
        list_p_arrange,
    )
    from ..qt import (
        QApplication,
        QButtonGroup,
        QCheckBox,
        QColor,
        QComboBox,
        QDoubleSpinBox,
        QFont,
        QGroupBox,
        QHBoxLayout,
        QIcon,
        QIntValidator,
        QLabel,
        QLineEdit,
        QMenu,
        QPainter,
        QPen,
        QPixmap,
        QImage,
        QPoint,
        QPointF,
        QPushButton,
        QRadioButton,
        QRect,
        QRectF,
        QScrollArea,
        QSlider,
        QSpinBox,
        Qt,
        QTimer,
        QVBoxLayout,
        QWidget,
        Signal,
    )


from six.moves import range

logger = logging.getLogger(__name__)

MyQWidgetWithQPainter = QWidget


def build_mask_item(img_paint_obj):

    try:
        x1 = img_paint_obj.x_prev / img_paint_obj.my_scale
        y1 = img_paint_obj.y_prev / img_paint_obj.my_scale
        x2 = img_paint_obj.x_pos / img_paint_obj.my_scale
        y2 = img_paint_obj.y_pos / img_paint_obj.my_scale

        same_item = False

        if img_paint_obj.my_parent.chk_box_mask.isChecked():
            if img_paint_obj.my_parent.rad_but_rect_mask.isChecked():
                if x1 > x2:
                    x1, x2 = x2, x1

                if y1 > y2:
                    y1, y2 = y2, y1

                if x2 > img_paint_obj.img_width:
                    x2 = float(img_paint_obj.img_width)

                if y2 > img_paint_obj.img_height:
                    y2 = float(img_paint_obj.img_height)

                if x1 < 0:
                    x1 = 0.0

                if y1 < 0:
                    y1 = 0.0

                # https://github.com/ccp4/DUI/issues/136
                if x1 == x2 and y1 == y2:
                    return False, None, False

                to_append = ("rect", int(x1), int(x2), int(y1), int(y2))

            elif img_paint_obj.my_parent.rad_but_circ_mask.isChecked():
                dx = x2 - x1
                dy = y2 - y1
                r = float(dx * dx + dy * dy) ** (0.5)

                if x1 + r > img_paint_obj.img_width:
                    r = img_paint_obj.img_width - x1

                if y1 + r > img_paint_obj.img_height:
                    r = img_paint_obj.img_height - y1

                if r > x1:
                    r = x1

                if r > y1:
                    r = y1

                # https://github.com/ccp4/DUI/issues/136
                if r < 1:
                    return False, None, False

                to_append = ("circ", int(x1), int(y1), int(r))

            if img_paint_obj.my_parent.rad_but_poly_mask.isChecked():

                if x2 > img_paint_obj.img_width:
                    x2 = float(img_paint_obj.img_width)

                if y2 > img_paint_obj.img_height:
                    y2 = float(img_paint_obj.img_height)

                if x2 < 0:
                    x2 = 0.0

                if y2 < 0:
                    y2 = 0.0

                to_append_append = (int(x2), int(y2))

                try:
                    if img_paint_obj.mask_items[-1][0] == "poly":
                        same_item = True
                        item_list = list(img_paint_obj.mask_items[-1])
                        item_list.append(to_append_append)
                        to_append = tuple(item_list)

                    else:
                        to_append = ("poly", to_append_append)

                except IndexError:
                    to_append = ("poly", to_append_append)

            return True, to_append, same_item

        else:
            return False, None, False

    except TypeError:
        # logger.info("except(build_mask_item) ... TypeError")
        return False, None, False

    except AttributeError:
        # logger.info(" except(build_mask_item) ... AttributeError")
        return False, None, False


class ImgPainter(QWidget):

    ll_mask_applied = Signal(list)
    ll_b_centr_applied = Signal(list)

    def __init__(self, parent=None):
        super(ImgPainter, self).__init__()
        self.my_parent = parent

        self.img = None
        self.setMouseTracking(True)
        self.xb = None
        self.yb = None
        self.np_mask = None
        self.mask_flex = None

        self.closer_ref = None
        self.my_scale = 0.333
        self.img_width = 247
        self.img_height = 253

        self.resize(self.img_width * self.my_scale, self.img_height * self.my_scale)

        self.p_h_svar = self.my_parent.my_scrollable.horizontalScrollBar
        self.p_v_svar = self.my_parent.my_scrollable.verticalScrollBar

        self.reset_mask_tool(None)
        self.reset_bc_tool(None)

    def reset_mask_tool(self, event):
        self.mask_items = []
        self.unpop_menu()

    def reset_bc_tool(self, event):
        self.new_bc = [None, None]
        self.update()

    def mousePressEvent(self, event):
        self.x_prev, self.y_prev = self.x_pos, self.y_pos

    def mouseReleaseEvent(self, event):

        emit_mask, to_append, same_item = build_mask_item(self)

        if emit_mask:
            if same_item:
                self.mask_items[-1] = to_append

            else:
                self.mask_items.append(to_append)

            self.ll_mask_applied.emit(self.mask_items)

        elif self.my_parent.chk_box_B_centr.isChecked():
            pix_col = int(self.x_pos / self.my_scale)
            pix_row = int(self.y_pos / self.my_scale)
            self.ll_b_centr_applied.emit([pix_col, pix_row])
            self.tmp_bc_x = pix_col
            self.tmp_bc_y = pix_row
            self.update()

        self.x_prev, self.y_prev = None, None

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            self.x_pos, self.y_pos = event.x(), event.y()
            pix_col = int(self.x_pos / self.my_scale)
            pix_row = int(self.y_pos / self.my_scale)

            self.my_parent.update_info_label(pix_col, pix_row)

            if self.my_parent.rad_but_near_hkl.isChecked():
                self.find_closer_hkl(self.x_pos, self.y_pos)

            else:
                self.closer_ref = None

        elif event.buttons() == Qt.LeftButton:
            if self.my_parent.chk_box_mask.isChecked():
                self.x_pos, self.y_pos = event.x(), event.y()
                self.update()

            elif self.my_parent.chk_box_B_centr.isChecked():
                self.x_pos, self.y_pos = event.x(), event.y()

            else:
                dx = event.x() - self.x_pos
                dy = event.y() - self.y_pos
                self.move_scrollbar(scrollBar=self.p_h_svar(), dst=dx)
                self.move_scrollbar(scrollBar=self.p_v_svar(), dst=dy)

        elif event.buttons() == Qt.RightButton:
            logger.debug("Right click drag")

    def wheelEvent(self, event):

        if event.delta() > 0.0 and self.my_scale < 100.0:
            scale_factor = 1.1

        elif event.delta() < 0.0 and self.my_scale > 0.2:
            scale_factor = 0.9

        else:
            scale_factor = None
            logger.debug("reaching scale limit")

        if scale_factor is not None:

            self.my_scale *= scale_factor

            h_scr_bar = float(self.p_h_svar().value())
            v_scr_bar = float(self.p_v_svar().value())

            border_dx = float(event.x() - h_scr_bar)
            border_dy = float(event.y() - v_scr_bar)

            h_new_pbar_pos = int(
                scale_factor * h_scr_bar + (scale_factor - 1.0) * border_dx
            )
            v_new_pbar_pos = int(
                scale_factor * v_scr_bar + (scale_factor - 1.0) * border_dy
            )

            self.update()

            self.move_scrollbar(scrollBar=self.p_h_svar(), new_pos=h_new_pbar_pos)
            self.move_scrollbar(scrollBar=self.p_v_svar(), new_pos=v_new_pbar_pos)

    def scale2fact(self, new_scale=None):
        old_scale = float(self.my_scale)

        if new_scale is None:
            self.my_scale = 1.0
        else:
            self.my_scale *= new_scale

        try:
            scale_factor = self.my_scale / old_scale
            self.update()

            h_scr_bar = float(self.p_h_svar().value())
            v_scr_bar = float(self.p_v_svar().value())
            self.move_scrollbar(
                scrollBar=self.p_h_svar(), new_pos=h_scr_bar * scale_factor
            )
            self.move_scrollbar(
                scrollBar=self.p_v_svar(), new_pos=v_scr_bar * scale_factor
            )
            logger.debug("rescaling to: %s", self.my_scale)

        except ZeroDivisionError:
            logger.info("NOT scaling my_painter")
            scale_factor = 1.0

    def move_scrollbar(self, scrollBar=None, dst=None, new_pos=None):
        if dst is not None:
            old_val = scrollBar.value()
            scrollBar.setValue(old_val - dst)

        if new_pos is not None:
            scrollBar.setValue(new_pos)

    def find_closer_hkl(self, x_mouse, y_mouse):
        if self.pre_flat_data is not None and self.user_choice[1]:
            tmp_flat_data = self.pre_flat_data

        elif self.obs_flat_data is not None and self.user_choice[0]:
            tmp_flat_data = self.obs_flat_data

        else:
            tmp_flat_data = None

        if tmp_flat_data is not None:
            x_mouse_scaled = float(x_mouse) / self.my_scale
            y_mouse_scaled = float(y_mouse) / self.my_scale
            try:
                closer_hkl, closer_slice = find_hkl_near(
                    x_mouse_scaled, y_mouse_scaled, tmp_flat_data
                )

                self.closer_ref = [closer_hkl, closer_slice]
                self.update()

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.debug(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("Failed to find closer HKL")

    def set_img_pix(
        self,
        q_img=None,
        obs_flat_data_in=None,
        pre_flat_data_in=None,
        user_choice_in=(None, None),
    ):

        self.img = q_img
        self.obs_flat_data = obs_flat_data_in
        self.pre_flat_data = pre_flat_data_in
        self.user_choice = user_choice_in

        self.img_width = q_img.width()
        self.img_height = q_img.height()
        self.update()

    def update_my_mask(self, np_mask, mask_flex):
        # logger.info("\n np_mask =", np_mask, "\n")
        self.np_mask = np_mask
        self.mask_flex = mask_flex

        if np_mask is not None:
            # logger.info("self.np_mask.shape =", self.np_mask.shape)

            width = self.np_mask.shape[0]
            height = self.np_mask.shape[1]

            img_array = np.zeros([width, height, 4], dtype=np.uint8)

            for row_pow, ent_row in enumerate(self.np_mask):
                for col_pos, elem in enumerate(ent_row):
                    if not elem:
                        # img_array[row_pow, col_pos, 0] = 155 # Blue
                        # img_array[row_pow, col_pos, 1] = 155 # Green
                        img_array[row_pow, col_pos, 2] = 255  # Red
                        img_array[row_pow, col_pos, 3] = 175  # Transp

            q_img = QImage(img_array.data, height, width, QImage.Format_ARGB32)
            self.mask_pixmap = QPixmap(q_img)

    def update_my_beam_centre(self, xb, yb, n_pan_xb_yb):
        self.xb = xb
        self.yb = yb
        self.n_pan_xb_yb = n_pan_xb_yb

    def _draw_hkl(self, reflection, painter, indexed_pen, non_indexed_pen, i, j):
        # x = float(reflection[0]) + 1.0
        # y = float(reflection[1]) + 1.0

        x = float(reflection[0] + reflection[2]) + 0.3
        y = float(reflection[1] + float(reflection[3]) * 0.5) + 6.0 / self.my_scale
        # y = float(reflection[1])

        if reflection[4] == "NOT indexed":
            painter.setPen(non_indexed_pen)

        else:
            painter.setPen(indexed_pen)

        if (
            self.my_parent.rad_but_all_hkl.isChecked()
            and reflection[4] != ""
            and reflection[4] != "NOT indexed"
        ):
            painter.drawText(
                QPoint(int(x * self.my_scale), int(y * self.my_scale)), reflection[4]
            )
        elif self.my_parent.rad_but_near_hkl.isChecked() and self.closer_ref == [i, j]:
            painter.drawText(
                QPoint(int(x * self.my_scale), int(y * self.my_scale)), reflection[4]
            )

    def unpop_menu(self):
        try:
            self.my_parent.pop_mask_menu.hide()
            self.setFocus()
            self.update()

        except AttributeError:
            logger.debug("No need to unpop_menu now")

    def ini_mask(self):
        self.ll_mask_applied.emit(self.mask_items)
        self.unpop_menu()

    def ini_centr(self):
        self.ll_b_centr_applied.emit(self.new_bc)
        self.unpop_menu()

    def paintEvent(self, event):
        # logger.info("paintEvent(img_viewer)")
        if self.img is None:
            return

        if self.my_scale == 0:
            self.my_scale = 1

        scaled_width = int(self.img_width * self.my_scale)
        scaled_height = int(self.img_height * self.my_scale)

        self.resize(scaled_width, scaled_height)

        rect = QRect(0, 0, scaled_width, scaled_height)
        pixmap = QPixmap(self.img)
        painter = QPainter(self)

        indexed_pen = QPen()  # creates a default indexed_pen

        try:
            pen_col = {
                "white2black": Qt.blue,
                "black2white": Qt.cyan,
                "hot descend": Qt.magenta,
            }
            indexed_pen.setBrush(pen_col[self.my_parent.palette])

        except KeyError:
            indexed_pen.setBrush(Qt.green)

        indexed_pen.setStyle(Qt.SolidLine)

        non_indexed_pen = QPen()  # creates a default non_indexed_pen
        if (
            self.my_parent.palette == "white2black"
            or self.my_parent.palette == "black2white"
        ):
            non_indexed_pen.setBrush(Qt.red)
            # non_indexed_pen.setBrush(Qt.magenta)

        else:
            non_indexed_pen.setBrush(QColor(75, 150, 200))

        to_do_pen = QPen()  # creates a default pen for user actions
        if (
            self.my_parent.palette == "white2black"
            or self.my_parent.palette == "hot descend"
        ):
            to_do_pen.setBrush(QColor(0, 155, 0))
        else:
            to_do_pen.setBrush(Qt.green)

        if self.my_scale >= 5.0:
            indexed_pen.setWidth(self.my_scale / 3.5)
            non_indexed_pen.setWidth(self.my_scale / 3.5)
            to_do_pen.setWidth(self.my_scale / 3.5)
            non_indexed_pen.setStyle(Qt.DotLine)

        else:
            indexed_pen.setWidth(0.0)
            non_indexed_pen.setWidth(0.0)
            to_do_pen.setWidth(0.0)
            non_indexed_pen.setStyle(Qt.SolidLine)

        painter.drawPixmap(rect, pixmap)

        if self.np_mask is not None:
            # logger.info("Drawing Mask start   ...", end="")
            painter.drawPixmap(rect, self.mask_pixmap)
            # logger.info(" .Drawing Mask end")

        cen_siz = 20.0
        if self.xb is not None and self.yb is not None:
            painter.setPen(indexed_pen)
            det_mov = self.n_pan_xb_yb * 213
            painter.drawLine(
                int(self.xb * self.my_scale),
                int((self.yb + det_mov) * self.my_scale - cen_siz),
                int(self.xb * self.my_scale),
                int((self.yb + det_mov) * self.my_scale + cen_siz),
            )

            painter.drawLine(
                int(self.xb * self.my_scale + cen_siz),
                int((self.yb + det_mov) * self.my_scale),
                int(self.xb * self.my_scale - cen_siz),
                int((self.yb + det_mov) * self.my_scale),
            )

        if self.my_parent.chk_box_B_centr.isChecked():
            try:
                painter.setPen(to_do_pen)
                painter.drawLine(
                    int(self.tmp_bc_x * self.my_scale),
                    int(self.tmp_bc_y * self.my_scale - cen_siz),
                    int(self.tmp_bc_x * self.my_scale),
                    int(self.tmp_bc_y * self.my_scale + cen_siz),
                )
                painter.drawLine(
                    int(self.tmp_bc_x * self.my_scale) - cen_siz,
                    int(self.tmp_bc_y * self.my_scale),
                    int(self.tmp_bc_x * self.my_scale) + cen_siz,
                    int(self.tmp_bc_y * self.my_scale),
                )

            except AttributeError:
                pass

        if self.my_parent.chk_box_mask.isChecked():
            painter.setPen(to_do_pen)

            # Drawing list of previous mask items
            try:
                for item in self.mask_items:
                    if item[0] == "rect":
                        xd = item[2] - item[1]
                        yd = item[4] - item[3]
                        painter.drawRect(
                            item[1] * self.my_scale,
                            item[3] * self.my_scale,
                            xd * self.my_scale,
                            yd * self.my_scale,
                        )

                    elif item[0] == "circ":
                        r = item[3] * self.my_scale
                        q_center = QPointF(
                            item[1] * self.my_scale, item[2] * self.my_scale
                        )
                        painter.drawEllipse(q_center, r, r)

                    elif item[0] == "poly":
                        if len(item[1:]) >= 2:
                            prev_tup = item[1]
                            for posi in item[2:]:
                                x1 = prev_tup[0]
                                y1 = prev_tup[1]
                                x2 = posi[0]
                                y2 = posi[1]

                                painter.drawLine(
                                    x1 * self.my_scale,
                                    y1 * self.my_scale,
                                    x2 * self.my_scale,
                                    y2 * self.my_scale,
                                )

                                prev_tup = posi

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.info(
                    "\n exception(item in self.mask_items ... for loop ): %s: %s",
                    type(e).__name__,
                    e,
                    "\n",
                )

            # Drawing current mask item
            draw_mask_item, item, same_item = build_mask_item(self)
            if draw_mask_item:
                try:
                    if item[0] == "rect":
                        xd = item[2] - item[1]
                        yd = item[4] - item[3]
                        painter.drawRect(
                            item[1] * self.my_scale,
                            item[3] * self.my_scale,
                            xd * self.my_scale,
                            yd * self.my_scale,
                        )

                    elif item[0] == "circ":
                        r = item[3] * self.my_scale
                        q_center = QPointF(
                            item[1] * self.my_scale, item[2] * self.my_scale
                        )
                        painter.drawEllipse(q_center, r, r)

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.info(
                        "\n exception(draw_mask_item) = %s: %s",
                        type(e).__name__,
                        e,
                        "\n",
                    )

        if (
            self.obs_flat_data is not None
            and self.my_parent.chk_box_show.checkState()
            and self.pre_flat_data is not None
        ):

            hkl_font = QFont()
            hkl_font.setPointSize(10)
            painter.setFont(hkl_font)

            lst_tmp_hkl = None
            if self.user_choice[0]:
                try:
                    for j, img_flat_data in enumerate(self.obs_flat_data):
                        for i, reflection in enumerate(img_flat_data):
                            x = float(reflection[0])
                            y = float(reflection[1])
                            width = float(reflection[2])
                            height = float(reflection[3])
                            rectangle = QRectF(
                                x * self.my_scale,
                                y * self.my_scale,
                                width * self.my_scale,
                                height * self.my_scale,
                            )

                            if reflection[4] == "NOT indexed":
                                painter.setPen(non_indexed_pen)

                            else:
                                painter.setPen(indexed_pen)

                            painter.drawRect(rectangle)
                            lst_tmp_hkl = self.obs_flat_data

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.info(
                        " \n >>> Caught unknown exception type %s: %s",
                        type(e).__name__,
                        e,
                    )
                    logger.info("No reflection (Obsevations) to show ... None type")

            if self.user_choice[1]:
                try:
                    for j, img_flat_data in enumerate(self.pre_flat_data):
                        for i, reflection in enumerate(img_flat_data):

                            x = float(reflection[0]) + 1.0
                            y = float(reflection[1]) + 1.0

                            if reflection[4] == "NOT indexed":
                                painter.setPen(non_indexed_pen)

                            else:
                                painter.setPen(indexed_pen)

                            cross_size = float(reflection[2]) + 1.0
                            cross_2_size = float(reflection[3])

                            painter.drawLine(
                                x * self.my_scale,
                                (y - cross_size) * self.my_scale,
                                x * self.my_scale,
                                (y + cross_size) * self.my_scale,
                            )

                            painter.drawLine(
                                (x + cross_size) * self.my_scale,
                                y * self.my_scale,
                                (x - cross_size) * self.my_scale,
                                y * self.my_scale,
                            )

                            painter.drawLine(
                                (x - cross_2_size) * self.my_scale,
                                (y - cross_2_size) * self.my_scale,
                                (x + cross_2_size) * self.my_scale,
                                (y + cross_2_size) * self.my_scale,
                            )

                            painter.drawLine(
                                (x + cross_2_size) * self.my_scale,
                                (y - cross_2_size) * self.my_scale,
                                (x - cross_2_size) * self.my_scale,
                                (y + cross_2_size) * self.my_scale,
                            )

                            lst_tmp_hkl = self.pre_flat_data

                except TypeError:
                    logger.info("No reflection (Predictions) to show ... None type")

            try:
                for j, img_flat_data in enumerate(lst_tmp_hkl):
                    for i, reflection in enumerate(img_flat_data):
                        self._draw_hkl(
                            reflection, painter, indexed_pen, non_indexed_pen, i, j
                        )

            except TypeError:
                logger.debug("not printing HKLs ")

        painter.end()


class PopActionsMenu(QMenu):
    def __init__(self, parent=None):
        super(PopActionsMenu, self).__init__(parent)
        self.my_parent = parent

        ref_bond_group = QButtonGroup()
        ref_bond_group.addButton(self.my_parent.rad_but_rect_mask)
        ref_bond_group.addButton(self.my_parent.rad_but_circ_mask)
        ref_bond_group.addButton(self.my_parent.rad_but_poly_mask)

        info_grp = QGroupBox("Mask Tool")
        ref_bond_group_box_layout = QVBoxLayout()
        ref_bond_group_box_layout.addWidget(self.my_parent.chk_box_mask)
        ref_bond_group_box_layout.addWidget(self.my_parent.rad_but_rect_mask)
        ref_bond_group_box_layout.addWidget(self.my_parent.rad_but_circ_mask)
        ref_bond_group_box_layout.addWidget(self.my_parent.rad_but_poly_mask)

        ref_bond_group_box_layout.addWidget(self.my_parent.btn_reset_mask)

        info_grp.setLayout(ref_bond_group_box_layout)

        spot_find_grp = QGroupBox("Spot Finding Steps")

        img_spot_find_box = QVBoxLayout()

        algorithm_layout = QHBoxLayout()
        algorithm_layout.addWidget(QLabel("Algorithm"))
        algorithm_layout.addWidget(self.my_parent.spot_algorithm_select)

        nsig_b_layout = QHBoxLayout()
        nsig_b_layout.addWidget(QLabel("Sigma Background"))
        nsig_b_layout.addWidget(self.my_parent.nsig_b_spin)

        nsig_s_layout = QHBoxLayout()
        nsig_s_layout.addWidget(QLabel("Sigma Strong"))
        nsig_s_layout.addWidget(self.my_parent.nsig_s_spin)

        global_threshold_spin_layout = QHBoxLayout()
        global_threshold_spin_layout.addWidget(QLabel("Global Threshold"))
        global_threshold_spin_layout.addWidget(self.my_parent.global_threshold_spin)

        min_local_layout = QHBoxLayout()
        min_local_layout.addWidget(QLabel("Minimum Local "))
        min_local_layout.addWidget(self.my_parent.min_count_spin)

        gain_layout = QHBoxLayout()
        gain_layout.addWidget(QLabel("Gain"))
        gain_layout.addWidget(self.my_parent.gain_spin)

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Kernel Size"))
        size_layout.addWidget(self.my_parent.size_1_spin)
        size_layout.addWidget(self.my_parent.size_2_spin)

        img_spot_find_box.addLayout(algorithm_layout)
        img_spot_find_box.addLayout(nsig_b_layout)
        img_spot_find_box.addLayout(nsig_s_layout)
        img_spot_find_box.addLayout(global_threshold_spin_layout)
        img_spot_find_box.addLayout(min_local_layout)
        img_spot_find_box.addLayout(gain_layout)
        img_spot_find_box.addLayout(size_layout)

        left_img_but_box = QVBoxLayout()
        left_img_but_box.addWidget(self.my_parent.btn_set_image)
        left_img_but_box.addWidget(self.my_parent.btn_set_mean)
        left_img_but_box.addWidget(self.my_parent.btn_set_varia)
        left_img_but_box.addWidget(self.my_parent.btn_set_disp)

        right_img_but_box = QVBoxLayout()
        right_img_but_box.addWidget(self.my_parent.btn_set_cv_mask)
        right_img_but_box.addWidget(self.my_parent.btn_set_val_mask)
        right_img_but_box.addWidget(self.my_parent.btn_set_glo_mask)
        right_img_but_box.addWidget(self.my_parent.btn_set_fin_mask)

        img_but_main_box = QHBoxLayout()
        img_but_main_box.addLayout(left_img_but_box)
        img_but_main_box.addLayout(right_img_but_box)

        img_spot_find_box.addLayout(img_but_main_box)

        spot_find_grp.setLayout(img_spot_find_box)

        my_main_box = QHBoxLayout()
        left_main_box = QVBoxLayout()
        left_main_box.addWidget(info_grp)
        left_main_box.addWidget(self.my_parent.chk_box_B_centr)
        my_main_box.addLayout(left_main_box)
        my_main_box.addWidget(spot_find_grp)

        self.setLayout(my_main_box)
        self.show()


class PopDisplayMenu(QMenu):

    sliders_changed = Signal(int, int)

    def __init__(self, parent=None):
        super(PopDisplayMenu, self).__init__(parent)
        self.my_parent = parent

        # group to tune up palette

        palette_grp = QGroupBox("Palette Tuning")
        colour_box = QHBoxLayout()
        colour_box.addWidget(QLabel("I min"))
        colour_box.addWidget(self.my_parent.min_i_edit)
        colour_box.addWidget(QLabel("I max"))
        colour_box.addWidget(self.my_parent.max_i_edit)
        colour_box.addWidget(self.my_parent.palette_select)
        colour_box.addStretch()

        self.my_parent.slider_min.setMinimum(-3)
        self.my_parent.slider_min.setMaximum(499)
        self.my_parent.slider_min.valueChanged[int].connect(self.slider_min_changed)

        self.my_parent.slider_max.setMinimum(-3)
        self.my_parent.slider_max.setMaximum(499)
        self.my_parent.slider_max.valueChanged[int].connect(self.slider_max_changed)

        palette_layout = QVBoxLayout()

        slider_max_Hlayout = QHBoxLayout()
        slider_max_Hlayout.addWidget(QLabel(" "))  # Left side margin
        slider_max_Hlayout.addWidget(self.my_parent.slider_max)
        slider_max_Hlayout.addWidget(QLabel(" "))  # Right side margin
        palette_layout.addLayout(slider_max_Hlayout)

        palette_Hlayout = QHBoxLayout()
        palette_Hlayout.addWidget(QLabel("   "))  # Left side margin
        palette_Hlayout.addWidget(self.my_parent.palette_label)
        palette_Hlayout.addWidget(QLabel("   "))  # Right side margin
        palette_layout.addLayout(palette_Hlayout)

        slider_min_Hlayout = QHBoxLayout()
        slider_min_Hlayout.addWidget(QLabel(" "))  # Left side margin
        slider_min_Hlayout.addWidget(self.my_parent.slider_min)
        slider_min_Hlayout.addWidget(QLabel(" "))  # Right side margin
        palette_layout.addLayout(slider_min_Hlayout)

        palette_layout.addWidget(self.my_parent.slider_min)
        palette_layout.addLayout(colour_box)
        palette_grp.setLayout(palette_layout)

        # group to control what to see from algorithms

        ref_bond_group = QButtonGroup()
        ref_bond_group.addButton(self.my_parent.rad_but_all_hkl)
        ref_bond_group.addButton(self.my_parent.rad_but_near_hkl)
        ref_bond_group.addButton(self.my_parent.rad_but_none_hkl)

        info_grp = QGroupBox("Reflection Info ")
        ref_bond_group_box_layout = QVBoxLayout()
        ref_bond_group_box_layout.addWidget(self.my_parent.chk_box_show)
        ref_bond_group_box_layout.addWidget(self.my_parent.rad_but_all_hkl)
        ref_bond_group_box_layout.addWidget(self.my_parent.rad_but_near_hkl)
        ref_bond_group_box_layout.addWidget(self.my_parent.rad_but_none_hkl)

        info_grp.setLayout(ref_bond_group_box_layout)

        # group to control how to navigate thru images

        mid_top_box = QHBoxLayout()
        mid_top_box.addWidget(QLabel("Image Jump Step"))
        mid_top_box.addWidget(self.my_parent.img_step)

        mid_bot_box = QHBoxLayout()
        mid_bot_box.addWidget(QLabel("Number of Images to Add"))
        mid_bot_box.addWidget(self.my_parent.num_of_imgs_to_add)

        img_select_box = QVBoxLayout()
        img_select_box.addLayout(mid_top_box)
        img_select_box.addLayout(mid_bot_box)

        img_select_group_box = QGroupBox("IMG Navigation")
        img_select_group_box.setLayout(img_select_box)

        main_top_layout = QVBoxLayout()
        main_top_layout.addWidget(palette_grp)

        bott_layout = QHBoxLayout()
        bott_layout.addWidget(info_grp)
        bott_layout.addWidget(img_select_group_box)

        main_top_layout.addLayout(bott_layout)

        self.setLayout(main_top_layout)
        self.show()

    def showEvent(self, event):
        logger.debug("repainting")
        try:

            self.my_parent.palette_label.setPixmap(
                QPixmap(
                    self.my_parent.palette_qimg(
                        draw_palette_label(self.my_parent.i_min, self.my_parent.i_max),
                        self.my_parent.palette,
                        self.my_parent.i_min,
                        self.my_parent.i_max,
                    )
                )
            )

        except BaseException as e:
            # We don't want to catch bare exceptions but don't know
            # what this was supposed to catch. Log it.
            logger.info("Caught unknown exception type %s: %s", type(e).__name__, e)
            logger.info("no (...my_sweep) yet, skipping palette label paint")

    def slider_max_changed(self, value):
        if self.my_parent.slider_min.sliderPosition() > value - 15:
            self.my_parent.slider_min.setValue(value - 15)

        self.sliders_changed.emit(
            int(value), int(self.my_parent.slider_min.sliderPosition())
        )

    def slider_min_changed(self, value):
        if self.my_parent.slider_max.sliderPosition() < value + 15:
            self.my_parent.slider_max.setValue(value + 15)

        self.sliders_changed.emit(
            int(self.my_parent.slider_max.sliderPosition()), int(value)
        )


class ThresholdDebugGenerator:
    def __init__(self, image_in):
        self.image = image_in

    def set_mask(self, mask_flex_in):
        self.mask = mask_flex_in

        if self.mask is None:
            self.mask = flex.bool(flex.grid(self.image.all()), True)

    def set_pars(
        self, algorithm, gain, size, nsig_b, nsig_s, global_threshold, min_count
    ):
        self.algorithm = algorithm
        self.gain = gain
        self.size = size
        self.nsig_b = nsig_b
        self.nsig_s = nsig_s
        self.global_threshold = global_threshold
        self.min_count = min_count

    def test_dispersion_debug(self):

        self.gain_map = flex.double(flex.grid(self.image.all()), self.gain)

        if self.algorithm == "dispersion":
            Debug = DispersionThresholdDebug
        elif self.algorithm == "dispersion extended":
            Debug = DispersionExtendedThresholdDebug
        else:
            raise ValueError(
                "Unknown spot-finding algorithm: {}".format(self.algorithm)
            )

        debug = Debug(
            self.image,
            self.mask,
            self.gain_map,
            self.size,
            self.nsig_b,
            self.nsig_s,
            self.global_threshold,
            self.min_count,
        )

        return debug


def GetDoubleFromBool(bool_in):
    double_out = bool_in.as_1d().as_double()
    double_out.reshape(bool_in.accessor())
    return double_out


class MyImgWin(QWidget):

    mask_applied = Signal(list)
    bc_applied = Signal(list)
    predic_changed = Signal()
    new_pars_applied = Signal(list)

    def __init__(self, json_file_path=None, pckl_file_path=None):
        super(MyImgWin, self).__init__()

        self.my_scrollable = QScrollArea()
        self.my_painter = ImgPainter(self)
        self.my_scrollable.setWidget(self.my_painter)

        self.img_arr = None
        self.img_select = QSpinBox()
        self.img_step = QSpinBox()
        self.num_of_imgs_to_add = QSpinBox()

        max_min_validator = QIntValidator(-5, 999999, self)

        sys_font = QFont()

        sys_font_point_size = sys_font.pointSize()
        self.video_timer = QTimer(self)

        self.i_min = -3

        self.min_i_edit = QLineEdit()
        self.min_i_edit.setFixedWidth(6 * sys_font_point_size)
        self.min_i_edit.setValidator(max_min_validator)
        self.min_i_edit.editingFinished.connect(self.min_changed_by_user)

        self.i_max = 100
        self.max_i_edit = QLineEdit()
        self.max_i_edit.setFixedWidth(6 * sys_font_point_size)
        self.max_i_edit.setValidator(max_min_validator)
        self.max_i_edit.editingFinished.connect(self.max_changed_by_user)

        self.slider_min = QSlider(Qt.Horizontal)
        self.slider_max = QSlider(Qt.Horizontal)

        # Viewing Tool
        self.chk_box_show = QCheckBox("Show reflection info")
        self.chk_box_show.setChecked(True)
        self.chk_box_show.stateChanged.connect(self.set_img)

        self.rad_but_all_hkl = QRadioButton("All HKLs")
        self.rad_but_all_hkl.clicked.connect(self.set_img)

        self.rad_but_all_hkl.setChecked(True)
        self.rad_but_near_hkl = QRadioButton("Nearest HKL")
        self.rad_but_near_hkl.clicked.connect(self.set_img)
        self.rad_but_none_hkl = QRadioButton("No HKL")
        self.rad_but_none_hkl.clicked.connect(self.set_img)

        self.rad_but_fnd_hkl = QCheckBox("Observations")
        self.rad_but_fnd_hkl.setChecked(True)
        self.rad_but_fnd_hkl.clicked.connect(self.set_img)
        self.rad_but_pre_hkl = QCheckBox("Predictions")
        self.rad_but_pre_hkl.clicked.connect(self.emit_predic_changed)

        # Mask tools
        self.btn_reset_mask = QPushButton("Reset")
        self.chk_box_mask = QCheckBox("Activate mask tool")
        self.chk_box_mask.setChecked(False)

        self.rad_but_rect_mask = QRadioButton("Rectangle")
        self.rad_but_circ_mask = QRadioButton("Circle")
        self.rad_but_poly_mask = QRadioButton("Polygon")
        self.rad_but_rect_mask.setChecked(True)

        self.rad_but_rect_mask.toggled.connect(self.my_painter.unpop_menu)
        self.rad_but_circ_mask.toggled.connect(self.my_painter.unpop_menu)
        self.rad_but_poly_mask.toggled.connect(self.my_painter.unpop_menu)

        self.chk_box_mask.stateChanged.connect(self.my_painter.ini_mask)
        self.btn_reset_mask.clicked.connect(self.my_painter.reset_mask_tool)

        self.my_painter.ll_mask_applied.connect(self.apply_mask)
        self.my_painter.ll_b_centr_applied.connect(self.apply_bc)

        # Manual beam center tools
        self.chk_box_B_centr = QCheckBox("Set beam centre")
        self.chk_box_B_centr.stateChanged.connect(self.my_painter.ini_centr)
        self.chk_box_B_centr.setChecked(False)

        ##############################################################################

        # previews for spot finding
        self.btn_set_image = QPushButton("Image")

        self.btn_set_varia = QPushButton("Variance")
        self.btn_set_mean = QPushButton("Mean")
        self.btn_set_disp = QPushButton("Dispersion")

        self.btn_set_cv_mask = QPushButton("sigma_b ")
        self.btn_set_val_mask = QPushButton("sigma_s")
        self.btn_set_glo_mask = QPushButton("Global")
        self.btn_set_fin_mask = QPushButton("Threshold")

        self.btn_set_varia.clicked.connect(self.set_variance_img)

        self.btn_set_mean.clicked.connect(self.set_mean_img)
        self.btn_set_disp.clicked.connect(self.set_disp_img)
        self.btn_set_fin_mask.clicked.connect(self.set_fin_mask_img)
        self.btn_set_glo_mask.clicked.connect(self.set_glo_mask_img)
        self.btn_set_cv_mask.clicked.connect(self.set_cv_mask_img)
        self.btn_set_val_mask.clicked.connect(self.set_val_mask_img)

        self.btn_set_image.clicked.connect(self.set_img_img)

        self.gain_spin = QDoubleSpinBox()
        self.gain_spin.setValue(1)

        self.size_1_spin = QSpinBox()
        self.size_1_spin.setValue(3)
        self.size_1_spin.setMinimum(1)
        self.size_2_spin = QSpinBox()
        self.size_2_spin.setValue(3)
        self.size_2_spin.setMinimum(1)

        self.spot_algorithm_select = QComboBox()
        self.spot_algorithm = ["dispersion extended", "dispersion"]
        for algorithm in self.spot_algorithm:
            self.spot_algorithm_select.addItem(algorithm)

        self.nsig_b_spin = QDoubleSpinBox()
        self.nsig_b_spin.setValue(6)

        self.nsig_s_spin = QDoubleSpinBox()
        self.nsig_s_spin.setValue(3)

        self.global_threshold_spin = QDoubleSpinBox()
        self.global_threshold_spin.setValue(0)

        self.min_count_spin = QSpinBox()
        self.min_count_spin.setValue(2)
        self.min_count_spin.setMinimum(2)
        # min_count_ <= (2 * size[0] + 1) * (2 * size[1] + 1) && min_count_ > 1

        self.debug_gen_timer = QTimer(self)
        self.debug_gen_timer.timeout.connect(self.check_debug_pars)
        self.debug_gen_data = None

        ##########################################################################

        # Grouping
        ref_type_group = QButtonGroup()
        ref_type_group.addButton(self.rad_but_fnd_hkl)
        ref_type_group.addButton(self.rad_but_pre_hkl)
        ref_type_group_box_layout = QVBoxLayout()
        ref_type_group_box_layout.addWidget(self.rad_but_fnd_hkl)
        ref_type_group_box_layout.addWidget(self.rad_but_pre_hkl)

        type_grp = QGroupBox("Reflection type ")
        type_grp.setLayout(ref_type_group_box_layout)

        self.palette_select = QComboBox()
        self.palette_lst = ["hot ascend", "hot descend", "black2white", "white2black"]
        self.palette = self.palette_lst[0]
        for plt in self.palette_lst:
            self.palette_select.addItem(plt)

        self.palette_select.currentIndexChanged.connect(self.palette_changed_by_user)

        self._button_panel = QWidget(self)

        def _create_and_connect(my_ico_path, slot):
            """Create a pushbutton for the Play/stop bar"""
            btn = QPushButton(parent=self._button_panel)
            btn.setIcon(QIcon(my_ico_path))
            btn.setMinimumWidth(30)
            btn.clicked.connect(slot)
            return btn

        my_code_path = get_main_path()
        icon_path = my_code_path + "/resources/"

        self.btn_first = _create_and_connect(
            icon_path + "first_img.png", self.btn_first_clicked
        )

        self.btn_rev = _create_and_connect(
            icon_path + "rew_img.png", self.btn_rev_clicked
        )

        self.btn_prev = _create_and_connect(
            icon_path + "prev_img.png", self.btn_prev_clicked
        )

        self.btn_next = _create_and_connect(
            icon_path + "next_img.png", self.btn_next_clicked
        )

        self.btn_ffw = _create_and_connect(
            icon_path + "ffw_img.png", self.btn_ffw_clicked
        )

        self.btn_last = _create_and_connect(
            icon_path + "last_img.png", self.btn_last_clicked
        )

        btn_f_size = sys_font_point_size - 1

        self.btn_prev.setFont(QFont("Monospace", btn_f_size))
        self.btn_next.setFont(QFont("Monospace", btn_f_size))
        self.btn_first.setFont(QFont("Monospace", btn_f_size))
        self.btn_rev.setFont(QFont("Monospace", btn_f_size))
        self.btn_ffw.setFont(QFont("Monospace", btn_f_size))
        self.btn_last.setFont(QFont("Monospace", btn_f_size))

        self.btn_play = QPushButton("Play/stop video")
        self.btn_play.clicked.connect(self.btn_play_clicked)

        nav_box = QHBoxLayout()
        nav_box.setMargin(0)
        nav_box.addWidget(self.btn_first)
        nav_box.addWidget(self.btn_rev)
        nav_box.addWidget(self.btn_prev)
        nav_box.addWidget(self.img_select)
        nav_box.addWidget(self.btn_next)
        nav_box.addWidget(self.btn_ffw)
        nav_box.addWidget(self.btn_last)
        nav_box.addStretch()

        self._button_panel.setLayout(nav_box)

        self.palette_label = QLabel()
        self.palette_qimg = build_qimg()

        palette_menu_but = QPushButton("Display")
        pop_palette_menu = PopDisplayMenu(self)
        palette_menu_but.setMenu(pop_palette_menu)
        pop_palette_menu.sliders_changed.connect(self.new_sliders_pos)

        mask_menu_but = QPushButton("Actions")
        self.pop_mask_menu = PopActionsMenu(self)
        mask_menu_but.setMenu(self.pop_mask_menu)

        zoom_in_but = QPushButton()
        zoom_in_but.setIcon(QIcon(icon_path + "zoom_plus_ico.png"))
        zoom_in_but.clicked.connect(self.zoom_in)
        zoom2one_but = QPushButton()
        zoom2one_but.setIcon(QIcon(icon_path + "zoom_ono_one_ico.png"))
        zoom2one_but.clicked.connect(self.zoom2one)

        zoom2border_but = QPushButton()
        zoom2border_but.setIcon(QIcon(icon_path + "zoom_border.png"))
        zoom2border_but.clicked.connect(self.scale2border)

        zoom_out_but = QPushButton()
        zoom_out_but.setIcon(QIcon(icon_path + "zoom_minus_ico.png"))
        zoom_out_but.clicked.connect(self.zoom_out)

        self.img_num = 1
        self.img_step_val = 1
        self.stack_size = 1
        # possible values of img2show are:
        # "origin", "modif" or "mask"
        self.img2show = "origin"

        self.ref2exp = None
        self.my_sweep = None
        self.find_spt_flat_data_lst = [None]
        self.pred_spt_flat_data_lst = [None]

        self.current_qimg = build_qimg()
        self.contrast_initiated = False

        if json_file_path is None:
            logger.debug("\n no datablock given \n")
            # n_of_imgs = 1

        else:
            self.ini_datablock(json_file_path)

        if pckl_file_path:
            self.set_reflection_table(pckl_file_path)

        else:
            logger.debug("No pickle file given")

        self.set_img()

        self.max_i_edit.setText(str(self.i_max))
        self.min_i_edit.setText(str(self.i_min))

        self.img_select.valueChanged.connect(self.img_changed_by_user)
        self.img_step.valueChanged.connect(self.step_changed_by_user)
        self.num_of_imgs_to_add.valueChanged.connect(self.stack_changed_by_user)
        self.img_step.setValue(10)

        top_box = QHBoxLayout()
        top_box.setMargin(0)
        top_box.addWidget(palette_menu_but)
        # top_box.addWidget(big_menu_but)
        top_box.addWidget(mask_menu_but)

        mid_box = QHBoxLayout()
        mid_box.addWidget(self.btn_play)
        mid_box.addStretch()
        mid_box.addWidget(zoom_in_but)
        mid_box.addWidget(zoom2one_but)
        mid_box.addWidget(zoom2border_but)
        mid_box.addWidget(zoom_out_but)

        self.info_label = QLabel("X, Y, I = ?,?,?")
        self.info_label.setFont(QFont("Monospace", btn_f_size))

        top_left_v_box = QVBoxLayout()
        top_left_v_box.setMargin(0)
        top_left_v_box.addWidget(self._button_panel)

        top_left_v_box.addLayout(mid_box)
        top_left_v_box.addLayout(top_box)

        top_hbox = QHBoxLayout()
        top_hbox.setMargin(0)
        top_hbox.addLayout(top_left_v_box)
        top_hbox.addWidget(type_grp)

        my_box = QVBoxLayout()
        my_box.setMargin(0)
        my_box.addLayout(top_hbox)

        my_box.addWidget(self.my_scrollable)
        my_box.addWidget(self.info_label)

        self.setLayout(my_box)

        # changing default palette:

        self.palette_select.setCurrentIndex(3)

    def set_img_img(self):
        self.draw_img_img()

    def draw_img_img(self):
        try:
            # logger.info("img_origin_arr")
            self.img2show = "origin"
            self.painter_set_img_pix(self.img_num - 1, 1)
            self.debug_gen_timer.stop()

        except AttributeError:
            logger.info("No image loaded yet")

    def set_variance_img(self):
        self.draw_variance_img()

    def draw_variance_img(self):
        try:
            # logger.info("img_varian_arr")
            self.get_debug_gen()
            self.img_varian_arr = self.debug_data.variance()
            self.img2show = "modif_varian"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def set_mean_img(self):
        self.draw_mean_img()

    def draw_mean_img(self):
        try:
            # logger.info("img_mean_arr")
            self.get_debug_gen()
            self.img_varian_arr = self.debug_data.mean()
            self.img2show = "modif_mean"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def set_disp_img(self):
        self.draw_disp_img()

    def draw_disp_img(self):
        try:
            # logger.info("img_disper_arr")
            self.get_debug_gen()
            self.img_varian_arr = self.debug_data.index_of_dispersion()
            self.img2show = "modif_disper"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def set_fin_mask_img(self):
        self.draw_fin_mask_img()

    def draw_fin_mask_img(self):
        try:
            # logger.info("img_final_mask_arr")
            self.get_debug_gen()
            self.img_varian_arr = GetDoubleFromBool(self.debug_data.final_mask())
            self.img2show = "mask_fin"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def set_glo_mask_img(self):
        self.draw_glo_mask_img()

    def draw_glo_mask_img(self):
        try:
            # logger.info("img_global_mask_arr")
            self.get_debug_gen()
            self.img_varian_arr = GetDoubleFromBool(self.debug_data.global_mask())
            self.img2show = "mask_glob"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def set_cv_mask_img(self):
        self.draw_cv_mask_img()

    def draw_cv_mask_img(self):
        try:
            # logger.info("img_cv_mask_arr")
            self.get_debug_gen()
            self.img_varian_arr = GetDoubleFromBool(self.debug_data.cv_mask())
            self.img2show = "mask_cv"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def set_val_mask_img(self):
        self.draw_val_mask_img()

    def draw_val_mask_img(self):
        try:
            # logger.info("img_value_mask_arr")
            self.get_debug_gen()
            self.img_varian_arr = GetDoubleFromBool(self.debug_data.value_mask())
            self.img2show = "mask_val"
            self.painter_set_img_pix(self.img_num - 1, 1)

        except AttributeError:
            logger.info("No image loaded yet")

    def get_debug_gen(self):
        self.debug_gen_data = ThresholdDebugGenerator(image_in=self.img_arr)
        self.debug_gen_data.set_mask(self.my_painter.mask_flex)
        self.debug_gen_data.set_pars(
            algorithm=self.spot_algorithm_select.currentText(),
            gain=self.gain_spin.value(),
            size=(self.size_1_spin.value(), self.size_2_spin.value()),
            nsig_b=self.nsig_b_spin.value(),
            nsig_s=self.nsig_s_spin.value(),
            global_threshold=self.global_threshold_spin.value(),
            min_count=self.min_count_spin.value(),
        )

        self.debug_data = self.debug_gen_data.test_dispersion_debug()

        if not self.debug_gen_timer.isActive():
            self.debug_gen_timer.start(500)

    def check_debug_pars(self, do_anyway=False):
        if (
            self.debug_gen_data.algorithm != self.spot_algorithm_select.currentText()
            or self.debug_gen_data.gain != self.gain_spin.value()
            or self.debug_gen_data.size
            != (self.size_1_spin.value(), self.size_2_spin.value())
            or self.debug_gen_data.nsig_b != self.nsig_b_spin.value()
            or self.debug_gen_data.nsig_s != self.nsig_s_spin.value()
            or self.debug_gen_data.global_threshold
            != self.global_threshold_spin.value()
            or self.debug_gen_data.min_count != self.min_count_spin.value()
            or do_anyway
        ):

            if self.img2show == "origin":
                self.debug_gen_timer.stop()

            if self.img2show == "modif_varian":
                self.draw_variance_img()

            if self.img2show == "modif_mean":
                self.draw_mean_img()

            if self.img2show == "modif_disper":
                self.draw_disp_img()

            if self.img2show == "mask_fin":
                self.draw_fin_mask_img()

            if self.img2show == "mask_glob":
                self.draw_glo_mask_img()

            if self.img2show == "mask_cv":
                self.draw_cv_mask_img()

            if self.img2show == "mask_val":
                self.draw_val_mask_img()

    def ini_contrast(self):
        if not self.contrast_initiated:
            try:
                n_of_imgs = len(self.my_sweep.indices())
                logger.debug("n_of_imgs(ini_contrast) = %s", n_of_imgs)

                img_arr_n0 = self.my_sweep.get_raw_data(0)[0]
                img_arr_n1 = self.my_sweep.get_raw_data(1)[0]
                img_arr_n2 = self.my_sweep.get_raw_data(2)[0]

                tst_sample = (
                    img_arr_n0[0:25, 0:25].as_double()
                    + img_arr_n1[0:25, 0:25].as_double()
                    + img_arr_n2[0:25, 0:25].as_double()
                ) / 3.0
                logger.debug("tst_sample = %s", tst_sample)

                i_mean = flex.mean(tst_sample)
                tst_new_max = (i_mean + 1) * 25

                logger.debug("flex.mean(tst_sample) = %s", i_mean)
                logger.debug("tst_new_max = %s", tst_new_max)
                self.try_change_max(tst_new_max)
                self.try_change_min(-3)
                self.contrast_initiated = True

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.info("Caught unknown exception type %s: %s", type(e).__name__, e)
                logger.info("Unable to calculate mean and adjust contrast")

    def ini_datablock(self, json_file_path):

        if json_file_path is not None:
            try:
                cwd_path = os.path.join(sys_arg.directory, "dui_files")
                n_json_file_path = os.path.join(cwd_path, json_file_path)

                experiments = ExperimentListFactory.from_json_file(n_json_file_path)
                self.my_sweep = experiments.imagesets()[0]
                ###########################################################
                # self.my_sweep = datablock.extract_sweeps()[0]
                self.img_select.clear()
            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.info("Caught unknown exception type %s: %s", type(e).__name__, e)
                logger.info("Failed to load images from  datablock.json")

            try:
                """
                logger.info(
                    "self.my_sweep.get_array_range() = %s",
                    self.my_sweep.get_array_range(),
                )
                """

                n_of_imgs = len(self.my_sweep.indices())
                # logger.info("n_of_imgs =", n_of_imgs)

                self.img_select.setMaximum(n_of_imgs)
                self.img_select.setMinimum(1)

                self.img_step.setMaximum(n_of_imgs / 2)
                self.img_step.setMinimum(1)

                self.num_of_imgs_to_add.setMaximum(n_of_imgs)
                self.num_of_imgs_to_add.setMinimum(1)

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.info("Caught unknown exception type %s: %s", type(e).__name__, e)
                logger.info("Failed to set up IMG control dialog")

        self.btn_first_clicked()
        self.ini_contrast()
        self.set_img()
        QTimer.singleShot(1000, self.scale2border)

    def scale2border(self):

        pt_width = float(self.my_painter.size().width())
        pt_height = float(self.my_painter.size().height())
        sc_width = float(self.my_scrollable.size().width())
        sc_height = float(self.my_scrollable.size().height())

        if pt_width == 0 or pt_height == 0:
            self.my_painter.scale2fact()

        else:
            a_ratio_pt = pt_width / pt_height
            a_ratio_sc = sc_width / sc_height

            if a_ratio_pt > a_ratio_sc:
                self.my_painter.scale2fact(sc_width / pt_width)

            else:
                self.my_painter.scale2fact(sc_height / pt_height)

    def set_reflection_table(self, pckl_file_path):
        if pckl_file_path[0] is not None:
            logger.debug("\npickle file (found) = %s", pckl_file_path[0])
            try:

                table = flex.reflection_table.from_file(pckl_file_path[0])

                logger.debug("table = %s", table)
                logger.debug("len(table) =  %s", len(table))
                bbox_col = map(list, table["bbox"])
                pan_col = map(int, table["panel"])
                try:
                    hkl_col = map(str, table["miller_index"])

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.debug(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    hkl_col = []

                n_imgs = self.img_select.maximum()
                self.find_spt_flat_data_lst = []
                if n_imgs > 0:
                    self.find_spt_flat_data_lst = list_arrange(
                        bbox_col, hkl_col, pan_col, n_imgs
                    )

                else:
                    logger.info("empty IMG lst")

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.info("Caught unknown exception type %s: %s", type(e).__name__, e)
                self.find_spt_flat_data_lst = [None]
                logger.debug("\n something failed with the reflection pickle \n\n")

            try:

                # logger.info("pckl_file_path[1]=", pckl_file_path[1])

                table = flex.reflection_table.from_file(pckl_file_path[1])

                logger.debug("table = %s", table)
                logger.debug("len(table) =  %s", len(table))
                # n_refs = len(table)
                pos_col = map(list, table["xyzcal.px"])
                pan_col = map(int, table["panel"])
                try:
                    hkl_col = map(str, table["miller_index"])

                except BaseException as e:
                    # We don't want to catch bare exceptions but don't know
                    # what this was supposed to catch. Log it.
                    logger.debug(
                        "Caught unknown exception type %s: %s", type(e).__name__, e
                    )
                    hkl_col = []

                n_imgs = self.img_select.maximum()
                self.pred_spt_flat_data_lst = []
                if n_imgs > 0:
                    self.pred_spt_flat_data_lst = list_p_arrange(
                        pos_col, hkl_col, pan_col, n_imgs
                    )

            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.debug(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                self.pred_spt_flat_data_lst = [None]
                logger.debug("\n something failed with the reflection pickle \n\n")

        else:
            self.find_spt_flat_data_lst = [None]
            self.pred_spt_flat_data_lst = [None]

        self.set_img()

    def apply_mask(self, new_mask_items):
        if self.chk_box_mask.isChecked():
            self.unchec_b_centr()
            self.mask_applied.emit(new_mask_items)

    def apply_bc(self, new_bc):
        if self.chk_box_B_centr.isChecked():
            self.unchec_my_mask()
            self.bc_applied.emit(new_bc)

    def unchec_my_mask(self):
        self.chk_box_mask.setCheckState(False)

    def chec_my_mask(self):
        self.chk_box_mask.setCheckState(True)

    def unchec_b_centr(self):
        self.chk_box_B_centr.setCheckState(False)

    def chec_b_centr(self):
        self.chk_box_B_centr.setCheckState(True)

    def zoom2one(self):
        self.my_painter.scale2fact()

    def zoom_in(self):
        self.my_painter.scale2fact(1.2)

    def zoom_out(self):
        self.my_painter.scale2fact(0.8)

    def update_painter_info(self, all_data):

        try:
            xb = all_data.xb / all_data.x_px_size
            yb = all_data.yb / all_data.y_px_size
            n_pan_xb_yb = all_data.n_pan_xb_yb

        except TypeError:
            xb, yb, n_pan_xb_yb = None, None, None
            logger.info("\n xb, yb, n_pan_xb_yb = None, None, None \n")

        self.my_painter.update_my_beam_centre(xb, yb, n_pan_xb_yb)
        self.my_painter.update_my_mask(all_data.np_mask, all_data.mask_flex)

    def update_exp(self, reference):
        self.ref2exp = reference
        logger.debug("\n update_exp(self, reference) \n")

    def update_info_label(self, x_pos, y_pos):

        new_label_txt = ""
        if self.ref2exp:
            image_file = os.path.basename(
                self.ref2exp.imageset.get_image_identifier(self.img_num - 1)
            )
            new_label_txt += "{0}: ".format(image_file)

        if self.img_arr:
            new_label_txt += (
                "X = "
                + str(x_pos).rjust(4)
                + ", Y = "
                + str(y_pos).rjust(4)
                + ", I = "
                + str(self.img_arr[y_pos, x_pos]).rjust(4)
            )

        else:
            new_label_txt += "X, Y, I = ?,?,?"

        if self.ref2exp and self.ref2exp.beam:
            mybeam = self.ref2exp.beam
            p = self.ref2exp.detector[0]
            res_float = p.get_resolution_at_pixel(mybeam.get_s0(), (x_pos, y_pos))
            res_str = str("{: 4.2f}".format(res_float))
            new_label_txt += ", resolution = " + res_str + " " + u"\u00C5"

        else:
            new_label_txt += ", resolution = ?"

        self.info_label.setText(new_label_txt)

    def emit_predic_changed(self):
        self.predic_changed.emit()
        self.set_img()

    def set_img(self):
        if self.my_sweep is not None:
            img_pos = self.img_num - 1
            loc_stk_siz = self.stack_size

            n_of_panels = len(self.my_sweep.get_detector())
            if n_of_panels == 1:
                pan_num = 0

            elif n_of_panels == 24:
                pan_num = tuple(range(24))

            else:
                logger.info(
                    "number of  panels NOT supported, defaulting to only first one"
                )
                pan_num = 1

            if loc_stk_siz == 1:
                self.img_arr = panel_data_as_double(self.my_sweep, img_pos, pan_num)

            elif loc_stk_siz > 1:

                if img_pos + loc_stk_siz > len(self.my_sweep.indices()) - 1:
                    loc_stk_siz = len(self.my_sweep.indices()) - img_pos

                loc_scale = 1.0 / float(loc_stk_siz)
                self.img_arr = panel_data_as_double(self.my_sweep, img_pos, pan_num)

                for times in range(1, loc_stk_siz):
                    pos_to_add = (img_pos) + times
                    self.img_arr = (
                        self.img_arr
                        + panel_data_as_double(self.my_sweep, pos_to_add, pan_num)
                        * loc_scale
                    )

            if self.img2show != "origin":
                self.check_debug_pars(do_anyway=True)

            self.painter_set_img_pix(img_pos, loc_stk_siz)

        self.palette_label.setPixmap(
            QPixmap(
                self.palette_qimg(
                    draw_palette_label(self.i_min, self.i_max),
                    self.palette,
                    self.i_min,
                    self.i_max,
                )
            )
        )

    def painter_set_img_pix(self, img_pos, loc_stk_siz):
        if self.img2show[0:4] == "mask":
            tmp_min = -0.5
            tmp_max = 1.5

        else:
            tmp_min = self.i_min
            tmp_max = self.i_max

        if self.img2show != "origin":
            self.new_pars_applied.emit(
                [
                    self.debug_gen_data.gain,
                    self.debug_gen_data.size,
                    self.debug_gen_data.nsig_b,
                    self.debug_gen_data.nsig_s,
                    self.debug_gen_data.global_threshold,
                    self.debug_gen_data.min_count,
                ]
            )

        if self.find_spt_flat_data_lst == [None] and self.pred_spt_flat_data_lst == [
            None
        ]:

            if self.img2show == "origin":
                self.my_painter.set_img_pix(
                    self.current_qimg(self.img_arr, self.palette, tmp_min, tmp_max)
                )

            else:
                self.my_painter.set_img_pix(
                    self.current_qimg(
                        self.img_varian_arr, self.palette, tmp_min, tmp_max
                    )
                )

        else:

            if self.img2show == "origin":
                self.my_painter.set_img_pix(
                    q_img=self.current_qimg(
                        self.img_arr, self.palette, tmp_min, tmp_max
                    ),
                    obs_flat_data_in=self.find_spt_flat_data_lst[
                        img_pos : img_pos + loc_stk_siz
                    ],
                    pre_flat_data_in=self.pred_spt_flat_data_lst[
                        img_pos : img_pos + loc_stk_siz
                    ],
                    user_choice_in=(
                        self.rad_but_fnd_hkl.checkState(),
                        self.rad_but_pre_hkl.checkState(),
                    ),
                )

            else:
                self.my_painter.set_img_pix(
                    q_img=self.current_qimg(
                        self.img_varian_arr, self.palette, tmp_min, tmp_max
                    ),
                    obs_flat_data_in=self.find_spt_flat_data_lst[
                        img_pos : img_pos + loc_stk_siz
                    ],
                    pre_flat_data_in=self.pred_spt_flat_data_lst[
                        img_pos : img_pos + loc_stk_siz
                    ],
                    user_choice_in=(
                        self.rad_but_fnd_hkl.checkState(),
                        self.rad_but_pre_hkl.checkState(),
                    ),
                )

        logger.debug("\n self.i_min = %s", self.i_min)
        logger.debug(" self.i_max = %s %s", self.i_max, "\n")

    def btn_play_clicked(self):
        if self.video_timer.isActive():
            logger.debug("Stoping video")
            self.video_timer.stop()
            try:
                self.video_timer.timeout.disconnect()
            except BaseException as e:
                # We don't want to catch bare exceptions but don't know
                # what this was supposed to catch. Log it.
                logger.debug(
                    "Caught unknown exception type %s: %s", type(e).__name__, e
                )
                logger.debug("unable to disconnect timer again")

        else:
            logger.debug("Playing video")
            self.video_timer.timeout.connect(self.btn_next_clicked)
            self.video_timer.start(1)

    def new_sliders_pos(self, pos1, pos2):
        self.max_i_edit.setText(str(int(pos1)))
        self.min_i_edit.setText(str(int(pos2)))
        self.min_changed_by_user()
        self.max_changed_by_user()

    def min_changed_by_user(self):
        self.try_change_min(self.min_i_edit.text())

    def try_change_min(self, new_value):
        try:
            self.i_min = int(new_value)
        except ValueError:
            self.i_min = 0

        self.slider_min.setValue(self.i_min)
        self.set_img()

    def max_changed_by_user(self):
        self.try_change_max(self.max_i_edit.text())

    def try_change_max(self, new_value):
        try:
            self.i_max = int(new_value)
        except ValueError:
            self.i_max = 0

        self.slider_max.setValue(self.i_max)
        self.set_img()

    def palette_changed_by_user(self, new_palette_num):
        self.palette = self.palette_lst[new_palette_num]
        self.set_img()

    def btn_first_clicked(self):
        # TODO have a look at why is unable to go to
        # TODO the very first image sometimes

        self.img_num = 1
        self.img_select.setValue(self.img_num)

    def btn_rev_clicked(self):
        self.img_num -= self.img_step_val
        if self.img_num < 1:
            self.img_num = 1

        self.img_select.setValue(self.img_num)

    def btn_prev_clicked(self):
        self.img_num -= 1
        if self.img_num < 1:
            self.img_num = 1

        self.img_select.setValue(self.img_num)

    def btn_next_clicked(self):
        self.img_num += 1
        if self.img_num > self.img_select.maximum():
            if self.video_timer.isActive():
                self.img_num = 1
            else:
                self.img_num = self.img_select.maximum()

        self.img_select.setValue(self.img_num)

    def btn_ffw_clicked(self):
        self.img_num += self.img_step_val
        if self.img_num > self.img_select.maximum():
            self.img_num = self.img_select.maximum()

        self.img_select.setValue(self.img_num)

    def btn_last_clicked(self):
        self.img_num = self.img_select.maximum()
        self.img_select.setValue(self.img_num)

    def step_changed_by_user(self, value):
        self.img_step_val = value

    def stack_changed_by_user(self, value):
        self.stack_size = value
        self.set_img()

    def img_changed_by_user(self, value):
        # self.img2show = "origin"
        self.img_num = value
        if self.img_num > self.img_select.maximum():
            self.img_num = self.img_select.maximum()
            self.img_select.setValue(self.img_num)

        self.set_img()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    logger.debug("sys.argv = %s", sys.argv)
    logger.debug("len(sys.argv) = %s", len(sys.argv))

    if len(sys.argv) > 1:
        img_path = sys.argv[1]
        if len(sys.argv) > 2:
            pckl_file_path = sys.argv[2]

        else:
            pckl_file_path = None

    else:
        img_path = None

    logger.debug("img_path = %s", img_path)
    logger.debug("pckl_file_path = %s", pckl_file_path)

    diag = MyImgWin(img_path, [pckl_file_path, None])
    diag.show()
    sys.exit(app.exec_())
    app.exec_()
