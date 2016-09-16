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


        label_0 = QLabel("output")
        label_0.setPalette(palette_scope)
        label_0.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_0)

        hbox_lay_reflections_1 =  QHBoxLayout()
        label_reflections_1 = QLabel("    reflections")
        label_reflections_1.setPalette(palette_object)
        label_reflections_1.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_1.addWidget(label_reflections_1)

        box_reflections_1 = QLineEdit()
        box_reflections_1.local_path = "output.reflections"
        box_reflections_1.textChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_1.addWidget(box_reflections_1)
        bg_box.addLayout(hbox_lay_reflections_1)

        hbox_lay_shoeboxes_2 =  QHBoxLayout()
        label_shoeboxes_2 = QLabel("    shoeboxes")
        label_shoeboxes_2.setPalette(palette_object)
        label_shoeboxes_2.setFont(QFont("Monospace", 10))
        hbox_lay_shoeboxes_2.addWidget(label_shoeboxes_2)

        box_shoeboxes_2 = QComboBox()
        box_shoeboxes_2.local_path = "output.shoeboxes"
        box_shoeboxes_2.tmp_lst=[]
        box_shoeboxes_2.tmp_lst.append("True")
        box_shoeboxes_2.tmp_lst.append("False")
        for lst_itm in box_shoeboxes_2.tmp_lst:
            box_shoeboxes_2.addItem(lst_itm)
        box_shoeboxes_2.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_shoeboxes_2.addWidget(box_shoeboxes_2)
        bg_box.addLayout(hbox_lay_shoeboxes_2)

        hbox_lay_datablock_3 =  QHBoxLayout()
        label_datablock_3 = QLabel("    datablock")
        label_datablock_3.setPalette(palette_object)
        label_datablock_3.setFont(QFont("Monospace", 10))
        hbox_lay_datablock_3.addWidget(label_datablock_3)

        box_datablock_3 = QLineEdit()
        box_datablock_3.local_path = "output.datablock"
        box_datablock_3.textChanged.connect(self.spnbox_changed)
        hbox_lay_datablock_3.addWidget(box_datablock_3)
        bg_box.addLayout(hbox_lay_datablock_3)

        hbox_lay_log_4 =  QHBoxLayout()
        label_log_4 = QLabel("    log")
        label_log_4.setPalette(palette_object)
        label_log_4.setFont(QFont("Monospace", 10))
        hbox_lay_log_4.addWidget(label_log_4)

        box_log_4 = QLineEdit()
        box_log_4.local_path = "output.log"
        box_log_4.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_4.addWidget(box_log_4)
        bg_box.addLayout(hbox_lay_log_4)

        hbox_lay_debug_log_5 =  QHBoxLayout()
        label_debug_log_5 = QLabel("    debug_log")
        label_debug_log_5.setPalette(palette_object)
        label_debug_log_5.setFont(QFont("Monospace", 10))
        hbox_lay_debug_log_5.addWidget(label_debug_log_5)

        box_debug_log_5 = QLineEdit()
        box_debug_log_5.local_path = "output.debug_log"
        box_debug_log_5.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_5.addWidget(box_debug_log_5)
        bg_box.addLayout(hbox_lay_debug_log_5)

        hbox_lay_per_image_statistics_6 =  QHBoxLayout()
        label_per_image_statistics_6 = QLabel("per_image_statistics")
        label_per_image_statistics_6.setPalette(palette_object)
        label_per_image_statistics_6.setFont(QFont("Monospace", 10))
        hbox_lay_per_image_statistics_6.addWidget(label_per_image_statistics_6)

        box_per_image_statistics_6 = QComboBox()
        box_per_image_statistics_6.local_path = "per_image_statistics"
        box_per_image_statistics_6.tmp_lst=[]
        box_per_image_statistics_6.tmp_lst.append("True")
        box_per_image_statistics_6.tmp_lst.append("False")
        for lst_itm in box_per_image_statistics_6.tmp_lst:
            box_per_image_statistics_6.addItem(lst_itm)
        box_per_image_statistics_6.setCurrentIndex(1)
        box_per_image_statistics_6.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_per_image_statistics_6.addWidget(box_per_image_statistics_6)
        bg_box.addLayout(hbox_lay_per_image_statistics_6)

        hbox_lay_verbosity_7 =  QHBoxLayout()
        label_verbosity_7 = QLabel("verbosity")
        label_verbosity_7.setPalette(palette_object)
        label_verbosity_7.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_7.addWidget(label_verbosity_7)

        box_verbosity_7 = QSpinBox()
        box_verbosity_7.setValue(1)
        box_verbosity_7.local_path = "verbosity"
        box_verbosity_7.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_7.addWidget(box_verbosity_7)
        bg_box.addLayout(hbox_lay_verbosity_7)

        label_8 = QLabel("spotfinder")
        label_8.setPalette(palette_scope)
        label_8.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_8)

        label_9 = QLabel("    lookup")
        label_9.setPalette(palette_scope)
        label_9.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_9)

        hbox_lay_mask_10 =  QHBoxLayout()
        label_mask_10 = QLabel("        mask")
        label_mask_10.setPalette(palette_object)
        label_mask_10.setFont(QFont("Monospace", 10))
        hbox_lay_mask_10.addWidget(label_mask_10)

        box_mask_10 = QLineEdit()
        box_mask_10.local_path = "spotfinder.lookup.mask"
        box_mask_10.textChanged.connect(self.spnbox_changed)
        hbox_lay_mask_10.addWidget(box_mask_10)
        bg_box.addLayout(hbox_lay_mask_10)

        hbox_lay_write_hot_mask_11 =  QHBoxLayout()
        label_write_hot_mask_11 = QLabel("    write_hot_mask")
        label_write_hot_mask_11.setPalette(palette_object)
        label_write_hot_mask_11.setFont(QFont("Monospace", 10))
        hbox_lay_write_hot_mask_11.addWidget(label_write_hot_mask_11)

        box_write_hot_mask_11 = QComboBox()
        box_write_hot_mask_11.local_path = "spotfinder.write_hot_mask"
        box_write_hot_mask_11.tmp_lst=[]
        box_write_hot_mask_11.tmp_lst.append("True")
        box_write_hot_mask_11.tmp_lst.append("False")
        for lst_itm in box_write_hot_mask_11.tmp_lst:
            box_write_hot_mask_11.addItem(lst_itm)
        box_write_hot_mask_11.setCurrentIndex(1)
        box_write_hot_mask_11.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_write_hot_mask_11.addWidget(box_write_hot_mask_11)
        bg_box.addLayout(hbox_lay_write_hot_mask_11)

        hbox_lay_force_2d_12 =  QHBoxLayout()
        label_force_2d_12 = QLabel("    force_2d")
        label_force_2d_12.setPalette(palette_object)
        label_force_2d_12.setFont(QFont("Monospace", 10))
        hbox_lay_force_2d_12.addWidget(label_force_2d_12)

        box_force_2d_12 = QComboBox()
        box_force_2d_12.local_path = "spotfinder.force_2d"
        box_force_2d_12.tmp_lst=[]
        box_force_2d_12.tmp_lst.append("True")
        box_force_2d_12.tmp_lst.append("False")
        for lst_itm in box_force_2d_12.tmp_lst:
            box_force_2d_12.addItem(lst_itm)
        box_force_2d_12.setCurrentIndex(1)
        box_force_2d_12.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_2d_12.addWidget(box_force_2d_12)
        bg_box.addLayout(hbox_lay_force_2d_12)

        hbox_lay_scan_range_13_0 =  QHBoxLayout()
        label_scan_range_13_0 = QLabel("    scan_range[1]")
        label_scan_range_13_0.setPalette(palette_object)
        label_scan_range_13_0.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_13_0.addWidget(label_scan_range_13_0)
        box_scan_range_13_0 = QSpinBox()
        box_scan_range_13_0.local_path = "spotfinder.scan_range"
        #box_scan_range_13_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_13_1 =  QHBoxLayout()
        label_scan_range_13_1 = QLabel("    scan_range[2]")
        label_scan_range_13_1.setPalette(palette_object)
        label_scan_range_13_1.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_13_1.addWidget(label_scan_range_13_1)
        box_scan_range_13_1 = QSpinBox()
        box_scan_range_13_1.local_path = "spotfinder.scan_range"
        #box_scan_range_13_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_13_0.addWidget(box_scan_range_13_0)
        bg_box.addLayout(hbox_lay_scan_range_13_0)
        hbox_lay_scan_range_13_1.addWidget(box_scan_range_13_1)
        bg_box.addLayout(hbox_lay_scan_range_13_1)

        hbox_lay_region_of_interest_14_0 =  QHBoxLayout()
        label_region_of_interest_14_0 = QLabel("    region_of_interest[1]")
        label_region_of_interest_14_0.setPalette(palette_object)
        label_region_of_interest_14_0.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_14_0.addWidget(label_region_of_interest_14_0)
        box_region_of_interest_14_0 = QSpinBox()
        box_region_of_interest_14_0.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_14_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_14_1 =  QHBoxLayout()
        label_region_of_interest_14_1 = QLabel("    region_of_interest[2]")
        label_region_of_interest_14_1.setPalette(palette_object)
        label_region_of_interest_14_1.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_14_1.addWidget(label_region_of_interest_14_1)
        box_region_of_interest_14_1 = QSpinBox()
        box_region_of_interest_14_1.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_14_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_14_2 =  QHBoxLayout()
        label_region_of_interest_14_2 = QLabel("    region_of_interest[3]")
        label_region_of_interest_14_2.setPalette(palette_object)
        label_region_of_interest_14_2.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_14_2.addWidget(label_region_of_interest_14_2)
        box_region_of_interest_14_2 = QSpinBox()
        box_region_of_interest_14_2.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_14_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_14_3 =  QHBoxLayout()
        label_region_of_interest_14_3 = QLabel("    region_of_interest[4]")
        label_region_of_interest_14_3.setPalette(palette_object)
        label_region_of_interest_14_3.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_14_3.addWidget(label_region_of_interest_14_3)
        box_region_of_interest_14_3 = QSpinBox()
        box_region_of_interest_14_3.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_14_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_14_0.addWidget(box_region_of_interest_14_0)
        bg_box.addLayout(hbox_lay_region_of_interest_14_0)
        hbox_lay_region_of_interest_14_1.addWidget(box_region_of_interest_14_1)
        bg_box.addLayout(hbox_lay_region_of_interest_14_1)
        hbox_lay_region_of_interest_14_2.addWidget(box_region_of_interest_14_2)
        bg_box.addLayout(hbox_lay_region_of_interest_14_2)
        hbox_lay_region_of_interest_14_3.addWidget(box_region_of_interest_14_3)
        bg_box.addLayout(hbox_lay_region_of_interest_14_3)

        hbox_lay_compute_mean_background_15 =  QHBoxLayout()
        label_compute_mean_background_15 = QLabel("    compute_mean_background")
        label_compute_mean_background_15.setPalette(palette_object)
        label_compute_mean_background_15.setFont(QFont("Monospace", 10))
        hbox_lay_compute_mean_background_15.addWidget(label_compute_mean_background_15)

        box_compute_mean_background_15 = QComboBox()
        box_compute_mean_background_15.local_path = "spotfinder.compute_mean_background"
        box_compute_mean_background_15.tmp_lst=[]
        box_compute_mean_background_15.tmp_lst.append("True")
        box_compute_mean_background_15.tmp_lst.append("False")
        for lst_itm in box_compute_mean_background_15.tmp_lst:
            box_compute_mean_background_15.addItem(lst_itm)
        box_compute_mean_background_15.setCurrentIndex(1)
        box_compute_mean_background_15.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_compute_mean_background_15.addWidget(box_compute_mean_background_15)
        bg_box.addLayout(hbox_lay_compute_mean_background_15)

        label_16 = QLabel("    filter")
        label_16.setPalette(palette_scope)
        label_16.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_16)

        hbox_lay_min_spot_size_17 =  QHBoxLayout()
        label_min_spot_size_17 = QLabel("        min_spot_size")
        label_min_spot_size_17.setPalette(palette_object)
        label_min_spot_size_17.setFont(QFont("Monospace", 10))
        hbox_lay_min_spot_size_17.addWidget(label_min_spot_size_17)

        box_min_spot_size_17 = QSpinBox()
        box_min_spot_size_17.local_path = "spotfinder.filter.min_spot_size"
        box_min_spot_size_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_spot_size_17.addWidget(box_min_spot_size_17)
        bg_box.addLayout(hbox_lay_min_spot_size_17)

        hbox_lay_max_spot_size_18 =  QHBoxLayout()
        label_max_spot_size_18 = QLabel("        max_spot_size")
        label_max_spot_size_18.setPalette(palette_object)
        label_max_spot_size_18.setFont(QFont("Monospace", 10))
        hbox_lay_max_spot_size_18.addWidget(label_max_spot_size_18)

        box_max_spot_size_18 = QSpinBox()
        box_max_spot_size_18.setValue(100)
        box_max_spot_size_18.local_path = "spotfinder.filter.max_spot_size"
        box_max_spot_size_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_spot_size_18.addWidget(box_max_spot_size_18)
        bg_box.addLayout(hbox_lay_max_spot_size_18)

        hbox_lay_max_separation_19 =  QHBoxLayout()
        label_max_separation_19 = QLabel("        max_separation")
        label_max_separation_19.setPalette(palette_object)
        label_max_separation_19.setFont(QFont("Monospace", 10))
        hbox_lay_max_separation_19.addWidget(label_max_separation_19)

        box_max_separation_19 = QDoubleSpinBox()
        box_max_separation_19.setValue(2.0)
        box_max_separation_19.local_path = "spotfinder.filter.max_separation"
        box_max_separation_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_separation_19.addWidget(box_max_separation_19)
        bg_box.addLayout(hbox_lay_max_separation_19)

        hbox_lay_max_strong_pixel_fraction_20 =  QHBoxLayout()
        label_max_strong_pixel_fraction_20 = QLabel("        max_strong_pixel_fraction")
        label_max_strong_pixel_fraction_20.setPalette(palette_object)
        label_max_strong_pixel_fraction_20.setFont(QFont("Monospace", 10))
        hbox_lay_max_strong_pixel_fraction_20.addWidget(label_max_strong_pixel_fraction_20)

        box_max_strong_pixel_fraction_20 = QDoubleSpinBox()
        box_max_strong_pixel_fraction_20.setValue(0.25)
        box_max_strong_pixel_fraction_20.local_path = "spotfinder.filter.max_strong_pixel_fraction"
        box_max_strong_pixel_fraction_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_strong_pixel_fraction_20.addWidget(box_max_strong_pixel_fraction_20)
        bg_box.addLayout(hbox_lay_max_strong_pixel_fraction_20)

        label_21 = QLabel("        background_gradient")
        label_21.setPalette(palette_scope)
        label_21.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_21)

        hbox_lay_filter_22 =  QHBoxLayout()
        label_filter_22 = QLabel("            filter")
        label_filter_22.setPalette(palette_object)
        label_filter_22.setFont(QFont("Monospace", 10))
        hbox_lay_filter_22.addWidget(label_filter_22)

        box_filter_22 = QComboBox()
        box_filter_22.local_path = "spotfinder.filter.background_gradient.filter"
        box_filter_22.tmp_lst=[]
        box_filter_22.tmp_lst.append("True")
        box_filter_22.tmp_lst.append("False")
        for lst_itm in box_filter_22.tmp_lst:
            box_filter_22.addItem(lst_itm)
        box_filter_22.setCurrentIndex(1)
        box_filter_22.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_22.addWidget(box_filter_22)
        bg_box.addLayout(hbox_lay_filter_22)

        hbox_lay_background_size_23 =  QHBoxLayout()
        label_background_size_23 = QLabel("            background_size")
        label_background_size_23.setPalette(palette_object)
        label_background_size_23.setFont(QFont("Monospace", 10))
        hbox_lay_background_size_23.addWidget(label_background_size_23)

        box_background_size_23 = QSpinBox()
        box_background_size_23.setValue(2)
        box_background_size_23.local_path = "spotfinder.filter.background_gradient.background_size"
        box_background_size_23.valueChanged.connect(self.spnbox_changed)
        hbox_lay_background_size_23.addWidget(box_background_size_23)
        bg_box.addLayout(hbox_lay_background_size_23)

        hbox_lay_gradient_cutoff_24 =  QHBoxLayout()
        label_gradient_cutoff_24 = QLabel("            gradient_cutoff")
        label_gradient_cutoff_24.setPalette(palette_object)
        label_gradient_cutoff_24.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_cutoff_24.addWidget(label_gradient_cutoff_24)

        box_gradient_cutoff_24 = QDoubleSpinBox()
        box_gradient_cutoff_24.setValue(4.0)
        box_gradient_cutoff_24.local_path = "spotfinder.filter.background_gradient.gradient_cutoff"
        box_gradient_cutoff_24.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_cutoff_24.addWidget(box_gradient_cutoff_24)
        bg_box.addLayout(hbox_lay_gradient_cutoff_24)

        label_25 = QLabel("        spot_density")
        label_25.setPalette(palette_scope)
        label_25.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_25)

        hbox_lay_filter_26 =  QHBoxLayout()
        label_filter_26 = QLabel("            filter")
        label_filter_26.setPalette(palette_object)
        label_filter_26.setFont(QFont("Monospace", 10))
        hbox_lay_filter_26.addWidget(label_filter_26)

        box_filter_26 = QComboBox()
        box_filter_26.local_path = "spotfinder.filter.spot_density.filter"
        box_filter_26.tmp_lst=[]
        box_filter_26.tmp_lst.append("True")
        box_filter_26.tmp_lst.append("False")
        for lst_itm in box_filter_26.tmp_lst:
            box_filter_26.addItem(lst_itm)
        box_filter_26.setCurrentIndex(1)
        box_filter_26.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_26.addWidget(box_filter_26)
        bg_box.addLayout(hbox_lay_filter_26)

        hbox_lay_border_27 =  QHBoxLayout()
        label_border_27 = QLabel("        border")
        label_border_27.setPalette(palette_object)
        label_border_27.setFont(QFont("Monospace", 10))
        hbox_lay_border_27.addWidget(label_border_27)

        box_border_27 = QSpinBox()
        box_border_27.setValue(0)
        box_border_27.local_path = "spotfinder.filter.border"
        box_border_27.valueChanged.connect(self.spnbox_changed)
        hbox_lay_border_27.addWidget(box_border_27)
        bg_box.addLayout(hbox_lay_border_27)

        hbox_lay_use_trusted_range_28 =  QHBoxLayout()
        label_use_trusted_range_28 = QLabel("        use_trusted_range")
        label_use_trusted_range_28.setPalette(palette_object)
        label_use_trusted_range_28.setFont(QFont("Monospace", 10))
        hbox_lay_use_trusted_range_28.addWidget(label_use_trusted_range_28)

        box_use_trusted_range_28 = QComboBox()
        box_use_trusted_range_28.local_path = "spotfinder.filter.use_trusted_range"
        box_use_trusted_range_28.tmp_lst=[]
        box_use_trusted_range_28.tmp_lst.append("True")
        box_use_trusted_range_28.tmp_lst.append("False")
        for lst_itm in box_use_trusted_range_28.tmp_lst:
            box_use_trusted_range_28.addItem(lst_itm)
        box_use_trusted_range_28.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_use_trusted_range_28.addWidget(box_use_trusted_range_28)
        bg_box.addLayout(hbox_lay_use_trusted_range_28)

        hbox_lay_d_min_29 =  QHBoxLayout()
        label_d_min_29 = QLabel("        d_min")
        label_d_min_29.setPalette(palette_object)
        label_d_min_29.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_29.addWidget(label_d_min_29)

        box_d_min_29 = QDoubleSpinBox()
        box_d_min_29.local_path = "spotfinder.filter.d_min"
        box_d_min_29.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_29.addWidget(box_d_min_29)
        bg_box.addLayout(hbox_lay_d_min_29)

        hbox_lay_d_max_30 =  QHBoxLayout()
        label_d_max_30 = QLabel("        d_max")
        label_d_max_30.setPalette(palette_object)
        label_d_max_30.setFont(QFont("Monospace", 10))
        hbox_lay_d_max_30.addWidget(label_d_max_30)

        box_d_max_30 = QDoubleSpinBox()
        box_d_max_30.local_path = "spotfinder.filter.d_max"
        box_d_max_30.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_30.addWidget(box_d_max_30)
        bg_box.addLayout(hbox_lay_d_max_30)

        hbox_lay_resolution_range_31_0 =  QHBoxLayout()
        label_resolution_range_31_0 = QLabel("        resolution_range[1]")
        label_resolution_range_31_0.setPalette(palette_object)
        label_resolution_range_31_0.setFont(QFont("Monospace", 10))
        hbox_lay_resolution_range_31_0.addWidget(label_resolution_range_31_0)
        box_resolution_range_31_0 = QDoubleSpinBox()
        box_resolution_range_31_0.local_path = "spotfinder.filter.resolution_range"
        #box_resolution_range_31_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_resolution_range_31_1 =  QHBoxLayout()
        label_resolution_range_31_1 = QLabel("        resolution_range[2]")
        label_resolution_range_31_1.setPalette(palette_object)
        label_resolution_range_31_1.setFont(QFont("Monospace", 10))
        hbox_lay_resolution_range_31_1.addWidget(label_resolution_range_31_1)
        box_resolution_range_31_1 = QDoubleSpinBox()
        box_resolution_range_31_1.local_path = "spotfinder.filter.resolution_range"
        #box_resolution_range_31_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_resolution_range_31_0.addWidget(box_resolution_range_31_0)
        bg_box.addLayout(hbox_lay_resolution_range_31_0)
        hbox_lay_resolution_range_31_1.addWidget(box_resolution_range_31_1)
        bg_box.addLayout(hbox_lay_resolution_range_31_1)

        label_32 = QLabel("        untrusted")
        label_32.setPalette(palette_scope)
        label_32.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_32)

        hbox_lay_panel_33 =  QHBoxLayout()
        label_panel_33 = QLabel("            panel")
        label_panel_33.setPalette(palette_object)
        label_panel_33.setFont(QFont("Monospace", 10))
        hbox_lay_panel_33.addWidget(label_panel_33)

        box_panel_33 = QSpinBox()
        box_panel_33.setValue(0)
        box_panel_33.local_path = "spotfinder.filter.untrusted.panel"
        box_panel_33.valueChanged.connect(self.spnbox_changed)
        hbox_lay_panel_33.addWidget(box_panel_33)
        bg_box.addLayout(hbox_lay_panel_33)

        hbox_lay_circle_34_0 =  QHBoxLayout()
        label_circle_34_0 = QLabel("            circle[1]")
        label_circle_34_0.setPalette(palette_object)
        label_circle_34_0.setFont(QFont("Monospace", 10))
        hbox_lay_circle_34_0.addWidget(label_circle_34_0)
        box_circle_34_0 = QSpinBox()
        box_circle_34_0.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_34_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_34_1 =  QHBoxLayout()
        label_circle_34_1 = QLabel("            circle[2]")
        label_circle_34_1.setPalette(palette_object)
        label_circle_34_1.setFont(QFont("Monospace", 10))
        hbox_lay_circle_34_1.addWidget(label_circle_34_1)
        box_circle_34_1 = QSpinBox()
        box_circle_34_1.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_34_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_34_2 =  QHBoxLayout()
        label_circle_34_2 = QLabel("            circle[3]")
        label_circle_34_2.setPalette(palette_object)
        label_circle_34_2.setFont(QFont("Monospace", 10))
        hbox_lay_circle_34_2.addWidget(label_circle_34_2)
        box_circle_34_2 = QSpinBox()
        box_circle_34_2.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_34_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_34_0.addWidget(box_circle_34_0)
        bg_box.addLayout(hbox_lay_circle_34_0)
        hbox_lay_circle_34_1.addWidget(box_circle_34_1)
        bg_box.addLayout(hbox_lay_circle_34_1)
        hbox_lay_circle_34_2.addWidget(box_circle_34_2)
        bg_box.addLayout(hbox_lay_circle_34_2)

        hbox_lay_rectangle_35_0 =  QHBoxLayout()
        label_rectangle_35_0 = QLabel("            rectangle[1]")
        label_rectangle_35_0.setPalette(palette_object)
        label_rectangle_35_0.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_35_0.addWidget(label_rectangle_35_0)
        box_rectangle_35_0 = QSpinBox()
        box_rectangle_35_0.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_35_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_35_1 =  QHBoxLayout()
        label_rectangle_35_1 = QLabel("            rectangle[2]")
        label_rectangle_35_1.setPalette(palette_object)
        label_rectangle_35_1.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_35_1.addWidget(label_rectangle_35_1)
        box_rectangle_35_1 = QSpinBox()
        box_rectangle_35_1.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_35_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_35_2 =  QHBoxLayout()
        label_rectangle_35_2 = QLabel("            rectangle[3]")
        label_rectangle_35_2.setPalette(palette_object)
        label_rectangle_35_2.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_35_2.addWidget(label_rectangle_35_2)
        box_rectangle_35_2 = QSpinBox()
        box_rectangle_35_2.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_35_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_35_3 =  QHBoxLayout()
        label_rectangle_35_3 = QLabel("            rectangle[4]")
        label_rectangle_35_3.setPalette(palette_object)
        label_rectangle_35_3.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_35_3.addWidget(label_rectangle_35_3)
        box_rectangle_35_3 = QSpinBox()
        box_rectangle_35_3.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_35_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_35_0.addWidget(box_rectangle_35_0)
        bg_box.addLayout(hbox_lay_rectangle_35_0)
        hbox_lay_rectangle_35_1.addWidget(box_rectangle_35_1)
        bg_box.addLayout(hbox_lay_rectangle_35_1)
        hbox_lay_rectangle_35_2.addWidget(box_rectangle_35_2)
        bg_box.addLayout(hbox_lay_rectangle_35_2)
        hbox_lay_rectangle_35_3.addWidget(box_rectangle_35_3)
        bg_box.addLayout(hbox_lay_rectangle_35_3)


        label_37 = QLabel("        ice_rings")
        label_37.setPalette(palette_scope)
        label_37.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_37)

        hbox_lay_filter_38 =  QHBoxLayout()
        label_filter_38 = QLabel("            filter")
        label_filter_38.setPalette(palette_object)
        label_filter_38.setFont(QFont("Monospace", 10))
        hbox_lay_filter_38.addWidget(label_filter_38)

        box_filter_38 = QComboBox()
        box_filter_38.local_path = "spotfinder.filter.ice_rings.filter"
        box_filter_38.tmp_lst=[]
        box_filter_38.tmp_lst.append("True")
        box_filter_38.tmp_lst.append("False")
        for lst_itm in box_filter_38.tmp_lst:
            box_filter_38.addItem(lst_itm)
        box_filter_38.setCurrentIndex(1)
        box_filter_38.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_38.addWidget(box_filter_38)
        bg_box.addLayout(hbox_lay_filter_38)



        hbox_lay_width_41 =  QHBoxLayout()
        label_width_41 = QLabel("            width")
        label_width_41.setPalette(palette_object)
        label_width_41.setFont(QFont("Monospace", 10))
        hbox_lay_width_41.addWidget(label_width_41)

        box_width_41 = QDoubleSpinBox()
        box_width_41.setValue(0.06)
        box_width_41.local_path = "spotfinder.filter.ice_rings.width"
        box_width_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_41.addWidget(box_width_41)
        bg_box.addLayout(hbox_lay_width_41)

        hbox_lay_d_min_42 =  QHBoxLayout()
        label_d_min_42 = QLabel("            d_min")
        label_d_min_42.setPalette(palette_object)
        label_d_min_42.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_42.addWidget(label_d_min_42)

        box_d_min_42 = QDoubleSpinBox()
        box_d_min_42.local_path = "spotfinder.filter.ice_rings.d_min"
        box_d_min_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_42.addWidget(box_d_min_42)
        bg_box.addLayout(hbox_lay_d_min_42)

        label_43 = QLabel("    mp")
        label_43.setPalette(palette_scope)
        label_43.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_43)

        hbox_lay_method_44 =  QHBoxLayout()
        label_method_44 = QLabel("        method")
        label_method_44.setPalette(palette_object)
        label_method_44.setFont(QFont("Monospace", 10))
        hbox_lay_method_44.addWidget(label_method_44)

        box_method_44 = QComboBox()
        box_method_44.local_path = "spotfinder.mp.method"
        box_method_44.tmp_lst=[]
        box_method_44.tmp_lst.append("none")
        box_method_44.tmp_lst.append("sge")
        box_method_44.tmp_lst.append("lsf")
        box_method_44.tmp_lst.append("pbs")
        for lst_itm in box_method_44.tmp_lst:
            box_method_44.addItem(lst_itm)
        box_method_44.setCurrentIndex(0)
        box_method_44.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_44.addWidget(box_method_44)
        bg_box.addLayout(hbox_lay_method_44)

        hbox_lay_njobs_45 =  QHBoxLayout()
        label_njobs_45 = QLabel("        njobs")
        label_njobs_45.setPalette(palette_object)
        label_njobs_45.setFont(QFont("Monospace", 10))
        hbox_lay_njobs_45.addWidget(label_njobs_45)

        box_njobs_45 = QSpinBox()
        box_njobs_45.setValue(1)
        box_njobs_45.local_path = "spotfinder.mp.njobs"
        box_njobs_45.valueChanged.connect(self.spnbox_changed)
        hbox_lay_njobs_45.addWidget(box_njobs_45)
        bg_box.addLayout(hbox_lay_njobs_45)

        hbox_lay_nproc_46 =  QHBoxLayout()
        label_nproc_46 = QLabel("        nproc")
        label_nproc_46.setPalette(palette_object)
        label_nproc_46.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_46.addWidget(label_nproc_46)

        box_nproc_46 = QSpinBox()
        box_nproc_46.setValue(1)
        box_nproc_46.local_path = "spotfinder.mp.nproc"
        box_nproc_46.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_46.addWidget(box_nproc_46)
        bg_box.addLayout(hbox_lay_nproc_46)

        hbox_lay_chunksize_47 =  QHBoxLayout()
        label_chunksize_47 = QLabel("        chunksize")
        label_chunksize_47.setPalette(palette_object)
        label_chunksize_47.setFont(QFont("Monospace", 10))
        hbox_lay_chunksize_47.addWidget(label_chunksize_47)

        box_chunksize_47 = QSpinBox()
        box_chunksize_47.local_path = "spotfinder.mp.chunksize"
        box_chunksize_47.valueChanged.connect(self.spnbox_changed)
        hbox_lay_chunksize_47.addWidget(box_chunksize_47)
        bg_box.addLayout(hbox_lay_chunksize_47)

        hbox_lay_min_chunksize_48 =  QHBoxLayout()
        label_min_chunksize_48 = QLabel("        min_chunksize")
        label_min_chunksize_48.setPalette(palette_object)
        label_min_chunksize_48.setFont(QFont("Monospace", 10))
        hbox_lay_min_chunksize_48.addWidget(label_min_chunksize_48)

        box_min_chunksize_48 = QSpinBox()
        box_min_chunksize_48.setValue(20)
        box_min_chunksize_48.local_path = "spotfinder.mp.min_chunksize"
        box_min_chunksize_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_chunksize_48.addWidget(box_min_chunksize_48)
        bg_box.addLayout(hbox_lay_min_chunksize_48)

        label_49 = QLabel("    threshold")
        label_49.setPalette(palette_scope)
        label_49.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_49)

        hbox_lay_algorithm_50 =  QHBoxLayout()
        label_algorithm_50 = QLabel("        algorithm")
        label_algorithm_50.setPalette(palette_object)
        label_algorithm_50.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_50.addWidget(label_algorithm_50)

        box_algorithm_50 = QComboBox()
        box_algorithm_50.local_path = "spotfinder.threshold.algorithm"
        box_algorithm_50.tmp_lst=[]
        box_algorithm_50.tmp_lst.append("xds")
        box_algorithm_50.tmp_lst.append("helen")
        for lst_itm in box_algorithm_50.tmp_lst:
            box_algorithm_50.addItem(lst_itm)
        box_algorithm_50.setCurrentIndex(0)
        box_algorithm_50.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_50.addWidget(box_algorithm_50)
        bg_box.addLayout(hbox_lay_algorithm_50)

        label_51 = QLabel("        xds")
        label_51.setPalette(palette_scope)
        label_51.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_51)

        hbox_lay_gain_52 =  QHBoxLayout()
        label_gain_52 = QLabel("            gain")
        label_gain_52.setPalette(palette_object)
        label_gain_52.setFont(QFont("Monospace", 10))
        hbox_lay_gain_52.addWidget(label_gain_52)

        box_gain_52 = QDoubleSpinBox()
        box_gain_52.local_path = "spotfinder.threshold.xds.gain"
        box_gain_52.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gain_52.addWidget(box_gain_52)
        bg_box.addLayout(hbox_lay_gain_52)

        hbox_lay_kernel_size_53_0 =  QHBoxLayout()
        label_kernel_size_53_0 = QLabel("            kernel_size[1]")
        label_kernel_size_53_0.setPalette(palette_object)
        label_kernel_size_53_0.setFont(QFont("Monospace", 10))
        hbox_lay_kernel_size_53_0.addWidget(label_kernel_size_53_0)
        box_kernel_size_53_0 = QSpinBox()
        box_kernel_size_53_0.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_53_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_53_1 =  QHBoxLayout()
        label_kernel_size_53_1 = QLabel("            kernel_size[2]")
        label_kernel_size_53_1.setPalette(palette_object)
        label_kernel_size_53_1.setFont(QFont("Monospace", 10))
        hbox_lay_kernel_size_53_1.addWidget(label_kernel_size_53_1)
        box_kernel_size_53_1 = QSpinBox()
        box_kernel_size_53_1.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_53_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_53_0.addWidget(box_kernel_size_53_0)
        bg_box.addLayout(hbox_lay_kernel_size_53_0)
        hbox_lay_kernel_size_53_1.addWidget(box_kernel_size_53_1)
        bg_box.addLayout(hbox_lay_kernel_size_53_1)

        hbox_lay_sigma_background_54 =  QHBoxLayout()
        label_sigma_background_54 = QLabel("            sigma_background")
        label_sigma_background_54.setPalette(palette_object)
        label_sigma_background_54.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_background_54.addWidget(label_sigma_background_54)

        box_sigma_background_54 = QDoubleSpinBox()
        box_sigma_background_54.setValue(6.0)
        box_sigma_background_54.local_path = "spotfinder.threshold.xds.sigma_background"
        box_sigma_background_54.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_background_54.addWidget(box_sigma_background_54)
        bg_box.addLayout(hbox_lay_sigma_background_54)

        hbox_lay_sigma_strong_55 =  QHBoxLayout()
        label_sigma_strong_55 = QLabel("            sigma_strong")
        label_sigma_strong_55.setPalette(palette_object)
        label_sigma_strong_55.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_strong_55.addWidget(label_sigma_strong_55)

        box_sigma_strong_55 = QDoubleSpinBox()
        box_sigma_strong_55.setValue(3.0)
        box_sigma_strong_55.local_path = "spotfinder.threshold.xds.sigma_strong"
        box_sigma_strong_55.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_strong_55.addWidget(box_sigma_strong_55)
        bg_box.addLayout(hbox_lay_sigma_strong_55)

        hbox_lay_min_local_56 =  QHBoxLayout()
        label_min_local_56 = QLabel("            min_local")
        label_min_local_56.setPalette(palette_object)
        label_min_local_56.setFont(QFont("Monospace", 10))
        hbox_lay_min_local_56.addWidget(label_min_local_56)

        box_min_local_56 = QSpinBox()
        box_min_local_56.setValue(2)
        box_min_local_56.local_path = "spotfinder.threshold.xds.min_local"
        box_min_local_56.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_local_56.addWidget(box_min_local_56)
        bg_box.addLayout(hbox_lay_min_local_56)

        hbox_lay_global_threshold_57 =  QHBoxLayout()
        label_global_threshold_57 = QLabel("            global_threshold")
        label_global_threshold_57.setPalette(palette_object)
        label_global_threshold_57.setFont(QFont("Monospace", 10))
        hbox_lay_global_threshold_57.addWidget(label_global_threshold_57)

        box_global_threshold_57 = QDoubleSpinBox()
        box_global_threshold_57.setValue(0.0)
        box_global_threshold_57.local_path = "spotfinder.threshold.xds.global_threshold"
        box_global_threshold_57.valueChanged.connect(self.spnbox_changed)
        hbox_lay_global_threshold_57.addWidget(box_global_threshold_57)
        bg_box.addLayout(hbox_lay_global_threshold_57)

        label_58 = QLabel("        helen")
        label_58.setPalette(palette_scope)
        label_58.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_58)

        hbox_lay_exp_spot_dimension_59 =  QHBoxLayout()
        label_exp_spot_dimension_59 = QLabel("            exp_spot_dimension")
        label_exp_spot_dimension_59.setPalette(palette_object)
        label_exp_spot_dimension_59.setFont(QFont("Monospace", 10))
        hbox_lay_exp_spot_dimension_59.addWidget(label_exp_spot_dimension_59)

        box_exp_spot_dimension_59 = QSpinBox()
        box_exp_spot_dimension_59.setValue(3)
        box_exp_spot_dimension_59.local_path = "spotfinder.threshold.helen.exp_spot_dimension"
        box_exp_spot_dimension_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_exp_spot_dimension_59.addWidget(box_exp_spot_dimension_59)
        bg_box.addLayout(hbox_lay_exp_spot_dimension_59)

        hbox_lay_global_threshold_60 =  QHBoxLayout()
        label_global_threshold_60 = QLabel("            global_threshold")
        label_global_threshold_60.setPalette(palette_object)
        label_global_threshold_60.setFont(QFont("Monospace", 10))
        hbox_lay_global_threshold_60.addWidget(label_global_threshold_60)

        box_global_threshold_60 = QDoubleSpinBox()
        box_global_threshold_60.setValue(100.0)
        box_global_threshold_60.local_path = "spotfinder.threshold.helen.global_threshold"
        box_global_threshold_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_global_threshold_60.addWidget(box_global_threshold_60)
        bg_box.addLayout(hbox_lay_global_threshold_60)

        hbox_lay_min_blob_score_61 =  QHBoxLayout()
        label_min_blob_score_61 = QLabel("            min_blob_score")
        label_min_blob_score_61.setPalette(palette_object)
        label_min_blob_score_61.setFont(QFont("Monospace", 10))
        hbox_lay_min_blob_score_61.addWidget(label_min_blob_score_61)

        box_min_blob_score_61 = QDoubleSpinBox()
        box_min_blob_score_61.setValue(0.7)
        box_min_blob_score_61.local_path = "spotfinder.threshold.helen.min_blob_score"
        box_min_blob_score_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_blob_score_61.addWidget(box_min_blob_score_61)
        bg_box.addLayout(hbox_lay_min_blob_score_61)

        hbox_lay_num_passes_62 =  QHBoxLayout()
        label_num_passes_62 = QLabel("            num_passes")
        label_num_passes_62.setPalette(palette_object)
        label_num_passes_62.setFont(QFont("Monospace", 10))
        hbox_lay_num_passes_62.addWidget(label_num_passes_62)

        box_num_passes_62 = QSpinBox()
        box_num_passes_62.setValue(0)
        box_num_passes_62.local_path = "spotfinder.threshold.helen.num_passes"
        box_num_passes_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_num_passes_62.addWidget(box_num_passes_62)
        bg_box.addLayout(hbox_lay_num_passes_62)

        hbox_lay_debug_63 =  QHBoxLayout()
        label_debug_63 = QLabel("            debug")
        label_debug_63.setPalette(palette_object)
        label_debug_63.setFont(QFont("Monospace", 10))
        hbox_lay_debug_63.addWidget(label_debug_63)

        box_debug_63 = QComboBox()
        box_debug_63.local_path = "spotfinder.threshold.helen.debug"
        box_debug_63.tmp_lst=[]
        box_debug_63.tmp_lst.append("True")
        box_debug_63.tmp_lst.append("False")
        for lst_itm in box_debug_63.tmp_lst:
            box_debug_63.addItem(lst_itm)
        box_debug_63.setCurrentIndex(1)
        box_debug_63.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_63.addWidget(box_debug_63)
        bg_box.addLayout(hbox_lay_debug_63)

 
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
