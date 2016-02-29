import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"


class inner_widg( QWidget):
    item_changed = pyqtSignal()
    def __init__(self, parent = None):
        super(inner_widg, self).__init__(parent)
        self.super_parent = parent
        palette_scope = QPalette()
        palette_scope.setColor(QPalette.Foreground, QColor(75, 75, 75, 255))
        palette_object = QPalette()
        palette_object.setColor(QPalette.Foreground,Qt.black)
        bg_box =  QVBoxLayout(self)


        label_0 = QLabel("output")
        label_0.setPalette(palette_scope)
        label_0.setFont(QFont("Monospace"))
        bg_box.addWidget(label_0)
        hbox_lay_reflections_1 =  QHBoxLayout()
        label_reflections_1 = QLabel("    reflections")
        label_reflections_1.setPalette(palette_object)
        label_reflections_1.setFont(QFont("Monospace"))
        hbox_lay_reflections_1.addWidget(label_reflections_1)

        box_reflections_1 = QLineEdit()
        box_reflections_1.local_path = "output.reflections"
        box_reflections_1.textChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_1.addWidget(box_reflections_1)
        bg_box.addLayout(hbox_lay_reflections_1)

        hbox_lay_shoeboxes_2 =  QHBoxLayout()
        label_shoeboxes_2 = QLabel("    shoeboxes")
        label_shoeboxes_2.setPalette(palette_object)
        label_shoeboxes_2.setFont(QFont("Monospace"))
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
        label_datablock_3.setFont(QFont("Monospace"))
        hbox_lay_datablock_3.addWidget(label_datablock_3)

        box_datablock_3 = QLineEdit()
        box_datablock_3.local_path = "output.datablock"
        box_datablock_3.textChanged.connect(self.spnbox_changed)
        hbox_lay_datablock_3.addWidget(box_datablock_3)
        bg_box.addLayout(hbox_lay_datablock_3)

        hbox_lay_log_4 =  QHBoxLayout()
        label_log_4 = QLabel("    log")
        label_log_4.setPalette(palette_object)
        label_log_4.setFont(QFont("Monospace"))
        hbox_lay_log_4.addWidget(label_log_4)

        box_log_4 = QLineEdit()
        box_log_4.local_path = "output.log"
        box_log_4.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_4.addWidget(box_log_4)
        bg_box.addLayout(hbox_lay_log_4)

        hbox_lay_debug_log_5 =  QHBoxLayout()
        label_debug_log_5 = QLabel("    debug_log")
        label_debug_log_5.setPalette(palette_object)
        label_debug_log_5.setFont(QFont("Monospace"))
        hbox_lay_debug_log_5.addWidget(label_debug_log_5)

        box_debug_log_5 = QLineEdit()
        box_debug_log_5.local_path = "output.debug_log"
        box_debug_log_5.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_5.addWidget(box_debug_log_5)
        bg_box.addLayout(hbox_lay_debug_log_5)

        hbox_lay_per_image_statistics_6 =  QHBoxLayout()
        label_per_image_statistics_6 = QLabel("per_image_statistics")
        label_per_image_statistics_6.setPalette(palette_object)
        label_per_image_statistics_6.setFont(QFont("Monospace"))
        hbox_lay_per_image_statistics_6.addWidget(label_per_image_statistics_6)

        box_per_image_statistics_6 = QComboBox()
        box_per_image_statistics_6.local_path = "per_image_statistics"
        box_per_image_statistics_6.tmp_lst=[]
        box_per_image_statistics_6.tmp_lst.append("True")
        box_per_image_statistics_6.tmp_lst.append("False")
        for lst_itm in box_per_image_statistics_6.tmp_lst:
            box_per_image_statistics_6.addItem(lst_itm)
        box_per_image_statistics_6.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_per_image_statistics_6.addWidget(box_per_image_statistics_6)
        bg_box.addLayout(hbox_lay_per_image_statistics_6)

        hbox_lay_verbosity_7 =  QHBoxLayout()
        label_verbosity_7 = QLabel("verbosity")
        label_verbosity_7.setPalette(palette_object)
        label_verbosity_7.setFont(QFont("Monospace"))
        hbox_lay_verbosity_7.addWidget(label_verbosity_7)

        box_verbosity_7 = QSpinBox()
        box_verbosity_7.local_path = "verbosity"
        box_verbosity_7.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_7.addWidget(box_verbosity_7)
        bg_box.addLayout(hbox_lay_verbosity_7)

        label_8 = QLabel("spotfinder")
        label_8.setPalette(palette_scope)
        label_8.setFont(QFont("Monospace"))
        bg_box.addWidget(label_8)
        label_9 = QLabel("    lookup")
        label_9.setPalette(palette_scope)
        label_9.setFont(QFont("Monospace"))
        bg_box.addWidget(label_9)
        hbox_lay_mask_10 =  QHBoxLayout()
        label_mask_10 = QLabel("        mask")
        label_mask_10.setPalette(palette_object)
        label_mask_10.setFont(QFont("Monospace"))
        hbox_lay_mask_10.addWidget(label_mask_10)

        box_mask_10 = QLineEdit()
        box_mask_10.local_path = "spotfinder.lookup.mask"
        box_mask_10.textChanged.connect(self.spnbox_changed)
        hbox_lay_mask_10.addWidget(box_mask_10)
        bg_box.addLayout(hbox_lay_mask_10)

        hbox_lay_write_hot_mask_11 =  QHBoxLayout()
        label_write_hot_mask_11 = QLabel("    write_hot_mask")
        label_write_hot_mask_11.setPalette(palette_object)
        label_write_hot_mask_11.setFont(QFont("Monospace"))
        hbox_lay_write_hot_mask_11.addWidget(label_write_hot_mask_11)

        box_write_hot_mask_11 = QComboBox()
        box_write_hot_mask_11.local_path = "spotfinder.write_hot_mask"
        box_write_hot_mask_11.tmp_lst=[]
        box_write_hot_mask_11.tmp_lst.append("True")
        box_write_hot_mask_11.tmp_lst.append("False")
        for lst_itm in box_write_hot_mask_11.tmp_lst:
            box_write_hot_mask_11.addItem(lst_itm)
        box_write_hot_mask_11.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_write_hot_mask_11.addWidget(box_write_hot_mask_11)
        bg_box.addLayout(hbox_lay_write_hot_mask_11)

        hbox_lay_scan_range_12_0 =  QHBoxLayout()
        label_scan_range_12_0 = QLabel("    scan_range[1]")
        label_scan_range_12_0.setPalette(palette_object)
        label_scan_range_12_0.setFont(QFont("Monospace"))
        hbox_lay_scan_range_12_0.addWidget(label_scan_range_12_0)
        box_scan_range_12_0 = QSpinBox()
        box_scan_range_12_0.local_path = "spotfinder.scan_range"
        #box_scan_range_12_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_12_1 =  QHBoxLayout()
        label_scan_range_12_1 = QLabel("    scan_range[2]")
        label_scan_range_12_1.setPalette(palette_object)
        label_scan_range_12_1.setFont(QFont("Monospace"))
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
        label_region_of_interest_13_0.setFont(QFont("Monospace"))
        hbox_lay_region_of_interest_13_0.addWidget(label_region_of_interest_13_0)
        box_region_of_interest_13_0 = QSpinBox()
        box_region_of_interest_13_0.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_1 =  QHBoxLayout()
        label_region_of_interest_13_1 = QLabel("    region_of_interest[2]")
        label_region_of_interest_13_1.setPalette(palette_object)
        label_region_of_interest_13_1.setFont(QFont("Monospace"))
        hbox_lay_region_of_interest_13_1.addWidget(label_region_of_interest_13_1)
        box_region_of_interest_13_1 = QSpinBox()
        box_region_of_interest_13_1.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_2 =  QHBoxLayout()
        label_region_of_interest_13_2 = QLabel("    region_of_interest[3]")
        label_region_of_interest_13_2.setPalette(palette_object)
        label_region_of_interest_13_2.setFont(QFont("Monospace"))
        hbox_lay_region_of_interest_13_2.addWidget(label_region_of_interest_13_2)
        box_region_of_interest_13_2 = QSpinBox()
        box_region_of_interest_13_2.local_path = "spotfinder.region_of_interest"
        #box_region_of_interest_13_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_region_of_interest_13_3 =  QHBoxLayout()
        label_region_of_interest_13_3 = QLabel("    region_of_interest[4]")
        label_region_of_interest_13_3.setPalette(palette_object)
        label_region_of_interest_13_3.setFont(QFont("Monospace"))
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
        label_14.setFont(QFont("Monospace"))
        bg_box.addWidget(label_14)
        hbox_lay_min_spot_size_15 =  QHBoxLayout()
        label_min_spot_size_15 = QLabel("        min_spot_size")
        label_min_spot_size_15.setPalette(palette_object)
        label_min_spot_size_15.setFont(QFont("Monospace"))
        hbox_lay_min_spot_size_15.addWidget(label_min_spot_size_15)

        box_min_spot_size_15 = QSpinBox()
        box_min_spot_size_15.local_path = "spotfinder.filter.min_spot_size"
        box_min_spot_size_15.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_spot_size_15.addWidget(box_min_spot_size_15)
        bg_box.addLayout(hbox_lay_min_spot_size_15)

        hbox_lay_max_separation_16 =  QHBoxLayout()
        label_max_separation_16 = QLabel("        max_separation")
        label_max_separation_16.setPalette(palette_object)
        label_max_separation_16.setFont(QFont("Monospace"))
        hbox_lay_max_separation_16.addWidget(label_max_separation_16)

        box_max_separation_16 = QDoubleSpinBox()
        box_max_separation_16.local_path = "spotfinder.filter.max_separation"
        box_max_separation_16.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_separation_16.addWidget(box_max_separation_16)
        bg_box.addLayout(hbox_lay_max_separation_16)

        hbox_lay_d_min_17 =  QHBoxLayout()
        label_d_min_17 = QLabel("        d_min")
        label_d_min_17.setPalette(palette_object)
        label_d_min_17.setFont(QFont("Monospace"))
        hbox_lay_d_min_17.addWidget(label_d_min_17)

        box_d_min_17 = QDoubleSpinBox()
        box_d_min_17.local_path = "spotfinder.filter.d_min"
        box_d_min_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_17.addWidget(box_d_min_17)
        bg_box.addLayout(hbox_lay_d_min_17)

        hbox_lay_d_max_18 =  QHBoxLayout()
        label_d_max_18 = QLabel("        d_max")
        label_d_max_18.setPalette(palette_object)
        label_d_max_18.setFont(QFont("Monospace"))
        hbox_lay_d_max_18.addWidget(label_d_max_18)

        box_d_max_18 = QDoubleSpinBox()
        box_d_max_18.local_path = "spotfinder.filter.d_max"
        box_d_max_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_18.addWidget(box_d_max_18)
        bg_box.addLayout(hbox_lay_d_max_18)

        hbox_lay_max_strong_pixel_fraction_19 =  QHBoxLayout()
        label_max_strong_pixel_fraction_19 = QLabel("        max_strong_pixel_fraction")
        label_max_strong_pixel_fraction_19.setPalette(palette_object)
        label_max_strong_pixel_fraction_19.setFont(QFont("Monospace"))
        hbox_lay_max_strong_pixel_fraction_19.addWidget(label_max_strong_pixel_fraction_19)

        box_max_strong_pixel_fraction_19 = QDoubleSpinBox()
        box_max_strong_pixel_fraction_19.local_path = "spotfinder.filter.max_strong_pixel_fraction"
        box_max_strong_pixel_fraction_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_strong_pixel_fraction_19.addWidget(box_max_strong_pixel_fraction_19)
        bg_box.addLayout(hbox_lay_max_strong_pixel_fraction_19)

        label_20 = QLabel("        background_gradient")
        label_20.setPalette(palette_scope)
        label_20.setFont(QFont("Monospace"))
        bg_box.addWidget(label_20)
        hbox_lay_filter_21 =  QHBoxLayout()
        label_filter_21 = QLabel("            filter")
        label_filter_21.setPalette(palette_object)
        label_filter_21.setFont(QFont("Monospace"))
        hbox_lay_filter_21.addWidget(label_filter_21)

        box_filter_21 = QComboBox()
        box_filter_21.local_path = "spotfinder.filter.background_gradient.filter"
        box_filter_21.tmp_lst=[]
        box_filter_21.tmp_lst.append("True")
        box_filter_21.tmp_lst.append("False")
        for lst_itm in box_filter_21.tmp_lst:
            box_filter_21.addItem(lst_itm)
        box_filter_21.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_21.addWidget(box_filter_21)
        bg_box.addLayout(hbox_lay_filter_21)

        hbox_lay_background_size_22 =  QHBoxLayout()
        label_background_size_22 = QLabel("            background_size")
        label_background_size_22.setPalette(palette_object)
        label_background_size_22.setFont(QFont("Monospace"))
        hbox_lay_background_size_22.addWidget(label_background_size_22)

        box_background_size_22 = QSpinBox()
        box_background_size_22.local_path = "spotfinder.filter.background_gradient.background_size"
        box_background_size_22.valueChanged.connect(self.spnbox_changed)
        hbox_lay_background_size_22.addWidget(box_background_size_22)
        bg_box.addLayout(hbox_lay_background_size_22)

        hbox_lay_gradient_cutoff_23 =  QHBoxLayout()
        label_gradient_cutoff_23 = QLabel("            gradient_cutoff")
        label_gradient_cutoff_23.setPalette(palette_object)
        label_gradient_cutoff_23.setFont(QFont("Monospace"))
        hbox_lay_gradient_cutoff_23.addWidget(label_gradient_cutoff_23)

        box_gradient_cutoff_23 = QDoubleSpinBox()
        box_gradient_cutoff_23.local_path = "spotfinder.filter.background_gradient.gradient_cutoff"
        box_gradient_cutoff_23.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_cutoff_23.addWidget(box_gradient_cutoff_23)
        bg_box.addLayout(hbox_lay_gradient_cutoff_23)

        label_24 = QLabel("        spot_density")
        label_24.setPalette(palette_scope)
        label_24.setFont(QFont("Monospace"))
        bg_box.addWidget(label_24)
        hbox_lay_filter_25 =  QHBoxLayout()
        label_filter_25 = QLabel("            filter")
        label_filter_25.setPalette(palette_object)
        label_filter_25.setFont(QFont("Monospace"))
        hbox_lay_filter_25.addWidget(label_filter_25)

        box_filter_25 = QComboBox()
        box_filter_25.local_path = "spotfinder.filter.spot_density.filter"
        box_filter_25.tmp_lst=[]
        box_filter_25.tmp_lst.append("True")
        box_filter_25.tmp_lst.append("False")
        for lst_itm in box_filter_25.tmp_lst:
            box_filter_25.addItem(lst_itm)
        box_filter_25.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_25.addWidget(box_filter_25)
        bg_box.addLayout(hbox_lay_filter_25)

        label_26 = QLabel("        ice_rings")
        label_26.setPalette(palette_scope)
        label_26.setFont(QFont("Monospace"))
        bg_box.addWidget(label_26)
        hbox_lay_filter_27 =  QHBoxLayout()
        label_filter_27 = QLabel("            filter")
        label_filter_27.setPalette(palette_object)
        label_filter_27.setFont(QFont("Monospace"))
        hbox_lay_filter_27.addWidget(label_filter_27)

        box_filter_27 = QComboBox()
        box_filter_27.local_path = "spotfinder.filter.ice_rings.filter"
        box_filter_27.tmp_lst=[]
        box_filter_27.tmp_lst.append("True")
        box_filter_27.tmp_lst.append("False")
        for lst_itm in box_filter_27.tmp_lst:
            box_filter_27.addItem(lst_itm)
        box_filter_27.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_27.addWidget(box_filter_27)
        bg_box.addLayout(hbox_lay_filter_27)

        hbox_lay_width_30 =  QHBoxLayout()
        label_width_30 = QLabel("            width")
        label_width_30.setPalette(palette_object)
        label_width_30.setFont(QFont("Monospace"))
        hbox_lay_width_30.addWidget(label_width_30)

        box_width_30 = QDoubleSpinBox()
        box_width_30.local_path = "spotfinder.filter.ice_rings.width"
        box_width_30.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_30.addWidget(box_width_30)
        bg_box.addLayout(hbox_lay_width_30)

        label_32 = QLabel("    mp")
        label_32.setPalette(palette_scope)
        label_32.setFont(QFont("Monospace"))
        bg_box.addWidget(label_32)
        hbox_lay_method_33 =  QHBoxLayout()
        label_method_33 = QLabel("        method")
        label_method_33.setPalette(palette_object)
        label_method_33.setFont(QFont("Monospace"))
        hbox_lay_method_33.addWidget(label_method_33)

        box_method_33 = QComboBox()
        box_method_33.local_path = "spotfinder.mp.method"
        box_method_33.tmp_lst=[]
        box_method_33.tmp_lst.append("*multiprocessing")
        box_method_33.tmp_lst.append("sge")
        box_method_33.tmp_lst.append("lsf")
        box_method_33.tmp_lst.append("pbs")
        for lst_itm in box_method_33.tmp_lst:
            box_method_33.addItem(lst_itm)
        box_method_33.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_33.addWidget(box_method_33)
        bg_box.addLayout(hbox_lay_method_33)

        hbox_lay_nproc_34 =  QHBoxLayout()
        label_nproc_34 = QLabel("        nproc")
        label_nproc_34.setPalette(palette_object)
        label_nproc_34.setFont(QFont("Monospace"))
        hbox_lay_nproc_34.addWidget(label_nproc_34)

        box_nproc_34 = QSpinBox()
        box_nproc_34.local_path = "spotfinder.mp.nproc"
        box_nproc_34.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_34.addWidget(box_nproc_34)
        bg_box.addLayout(hbox_lay_nproc_34)

        hbox_lay_chunksize_35 =  QHBoxLayout()
        label_chunksize_35 = QLabel("        chunksize")
        label_chunksize_35.setPalette(palette_object)
        label_chunksize_35.setFont(QFont("Monospace"))
        hbox_lay_chunksize_35.addWidget(label_chunksize_35)

        box_chunksize_35 = QSpinBox()
        box_chunksize_35.local_path = "spotfinder.mp.chunksize"
        box_chunksize_35.valueChanged.connect(self.spnbox_changed)
        hbox_lay_chunksize_35.addWidget(box_chunksize_35)
        bg_box.addLayout(hbox_lay_chunksize_35)

        label_36 = QLabel("    threshold")
        label_36.setPalette(palette_scope)
        label_36.setFont(QFont("Monospace"))
        bg_box.addWidget(label_36)
        hbox_lay_algorithm_37 =  QHBoxLayout()
        label_algorithm_37 = QLabel("        algorithm")
        label_algorithm_37.setPalette(palette_object)
        label_algorithm_37.setFont(QFont("Monospace"))
        hbox_lay_algorithm_37.addWidget(label_algorithm_37)

        box_algorithm_37 = QComboBox()
        box_algorithm_37.local_path = "spotfinder.threshold.algorithm"
        box_algorithm_37.tmp_lst=[]
        box_algorithm_37.tmp_lst.append("*xds")
        for lst_itm in box_algorithm_37.tmp_lst:
            box_algorithm_37.addItem(lst_itm)
        box_algorithm_37.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_37.addWidget(box_algorithm_37)
        bg_box.addLayout(hbox_lay_algorithm_37)

        label_38 = QLabel("        xds")
        label_38.setPalette(palette_scope)
        label_38.setFont(QFont("Monospace"))
        bg_box.addWidget(label_38)
        hbox_lay_gain_39 =  QHBoxLayout()
        label_gain_39 = QLabel("            gain")
        label_gain_39.setPalette(palette_object)
        label_gain_39.setFont(QFont("Monospace"))
        hbox_lay_gain_39.addWidget(label_gain_39)

        box_gain_39 = QDoubleSpinBox()
        box_gain_39.local_path = "spotfinder.threshold.xds.gain"
        box_gain_39.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gain_39.addWidget(box_gain_39)
        bg_box.addLayout(hbox_lay_gain_39)

        hbox_lay_kernel_size_40_0 =  QHBoxLayout()
        label_kernel_size_40_0 = QLabel("            kernel_size[1]")
        label_kernel_size_40_0.setPalette(palette_object)
        label_kernel_size_40_0.setFont(QFont("Monospace"))
        hbox_lay_kernel_size_40_0.addWidget(label_kernel_size_40_0)
        box_kernel_size_40_0 = QSpinBox()
        box_kernel_size_40_0.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_40_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_40_1 =  QHBoxLayout()
        label_kernel_size_40_1 = QLabel("            kernel_size[2]")
        label_kernel_size_40_1.setPalette(palette_object)
        label_kernel_size_40_1.setFont(QFont("Monospace"))
        hbox_lay_kernel_size_40_1.addWidget(label_kernel_size_40_1)
        box_kernel_size_40_1 = QSpinBox()
        box_kernel_size_40_1.local_path = "spotfinder.threshold.xds.kernel_size"
        #box_kernel_size_40_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_kernel_size_40_0.addWidget(box_kernel_size_40_0)
        bg_box.addLayout(hbox_lay_kernel_size_40_0)

        hbox_lay_kernel_size_40_1.addWidget(box_kernel_size_40_1)
        bg_box.addLayout(hbox_lay_kernel_size_40_1)

        hbox_lay_sigma_background_41 =  QHBoxLayout()
        label_sigma_background_41 = QLabel("            sigma_background")
        label_sigma_background_41.setPalette(palette_object)
        label_sigma_background_41.setFont(QFont("Monospace"))
        hbox_lay_sigma_background_41.addWidget(label_sigma_background_41)

        box_sigma_background_41 = QDoubleSpinBox()
        box_sigma_background_41.local_path = "spotfinder.threshold.xds.sigma_background"
        box_sigma_background_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_background_41.addWidget(box_sigma_background_41)
        bg_box.addLayout(hbox_lay_sigma_background_41)

        hbox_lay_sigma_strong_42 =  QHBoxLayout()
        label_sigma_strong_42 = QLabel("            sigma_strong")
        label_sigma_strong_42.setPalette(palette_object)
        label_sigma_strong_42.setFont(QFont("Monospace"))
        hbox_lay_sigma_strong_42.addWidget(label_sigma_strong_42)

        box_sigma_strong_42 = QDoubleSpinBox()
        box_sigma_strong_42.local_path = "spotfinder.threshold.xds.sigma_strong"
        box_sigma_strong_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_strong_42.addWidget(box_sigma_strong_42)
        bg_box.addLayout(hbox_lay_sigma_strong_42)

        hbox_lay_min_local_43 =  QHBoxLayout()
        label_min_local_43 = QLabel("            min_local")
        label_min_local_43.setPalette(palette_object)
        label_min_local_43.setFont(QFont("Monospace"))
        hbox_lay_min_local_43.addWidget(label_min_local_43)

        box_min_local_43 = QSpinBox()
        box_min_local_43.local_path = "spotfinder.threshold.xds.min_local"
        box_min_local_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_local_43.addWidget(box_min_local_43)
        bg_box.addLayout(hbox_lay_min_local_43)

        hbox_lay_global_threshold_44 =  QHBoxLayout()
        label_global_threshold_44 = QLabel("            global_threshold")
        label_global_threshold_44.setPalette(palette_object)
        label_global_threshold_44.setFont(QFont("Monospace"))
        hbox_lay_global_threshold_44.addWidget(label_global_threshold_44)

        box_global_threshold_44 = QDoubleSpinBox()
        box_global_threshold_44.local_path = "spotfinder.threshold.xds.global_threshold"
        box_global_threshold_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_global_threshold_44.addWidget(box_global_threshold_44)
        bg_box.addLayout(hbox_lay_global_threshold_44)

 
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
        self.super_parent = parent
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
