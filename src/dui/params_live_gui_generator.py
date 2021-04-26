"""
DUI's code generator from phil parameters

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
"""

import logging
import sys

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


# FIXME Copied from dials.index.py. This is needed here because scipy needs to
# be imported before cctbx otherwise there will be a segmentation fault. This
# should be fixed in dials.index so that we don't need to import here.
try:
    # try importing scipy.linalg before any cctbx modules, otherwise we
    # sometimes get a segmentation fault/core dump if it is imported after
    # scipy.linalg is a dependency of sklearn.cluster.DBSCAN
    import scipy.linalg  # noqa
except ImportError:
    pass

from dui.qt import (
    QApplication,
    QComboBox,
    QFont,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    Qt,
    QVBoxLayout,
    QWidget,
    Signal,
    QStyledItemDelegate,
    QPalette,
    QStandardItem,
    QEvent,
    QFontMetrics,
)

logger = logging.getLogger(__name__)


class ScopeData:
    """
    class conceived to store only data related to the scope Phil object
    """

    pass


class tree_2_lineal:
    """
    Recursively navigates the Phil objects in a way that the final
    self.lst_obj is a lineal list without ramifications, this final list
    will be used later to generate a dynamic GUI
    """

    def __init__(self, phl_obj):
        self.lst_obj = []
        self.deep_in_rec(phl_obj)

    def __call__(self):
        return self.lst_obj

    def deep_in_rec(self, phl_obj):

        for single_obj in phl_obj:
            if single_obj.is_definition:
                self.lst_obj.append(single_obj)

            elif single_obj.is_scope:
                if single_obj.name != "output":
                    scope_info = ScopeData()
                    scope_info.name = str(single_obj.name)
                    scope_info.f_path = str(single_obj.full_path())
                    scope_info.i_m_scope = True
                    scope_info.short_caption = single_obj.short_caption
                    scope_info.help = single_obj.help

                    # print "scope_info.f_path =", scope_info.f_path
                    scope_info.indent = scope_info.f_path.count(".")
                    # print "scope_info.f_path.count('.') =", scope_info.indent

                    self.lst_obj.append(scope_info)
                    self.deep_in_rec(single_obj.objects)

                else:
                    logger.debug(
                        'The " %s %s',
                        single_obj.name,
                        '" set of parameters is automatically handled by idials',
                    )
                    # pass

            else:
                logger.debug(
                    "\n _____________ <<< WARNING neither definition or scope\n"
                )
                # pass


class MyQComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.ClickFocus)

    def wheelEvent(self, event):
        """
        if self.hasFocus():
            logger.info("self.hasFocus")
            #return QComboBox.wheelEvent(event)
        else:
            logger.info("NO hasFocus")
        """
        logger.info("event: %s", event)
        return

# https://gis.stackexchange.com/questions/350148/qcombobox-multiple-selection-pyqt5
class CheckableComboBox(QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        palette = qApp.palette()
        palette.setBrush(QPalette.Base, palette.button())
        self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None, checked=False):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        if checked:
            item.setData(Qt.Checked, Qt.CheckStateRole)
        else:
            item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data, prepending "*" to selected items
        res = []
        for i in range(self.model().rowCount()):
            elt = str(self.model().item(i).data())
            if self.model().item(i).checkState() == Qt.Checked:
                elt = "*" + elt
            res.append(elt)
        return res


class PhilWidget(QWidget):
    item_changed = Signal(str, str)

    def __init__(self, phl_obj, parent=None):
        # TODO fix the order of this two parameters
        super().__init__(parent)
        self.original_parent = parent

        self.bg_box = QVBoxLayout(self)

        lst_obj = tree_2_lineal(phl_obj.objects)
        lst_phil_obj = lst_obj()

        self.phil_list2gui(lst_phil_obj)

        self.setLayout(self.bg_box)

        self._found_labels = []
        self._current_label = 0

    @staticmethod
    def _tooltip_from_phil_object(obj):
        if obj.help:
            tooltip = "<p>" + obj.help + "</p>"
        else:
            tooltip = ""
        return tooltip

    def user_searching(self, value):

        self.original_parent.search_next_button.setEnabled(False)
        self._found_labels = []

        for nm, labl_obj in enumerate(self.lst_label_widg):
            labl_obj.setStyleSheet(labl_obj.style_orign)

        if len(value) < 2:
            return

        logger.debug("user searching for: %s", value)
        logger.debug("len = %s", len(value))

        for nm, labl_obj in enumerate(self.lst_label_widg):
            labl_text = labl_obj.text()
            if value in labl_text:
                self._found_labels.append(labl_obj)
                logger.debug("pos_str = %s", nm)

        if self._found_labels:
            self.parent().parent().ensureWidgetVisible(self._found_labels[0])
            self._found_labels[0].setStyleSheet(
                "color: rgba(0, 155, 255, 255);" "background-color: yellow;"
            )
            self._current_label = 0

        if len(self._found_labels) > 1:
            self.original_parent.search_next_button.setEnabled(True)

    def find_next(self):
        label = self._found_labels[self._current_label]
        label.setStyleSheet(label.style_orign)
        self._current_label += 1
        self._current_label = self._current_label % len(self._found_labels)

        label = self._found_labels[self._current_label]
        self.parent().parent().ensureWidgetVisible(label)
        label.setStyleSheet(
            "color: rgba(0, 155, 255, 255);" "background-color: yellow;"
        )

    def phil_list2gui(self, lst_phil_obj):

        sys_font = QFont()
        sys_font_point_size = sys_font.pointSize()

        inde_step = 4

        self.lst_label_widg = []
        self.lst_var_widg = []

        non_added_lst = []

        for nm, obj in enumerate(lst_phil_obj):

            if isinstance(obj, ScopeData):
                tmp_str = " " * int(obj.indent * inde_step) + str(obj.name)
                # print tmp_str
                tmp_widg = QLabel(tmp_str)
                tmp_widg.setAutoFillBackground(True)
                # tmp_widg.setPalette(self.plt_scp)
                tmp_widg.setFont(QFont("Monospace", sys_font_point_size, QFont.Bold))
                tmp_widg.style_orign = "color: rgba(85, 85, 85, 255)"
                tmp_widg.setStyleSheet(tmp_widg.style_orign)

                tooltip = self._tooltip_from_phil_object(obj)
                if tooltip:
                    tmp_widg.setToolTip(tooltip)

                self.bg_box.addWidget(tmp_widg)

                tmp_widg.test_flag = "Yes"

                self.lst_label_widg.append(tmp_widg)

            else:

                tmp_h_box = QHBoxLayout()

                indent = str(obj.full_path()).count(".")
                tmp_str = " " * indent * inde_step + str(obj.name)
                tmp_label = QLabel(tmp_str)
                tmp_label.setAutoFillBackground(True)
                # tmp_label.setPalette(self.plt_obj)
                tmp_label.style_orign = "color: rgba(0, 0, 0, 255)"
                tmp_label.setStyleSheet(tmp_label.style_orign)
                tmp_label.setFont(QFont("Monospace", sys_font_point_size))

                tmp_h_box.addWidget(tmp_label)

                self.lst_label_widg.append(tmp_label)

                if obj.type.phil_type == "bool":

                    tmp_widg = MyQComboBox()
                    tmp_widg.tmp_lst = []
                    tmp_widg.tmp_lst.append("True")
                    tmp_widg.tmp_lst.append("False")
                    tmp_widg.tmp_lst.append("Auto")
                    # tmp_widg.setFocusPolicy(Qt.StrongFocus)
                    for lst_itm in tmp_widg.tmp_lst:
                        tmp_widg.addItem(lst_itm)

                    if str(obj.extract()) == "True":
                        tmp_widg.setCurrentIndex(0)
                        tmp_str += "                          True"

                    elif str(obj.extract()) == "False":
                        tmp_widg.setCurrentIndex(1)
                        tmp_str += "                          False"

                    elif str(obj.extract()) == "Auto":
                        tmp_widg.setCurrentIndex(2)
                        tmp_str += "                          Auto"

                    else:
                        tmp_str = None

                    tmp_widg.currentIndexChanged.connect(self.combobox_changed)

                elif obj.type.phil_type == "choice":

                    # Multi choice checkable combo box
                    if obj.type.multi:
                        tmp_widg = CheckableComboBox()

                        tmp_widg.tmp_lst = []

                        for num, opt in enumerate(obj.words):
                            opt = str(opt)
                            if opt[0] == "*":
                                opt = opt[1:]
                                tmp_widg.addItem(opt, checked=True)
                            else:
                                tmp_widg.addItem(opt)
                            tmp_str += "                          " + opt
                            tmp_widg.tmp_lst.append(opt)

                        tmp_widg.currentTextChanged.connect(self.checkable_combobox_changed)

                    else:
                    # Single choice combo box
                        tmp_widg = MyQComboBox()

                        tmp_widg.tmp_lst = []
                        pos = 0
                        found_choise = False
                        for num, opt in enumerate(obj.words):
                            opt = str(opt)
                            if opt[0] == "*":
                                found_choise = True
                                opt = opt[1:]
                                pos = num
                                tmp_str += "                          " + opt

                            tmp_widg.tmp_lst.append(opt)

                        if not found_choise:
                            tmp_str += "                          " + str(obj.extract())

                        for lst_itm in tmp_widg.tmp_lst:
                            tmp_widg.addItem(lst_itm)

                        tmp_widg.setCurrentIndex(pos)
                        tmp_widg.currentIndexChanged.connect(self.combobox_changed)

                else:
                    tmp_widg = QLineEdit()
                    tmp_widg.setText("")
                    tmp_widg.str_defl = None
                    tmp_widg.textChanged.connect(self.spnbox_changed)
                    # tmp_widg.tmp_lst = None
                    tmp_str += "                          " + str(obj.extract())

                if tmp_str is not None:
                    tmp_widg.local_path = str(obj.full_path())
                    # tmp_h_box.addStretch()
                    tooltip = self._tooltip_from_phil_object(obj)
                    if tooltip:
                        tmp_widg.setToolTip(tooltip)
                    tmp_h_box.addWidget(tmp_widg)
                    self.lst_var_widg.append(tmp_widg)
                    self.bg_box.addLayout(tmp_h_box)

        # debugging = '''
        logger.debug("Non added parameters:")
        for lin_to_print in non_added_lst:
            logger.debug(lin_to_print)

    def spnbox_changed(self, value):
        sender = self.sender()
        if sender.str_defl is not None and float(value) == 0.0:
            str_value = sender.str_defl

        else:
            str_value = str(value)

        logger.debug("sender = %s", sender)
        logger.debug("spnbox_changed to: %s", str_value)
        str_path = str(sender.local_path)
        logger.debug("local_path = %s", str_path)

        # self.param_widget_parent.update_lin_txt(str_path, str_value)
        self.item_changed.emit(str_path, str_value)

    def combobox_changed(self, value):
        sender = self.sender()
        str_value = str(sender.tmp_lst[value])
        logger.debug("combobox_changed to:  %s", str_value)
        str_path = str(sender.local_path)
        logger.debug("local_path = %s", str_path)

        # self.param_widget_parent.update_lin_txt(str_path, str_value)
        self.item_changed.emit(str_path, str_value)

    def checkable_combobox_changed(self, value):
        sender = self.sender()
        data = sender.currentData()
        str_value = " ".join(data)
        str_path = str(sender.local_path)
        self.item_changed.emit(str_path, str_value)

class TstTmpWidget(QWidget):
    def __init__(self, phl_obj=None, parent=None):
        super().__init__(parent)
        # self.param_widget_parent = self
        inner_widget = PhilWidget(
            phl_obj, self
        )  # TODO fix the order of this two parameters
        inner_widget.item_changed.connect(self.update_lin_txt)

        my_box = QVBoxLayout()
        my_box.addWidget(inner_widget)
        self.setLayout(my_box)

    def update_lin_txt(self, new_path, new_value):
        logger.debug("new_path = %s", new_path)
        logger.debug("new_value = %s", new_value)
        logger.debug("from update_lin_txt(self) in TstTmpWidget")


if __name__ == "__main__":
    from dials.command_line.refine import working_phil as phil_scope_refine

    # from dials.command_line.find_spots import phil_scope
    app = QApplication(sys.argv)
    ex = TstTmpWidget(phil_scope_refine)
    ex.show()
    sys.exit(app.exec_())
    logger.info("running ...")
