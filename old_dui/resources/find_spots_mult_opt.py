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

        hbox_lay_goniometer_shadow_mask_11 =  QHBoxLayout()
        label_goniometer_shadow_mask_11 = QLabel("    goniometer_shadow_mask")
        label_goniometer_shadow_mask_11.setPalette(palette_object)
        label_goniometer_shadow_mask_11.setFont(QFont("Monospace", 10))
        hbox_lay_goniometer_shadow_mask_11.addWidget(label_goniometer_shadow_mask_11)

        box_goniometer_shadow_mask_11 = QComboBox()
        box_goniometer_shadow_mask_11.local_path = "spotfinder.goniometer_shadow_mask"
        box_goniometer_shadow_mask_11.tmp_lst=[]
        box_goniometer_shadow_mask_11.tmp_lst.append("True")
        box_goniometer_shadow_mask_11.tmp_lst.append("False")
        for lst_itm in box_goniometer_shadow_mask_11.tmp_lst:
            box_goniometer_shadow_mask_11.addItem(lst_itm)
        box_goniometer_shadow_mask_11.setCurrentIndex(1)
        box_goniometer_shadow_mask_11.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_goniometer_shadow_mask_11.addWidget(box_goniometer_shadow_mask_11)
        bg_box.addLayout(hbox_lay_goniometer_shadow_mask_11)

        hbox_lay_write_hot_mask_12 =  QHBoxLayout()
        label_write_hot_mask_12 = QLabel("    write_hot_mask")
        label_write_hot_mask_12.setPalette(palette_object)
        label_write_hot_mask_12.setFont(QFont("Monospace", 10))
        hbox_lay_write_hot_mask_12.addWidget(label_write_hot_mask_12)

        box_write_hot_mask_12 = QComboBox()
        box_write_hot_mask_12.local_path = "spotfinder.write_hot_mask"
        box_write_hot_mask_12.tmp_lst=[]
        box_write_hot_mask_12.tmp_lst.append("True")
        box_write_hot_mask_12.tmp_lst.append("False")
        for lst_itm in box_write_hot_mask_12.tmp_lst:
            box_write_hot_mask_12.addItem(lst_itm)
        box_write_hot_mask_12.setCurrentIndex(1)
        box_write_hot_mask_12.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_write_hot_mask_12.addWidget(box_write_hot_mask_12)
        bg_box.addLayout(hbox_lay_write_hot_mask_12)

        hbox_lay_force_2d_13 =  QHBoxLayout()
        label_force_2d_13 = QLabel("    force_2d")
        label_force_2d_13.setPalette(palette_object)
        label_force_2d_13.setFont(QFont("Monospace", 10))
        hbox_lay_force_2d_13.addWidget(label_force_2d_13)

        box_force_2d_13 = QComboBox()
        box_force_2d_13.local_path = "spotfinder.force_2d"
        box_force_2d_13.tmp_lst=[]
        box_force_2d_13.tmp_lst.append("True")
        box_force_2d_13.tmp_lst.append("False")
        for lst_itm in box_force_2d_13.tmp_lst:
            box_force_2d_13.addItem(lst_itm)
        box_force_2d_13.setCurrentIndex(1)
        box_force_2d_13.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_2d_13.addWidget(box_force_2d_13)
        bg_box.addLayout(hbox_lay_force_2d_13)

        hbox_lay_scan_range_14_0 =  QHBoxLayout()
        label_scan_range_14_0 = QLabel("    scan_range[1]")
        label_scan_range_14_0.setPalette(palette_object)
        label_scan_range_14_0.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_14_0.addWidget(label_scan_range_14_0)
        box_scan_range_14_0 = QSpinBox()
        box_scan_range_14_0.local_path = "spotfinder.scan_range"
        #box_scan_range_14_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_14_1 =  QHBoxLayout()
        label_scan_range_14_1 = QLabel("    scan_range[2]")
        label_scan_range_14_1.setPalette(palette_object)
        label_scan_range_14_1.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_14_1.addWidget(label_scan_range_14_1)
        box_scan_range_14_1 = QSpinBox()
        box_scan_range_14_1.local_path = "spotfinder.scan_range"
        #box_scan_range_14_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_14_0.addWidget(box_scan_range_14_0)
        bg_box.addLayout(hbox_lay_scan_range_14_0)
        hbox_lay_scan_range_14_1.addWidget(box_scan_range_14_1)
        bg_box.addLayout(hbox_lay_scan_range_14_1)

        hbox_lay_region_of_interest_15_0 =  QHBoxLayout()
        label_region_of_interest_15_0 = QLabel("    region_of_interest[1]")
        label_region_of_interest_15_0.setPalette(palette_object)
        label_region_of_interest_15_0.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_15_0.addWidget(label_region_of_interest_15_0)
        box_region_of_interest_15_0 = QSpinBox()
        box_region_of_interest_15_0.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_15_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_15_1 =  QHBoxLayout()
        label_region_of_interest_15_1 = QLabel("    region_of_interest[2]")
        label_region_of_interest_15_1.setPalette(palette_object)
        label_region_of_interest_15_1.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_15_1.addWidget(label_region_of_interest_15_1)
        box_region_of_interest_15_1 = QSpinBox()
        box_region_of_interest_15_1.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_15_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_15_2 =  QHBoxLayout()
        label_region_of_interest_15_2 = QLabel("    region_of_interest[3]")
        label_region_of_interest_15_2.setPalette(palette_object)
        label_region_of_interest_15_2.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_15_2.addWidget(label_region_of_interest_15_2)
        box_region_of_interest_15_2 = QSpinBox()
        box_region_of_interest_15_2.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_15_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_15_3 =  QHBoxLayout()
        label_region_of_interest_15_3 = QLabel("    region_of_interest[4]")
        label_region_of_interest_15_3.setPalette(palette_object)
        label_region_of_interest_15_3.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_15_3.addWidget(label_region_of_interest_15_3)
        box_region_of_interest_15_3 = QSpinBox()
        box_region_of_interest_15_3.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_15_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_15_0.addWidget(box_region_of_interest_15_0)
        bg_box.addLayout(hbox_lay_region_of_interest_15_0)
        hbox_lay_region_of_interest_15_1.addWidget(box_region_of_interest_15_1)
        bg_box.addLayout(hbox_lay_region_of_interest_15_1)
        hbox_lay_region_of_interest_15_2.addWidget(box_region_of_interest_15_2)
        bg_box.addLayout(hbox_lay_region_of_interest_15_2)
        hbox_lay_region_of_interest_15_3.addWidget(box_region_of_interest_15_3)
        bg_box.addLayout(hbox_lay_region_of_interest_15_3)

        hbox_lay_compute_mean_background_16 =  QHBoxLayout()
        label_compute_mean_background_16 = QLabel("    compute_mean_background")
        label_compute_mean_background_16.setPalette(palette_object)
        label_compute_mean_background_16.setFont(QFont("Monospace", 10))
        hbox_lay_compute_mean_background_16.addWidget(label_compute_mean_background_16)

        box_compute_mean_background_16 = QComboBox()
        box_compute_mean_background_16.local_path = "spotfinder.compute_mean_background"
        box_compute_mean_background_16.tmp_lst=[]
        box_compute_mean_background_16.tmp_lst.append("True")
        box_compute_mean_background_16.tmp_lst.append("False")
        for lst_itm in box_compute_mean_background_16.tmp_lst:
            box_compute_mean_background_16.addItem(lst_itm)
        box_compute_mean_background_16.setCurrentIndex(1)
        box_compute_mean_background_16.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_compute_mean_background_16.addWidget(box_compute_mean_background_16)
        bg_box.addLayout(hbox_lay_compute_mean_background_16)

        label_17 = QLabel("    filter")
        label_17.setPalette(palette_scope)
        label_17.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_17)

        hbox_lay_min_spot_size_18 =  QHBoxLayout()
        label_min_spot_size_18 = QLabel("        min_spot_size")
        label_min_spot_size_18.setPalette(palette_object)
        label_min_spot_size_18.setFont(QFont("Monospace", 10))
        hbox_lay_min_spot_size_18.addWidget(label_min_spot_size_18)

        box_min_spot_size_18 = QSpinBox()
        box_min_spot_size_18.local_path = "spotfinder.filter.min_spot_size"
        box_min_spot_size_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_spot_size_18.addWidget(box_min_spot_size_18)
        bg_box.addLayout(hbox_lay_min_spot_size_18)

        hbox_lay_max_spot_size_19 =  QHBoxLayout()
        label_max_spot_size_19 = QLabel("        max_spot_size")
        label_max_spot_size_19.setPalette(palette_object)
        label_max_spot_size_19.setFont(QFont("Monospace", 10))
        hbox_lay_max_spot_size_19.addWidget(label_max_spot_size_19)

        box_max_spot_size_19 = QSpinBox()
        box_max_spot_size_19.setValue(100)
        box_max_spot_size_19.local_path = "spotfinder.filter.max_spot_size"
        box_max_spot_size_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_spot_size_19.addWidget(box_max_spot_size_19)
        bg_box.addLayout(hbox_lay_max_spot_size_19)

        hbox_lay_max_separation_20 =  QHBoxLayout()
        label_max_separation_20 = QLabel("        max_separation")
        label_max_separation_20.setPalette(palette_object)
        label_max_separation_20.setFont(QFont("Monospace", 10))
        hbox_lay_max_separation_20.addWidget(label_max_separation_20)

        box_max_separation_20 = QDoubleSpinBox()
        box_max_separation_20.setValue(2.0)
        box_max_separation_20.local_path = "spotfinder.filter.max_separation"
        box_max_separation_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_separation_20.addWidget(box_max_separation_20)
        bg_box.addLayout(hbox_lay_max_separation_20)

        hbox_lay_max_strong_pixel_fraction_21 =  QHBoxLayout()
        label_max_strong_pixel_fraction_21 = QLabel("        max_strong_pixel_fraction")
        label_max_strong_pixel_fraction_21.setPalette(palette_object)
        label_max_strong_pixel_fraction_21.setFont(QFont("Monospace", 10))
        hbox_lay_max_strong_pixel_fraction_21.addWidget(label_max_strong_pixel_fraction_21)

        box_max_strong_pixel_fraction_21 = QDoubleSpinBox()
        box_max_strong_pixel_fraction_21.setValue(0.25)
        box_max_strong_pixel_fraction_21.local_path = "spotfinder.filter.max_strong_pixel_fraction"
        box_max_strong_pixel_fraction_21.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_strong_pixel_fraction_21.addWidget(box_max_strong_pixel_fraction_21)
        bg_box.addLayout(hbox_lay_max_strong_pixel_fraction_21)

        label_22 = QLabel("        background_gradient")
        label_22.setPalette(palette_scope)
        label_22.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_22)

        hbox_lay_filter_23 =  QHBoxLayout()
        label_filter_23 = QLabel("            filter")
        label_filter_23.setPalette(palette_object)
        label_filter_23.setFont(QFont("Monospace", 10))
        hbox_lay_filter_23.addWidget(label_filter_23)

        box_filter_23 = QComboBox()
        box_filter_23.local_path = "spotfinder.filter.background_gradient.filter"
        box_filter_23.tmp_lst=[]
        box_filter_23.tmp_lst.append("True")
        box_filter_23.tmp_lst.append("False")
        for lst_itm in box_filter_23.tmp_lst:
            box_filter_23.addItem(lst_itm)
        box_filter_23.setCurrentIndex(1)
        box_filter_23.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_23.addWidget(box_filter_23)
        bg_box.addLayout(hbox_lay_filter_23)

        hbox_lay_background_size_24 =  QHBoxLayout()
        label_background_size_24 = QLabel("            background_size")
        label_background_size_24.setPalette(palette_object)
        label_background_size_24.setFont(QFont("Monospace", 10))
        hbox_lay_background_size_24.addWidget(label_background_size_24)

        box_background_size_24 = QSpinBox()
        box_background_size_24.setValue(2)
        box_background_size_24.local_path = "spotfinder.filter.background_gradient.background_size"
        box_background_size_24.valueChanged.connect(self.spnbox_changed)
        hbox_lay_background_size_24.addWidget(box_background_size_24)
        bg_box.addLayout(hbox_lay_background_size_24)

        hbox_lay_gradient_cutoff_25 =  QHBoxLayout()
        label_gradient_cutoff_25 = QLabel("            gradient_cutoff")
        label_gradient_cutoff_25.setPalette(palette_object)
        label_gradient_cutoff_25.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_cutoff_25.addWidget(label_gradient_cutoff_25)

        box_gradient_cutoff_25 = QDoubleSpinBox()
        box_gradient_cutoff_25.setValue(4.0)
        box_gradient_cutoff_25.local_path = "spotfinder.filter.background_gradient.gradient_cutoff"
        box_gradient_cutoff_25.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_cutoff_25.addWidget(box_gradient_cutoff_25)
        bg_box.addLayout(hbox_lay_gradient_cutoff_25)

        label_26 = QLabel("        spot_density")
        label_26.setPalette(palette_scope)
        label_26.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_26)

        hbox_lay_filter_27 =  QHBoxLayout()
        label_filter_27 = QLabel("            filter")
        label_filter_27.setPalette(palette_object)
        label_filter_27.setFont(QFont("Monospace", 10))
        hbox_lay_filter_27.addWidget(label_filter_27)

        box_filter_27 = QComboBox()
        box_filter_27.local_path = "spotfinder.filter.spot_density.filter"
        box_filter_27.tmp_lst=[]
        box_filter_27.tmp_lst.append("True")
        box_filter_27.tmp_lst.append("False")
        for lst_itm in box_filter_27.tmp_lst:
            box_filter_27.addItem(lst_itm)
        box_filter_27.setCurrentIndex(1)
        box_filter_27.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_27.addWidget(box_filter_27)
        bg_box.addLayout(hbox_lay_filter_27)

        hbox_lay_border_28 =  QHBoxLayout()
        label_border_28 = QLabel("        border")
        label_border_28.setPalette(palette_object)
        label_border_28.setFont(QFont("Monospace", 10))
        hbox_lay_border_28.addWidget(label_border_28)

        box_border_28 = QSpinBox()
        box_border_28.setValue(0)
        box_border_28.local_path = "spotfinder.filter.border"
        box_border_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_border_28.addWidget(box_border_28)
        bg_box.addLayout(hbox_lay_border_28)

        hbox_lay_use_trusted_range_29 =  QHBoxLayout()
        label_use_trusted_range_29 = QLabel("        use_trusted_range")
        label_use_trusted_range_29.setPalette(palette_object)
        label_use_trusted_range_29.setFont(QFont("Monospace", 10))
        hbox_lay_use_trusted_range_29.addWidget(label_use_trusted_range_29)

        box_use_trusted_range_29 = QComboBox()
        box_use_trusted_range_29.local_path = "spotfinder.filter.use_trusted_range"
        box_use_trusted_range_29.tmp_lst=[]
        box_use_trusted_range_29.tmp_lst.append("True")
        box_use_trusted_range_29.tmp_lst.append("False")
        for lst_itm in box_use_trusted_range_29.tmp_lst:
            box_use_trusted_range_29.addItem(lst_itm)
        box_use_trusted_range_29.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_use_trusted_range_29.addWidget(box_use_trusted_range_29)
        bg_box.addLayout(hbox_lay_use_trusted_range_29)

        hbox_lay_d_min_30 =  QHBoxLayout()
        label_d_min_30 = QLabel("        d_min")
        label_d_min_30.setPalette(palette_object)
        label_d_min_30.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_30.addWidget(label_d_min_30)

        box_d_min_30 = QDoubleSpinBox()
        box_d_min_30.local_path = "spotfinder.filter.d_min"
        box_d_min_30.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_30.addWidget(box_d_min_30)
        bg_box.addLayout(hbox_lay_d_min_30)

        hbox_lay_d_max_31 =  QHBoxLayout()
        label_d_max_31 = QLabel("        d_max")
        label_d_max_31.setPalette(palette_object)
        label_d_max_31.setFont(QFont("Monospace", 10))
        hbox_lay_d_max_31.addWidget(label_d_max_31)

        box_d_max_31 = QDoubleSpinBox()
        box_d_max_31.local_path = "spotfinder.filter.d_max"
        box_d_max_31.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_31.addWidget(box_d_max_31)
        bg_box.addLayout(hbox_lay_d_max_31)

        hbox_lay_resolution_range_32_0 =  QHBoxLayout()
        label_resolution_range_32_0 = QLabel("        resolution_range[1]")
        label_resolution_range_32_0.setPalette(palette_object)
        label_resolution_range_32_0.setFont(QFont("Monospace", 10))
        hbox_lay_resolution_range_32_0.addWidget(label_resolution_range_32_0)
        box_resolution_range_32_0 = QDoubleSpinBox()
        box_resolution_range_32_0.local_path = "spotfinder.filter.resolution_range"
        #box_resolution_range_32_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_resolution_range_32_1 =  QHBoxLayout()
        label_resolution_range_32_1 = QLabel("        resolution_range[2]")
        label_resolution_range_32_1.setPalette(palette_object)
        label_resolution_range_32_1.setFont(QFont("Monospace", 10))
        hbox_lay_resolution_range_32_1.addWidget(label_resolution_range_32_1)
        box_resolution_range_32_1 = QDoubleSpinBox()
        box_resolution_range_32_1.local_path = "spotfinder.filter.resolution_range"
        #box_resolution_range_32_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_resolution_range_32_0.addWidget(box_resolution_range_32_0)
        bg_box.addLayout(hbox_lay_resolution_range_32_0)
        hbox_lay_resolution_range_32_1.addWidget(box_resolution_range_32_1)
        bg_box.addLayout(hbox_lay_resolution_range_32_1)

        label_33 = QLabel("        untrusted")
        label_33.setPalette(palette_scope)
        label_33.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_33)

        hbox_lay_panel_34 =  QHBoxLayout()
        label_panel_34 = QLabel("            panel")
        label_panel_34.setPalette(palette_object)
        label_panel_34.setFont(QFont("Monospace", 10))
        hbox_lay_panel_34.addWidget(label_panel_34)

        box_panel_34 = QSpinBox()
        box_panel_34.setValue(0)
        box_panel_34.local_path = "spotfinder.filter.untrusted.panel"
        box_panel_34.valueChanged.connect(self.spnbox_changed)
        hbox_lay_panel_34.addWidget(box_panel_34)
        bg_box.addLayout(hbox_lay_panel_34)

        hbox_lay_circle_35_0 =  QHBoxLayout()
        label_circle_35_0 = QLabel("            circle[1]")
        label_circle_35_0.setPalette(palette_object)
        label_circle_35_0.setFont(QFont("Monospace", 10))
        hbox_lay_circle_35_0.addWidget(label_circle_35_0)
        box_circle_35_0 = QSpinBox()
        box_circle_35_0.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_35_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_35_1 =  QHBoxLayout()
        label_circle_35_1 = QLabel("            circle[2]")
        label_circle_35_1.setPalette(palette_object)
        label_circle_35_1.setFont(QFont("Monospace", 10))
        hbox_lay_circle_35_1.addWidget(label_circle_35_1)
        box_circle_35_1 = QSpinBox()
        box_circle_35_1.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_35_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_35_2 =  QHBoxLayout()
        label_circle_35_2 = QLabel("            circle[3]")
        label_circle_35_2.setPalette(palette_object)
        label_circle_35_2.setFont(QFont("Monospace", 10))
        hbox_lay_circle_35_2.addWidget(label_circle_35_2)
        box_circle_35_2 = QSpinBox()
        box_circle_35_2.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_35_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_35_0.addWidget(box_circle_35_0)
        bg_box.addLayout(hbox_lay_circle_35_0)
        hbox_lay_circle_35_1.addWidget(box_circle_35_1)
        bg_box.addLayout(hbox_lay_circle_35_1)
        hbox_lay_circle_35_2.addWidget(box_circle_35_2)
        bg_box.addLayout(hbox_lay_circle_35_2)

        hbox_lay_rectangle_36_0 =  QHBoxLayout()
        label_rectangle_36_0 = QLabel("            rectangle[1]")
        label_rectangle_36_0.setPalette(palette_object)
        label_rectangle_36_0.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_36_0.addWidget(label_rectangle_36_0)
        box_rectangle_36_0 = QSpinBox()
        box_rectangle_36_0.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_36_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_36_1 =  QHBoxLayout()
        label_rectangle_36_1 = QLabel("            rectangle[2]")
        label_rectangle_36_1.setPalette(palette_object)
        label_rectangle_36_1.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_36_1.addWidget(label_rectangle_36_1)
        box_rectangle_36_1 = QSpinBox()
        box_rectangle_36_1.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_36_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_36_2 =  QHBoxLayout()
        label_rectangle_36_2 = QLabel("            rectangle[3]")
        label_rectangle_36_2.setPalette(palette_object)
        label_rectangle_36_2.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_36_2.addWidget(label_rectangle_36_2)
        box_rectangle_36_2 = QSpinBox()
        box_rectangle_36_2.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_36_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_36_3 =  QHBoxLayout()
        label_rectangle_36_3 = QLabel("            rectangle[4]")
        label_rectangle_36_3.setPalette(palette_object)
        label_rectangle_36_3.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_36_3.addWidget(label_rectangle_36_3)
        box_rectangle_36_3 = QSpinBox()
        box_rectangle_36_3.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_36_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_36_0.addWidget(box_rectangle_36_0)
        bg_box.addLayout(hbox_lay_rectangle_36_0)
        hbox_lay_rectangle_36_1.addWidget(box_rectangle_36_1)
        bg_box.addLayout(hbox_lay_rectangle_36_1)
        hbox_lay_rectangle_36_2.addWidget(box_rectangle_36_2)
        bg_box.addLayout(hbox_lay_rectangle_36_2)
        hbox_lay_rectangle_36_3.addWidget(box_rectangle_36_3)
        bg_box.addLayout(hbox_lay_rectangle_36_3)


        label_38 = QLabel("        ice_rings")
        label_38.setPalette(palette_scope)
        label_38.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_38)

        hbox_lay_filter_39 =  QHBoxLayout()
        label_filter_39 = QLabel("            filter")
        label_filter_39.setPalette(palette_object)
        label_filter_39.setFont(QFont("Monospace", 10))
        hbox_lay_filter_39.addWidget(label_filter_39)

        box_filter_39 = QComboBox()
        box_filter_39.local_path = "spotfinder.filter.ice_rings.filter"
        box_filter_39.tmp_lst=[]
        box_filter_39.tmp_lst.append("True")
        box_filter_39.tmp_lst.append("False")
        for lst_itm in box_filter_39.tmp_lst:
            box_filter_39.addItem(lst_itm)
        box_filter_39.setCurrentIndex(1)
        box_filter_39.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_39.addWidget(box_filter_39)
        bg_box.addLayout(hbox_lay_filter_39)



        hbox_lay_width_42 =  QHBoxLayout()
        label_width_42 = QLabel("            width")
        label_width_42.setPalette(palette_object)
        label_width_42.setFont(QFont("Monospace", 10))
        hbox_lay_width_42.addWidget(label_width_42)

        box_width_42 = QDoubleSpinBox()
        box_width_42.setValue(0.06)
        box_width_42.local_path = "spotfinder.filter.ice_rings.width"
        box_width_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_42.addWidget(box_width_42)
        bg_box.addLayout(hbox_lay_width_42)

        hbox_lay_d_min_43 =  QHBoxLayout()
        label_d_min_43 = QLabel("            d_min")
        label_d_min_43.setPalette(palette_object)
        label_d_min_43.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_43.addWidget(label_d_min_43)

        box_d_min_43 = QDoubleSpinBox()
        box_d_min_43.local_path = "spotfinder.filter.ice_rings.d_min"
        box_d_min_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_43.addWidget(box_d_min_43)
        bg_box.addLayout(hbox_lay_d_min_43)

        label_44 = QLabel("    mp")
        label_44.setPalette(palette_scope)
        label_44.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_44)

        hbox_lay_method_45 =  QHBoxLayout()
        label_method_45 = QLabel("        method")
        label_method_45.setPalette(palette_object)
        label_method_45.setFont(QFont("Monospace", 10))
        hbox_lay_method_45.addWidget(label_method_45)

        box_method_45 = QComboBox()
        box_method_45.local_path = "spotfinder.mp.method"
        box_method_45.tmp_lst=[]
        box_method_45.tmp_lst.append("none")
        box_method_45.tmp_lst.append("sge")
        box_method_45.tmp_lst.append("lsf")
        box_method_45.tmp_lst.append("pbs")
        for lst_itm in box_method_45.tmp_lst:
            box_method_45.addItem(lst_itm)
        box_method_45.setCurrentIndex(0)
        box_method_45.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_45.addWidget(box_method_45)
        bg_box.addLayout(hbox_lay_method_45)

        hbox_lay_njobs_46 =  QHBoxLayout()
        label_njobs_46 = QLabel("        njobs")
        label_njobs_46.setPalette(palette_object)
        label_njobs_46.setFont(QFont("Monospace", 10))
        hbox_lay_njobs_46.addWidget(label_njobs_46)

        box_njobs_46 = QSpinBox()
        box_njobs_46.setValue(1)
        box_njobs_46.local_path = "spotfinder.mp.njobs"
        box_njobs_46.valueChanged.connect(self.spnbox_changed)
        hbox_lay_njobs_46.addWidget(box_njobs_46)
        bg_box.addLayout(hbox_lay_njobs_46)

        hbox_lay_nproc_47 =  QHBoxLayout()
        label_nproc_47 = QLabel("        nproc")
        label_nproc_47.setPalette(palette_object)
        label_nproc_47.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_47.addWidget(label_nproc_47)

        box_nproc_47 = QSpinBox()
        box_nproc_47.setValue(1)
        box_nproc_47.local_path = "spotfinder.mp.nproc"
        box_nproc_47.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_47.addWidget(box_nproc_47)
        bg_box.addLayout(hbox_lay_nproc_47)

        hbox_lay_chunksize_48 =  QHBoxLayout()
        label_chunksize_48 = QLabel("        chunksize")
        label_chunksize_48.setPalette(palette_object)
        label_chunksize_48.setFont(QFont("Monospace", 10))
        hbox_lay_chunksize_48.addWidget(label_chunksize_48)

        box_chunksize_48 = QSpinBox()
        box_chunksize_48.local_path = "spotfinder.mp.chunksize"
        box_chunksize_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_chunksize_48.addWidget(box_chunksize_48)
        bg_box.addLayout(hbox_lay_chunksize_48)

        hbox_lay_min_chunksize_49 =  QHBoxLayout()
        label_min_chunksize_49 = QLabel("        min_chunksize")
        label_min_chunksize_49.setPalette(palette_object)
        label_min_chunksize_49.setFont(QFont("Monospace", 10))
        hbox_lay_min_chunksize_49.addWidget(label_min_chunksize_49)

        box_min_chunksize_49 = QSpinBox()
        box_min_chunksize_49.setValue(20)
        box_min_chunksize_49.local_path = "spotfinder.mp.min_chunksize"
        box_min_chunksize_49.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_chunksize_49.addWidget(box_min_chunksize_49)
        bg_box.addLayout(hbox_lay_min_chunksize_49)

        label_50 = QLabel("    threshold")
        label_50.setPalette(palette_scope)
        label_50.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_50)

        hbox_lay_algorithm_51 =  QHBoxLayout()
        label_algorithm_51 = QLabel("        algorithm")
        label_algorithm_51.setPalette(palette_object)
        label_algorithm_51.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_51.addWidget(label_algorithm_51)

        box_algorithm_51 = QComboBox()
        box_algorithm_51.local_path = "spotfinder.threshold.algorithm"
        box_algorithm_51.tmp_lst=[]
        box_algorithm_51.tmp_lst.append("xds")
        box_algorithm_51.tmp_lst.append("helen")
        for lst_itm in box_algorithm_51.tmp_lst:
            box_algorithm_51.addItem(lst_itm)
        box_algorithm_51.setCurrentIndex(0)
        box_algorithm_51.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_51.addWidget(box_algorithm_51)
        bg_box.addLayout(hbox_lay_algorithm_51)

        label_52 = QLabel("        xds")
        label_52.setPalette(palette_scope)
        label_52.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_52)

        hbox_lay_gain_53 =  QHBoxLayout()
        label_gain_53 = QLabel("            gain")
        label_gain_53.setPalette(palette_object)
        label_gain_53.setFont(QFont("Monospace", 10))
        hbox_lay_gain_53.addWidget(label_gain_53)

        box_gain_53 = QDoubleSpinBox()
        box_gain_53.local_path = "spotfinder.threshold.xds.gain"
        box_gain_53.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gain_53.addWidget(box_gain_53)
        bg_box.addLayout(hbox_lay_gain_53)

        hbox_lay_kernel_size_54_0 =  QHBoxLayout()
        label_kernel_size_54_0 = QLabel("            kernel_size[1]")
        label_kernel_size_54_0.setPalette(palette_object)
        label_kernel_size_54_0.setFont(QFont("Monospace", 10))
        hbox_lay_kernel_size_54_0.addWidget(label_kernel_size_54_0)
        box_kernel_size_54_0 = QSpinBox()
        box_kernel_size_54_0.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_54_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_54_1 =  QHBoxLayout()
        label_kernel_size_54_1 = QLabel("            kernel_size[2]")
        label_kernel_size_54_1.setPalette(palette_object)
        label_kernel_size_54_1.setFont(QFont("Monospace", 10))
        hbox_lay_kernel_size_54_1.addWidget(label_kernel_size_54_1)
        box_kernel_size_54_1 = QSpinBox()
        box_kernel_size_54_1.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_54_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_54_0.addWidget(box_kernel_size_54_0)
        bg_box.addLayout(hbox_lay_kernel_size_54_0)
        hbox_lay_kernel_size_54_1.addWidget(box_kernel_size_54_1)
        bg_box.addLayout(hbox_lay_kernel_size_54_1)

        hbox_lay_sigma_background_55 =  QHBoxLayout()
        label_sigma_background_55 = QLabel("            sigma_background")
        label_sigma_background_55.setPalette(palette_object)
        label_sigma_background_55.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_background_55.addWidget(label_sigma_background_55)

        box_sigma_background_55 = QDoubleSpinBox()
        box_sigma_background_55.setValue(6.0)
        box_sigma_background_55.local_path = "spotfinder.threshold.xds.sigma_background"
        box_sigma_background_55.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_background_55.addWidget(box_sigma_background_55)
        bg_box.addLayout(hbox_lay_sigma_background_55)

        hbox_lay_sigma_strong_56 =  QHBoxLayout()
        label_sigma_strong_56 = QLabel("            sigma_strong")
        label_sigma_strong_56.setPalette(palette_object)
        label_sigma_strong_56.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_strong_56.addWidget(label_sigma_strong_56)

        box_sigma_strong_56 = QDoubleSpinBox()
        box_sigma_strong_56.setValue(3.0)
        box_sigma_strong_56.local_path = "spotfinder.threshold.xds.sigma_strong"
        box_sigma_strong_56.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_strong_56.addWidget(box_sigma_strong_56)
        bg_box.addLayout(hbox_lay_sigma_strong_56)

        hbox_lay_min_local_57 =  QHBoxLayout()
        label_min_local_57 = QLabel("            min_local")
        label_min_local_57.setPalette(palette_object)
        label_min_local_57.setFont(QFont("Monospace", 10))
        hbox_lay_min_local_57.addWidget(label_min_local_57)

        box_min_local_57 = QSpinBox()
        box_min_local_57.setValue(2)
        box_min_local_57.local_path = "spotfinder.threshold.xds.min_local"
        box_min_local_57.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_local_57.addWidget(box_min_local_57)
        bg_box.addLayout(hbox_lay_min_local_57)

        hbox_lay_global_threshold_58 =  QHBoxLayout()
        label_global_threshold_58 = QLabel("            global_threshold")
        label_global_threshold_58.setPalette(palette_object)
        label_global_threshold_58.setFont(QFont("Monospace", 10))
        hbox_lay_global_threshold_58.addWidget(label_global_threshold_58)

        box_global_threshold_58 = QDoubleSpinBox()
        box_global_threshold_58.setValue(0.0)
        box_global_threshold_58.local_path = "spotfinder.threshold.xds.global_threshold"
        box_global_threshold_58.valueChanged.connect(self.spnbox_changed)
        hbox_lay_global_threshold_58.addWidget(box_global_threshold_58)
        bg_box.addLayout(hbox_lay_global_threshold_58)

        label_59 = QLabel("        helen")
        label_59.setPalette(palette_scope)
        label_59.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_59)

        hbox_lay_exp_spot_dimension_60 =  QHBoxLayout()
        label_exp_spot_dimension_60 = QLabel("            exp_spot_dimension")
        label_exp_spot_dimension_60.setPalette(palette_object)
        label_exp_spot_dimension_60.setFont(QFont("Monospace", 10))
        hbox_lay_exp_spot_dimension_60.addWidget(label_exp_spot_dimension_60)

        box_exp_spot_dimension_60 = QSpinBox()
        box_exp_spot_dimension_60.setValue(3)
        box_exp_spot_dimension_60.local_path = "spotfinder.threshold.helen.exp_spot_dimension"
        box_exp_spot_dimension_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_exp_spot_dimension_60.addWidget(box_exp_spot_dimension_60)
        bg_box.addLayout(hbox_lay_exp_spot_dimension_60)

        hbox_lay_global_threshold_61 =  QHBoxLayout()
        label_global_threshold_61 = QLabel("            global_threshold")
        label_global_threshold_61.setPalette(palette_object)
        label_global_threshold_61.setFont(QFont("Monospace", 10))
        hbox_lay_global_threshold_61.addWidget(label_global_threshold_61)

        box_global_threshold_61 = QDoubleSpinBox()
        box_global_threshold_61.setValue(100.0)
        box_global_threshold_61.local_path = "spotfinder.threshold.helen.global_threshold"
        box_global_threshold_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_global_threshold_61.addWidget(box_global_threshold_61)
        bg_box.addLayout(hbox_lay_global_threshold_61)

        hbox_lay_min_blob_score_62 =  QHBoxLayout()
        label_min_blob_score_62 = QLabel("            min_blob_score")
        label_min_blob_score_62.setPalette(palette_object)
        label_min_blob_score_62.setFont(QFont("Monospace", 10))
        hbox_lay_min_blob_score_62.addWidget(label_min_blob_score_62)

        box_min_blob_score_62 = QDoubleSpinBox()
        box_min_blob_score_62.setValue(0.7)
        box_min_blob_score_62.local_path = "spotfinder.threshold.helen.min_blob_score"
        box_min_blob_score_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_blob_score_62.addWidget(box_min_blob_score_62)
        bg_box.addLayout(hbox_lay_min_blob_score_62)

        hbox_lay_num_passes_63 =  QHBoxLayout()
        label_num_passes_63 = QLabel("            num_passes")
        label_num_passes_63.setPalette(palette_object)
        label_num_passes_63.setFont(QFont("Monospace", 10))
        hbox_lay_num_passes_63.addWidget(label_num_passes_63)

        box_num_passes_63 = QSpinBox()
        box_num_passes_63.setValue(0)
        box_num_passes_63.local_path = "spotfinder.threshold.helen.num_passes"
        box_num_passes_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_num_passes_63.addWidget(box_num_passes_63)
        bg_box.addLayout(hbox_lay_num_passes_63)

        hbox_lay_debug_64 =  QHBoxLayout()
        label_debug_64 = QLabel("            debug")
        label_debug_64.setPalette(palette_object)
        label_debug_64.setFont(QFont("Monospace", 10))
        hbox_lay_debug_64.addWidget(label_debug_64)

        box_debug_64 = QComboBox()
        box_debug_64.local_path = "spotfinder.threshold.helen.debug"
        box_debug_64.tmp_lst=[]
        box_debug_64.tmp_lst.append("True")
        box_debug_64.tmp_lst.append("False")
        for lst_itm in box_debug_64.tmp_lst:
            box_debug_64.addItem(lst_itm)
        box_debug_64.setCurrentIndex(1)
        box_debug_64.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_64.addWidget(box_debug_64)
        bg_box.addLayout(hbox_lay_debug_64)

 
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
