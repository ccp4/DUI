import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"


class inner_widg( QWidget):
    item_changed = pyqtSignal()
    def __init__(self, parent = None):
        super(inner_widg, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        palette_scope = QPalette()
        palette_scope.setColor(QPalette.Foreground, QColor(75, 75, 75, 255))
        palette_object = QPalette()
        palette_object.setColor(QPalette.Foreground,Qt.black)
        bg_box =  QVBoxLayout(self)


        hbox_lay_format_0 =  QHBoxLayout()
        label_format_0 = QLabel("format")
        label_format_0.setPalette(palette_object)
        label_format_0.setFont(QFont("Monospace"))
        hbox_lay_format_0.addWidget(label_format_0)

        box_format_0 = QComboBox()
        box_format_0.local_path = "format"
        box_format_0.tmp_lst=[]
        box_format_0.tmp_lst.append("mtz")
        box_format_0.tmp_lst.append("nxs")
        box_format_0.tmp_lst.append("mosflm")
        box_format_0.tmp_lst.append("xds")
        for lst_itm in box_format_0.tmp_lst:
            box_format_0.addItem(lst_itm)
        box_format_0.setCurrentIndex(0)
        box_format_0.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_format_0.addWidget(box_format_0)
        bg_box.addLayout(hbox_lay_format_0)


        label_1 = QLabel("mtz")
        label_1.setPalette(palette_scope)
        label_1.setFont(QFont("Monospace"))
        bg_box.addWidget(label_1)

        hbox_lay_ignore_panels_2 =  QHBoxLayout()
        label_ignore_panels_2 = QLabel("    ignore_panels")
        label_ignore_panels_2.setPalette(palette_object)
        label_ignore_panels_2.setFont(QFont("Monospace"))
        hbox_lay_ignore_panels_2.addWidget(label_ignore_panels_2)

        box_ignore_panels_2 = QComboBox()
        box_ignore_panels_2.local_path = "mtz.ignore_panels"
        box_ignore_panels_2.tmp_lst=[]
        box_ignore_panels_2.tmp_lst.append("True")
        box_ignore_panels_2.tmp_lst.append("False")
        for lst_itm in box_ignore_panels_2.tmp_lst:
            box_ignore_panels_2.addItem(lst_itm)
        box_ignore_panels_2.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_ignore_panels_2.addWidget(box_ignore_panels_2)
        bg_box.addLayout(hbox_lay_ignore_panels_2)


        hbox_lay_include_partials_3 =  QHBoxLayout()
        label_include_partials_3 = QLabel("    include_partials")
        label_include_partials_3.setPalette(palette_object)
        label_include_partials_3.setFont(QFont("Monospace"))
        hbox_lay_include_partials_3.addWidget(label_include_partials_3)

        box_include_partials_3 = QComboBox()
        box_include_partials_3.local_path = "mtz.include_partials"
        box_include_partials_3.tmp_lst=[]
        box_include_partials_3.tmp_lst.append("True")
        box_include_partials_3.tmp_lst.append("False")
        for lst_itm in box_include_partials_3.tmp_lst:
            box_include_partials_3.addItem(lst_itm)
        box_include_partials_3.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_include_partials_3.addWidget(box_include_partials_3)
        bg_box.addLayout(hbox_lay_include_partials_3)


        hbox_lay_keep_partials_4 =  QHBoxLayout()
        label_keep_partials_4 = QLabel("    keep_partials")
        label_keep_partials_4.setPalette(palette_object)
        label_keep_partials_4.setFont(QFont("Monospace"))
        hbox_lay_keep_partials_4.addWidget(label_keep_partials_4)

        box_keep_partials_4 = QComboBox()
        box_keep_partials_4.local_path = "mtz.keep_partials"
        box_keep_partials_4.tmp_lst=[]
        box_keep_partials_4.tmp_lst.append("True")
        box_keep_partials_4.tmp_lst.append("False")
        for lst_itm in box_keep_partials_4.tmp_lst:
            box_keep_partials_4.addItem(lst_itm)
        box_keep_partials_4.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_keep_partials_4.addWidget(box_keep_partials_4)
        bg_box.addLayout(hbox_lay_keep_partials_4)


        hbox_lay_min_isigi_5 =  QHBoxLayout()
        label_min_isigi_5 = QLabel("    min_isigi")
        label_min_isigi_5.setPalette(palette_object)
        label_min_isigi_5.setFont(QFont("Monospace"))
        hbox_lay_min_isigi_5.addWidget(label_min_isigi_5)

        box_min_isigi_5 = QDoubleSpinBox()
        box_min_isigi_5.setValue(-5.0)
        box_min_isigi_5.local_path = "mtz.min_isigi"
        box_min_isigi_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_isigi_5.addWidget(box_min_isigi_5)
        bg_box.addLayout(hbox_lay_min_isigi_5)


        hbox_lay_hklout_6 =  QHBoxLayout()
        label_hklout_6 = QLabel("    hklout")
        label_hklout_6.setPalette(palette_object)
        label_hklout_6.setFont(QFont("Monospace"))
        hbox_lay_hklout_6.addWidget(label_hklout_6)

        box_hklout_6 = QLineEdit()
        box_hklout_6.local_path = "mtz.hklout"
        box_hklout_6.textChanged.connect(self.spnbox_changed)
        hbox_lay_hklout_6.addWidget(box_hklout_6)
        bg_box.addLayout(hbox_lay_hklout_6)


        label_7 = QLabel("nxs")
        label_7.setPalette(palette_scope)
        label_7.setFont(QFont("Monospace"))
        bg_box.addWidget(label_7)

        hbox_lay_hklout_8 =  QHBoxLayout()
        label_hklout_8 = QLabel("    hklout")
        label_hklout_8.setPalette(palette_object)
        label_hklout_8.setFont(QFont("Monospace"))
        hbox_lay_hklout_8.addWidget(label_hklout_8)

        box_hklout_8 = QLineEdit()
        box_hklout_8.local_path = "nxs.hklout"
        box_hklout_8.textChanged.connect(self.spnbox_changed)
        hbox_lay_hklout_8.addWidget(box_hklout_8)
        bg_box.addLayout(hbox_lay_hklout_8)


        label_9 = QLabel("mosflm")
        label_9.setPalette(palette_scope)
        label_9.setFont(QFont("Monospace"))
        bg_box.addWidget(label_9)

        hbox_lay_directory_10 =  QHBoxLayout()
        label_directory_10 = QLabel("    directory")
        label_directory_10.setPalette(palette_object)
        label_directory_10.setFont(QFont("Monospace"))
        hbox_lay_directory_10.addWidget(label_directory_10)

        box_directory_10 = QLineEdit()
        box_directory_10.local_path = "mosflm.directory"
        box_directory_10.textChanged.connect(self.spnbox_changed)
        hbox_lay_directory_10.addWidget(box_directory_10)
        bg_box.addLayout(hbox_lay_directory_10)


        label_11 = QLabel("xds")
        label_11.setPalette(palette_scope)
        label_11.setFont(QFont("Monospace"))
        bg_box.addWidget(label_11)

        hbox_lay_directory_12 =  QHBoxLayout()
        label_directory_12 = QLabel("    directory")
        label_directory_12.setPalette(palette_object)
        label_directory_12.setFont(QFont("Monospace"))
        hbox_lay_directory_12.addWidget(label_directory_12)

        box_directory_12 = QLineEdit()
        box_directory_12.local_path = "xds.directory"
        box_directory_12.textChanged.connect(self.spnbox_changed)
        hbox_lay_directory_12.addWidget(box_directory_12)
        bg_box.addLayout(hbox_lay_directory_12)


        label_13 = QLabel("output")
        label_13.setPalette(palette_scope)
        label_13.setFont(QFont("Monospace"))
        bg_box.addWidget(label_13)

        hbox_lay_log_14 =  QHBoxLayout()
        label_log_14 = QLabel("    log")
        label_log_14.setPalette(palette_object)
        label_log_14.setFont(QFont("Monospace"))
        hbox_lay_log_14.addWidget(label_log_14)

        box_log_14 = QLineEdit()
        box_log_14.local_path = "output.log"
        box_log_14.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_14.addWidget(box_log_14)
        bg_box.addLayout(hbox_lay_log_14)


        hbox_lay_debug_log_15 =  QHBoxLayout()
        label_debug_log_15 = QLabel("    debug_log")
        label_debug_log_15.setPalette(palette_object)
        label_debug_log_15.setFont(QFont("Monospace"))
        hbox_lay_debug_log_15.addWidget(label_debug_log_15)

        box_debug_log_15 = QLineEdit()
        box_debug_log_15.local_path = "output.debug_log"
        box_debug_log_15.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_15.addWidget(box_debug_log_15)
        bg_box.addLayout(hbox_lay_debug_log_15)


 
        self.setLayout(bg_box)
        self.show()


    def spnbox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "spnbox_changed to:",
        str_value = str(value)
        print value
        print "local_path =",
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value)
        self.super_parent.update_lin_txt(sender.local_path, value)


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        print "local_path =",
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value)


class ParamMainWidget( QWidget):
    def __init__(self, parent = None):
        super(ParamMainWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog
        self.scrollable_widget = inner_widg(self.super_parent)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.scrollable_widget)
        hbox =  QHBoxLayout()
        hbox.addWidget(scrollArea)
        self.setLayout(hbox)
        self.setWindowTitle('Phil dialog')
        self.show()


    def to_be_caled_from_son_widg(self):
        print "from parent parent_widget"


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = ParamMainWidget()
    sys.exit(app.exec_())
