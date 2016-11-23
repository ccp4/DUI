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
        palette_scope.setColor(QPalette.Foreground, QColor(85, 85, 85, 255))
        palette_object = QPalette()
        palette_object.setColor(QPalette.Foreground,Qt.black)
        bg_box =  QVBoxLayout(self)


        hbox_lay_format_0 =  QHBoxLayout()
        label_format_0 = QLabel("format")
        label_format_0.setPalette(palette_object)
        label_format_0.setFont(QFont("Monospace", 10))
        hbox_lay_format_0.addWidget(label_format_0)

        box_format_0 = QComboBox()
        box_format_0.local_path = "format"
        box_format_0.tmp_lst=[]
        box_format_0.tmp_lst.append("mtz")
        box_format_0.tmp_lst.append("sadabs")
        box_format_0.tmp_lst.append("nxs")
        box_format_0.tmp_lst.append("mosflm")
        box_format_0.tmp_lst.append("xds")
        box_format_0.tmp_lst.append("best")
        box_format_0.tmp_lst.append("xds_ascii")
        for lst_itm in box_format_0.tmp_lst:
            box_format_0.addItem(lst_itm)
        box_format_0.setCurrentIndex(0)
        box_format_0.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_format_0.addWidget(box_format_0)
        bg_box.addLayout(hbox_lay_format_0)

        hbox_lay_summation_1 =  QHBoxLayout()
        label_summation_1 = QLabel("summation")
        label_summation_1.setPalette(palette_object)
        label_summation_1.setFont(QFont("Monospace", 10))
        hbox_lay_summation_1.addWidget(label_summation_1)

        box_summation_1 = QComboBox()
        box_summation_1.local_path = "summation"
        box_summation_1.tmp_lst=[]
        box_summation_1.tmp_lst.append("True")
        box_summation_1.tmp_lst.append("False")
        for lst_itm in box_summation_1.tmp_lst:
            box_summation_1.addItem(lst_itm)
        box_summation_1.setCurrentIndex(1)
        box_summation_1.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_summation_1.addWidget(box_summation_1)
        bg_box.addLayout(hbox_lay_summation_1)

        hbox_lay_debug_2 =  QHBoxLayout()
        label_debug_2 = QLabel("debug")
        label_debug_2.setPalette(palette_object)
        label_debug_2.setFont(QFont("Monospace", 10))
        hbox_lay_debug_2.addWidget(label_debug_2)

        box_debug_2 = QComboBox()
        box_debug_2.local_path = "debug"
        box_debug_2.tmp_lst=[]
        box_debug_2.tmp_lst.append("True")
        box_debug_2.tmp_lst.append("False")
        for lst_itm in box_debug_2.tmp_lst:
            box_debug_2.addItem(lst_itm)
        box_debug_2.setCurrentIndex(1)
        box_debug_2.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_2.addWidget(box_debug_2)
        bg_box.addLayout(hbox_lay_debug_2)

        label_3 = QLabel("mtz")
        label_3.setPalette(palette_scope)
        label_3.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_3)

        hbox_lay_ignore_panels_4 =  QHBoxLayout()
        label_ignore_panels_4 = QLabel("    ignore_panels")
        label_ignore_panels_4.setPalette(palette_object)
        label_ignore_panels_4.setFont(QFont("Monospace", 10))
        hbox_lay_ignore_panels_4.addWidget(label_ignore_panels_4)

        box_ignore_panels_4 = QComboBox()
        box_ignore_panels_4.local_path = "mtz.ignore_panels"
        box_ignore_panels_4.tmp_lst=[]
        box_ignore_panels_4.tmp_lst.append("True")
        box_ignore_panels_4.tmp_lst.append("False")
        for lst_itm in box_ignore_panels_4.tmp_lst:
            box_ignore_panels_4.addItem(lst_itm)
        box_ignore_panels_4.setCurrentIndex(1)
        box_ignore_panels_4.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_ignore_panels_4.addWidget(box_ignore_panels_4)
        bg_box.addLayout(hbox_lay_ignore_panels_4)

        hbox_lay_include_partials_5 =  QHBoxLayout()
        label_include_partials_5 = QLabel("    include_partials")
        label_include_partials_5.setPalette(palette_object)
        label_include_partials_5.setFont(QFont("Monospace", 10))
        hbox_lay_include_partials_5.addWidget(label_include_partials_5)

        box_include_partials_5 = QComboBox()
        box_include_partials_5.local_path = "mtz.include_partials"
        box_include_partials_5.tmp_lst=[]
        box_include_partials_5.tmp_lst.append("True")
        box_include_partials_5.tmp_lst.append("False")
        for lst_itm in box_include_partials_5.tmp_lst:
            box_include_partials_5.addItem(lst_itm)
        box_include_partials_5.setCurrentIndex(1)
        box_include_partials_5.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_include_partials_5.addWidget(box_include_partials_5)
        bg_box.addLayout(hbox_lay_include_partials_5)

        hbox_lay_keep_partials_6 =  QHBoxLayout()
        label_keep_partials_6 = QLabel("    keep_partials")
        label_keep_partials_6.setPalette(palette_object)
        label_keep_partials_6.setFont(QFont("Monospace", 10))
        hbox_lay_keep_partials_6.addWidget(label_keep_partials_6)

        box_keep_partials_6 = QComboBox()
        box_keep_partials_6.local_path = "mtz.keep_partials"
        box_keep_partials_6.tmp_lst=[]
        box_keep_partials_6.tmp_lst.append("True")
        box_keep_partials_6.tmp_lst.append("False")
        for lst_itm in box_keep_partials_6.tmp_lst:
            box_keep_partials_6.addItem(lst_itm)
        box_keep_partials_6.setCurrentIndex(1)
        box_keep_partials_6.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_keep_partials_6.addWidget(box_keep_partials_6)
        bg_box.addLayout(hbox_lay_keep_partials_6)

        hbox_lay_min_isigi_7 =  QHBoxLayout()
        label_min_isigi_7 = QLabel("    min_isigi")
        label_min_isigi_7.setPalette(palette_object)
        label_min_isigi_7.setFont(QFont("Monospace", 10))
        hbox_lay_min_isigi_7.addWidget(label_min_isigi_7)

        box_min_isigi_7 = QDoubleSpinBox()
        box_min_isigi_7.setValue(-5.0)
        box_min_isigi_7.local_path = "mtz.min_isigi"
        box_min_isigi_7.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_isigi_7.addWidget(box_min_isigi_7)
        bg_box.addLayout(hbox_lay_min_isigi_7)

        hbox_lay_force_static_model_8 =  QHBoxLayout()
        label_force_static_model_8 = QLabel("    force_static_model")
        label_force_static_model_8.setPalette(palette_object)
        label_force_static_model_8.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_model_8.addWidget(label_force_static_model_8)

        box_force_static_model_8 = QComboBox()
        box_force_static_model_8.local_path = "mtz.force_static_model"
        box_force_static_model_8.tmp_lst=[]
        box_force_static_model_8.tmp_lst.append("True")
        box_force_static_model_8.tmp_lst.append("False")
        for lst_itm in box_force_static_model_8.tmp_lst:
            box_force_static_model_8.addItem(lst_itm)
        box_force_static_model_8.setCurrentIndex(1)
        box_force_static_model_8.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_model_8.addWidget(box_force_static_model_8)
        bg_box.addLayout(hbox_lay_force_static_model_8)


        label_10 = QLabel("sadabs")
        label_10.setPalette(palette_scope)
        label_10.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_10)


        hbox_lay_run_12 =  QHBoxLayout()
        label_run_12 = QLabel("    run")
        label_run_12.setPalette(palette_object)
        label_run_12.setFont(QFont("Monospace", 10))
        hbox_lay_run_12.addWidget(label_run_12)

        box_run_12 = QSpinBox()
        box_run_12.setValue(1)
        box_run_12.local_path = "sadabs.run"
        box_run_12.valueChanged.connect(self.spnbox_changed)
        hbox_lay_run_12.addWidget(box_run_12)
        bg_box.addLayout(hbox_lay_run_12)

        hbox_lay_predict_13 =  QHBoxLayout()
        label_predict_13 = QLabel("    predict")
        label_predict_13.setPalette(palette_object)
        label_predict_13.setFont(QFont("Monospace", 10))
        hbox_lay_predict_13.addWidget(label_predict_13)

        box_predict_13 = QComboBox()
        box_predict_13.local_path = "sadabs.predict"
        box_predict_13.tmp_lst=[]
        box_predict_13.tmp_lst.append("True")
        box_predict_13.tmp_lst.append("False")
        for lst_itm in box_predict_13.tmp_lst:
            box_predict_13.addItem(lst_itm)
        box_predict_13.setCurrentIndex(1)
        box_predict_13.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_predict_13.addWidget(box_predict_13)
        bg_box.addLayout(hbox_lay_predict_13)

        label_14 = QLabel("xds_ascii")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_14)


        label_16 = QLabel("nxs")
        label_16.setPalette(palette_scope)
        label_16.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_16)


        label_18 = QLabel("mosflm")
        label_18.setPalette(palette_scope)
        label_18.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_18)


        label_20 = QLabel("xds")
        label_20.setPalette(palette_scope)
        label_20.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_20)


        label_22 = QLabel("best")
        label_22.setPalette(palette_scope)
        label_22.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_22)

        hbox_lay_prefix_23 =  QHBoxLayout()
        label_prefix_23 = QLabel("    prefix")
        label_prefix_23.setPalette(palette_object)
        label_prefix_23.setFont(QFont("Monospace", 10))
        hbox_lay_prefix_23.addWidget(label_prefix_23)

        box_prefix_23 = QLineEdit()
        box_prefix_23.local_path = "best.prefix"
        box_prefix_23.textChanged.connect(self.spnbox_changed)
        hbox_lay_prefix_23.addWidget(box_prefix_23)
        bg_box.addLayout(hbox_lay_prefix_23)

        hbox_lay_n_bins_24 =  QHBoxLayout()
        label_n_bins_24 = QLabel("    n_bins")
        label_n_bins_24.setPalette(palette_object)
        label_n_bins_24.setFont(QFont("Monospace", 10))
        hbox_lay_n_bins_24.addWidget(label_n_bins_24)

        box_n_bins_24 = QSpinBox()
        box_n_bins_24.setValue(100)
        box_n_bins_24.local_path = "best.n_bins"
        box_n_bins_24.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_bins_24.addWidget(box_n_bins_24)
        bg_box.addLayout(hbox_lay_n_bins_24)

        label_25 = QLabel("output")
        label_25.setPalette(palette_scope)
        label_25.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_25)



 
        self.setLayout(bg_box)
        self.show()


    def spnbox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "spnbox_changed to:",
        str_value = str(value)
        print value
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = False)


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = False)


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
