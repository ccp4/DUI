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


        label_0 = QLabel("indexing")
        label_0.setPalette(palette_scope)
        label_0.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_0)

        hbox_lay_nproc_1 =  QHBoxLayout()
        label_nproc_1 = QLabel("    nproc")
        label_nproc_1.setPalette(palette_object)
        label_nproc_1.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_1.addWidget(label_nproc_1)

        box_nproc_1 = QSpinBox()
        box_nproc_1.setValue(1)
        box_nproc_1.local_path = "indexing.nproc"
        box_nproc_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_1.addWidget(box_nproc_1)
        bg_box.addLayout(hbox_lay_nproc_1)

        hbox_lay_discover_better_experimental_model_2 =  QHBoxLayout()
        label_discover_better_experimental_model_2 = QLabel("    discover_better_experimental_model")
        label_discover_better_experimental_model_2.setPalette(palette_object)
        label_discover_better_experimental_model_2.setFont(QFont("Monospace", 10))
        hbox_lay_discover_better_experimental_model_2.addWidget(label_discover_better_experimental_model_2)

        box_discover_better_experimental_model_2 = QComboBox()
        box_discover_better_experimental_model_2.local_path = "indexing.discover_better_experimental_model"
        box_discover_better_experimental_model_2.tmp_lst=[]
        box_discover_better_experimental_model_2.tmp_lst.append("True")
        box_discover_better_experimental_model_2.tmp_lst.append("False")
        for lst_itm in box_discover_better_experimental_model_2.tmp_lst:
            box_discover_better_experimental_model_2.addItem(lst_itm)
        box_discover_better_experimental_model_2.setCurrentIndex(1)
        box_discover_better_experimental_model_2.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_discover_better_experimental_model_2.addWidget(box_discover_better_experimental_model_2)
        bg_box.addLayout(hbox_lay_discover_better_experimental_model_2)

        hbox_lay_mm_search_scope_3 =  QHBoxLayout()
        label_mm_search_scope_3 = QLabel("    mm_search_scope")
        label_mm_search_scope_3.setPalette(palette_object)
        label_mm_search_scope_3.setFont(QFont("Monospace", 10))
        hbox_lay_mm_search_scope_3.addWidget(label_mm_search_scope_3)

        box_mm_search_scope_3 = QDoubleSpinBox()
        box_mm_search_scope_3.setValue(4.0)
        box_mm_search_scope_3.local_path = "indexing.mm_search_scope"
        box_mm_search_scope_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_mm_search_scope_3.addWidget(box_mm_search_scope_3)
        bg_box.addLayout(hbox_lay_mm_search_scope_3)

        hbox_lay_wide_search_binning_4 =  QHBoxLayout()
        label_wide_search_binning_4 = QLabel("    wide_search_binning")
        label_wide_search_binning_4.setPalette(palette_object)
        label_wide_search_binning_4.setFont(QFont("Monospace", 10))
        hbox_lay_wide_search_binning_4.addWidget(label_wide_search_binning_4)

        box_wide_search_binning_4 = QDoubleSpinBox()
        box_wide_search_binning_4.setValue(2.0)
        box_wide_search_binning_4.local_path = "indexing.wide_search_binning"
        box_wide_search_binning_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_wide_search_binning_4.addWidget(box_wide_search_binning_4)
        bg_box.addLayout(hbox_lay_wide_search_binning_4)

        hbox_lay_min_cell_volume_5 =  QHBoxLayout()
        label_min_cell_volume_5 = QLabel("    min_cell_volume")
        label_min_cell_volume_5.setPalette(palette_object)
        label_min_cell_volume_5.setFont(QFont("Monospace", 10))
        hbox_lay_min_cell_volume_5.addWidget(label_min_cell_volume_5)

        box_min_cell_volume_5 = QDoubleSpinBox()
        box_min_cell_volume_5.setValue(25.0)
        box_min_cell_volume_5.local_path = "indexing.min_cell_volume"
        box_min_cell_volume_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cell_volume_5.addWidget(box_min_cell_volume_5)
        bg_box.addLayout(hbox_lay_min_cell_volume_5)

        hbox_lay_min_cell_6 =  QHBoxLayout()
        label_min_cell_6 = QLabel("    min_cell")
        label_min_cell_6.setPalette(palette_object)
        label_min_cell_6.setFont(QFont("Monospace", 10))
        hbox_lay_min_cell_6.addWidget(label_min_cell_6)

        box_min_cell_6 = QDoubleSpinBox()
        box_min_cell_6.setValue(3.0)
        box_min_cell_6.local_path = "indexing.min_cell"
        box_min_cell_6.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cell_6.addWidget(box_min_cell_6)
        bg_box.addLayout(hbox_lay_min_cell_6)

        hbox_lay_max_cell_7 =  QHBoxLayout()
        label_max_cell_7 = QLabel("    max_cell")
        label_max_cell_7.setPalette(palette_object)
        label_max_cell_7.setFont(QFont("Monospace", 10))
        hbox_lay_max_cell_7.addWidget(label_max_cell_7)

        box_max_cell_7 = QDoubleSpinBox()
        box_max_cell_7.local_path = "indexing.max_cell"
        box_max_cell_7.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_cell_7.addWidget(box_max_cell_7)
        bg_box.addLayout(hbox_lay_max_cell_7)

        label_8 = QLabel("    max_cell_estimation")
        label_8.setPalette(palette_scope)
        label_8.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_8)

        hbox_lay_filter_ice_9 =  QHBoxLayout()
        label_filter_ice_9 = QLabel("        filter_ice")
        label_filter_ice_9.setPalette(palette_object)
        label_filter_ice_9.setFont(QFont("Monospace", 10))
        hbox_lay_filter_ice_9.addWidget(label_filter_ice_9)

        box_filter_ice_9 = QComboBox()
        box_filter_ice_9.local_path = "indexing.max_cell_estimation.filter_ice"
        box_filter_ice_9.tmp_lst=[]
        box_filter_ice_9.tmp_lst.append("True")
        box_filter_ice_9.tmp_lst.append("False")
        for lst_itm in box_filter_ice_9.tmp_lst:
            box_filter_ice_9.addItem(lst_itm)
        box_filter_ice_9.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_ice_9.addWidget(box_filter_ice_9)
        bg_box.addLayout(hbox_lay_filter_ice_9)

        hbox_lay_filter_overlaps_10 =  QHBoxLayout()
        label_filter_overlaps_10 = QLabel("        filter_overlaps")
        label_filter_overlaps_10.setPalette(palette_object)
        label_filter_overlaps_10.setFont(QFont("Monospace", 10))
        hbox_lay_filter_overlaps_10.addWidget(label_filter_overlaps_10)

        box_filter_overlaps_10 = QComboBox()
        box_filter_overlaps_10.local_path = "indexing.max_cell_estimation.filter_overlaps"
        box_filter_overlaps_10.tmp_lst=[]
        box_filter_overlaps_10.tmp_lst.append("True")
        box_filter_overlaps_10.tmp_lst.append("False")
        for lst_itm in box_filter_overlaps_10.tmp_lst:
            box_filter_overlaps_10.addItem(lst_itm)
        box_filter_overlaps_10.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_overlaps_10.addWidget(box_filter_overlaps_10)
        bg_box.addLayout(hbox_lay_filter_overlaps_10)

        hbox_lay_overlaps_border_11 =  QHBoxLayout()
        label_overlaps_border_11 = QLabel("        overlaps_border")
        label_overlaps_border_11.setPalette(palette_object)
        label_overlaps_border_11.setFont(QFont("Monospace", 10))
        hbox_lay_overlaps_border_11.addWidget(label_overlaps_border_11)

        box_overlaps_border_11 = QSpinBox()
        box_overlaps_border_11.setValue(0)
        box_overlaps_border_11.local_path = "indexing.max_cell_estimation.overlaps_border"
        box_overlaps_border_11.valueChanged.connect(self.spnbox_changed)
        hbox_lay_overlaps_border_11.addWidget(box_overlaps_border_11)
        bg_box.addLayout(hbox_lay_overlaps_border_11)

        hbox_lay_multiplier_12 =  QHBoxLayout()
        label_multiplier_12 = QLabel("        multiplier")
        label_multiplier_12.setPalette(palette_object)
        label_multiplier_12.setFont(QFont("Monospace", 10))
        hbox_lay_multiplier_12.addWidget(label_multiplier_12)

        box_multiplier_12 = QDoubleSpinBox()
        box_multiplier_12.setValue(1.3)
        box_multiplier_12.local_path = "indexing.max_cell_estimation.multiplier"
        box_multiplier_12.valueChanged.connect(self.spnbox_changed)
        hbox_lay_multiplier_12.addWidget(box_multiplier_12)
        bg_box.addLayout(hbox_lay_multiplier_12)

        hbox_lay_step_size_13 =  QHBoxLayout()
        label_step_size_13 = QLabel("        step_size")
        label_step_size_13.setPalette(palette_object)
        label_step_size_13.setFont(QFont("Monospace", 10))
        hbox_lay_step_size_13.addWidget(label_step_size_13)

        box_step_size_13 = QDoubleSpinBox()
        box_step_size_13.setValue(45.0)
        box_step_size_13.local_path = "indexing.max_cell_estimation.step_size"
        box_step_size_13.valueChanged.connect(self.spnbox_changed)
        hbox_lay_step_size_13.addWidget(box_step_size_13)
        bg_box.addLayout(hbox_lay_step_size_13)

        hbox_lay_nearest_neighbor_percentile_14 =  QHBoxLayout()
        label_nearest_neighbor_percentile_14 = QLabel("        nearest_neighbor_percentile")
        label_nearest_neighbor_percentile_14.setPalette(palette_object)
        label_nearest_neighbor_percentile_14.setFont(QFont("Monospace", 10))
        hbox_lay_nearest_neighbor_percentile_14.addWidget(label_nearest_neighbor_percentile_14)

        box_nearest_neighbor_percentile_14 = QDoubleSpinBox()
        box_nearest_neighbor_percentile_14.setValue(0.05)
        box_nearest_neighbor_percentile_14.local_path = "indexing.max_cell_estimation.nearest_neighbor_percentile"
        box_nearest_neighbor_percentile_14.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbor_percentile_14.addWidget(box_nearest_neighbor_percentile_14)
        bg_box.addLayout(hbox_lay_nearest_neighbor_percentile_14)

        label_15 = QLabel("    fft3d")
        label_15.setPalette(palette_scope)
        label_15.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_15)

        hbox_lay_peak_search_16 =  QHBoxLayout()
        label_peak_search_16 = QLabel("        peak_search")
        label_peak_search_16.setPalette(palette_object)
        label_peak_search_16.setFont(QFont("Monospace", 10))
        hbox_lay_peak_search_16.addWidget(label_peak_search_16)

        box_peak_search_16 = QComboBox()
        box_peak_search_16.local_path = "indexing.fft3d.peak_search"
        box_peak_search_16.tmp_lst=[]
        box_peak_search_16.tmp_lst.append("flood_fill")
        box_peak_search_16.tmp_lst.append("clean")
        for lst_itm in box_peak_search_16.tmp_lst:
            box_peak_search_16.addItem(lst_itm)
        box_peak_search_16.setCurrentIndex(0)
        box_peak_search_16.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_peak_search_16.addWidget(box_peak_search_16)
        bg_box.addLayout(hbox_lay_peak_search_16)

        hbox_lay_peak_volume_cutoff_17 =  QHBoxLayout()
        label_peak_volume_cutoff_17 = QLabel("        peak_volume_cutoff")
        label_peak_volume_cutoff_17.setPalette(palette_object)
        label_peak_volume_cutoff_17.setFont(QFont("Monospace", 10))
        hbox_lay_peak_volume_cutoff_17.addWidget(label_peak_volume_cutoff_17)

        box_peak_volume_cutoff_17 = QDoubleSpinBox()
        box_peak_volume_cutoff_17.setValue(0.15)
        box_peak_volume_cutoff_17.local_path = "indexing.fft3d.peak_volume_cutoff"
        box_peak_volume_cutoff_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_peak_volume_cutoff_17.addWidget(box_peak_volume_cutoff_17)
        bg_box.addLayout(hbox_lay_peak_volume_cutoff_17)

        label_18 = QLabel("        reciprocal_space_grid")
        label_18.setPalette(palette_scope)
        label_18.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_18)

        hbox_lay_n_points_19 =  QHBoxLayout()
        label_n_points_19 = QLabel("            n_points")
        label_n_points_19.setPalette(palette_object)
        label_n_points_19.setFont(QFont("Monospace", 10))
        hbox_lay_n_points_19.addWidget(label_n_points_19)

        box_n_points_19 = QSpinBox()
        box_n_points_19.setValue(256)
        box_n_points_19.local_path = "indexing.fft3d.reciprocal_space_grid.n_points"
        box_n_points_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_points_19.addWidget(box_n_points_19)
        bg_box.addLayout(hbox_lay_n_points_19)

        hbox_lay_d_min_20 =  QHBoxLayout()
        label_d_min_20 = QLabel("            d_min")
        label_d_min_20.setPalette(palette_object)
        label_d_min_20.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_20.addWidget(label_d_min_20)

        box_d_min_20 = QDoubleSpinBox()
        box_d_min_20.local_path = "indexing.fft3d.reciprocal_space_grid.d_min"
        box_d_min_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_20.addWidget(box_d_min_20)
        bg_box.addLayout(hbox_lay_d_min_20)

        hbox_lay_sigma_phi_deg_21 =  QHBoxLayout()
        label_sigma_phi_deg_21 = QLabel("    sigma_phi_deg")
        label_sigma_phi_deg_21.setPalette(palette_object)
        label_sigma_phi_deg_21.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_phi_deg_21.addWidget(label_sigma_phi_deg_21)

        box_sigma_phi_deg_21 = QDoubleSpinBox()
        box_sigma_phi_deg_21.local_path = "indexing.sigma_phi_deg"
        box_sigma_phi_deg_21.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_phi_deg_21.addWidget(box_sigma_phi_deg_21)
        bg_box.addLayout(hbox_lay_sigma_phi_deg_21)

        hbox_lay_b_iso_22 =  QHBoxLayout()
        label_b_iso_22 = QLabel("    b_iso")
        label_b_iso_22.setPalette(palette_object)
        label_b_iso_22.setFont(QFont("Monospace", 10))
        hbox_lay_b_iso_22.addWidget(label_b_iso_22)

        box_b_iso_22 = QDoubleSpinBox()
        box_b_iso_22.local_path = "indexing.b_iso"
        box_b_iso_22.valueChanged.connect(self.spnbox_changed)
        hbox_lay_b_iso_22.addWidget(box_b_iso_22)
        bg_box.addLayout(hbox_lay_b_iso_22)

        hbox_lay_rmsd_cutoff_23 =  QHBoxLayout()
        label_rmsd_cutoff_23 = QLabel("    rmsd_cutoff")
        label_rmsd_cutoff_23.setPalette(palette_object)
        label_rmsd_cutoff_23.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_23.addWidget(label_rmsd_cutoff_23)

        box_rmsd_cutoff_23 = QDoubleSpinBox()
        box_rmsd_cutoff_23.setValue(15.0)
        box_rmsd_cutoff_23.local_path = "indexing.rmsd_cutoff"
        box_rmsd_cutoff_23.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_cutoff_23.addWidget(box_rmsd_cutoff_23)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_23)

        hbox_lay_scan_range_24_0 =  QHBoxLayout()
        label_scan_range_24_0 = QLabel("    scan_range[1]")
        label_scan_range_24_0.setPalette(palette_object)
        label_scan_range_24_0.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_24_0.addWidget(label_scan_range_24_0)
        box_scan_range_24_0 = QSpinBox()
        box_scan_range_24_0.local_path = "indexing.scan_range"
        #box_scan_range_24_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_24_1 =  QHBoxLayout()
        label_scan_range_24_1 = QLabel("    scan_range[2]")
        label_scan_range_24_1.setPalette(palette_object)
        label_scan_range_24_1.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_24_1.addWidget(label_scan_range_24_1)
        box_scan_range_24_1 = QSpinBox()
        box_scan_range_24_1.local_path = "indexing.scan_range"
        #box_scan_range_24_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_24_0.addWidget(box_scan_range_24_0)
        bg_box.addLayout(hbox_lay_scan_range_24_0)
        hbox_lay_scan_range_24_1.addWidget(box_scan_range_24_1)
        bg_box.addLayout(hbox_lay_scan_range_24_1)

        label_25 = QLabel("    known_symmetry")
        label_25.setPalette(palette_scope)
        label_25.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_25)



        hbox_lay_relative_length_tolerance_28 =  QHBoxLayout()
        label_relative_length_tolerance_28 = QLabel("        relative_length_tolerance")
        label_relative_length_tolerance_28.setPalette(palette_object)
        label_relative_length_tolerance_28.setFont(QFont("Monospace", 10))
        hbox_lay_relative_length_tolerance_28.addWidget(label_relative_length_tolerance_28)

        box_relative_length_tolerance_28 = QDoubleSpinBox()
        box_relative_length_tolerance_28.setValue(0.1)
        box_relative_length_tolerance_28.local_path = "indexing.known_symmetry.relative_length_tolerance"
        box_relative_length_tolerance_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_relative_length_tolerance_28.addWidget(box_relative_length_tolerance_28)
        bg_box.addLayout(hbox_lay_relative_length_tolerance_28)

        hbox_lay_absolute_angle_tolerance_29 =  QHBoxLayout()
        label_absolute_angle_tolerance_29 = QLabel("        absolute_angle_tolerance")
        label_absolute_angle_tolerance_29.setPalette(palette_object)
        label_absolute_angle_tolerance_29.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_angle_tolerance_29.addWidget(label_absolute_angle_tolerance_29)

        box_absolute_angle_tolerance_29 = QDoubleSpinBox()
        box_absolute_angle_tolerance_29.setValue(5.0)
        box_absolute_angle_tolerance_29.local_path = "indexing.known_symmetry.absolute_angle_tolerance"
        box_absolute_angle_tolerance_29.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_angle_tolerance_29.addWidget(box_absolute_angle_tolerance_29)
        bg_box.addLayout(hbox_lay_absolute_angle_tolerance_29)

        hbox_lay_max_delta_30 =  QHBoxLayout()
        label_max_delta_30 = QLabel("        max_delta")
        label_max_delta_30.setPalette(palette_object)
        label_max_delta_30.setFont(QFont("Monospace", 10))
        hbox_lay_max_delta_30.addWidget(label_max_delta_30)

        box_max_delta_30 = QDoubleSpinBox()
        box_max_delta_30.setValue(5.0)
        box_max_delta_30.local_path = "indexing.known_symmetry.max_delta"
        box_max_delta_30.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_delta_30.addWidget(box_max_delta_30)
        bg_box.addLayout(hbox_lay_max_delta_30)

        label_31 = QLabel("    basis_vector_combinations")
        label_31.setPalette(palette_scope)
        label_31.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_31)

        hbox_lay_max_try_32 =  QHBoxLayout()
        label_max_try_32 = QLabel("        max_try")
        label_max_try_32.setPalette(palette_object)
        label_max_try_32.setFont(QFont("Monospace", 10))
        hbox_lay_max_try_32.addWidget(label_max_try_32)

        box_max_try_32 = QSpinBox()
        box_max_try_32.setValue(50)
        box_max_try_32.local_path = "indexing.basis_vector_combinations.max_try"
        box_max_try_32.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_try_32.addWidget(box_max_try_32)
        bg_box.addLayout(hbox_lay_max_try_32)

        hbox_lay_sys_absent_threshold_33 =  QHBoxLayout()
        label_sys_absent_threshold_33 = QLabel("        sys_absent_threshold")
        label_sys_absent_threshold_33.setPalette(palette_object)
        label_sys_absent_threshold_33.setFont(QFont("Monospace", 10))
        hbox_lay_sys_absent_threshold_33.addWidget(label_sys_absent_threshold_33)

        box_sys_absent_threshold_33 = QDoubleSpinBox()
        box_sys_absent_threshold_33.setValue(0.9)
        box_sys_absent_threshold_33.local_path = "indexing.basis_vector_combinations.sys_absent_threshold"
        box_sys_absent_threshold_33.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sys_absent_threshold_33.addWidget(box_sys_absent_threshold_33)
        bg_box.addLayout(hbox_lay_sys_absent_threshold_33)

        hbox_lay_solution_scorer_34 =  QHBoxLayout()
        label_solution_scorer_34 = QLabel("        solution_scorer")
        label_solution_scorer_34.setPalette(palette_object)
        label_solution_scorer_34.setFont(QFont("Monospace", 10))
        hbox_lay_solution_scorer_34.addWidget(label_solution_scorer_34)

        box_solution_scorer_34 = QComboBox()
        box_solution_scorer_34.local_path = "indexing.basis_vector_combinations.solution_scorer"
        box_solution_scorer_34.tmp_lst=[]
        box_solution_scorer_34.tmp_lst.append("filter")
        box_solution_scorer_34.tmp_lst.append("weighted")
        for lst_itm in box_solution_scorer_34.tmp_lst:
            box_solution_scorer_34.addItem(lst_itm)
        box_solution_scorer_34.setCurrentIndex(1)
        box_solution_scorer_34.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_solution_scorer_34.addWidget(box_solution_scorer_34)
        bg_box.addLayout(hbox_lay_solution_scorer_34)

        label_35 = QLabel("        filter")
        label_35.setPalette(palette_scope)
        label_35.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_35)

        hbox_lay_check_doubled_cell_36 =  QHBoxLayout()
        label_check_doubled_cell_36 = QLabel("            check_doubled_cell")
        label_check_doubled_cell_36.setPalette(palette_object)
        label_check_doubled_cell_36.setFont(QFont("Monospace", 10))
        hbox_lay_check_doubled_cell_36.addWidget(label_check_doubled_cell_36)

        box_check_doubled_cell_36 = QComboBox()
        box_check_doubled_cell_36.local_path = "indexing.basis_vector_combinations.filter.check_doubled_cell"
        box_check_doubled_cell_36.tmp_lst=[]
        box_check_doubled_cell_36.tmp_lst.append("True")
        box_check_doubled_cell_36.tmp_lst.append("False")
        for lst_itm in box_check_doubled_cell_36.tmp_lst:
            box_check_doubled_cell_36.addItem(lst_itm)
        box_check_doubled_cell_36.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_check_doubled_cell_36.addWidget(box_check_doubled_cell_36)
        bg_box.addLayout(hbox_lay_check_doubled_cell_36)

        hbox_lay_likelihood_cutoff_37 =  QHBoxLayout()
        label_likelihood_cutoff_37 = QLabel("            likelihood_cutoff")
        label_likelihood_cutoff_37.setPalette(palette_object)
        label_likelihood_cutoff_37.setFont(QFont("Monospace", 10))
        hbox_lay_likelihood_cutoff_37.addWidget(label_likelihood_cutoff_37)

        box_likelihood_cutoff_37 = QDoubleSpinBox()
        box_likelihood_cutoff_37.setValue(0.8)
        box_likelihood_cutoff_37.local_path = "indexing.basis_vector_combinations.filter.likelihood_cutoff"
        box_likelihood_cutoff_37.valueChanged.connect(self.spnbox_changed)
        hbox_lay_likelihood_cutoff_37.addWidget(box_likelihood_cutoff_37)
        bg_box.addLayout(hbox_lay_likelihood_cutoff_37)

        hbox_lay_volume_cutoff_38 =  QHBoxLayout()
        label_volume_cutoff_38 = QLabel("            volume_cutoff")
        label_volume_cutoff_38.setPalette(palette_object)
        label_volume_cutoff_38.setFont(QFont("Monospace", 10))
        hbox_lay_volume_cutoff_38.addWidget(label_volume_cutoff_38)

        box_volume_cutoff_38 = QDoubleSpinBox()
        box_volume_cutoff_38.setValue(1.25)
        box_volume_cutoff_38.local_path = "indexing.basis_vector_combinations.filter.volume_cutoff"
        box_volume_cutoff_38.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_cutoff_38.addWidget(box_volume_cutoff_38)
        bg_box.addLayout(hbox_lay_volume_cutoff_38)

        hbox_lay_n_indexed_cutoff_39 =  QHBoxLayout()
        label_n_indexed_cutoff_39 = QLabel("            n_indexed_cutoff")
        label_n_indexed_cutoff_39.setPalette(palette_object)
        label_n_indexed_cutoff_39.setFont(QFont("Monospace", 10))
        hbox_lay_n_indexed_cutoff_39.addWidget(label_n_indexed_cutoff_39)

        box_n_indexed_cutoff_39 = QDoubleSpinBox()
        box_n_indexed_cutoff_39.setValue(0.9)
        box_n_indexed_cutoff_39.local_path = "indexing.basis_vector_combinations.filter.n_indexed_cutoff"
        box_n_indexed_cutoff_39.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_cutoff_39.addWidget(box_n_indexed_cutoff_39)
        bg_box.addLayout(hbox_lay_n_indexed_cutoff_39)

        label_40 = QLabel("        weighted")
        label_40.setPalette(palette_scope)
        label_40.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_40)

        hbox_lay_power_41 =  QHBoxLayout()
        label_power_41 = QLabel("            power")
        label_power_41.setPalette(palette_object)
        label_power_41.setFont(QFont("Monospace", 10))
        hbox_lay_power_41.addWidget(label_power_41)

        box_power_41 = QSpinBox()
        box_power_41.setValue(1)
        box_power_41.local_path = "indexing.basis_vector_combinations.weighted.power"
        box_power_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_power_41.addWidget(box_power_41)
        bg_box.addLayout(hbox_lay_power_41)

        hbox_lay_volume_weight_42 =  QHBoxLayout()
        label_volume_weight_42 = QLabel("            volume_weight")
        label_volume_weight_42.setPalette(palette_object)
        label_volume_weight_42.setFont(QFont("Monospace", 10))
        hbox_lay_volume_weight_42.addWidget(label_volume_weight_42)

        box_volume_weight_42 = QDoubleSpinBox()
        box_volume_weight_42.setValue(1.0)
        box_volume_weight_42.local_path = "indexing.basis_vector_combinations.weighted.volume_weight"
        box_volume_weight_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_weight_42.addWidget(box_volume_weight_42)
        bg_box.addLayout(hbox_lay_volume_weight_42)

        hbox_lay_n_indexed_weight_43 =  QHBoxLayout()
        label_n_indexed_weight_43 = QLabel("            n_indexed_weight")
        label_n_indexed_weight_43.setPalette(palette_object)
        label_n_indexed_weight_43.setFont(QFont("Monospace", 10))
        hbox_lay_n_indexed_weight_43.addWidget(label_n_indexed_weight_43)

        box_n_indexed_weight_43 = QDoubleSpinBox()
        box_n_indexed_weight_43.setValue(1.0)
        box_n_indexed_weight_43.local_path = "indexing.basis_vector_combinations.weighted.n_indexed_weight"
        box_n_indexed_weight_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_weight_43.addWidget(box_n_indexed_weight_43)
        bg_box.addLayout(hbox_lay_n_indexed_weight_43)

        hbox_lay_rmsd_weight_44 =  QHBoxLayout()
        label_rmsd_weight_44 = QLabel("            rmsd_weight")
        label_rmsd_weight_44.setPalette(palette_object)
        label_rmsd_weight_44.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_weight_44.addWidget(label_rmsd_weight_44)

        box_rmsd_weight_44 = QDoubleSpinBox()
        box_rmsd_weight_44.setValue(1.0)
        box_rmsd_weight_44.local_path = "indexing.basis_vector_combinations.weighted.rmsd_weight"
        box_rmsd_weight_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_weight_44.addWidget(box_rmsd_weight_44)
        bg_box.addLayout(hbox_lay_rmsd_weight_44)

        label_45 = QLabel("    index_assignment")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_45)

        hbox_lay_method_46 =  QHBoxLayout()
        label_method_46 = QLabel("        method")
        label_method_46.setPalette(palette_object)
        label_method_46.setFont(QFont("Monospace", 10))
        hbox_lay_method_46.addWidget(label_method_46)

        box_method_46 = QComboBox()
        box_method_46.local_path = "indexing.index_assignment.method"
        box_method_46.tmp_lst=[]
        box_method_46.tmp_lst.append("simple")
        box_method_46.tmp_lst.append("local")
        for lst_itm in box_method_46.tmp_lst:
            box_method_46.addItem(lst_itm)
        box_method_46.setCurrentIndex(0)
        box_method_46.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_46.addWidget(box_method_46)
        bg_box.addLayout(hbox_lay_method_46)

        label_47 = QLabel("        simple")
        label_47.setPalette(palette_scope)
        label_47.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_47)

        hbox_lay_hkl_tolerance_48 =  QHBoxLayout()
        label_hkl_tolerance_48 = QLabel("            hkl_tolerance")
        label_hkl_tolerance_48.setPalette(palette_object)
        label_hkl_tolerance_48.setFont(QFont("Monospace", 10))
        hbox_lay_hkl_tolerance_48.addWidget(label_hkl_tolerance_48)

        box_hkl_tolerance_48 = QDoubleSpinBox()
        box_hkl_tolerance_48.setValue(0.3)
        box_hkl_tolerance_48.local_path = "indexing.index_assignment.simple.hkl_tolerance"
        box_hkl_tolerance_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hkl_tolerance_48.addWidget(box_hkl_tolerance_48)
        bg_box.addLayout(hbox_lay_hkl_tolerance_48)

        label_49 = QLabel("        local")
        label_49.setPalette(palette_scope)
        label_49.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_49)

        hbox_lay_epsilon_50 =  QHBoxLayout()
        label_epsilon_50 = QLabel("            epsilon")
        label_epsilon_50.setPalette(palette_object)
        label_epsilon_50.setFont(QFont("Monospace", 10))
        hbox_lay_epsilon_50.addWidget(label_epsilon_50)

        box_epsilon_50 = QDoubleSpinBox()
        box_epsilon_50.setValue(0.05)
        box_epsilon_50.local_path = "indexing.index_assignment.local.epsilon"
        box_epsilon_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_epsilon_50.addWidget(box_epsilon_50)
        bg_box.addLayout(hbox_lay_epsilon_50)

        hbox_lay_delta_51 =  QHBoxLayout()
        label_delta_51 = QLabel("            delta")
        label_delta_51.setPalette(palette_object)
        label_delta_51.setFont(QFont("Monospace", 10))
        hbox_lay_delta_51.addWidget(label_delta_51)

        box_delta_51 = QSpinBox()
        box_delta_51.setValue(8)
        box_delta_51.local_path = "indexing.index_assignment.local.delta"
        box_delta_51.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delta_51.addWidget(box_delta_51)
        bg_box.addLayout(hbox_lay_delta_51)

        hbox_lay_l_min_52 =  QHBoxLayout()
        label_l_min_52 = QLabel("            l_min")
        label_l_min_52.setPalette(palette_object)
        label_l_min_52.setFont(QFont("Monospace", 10))
        hbox_lay_l_min_52.addWidget(label_l_min_52)

        box_l_min_52 = QDoubleSpinBox()
        box_l_min_52.setValue(0.8)
        box_l_min_52.local_path = "indexing.index_assignment.local.l_min"
        box_l_min_52.valueChanged.connect(self.spnbox_changed)
        hbox_lay_l_min_52.addWidget(box_l_min_52)
        bg_box.addLayout(hbox_lay_l_min_52)

        hbox_lay_nearest_neighbours_53 =  QHBoxLayout()
        label_nearest_neighbours_53 = QLabel("            nearest_neighbours")
        label_nearest_neighbours_53.setPalette(palette_object)
        label_nearest_neighbours_53.setFont(QFont("Monospace", 10))
        hbox_lay_nearest_neighbours_53.addWidget(label_nearest_neighbours_53)

        box_nearest_neighbours_53 = QSpinBox()
        box_nearest_neighbours_53.setValue(20)
        box_nearest_neighbours_53.local_path = "indexing.index_assignment.local.nearest_neighbours"
        box_nearest_neighbours_53.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbours_53.addWidget(box_nearest_neighbours_53)
        bg_box.addLayout(hbox_lay_nearest_neighbours_53)

        label_54 = QLabel("    check_misindexing")
        label_54.setPalette(palette_scope)
        label_54.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_54)

        hbox_lay_grid_search_scope_55 =  QHBoxLayout()
        label_grid_search_scope_55 = QLabel("        grid_search_scope")
        label_grid_search_scope_55.setPalette(palette_object)
        label_grid_search_scope_55.setFont(QFont("Monospace", 10))
        hbox_lay_grid_search_scope_55.addWidget(label_grid_search_scope_55)

        box_grid_search_scope_55 = QSpinBox()
        box_grid_search_scope_55.setValue(0)
        box_grid_search_scope_55.local_path = "indexing.check_misindexing.grid_search_scope"
        box_grid_search_scope_55.valueChanged.connect(self.spnbox_changed)
        hbox_lay_grid_search_scope_55.addWidget(box_grid_search_scope_55)
        bg_box.addLayout(hbox_lay_grid_search_scope_55)

        hbox_lay_optimise_initial_basis_vectors_56 =  QHBoxLayout()
        label_optimise_initial_basis_vectors_56 = QLabel("    optimise_initial_basis_vectors")
        label_optimise_initial_basis_vectors_56.setPalette(palette_object)
        label_optimise_initial_basis_vectors_56.setFont(QFont("Monospace", 10))
        hbox_lay_optimise_initial_basis_vectors_56.addWidget(label_optimise_initial_basis_vectors_56)

        box_optimise_initial_basis_vectors_56 = QComboBox()
        box_optimise_initial_basis_vectors_56.local_path = "indexing.optimise_initial_basis_vectors"
        box_optimise_initial_basis_vectors_56.tmp_lst=[]
        box_optimise_initial_basis_vectors_56.tmp_lst.append("True")
        box_optimise_initial_basis_vectors_56.tmp_lst.append("False")
        for lst_itm in box_optimise_initial_basis_vectors_56.tmp_lst:
            box_optimise_initial_basis_vectors_56.addItem(lst_itm)
        box_optimise_initial_basis_vectors_56.setCurrentIndex(1)
        box_optimise_initial_basis_vectors_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_optimise_initial_basis_vectors_56.addWidget(box_optimise_initial_basis_vectors_56)
        bg_box.addLayout(hbox_lay_optimise_initial_basis_vectors_56)

        hbox_lay_debug_57 =  QHBoxLayout()
        label_debug_57 = QLabel("    debug")
        label_debug_57.setPalette(palette_object)
        label_debug_57.setFont(QFont("Monospace", 10))
        hbox_lay_debug_57.addWidget(label_debug_57)

        box_debug_57 = QComboBox()
        box_debug_57.local_path = "indexing.debug"
        box_debug_57.tmp_lst=[]
        box_debug_57.tmp_lst.append("True")
        box_debug_57.tmp_lst.append("False")
        for lst_itm in box_debug_57.tmp_lst:
            box_debug_57.addItem(lst_itm)
        box_debug_57.setCurrentIndex(1)
        box_debug_57.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_57.addWidget(box_debug_57)
        bg_box.addLayout(hbox_lay_debug_57)

        hbox_lay_debug_plots_58 =  QHBoxLayout()
        label_debug_plots_58 = QLabel("    debug_plots")
        label_debug_plots_58.setPalette(palette_object)
        label_debug_plots_58.setFont(QFont("Monospace", 10))
        hbox_lay_debug_plots_58.addWidget(label_debug_plots_58)

        box_debug_plots_58 = QComboBox()
        box_debug_plots_58.local_path = "indexing.debug_plots"
        box_debug_plots_58.tmp_lst=[]
        box_debug_plots_58.tmp_lst.append("True")
        box_debug_plots_58.tmp_lst.append("False")
        for lst_itm in box_debug_plots_58.tmp_lst:
            box_debug_plots_58.addItem(lst_itm)
        box_debug_plots_58.setCurrentIndex(1)
        box_debug_plots_58.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_plots_58.addWidget(box_debug_plots_58)
        bg_box.addLayout(hbox_lay_debug_plots_58)

        hbox_lay_combine_scans_59 =  QHBoxLayout()
        label_combine_scans_59 = QLabel("    combine_scans")
        label_combine_scans_59.setPalette(palette_object)
        label_combine_scans_59.setFont(QFont("Monospace", 10))
        hbox_lay_combine_scans_59.addWidget(label_combine_scans_59)

        box_combine_scans_59 = QComboBox()
        box_combine_scans_59.local_path = "indexing.combine_scans"
        box_combine_scans_59.tmp_lst=[]
        box_combine_scans_59.tmp_lst.append("True")
        box_combine_scans_59.tmp_lst.append("False")
        for lst_itm in box_combine_scans_59.tmp_lst:
            box_combine_scans_59.addItem(lst_itm)
        box_combine_scans_59.setCurrentIndex(1)
        box_combine_scans_59.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_combine_scans_59.addWidget(box_combine_scans_59)
        bg_box.addLayout(hbox_lay_combine_scans_59)

        label_60 = QLabel("    refinement_protocol")
        label_60.setPalette(palette_scope)
        label_60.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_60)

        hbox_lay_n_macro_cycles_61 =  QHBoxLayout()
        label_n_macro_cycles_61 = QLabel("        n_macro_cycles")
        label_n_macro_cycles_61.setPalette(palette_object)
        label_n_macro_cycles_61.setFont(QFont("Monospace", 10))
        hbox_lay_n_macro_cycles_61.addWidget(label_n_macro_cycles_61)

        box_n_macro_cycles_61 = QSpinBox()
        box_n_macro_cycles_61.local_path = "indexing.refinement_protocol.n_macro_cycles"
        box_n_macro_cycles_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_macro_cycles_61.addWidget(box_n_macro_cycles_61)
        bg_box.addLayout(hbox_lay_n_macro_cycles_61)

        hbox_lay_d_min_step_62 =  QHBoxLayout()
        label_d_min_step_62 = QLabel("        d_min_step")
        label_d_min_step_62.setPalette(palette_object)
        label_d_min_step_62.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_step_62.addWidget(label_d_min_step_62)

        box_d_min_step_62 = QDoubleSpinBox()
        box_d_min_step_62.local_path = "indexing.refinement_protocol.d_min_step"
        box_d_min_step_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_step_62.addWidget(box_d_min_step_62)
        bg_box.addLayout(hbox_lay_d_min_step_62)

        hbox_lay_d_min_start_63 =  QHBoxLayout()
        label_d_min_start_63 = QLabel("        d_min_start")
        label_d_min_start_63.setPalette(palette_object)
        label_d_min_start_63.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_start_63.addWidget(label_d_min_start_63)

        box_d_min_start_63 = QDoubleSpinBox()
        box_d_min_start_63.local_path = "indexing.refinement_protocol.d_min_start"
        box_d_min_start_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_start_63.addWidget(box_d_min_start_63)
        bg_box.addLayout(hbox_lay_d_min_start_63)

        hbox_lay_d_min_final_64 =  QHBoxLayout()
        label_d_min_final_64 = QLabel("        d_min_final")
        label_d_min_final_64.setPalette(palette_object)
        label_d_min_final_64.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_final_64.addWidget(label_d_min_final_64)

        box_d_min_final_64 = QDoubleSpinBox()
        box_d_min_final_64.local_path = "indexing.refinement_protocol.d_min_final"
        box_d_min_final_64.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_final_64.addWidget(box_d_min_final_64)
        bg_box.addLayout(hbox_lay_d_min_final_64)

        hbox_lay_verbosity_65 =  QHBoxLayout()
        label_verbosity_65 = QLabel("        verbosity")
        label_verbosity_65.setPalette(palette_object)
        label_verbosity_65.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_65.addWidget(label_verbosity_65)

        box_verbosity_65 = QSpinBox()
        box_verbosity_65.setValue(1)
        box_verbosity_65.local_path = "indexing.refinement_protocol.verbosity"
        box_verbosity_65.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_65.addWidget(box_verbosity_65)
        bg_box.addLayout(hbox_lay_verbosity_65)

        hbox_lay_disable_unit_cell_volume_sanity_check_66 =  QHBoxLayout()
        label_disable_unit_cell_volume_sanity_check_66 = QLabel("        disable_unit_cell_volume_sanity_check")
        label_disable_unit_cell_volume_sanity_check_66.setPalette(palette_object)
        label_disable_unit_cell_volume_sanity_check_66.setFont(QFont("Monospace", 10))
        hbox_lay_disable_unit_cell_volume_sanity_check_66.addWidget(label_disable_unit_cell_volume_sanity_check_66)

        box_disable_unit_cell_volume_sanity_check_66 = QComboBox()
        box_disable_unit_cell_volume_sanity_check_66.local_path = "indexing.refinement_protocol.disable_unit_cell_volume_sanity_check"
        box_disable_unit_cell_volume_sanity_check_66.tmp_lst=[]
        box_disable_unit_cell_volume_sanity_check_66.tmp_lst.append("True")
        box_disable_unit_cell_volume_sanity_check_66.tmp_lst.append("False")
        for lst_itm in box_disable_unit_cell_volume_sanity_check_66.tmp_lst:
            box_disable_unit_cell_volume_sanity_check_66.addItem(lst_itm)
        box_disable_unit_cell_volume_sanity_check_66.setCurrentIndex(1)
        box_disable_unit_cell_volume_sanity_check_66.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_disable_unit_cell_volume_sanity_check_66.addWidget(box_disable_unit_cell_volume_sanity_check_66)
        bg_box.addLayout(hbox_lay_disable_unit_cell_volume_sanity_check_66)

        hbox_lay_method_67 =  QHBoxLayout()
        label_method_67 = QLabel("    method")
        label_method_67.setPalette(palette_object)
        label_method_67.setFont(QFont("Monospace", 10))
        hbox_lay_method_67.addWidget(label_method_67)

        box_method_67 = QComboBox()
        box_method_67.local_path = "indexing.method"
        box_method_67.tmp_lst=[]
        box_method_67.tmp_lst.append("fft3d")
        box_method_67.tmp_lst.append("fft1d")
        box_method_67.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_67.tmp_lst:
            box_method_67.addItem(lst_itm)
        box_method_67.setCurrentIndex(0)
        box_method_67.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_67.addWidget(box_method_67)
        bg_box.addLayout(hbox_lay_method_67)

        label_68 = QLabel("    multiple_lattice_search")
        label_68.setPalette(palette_scope)
        label_68.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_68)

        hbox_lay_cluster_analysis_search_69 =  QHBoxLayout()
        label_cluster_analysis_search_69 = QLabel("        cluster_analysis_search")
        label_cluster_analysis_search_69.setPalette(palette_object)
        label_cluster_analysis_search_69.setFont(QFont("Monospace", 10))
        hbox_lay_cluster_analysis_search_69.addWidget(label_cluster_analysis_search_69)

        box_cluster_analysis_search_69 = QComboBox()
        box_cluster_analysis_search_69.local_path = "indexing.multiple_lattice_search.cluster_analysis_search"
        box_cluster_analysis_search_69.tmp_lst=[]
        box_cluster_analysis_search_69.tmp_lst.append("True")
        box_cluster_analysis_search_69.tmp_lst.append("False")
        for lst_itm in box_cluster_analysis_search_69.tmp_lst:
            box_cluster_analysis_search_69.addItem(lst_itm)
        box_cluster_analysis_search_69.setCurrentIndex(1)
        box_cluster_analysis_search_69.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cluster_analysis_search_69.addWidget(box_cluster_analysis_search_69)
        bg_box.addLayout(hbox_lay_cluster_analysis_search_69)

        hbox_lay_recycle_unindexed_reflections_cutoff_70 =  QHBoxLayout()
        label_recycle_unindexed_reflections_cutoff_70 = QLabel("        recycle_unindexed_reflections_cutoff")
        label_recycle_unindexed_reflections_cutoff_70.setPalette(palette_object)
        label_recycle_unindexed_reflections_cutoff_70.setFont(QFont("Monospace", 10))
        hbox_lay_recycle_unindexed_reflections_cutoff_70.addWidget(label_recycle_unindexed_reflections_cutoff_70)

        box_recycle_unindexed_reflections_cutoff_70 = QDoubleSpinBox()
        box_recycle_unindexed_reflections_cutoff_70.setValue(0.1)
        box_recycle_unindexed_reflections_cutoff_70.local_path = "indexing.multiple_lattice_search.recycle_unindexed_reflections_cutoff"
        box_recycle_unindexed_reflections_cutoff_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_recycle_unindexed_reflections_cutoff_70.addWidget(box_recycle_unindexed_reflections_cutoff_70)
        bg_box.addLayout(hbox_lay_recycle_unindexed_reflections_cutoff_70)

        hbox_lay_minimum_angular_separation_71 =  QHBoxLayout()
        label_minimum_angular_separation_71 = QLabel("        minimum_angular_separation")
        label_minimum_angular_separation_71.setPalette(palette_object)
        label_minimum_angular_separation_71.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_angular_separation_71.addWidget(label_minimum_angular_separation_71)

        box_minimum_angular_separation_71 = QDoubleSpinBox()
        box_minimum_angular_separation_71.setValue(5.0)
        box_minimum_angular_separation_71.local_path = "indexing.multiple_lattice_search.minimum_angular_separation"
        box_minimum_angular_separation_71.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_angular_separation_71.addWidget(box_minimum_angular_separation_71)
        bg_box.addLayout(hbox_lay_minimum_angular_separation_71)

        hbox_lay_max_lattices_72 =  QHBoxLayout()
        label_max_lattices_72 = QLabel("        max_lattices")
        label_max_lattices_72.setPalette(palette_object)
        label_max_lattices_72.setFont(QFont("Monospace", 10))
        hbox_lay_max_lattices_72.addWidget(label_max_lattices_72)

        box_max_lattices_72 = QSpinBox()
        box_max_lattices_72.setValue(1)
        box_max_lattices_72.local_path = "indexing.multiple_lattice_search.max_lattices"
        box_max_lattices_72.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_lattices_72.addWidget(box_max_lattices_72)
        bg_box.addLayout(hbox_lay_max_lattices_72)

        label_73 = QLabel("        cluster_analysis")
        label_73.setPalette(palette_scope)
        label_73.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_73)

        hbox_lay_method_74 =  QHBoxLayout()
        label_method_74 = QLabel("            method")
        label_method_74.setPalette(palette_object)
        label_method_74.setFont(QFont("Monospace", 10))
        hbox_lay_method_74.addWidget(label_method_74)

        box_method_74 = QComboBox()
        box_method_74.local_path = "indexing.multiple_lattice_search.cluster_analysis.method"
        box_method_74.tmp_lst=[]
        box_method_74.tmp_lst.append("dbscan")
        box_method_74.tmp_lst.append("hcluster")
        for lst_itm in box_method_74.tmp_lst:
            box_method_74.addItem(lst_itm)
        box_method_74.setCurrentIndex(0)
        box_method_74.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_74.addWidget(box_method_74)
        bg_box.addLayout(hbox_lay_method_74)

        label_75 = QLabel("            hcluster")
        label_75.setPalette(palette_scope)
        label_75.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_75)

        label_76 = QLabel("                linkage")
        label_76.setPalette(palette_scope)
        label_76.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_76)

        hbox_lay_method_77 =  QHBoxLayout()
        label_method_77 = QLabel("                    method")
        label_method_77.setPalette(palette_object)
        label_method_77.setFont(QFont("Monospace", 10))
        hbox_lay_method_77.addWidget(label_method_77)

        box_method_77 = QComboBox()
        box_method_77.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.method"
        box_method_77.tmp_lst=[]
        box_method_77.tmp_lst.append("ward")
        for lst_itm in box_method_77.tmp_lst:
            box_method_77.addItem(lst_itm)
        box_method_77.setCurrentIndex(0)
        box_method_77.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_77.addWidget(box_method_77)
        bg_box.addLayout(hbox_lay_method_77)

        hbox_lay_metric_78 =  QHBoxLayout()
        label_metric_78 = QLabel("                    metric")
        label_metric_78.setPalette(palette_object)
        label_metric_78.setFont(QFont("Monospace", 10))
        hbox_lay_metric_78.addWidget(label_metric_78)

        box_metric_78 = QComboBox()
        box_metric_78.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.metric"
        box_metric_78.tmp_lst=[]
        box_metric_78.tmp_lst.append("euclidean")
        for lst_itm in box_metric_78.tmp_lst:
            box_metric_78.addItem(lst_itm)
        box_metric_78.setCurrentIndex(0)
        box_metric_78.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_metric_78.addWidget(box_metric_78)
        bg_box.addLayout(hbox_lay_metric_78)

        hbox_lay_cutoff_79 =  QHBoxLayout()
        label_cutoff_79 = QLabel("                cutoff")
        label_cutoff_79.setPalette(palette_object)
        label_cutoff_79.setFont(QFont("Monospace", 10))
        hbox_lay_cutoff_79.addWidget(label_cutoff_79)

        box_cutoff_79 = QDoubleSpinBox()
        box_cutoff_79.setValue(15.0)
        box_cutoff_79.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff"
        box_cutoff_79.valueChanged.connect(self.spnbox_changed)
        hbox_lay_cutoff_79.addWidget(box_cutoff_79)
        bg_box.addLayout(hbox_lay_cutoff_79)

        hbox_lay_cutoff_criterion_80 =  QHBoxLayout()
        label_cutoff_criterion_80 = QLabel("                cutoff_criterion")
        label_cutoff_criterion_80.setPalette(palette_object)
        label_cutoff_criterion_80.setFont(QFont("Monospace", 10))
        hbox_lay_cutoff_criterion_80.addWidget(label_cutoff_criterion_80)

        box_cutoff_criterion_80 = QComboBox()
        box_cutoff_criterion_80.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff_criterion"
        box_cutoff_criterion_80.tmp_lst=[]
        box_cutoff_criterion_80.tmp_lst.append("distance")
        box_cutoff_criterion_80.tmp_lst.append("inconsistent")
        for lst_itm in box_cutoff_criterion_80.tmp_lst:
            box_cutoff_criterion_80.addItem(lst_itm)
        box_cutoff_criterion_80.setCurrentIndex(0)
        box_cutoff_criterion_80.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cutoff_criterion_80.addWidget(box_cutoff_criterion_80)
        bg_box.addLayout(hbox_lay_cutoff_criterion_80)

        label_81 = QLabel("            dbscan")
        label_81.setPalette(palette_scope)
        label_81.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_81)

        hbox_lay_eps_82 =  QHBoxLayout()
        label_eps_82 = QLabel("                eps")
        label_eps_82.setPalette(palette_object)
        label_eps_82.setFont(QFont("Monospace", 10))
        hbox_lay_eps_82.addWidget(label_eps_82)

        box_eps_82 = QDoubleSpinBox()
        box_eps_82.setValue(0.05)
        box_eps_82.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.eps"
        box_eps_82.valueChanged.connect(self.spnbox_changed)
        hbox_lay_eps_82.addWidget(box_eps_82)
        bg_box.addLayout(hbox_lay_eps_82)

        hbox_lay_min_samples_83 =  QHBoxLayout()
        label_min_samples_83 = QLabel("                min_samples")
        label_min_samples_83.setPalette(palette_object)
        label_min_samples_83.setFont(QFont("Monospace", 10))
        hbox_lay_min_samples_83.addWidget(label_min_samples_83)

        box_min_samples_83 = QSpinBox()
        box_min_samples_83.setValue(30)
        box_min_samples_83.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.min_samples"
        box_min_samples_83.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_samples_83.addWidget(box_min_samples_83)
        bg_box.addLayout(hbox_lay_min_samples_83)

        hbox_lay_min_cluster_size_84 =  QHBoxLayout()
        label_min_cluster_size_84 = QLabel("            min_cluster_size")
        label_min_cluster_size_84.setPalette(palette_object)
        label_min_cluster_size_84.setFont(QFont("Monospace", 10))
        hbox_lay_min_cluster_size_84.addWidget(label_min_cluster_size_84)

        box_min_cluster_size_84 = QSpinBox()
        box_min_cluster_size_84.setValue(20)
        box_min_cluster_size_84.local_path = "indexing.multiple_lattice_search.cluster_analysis.min_cluster_size"
        box_min_cluster_size_84.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cluster_size_84.addWidget(box_min_cluster_size_84)
        bg_box.addLayout(hbox_lay_min_cluster_size_84)

        hbox_lay_intersection_union_ratio_cutoff_85 =  QHBoxLayout()
        label_intersection_union_ratio_cutoff_85 = QLabel("            intersection_union_ratio_cutoff")
        label_intersection_union_ratio_cutoff_85.setPalette(palette_object)
        label_intersection_union_ratio_cutoff_85.setFont(QFont("Monospace", 10))
        hbox_lay_intersection_union_ratio_cutoff_85.addWidget(label_intersection_union_ratio_cutoff_85)

        box_intersection_union_ratio_cutoff_85 = QDoubleSpinBox()
        box_intersection_union_ratio_cutoff_85.setValue(0.4)
        box_intersection_union_ratio_cutoff_85.local_path = "indexing.multiple_lattice_search.cluster_analysis.intersection_union_ratio_cutoff"
        box_intersection_union_ratio_cutoff_85.valueChanged.connect(self.spnbox_changed)
        hbox_lay_intersection_union_ratio_cutoff_85.addWidget(box_intersection_union_ratio_cutoff_85)
        bg_box.addLayout(hbox_lay_intersection_union_ratio_cutoff_85)

        label_86 = QLabel("    real_space_grid_search")
        label_86.setPalette(palette_scope)
        label_86.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_86)

        hbox_lay_characteristic_grid_87 =  QHBoxLayout()
        label_characteristic_grid_87 = QLabel("        characteristic_grid")
        label_characteristic_grid_87.setPalette(palette_object)
        label_characteristic_grid_87.setFont(QFont("Monospace", 10))
        hbox_lay_characteristic_grid_87.addWidget(label_characteristic_grid_87)

        box_characteristic_grid_87 = QDoubleSpinBox()
        box_characteristic_grid_87.setValue(0.02)
        box_characteristic_grid_87.local_path = "indexing.real_space_grid_search.characteristic_grid"
        box_characteristic_grid_87.valueChanged.connect(self.spnbox_changed)
        hbox_lay_characteristic_grid_87.addWidget(box_characteristic_grid_87)
        bg_box.addLayout(hbox_lay_characteristic_grid_87)

        label_88 = QLabel("    stills")
        label_88.setPalette(palette_scope)
        label_88.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_88)

        hbox_lay_indexer_89 =  QHBoxLayout()
        label_indexer_89 = QLabel("        indexer")
        label_indexer_89.setPalette(palette_object)
        label_indexer_89.setFont(QFont("Monospace", 10))
        hbox_lay_indexer_89.addWidget(label_indexer_89)

        box_indexer_89 = QComboBox()
        box_indexer_89.local_path = "indexing.stills.indexer"
        box_indexer_89.tmp_lst=[]
        box_indexer_89.tmp_lst.append("Auto")
        box_indexer_89.tmp_lst.append("stills")
        box_indexer_89.tmp_lst.append("sweeps")
        for lst_itm in box_indexer_89.tmp_lst:
            box_indexer_89.addItem(lst_itm)
        box_indexer_89.setCurrentIndex(0)
        box_indexer_89.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_indexer_89.addWidget(box_indexer_89)
        bg_box.addLayout(hbox_lay_indexer_89)

        hbox_lay_ewald_proximity_resolution_cutoff_90 =  QHBoxLayout()
        label_ewald_proximity_resolution_cutoff_90 = QLabel("        ewald_proximity_resolution_cutoff")
        label_ewald_proximity_resolution_cutoff_90.setPalette(palette_object)
        label_ewald_proximity_resolution_cutoff_90.setFont(QFont("Monospace", 10))
        hbox_lay_ewald_proximity_resolution_cutoff_90.addWidget(label_ewald_proximity_resolution_cutoff_90)

        box_ewald_proximity_resolution_cutoff_90 = QDoubleSpinBox()
        box_ewald_proximity_resolution_cutoff_90.setValue(2.0)
        box_ewald_proximity_resolution_cutoff_90.local_path = "indexing.stills.ewald_proximity_resolution_cutoff"
        box_ewald_proximity_resolution_cutoff_90.valueChanged.connect(self.spnbox_changed)
        hbox_lay_ewald_proximity_resolution_cutoff_90.addWidget(box_ewald_proximity_resolution_cutoff_90)
        bg_box.addLayout(hbox_lay_ewald_proximity_resolution_cutoff_90)

        label_91 = QLabel("refinement")
        label_91.setPalette(palette_scope)
        label_91.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_91)

        label_92 = QLabel("    mp")
        label_92.setPalette(palette_scope)
        label_92.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_92)

        hbox_lay_nproc_93 =  QHBoxLayout()
        label_nproc_93 = QLabel("        nproc")
        label_nproc_93.setPalette(palette_object)
        label_nproc_93.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_93.addWidget(label_nproc_93)

        box_nproc_93 = QSpinBox()
        box_nproc_93.setValue(1)
        box_nproc_93.local_path = "refinement.mp.nproc"
        box_nproc_93.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_93.addWidget(box_nproc_93)
        bg_box.addLayout(hbox_lay_nproc_93)

        hbox_lay_verbosity_94 =  QHBoxLayout()
        label_verbosity_94 = QLabel("    verbosity")
        label_verbosity_94.setPalette(palette_object)
        label_verbosity_94.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_94.addWidget(label_verbosity_94)

        box_verbosity_94 = QSpinBox()
        box_verbosity_94.setValue(0)
        box_verbosity_94.local_path = "refinement.verbosity"
        box_verbosity_94.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_94.addWidget(box_verbosity_94)
        bg_box.addLayout(hbox_lay_verbosity_94)

        label_95 = QLabel("    parameterisation")
        label_95.setPalette(palette_scope)
        label_95.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_95)

        label_96 = QLabel("        auto_reduction")
        label_96.setPalette(palette_scope)
        label_96.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_96)

        hbox_lay_min_nref_per_parameter_97 =  QHBoxLayout()
        label_min_nref_per_parameter_97 = QLabel("            min_nref_per_parameter")
        label_min_nref_per_parameter_97.setPalette(palette_object)
        label_min_nref_per_parameter_97.setFont(QFont("Monospace", 10))
        hbox_lay_min_nref_per_parameter_97.addWidget(label_min_nref_per_parameter_97)

        box_min_nref_per_parameter_97 = QSpinBox()
        box_min_nref_per_parameter_97.setValue(5)
        box_min_nref_per_parameter_97.local_path = "refinement.parameterisation.auto_reduction.min_nref_per_parameter"
        box_min_nref_per_parameter_97.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_nref_per_parameter_97.addWidget(box_min_nref_per_parameter_97)
        bg_box.addLayout(hbox_lay_min_nref_per_parameter_97)

        hbox_lay_action_98 =  QHBoxLayout()
        label_action_98 = QLabel("            action")
        label_action_98.setPalette(palette_object)
        label_action_98.setFont(QFont("Monospace", 10))
        hbox_lay_action_98.addWidget(label_action_98)

        box_action_98 = QComboBox()
        box_action_98.local_path = "refinement.parameterisation.auto_reduction.action"
        box_action_98.tmp_lst=[]
        box_action_98.tmp_lst.append("fail")
        box_action_98.tmp_lst.append("fix")
        box_action_98.tmp_lst.append("remove")
        for lst_itm in box_action_98.tmp_lst:
            box_action_98.addItem(lst_itm)
        box_action_98.setCurrentIndex(0)
        box_action_98.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_action_98.addWidget(box_action_98)
        bg_box.addLayout(hbox_lay_action_98)

        label_99 = QLabel("        beam")
        label_99.setPalette(palette_scope)
        label_99.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_99)

        hbox_lay_fix_100 =  QHBoxLayout()
        label_fix_100 = QLabel("            fix")
        label_fix_100.setPalette(palette_object)
        label_fix_100.setFont(QFont("Monospace", 10))
        hbox_lay_fix_100.addWidget(label_fix_100)

        box_fix_100 = QComboBox()
        box_fix_100.local_path = "refinement.parameterisation.beam.fix"
        box_fix_100.tmp_lst=[]
        box_fix_100.tmp_lst.append("all")
        box_fix_100.tmp_lst.append("in_spindle_plane")
        box_fix_100.tmp_lst.append("out_spindle_plane")
        box_fix_100.tmp_lst.append("wavelength")
        for lst_itm in box_fix_100.tmp_lst:
            box_fix_100.addItem(lst_itm)
        box_fix_100.setCurrentIndex(3)
        box_fix_100.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_100.addWidget(box_fix_100)
        bg_box.addLayout(hbox_lay_fix_100)


        label_102 = QLabel("        crystal")
        label_102.setPalette(palette_scope)
        label_102.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_102)

        hbox_lay_fix_103 =  QHBoxLayout()
        label_fix_103 = QLabel("            fix")
        label_fix_103.setPalette(palette_object)
        label_fix_103.setFont(QFont("Monospace", 10))
        hbox_lay_fix_103.addWidget(label_fix_103)

        box_fix_103 = QComboBox()
        box_fix_103.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_103.tmp_lst=[]
        box_fix_103.tmp_lst.append("all")
        box_fix_103.tmp_lst.append("cell")
        box_fix_103.tmp_lst.append("orientation")
        for lst_itm in box_fix_103.tmp_lst:
            box_fix_103.addItem(lst_itm)
        box_fix_103.setCurrentIndex(0)
        box_fix_103.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_103.addWidget(box_fix_103)
        bg_box.addLayout(hbox_lay_fix_103)

        label_104 = QLabel("            unit_cell")
        label_104.setPalette(palette_scope)
        label_104.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_104)


        label_106 = QLabel("                restraints")
        label_106.setPalette(palette_scope)
        label_106.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_106)

        label_107 = QLabel("                    tie_to_target")
        label_107.setPalette(palette_scope)
        label_107.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_107)

        hbox_lay_values_108_0 =  QHBoxLayout()
        label_values_108_0 = QLabel("                        values[1]")
        label_values_108_0.setPalette(palette_object)
        label_values_108_0.setFont(QFont("Monospace", 10))
        hbox_lay_values_108_0.addWidget(label_values_108_0)
        box_values_108_0 = QDoubleSpinBox()
        box_values_108_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_108_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_108_1 =  QHBoxLayout()
        label_values_108_1 = QLabel("                        values[2]")
        label_values_108_1.setPalette(palette_object)
        label_values_108_1.setFont(QFont("Monospace", 10))
        hbox_lay_values_108_1.addWidget(label_values_108_1)
        box_values_108_1 = QDoubleSpinBox()
        box_values_108_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_108_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_108_2 =  QHBoxLayout()
        label_values_108_2 = QLabel("                        values[3]")
        label_values_108_2.setPalette(palette_object)
        label_values_108_2.setFont(QFont("Monospace", 10))
        hbox_lay_values_108_2.addWidget(label_values_108_2)
        box_values_108_2 = QDoubleSpinBox()
        box_values_108_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_108_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_108_3 =  QHBoxLayout()
        label_values_108_3 = QLabel("                        values[4]")
        label_values_108_3.setPalette(palette_object)
        label_values_108_3.setFont(QFont("Monospace", 10))
        hbox_lay_values_108_3.addWidget(label_values_108_3)
        box_values_108_3 = QDoubleSpinBox()
        box_values_108_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_108_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_108_4 =  QHBoxLayout()
        label_values_108_4 = QLabel("                        values[5]")
        label_values_108_4.setPalette(palette_object)
        label_values_108_4.setFont(QFont("Monospace", 10))
        hbox_lay_values_108_4.addWidget(label_values_108_4)
        box_values_108_4 = QDoubleSpinBox()
        box_values_108_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_108_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_108_5 =  QHBoxLayout()
        label_values_108_5 = QLabel("                        values[6]")
        label_values_108_5.setPalette(palette_object)
        label_values_108_5.setFont(QFont("Monospace", 10))
        hbox_lay_values_108_5.addWidget(label_values_108_5)
        box_values_108_5 = QDoubleSpinBox()
        box_values_108_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_108_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_sigmas_109_0 =  QHBoxLayout()
        label_sigmas_109_0 = QLabel("                        sigmas[1]")
        label_sigmas_109_0.setPalette(palette_object)
        label_sigmas_109_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_109_0.addWidget(label_sigmas_109_0)
        box_sigmas_109_0 = QDoubleSpinBox()
        box_sigmas_109_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_109_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_109_1 =  QHBoxLayout()
        label_sigmas_109_1 = QLabel("                        sigmas[2]")
        label_sigmas_109_1.setPalette(palette_object)
        label_sigmas_109_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_109_1.addWidget(label_sigmas_109_1)
        box_sigmas_109_1 = QDoubleSpinBox()
        box_sigmas_109_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_109_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_109_2 =  QHBoxLayout()
        label_sigmas_109_2 = QLabel("                        sigmas[3]")
        label_sigmas_109_2.setPalette(palette_object)
        label_sigmas_109_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_109_2.addWidget(label_sigmas_109_2)
        box_sigmas_109_2 = QDoubleSpinBox()
        box_sigmas_109_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_109_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_109_3 =  QHBoxLayout()
        label_sigmas_109_3 = QLabel("                        sigmas[4]")
        label_sigmas_109_3.setPalette(palette_object)
        label_sigmas_109_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_109_3.addWidget(label_sigmas_109_3)
        box_sigmas_109_3 = QDoubleSpinBox()
        box_sigmas_109_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_109_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_109_4 =  QHBoxLayout()
        label_sigmas_109_4 = QLabel("                        sigmas[5]")
        label_sigmas_109_4.setPalette(palette_object)
        label_sigmas_109_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_109_4.addWidget(label_sigmas_109_4)
        box_sigmas_109_4 = QDoubleSpinBox()
        box_sigmas_109_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_109_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_109_5 =  QHBoxLayout()
        label_sigmas_109_5 = QLabel("                        sigmas[6]")
        label_sigmas_109_5.setPalette(palette_object)
        label_sigmas_109_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_109_5.addWidget(label_sigmas_109_5)
        box_sigmas_109_5 = QDoubleSpinBox()
        box_sigmas_109_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_109_5.valueChanged.connect(self.spnbox_changed)


        hbox_lay_apply_to_all_111 =  QHBoxLayout()
        label_apply_to_all_111 = QLabel("                        apply_to_all")
        label_apply_to_all_111.setPalette(palette_object)
        label_apply_to_all_111.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_111.addWidget(label_apply_to_all_111)

        box_apply_to_all_111 = QComboBox()
        box_apply_to_all_111.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.apply_to_all"
        box_apply_to_all_111.tmp_lst=[]
        box_apply_to_all_111.tmp_lst.append("True")
        box_apply_to_all_111.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_111.tmp_lst:
            box_apply_to_all_111.addItem(lst_itm)
        box_apply_to_all_111.setCurrentIndex(1)
        box_apply_to_all_111.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_111.addWidget(box_apply_to_all_111)
        bg_box.addLayout(hbox_lay_apply_to_all_111)

        label_112 = QLabel("                    tie_to_group")
        label_112.setPalette(palette_scope)
        label_112.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_112)

        hbox_lay_target_113 =  QHBoxLayout()
        label_target_113 = QLabel("                        target")
        label_target_113.setPalette(palette_object)
        label_target_113.setFont(QFont("Monospace", 10))
        hbox_lay_target_113.addWidget(label_target_113)

        box_target_113 = QComboBox()
        box_target_113.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_113.tmp_lst=[]
        box_target_113.tmp_lst.append("mean")
        box_target_113.tmp_lst.append("low_memory_mean")
        box_target_113.tmp_lst.append("median")
        for lst_itm in box_target_113.tmp_lst:
            box_target_113.addItem(lst_itm)
        box_target_113.setCurrentIndex(0)
        box_target_113.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_113.addWidget(box_target_113)
        bg_box.addLayout(hbox_lay_target_113)

        hbox_lay_sigmas_114_0 =  QHBoxLayout()
        label_sigmas_114_0 = QLabel("                        sigmas[1]")
        label_sigmas_114_0.setPalette(palette_object)
        label_sigmas_114_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_114_0.addWidget(label_sigmas_114_0)
        box_sigmas_114_0 = QDoubleSpinBox()
        box_sigmas_114_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_114_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_114_1 =  QHBoxLayout()
        label_sigmas_114_1 = QLabel("                        sigmas[2]")
        label_sigmas_114_1.setPalette(palette_object)
        label_sigmas_114_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_114_1.addWidget(label_sigmas_114_1)
        box_sigmas_114_1 = QDoubleSpinBox()
        box_sigmas_114_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_114_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_114_2 =  QHBoxLayout()
        label_sigmas_114_2 = QLabel("                        sigmas[3]")
        label_sigmas_114_2.setPalette(palette_object)
        label_sigmas_114_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_114_2.addWidget(label_sigmas_114_2)
        box_sigmas_114_2 = QDoubleSpinBox()
        box_sigmas_114_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_114_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_114_3 =  QHBoxLayout()
        label_sigmas_114_3 = QLabel("                        sigmas[4]")
        label_sigmas_114_3.setPalette(palette_object)
        label_sigmas_114_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_114_3.addWidget(label_sigmas_114_3)
        box_sigmas_114_3 = QDoubleSpinBox()
        box_sigmas_114_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_114_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_114_4 =  QHBoxLayout()
        label_sigmas_114_4 = QLabel("                        sigmas[5]")
        label_sigmas_114_4.setPalette(palette_object)
        label_sigmas_114_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_114_4.addWidget(label_sigmas_114_4)
        box_sigmas_114_4 = QDoubleSpinBox()
        box_sigmas_114_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_114_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_114_5 =  QHBoxLayout()
        label_sigmas_114_5 = QLabel("                        sigmas[6]")
        label_sigmas_114_5.setPalette(palette_object)
        label_sigmas_114_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_114_5.addWidget(label_sigmas_114_5)
        box_sigmas_114_5 = QDoubleSpinBox()
        box_sigmas_114_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_114_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_114_0.addWidget(box_sigmas_114_0)
        bg_box.addLayout(hbox_lay_sigmas_114_0)
        hbox_lay_sigmas_114_1.addWidget(box_sigmas_114_1)
        bg_box.addLayout(hbox_lay_sigmas_114_1)
        hbox_lay_sigmas_114_2.addWidget(box_sigmas_114_2)
        bg_box.addLayout(hbox_lay_sigmas_114_2)
        hbox_lay_sigmas_114_3.addWidget(box_sigmas_114_3)
        bg_box.addLayout(hbox_lay_sigmas_114_3)
        hbox_lay_sigmas_114_4.addWidget(box_sigmas_114_4)
        bg_box.addLayout(hbox_lay_sigmas_114_4)
        hbox_lay_sigmas_114_5.addWidget(box_sigmas_114_5)
        bg_box.addLayout(hbox_lay_sigmas_114_5)


        hbox_lay_apply_to_all_116 =  QHBoxLayout()
        label_apply_to_all_116 = QLabel("                        apply_to_all")
        label_apply_to_all_116.setPalette(palette_object)
        label_apply_to_all_116.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_116.addWidget(label_apply_to_all_116)

        box_apply_to_all_116 = QComboBox()
        box_apply_to_all_116.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.apply_to_all"
        box_apply_to_all_116.tmp_lst=[]
        box_apply_to_all_116.tmp_lst.append("True")
        box_apply_to_all_116.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_116.tmp_lst:
            box_apply_to_all_116.addItem(lst_itm)
        box_apply_to_all_116.setCurrentIndex(1)
        box_apply_to_all_116.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_116.addWidget(box_apply_to_all_116)
        bg_box.addLayout(hbox_lay_apply_to_all_116)

        label_117 = QLabel("            orientation")
        label_117.setPalette(palette_scope)
        label_117.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_117)


        hbox_lay_scan_varying_119 =  QHBoxLayout()
        label_scan_varying_119 = QLabel("            scan_varying")
        label_scan_varying_119.setPalette(palette_object)
        label_scan_varying_119.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_119.addWidget(label_scan_varying_119)

        box_scan_varying_119 = QComboBox()
        box_scan_varying_119.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_119.tmp_lst=[]
        box_scan_varying_119.tmp_lst.append("True")
        box_scan_varying_119.tmp_lst.append("False")
        for lst_itm in box_scan_varying_119.tmp_lst:
            box_scan_varying_119.addItem(lst_itm)
        box_scan_varying_119.setCurrentIndex(1)
        box_scan_varying_119.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_119.addWidget(box_scan_varying_119)
        bg_box.addLayout(hbox_lay_scan_varying_119)

        hbox_lay_num_intervals_120 =  QHBoxLayout()
        label_num_intervals_120 = QLabel("            num_intervals")
        label_num_intervals_120.setPalette(palette_object)
        label_num_intervals_120.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_120.addWidget(label_num_intervals_120)

        box_num_intervals_120 = QComboBox()
        box_num_intervals_120.local_path = "refinement.parameterisation.crystal.num_intervals"
        box_num_intervals_120.tmp_lst=[]
        box_num_intervals_120.tmp_lst.append("fixed_width")
        box_num_intervals_120.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_120.tmp_lst:
            box_num_intervals_120.addItem(lst_itm)
        box_num_intervals_120.setCurrentIndex(0)
        box_num_intervals_120.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_120.addWidget(box_num_intervals_120)
        bg_box.addLayout(hbox_lay_num_intervals_120)

        hbox_lay_interval_width_degrees_121 =  QHBoxLayout()
        label_interval_width_degrees_121 = QLabel("            interval_width_degrees")
        label_interval_width_degrees_121.setPalette(palette_object)
        label_interval_width_degrees_121.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_121.addWidget(label_interval_width_degrees_121)

        box_interval_width_degrees_121 = QDoubleSpinBox()
        box_interval_width_degrees_121.setValue(36.0)
        box_interval_width_degrees_121.local_path = "refinement.parameterisation.crystal.interval_width_degrees"
        box_interval_width_degrees_121.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_121.addWidget(box_interval_width_degrees_121)
        bg_box.addLayout(hbox_lay_interval_width_degrees_121)

        hbox_lay_absolute_num_intervals_122 =  QHBoxLayout()
        label_absolute_num_intervals_122 = QLabel("            absolute_num_intervals")
        label_absolute_num_intervals_122.setPalette(palette_object)
        label_absolute_num_intervals_122.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_122.addWidget(label_absolute_num_intervals_122)

        box_absolute_num_intervals_122 = QSpinBox()
        box_absolute_num_intervals_122.setValue(5)
        box_absolute_num_intervals_122.local_path = "refinement.parameterisation.crystal.absolute_num_intervals"
        box_absolute_num_intervals_122.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_122.addWidget(box_absolute_num_intervals_122)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_122)

        hbox_lay_UB_model_per_123 =  QHBoxLayout()
        label_UB_model_per_123 = QLabel("            UB_model_per")
        label_UB_model_per_123.setPalette(palette_object)
        label_UB_model_per_123.setFont(QFont("Monospace", 10))
        hbox_lay_UB_model_per_123.addWidget(label_UB_model_per_123)

        box_UB_model_per_123 = QComboBox()
        box_UB_model_per_123.local_path = "refinement.parameterisation.crystal.UB_model_per"
        box_UB_model_per_123.tmp_lst=[]
        box_UB_model_per_123.tmp_lst.append("reflection")
        box_UB_model_per_123.tmp_lst.append("image")
        box_UB_model_per_123.tmp_lst.append("block")
        for lst_itm in box_UB_model_per_123.tmp_lst:
            box_UB_model_per_123.addItem(lst_itm)
        box_UB_model_per_123.setCurrentIndex(2)
        box_UB_model_per_123.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_UB_model_per_123.addWidget(box_UB_model_per_123)
        bg_box.addLayout(hbox_lay_UB_model_per_123)

        label_124 = QLabel("        detector")
        label_124.setPalette(palette_scope)
        label_124.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_124)

        hbox_lay_panels_125 =  QHBoxLayout()
        label_panels_125 = QLabel("            panels")
        label_panels_125.setPalette(palette_object)
        label_panels_125.setFont(QFont("Monospace", 10))
        hbox_lay_panels_125.addWidget(label_panels_125)

        box_panels_125 = QComboBox()
        box_panels_125.local_path = "refinement.parameterisation.detector.panels"
        box_panels_125.tmp_lst=[]
        box_panels_125.tmp_lst.append("automatic")
        box_panels_125.tmp_lst.append("single")
        box_panels_125.tmp_lst.append("multiple")
        box_panels_125.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_125.tmp_lst:
            box_panels_125.addItem(lst_itm)
        box_panels_125.setCurrentIndex(0)
        box_panels_125.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_125.addWidget(box_panels_125)
        bg_box.addLayout(hbox_lay_panels_125)

        hbox_lay_hierarchy_level_126 =  QHBoxLayout()
        label_hierarchy_level_126 = QLabel("            hierarchy_level")
        label_hierarchy_level_126.setPalette(palette_object)
        label_hierarchy_level_126.setFont(QFont("Monospace", 10))
        hbox_lay_hierarchy_level_126.addWidget(label_hierarchy_level_126)

        box_hierarchy_level_126 = QSpinBox()
        box_hierarchy_level_126.setValue(0)
        box_hierarchy_level_126.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_126.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_126.addWidget(box_hierarchy_level_126)
        bg_box.addLayout(hbox_lay_hierarchy_level_126)

        hbox_lay_fix_127 =  QHBoxLayout()
        label_fix_127 = QLabel("            fix")
        label_fix_127.setPalette(palette_object)
        label_fix_127.setFont(QFont("Monospace", 10))
        hbox_lay_fix_127.addWidget(label_fix_127)

        box_fix_127 = QComboBox()
        box_fix_127.local_path = "refinement.parameterisation.detector.fix"
        box_fix_127.tmp_lst=[]
        box_fix_127.tmp_lst.append("all")
        box_fix_127.tmp_lst.append("position")
        box_fix_127.tmp_lst.append("orientation")
        for lst_itm in box_fix_127.tmp_lst:
            box_fix_127.addItem(lst_itm)
        box_fix_127.setCurrentIndex(0)
        box_fix_127.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_127.addWidget(box_fix_127)
        bg_box.addLayout(hbox_lay_fix_127)


        hbox_lay_sparse_129 =  QHBoxLayout()
        label_sparse_129 = QLabel("        sparse")
        label_sparse_129.setPalette(palette_object)
        label_sparse_129.setFont(QFont("Monospace", 10))
        hbox_lay_sparse_129.addWidget(label_sparse_129)

        box_sparse_129 = QComboBox()
        box_sparse_129.local_path = "refinement.parameterisation.sparse"
        box_sparse_129.tmp_lst=[]
        box_sparse_129.tmp_lst.append("True")
        box_sparse_129.tmp_lst.append("False")
        for lst_itm in box_sparse_129.tmp_lst:
            box_sparse_129.addItem(lst_itm)
        box_sparse_129.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_129.addWidget(box_sparse_129)
        bg_box.addLayout(hbox_lay_sparse_129)

        hbox_lay_treat_single_image_as_still_130 =  QHBoxLayout()
        label_treat_single_image_as_still_130 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_130.setPalette(palette_object)
        label_treat_single_image_as_still_130.setFont(QFont("Monospace", 10))
        hbox_lay_treat_single_image_as_still_130.addWidget(label_treat_single_image_as_still_130)

        box_treat_single_image_as_still_130 = QComboBox()
        box_treat_single_image_as_still_130.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_130.tmp_lst=[]
        box_treat_single_image_as_still_130.tmp_lst.append("True")
        box_treat_single_image_as_still_130.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_130.tmp_lst:
            box_treat_single_image_as_still_130.addItem(lst_itm)
        box_treat_single_image_as_still_130.setCurrentIndex(1)
        box_treat_single_image_as_still_130.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_130.addWidget(box_treat_single_image_as_still_130)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_130)

        label_131 = QLabel("    refinery")
        label_131.setPalette(palette_scope)
        label_131.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_131)

        hbox_lay_engine_132 =  QHBoxLayout()
        label_engine_132 = QLabel("        engine")
        label_engine_132.setPalette(palette_object)
        label_engine_132.setFont(QFont("Monospace", 10))
        hbox_lay_engine_132.addWidget(label_engine_132)

        box_engine_132 = QComboBox()
        box_engine_132.local_path = "refinement.refinery.engine"
        box_engine_132.tmp_lst=[]
        box_engine_132.tmp_lst.append("SimpleLBFGS")
        box_engine_132.tmp_lst.append("LBFGScurvs")
        box_engine_132.tmp_lst.append("GaussNewton")
        box_engine_132.tmp_lst.append("LevMar")
        box_engine_132.tmp_lst.append("SparseLevMar")
        for lst_itm in box_engine_132.tmp_lst:
            box_engine_132.addItem(lst_itm)
        box_engine_132.setCurrentIndex(3)
        box_engine_132.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_132.addWidget(box_engine_132)
        bg_box.addLayout(hbox_lay_engine_132)

        hbox_lay_track_step_133 =  QHBoxLayout()
        label_track_step_133 = QLabel("        track_step")
        label_track_step_133.setPalette(palette_object)
        label_track_step_133.setFont(QFont("Monospace", 10))
        hbox_lay_track_step_133.addWidget(label_track_step_133)

        box_track_step_133 = QComboBox()
        box_track_step_133.local_path = "refinement.refinery.track_step"
        box_track_step_133.tmp_lst=[]
        box_track_step_133.tmp_lst.append("True")
        box_track_step_133.tmp_lst.append("False")
        for lst_itm in box_track_step_133.tmp_lst:
            box_track_step_133.addItem(lst_itm)
        box_track_step_133.setCurrentIndex(1)
        box_track_step_133.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_133.addWidget(box_track_step_133)
        bg_box.addLayout(hbox_lay_track_step_133)

        hbox_lay_track_gradient_134 =  QHBoxLayout()
        label_track_gradient_134 = QLabel("        track_gradient")
        label_track_gradient_134.setPalette(palette_object)
        label_track_gradient_134.setFont(QFont("Monospace", 10))
        hbox_lay_track_gradient_134.addWidget(label_track_gradient_134)

        box_track_gradient_134 = QComboBox()
        box_track_gradient_134.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_134.tmp_lst=[]
        box_track_gradient_134.tmp_lst.append("True")
        box_track_gradient_134.tmp_lst.append("False")
        for lst_itm in box_track_gradient_134.tmp_lst:
            box_track_gradient_134.addItem(lst_itm)
        box_track_gradient_134.setCurrentIndex(1)
        box_track_gradient_134.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_134.addWidget(box_track_gradient_134)
        bg_box.addLayout(hbox_lay_track_gradient_134)

        hbox_lay_track_parameter_correlation_135 =  QHBoxLayout()
        label_track_parameter_correlation_135 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_135.setPalette(palette_object)
        label_track_parameter_correlation_135.setFont(QFont("Monospace", 10))
        hbox_lay_track_parameter_correlation_135.addWidget(label_track_parameter_correlation_135)

        box_track_parameter_correlation_135 = QComboBox()
        box_track_parameter_correlation_135.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_135.tmp_lst=[]
        box_track_parameter_correlation_135.tmp_lst.append("True")
        box_track_parameter_correlation_135.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_135.tmp_lst:
            box_track_parameter_correlation_135.addItem(lst_itm)
        box_track_parameter_correlation_135.setCurrentIndex(1)
        box_track_parameter_correlation_135.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_135.addWidget(box_track_parameter_correlation_135)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_135)

        hbox_lay_track_out_of_sample_rmsd_136 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_136 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_136.setPalette(palette_object)
        label_track_out_of_sample_rmsd_136.setFont(QFont("Monospace", 10))
        hbox_lay_track_out_of_sample_rmsd_136.addWidget(label_track_out_of_sample_rmsd_136)

        box_track_out_of_sample_rmsd_136 = QComboBox()
        box_track_out_of_sample_rmsd_136.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_136.tmp_lst=[]
        box_track_out_of_sample_rmsd_136.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_136.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_136.tmp_lst:
            box_track_out_of_sample_rmsd_136.addItem(lst_itm)
        box_track_out_of_sample_rmsd_136.setCurrentIndex(1)
        box_track_out_of_sample_rmsd_136.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_136.addWidget(box_track_out_of_sample_rmsd_136)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_136)


        hbox_lay_max_iterations_138 =  QHBoxLayout()
        label_max_iterations_138 = QLabel("        max_iterations")
        label_max_iterations_138.setPalette(palette_object)
        label_max_iterations_138.setFont(QFont("Monospace", 10))
        hbox_lay_max_iterations_138.addWidget(label_max_iterations_138)

        box_max_iterations_138 = QSpinBox()
        box_max_iterations_138.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_138.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_138.addWidget(box_max_iterations_138)
        bg_box.addLayout(hbox_lay_max_iterations_138)

        label_139 = QLabel("    target")
        label_139.setPalette(palette_scope)
        label_139.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_139)

        hbox_lay_rmsd_cutoff_140 =  QHBoxLayout()
        label_rmsd_cutoff_140 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_140.setPalette(palette_object)
        label_rmsd_cutoff_140.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_140.addWidget(label_rmsd_cutoff_140)

        box_rmsd_cutoff_140 = QComboBox()
        box_rmsd_cutoff_140.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_140.tmp_lst=[]
        box_rmsd_cutoff_140.tmp_lst.append("fraction_of_bin_size")
        box_rmsd_cutoff_140.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_140.tmp_lst:
            box_rmsd_cutoff_140.addItem(lst_itm)
        box_rmsd_cutoff_140.setCurrentIndex(0)
        box_rmsd_cutoff_140.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_140.addWidget(box_rmsd_cutoff_140)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_140)

        hbox_lay_bin_size_fraction_141 =  QHBoxLayout()
        label_bin_size_fraction_141 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_141.setPalette(palette_object)
        label_bin_size_fraction_141.setFont(QFont("Monospace", 10))
        hbox_lay_bin_size_fraction_141.addWidget(label_bin_size_fraction_141)

        box_bin_size_fraction_141 = QDoubleSpinBox()
        box_bin_size_fraction_141.setValue(0.2)
        box_bin_size_fraction_141.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_141.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_141.addWidget(box_bin_size_fraction_141)
        bg_box.addLayout(hbox_lay_bin_size_fraction_141)

        hbox_lay_absolute_cutoffs_142_0 =  QHBoxLayout()
        label_absolute_cutoffs_142_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_142_0.setPalette(palette_object)
        label_absolute_cutoffs_142_0.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_142_0.addWidget(label_absolute_cutoffs_142_0)
        box_absolute_cutoffs_142_0 = QDoubleSpinBox()
        box_absolute_cutoffs_142_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_142_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_142_1 =  QHBoxLayout()
        label_absolute_cutoffs_142_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_142_1.setPalette(palette_object)
        label_absolute_cutoffs_142_1.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_142_1.addWidget(label_absolute_cutoffs_142_1)
        box_absolute_cutoffs_142_1 = QDoubleSpinBox()
        box_absolute_cutoffs_142_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_142_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_142_2 =  QHBoxLayout()
        label_absolute_cutoffs_142_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_142_2.setPalette(palette_object)
        label_absolute_cutoffs_142_2.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_142_2.addWidget(label_absolute_cutoffs_142_2)
        box_absolute_cutoffs_142_2 = QDoubleSpinBox()
        box_absolute_cutoffs_142_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_142_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_142_0.addWidget(box_absolute_cutoffs_142_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_142_0)
        hbox_lay_absolute_cutoffs_142_1.addWidget(box_absolute_cutoffs_142_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_142_1)
        hbox_lay_absolute_cutoffs_142_2.addWidget(box_absolute_cutoffs_142_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_142_2)

        hbox_lay_gradient_calculation_blocksize_143 =  QHBoxLayout()
        label_gradient_calculation_blocksize_143 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_143.setPalette(palette_object)
        label_gradient_calculation_blocksize_143.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_calculation_blocksize_143.addWidget(label_gradient_calculation_blocksize_143)

        box_gradient_calculation_blocksize_143 = QSpinBox()
        box_gradient_calculation_blocksize_143.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_143.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_143.addWidget(box_gradient_calculation_blocksize_143)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_143)

        label_144 = QLabel("    reflections")
        label_144.setPalette(palette_scope)
        label_144.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_144)

        hbox_lay_reflections_per_degree_145 =  QHBoxLayout()
        label_reflections_per_degree_145 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_145.setPalette(palette_object)
        label_reflections_per_degree_145.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_145.addWidget(label_reflections_per_degree_145)

        box_reflections_per_degree_145 = QDoubleSpinBox()
        box_reflections_per_degree_145.setValue(100.0)
        box_reflections_per_degree_145.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_145.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_145.addWidget(box_reflections_per_degree_145)
        bg_box.addLayout(hbox_lay_reflections_per_degree_145)

        hbox_lay_minimum_sample_size_146 =  QHBoxLayout()
        label_minimum_sample_size_146 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_146.setPalette(palette_object)
        label_minimum_sample_size_146.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_146.addWidget(label_minimum_sample_size_146)

        box_minimum_sample_size_146 = QSpinBox()
        box_minimum_sample_size_146.setValue(1000)
        box_minimum_sample_size_146.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_146.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_146.addWidget(box_minimum_sample_size_146)
        bg_box.addLayout(hbox_lay_minimum_sample_size_146)

        hbox_lay_maximum_sample_size_147 =  QHBoxLayout()
        label_maximum_sample_size_147 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_147.setPalette(palette_object)
        label_maximum_sample_size_147.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_147.addWidget(label_maximum_sample_size_147)

        box_maximum_sample_size_147 = QSpinBox()
        box_maximum_sample_size_147.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_147.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_147.addWidget(box_maximum_sample_size_147)
        bg_box.addLayout(hbox_lay_maximum_sample_size_147)

        hbox_lay_random_seed_148 =  QHBoxLayout()
        label_random_seed_148 = QLabel("        random_seed")
        label_random_seed_148.setPalette(palette_object)
        label_random_seed_148.setFont(QFont("Monospace", 10))
        hbox_lay_random_seed_148.addWidget(label_random_seed_148)

        box_random_seed_148 = QSpinBox()
        box_random_seed_148.setValue(42)
        box_random_seed_148.local_path = "refinement.reflections.random_seed"
        box_random_seed_148.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_148.addWidget(box_random_seed_148)
        bg_box.addLayout(hbox_lay_random_seed_148)

        hbox_lay_close_to_spindle_cutoff_149 =  QHBoxLayout()
        label_close_to_spindle_cutoff_149 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_149.setPalette(palette_object)
        label_close_to_spindle_cutoff_149.setFont(QFont("Monospace", 10))
        hbox_lay_close_to_spindle_cutoff_149.addWidget(label_close_to_spindle_cutoff_149)

        box_close_to_spindle_cutoff_149 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_149.setValue(0.02)
        box_close_to_spindle_cutoff_149.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_149.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_149.addWidget(box_close_to_spindle_cutoff_149)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_149)

        hbox_lay_block_width_150 =  QHBoxLayout()
        label_block_width_150 = QLabel("        block_width")
        label_block_width_150.setPalette(palette_object)
        label_block_width_150.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_150.addWidget(label_block_width_150)

        box_block_width_150 = QDoubleSpinBox()
        box_block_width_150.setValue(1.0)
        box_block_width_150.local_path = "refinement.reflections.block_width"
        box_block_width_150.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_150.addWidget(box_block_width_150)
        bg_box.addLayout(hbox_lay_block_width_150)

        label_151 = QLabel("        weighting_strategy")
        label_151.setPalette(palette_scope)
        label_151.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_151)

        hbox_lay_override_152 =  QHBoxLayout()
        label_override_152 = QLabel("            override")
        label_override_152.setPalette(palette_object)
        label_override_152.setFont(QFont("Monospace", 10))
        hbox_lay_override_152.addWidget(label_override_152)

        box_override_152 = QComboBox()
        box_override_152.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_152.tmp_lst=[]
        box_override_152.tmp_lst.append("statistical")
        box_override_152.tmp_lst.append("stills")
        box_override_152.tmp_lst.append("constant")
        for lst_itm in box_override_152.tmp_lst:
            box_override_152.addItem(lst_itm)
        box_override_152.setCurrentIndex(0)
        box_override_152.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_152.addWidget(box_override_152)
        bg_box.addLayout(hbox_lay_override_152)

        hbox_lay_delpsi_constant_153 =  QHBoxLayout()
        label_delpsi_constant_153 = QLabel("            delpsi_constant")
        label_delpsi_constant_153.setPalette(palette_object)
        label_delpsi_constant_153.setFont(QFont("Monospace", 10))
        hbox_lay_delpsi_constant_153.addWidget(label_delpsi_constant_153)

        box_delpsi_constant_153 = QDoubleSpinBox()
        box_delpsi_constant_153.setValue(1000000.0)
        box_delpsi_constant_153.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_153.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_153.addWidget(box_delpsi_constant_153)
        bg_box.addLayout(hbox_lay_delpsi_constant_153)

        hbox_lay_constants_154_0 =  QHBoxLayout()
        label_constants_154_0 = QLabel("            constants[1]")
        label_constants_154_0.setPalette(palette_object)
        label_constants_154_0.setFont(QFont("Monospace", 10))
        hbox_lay_constants_154_0.addWidget(label_constants_154_0)
        box_constants_154_0 = QDoubleSpinBox()
        box_constants_154_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_154_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_154_1 =  QHBoxLayout()
        label_constants_154_1 = QLabel("            constants[2]")
        label_constants_154_1.setPalette(palette_object)
        label_constants_154_1.setFont(QFont("Monospace", 10))
        hbox_lay_constants_154_1.addWidget(label_constants_154_1)
        box_constants_154_1 = QDoubleSpinBox()
        box_constants_154_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_154_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_154_2 =  QHBoxLayout()
        label_constants_154_2 = QLabel("            constants[3]")
        label_constants_154_2.setPalette(palette_object)
        label_constants_154_2.setFont(QFont("Monospace", 10))
        hbox_lay_constants_154_2.addWidget(label_constants_154_2)
        box_constants_154_2 = QDoubleSpinBox()
        box_constants_154_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_154_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_154_0.addWidget(box_constants_154_0)
        bg_box.addLayout(hbox_lay_constants_154_0)
        hbox_lay_constants_154_1.addWidget(box_constants_154_1)
        bg_box.addLayout(hbox_lay_constants_154_1)
        hbox_lay_constants_154_2.addWidget(box_constants_154_2)
        bg_box.addLayout(hbox_lay_constants_154_2)

        label_155 = QLabel("        outlier")
        label_155.setPalette(palette_scope)
        label_155.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_155)

        hbox_lay_algorithm_156 =  QHBoxLayout()
        label_algorithm_156 = QLabel("            algorithm")
        label_algorithm_156.setPalette(palette_object)
        label_algorithm_156.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_156.addWidget(label_algorithm_156)

        box_algorithm_156 = QComboBox()
        box_algorithm_156.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_156.tmp_lst=[]
        box_algorithm_156.tmp_lst.append("null")
        box_algorithm_156.tmp_lst.append("auto")
        box_algorithm_156.tmp_lst.append("mcd")
        box_algorithm_156.tmp_lst.append("tukey")
        box_algorithm_156.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_156.tmp_lst:
            box_algorithm_156.addItem(lst_itm)
        box_algorithm_156.setCurrentIndex(1)
        box_algorithm_156.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_156.addWidget(box_algorithm_156)
        bg_box.addLayout(hbox_lay_algorithm_156)

        hbox_lay_minimum_number_of_reflections_157 =  QHBoxLayout()
        label_minimum_number_of_reflections_157 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_157.setPalette(palette_object)
        label_minimum_number_of_reflections_157.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_number_of_reflections_157.addWidget(label_minimum_number_of_reflections_157)

        box_minimum_number_of_reflections_157 = QSpinBox()
        box_minimum_number_of_reflections_157.setValue(20)
        box_minimum_number_of_reflections_157.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_157.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_157.addWidget(box_minimum_number_of_reflections_157)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_157)

        hbox_lay_separate_experiments_158 =  QHBoxLayout()
        label_separate_experiments_158 = QLabel("            separate_experiments")
        label_separate_experiments_158.setPalette(palette_object)
        label_separate_experiments_158.setFont(QFont("Monospace", 10))
        hbox_lay_separate_experiments_158.addWidget(label_separate_experiments_158)

        box_separate_experiments_158 = QComboBox()
        box_separate_experiments_158.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_158.tmp_lst=[]
        box_separate_experiments_158.tmp_lst.append("True")
        box_separate_experiments_158.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_158.tmp_lst:
            box_separate_experiments_158.addItem(lst_itm)
        box_separate_experiments_158.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_158.addWidget(box_separate_experiments_158)
        bg_box.addLayout(hbox_lay_separate_experiments_158)

        hbox_lay_separate_panels_159 =  QHBoxLayout()
        label_separate_panels_159 = QLabel("            separate_panels")
        label_separate_panels_159.setPalette(palette_object)
        label_separate_panels_159.setFont(QFont("Monospace", 10))
        hbox_lay_separate_panels_159.addWidget(label_separate_panels_159)

        box_separate_panels_159 = QComboBox()
        box_separate_panels_159.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_159.tmp_lst=[]
        box_separate_panels_159.tmp_lst.append("True")
        box_separate_panels_159.tmp_lst.append("False")
        for lst_itm in box_separate_panels_159.tmp_lst:
            box_separate_panels_159.addItem(lst_itm)
        box_separate_panels_159.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_159.addWidget(box_separate_panels_159)
        bg_box.addLayout(hbox_lay_separate_panels_159)

        label_160 = QLabel("            tukey")
        label_160.setPalette(palette_scope)
        label_160.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_160)

        hbox_lay_iqr_multiplier_161 =  QHBoxLayout()
        label_iqr_multiplier_161 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_161.setPalette(palette_object)
        label_iqr_multiplier_161.setFont(QFont("Monospace", 10))
        hbox_lay_iqr_multiplier_161.addWidget(label_iqr_multiplier_161)

        box_iqr_multiplier_161 = QDoubleSpinBox()
        box_iqr_multiplier_161.setValue(1.5)
        box_iqr_multiplier_161.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_161.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_161.addWidget(box_iqr_multiplier_161)
        bg_box.addLayout(hbox_lay_iqr_multiplier_161)

        label_162 = QLabel("            mcd")
        label_162.setPalette(palette_scope)
        label_162.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_162)

        hbox_lay_alpha_163 =  QHBoxLayout()
        label_alpha_163 = QLabel("                alpha")
        label_alpha_163.setPalette(palette_object)
        label_alpha_163.setFont(QFont("Monospace", 10))
        hbox_lay_alpha_163.addWidget(label_alpha_163)

        box_alpha_163 = QDoubleSpinBox()
        box_alpha_163.setValue(0.5)
        box_alpha_163.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_163.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_163.addWidget(box_alpha_163)
        bg_box.addLayout(hbox_lay_alpha_163)

        hbox_lay_max_n_groups_164 =  QHBoxLayout()
        label_max_n_groups_164 = QLabel("                max_n_groups")
        label_max_n_groups_164.setPalette(palette_object)
        label_max_n_groups_164.setFont(QFont("Monospace", 10))
        hbox_lay_max_n_groups_164.addWidget(label_max_n_groups_164)

        box_max_n_groups_164 = QSpinBox()
        box_max_n_groups_164.setValue(5)
        box_max_n_groups_164.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_164.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_164.addWidget(box_max_n_groups_164)
        bg_box.addLayout(hbox_lay_max_n_groups_164)

        hbox_lay_min_group_size_165 =  QHBoxLayout()
        label_min_group_size_165 = QLabel("                min_group_size")
        label_min_group_size_165.setPalette(palette_object)
        label_min_group_size_165.setFont(QFont("Monospace", 10))
        hbox_lay_min_group_size_165.addWidget(label_min_group_size_165)

        box_min_group_size_165 = QSpinBox()
        box_min_group_size_165.setValue(300)
        box_min_group_size_165.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_165.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_165.addWidget(box_min_group_size_165)
        bg_box.addLayout(hbox_lay_min_group_size_165)

        hbox_lay_n_trials_166 =  QHBoxLayout()
        label_n_trials_166 = QLabel("                n_trials")
        label_n_trials_166.setPalette(palette_object)
        label_n_trials_166.setFont(QFont("Monospace", 10))
        hbox_lay_n_trials_166.addWidget(label_n_trials_166)

        box_n_trials_166 = QSpinBox()
        box_n_trials_166.setValue(500)
        box_n_trials_166.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_166.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_166.addWidget(box_n_trials_166)
        bg_box.addLayout(hbox_lay_n_trials_166)

        hbox_lay_k1_167 =  QHBoxLayout()
        label_k1_167 = QLabel("                k1")
        label_k1_167.setPalette(palette_object)
        label_k1_167.setFont(QFont("Monospace", 10))
        hbox_lay_k1_167.addWidget(label_k1_167)

        box_k1_167 = QSpinBox()
        box_k1_167.setValue(2)
        box_k1_167.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_167.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_167.addWidget(box_k1_167)
        bg_box.addLayout(hbox_lay_k1_167)

        hbox_lay_k2_168 =  QHBoxLayout()
        label_k2_168 = QLabel("                k2")
        label_k2_168.setPalette(palette_object)
        label_k2_168.setFont(QFont("Monospace", 10))
        hbox_lay_k2_168.addWidget(label_k2_168)

        box_k2_168 = QSpinBox()
        box_k2_168.setValue(2)
        box_k2_168.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_168.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_168.addWidget(box_k2_168)
        bg_box.addLayout(hbox_lay_k2_168)

        hbox_lay_k3_169 =  QHBoxLayout()
        label_k3_169 = QLabel("                k3")
        label_k3_169.setPalette(palette_object)
        label_k3_169.setFont(QFont("Monospace", 10))
        hbox_lay_k3_169.addWidget(label_k3_169)

        box_k3_169 = QSpinBox()
        box_k3_169.setValue(100)
        box_k3_169.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_169.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_169.addWidget(box_k3_169)
        bg_box.addLayout(hbox_lay_k3_169)

        hbox_lay_threshold_probability_170 =  QHBoxLayout()
        label_threshold_probability_170 = QLabel("                threshold_probability")
        label_threshold_probability_170.setPalette(palette_object)
        label_threshold_probability_170.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_probability_170.addWidget(label_threshold_probability_170)

        box_threshold_probability_170 = QDoubleSpinBox()
        box_threshold_probability_170.setValue(0.975)
        box_threshold_probability_170.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_170.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_170.addWidget(box_threshold_probability_170)
        bg_box.addLayout(hbox_lay_threshold_probability_170)

        label_171 = QLabel("            sauter_poon")
        label_171.setPalette(palette_scope)
        label_171.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_171)

        hbox_lay_px_sz_172_0 =  QHBoxLayout()
        label_px_sz_172_0 = QLabel("                px_sz[1]")
        label_px_sz_172_0.setPalette(palette_object)
        label_px_sz_172_0.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_172_0.addWidget(label_px_sz_172_0)
        box_px_sz_172_0 = QDoubleSpinBox()
        box_px_sz_172_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_172_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_172_1 =  QHBoxLayout()
        label_px_sz_172_1 = QLabel("                px_sz[2]")
        label_px_sz_172_1.setPalette(palette_object)
        label_px_sz_172_1.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_172_1.addWidget(label_px_sz_172_1)
        box_px_sz_172_1 = QDoubleSpinBox()
        box_px_sz_172_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_172_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_172_0.addWidget(box_px_sz_172_0)
        bg_box.addLayout(hbox_lay_px_sz_172_0)
        hbox_lay_px_sz_172_1.addWidget(box_px_sz_172_1)
        bg_box.addLayout(hbox_lay_px_sz_172_1)

        hbox_lay_verbose_173 =  QHBoxLayout()
        label_verbose_173 = QLabel("                verbose")
        label_verbose_173.setPalette(palette_object)
        label_verbose_173.setFont(QFont("Monospace", 10))
        hbox_lay_verbose_173.addWidget(label_verbose_173)

        box_verbose_173 = QComboBox()
        box_verbose_173.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_173.tmp_lst=[]
        box_verbose_173.tmp_lst.append("True")
        box_verbose_173.tmp_lst.append("False")
        for lst_itm in box_verbose_173.tmp_lst:
            box_verbose_173.addItem(lst_itm)
        box_verbose_173.setCurrentIndex(1)
        box_verbose_173.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_173.addWidget(box_verbose_173)
        bg_box.addLayout(hbox_lay_verbose_173)

        hbox_lay_pdf_174 =  QHBoxLayout()
        label_pdf_174 = QLabel("                pdf")
        label_pdf_174.setPalette(palette_object)
        label_pdf_174.setFont(QFont("Monospace", 10))
        hbox_lay_pdf_174.addWidget(label_pdf_174)

        box_pdf_174 = QLineEdit()
        box_pdf_174.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_174.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_174.addWidget(box_pdf_174)
        bg_box.addLayout(hbox_lay_pdf_174)

        label_175 = QLabel("output")
        label_175.setPalette(palette_scope)
        label_175.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_175)




        hbox_lay_log_179 =  QHBoxLayout()
        label_log_179 = QLabel("    log")
        label_log_179.setPalette(palette_object)
        label_log_179.setFont(QFont("Monospace", 10))
        hbox_lay_log_179.addWidget(label_log_179)

        box_log_179 = QLineEdit()
        box_log_179.local_path = "output.log"
        box_log_179.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_179.addWidget(box_log_179)
        bg_box.addLayout(hbox_lay_log_179)

        hbox_lay_debug_log_180 =  QHBoxLayout()
        label_debug_log_180 = QLabel("    debug_log")
        label_debug_log_180.setPalette(palette_object)
        label_debug_log_180.setFont(QFont("Monospace", 10))
        hbox_lay_debug_log_180.addWidget(label_debug_log_180)

        box_debug_log_180 = QLineEdit()
        box_debug_log_180.local_path = "output.debug_log"
        box_debug_log_180.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_180.addWidget(box_debug_log_180)
        bg_box.addLayout(hbox_lay_debug_log_180)

        hbox_lay_verbosity_181 =  QHBoxLayout()
        label_verbosity_181 = QLabel("verbosity")
        label_verbosity_181.setPalette(palette_object)
        label_verbosity_181.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_181.addWidget(label_verbosity_181)

        box_verbosity_181 = QSpinBox()
        box_verbosity_181.setValue(1)
        box_verbosity_181.local_path = "verbosity"
        box_verbosity_181.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_181.addWidget(box_verbosity_181)
        bg_box.addLayout(hbox_lay_verbosity_181)

 
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
