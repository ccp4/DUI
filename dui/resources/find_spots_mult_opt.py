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
        palette_scope.setColor(QPalette.Foreground, QColor(45, 45, 45, 255))
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

        hbox_lay_scan_range_12_0 =  QHBoxLayout()
        label_scan_range_12_0 = QLabel("    scan_range[1]")
        label_scan_range_12_0.setPalette(palette_object)
        label_scan_range_12_0.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_12_0.addWidget(label_scan_range_12_0)
        box_scan_range_12_0 = QSpinBox()
        box_scan_range_12_0.local_path = "spotfinder.scan_range"
        #box_scan_range_12_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_12_1 =  QHBoxLayout()
        label_scan_range_12_1 = QLabel("    scan_range[2]")
        label_scan_range_12_1.setPalette(palette_object)
        label_scan_range_12_1.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_12_1.addWidget(label_scan_range_12_1)
        box_scan_range_12_1 = QSpinBox()
        box_scan_range_12_1.local_path = "spotfinder.scan_range"
        #box_scan_range_12_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_12_0.addWidget(box_scan_range_12_0)
        bg_box.addLayout(hbox_lay_scan_range_12_0)
        hbox_lay_scan_range_12_1.addWidget(box_scan_range_12_1)
        bg_box.addLayout(hbox_lay_scan_range_12_1)

        hbox_lay_region_of_interest_13_0 =  QHBoxLayout()
        label_region_of_interest_13_0 = QLabel("    region_of_interest[1]")
        label_region_of_interest_13_0.setPalette(palette_object)
        label_region_of_interest_13_0.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_13_0.addWidget(label_region_of_interest_13_0)
        box_region_of_interest_13_0 = QSpinBox()
        box_region_of_interest_13_0.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_1 =  QHBoxLayout()
        label_region_of_interest_13_1 = QLabel("    region_of_interest[2]")
        label_region_of_interest_13_1.setPalette(palette_object)
        label_region_of_interest_13_1.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_13_1.addWidget(label_region_of_interest_13_1)
        box_region_of_interest_13_1 = QSpinBox()
        box_region_of_interest_13_1.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_2 =  QHBoxLayout()
        label_region_of_interest_13_2 = QLabel("    region_of_interest[3]")
        label_region_of_interest_13_2.setPalette(palette_object)
        label_region_of_interest_13_2.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_13_2.addWidget(label_region_of_interest_13_2)
        box_region_of_interest_13_2 = QSpinBox()
        box_region_of_interest_13_2.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_3 =  QHBoxLayout()
        label_region_of_interest_13_3 = QLabel("    region_of_interest[4]")
        label_region_of_interest_13_3.setPalette(palette_object)
        label_region_of_interest_13_3.setFont(QFont("Monospace", 10))
        hbox_lay_region_of_interest_13_3.addWidget(label_region_of_interest_13_3)
        box_region_of_interest_13_3 = QSpinBox()
        box_region_of_interest_13_3.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_0.addWidget(box_region_of_interest_13_0)
        bg_box.addLayout(hbox_lay_region_of_interest_13_0)
        hbox_lay_region_of_interest_13_1.addWidget(box_region_of_interest_13_1)
        bg_box.addLayout(hbox_lay_region_of_interest_13_1)
        hbox_lay_region_of_interest_13_2.addWidget(box_region_of_interest_13_2)
        bg_box.addLayout(hbox_lay_region_of_interest_13_2)
        hbox_lay_region_of_interest_13_3.addWidget(box_region_of_interest_13_3)
        bg_box.addLayout(hbox_lay_region_of_interest_13_3)

        label_14 = QLabel("    filter")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_14)

        hbox_lay_min_spot_size_15 =  QHBoxLayout()
        label_min_spot_size_15 = QLabel("        min_spot_size")
        label_min_spot_size_15.setPalette(palette_object)
        label_min_spot_size_15.setFont(QFont("Monospace", 10))
        hbox_lay_min_spot_size_15.addWidget(label_min_spot_size_15)

        box_min_spot_size_15 = QSpinBox()
        box_min_spot_size_15.local_path = "spotfinder.filter.min_spot_size"
        box_min_spot_size_15.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_spot_size_15.addWidget(box_min_spot_size_15)
        bg_box.addLayout(hbox_lay_min_spot_size_15)

        hbox_lay_max_spot_size_16 =  QHBoxLayout()
        label_max_spot_size_16 = QLabel("        max_spot_size")
        label_max_spot_size_16.setPalette(palette_object)
        label_max_spot_size_16.setFont(QFont("Monospace", 10))
        hbox_lay_max_spot_size_16.addWidget(label_max_spot_size_16)

        box_max_spot_size_16 = QSpinBox()
        box_max_spot_size_16.setValue(100)
        box_max_spot_size_16.local_path = "spotfinder.filter.max_spot_size"
        box_max_spot_size_16.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_spot_size_16.addWidget(box_max_spot_size_16)
        bg_box.addLayout(hbox_lay_max_spot_size_16)

        hbox_lay_max_separation_17 =  QHBoxLayout()
        label_max_separation_17 = QLabel("        max_separation")
        label_max_separation_17.setPalette(palette_object)
        label_max_separation_17.setFont(QFont("Monospace", 10))
        hbox_lay_max_separation_17.addWidget(label_max_separation_17)

        box_max_separation_17 = QDoubleSpinBox()
        box_max_separation_17.setValue(2.0)
        box_max_separation_17.local_path = "spotfinder.filter.max_separation"
        box_max_separation_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_separation_17.addWidget(box_max_separation_17)
        bg_box.addLayout(hbox_lay_max_separation_17)

        hbox_lay_max_strong_pixel_fraction_18 =  QHBoxLayout()
        label_max_strong_pixel_fraction_18 = QLabel("        max_strong_pixel_fraction")
        label_max_strong_pixel_fraction_18.setPalette(palette_object)
        label_max_strong_pixel_fraction_18.setFont(QFont("Monospace", 10))
        hbox_lay_max_strong_pixel_fraction_18.addWidget(label_max_strong_pixel_fraction_18)

        box_max_strong_pixel_fraction_18 = QDoubleSpinBox()
        box_max_strong_pixel_fraction_18.setValue(0.25)
        box_max_strong_pixel_fraction_18.local_path = "spotfinder.filter.max_strong_pixel_fraction"
        box_max_strong_pixel_fraction_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_strong_pixel_fraction_18.addWidget(box_max_strong_pixel_fraction_18)
        bg_box.addLayout(hbox_lay_max_strong_pixel_fraction_18)

        label_19 = QLabel("        background_gradient")
        label_19.setPalette(palette_scope)
        label_19.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_19)

        hbox_lay_filter_20 =  QHBoxLayout()
        label_filter_20 = QLabel("            filter")
        label_filter_20.setPalette(palette_object)
        label_filter_20.setFont(QFont("Monospace", 10))
        hbox_lay_filter_20.addWidget(label_filter_20)

        box_filter_20 = QComboBox()
        box_filter_20.local_path = "spotfinder.filter.background_gradient.filter"
        box_filter_20.tmp_lst=[]
        box_filter_20.tmp_lst.append("True")
        box_filter_20.tmp_lst.append("False")
        for lst_itm in box_filter_20.tmp_lst:
            box_filter_20.addItem(lst_itm)
        box_filter_20.setCurrentIndex(1)
        box_filter_20.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_20.addWidget(box_filter_20)
        bg_box.addLayout(hbox_lay_filter_20)

        hbox_lay_background_size_21 =  QHBoxLayout()
        label_background_size_21 = QLabel("            background_size")
        label_background_size_21.setPalette(palette_object)
        label_background_size_21.setFont(QFont("Monospace", 10))
        hbox_lay_background_size_21.addWidget(label_background_size_21)

        box_background_size_21 = QSpinBox()
        box_background_size_21.setValue(2)
        box_background_size_21.local_path = "spotfinder.filter.background_gradient.background_size"
        box_background_size_21.valueChanged.connect(self.spnbox_changed)
        hbox_lay_background_size_21.addWidget(box_background_size_21)
        bg_box.addLayout(hbox_lay_background_size_21)

        hbox_lay_gradient_cutoff_22 =  QHBoxLayout()
        label_gradient_cutoff_22 = QLabel("            gradient_cutoff")
        label_gradient_cutoff_22.setPalette(palette_object)
        label_gradient_cutoff_22.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_cutoff_22.addWidget(label_gradient_cutoff_22)

        box_gradient_cutoff_22 = QDoubleSpinBox()
        box_gradient_cutoff_22.setValue(4.0)
        box_gradient_cutoff_22.local_path = "spotfinder.filter.background_gradient.gradient_cutoff"
        box_gradient_cutoff_22.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_cutoff_22.addWidget(box_gradient_cutoff_22)
        bg_box.addLayout(hbox_lay_gradient_cutoff_22)

        label_23 = QLabel("        spot_density")
        label_23.setPalette(palette_scope)
        label_23.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_23)

        hbox_lay_filter_24 =  QHBoxLayout()
        label_filter_24 = QLabel("            filter")
        label_filter_24.setPalette(palette_object)
        label_filter_24.setFont(QFont("Monospace", 10))
        hbox_lay_filter_24.addWidget(label_filter_24)

        box_filter_24 = QComboBox()
        box_filter_24.local_path = "spotfinder.filter.spot_density.filter"
        box_filter_24.tmp_lst=[]
        box_filter_24.tmp_lst.append("True")
        box_filter_24.tmp_lst.append("False")
        for lst_itm in box_filter_24.tmp_lst:
            box_filter_24.addItem(lst_itm)
        box_filter_24.setCurrentIndex(1)
        box_filter_24.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_24.addWidget(box_filter_24)
        bg_box.addLayout(hbox_lay_filter_24)

        hbox_lay_border_25 =  QHBoxLayout()
        label_border_25 = QLabel("        border")
        label_border_25.setPalette(palette_object)
        label_border_25.setFont(QFont("Monospace", 10))
        hbox_lay_border_25.addWidget(label_border_25)

        box_border_25 = QSpinBox()
        box_border_25.setValue(0)
        box_border_25.local_path = "spotfinder.filter.border"
        box_border_25.valueChanged.connect(self.spnbox_changed)
        hbox_lay_border_25.addWidget(box_border_25)
        bg_box.addLayout(hbox_lay_border_25)

        hbox_lay_use_trusted_range_26 =  QHBoxLayout()
        label_use_trusted_range_26 = QLabel("        use_trusted_range")
        label_use_trusted_range_26.setPalette(palette_object)
        label_use_trusted_range_26.setFont(QFont("Monospace", 10))
        hbox_lay_use_trusted_range_26.addWidget(label_use_trusted_range_26)

        box_use_trusted_range_26 = QComboBox()
        box_use_trusted_range_26.local_path = "spotfinder.filter.use_trusted_range"
        box_use_trusted_range_26.tmp_lst=[]
        box_use_trusted_range_26.tmp_lst.append("True")
        box_use_trusted_range_26.tmp_lst.append("False")
        for lst_itm in box_use_trusted_range_26.tmp_lst:
            box_use_trusted_range_26.addItem(lst_itm)
        box_use_trusted_range_26.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_use_trusted_range_26.addWidget(box_use_trusted_range_26)
        bg_box.addLayout(hbox_lay_use_trusted_range_26)

        hbox_lay_d_min_27 =  QHBoxLayout()
        label_d_min_27 = QLabel("        d_min")
        label_d_min_27.setPalette(palette_object)
        label_d_min_27.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_27.addWidget(label_d_min_27)

        box_d_min_27 = QDoubleSpinBox()
        box_d_min_27.local_path = "spotfinder.filter.d_min"
        box_d_min_27.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_27.addWidget(box_d_min_27)
        bg_box.addLayout(hbox_lay_d_min_27)

        hbox_lay_d_max_28 =  QHBoxLayout()
        label_d_max_28 = QLabel("        d_max")
        label_d_max_28.setPalette(palette_object)
        label_d_max_28.setFont(QFont("Monospace", 10))
        hbox_lay_d_max_28.addWidget(label_d_max_28)

        box_d_max_28 = QDoubleSpinBox()
        box_d_max_28.local_path = "spotfinder.filter.d_max"
        box_d_max_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_28.addWidget(box_d_max_28)
        bg_box.addLayout(hbox_lay_d_max_28)

        hbox_lay_resolution_range_29_0 =  QHBoxLayout()
        label_resolution_range_29_0 = QLabel("        resolution_range[1]")
        label_resolution_range_29_0.setPalette(palette_object)
        label_resolution_range_29_0.setFont(QFont("Monospace", 10))
        hbox_lay_resolution_range_29_0.addWidget(label_resolution_range_29_0)
        box_resolution_range_29_0 = QDoubleSpinBox()
        box_resolution_range_29_0.local_path = "spotfinder.filter.resolution_range"
        #box_resolution_range_29_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_resolution_range_29_1 =  QHBoxLayout()
        label_resolution_range_29_1 = QLabel("        resolution_range[2]")
        label_resolution_range_29_1.setPalette(palette_object)
        label_resolution_range_29_1.setFont(QFont("Monospace", 10))
        hbox_lay_resolution_range_29_1.addWidget(label_resolution_range_29_1)
        box_resolution_range_29_1 = QDoubleSpinBox()
        box_resolution_range_29_1.local_path = "spotfinder.filter.resolution_range"
        #box_resolution_range_29_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_resolution_range_29_0.addWidget(box_resolution_range_29_0)
        bg_box.addLayout(hbox_lay_resolution_range_29_0)
        hbox_lay_resolution_range_29_1.addWidget(box_resolution_range_29_1)
        bg_box.addLayout(hbox_lay_resolution_range_29_1)

        label_30 = QLabel("        untrusted")
        label_30.setPalette(palette_scope)
        label_30.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_30)

        hbox_lay_panel_31 =  QHBoxLayout()
        label_panel_31 = QLabel("            panel")
        label_panel_31.setPalette(palette_object)
        label_panel_31.setFont(QFont("Monospace", 10))
        hbox_lay_panel_31.addWidget(label_panel_31)

        box_panel_31 = QSpinBox()
        box_panel_31.setValue(0)
        box_panel_31.local_path = "spotfinder.filter.untrusted.panel"
        box_panel_31.valueChanged.connect(self.spnbox_changed)
        hbox_lay_panel_31.addWidget(box_panel_31)
        bg_box.addLayout(hbox_lay_panel_31)

        hbox_lay_circle_32_0 =  QHBoxLayout()
        label_circle_32_0 = QLabel("            circle[1]")
        label_circle_32_0.setPalette(palette_object)
        label_circle_32_0.setFont(QFont("Monospace", 10))
        hbox_lay_circle_32_0.addWidget(label_circle_32_0)
        box_circle_32_0 = QSpinBox()
        box_circle_32_0.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_32_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_32_1 =  QHBoxLayout()
        label_circle_32_1 = QLabel("            circle[2]")
        label_circle_32_1.setPalette(palette_object)
        label_circle_32_1.setFont(QFont("Monospace", 10))
        hbox_lay_circle_32_1.addWidget(label_circle_32_1)
        box_circle_32_1 = QSpinBox()
        box_circle_32_1.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_32_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_32_2 =  QHBoxLayout()
        label_circle_32_2 = QLabel("            circle[3]")
        label_circle_32_2.setPalette(palette_object)
        label_circle_32_2.setFont(QFont("Monospace", 10))
        hbox_lay_circle_32_2.addWidget(label_circle_32_2)
        box_circle_32_2 = QSpinBox()
        box_circle_32_2.local_path = "spotfinder.filter.untrusted.circle"
        #box_circle_32_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_circle_32_0.addWidget(box_circle_32_0)
        bg_box.addLayout(hbox_lay_circle_32_0)
        hbox_lay_circle_32_1.addWidget(box_circle_32_1)
        bg_box.addLayout(hbox_lay_circle_32_1)
        hbox_lay_circle_32_2.addWidget(box_circle_32_2)
        bg_box.addLayout(hbox_lay_circle_32_2)

        hbox_lay_rectangle_33_0 =  QHBoxLayout()
        label_rectangle_33_0 = QLabel("            rectangle[1]")
        label_rectangle_33_0.setPalette(palette_object)
        label_rectangle_33_0.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_33_0.addWidget(label_rectangle_33_0)
        box_rectangle_33_0 = QSpinBox()
        box_rectangle_33_0.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_33_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_33_1 =  QHBoxLayout()
        label_rectangle_33_1 = QLabel("            rectangle[2]")
        label_rectangle_33_1.setPalette(palette_object)
        label_rectangle_33_1.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_33_1.addWidget(label_rectangle_33_1)
        box_rectangle_33_1 = QSpinBox()
        box_rectangle_33_1.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_33_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_33_2 =  QHBoxLayout()
        label_rectangle_33_2 = QLabel("            rectangle[3]")
        label_rectangle_33_2.setPalette(palette_object)
        label_rectangle_33_2.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_33_2.addWidget(label_rectangle_33_2)
        box_rectangle_33_2 = QSpinBox()
        box_rectangle_33_2.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_33_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_33_3 =  QHBoxLayout()
        label_rectangle_33_3 = QLabel("            rectangle[4]")
        label_rectangle_33_3.setPalette(palette_object)
        label_rectangle_33_3.setFont(QFont("Monospace", 10))
        hbox_lay_rectangle_33_3.addWidget(label_rectangle_33_3)
        box_rectangle_33_3 = QSpinBox()
        box_rectangle_33_3.local_path = "spotfinder.filter.untrusted.rectangle"
        #box_rectangle_33_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rectangle_33_0.addWidget(box_rectangle_33_0)
        bg_box.addLayout(hbox_lay_rectangle_33_0)
        hbox_lay_rectangle_33_1.addWidget(box_rectangle_33_1)
        bg_box.addLayout(hbox_lay_rectangle_33_1)
        hbox_lay_rectangle_33_2.addWidget(box_rectangle_33_2)
        bg_box.addLayout(hbox_lay_rectangle_33_2)
        hbox_lay_rectangle_33_3.addWidget(box_rectangle_33_3)
        bg_box.addLayout(hbox_lay_rectangle_33_3)


        label_35 = QLabel("        ice_rings")
        label_35.setPalette(palette_scope)
        label_35.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_35)

        hbox_lay_filter_36 =  QHBoxLayout()
        label_filter_36 = QLabel("            filter")
        label_filter_36.setPalette(palette_object)
        label_filter_36.setFont(QFont("Monospace", 10))
        hbox_lay_filter_36.addWidget(label_filter_36)

        box_filter_36 = QComboBox()
        box_filter_36.local_path = "spotfinder.filter.ice_rings.filter"
        box_filter_36.tmp_lst=[]
        box_filter_36.tmp_lst.append("True")
        box_filter_36.tmp_lst.append("False")
        for lst_itm in box_filter_36.tmp_lst:
            box_filter_36.addItem(lst_itm)
        box_filter_36.setCurrentIndex(1)
        box_filter_36.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_36.addWidget(box_filter_36)
        bg_box.addLayout(hbox_lay_filter_36)



        hbox_lay_width_39 =  QHBoxLayout()
        label_width_39 = QLabel("            width")
        label_width_39.setPalette(palette_object)
        label_width_39.setFont(QFont("Monospace", 10))
        hbox_lay_width_39.addWidget(label_width_39)

        box_width_39 = QDoubleSpinBox()
        box_width_39.setValue(0.06)
        box_width_39.local_path = "spotfinder.filter.ice_rings.width"
        box_width_39.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_39.addWidget(box_width_39)
        bg_box.addLayout(hbox_lay_width_39)

        hbox_lay_d_min_40 =  QHBoxLayout()
        label_d_min_40 = QLabel("            d_min")
        label_d_min_40.setPalette(palette_object)
        label_d_min_40.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_40.addWidget(label_d_min_40)

        box_d_min_40 = QDoubleSpinBox()
        box_d_min_40.local_path = "spotfinder.filter.ice_rings.d_min"
        box_d_min_40.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_40.addWidget(box_d_min_40)
        bg_box.addLayout(hbox_lay_d_min_40)

        label_41 = QLabel("    mp")
        label_41.setPalette(palette_scope)
        label_41.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_41)

        hbox_lay_method_42 =  QHBoxLayout()
        label_method_42 = QLabel("        method")
        label_method_42.setPalette(palette_object)
        label_method_42.setFont(QFont("Monospace", 10))
        hbox_lay_method_42.addWidget(label_method_42)

        box_method_42 = QComboBox()
        box_method_42.local_path = "spotfinder.mp.method"
        box_method_42.tmp_lst=[]
        box_method_42.tmp_lst.append("multiprocessing")
        box_method_42.tmp_lst.append("sge")
        box_method_42.tmp_lst.append("lsf")
        box_method_42.tmp_lst.append("pbs")
        for lst_itm in box_method_42.tmp_lst:
            box_method_42.addItem(lst_itm)
        box_method_42.setCurrentIndex(0)
        box_method_42.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_42.addWidget(box_method_42)
        bg_box.addLayout(hbox_lay_method_42)

        hbox_lay_nproc_43 =  QHBoxLayout()
        label_nproc_43 = QLabel("        nproc")
        label_nproc_43.setPalette(palette_object)
        label_nproc_43.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_43.addWidget(label_nproc_43)

        box_nproc_43 = QSpinBox()
        box_nproc_43.setValue(1)
        box_nproc_43.local_path = "spotfinder.mp.nproc"
        box_nproc_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_43.addWidget(box_nproc_43)
        bg_box.addLayout(hbox_lay_nproc_43)

        hbox_lay_chunksize_44 =  QHBoxLayout()
        label_chunksize_44 = QLabel("        chunksize")
        label_chunksize_44.setPalette(palette_object)
        label_chunksize_44.setFont(QFont("Monospace", 10))
        hbox_lay_chunksize_44.addWidget(label_chunksize_44)

        box_chunksize_44 = QSpinBox()
        box_chunksize_44.setValue(20)
        box_chunksize_44.local_path = "spotfinder.mp.chunksize"
        box_chunksize_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_chunksize_44.addWidget(box_chunksize_44)
        bg_box.addLayout(hbox_lay_chunksize_44)

        label_45 = QLabel("    threshold")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_45)

        hbox_lay_algorithm_46 =  QHBoxLayout()
        label_algorithm_46 = QLabel("        algorithm")
        label_algorithm_46.setPalette(palette_object)
        label_algorithm_46.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_46.addWidget(label_algorithm_46)

        box_algorithm_46 = QComboBox()
        box_algorithm_46.local_path = "spotfinder.threshold.algorithm"
        box_algorithm_46.tmp_lst=[]
        box_algorithm_46.tmp_lst.append("xds")
        for lst_itm in box_algorithm_46.tmp_lst:
            box_algorithm_46.addItem(lst_itm)
        box_algorithm_46.setCurrentIndex(0)
        box_algorithm_46.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_46.addWidget(box_algorithm_46)
        bg_box.addLayout(hbox_lay_algorithm_46)

        label_47 = QLabel("        xds")
        label_47.setPalette(palette_scope)
        label_47.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_47)

        hbox_lay_gain_48 =  QHBoxLayout()
        label_gain_48 = QLabel("            gain")
        label_gain_48.setPalette(palette_object)
        label_gain_48.setFont(QFont("Monospace", 10))
        hbox_lay_gain_48.addWidget(label_gain_48)

        box_gain_48 = QDoubleSpinBox()
        box_gain_48.local_path = "spotfinder.threshold.xds.gain"
        box_gain_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gain_48.addWidget(box_gain_48)
        bg_box.addLayout(hbox_lay_gain_48)

        hbox_lay_kernel_size_49_0 =  QHBoxLayout()
        label_kernel_size_49_0 = QLabel("            kernel_size[1]")
        label_kernel_size_49_0.setPalette(palette_object)
        label_kernel_size_49_0.setFont(QFont("Monospace", 10))
        hbox_lay_kernel_size_49_0.addWidget(label_kernel_size_49_0)
        box_kernel_size_49_0 = QSpinBox()
        box_kernel_size_49_0.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_49_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_49_1 =  QHBoxLayout()
        label_kernel_size_49_1 = QLabel("            kernel_size[2]")
        label_kernel_size_49_1.setPalette(palette_object)
        label_kernel_size_49_1.setFont(QFont("Monospace", 10))
        hbox_lay_kernel_size_49_1.addWidget(label_kernel_size_49_1)
        box_kernel_size_49_1 = QSpinBox()
        box_kernel_size_49_1.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_49_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_49_0.addWidget(box_kernel_size_49_0)
        bg_box.addLayout(hbox_lay_kernel_size_49_0)
        hbox_lay_kernel_size_49_1.addWidget(box_kernel_size_49_1)
        bg_box.addLayout(hbox_lay_kernel_size_49_1)

        hbox_lay_sigma_background_50 =  QHBoxLayout()
        label_sigma_background_50 = QLabel("            sigma_background")
        label_sigma_background_50.setPalette(palette_object)
        label_sigma_background_50.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_background_50.addWidget(label_sigma_background_50)

        box_sigma_background_50 = QDoubleSpinBox()
        box_sigma_background_50.setValue(6.0)
        box_sigma_background_50.local_path = "spotfinder.threshold.xds.sigma_background"
        box_sigma_background_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_background_50.addWidget(box_sigma_background_50)
        bg_box.addLayout(hbox_lay_sigma_background_50)

        hbox_lay_sigma_strong_51 =  QHBoxLayout()
        label_sigma_strong_51 = QLabel("            sigma_strong")
        label_sigma_strong_51.setPalette(palette_object)
        label_sigma_strong_51.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_strong_51.addWidget(label_sigma_strong_51)

        box_sigma_strong_51 = QDoubleSpinBox()
        box_sigma_strong_51.setValue(3.0)
        box_sigma_strong_51.local_path = "spotfinder.threshold.xds.sigma_strong"
        box_sigma_strong_51.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_strong_51.addWidget(box_sigma_strong_51)
        bg_box.addLayout(hbox_lay_sigma_strong_51)

        hbox_lay_min_local_52 =  QHBoxLayout()
        label_min_local_52 = QLabel("            min_local")
        label_min_local_52.setPalette(palette_object)
        label_min_local_52.setFont(QFont("Monospace", 10))
        hbox_lay_min_local_52.addWidget(label_min_local_52)

        box_min_local_52 = QSpinBox()
        box_min_local_52.setValue(2)
        box_min_local_52.local_path = "spotfinder.threshold.xds.min_local"
        box_min_local_52.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_local_52.addWidget(box_min_local_52)
        bg_box.addLayout(hbox_lay_min_local_52)

        hbox_lay_global_threshold_53 =  QHBoxLayout()
        label_global_threshold_53 = QLabel("            global_threshold")
        label_global_threshold_53.setPalette(palette_object)
        label_global_threshold_53.setFont(QFont("Monospace", 10))
        hbox_lay_global_threshold_53.addWidget(label_global_threshold_53)

        box_global_threshold_53 = QDoubleSpinBox()
        box_global_threshold_53.setValue(0.0)
        box_global_threshold_53.local_path = "spotfinder.threshold.xds.global_threshold"
        box_global_threshold_53.valueChanged.connect(self.spnbox_changed)
        hbox_lay_global_threshold_53.addWidget(box_global_threshold_53)
        bg_box.addLayout(hbox_lay_global_threshold_53)

 
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
