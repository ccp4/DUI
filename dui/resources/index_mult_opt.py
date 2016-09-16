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

        hbox_lay_mm_search_scope_2 =  QHBoxLayout()
        label_mm_search_scope_2 = QLabel("    mm_search_scope")
        label_mm_search_scope_2.setPalette(palette_object)
        label_mm_search_scope_2.setFont(QFont("Monospace", 10))
        hbox_lay_mm_search_scope_2.addWidget(label_mm_search_scope_2)

        box_mm_search_scope_2 = QDoubleSpinBox()
        box_mm_search_scope_2.setValue(4.0)
        box_mm_search_scope_2.local_path = "indexing.mm_search_scope"
        box_mm_search_scope_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_mm_search_scope_2.addWidget(box_mm_search_scope_2)
        bg_box.addLayout(hbox_lay_mm_search_scope_2)

        hbox_lay_wide_search_binning_3 =  QHBoxLayout()
        label_wide_search_binning_3 = QLabel("    wide_search_binning")
        label_wide_search_binning_3.setPalette(palette_object)
        label_wide_search_binning_3.setFont(QFont("Monospace", 10))
        hbox_lay_wide_search_binning_3.addWidget(label_wide_search_binning_3)

        box_wide_search_binning_3 = QDoubleSpinBox()
        box_wide_search_binning_3.setValue(2.0)
        box_wide_search_binning_3.local_path = "indexing.wide_search_binning"
        box_wide_search_binning_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_wide_search_binning_3.addWidget(box_wide_search_binning_3)
        bg_box.addLayout(hbox_lay_wide_search_binning_3)

        hbox_lay_min_cell_volume_4 =  QHBoxLayout()
        label_min_cell_volume_4 = QLabel("    min_cell_volume")
        label_min_cell_volume_4.setPalette(palette_object)
        label_min_cell_volume_4.setFont(QFont("Monospace", 10))
        hbox_lay_min_cell_volume_4.addWidget(label_min_cell_volume_4)

        box_min_cell_volume_4 = QDoubleSpinBox()
        box_min_cell_volume_4.setValue(25.0)
        box_min_cell_volume_4.local_path = "indexing.min_cell_volume"
        box_min_cell_volume_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cell_volume_4.addWidget(box_min_cell_volume_4)
        bg_box.addLayout(hbox_lay_min_cell_volume_4)

        hbox_lay_min_cell_5 =  QHBoxLayout()
        label_min_cell_5 = QLabel("    min_cell")
        label_min_cell_5.setPalette(palette_object)
        label_min_cell_5.setFont(QFont("Monospace", 10))
        hbox_lay_min_cell_5.addWidget(label_min_cell_5)

        box_min_cell_5 = QDoubleSpinBox()
        box_min_cell_5.setValue(3.0)
        box_min_cell_5.local_path = "indexing.min_cell"
        box_min_cell_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cell_5.addWidget(box_min_cell_5)
        bg_box.addLayout(hbox_lay_min_cell_5)

        hbox_lay_max_cell_6 =  QHBoxLayout()
        label_max_cell_6 = QLabel("    max_cell")
        label_max_cell_6.setPalette(palette_object)
        label_max_cell_6.setFont(QFont("Monospace", 10))
        hbox_lay_max_cell_6.addWidget(label_max_cell_6)

        box_max_cell_6 = QDoubleSpinBox()
        box_max_cell_6.local_path = "indexing.max_cell"
        box_max_cell_6.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_cell_6.addWidget(box_max_cell_6)
        bg_box.addLayout(hbox_lay_max_cell_6)

        label_7 = QLabel("    max_cell_estimation")
        label_7.setPalette(palette_scope)
        label_7.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_7)

        hbox_lay_filter_ice_8 =  QHBoxLayout()
        label_filter_ice_8 = QLabel("        filter_ice")
        label_filter_ice_8.setPalette(palette_object)
        label_filter_ice_8.setFont(QFont("Monospace", 10))
        hbox_lay_filter_ice_8.addWidget(label_filter_ice_8)

        box_filter_ice_8 = QComboBox()
        box_filter_ice_8.local_path = "indexing.max_cell_estimation.filter_ice"
        box_filter_ice_8.tmp_lst=[]
        box_filter_ice_8.tmp_lst.append("True")
        box_filter_ice_8.tmp_lst.append("False")
        for lst_itm in box_filter_ice_8.tmp_lst:
            box_filter_ice_8.addItem(lst_itm)
        box_filter_ice_8.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_ice_8.addWidget(box_filter_ice_8)
        bg_box.addLayout(hbox_lay_filter_ice_8)

        hbox_lay_filter_overlaps_9 =  QHBoxLayout()
        label_filter_overlaps_9 = QLabel("        filter_overlaps")
        label_filter_overlaps_9.setPalette(palette_object)
        label_filter_overlaps_9.setFont(QFont("Monospace", 10))
        hbox_lay_filter_overlaps_9.addWidget(label_filter_overlaps_9)

        box_filter_overlaps_9 = QComboBox()
        box_filter_overlaps_9.local_path = "indexing.max_cell_estimation.filter_overlaps"
        box_filter_overlaps_9.tmp_lst=[]
        box_filter_overlaps_9.tmp_lst.append("True")
        box_filter_overlaps_9.tmp_lst.append("False")
        for lst_itm in box_filter_overlaps_9.tmp_lst:
            box_filter_overlaps_9.addItem(lst_itm)
        box_filter_overlaps_9.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_overlaps_9.addWidget(box_filter_overlaps_9)
        bg_box.addLayout(hbox_lay_filter_overlaps_9)

        hbox_lay_overlaps_border_10 =  QHBoxLayout()
        label_overlaps_border_10 = QLabel("        overlaps_border")
        label_overlaps_border_10.setPalette(palette_object)
        label_overlaps_border_10.setFont(QFont("Monospace", 10))
        hbox_lay_overlaps_border_10.addWidget(label_overlaps_border_10)

        box_overlaps_border_10 = QSpinBox()
        box_overlaps_border_10.setValue(0)
        box_overlaps_border_10.local_path = "indexing.max_cell_estimation.overlaps_border"
        box_overlaps_border_10.valueChanged.connect(self.spnbox_changed)
        hbox_lay_overlaps_border_10.addWidget(box_overlaps_border_10)
        bg_box.addLayout(hbox_lay_overlaps_border_10)

        hbox_lay_multiplier_11 =  QHBoxLayout()
        label_multiplier_11 = QLabel("        multiplier")
        label_multiplier_11.setPalette(palette_object)
        label_multiplier_11.setFont(QFont("Monospace", 10))
        hbox_lay_multiplier_11.addWidget(label_multiplier_11)

        box_multiplier_11 = QDoubleSpinBox()
        box_multiplier_11.setValue(1.3)
        box_multiplier_11.local_path = "indexing.max_cell_estimation.multiplier"
        box_multiplier_11.valueChanged.connect(self.spnbox_changed)
        hbox_lay_multiplier_11.addWidget(box_multiplier_11)
        bg_box.addLayout(hbox_lay_multiplier_11)

        hbox_lay_step_size_12 =  QHBoxLayout()
        label_step_size_12 = QLabel("        step_size")
        label_step_size_12.setPalette(palette_object)
        label_step_size_12.setFont(QFont("Monospace", 10))
        hbox_lay_step_size_12.addWidget(label_step_size_12)

        box_step_size_12 = QDoubleSpinBox()
        box_step_size_12.setValue(45.0)
        box_step_size_12.local_path = "indexing.max_cell_estimation.step_size"
        box_step_size_12.valueChanged.connect(self.spnbox_changed)
        hbox_lay_step_size_12.addWidget(box_step_size_12)
        bg_box.addLayout(hbox_lay_step_size_12)

        hbox_lay_nearest_neighbor_percentile_13 =  QHBoxLayout()
        label_nearest_neighbor_percentile_13 = QLabel("        nearest_neighbor_percentile")
        label_nearest_neighbor_percentile_13.setPalette(palette_object)
        label_nearest_neighbor_percentile_13.setFont(QFont("Monospace", 10))
        hbox_lay_nearest_neighbor_percentile_13.addWidget(label_nearest_neighbor_percentile_13)

        box_nearest_neighbor_percentile_13 = QDoubleSpinBox()
        box_nearest_neighbor_percentile_13.setValue(0.05)
        box_nearest_neighbor_percentile_13.local_path = "indexing.max_cell_estimation.nearest_neighbor_percentile"
        box_nearest_neighbor_percentile_13.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbor_percentile_13.addWidget(box_nearest_neighbor_percentile_13)
        bg_box.addLayout(hbox_lay_nearest_neighbor_percentile_13)

        label_14 = QLabel("    fft3d")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_14)

        hbox_lay_peak_search_15 =  QHBoxLayout()
        label_peak_search_15 = QLabel("        peak_search")
        label_peak_search_15.setPalette(palette_object)
        label_peak_search_15.setFont(QFont("Monospace", 10))
        hbox_lay_peak_search_15.addWidget(label_peak_search_15)

        box_peak_search_15 = QComboBox()
        box_peak_search_15.local_path = "indexing.fft3d.peak_search"
        box_peak_search_15.tmp_lst=[]
        box_peak_search_15.tmp_lst.append("flood_fill")
        box_peak_search_15.tmp_lst.append("clean")
        for lst_itm in box_peak_search_15.tmp_lst:
            box_peak_search_15.addItem(lst_itm)
        box_peak_search_15.setCurrentIndex(0)
        box_peak_search_15.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_peak_search_15.addWidget(box_peak_search_15)
        bg_box.addLayout(hbox_lay_peak_search_15)

        hbox_lay_peak_volume_cutoff_16 =  QHBoxLayout()
        label_peak_volume_cutoff_16 = QLabel("        peak_volume_cutoff")
        label_peak_volume_cutoff_16.setPalette(palette_object)
        label_peak_volume_cutoff_16.setFont(QFont("Monospace", 10))
        hbox_lay_peak_volume_cutoff_16.addWidget(label_peak_volume_cutoff_16)

        box_peak_volume_cutoff_16 = QDoubleSpinBox()
        box_peak_volume_cutoff_16.setValue(0.15)
        box_peak_volume_cutoff_16.local_path = "indexing.fft3d.peak_volume_cutoff"
        box_peak_volume_cutoff_16.valueChanged.connect(self.spnbox_changed)
        hbox_lay_peak_volume_cutoff_16.addWidget(box_peak_volume_cutoff_16)
        bg_box.addLayout(hbox_lay_peak_volume_cutoff_16)

        label_17 = QLabel("        reciprocal_space_grid")
        label_17.setPalette(palette_scope)
        label_17.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_17)

        hbox_lay_n_points_18 =  QHBoxLayout()
        label_n_points_18 = QLabel("            n_points")
        label_n_points_18.setPalette(palette_object)
        label_n_points_18.setFont(QFont("Monospace", 10))
        hbox_lay_n_points_18.addWidget(label_n_points_18)

        box_n_points_18 = QSpinBox()
        box_n_points_18.setValue(256)
        box_n_points_18.local_path = "indexing.fft3d.reciprocal_space_grid.n_points"
        box_n_points_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_points_18.addWidget(box_n_points_18)
        bg_box.addLayout(hbox_lay_n_points_18)

        hbox_lay_d_min_19 =  QHBoxLayout()
        label_d_min_19 = QLabel("            d_min")
        label_d_min_19.setPalette(palette_object)
        label_d_min_19.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_19.addWidget(label_d_min_19)

        box_d_min_19 = QDoubleSpinBox()
        box_d_min_19.local_path = "indexing.fft3d.reciprocal_space_grid.d_min"
        box_d_min_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_19.addWidget(box_d_min_19)
        bg_box.addLayout(hbox_lay_d_min_19)

        hbox_lay_sigma_phi_deg_20 =  QHBoxLayout()
        label_sigma_phi_deg_20 = QLabel("    sigma_phi_deg")
        label_sigma_phi_deg_20.setPalette(palette_object)
        label_sigma_phi_deg_20.setFont(QFont("Monospace", 10))
        hbox_lay_sigma_phi_deg_20.addWidget(label_sigma_phi_deg_20)

        box_sigma_phi_deg_20 = QDoubleSpinBox()
        box_sigma_phi_deg_20.local_path = "indexing.sigma_phi_deg"
        box_sigma_phi_deg_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_phi_deg_20.addWidget(box_sigma_phi_deg_20)
        bg_box.addLayout(hbox_lay_sigma_phi_deg_20)

        hbox_lay_b_iso_21 =  QHBoxLayout()
        label_b_iso_21 = QLabel("    b_iso")
        label_b_iso_21.setPalette(palette_object)
        label_b_iso_21.setFont(QFont("Monospace", 10))
        hbox_lay_b_iso_21.addWidget(label_b_iso_21)

        box_b_iso_21 = QDoubleSpinBox()
        box_b_iso_21.local_path = "indexing.b_iso"
        box_b_iso_21.valueChanged.connect(self.spnbox_changed)
        hbox_lay_b_iso_21.addWidget(box_b_iso_21)
        bg_box.addLayout(hbox_lay_b_iso_21)

        hbox_lay_rmsd_cutoff_22 =  QHBoxLayout()
        label_rmsd_cutoff_22 = QLabel("    rmsd_cutoff")
        label_rmsd_cutoff_22.setPalette(palette_object)
        label_rmsd_cutoff_22.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_22.addWidget(label_rmsd_cutoff_22)

        box_rmsd_cutoff_22 = QDoubleSpinBox()
        box_rmsd_cutoff_22.setValue(15.0)
        box_rmsd_cutoff_22.local_path = "indexing.rmsd_cutoff"
        box_rmsd_cutoff_22.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_cutoff_22.addWidget(box_rmsd_cutoff_22)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_22)

        hbox_lay_scan_range_23_0 =  QHBoxLayout()
        label_scan_range_23_0 = QLabel("    scan_range[1]")
        label_scan_range_23_0.setPalette(palette_object)
        label_scan_range_23_0.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_23_0.addWidget(label_scan_range_23_0)
        box_scan_range_23_0 = QSpinBox()
        box_scan_range_23_0.local_path = "indexing.scan_range"
        #box_scan_range_23_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_23_1 =  QHBoxLayout()
        label_scan_range_23_1 = QLabel("    scan_range[2]")
        label_scan_range_23_1.setPalette(palette_object)
        label_scan_range_23_1.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_23_1.addWidget(label_scan_range_23_1)
        box_scan_range_23_1 = QSpinBox()
        box_scan_range_23_1.local_path = "indexing.scan_range"
        #box_scan_range_23_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_23_0.addWidget(box_scan_range_23_0)
        bg_box.addLayout(hbox_lay_scan_range_23_0)
        hbox_lay_scan_range_23_1.addWidget(box_scan_range_23_1)
        bg_box.addLayout(hbox_lay_scan_range_23_1)

        label_24 = QLabel("    known_symmetry")
        label_24.setPalette(palette_scope)
        label_24.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_24)



        hbox_lay_relative_length_tolerance_27 =  QHBoxLayout()
        label_relative_length_tolerance_27 = QLabel("        relative_length_tolerance")
        label_relative_length_tolerance_27.setPalette(palette_object)
        label_relative_length_tolerance_27.setFont(QFont("Monospace", 10))
        hbox_lay_relative_length_tolerance_27.addWidget(label_relative_length_tolerance_27)

        box_relative_length_tolerance_27 = QDoubleSpinBox()
        box_relative_length_tolerance_27.setValue(0.1)
        box_relative_length_tolerance_27.local_path = "indexing.known_symmetry.relative_length_tolerance"
        box_relative_length_tolerance_27.valueChanged.connect(self.spnbox_changed)
        hbox_lay_relative_length_tolerance_27.addWidget(box_relative_length_tolerance_27)
        bg_box.addLayout(hbox_lay_relative_length_tolerance_27)

        hbox_lay_absolute_angle_tolerance_28 =  QHBoxLayout()
        label_absolute_angle_tolerance_28 = QLabel("        absolute_angle_tolerance")
        label_absolute_angle_tolerance_28.setPalette(palette_object)
        label_absolute_angle_tolerance_28.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_angle_tolerance_28.addWidget(label_absolute_angle_tolerance_28)

        box_absolute_angle_tolerance_28 = QDoubleSpinBox()
        box_absolute_angle_tolerance_28.setValue(5.0)
        box_absolute_angle_tolerance_28.local_path = "indexing.known_symmetry.absolute_angle_tolerance"
        box_absolute_angle_tolerance_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_angle_tolerance_28.addWidget(box_absolute_angle_tolerance_28)
        bg_box.addLayout(hbox_lay_absolute_angle_tolerance_28)

        hbox_lay_max_delta_29 =  QHBoxLayout()
        label_max_delta_29 = QLabel("        max_delta")
        label_max_delta_29.setPalette(palette_object)
        label_max_delta_29.setFont(QFont("Monospace", 10))
        hbox_lay_max_delta_29.addWidget(label_max_delta_29)

        box_max_delta_29 = QDoubleSpinBox()
        box_max_delta_29.setValue(5.0)
        box_max_delta_29.local_path = "indexing.known_symmetry.max_delta"
        box_max_delta_29.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_delta_29.addWidget(box_max_delta_29)
        bg_box.addLayout(hbox_lay_max_delta_29)

        label_30 = QLabel("    basis_vector_combinations")
        label_30.setPalette(palette_scope)
        label_30.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_30)

        hbox_lay_max_try_31 =  QHBoxLayout()
        label_max_try_31 = QLabel("        max_try")
        label_max_try_31.setPalette(palette_object)
        label_max_try_31.setFont(QFont("Monospace", 10))
        hbox_lay_max_try_31.addWidget(label_max_try_31)

        box_max_try_31 = QSpinBox()
        box_max_try_31.setValue(50)
        box_max_try_31.local_path = "indexing.basis_vector_combinations.max_try"
        box_max_try_31.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_try_31.addWidget(box_max_try_31)
        bg_box.addLayout(hbox_lay_max_try_31)

        hbox_lay_sys_absent_threshold_32 =  QHBoxLayout()
        label_sys_absent_threshold_32 = QLabel("        sys_absent_threshold")
        label_sys_absent_threshold_32.setPalette(palette_object)
        label_sys_absent_threshold_32.setFont(QFont("Monospace", 10))
        hbox_lay_sys_absent_threshold_32.addWidget(label_sys_absent_threshold_32)

        box_sys_absent_threshold_32 = QDoubleSpinBox()
        box_sys_absent_threshold_32.setValue(0.9)
        box_sys_absent_threshold_32.local_path = "indexing.basis_vector_combinations.sys_absent_threshold"
        box_sys_absent_threshold_32.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sys_absent_threshold_32.addWidget(box_sys_absent_threshold_32)
        bg_box.addLayout(hbox_lay_sys_absent_threshold_32)

        hbox_lay_solution_scorer_33 =  QHBoxLayout()
        label_solution_scorer_33 = QLabel("        solution_scorer")
        label_solution_scorer_33.setPalette(palette_object)
        label_solution_scorer_33.setFont(QFont("Monospace", 10))
        hbox_lay_solution_scorer_33.addWidget(label_solution_scorer_33)

        box_solution_scorer_33 = QComboBox()
        box_solution_scorer_33.local_path = "indexing.basis_vector_combinations.solution_scorer"
        box_solution_scorer_33.tmp_lst=[]
        box_solution_scorer_33.tmp_lst.append("filter")
        box_solution_scorer_33.tmp_lst.append("weighted")
        for lst_itm in box_solution_scorer_33.tmp_lst:
            box_solution_scorer_33.addItem(lst_itm)
        box_solution_scorer_33.setCurrentIndex(1)
        box_solution_scorer_33.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_solution_scorer_33.addWidget(box_solution_scorer_33)
        bg_box.addLayout(hbox_lay_solution_scorer_33)

        label_34 = QLabel("        filter")
        label_34.setPalette(palette_scope)
        label_34.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_34)

        hbox_lay_check_doubled_cell_35 =  QHBoxLayout()
        label_check_doubled_cell_35 = QLabel("            check_doubled_cell")
        label_check_doubled_cell_35.setPalette(palette_object)
        label_check_doubled_cell_35.setFont(QFont("Monospace", 10))
        hbox_lay_check_doubled_cell_35.addWidget(label_check_doubled_cell_35)

        box_check_doubled_cell_35 = QComboBox()
        box_check_doubled_cell_35.local_path = "indexing.basis_vector_combinations.filter.check_doubled_cell"
        box_check_doubled_cell_35.tmp_lst=[]
        box_check_doubled_cell_35.tmp_lst.append("True")
        box_check_doubled_cell_35.tmp_lst.append("False")
        for lst_itm in box_check_doubled_cell_35.tmp_lst:
            box_check_doubled_cell_35.addItem(lst_itm)
        box_check_doubled_cell_35.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_check_doubled_cell_35.addWidget(box_check_doubled_cell_35)
        bg_box.addLayout(hbox_lay_check_doubled_cell_35)

        hbox_lay_likelihood_cutoff_36 =  QHBoxLayout()
        label_likelihood_cutoff_36 = QLabel("            likelihood_cutoff")
        label_likelihood_cutoff_36.setPalette(palette_object)
        label_likelihood_cutoff_36.setFont(QFont("Monospace", 10))
        hbox_lay_likelihood_cutoff_36.addWidget(label_likelihood_cutoff_36)

        box_likelihood_cutoff_36 = QDoubleSpinBox()
        box_likelihood_cutoff_36.setValue(0.8)
        box_likelihood_cutoff_36.local_path = "indexing.basis_vector_combinations.filter.likelihood_cutoff"
        box_likelihood_cutoff_36.valueChanged.connect(self.spnbox_changed)
        hbox_lay_likelihood_cutoff_36.addWidget(box_likelihood_cutoff_36)
        bg_box.addLayout(hbox_lay_likelihood_cutoff_36)

        hbox_lay_volume_cutoff_37 =  QHBoxLayout()
        label_volume_cutoff_37 = QLabel("            volume_cutoff")
        label_volume_cutoff_37.setPalette(palette_object)
        label_volume_cutoff_37.setFont(QFont("Monospace", 10))
        hbox_lay_volume_cutoff_37.addWidget(label_volume_cutoff_37)

        box_volume_cutoff_37 = QDoubleSpinBox()
        box_volume_cutoff_37.setValue(1.25)
        box_volume_cutoff_37.local_path = "indexing.basis_vector_combinations.filter.volume_cutoff"
        box_volume_cutoff_37.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_cutoff_37.addWidget(box_volume_cutoff_37)
        bg_box.addLayout(hbox_lay_volume_cutoff_37)

        hbox_lay_n_indexed_cutoff_38 =  QHBoxLayout()
        label_n_indexed_cutoff_38 = QLabel("            n_indexed_cutoff")
        label_n_indexed_cutoff_38.setPalette(palette_object)
        label_n_indexed_cutoff_38.setFont(QFont("Monospace", 10))
        hbox_lay_n_indexed_cutoff_38.addWidget(label_n_indexed_cutoff_38)

        box_n_indexed_cutoff_38 = QDoubleSpinBox()
        box_n_indexed_cutoff_38.setValue(0.9)
        box_n_indexed_cutoff_38.local_path = "indexing.basis_vector_combinations.filter.n_indexed_cutoff"
        box_n_indexed_cutoff_38.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_cutoff_38.addWidget(box_n_indexed_cutoff_38)
        bg_box.addLayout(hbox_lay_n_indexed_cutoff_38)

        label_39 = QLabel("        weighted")
        label_39.setPalette(palette_scope)
        label_39.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_39)

        hbox_lay_power_40 =  QHBoxLayout()
        label_power_40 = QLabel("            power")
        label_power_40.setPalette(palette_object)
        label_power_40.setFont(QFont("Monospace", 10))
        hbox_lay_power_40.addWidget(label_power_40)

        box_power_40 = QSpinBox()
        box_power_40.setValue(1)
        box_power_40.local_path = "indexing.basis_vector_combinations.weighted.power"
        box_power_40.valueChanged.connect(self.spnbox_changed)
        hbox_lay_power_40.addWidget(box_power_40)
        bg_box.addLayout(hbox_lay_power_40)

        hbox_lay_volume_weight_41 =  QHBoxLayout()
        label_volume_weight_41 = QLabel("            volume_weight")
        label_volume_weight_41.setPalette(palette_object)
        label_volume_weight_41.setFont(QFont("Monospace", 10))
        hbox_lay_volume_weight_41.addWidget(label_volume_weight_41)

        box_volume_weight_41 = QDoubleSpinBox()
        box_volume_weight_41.setValue(1.0)
        box_volume_weight_41.local_path = "indexing.basis_vector_combinations.weighted.volume_weight"
        box_volume_weight_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_weight_41.addWidget(box_volume_weight_41)
        bg_box.addLayout(hbox_lay_volume_weight_41)

        hbox_lay_n_indexed_weight_42 =  QHBoxLayout()
        label_n_indexed_weight_42 = QLabel("            n_indexed_weight")
        label_n_indexed_weight_42.setPalette(palette_object)
        label_n_indexed_weight_42.setFont(QFont("Monospace", 10))
        hbox_lay_n_indexed_weight_42.addWidget(label_n_indexed_weight_42)

        box_n_indexed_weight_42 = QDoubleSpinBox()
        box_n_indexed_weight_42.setValue(1.0)
        box_n_indexed_weight_42.local_path = "indexing.basis_vector_combinations.weighted.n_indexed_weight"
        box_n_indexed_weight_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_weight_42.addWidget(box_n_indexed_weight_42)
        bg_box.addLayout(hbox_lay_n_indexed_weight_42)

        hbox_lay_rmsd_weight_43 =  QHBoxLayout()
        label_rmsd_weight_43 = QLabel("            rmsd_weight")
        label_rmsd_weight_43.setPalette(palette_object)
        label_rmsd_weight_43.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_weight_43.addWidget(label_rmsd_weight_43)

        box_rmsd_weight_43 = QDoubleSpinBox()
        box_rmsd_weight_43.setValue(1.0)
        box_rmsd_weight_43.local_path = "indexing.basis_vector_combinations.weighted.rmsd_weight"
        box_rmsd_weight_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_weight_43.addWidget(box_rmsd_weight_43)
        bg_box.addLayout(hbox_lay_rmsd_weight_43)

        label_44 = QLabel("    index_assignment")
        label_44.setPalette(palette_scope)
        label_44.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_44)

        hbox_lay_method_45 =  QHBoxLayout()
        label_method_45 = QLabel("        method")
        label_method_45.setPalette(palette_object)
        label_method_45.setFont(QFont("Monospace", 10))
        hbox_lay_method_45.addWidget(label_method_45)

        box_method_45 = QComboBox()
        box_method_45.local_path = "indexing.index_assignment.method"
        box_method_45.tmp_lst=[]
        box_method_45.tmp_lst.append("simple")
        box_method_45.tmp_lst.append("local")
        for lst_itm in box_method_45.tmp_lst:
            box_method_45.addItem(lst_itm)
        box_method_45.setCurrentIndex(0)
        box_method_45.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_45.addWidget(box_method_45)
        bg_box.addLayout(hbox_lay_method_45)

        label_46 = QLabel("        simple")
        label_46.setPalette(palette_scope)
        label_46.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_46)

        hbox_lay_hkl_tolerance_47 =  QHBoxLayout()
        label_hkl_tolerance_47 = QLabel("            hkl_tolerance")
        label_hkl_tolerance_47.setPalette(palette_object)
        label_hkl_tolerance_47.setFont(QFont("Monospace", 10))
        hbox_lay_hkl_tolerance_47.addWidget(label_hkl_tolerance_47)

        box_hkl_tolerance_47 = QDoubleSpinBox()
        box_hkl_tolerance_47.setValue(0.3)
        box_hkl_tolerance_47.local_path = "indexing.index_assignment.simple.hkl_tolerance"
        box_hkl_tolerance_47.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hkl_tolerance_47.addWidget(box_hkl_tolerance_47)
        bg_box.addLayout(hbox_lay_hkl_tolerance_47)

        label_48 = QLabel("        local")
        label_48.setPalette(palette_scope)
        label_48.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_48)

        hbox_lay_epsilon_49 =  QHBoxLayout()
        label_epsilon_49 = QLabel("            epsilon")
        label_epsilon_49.setPalette(palette_object)
        label_epsilon_49.setFont(QFont("Monospace", 10))
        hbox_lay_epsilon_49.addWidget(label_epsilon_49)

        box_epsilon_49 = QDoubleSpinBox()
        box_epsilon_49.setValue(0.05)
        box_epsilon_49.local_path = "indexing.index_assignment.local.epsilon"
        box_epsilon_49.valueChanged.connect(self.spnbox_changed)
        hbox_lay_epsilon_49.addWidget(box_epsilon_49)
        bg_box.addLayout(hbox_lay_epsilon_49)

        hbox_lay_delta_50 =  QHBoxLayout()
        label_delta_50 = QLabel("            delta")
        label_delta_50.setPalette(palette_object)
        label_delta_50.setFont(QFont("Monospace", 10))
        hbox_lay_delta_50.addWidget(label_delta_50)

        box_delta_50 = QSpinBox()
        box_delta_50.setValue(8)
        box_delta_50.local_path = "indexing.index_assignment.local.delta"
        box_delta_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delta_50.addWidget(box_delta_50)
        bg_box.addLayout(hbox_lay_delta_50)

        hbox_lay_l_min_51 =  QHBoxLayout()
        label_l_min_51 = QLabel("            l_min")
        label_l_min_51.setPalette(palette_object)
        label_l_min_51.setFont(QFont("Monospace", 10))
        hbox_lay_l_min_51.addWidget(label_l_min_51)

        box_l_min_51 = QDoubleSpinBox()
        box_l_min_51.setValue(0.8)
        box_l_min_51.local_path = "indexing.index_assignment.local.l_min"
        box_l_min_51.valueChanged.connect(self.spnbox_changed)
        hbox_lay_l_min_51.addWidget(box_l_min_51)
        bg_box.addLayout(hbox_lay_l_min_51)

        hbox_lay_nearest_neighbours_52 =  QHBoxLayout()
        label_nearest_neighbours_52 = QLabel("            nearest_neighbours")
        label_nearest_neighbours_52.setPalette(palette_object)
        label_nearest_neighbours_52.setFont(QFont("Monospace", 10))
        hbox_lay_nearest_neighbours_52.addWidget(label_nearest_neighbours_52)

        box_nearest_neighbours_52 = QSpinBox()
        box_nearest_neighbours_52.setValue(20)
        box_nearest_neighbours_52.local_path = "indexing.index_assignment.local.nearest_neighbours"
        box_nearest_neighbours_52.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbours_52.addWidget(box_nearest_neighbours_52)
        bg_box.addLayout(hbox_lay_nearest_neighbours_52)

        label_53 = QLabel("    check_misindexing")
        label_53.setPalette(palette_scope)
        label_53.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_53)

        hbox_lay_grid_search_scope_54 =  QHBoxLayout()
        label_grid_search_scope_54 = QLabel("        grid_search_scope")
        label_grid_search_scope_54.setPalette(palette_object)
        label_grid_search_scope_54.setFont(QFont("Monospace", 10))
        hbox_lay_grid_search_scope_54.addWidget(label_grid_search_scope_54)

        box_grid_search_scope_54 = QSpinBox()
        box_grid_search_scope_54.setValue(0)
        box_grid_search_scope_54.local_path = "indexing.check_misindexing.grid_search_scope"
        box_grid_search_scope_54.valueChanged.connect(self.spnbox_changed)
        hbox_lay_grid_search_scope_54.addWidget(box_grid_search_scope_54)
        bg_box.addLayout(hbox_lay_grid_search_scope_54)

        hbox_lay_optimise_initial_basis_vectors_55 =  QHBoxLayout()
        label_optimise_initial_basis_vectors_55 = QLabel("    optimise_initial_basis_vectors")
        label_optimise_initial_basis_vectors_55.setPalette(palette_object)
        label_optimise_initial_basis_vectors_55.setFont(QFont("Monospace", 10))
        hbox_lay_optimise_initial_basis_vectors_55.addWidget(label_optimise_initial_basis_vectors_55)

        box_optimise_initial_basis_vectors_55 = QComboBox()
        box_optimise_initial_basis_vectors_55.local_path = "indexing.optimise_initial_basis_vectors"
        box_optimise_initial_basis_vectors_55.tmp_lst=[]
        box_optimise_initial_basis_vectors_55.tmp_lst.append("True")
        box_optimise_initial_basis_vectors_55.tmp_lst.append("False")
        for lst_itm in box_optimise_initial_basis_vectors_55.tmp_lst:
            box_optimise_initial_basis_vectors_55.addItem(lst_itm)
        box_optimise_initial_basis_vectors_55.setCurrentIndex(1)
        box_optimise_initial_basis_vectors_55.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_optimise_initial_basis_vectors_55.addWidget(box_optimise_initial_basis_vectors_55)
        bg_box.addLayout(hbox_lay_optimise_initial_basis_vectors_55)

        hbox_lay_debug_56 =  QHBoxLayout()
        label_debug_56 = QLabel("    debug")
        label_debug_56.setPalette(palette_object)
        label_debug_56.setFont(QFont("Monospace", 10))
        hbox_lay_debug_56.addWidget(label_debug_56)

        box_debug_56 = QComboBox()
        box_debug_56.local_path = "indexing.debug"
        box_debug_56.tmp_lst=[]
        box_debug_56.tmp_lst.append("True")
        box_debug_56.tmp_lst.append("False")
        for lst_itm in box_debug_56.tmp_lst:
            box_debug_56.addItem(lst_itm)
        box_debug_56.setCurrentIndex(1)
        box_debug_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_56.addWidget(box_debug_56)
        bg_box.addLayout(hbox_lay_debug_56)

        hbox_lay_debug_plots_57 =  QHBoxLayout()
        label_debug_plots_57 = QLabel("    debug_plots")
        label_debug_plots_57.setPalette(palette_object)
        label_debug_plots_57.setFont(QFont("Monospace", 10))
        hbox_lay_debug_plots_57.addWidget(label_debug_plots_57)

        box_debug_plots_57 = QComboBox()
        box_debug_plots_57.local_path = "indexing.debug_plots"
        box_debug_plots_57.tmp_lst=[]
        box_debug_plots_57.tmp_lst.append("True")
        box_debug_plots_57.tmp_lst.append("False")
        for lst_itm in box_debug_plots_57.tmp_lst:
            box_debug_plots_57.addItem(lst_itm)
        box_debug_plots_57.setCurrentIndex(1)
        box_debug_plots_57.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_plots_57.addWidget(box_debug_plots_57)
        bg_box.addLayout(hbox_lay_debug_plots_57)

        hbox_lay_combine_scans_58 =  QHBoxLayout()
        label_combine_scans_58 = QLabel("    combine_scans")
        label_combine_scans_58.setPalette(palette_object)
        label_combine_scans_58.setFont(QFont("Monospace", 10))
        hbox_lay_combine_scans_58.addWidget(label_combine_scans_58)

        box_combine_scans_58 = QComboBox()
        box_combine_scans_58.local_path = "indexing.combine_scans"
        box_combine_scans_58.tmp_lst=[]
        box_combine_scans_58.tmp_lst.append("True")
        box_combine_scans_58.tmp_lst.append("False")
        for lst_itm in box_combine_scans_58.tmp_lst:
            box_combine_scans_58.addItem(lst_itm)
        box_combine_scans_58.setCurrentIndex(1)
        box_combine_scans_58.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_combine_scans_58.addWidget(box_combine_scans_58)
        bg_box.addLayout(hbox_lay_combine_scans_58)

        label_59 = QLabel("    refinement_protocol")
        label_59.setPalette(palette_scope)
        label_59.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_59)

        hbox_lay_n_macro_cycles_60 =  QHBoxLayout()
        label_n_macro_cycles_60 = QLabel("        n_macro_cycles")
        label_n_macro_cycles_60.setPalette(palette_object)
        label_n_macro_cycles_60.setFont(QFont("Monospace", 10))
        hbox_lay_n_macro_cycles_60.addWidget(label_n_macro_cycles_60)

        box_n_macro_cycles_60 = QSpinBox()
        box_n_macro_cycles_60.local_path = "indexing.refinement_protocol.n_macro_cycles"
        box_n_macro_cycles_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_macro_cycles_60.addWidget(box_n_macro_cycles_60)
        bg_box.addLayout(hbox_lay_n_macro_cycles_60)

        hbox_lay_d_min_step_61 =  QHBoxLayout()
        label_d_min_step_61 = QLabel("        d_min_step")
        label_d_min_step_61.setPalette(palette_object)
        label_d_min_step_61.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_step_61.addWidget(label_d_min_step_61)

        box_d_min_step_61 = QDoubleSpinBox()
        box_d_min_step_61.local_path = "indexing.refinement_protocol.d_min_step"
        box_d_min_step_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_step_61.addWidget(box_d_min_step_61)
        bg_box.addLayout(hbox_lay_d_min_step_61)

        hbox_lay_d_min_start_62 =  QHBoxLayout()
        label_d_min_start_62 = QLabel("        d_min_start")
        label_d_min_start_62.setPalette(palette_object)
        label_d_min_start_62.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_start_62.addWidget(label_d_min_start_62)

        box_d_min_start_62 = QDoubleSpinBox()
        box_d_min_start_62.local_path = "indexing.refinement_protocol.d_min_start"
        box_d_min_start_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_start_62.addWidget(box_d_min_start_62)
        bg_box.addLayout(hbox_lay_d_min_start_62)

        hbox_lay_d_min_final_63 =  QHBoxLayout()
        label_d_min_final_63 = QLabel("        d_min_final")
        label_d_min_final_63.setPalette(palette_object)
        label_d_min_final_63.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_final_63.addWidget(label_d_min_final_63)

        box_d_min_final_63 = QDoubleSpinBox()
        box_d_min_final_63.local_path = "indexing.refinement_protocol.d_min_final"
        box_d_min_final_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_final_63.addWidget(box_d_min_final_63)
        bg_box.addLayout(hbox_lay_d_min_final_63)

        hbox_lay_verbosity_64 =  QHBoxLayout()
        label_verbosity_64 = QLabel("        verbosity")
        label_verbosity_64.setPalette(palette_object)
        label_verbosity_64.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_64.addWidget(label_verbosity_64)

        box_verbosity_64 = QSpinBox()
        box_verbosity_64.setValue(1)
        box_verbosity_64.local_path = "indexing.refinement_protocol.verbosity"
        box_verbosity_64.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_64.addWidget(box_verbosity_64)
        bg_box.addLayout(hbox_lay_verbosity_64)

        hbox_lay_disable_unit_cell_volume_sanity_check_65 =  QHBoxLayout()
        label_disable_unit_cell_volume_sanity_check_65 = QLabel("        disable_unit_cell_volume_sanity_check")
        label_disable_unit_cell_volume_sanity_check_65.setPalette(palette_object)
        label_disable_unit_cell_volume_sanity_check_65.setFont(QFont("Monospace", 10))
        hbox_lay_disable_unit_cell_volume_sanity_check_65.addWidget(label_disable_unit_cell_volume_sanity_check_65)

        box_disable_unit_cell_volume_sanity_check_65 = QComboBox()
        box_disable_unit_cell_volume_sanity_check_65.local_path = "indexing.refinement_protocol.disable_unit_cell_volume_sanity_check"
        box_disable_unit_cell_volume_sanity_check_65.tmp_lst=[]
        box_disable_unit_cell_volume_sanity_check_65.tmp_lst.append("True")
        box_disable_unit_cell_volume_sanity_check_65.tmp_lst.append("False")
        for lst_itm in box_disable_unit_cell_volume_sanity_check_65.tmp_lst:
            box_disable_unit_cell_volume_sanity_check_65.addItem(lst_itm)
        box_disable_unit_cell_volume_sanity_check_65.setCurrentIndex(1)
        box_disable_unit_cell_volume_sanity_check_65.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_disable_unit_cell_volume_sanity_check_65.addWidget(box_disable_unit_cell_volume_sanity_check_65)
        bg_box.addLayout(hbox_lay_disable_unit_cell_volume_sanity_check_65)

        hbox_lay_method_66 =  QHBoxLayout()
        label_method_66 = QLabel("    method")
        label_method_66.setPalette(palette_object)
        label_method_66.setFont(QFont("Monospace", 10))
        hbox_lay_method_66.addWidget(label_method_66)

        box_method_66 = QComboBox()
        box_method_66.local_path = "indexing.method"
        box_method_66.tmp_lst=[]
        box_method_66.tmp_lst.append("fft3d")
        box_method_66.tmp_lst.append("fft1d")
        box_method_66.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_66.tmp_lst:
            box_method_66.addItem(lst_itm)
        box_method_66.setCurrentIndex(0)
        box_method_66.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_66.addWidget(box_method_66)
        bg_box.addLayout(hbox_lay_method_66)

        label_67 = QLabel("    multiple_lattice_search")
        label_67.setPalette(palette_scope)
        label_67.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_67)

        hbox_lay_cluster_analysis_search_68 =  QHBoxLayout()
        label_cluster_analysis_search_68 = QLabel("        cluster_analysis_search")
        label_cluster_analysis_search_68.setPalette(palette_object)
        label_cluster_analysis_search_68.setFont(QFont("Monospace", 10))
        hbox_lay_cluster_analysis_search_68.addWidget(label_cluster_analysis_search_68)

        box_cluster_analysis_search_68 = QComboBox()
        box_cluster_analysis_search_68.local_path = "indexing.multiple_lattice_search.cluster_analysis_search"
        box_cluster_analysis_search_68.tmp_lst=[]
        box_cluster_analysis_search_68.tmp_lst.append("True")
        box_cluster_analysis_search_68.tmp_lst.append("False")
        for lst_itm in box_cluster_analysis_search_68.tmp_lst:
            box_cluster_analysis_search_68.addItem(lst_itm)
        box_cluster_analysis_search_68.setCurrentIndex(1)
        box_cluster_analysis_search_68.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cluster_analysis_search_68.addWidget(box_cluster_analysis_search_68)
        bg_box.addLayout(hbox_lay_cluster_analysis_search_68)

        hbox_lay_recycle_unindexed_reflections_cutoff_69 =  QHBoxLayout()
        label_recycle_unindexed_reflections_cutoff_69 = QLabel("        recycle_unindexed_reflections_cutoff")
        label_recycle_unindexed_reflections_cutoff_69.setPalette(palette_object)
        label_recycle_unindexed_reflections_cutoff_69.setFont(QFont("Monospace", 10))
        hbox_lay_recycle_unindexed_reflections_cutoff_69.addWidget(label_recycle_unindexed_reflections_cutoff_69)

        box_recycle_unindexed_reflections_cutoff_69 = QDoubleSpinBox()
        box_recycle_unindexed_reflections_cutoff_69.setValue(0.1)
        box_recycle_unindexed_reflections_cutoff_69.local_path = "indexing.multiple_lattice_search.recycle_unindexed_reflections_cutoff"
        box_recycle_unindexed_reflections_cutoff_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_recycle_unindexed_reflections_cutoff_69.addWidget(box_recycle_unindexed_reflections_cutoff_69)
        bg_box.addLayout(hbox_lay_recycle_unindexed_reflections_cutoff_69)

        hbox_lay_minimum_angular_separation_70 =  QHBoxLayout()
        label_minimum_angular_separation_70 = QLabel("        minimum_angular_separation")
        label_minimum_angular_separation_70.setPalette(palette_object)
        label_minimum_angular_separation_70.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_angular_separation_70.addWidget(label_minimum_angular_separation_70)

        box_minimum_angular_separation_70 = QDoubleSpinBox()
        box_minimum_angular_separation_70.setValue(5.0)
        box_minimum_angular_separation_70.local_path = "indexing.multiple_lattice_search.minimum_angular_separation"
        box_minimum_angular_separation_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_angular_separation_70.addWidget(box_minimum_angular_separation_70)
        bg_box.addLayout(hbox_lay_minimum_angular_separation_70)

        hbox_lay_max_lattices_71 =  QHBoxLayout()
        label_max_lattices_71 = QLabel("        max_lattices")
        label_max_lattices_71.setPalette(palette_object)
        label_max_lattices_71.setFont(QFont("Monospace", 10))
        hbox_lay_max_lattices_71.addWidget(label_max_lattices_71)

        box_max_lattices_71 = QSpinBox()
        box_max_lattices_71.setValue(1)
        box_max_lattices_71.local_path = "indexing.multiple_lattice_search.max_lattices"
        box_max_lattices_71.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_lattices_71.addWidget(box_max_lattices_71)
        bg_box.addLayout(hbox_lay_max_lattices_71)

        label_72 = QLabel("        cluster_analysis")
        label_72.setPalette(palette_scope)
        label_72.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_72)

        hbox_lay_method_73 =  QHBoxLayout()
        label_method_73 = QLabel("            method")
        label_method_73.setPalette(palette_object)
        label_method_73.setFont(QFont("Monospace", 10))
        hbox_lay_method_73.addWidget(label_method_73)

        box_method_73 = QComboBox()
        box_method_73.local_path = "indexing.multiple_lattice_search.cluster_analysis.method"
        box_method_73.tmp_lst=[]
        box_method_73.tmp_lst.append("dbscan")
        box_method_73.tmp_lst.append("hcluster")
        for lst_itm in box_method_73.tmp_lst:
            box_method_73.addItem(lst_itm)
        box_method_73.setCurrentIndex(0)
        box_method_73.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_73.addWidget(box_method_73)
        bg_box.addLayout(hbox_lay_method_73)

        label_74 = QLabel("            hcluster")
        label_74.setPalette(palette_scope)
        label_74.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_74)

        label_75 = QLabel("                linkage")
        label_75.setPalette(palette_scope)
        label_75.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_75)

        hbox_lay_method_76 =  QHBoxLayout()
        label_method_76 = QLabel("                    method")
        label_method_76.setPalette(palette_object)
        label_method_76.setFont(QFont("Monospace", 10))
        hbox_lay_method_76.addWidget(label_method_76)

        box_method_76 = QComboBox()
        box_method_76.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.method"
        box_method_76.tmp_lst=[]
        box_method_76.tmp_lst.append("ward")
        for lst_itm in box_method_76.tmp_lst:
            box_method_76.addItem(lst_itm)
        box_method_76.setCurrentIndex(0)
        box_method_76.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_76.addWidget(box_method_76)
        bg_box.addLayout(hbox_lay_method_76)

        hbox_lay_metric_77 =  QHBoxLayout()
        label_metric_77 = QLabel("                    metric")
        label_metric_77.setPalette(palette_object)
        label_metric_77.setFont(QFont("Monospace", 10))
        hbox_lay_metric_77.addWidget(label_metric_77)

        box_metric_77 = QComboBox()
        box_metric_77.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.metric"
        box_metric_77.tmp_lst=[]
        box_metric_77.tmp_lst.append("euclidean")
        for lst_itm in box_metric_77.tmp_lst:
            box_metric_77.addItem(lst_itm)
        box_metric_77.setCurrentIndex(0)
        box_metric_77.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_metric_77.addWidget(box_metric_77)
        bg_box.addLayout(hbox_lay_metric_77)

        hbox_lay_cutoff_78 =  QHBoxLayout()
        label_cutoff_78 = QLabel("                cutoff")
        label_cutoff_78.setPalette(palette_object)
        label_cutoff_78.setFont(QFont("Monospace", 10))
        hbox_lay_cutoff_78.addWidget(label_cutoff_78)

        box_cutoff_78 = QDoubleSpinBox()
        box_cutoff_78.setValue(15.0)
        box_cutoff_78.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff"
        box_cutoff_78.valueChanged.connect(self.spnbox_changed)
        hbox_lay_cutoff_78.addWidget(box_cutoff_78)
        bg_box.addLayout(hbox_lay_cutoff_78)

        hbox_lay_cutoff_criterion_79 =  QHBoxLayout()
        label_cutoff_criterion_79 = QLabel("                cutoff_criterion")
        label_cutoff_criterion_79.setPalette(palette_object)
        label_cutoff_criterion_79.setFont(QFont("Monospace", 10))
        hbox_lay_cutoff_criterion_79.addWidget(label_cutoff_criterion_79)

        box_cutoff_criterion_79 = QComboBox()
        box_cutoff_criterion_79.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff_criterion"
        box_cutoff_criterion_79.tmp_lst=[]
        box_cutoff_criterion_79.tmp_lst.append("distance")
        box_cutoff_criterion_79.tmp_lst.append("inconsistent")
        for lst_itm in box_cutoff_criterion_79.tmp_lst:
            box_cutoff_criterion_79.addItem(lst_itm)
        box_cutoff_criterion_79.setCurrentIndex(0)
        box_cutoff_criterion_79.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cutoff_criterion_79.addWidget(box_cutoff_criterion_79)
        bg_box.addLayout(hbox_lay_cutoff_criterion_79)

        label_80 = QLabel("            dbscan")
        label_80.setPalette(palette_scope)
        label_80.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_80)

        hbox_lay_eps_81 =  QHBoxLayout()
        label_eps_81 = QLabel("                eps")
        label_eps_81.setPalette(palette_object)
        label_eps_81.setFont(QFont("Monospace", 10))
        hbox_lay_eps_81.addWidget(label_eps_81)

        box_eps_81 = QDoubleSpinBox()
        box_eps_81.setValue(0.05)
        box_eps_81.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.eps"
        box_eps_81.valueChanged.connect(self.spnbox_changed)
        hbox_lay_eps_81.addWidget(box_eps_81)
        bg_box.addLayout(hbox_lay_eps_81)

        hbox_lay_min_samples_82 =  QHBoxLayout()
        label_min_samples_82 = QLabel("                min_samples")
        label_min_samples_82.setPalette(palette_object)
        label_min_samples_82.setFont(QFont("Monospace", 10))
        hbox_lay_min_samples_82.addWidget(label_min_samples_82)

        box_min_samples_82 = QSpinBox()
        box_min_samples_82.setValue(30)
        box_min_samples_82.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.min_samples"
        box_min_samples_82.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_samples_82.addWidget(box_min_samples_82)
        bg_box.addLayout(hbox_lay_min_samples_82)

        hbox_lay_min_cluster_size_83 =  QHBoxLayout()
        label_min_cluster_size_83 = QLabel("            min_cluster_size")
        label_min_cluster_size_83.setPalette(palette_object)
        label_min_cluster_size_83.setFont(QFont("Monospace", 10))
        hbox_lay_min_cluster_size_83.addWidget(label_min_cluster_size_83)

        box_min_cluster_size_83 = QSpinBox()
        box_min_cluster_size_83.setValue(20)
        box_min_cluster_size_83.local_path = "indexing.multiple_lattice_search.cluster_analysis.min_cluster_size"
        box_min_cluster_size_83.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cluster_size_83.addWidget(box_min_cluster_size_83)
        bg_box.addLayout(hbox_lay_min_cluster_size_83)

        hbox_lay_intersection_union_ratio_cutoff_84 =  QHBoxLayout()
        label_intersection_union_ratio_cutoff_84 = QLabel("            intersection_union_ratio_cutoff")
        label_intersection_union_ratio_cutoff_84.setPalette(palette_object)
        label_intersection_union_ratio_cutoff_84.setFont(QFont("Monospace", 10))
        hbox_lay_intersection_union_ratio_cutoff_84.addWidget(label_intersection_union_ratio_cutoff_84)

        box_intersection_union_ratio_cutoff_84 = QDoubleSpinBox()
        box_intersection_union_ratio_cutoff_84.setValue(0.4)
        box_intersection_union_ratio_cutoff_84.local_path = "indexing.multiple_lattice_search.cluster_analysis.intersection_union_ratio_cutoff"
        box_intersection_union_ratio_cutoff_84.valueChanged.connect(self.spnbox_changed)
        hbox_lay_intersection_union_ratio_cutoff_84.addWidget(box_intersection_union_ratio_cutoff_84)
        bg_box.addLayout(hbox_lay_intersection_union_ratio_cutoff_84)

        label_85 = QLabel("    real_space_grid_search")
        label_85.setPalette(palette_scope)
        label_85.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_85)

        hbox_lay_characteristic_grid_86 =  QHBoxLayout()
        label_characteristic_grid_86 = QLabel("        characteristic_grid")
        label_characteristic_grid_86.setPalette(palette_object)
        label_characteristic_grid_86.setFont(QFont("Monospace", 10))
        hbox_lay_characteristic_grid_86.addWidget(label_characteristic_grid_86)

        box_characteristic_grid_86 = QDoubleSpinBox()
        box_characteristic_grid_86.setValue(0.02)
        box_characteristic_grid_86.local_path = "indexing.real_space_grid_search.characteristic_grid"
        box_characteristic_grid_86.valueChanged.connect(self.spnbox_changed)
        hbox_lay_characteristic_grid_86.addWidget(box_characteristic_grid_86)
        bg_box.addLayout(hbox_lay_characteristic_grid_86)

        label_87 = QLabel("    stills")
        label_87.setPalette(palette_scope)
        label_87.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_87)

        hbox_lay_indexer_88 =  QHBoxLayout()
        label_indexer_88 = QLabel("        indexer")
        label_indexer_88.setPalette(palette_object)
        label_indexer_88.setFont(QFont("Monospace", 10))
        hbox_lay_indexer_88.addWidget(label_indexer_88)

        box_indexer_88 = QComboBox()
        box_indexer_88.local_path = "indexing.stills.indexer"
        box_indexer_88.tmp_lst=[]
        box_indexer_88.tmp_lst.append("Auto")
        box_indexer_88.tmp_lst.append("stills")
        box_indexer_88.tmp_lst.append("sweeps")
        for lst_itm in box_indexer_88.tmp_lst:
            box_indexer_88.addItem(lst_itm)
        box_indexer_88.setCurrentIndex(0)
        box_indexer_88.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_indexer_88.addWidget(box_indexer_88)
        bg_box.addLayout(hbox_lay_indexer_88)

        hbox_lay_ewald_proximity_resolution_cutoff_89 =  QHBoxLayout()
        label_ewald_proximity_resolution_cutoff_89 = QLabel("        ewald_proximity_resolution_cutoff")
        label_ewald_proximity_resolution_cutoff_89.setPalette(palette_object)
        label_ewald_proximity_resolution_cutoff_89.setFont(QFont("Monospace", 10))
        hbox_lay_ewald_proximity_resolution_cutoff_89.addWidget(label_ewald_proximity_resolution_cutoff_89)

        box_ewald_proximity_resolution_cutoff_89 = QDoubleSpinBox()
        box_ewald_proximity_resolution_cutoff_89.setValue(2.0)
        box_ewald_proximity_resolution_cutoff_89.local_path = "indexing.stills.ewald_proximity_resolution_cutoff"
        box_ewald_proximity_resolution_cutoff_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_ewald_proximity_resolution_cutoff_89.addWidget(box_ewald_proximity_resolution_cutoff_89)
        bg_box.addLayout(hbox_lay_ewald_proximity_resolution_cutoff_89)

        hbox_lay_refine_all_candidates_90 =  QHBoxLayout()
        label_refine_all_candidates_90 = QLabel("        refine_all_candidates")
        label_refine_all_candidates_90.setPalette(palette_object)
        label_refine_all_candidates_90.setFont(QFont("Monospace", 10))
        hbox_lay_refine_all_candidates_90.addWidget(label_refine_all_candidates_90)

        box_refine_all_candidates_90 = QComboBox()
        box_refine_all_candidates_90.local_path = "indexing.stills.refine_all_candidates"
        box_refine_all_candidates_90.tmp_lst=[]
        box_refine_all_candidates_90.tmp_lst.append("True")
        box_refine_all_candidates_90.tmp_lst.append("False")
        for lst_itm in box_refine_all_candidates_90.tmp_lst:
            box_refine_all_candidates_90.addItem(lst_itm)
        box_refine_all_candidates_90.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_refine_all_candidates_90.addWidget(box_refine_all_candidates_90)
        bg_box.addLayout(hbox_lay_refine_all_candidates_90)

        hbox_lay_rmsd_min_px_91 =  QHBoxLayout()
        label_rmsd_min_px_91 = QLabel("        rmsd_min_px")
        label_rmsd_min_px_91.setPalette(palette_object)
        label_rmsd_min_px_91.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_min_px_91.addWidget(label_rmsd_min_px_91)

        box_rmsd_min_px_91 = QDoubleSpinBox()
        box_rmsd_min_px_91.setValue(1.5)
        box_rmsd_min_px_91.local_path = "indexing.stills.rmsd_min_px"
        box_rmsd_min_px_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_min_px_91.addWidget(box_rmsd_min_px_91)
        bg_box.addLayout(hbox_lay_rmsd_min_px_91)

        hbox_lay_ewald_proximal_volume_max_92 =  QHBoxLayout()
        label_ewald_proximal_volume_max_92 = QLabel("        ewald_proximal_volume_max")
        label_ewald_proximal_volume_max_92.setPalette(palette_object)
        label_ewald_proximal_volume_max_92.setFont(QFont("Monospace", 10))
        hbox_lay_ewald_proximal_volume_max_92.addWidget(label_ewald_proximal_volume_max_92)

        box_ewald_proximal_volume_max_92 = QDoubleSpinBox()
        box_ewald_proximal_volume_max_92.setValue(0.0015)
        box_ewald_proximal_volume_max_92.local_path = "indexing.stills.ewald_proximal_volume_max"
        box_ewald_proximal_volume_max_92.valueChanged.connect(self.spnbox_changed)
        hbox_lay_ewald_proximal_volume_max_92.addWidget(box_ewald_proximal_volume_max_92)
        bg_box.addLayout(hbox_lay_ewald_proximal_volume_max_92)

        label_93 = QLabel("        isoforms")
        label_93.setPalette(palette_scope)
        label_93.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_93)

        hbox_lay_name_94 =  QHBoxLayout()
        label_name_94 = QLabel("            name")
        label_name_94.setPalette(palette_object)
        label_name_94.setFont(QFont("Monospace", 10))
        hbox_lay_name_94.addWidget(label_name_94)

        box_name_94 = QLineEdit()
        box_name_94.local_path = "indexing.stills.isoforms.name"
        box_name_94.textChanged.connect(self.spnbox_changed)
        hbox_lay_name_94.addWidget(box_name_94)
        bg_box.addLayout(hbox_lay_name_94)


        hbox_lay_lookup_symbol_96 =  QHBoxLayout()
        label_lookup_symbol_96 = QLabel("            lookup_symbol")
        label_lookup_symbol_96.setPalette(palette_object)
        label_lookup_symbol_96.setFont(QFont("Monospace", 10))
        hbox_lay_lookup_symbol_96.addWidget(label_lookup_symbol_96)

        box_lookup_symbol_96 = QLineEdit()
        box_lookup_symbol_96.local_path = "indexing.stills.isoforms.lookup_symbol"
        box_lookup_symbol_96.textChanged.connect(self.spnbox_changed)
        hbox_lay_lookup_symbol_96.addWidget(box_lookup_symbol_96)
        bg_box.addLayout(hbox_lay_lookup_symbol_96)

        hbox_lay_rmsd_target_mm_97 =  QHBoxLayout()
        label_rmsd_target_mm_97 = QLabel("            rmsd_target_mm")
        label_rmsd_target_mm_97.setPalette(palette_object)
        label_rmsd_target_mm_97.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_target_mm_97.addWidget(label_rmsd_target_mm_97)

        box_rmsd_target_mm_97 = QDoubleSpinBox()
        box_rmsd_target_mm_97.local_path = "indexing.stills.isoforms.rmsd_target_mm"
        box_rmsd_target_mm_97.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_target_mm_97.addWidget(box_rmsd_target_mm_97)
        bg_box.addLayout(hbox_lay_rmsd_target_mm_97)

        hbox_lay_beam_restraint_98_0 =  QHBoxLayout()
        label_beam_restraint_98_0 = QLabel("            beam_restraint[1]")
        label_beam_restraint_98_0.setPalette(palette_object)
        label_beam_restraint_98_0.setFont(QFont("Monospace", 10))
        hbox_lay_beam_restraint_98_0.addWidget(label_beam_restraint_98_0)
        box_beam_restraint_98_0 = QDoubleSpinBox()
        box_beam_restraint_98_0.local_path = "indexing.stills.isoforms.beam_restraint"
        #box_beam_restraint_98_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_beam_restraint_98_1 =  QHBoxLayout()
        label_beam_restraint_98_1 = QLabel("            beam_restraint[2]")
        label_beam_restraint_98_1.setPalette(palette_object)
        label_beam_restraint_98_1.setFont(QFont("Monospace", 10))
        hbox_lay_beam_restraint_98_1.addWidget(label_beam_restraint_98_1)
        box_beam_restraint_98_1 = QDoubleSpinBox()
        box_beam_restraint_98_1.local_path = "indexing.stills.isoforms.beam_restraint"
        #box_beam_restraint_98_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_beam_restraint_98_0.addWidget(box_beam_restraint_98_0)
        bg_box.addLayout(hbox_lay_beam_restraint_98_0)
        hbox_lay_beam_restraint_98_1.addWidget(box_beam_restraint_98_1)
        bg_box.addLayout(hbox_lay_beam_restraint_98_1)

        label_99 = QLabel("refinement")
        label_99.setPalette(palette_scope)
        label_99.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_99)

        label_100 = QLabel("    mp")
        label_100.setPalette(palette_scope)
        label_100.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_100)

        hbox_lay_nproc_101 =  QHBoxLayout()
        label_nproc_101 = QLabel("        nproc")
        label_nproc_101.setPalette(palette_object)
        label_nproc_101.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_101.addWidget(label_nproc_101)

        box_nproc_101 = QSpinBox()
        box_nproc_101.setValue(1)
        box_nproc_101.local_path = "refinement.mp.nproc"
        box_nproc_101.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_101.addWidget(box_nproc_101)
        bg_box.addLayout(hbox_lay_nproc_101)

        hbox_lay_verbosity_102 =  QHBoxLayout()
        label_verbosity_102 = QLabel("    verbosity")
        label_verbosity_102.setPalette(palette_object)
        label_verbosity_102.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_102.addWidget(label_verbosity_102)

        box_verbosity_102 = QSpinBox()
        box_verbosity_102.setValue(0)
        box_verbosity_102.local_path = "refinement.verbosity"
        box_verbosity_102.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_102.addWidget(box_verbosity_102)
        bg_box.addLayout(hbox_lay_verbosity_102)

        label_103 = QLabel("    parameterisation")
        label_103.setPalette(palette_scope)
        label_103.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_103)

        label_104 = QLabel("        auto_reduction")
        label_104.setPalette(palette_scope)
        label_104.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_104)

        hbox_lay_min_nref_per_parameter_105 =  QHBoxLayout()
        label_min_nref_per_parameter_105 = QLabel("            min_nref_per_parameter")
        label_min_nref_per_parameter_105.setPalette(palette_object)
        label_min_nref_per_parameter_105.setFont(QFont("Monospace", 10))
        hbox_lay_min_nref_per_parameter_105.addWidget(label_min_nref_per_parameter_105)

        box_min_nref_per_parameter_105 = QSpinBox()
        box_min_nref_per_parameter_105.setValue(5)
        box_min_nref_per_parameter_105.local_path = "refinement.parameterisation.auto_reduction.min_nref_per_parameter"
        box_min_nref_per_parameter_105.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_nref_per_parameter_105.addWidget(box_min_nref_per_parameter_105)
        bg_box.addLayout(hbox_lay_min_nref_per_parameter_105)

        hbox_lay_action_106 =  QHBoxLayout()
        label_action_106 = QLabel("            action")
        label_action_106.setPalette(palette_object)
        label_action_106.setFont(QFont("Monospace", 10))
        hbox_lay_action_106.addWidget(label_action_106)

        box_action_106 = QComboBox()
        box_action_106.local_path = "refinement.parameterisation.auto_reduction.action"
        box_action_106.tmp_lst=[]
        box_action_106.tmp_lst.append("fail")
        box_action_106.tmp_lst.append("fix")
        box_action_106.tmp_lst.append("remove")
        for lst_itm in box_action_106.tmp_lst:
            box_action_106.addItem(lst_itm)
        box_action_106.setCurrentIndex(0)
        box_action_106.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_action_106.addWidget(box_action_106)
        bg_box.addLayout(hbox_lay_action_106)

        hbox_lay_detector_reduce_107 =  QHBoxLayout()
        label_detector_reduce_107 = QLabel("            detector_reduce")
        label_detector_reduce_107.setPalette(palette_object)
        label_detector_reduce_107.setFont(QFont("Monospace", 10))
        hbox_lay_detector_reduce_107.addWidget(label_detector_reduce_107)

        box_detector_reduce_107 = QComboBox()
        box_detector_reduce_107.local_path = "refinement.parameterisation.auto_reduction.detector_reduce"
        box_detector_reduce_107.tmp_lst=[]
        box_detector_reduce_107.tmp_lst.append("True")
        box_detector_reduce_107.tmp_lst.append("False")
        for lst_itm in box_detector_reduce_107.tmp_lst:
            box_detector_reduce_107.addItem(lst_itm)
        box_detector_reduce_107.setCurrentIndex(1)
        box_detector_reduce_107.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_detector_reduce_107.addWidget(box_detector_reduce_107)
        bg_box.addLayout(hbox_lay_detector_reduce_107)


        hbox_lay_scan_varying_109 =  QHBoxLayout()
        label_scan_varying_109 = QLabel("        scan_varying")
        label_scan_varying_109.setPalette(palette_object)
        label_scan_varying_109.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_109.addWidget(label_scan_varying_109)

        box_scan_varying_109 = QComboBox()
        box_scan_varying_109.local_path = "refinement.parameterisation.scan_varying"
        box_scan_varying_109.tmp_lst=[]
        box_scan_varying_109.tmp_lst.append("True")
        box_scan_varying_109.tmp_lst.append("False")
        for lst_itm in box_scan_varying_109.tmp_lst:
            box_scan_varying_109.addItem(lst_itm)
        box_scan_varying_109.setCurrentIndex(1)
        box_scan_varying_109.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_109.addWidget(box_scan_varying_109)
        bg_box.addLayout(hbox_lay_scan_varying_109)

        hbox_lay_compose_model_per_110 =  QHBoxLayout()
        label_compose_model_per_110 = QLabel("        compose_model_per")
        label_compose_model_per_110.setPalette(palette_object)
        label_compose_model_per_110.setFont(QFont("Monospace", 10))
        hbox_lay_compose_model_per_110.addWidget(label_compose_model_per_110)

        box_compose_model_per_110 = QComboBox()
        box_compose_model_per_110.local_path = "refinement.parameterisation.compose_model_per"
        box_compose_model_per_110.tmp_lst=[]
        box_compose_model_per_110.tmp_lst.append("reflection")
        box_compose_model_per_110.tmp_lst.append("image")
        box_compose_model_per_110.tmp_lst.append("block")
        for lst_itm in box_compose_model_per_110.tmp_lst:
            box_compose_model_per_110.addItem(lst_itm)
        box_compose_model_per_110.setCurrentIndex(2)
        box_compose_model_per_110.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_compose_model_per_110.addWidget(box_compose_model_per_110)
        bg_box.addLayout(hbox_lay_compose_model_per_110)

        label_111 = QLabel("        beam")
        label_111.setPalette(palette_scope)
        label_111.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_111)

        hbox_lay_fix_112 =  QHBoxLayout()
        label_fix_112 = QLabel("            fix")
        label_fix_112.setPalette(palette_object)
        label_fix_112.setFont(QFont("Monospace", 10))
        hbox_lay_fix_112.addWidget(label_fix_112)

        box_fix_112 = QComboBox()
        box_fix_112.local_path = "refinement.parameterisation.beam.fix"
        box_fix_112.tmp_lst=[]
        box_fix_112.tmp_lst.append("all")
        box_fix_112.tmp_lst.append("in_spindle_plane")
        box_fix_112.tmp_lst.append("out_spindle_plane")
        box_fix_112.tmp_lst.append("wavelength")
        for lst_itm in box_fix_112.tmp_lst:
            box_fix_112.addItem(lst_itm)
        box_fix_112.setCurrentIndex(3)
        box_fix_112.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_112.addWidget(box_fix_112)
        bg_box.addLayout(hbox_lay_fix_112)


        hbox_lay_force_static_114 =  QHBoxLayout()
        label_force_static_114 = QLabel("            force_static")
        label_force_static_114.setPalette(palette_object)
        label_force_static_114.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_114.addWidget(label_force_static_114)

        box_force_static_114 = QComboBox()
        box_force_static_114.local_path = "refinement.parameterisation.beam.force_static"
        box_force_static_114.tmp_lst=[]
        box_force_static_114.tmp_lst.append("True")
        box_force_static_114.tmp_lst.append("False")
        for lst_itm in box_force_static_114.tmp_lst:
            box_force_static_114.addItem(lst_itm)
        box_force_static_114.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_114.addWidget(box_force_static_114)
        bg_box.addLayout(hbox_lay_force_static_114)

        label_115 = QLabel("            smoother")
        label_115.setPalette(palette_scope)
        label_115.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_115)

        hbox_lay_num_intervals_116 =  QHBoxLayout()
        label_num_intervals_116 = QLabel("                num_intervals")
        label_num_intervals_116.setPalette(palette_object)
        label_num_intervals_116.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_116.addWidget(label_num_intervals_116)

        box_num_intervals_116 = QComboBox()
        box_num_intervals_116.local_path = "refinement.parameterisation.beam.smoother.num_intervals"
        box_num_intervals_116.tmp_lst=[]
        box_num_intervals_116.tmp_lst.append("fixed_width")
        box_num_intervals_116.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_116.tmp_lst:
            box_num_intervals_116.addItem(lst_itm)
        box_num_intervals_116.setCurrentIndex(0)
        box_num_intervals_116.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_116.addWidget(box_num_intervals_116)
        bg_box.addLayout(hbox_lay_num_intervals_116)

        hbox_lay_interval_width_degrees_117 =  QHBoxLayout()
        label_interval_width_degrees_117 = QLabel("                interval_width_degrees")
        label_interval_width_degrees_117.setPalette(palette_object)
        label_interval_width_degrees_117.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_117.addWidget(label_interval_width_degrees_117)

        box_interval_width_degrees_117 = QDoubleSpinBox()
        box_interval_width_degrees_117.setValue(36.0)
        box_interval_width_degrees_117.local_path = "refinement.parameterisation.beam.smoother.interval_width_degrees"
        box_interval_width_degrees_117.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_117.addWidget(box_interval_width_degrees_117)
        bg_box.addLayout(hbox_lay_interval_width_degrees_117)

        hbox_lay_absolute_num_intervals_118 =  QHBoxLayout()
        label_absolute_num_intervals_118 = QLabel("                absolute_num_intervals")
        label_absolute_num_intervals_118.setPalette(palette_object)
        label_absolute_num_intervals_118.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_118.addWidget(label_absolute_num_intervals_118)

        box_absolute_num_intervals_118 = QSpinBox()
        box_absolute_num_intervals_118.setValue(5)
        box_absolute_num_intervals_118.local_path = "refinement.parameterisation.beam.smoother.absolute_num_intervals"
        box_absolute_num_intervals_118.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_118.addWidget(box_absolute_num_intervals_118)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_118)

        label_119 = QLabel("        crystal")
        label_119.setPalette(palette_scope)
        label_119.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_119)

        hbox_lay_fix_120 =  QHBoxLayout()
        label_fix_120 = QLabel("            fix")
        label_fix_120.setPalette(palette_object)
        label_fix_120.setFont(QFont("Monospace", 10))
        hbox_lay_fix_120.addWidget(label_fix_120)

        box_fix_120 = QComboBox()
        box_fix_120.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_120.tmp_lst=[]
        box_fix_120.tmp_lst.append("all")
        box_fix_120.tmp_lst.append("cell")
        box_fix_120.tmp_lst.append("orientation")
        for lst_itm in box_fix_120.tmp_lst:
            box_fix_120.addItem(lst_itm)
        box_fix_120.setCurrentIndex(0)
        box_fix_120.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_120.addWidget(box_fix_120)
        bg_box.addLayout(hbox_lay_fix_120)

        label_121 = QLabel("            unit_cell")
        label_121.setPalette(palette_scope)
        label_121.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_121)


        label_123 = QLabel("                restraints")
        label_123.setPalette(palette_scope)
        label_123.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_123)

        label_124 = QLabel("                    tie_to_target")
        label_124.setPalette(palette_scope)
        label_124.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_124)

        hbox_lay_values_125_0 =  QHBoxLayout()
        label_values_125_0 = QLabel("                        values[1]")
        label_values_125_0.setPalette(palette_object)
        label_values_125_0.setFont(QFont("Monospace", 10))
        hbox_lay_values_125_0.addWidget(label_values_125_0)
        box_values_125_0 = QDoubleSpinBox()
        box_values_125_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_125_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_125_1 =  QHBoxLayout()
        label_values_125_1 = QLabel("                        values[2]")
        label_values_125_1.setPalette(palette_object)
        label_values_125_1.setFont(QFont("Monospace", 10))
        hbox_lay_values_125_1.addWidget(label_values_125_1)
        box_values_125_1 = QDoubleSpinBox()
        box_values_125_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_125_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_125_2 =  QHBoxLayout()
        label_values_125_2 = QLabel("                        values[3]")
        label_values_125_2.setPalette(palette_object)
        label_values_125_2.setFont(QFont("Monospace", 10))
        hbox_lay_values_125_2.addWidget(label_values_125_2)
        box_values_125_2 = QDoubleSpinBox()
        box_values_125_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_125_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_125_3 =  QHBoxLayout()
        label_values_125_3 = QLabel("                        values[4]")
        label_values_125_3.setPalette(palette_object)
        label_values_125_3.setFont(QFont("Monospace", 10))
        hbox_lay_values_125_3.addWidget(label_values_125_3)
        box_values_125_3 = QDoubleSpinBox()
        box_values_125_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_125_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_125_4 =  QHBoxLayout()
        label_values_125_4 = QLabel("                        values[5]")
        label_values_125_4.setPalette(palette_object)
        label_values_125_4.setFont(QFont("Monospace", 10))
        hbox_lay_values_125_4.addWidget(label_values_125_4)
        box_values_125_4 = QDoubleSpinBox()
        box_values_125_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_125_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_125_5 =  QHBoxLayout()
        label_values_125_5 = QLabel("                        values[6]")
        label_values_125_5.setPalette(palette_object)
        label_values_125_5.setFont(QFont("Monospace", 10))
        hbox_lay_values_125_5.addWidget(label_values_125_5)
        box_values_125_5 = QDoubleSpinBox()
        box_values_125_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_125_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_sigmas_126_0 =  QHBoxLayout()
        label_sigmas_126_0 = QLabel("                        sigmas[1]")
        label_sigmas_126_0.setPalette(palette_object)
        label_sigmas_126_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_126_0.addWidget(label_sigmas_126_0)
        box_sigmas_126_0 = QDoubleSpinBox()
        box_sigmas_126_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_126_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_126_1 =  QHBoxLayout()
        label_sigmas_126_1 = QLabel("                        sigmas[2]")
        label_sigmas_126_1.setPalette(palette_object)
        label_sigmas_126_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_126_1.addWidget(label_sigmas_126_1)
        box_sigmas_126_1 = QDoubleSpinBox()
        box_sigmas_126_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_126_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_126_2 =  QHBoxLayout()
        label_sigmas_126_2 = QLabel("                        sigmas[3]")
        label_sigmas_126_2.setPalette(palette_object)
        label_sigmas_126_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_126_2.addWidget(label_sigmas_126_2)
        box_sigmas_126_2 = QDoubleSpinBox()
        box_sigmas_126_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_126_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_126_3 =  QHBoxLayout()
        label_sigmas_126_3 = QLabel("                        sigmas[4]")
        label_sigmas_126_3.setPalette(palette_object)
        label_sigmas_126_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_126_3.addWidget(label_sigmas_126_3)
        box_sigmas_126_3 = QDoubleSpinBox()
        box_sigmas_126_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_126_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_126_4 =  QHBoxLayout()
        label_sigmas_126_4 = QLabel("                        sigmas[5]")
        label_sigmas_126_4.setPalette(palette_object)
        label_sigmas_126_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_126_4.addWidget(label_sigmas_126_4)
        box_sigmas_126_4 = QDoubleSpinBox()
        box_sigmas_126_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_126_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_126_5 =  QHBoxLayout()
        label_sigmas_126_5 = QLabel("                        sigmas[6]")
        label_sigmas_126_5.setPalette(palette_object)
        label_sigmas_126_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_126_5.addWidget(label_sigmas_126_5)
        box_sigmas_126_5 = QDoubleSpinBox()
        box_sigmas_126_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_126_5.valueChanged.connect(self.spnbox_changed)


        hbox_lay_apply_to_all_128 =  QHBoxLayout()
        label_apply_to_all_128 = QLabel("                        apply_to_all")
        label_apply_to_all_128.setPalette(palette_object)
        label_apply_to_all_128.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_128.addWidget(label_apply_to_all_128)

        box_apply_to_all_128 = QComboBox()
        box_apply_to_all_128.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.apply_to_all"
        box_apply_to_all_128.tmp_lst=[]
        box_apply_to_all_128.tmp_lst.append("True")
        box_apply_to_all_128.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_128.tmp_lst:
            box_apply_to_all_128.addItem(lst_itm)
        box_apply_to_all_128.setCurrentIndex(1)
        box_apply_to_all_128.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_128.addWidget(box_apply_to_all_128)
        bg_box.addLayout(hbox_lay_apply_to_all_128)

        label_129 = QLabel("                    tie_to_group")
        label_129.setPalette(palette_scope)
        label_129.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_129)

        hbox_lay_target_130 =  QHBoxLayout()
        label_target_130 = QLabel("                        target")
        label_target_130.setPalette(palette_object)
        label_target_130.setFont(QFont("Monospace", 10))
        hbox_lay_target_130.addWidget(label_target_130)

        box_target_130 = QComboBox()
        box_target_130.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_130.tmp_lst=[]
        box_target_130.tmp_lst.append("mean")
        box_target_130.tmp_lst.append("low_memory_mean")
        box_target_130.tmp_lst.append("median")
        for lst_itm in box_target_130.tmp_lst:
            box_target_130.addItem(lst_itm)
        box_target_130.setCurrentIndex(0)
        box_target_130.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_130.addWidget(box_target_130)
        bg_box.addLayout(hbox_lay_target_130)

        hbox_lay_sigmas_131_0 =  QHBoxLayout()
        label_sigmas_131_0 = QLabel("                        sigmas[1]")
        label_sigmas_131_0.setPalette(palette_object)
        label_sigmas_131_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_131_0.addWidget(label_sigmas_131_0)
        box_sigmas_131_0 = QDoubleSpinBox()
        box_sigmas_131_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_131_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_131_1 =  QHBoxLayout()
        label_sigmas_131_1 = QLabel("                        sigmas[2]")
        label_sigmas_131_1.setPalette(palette_object)
        label_sigmas_131_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_131_1.addWidget(label_sigmas_131_1)
        box_sigmas_131_1 = QDoubleSpinBox()
        box_sigmas_131_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_131_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_131_2 =  QHBoxLayout()
        label_sigmas_131_2 = QLabel("                        sigmas[3]")
        label_sigmas_131_2.setPalette(palette_object)
        label_sigmas_131_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_131_2.addWidget(label_sigmas_131_2)
        box_sigmas_131_2 = QDoubleSpinBox()
        box_sigmas_131_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_131_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_131_3 =  QHBoxLayout()
        label_sigmas_131_3 = QLabel("                        sigmas[4]")
        label_sigmas_131_3.setPalette(palette_object)
        label_sigmas_131_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_131_3.addWidget(label_sigmas_131_3)
        box_sigmas_131_3 = QDoubleSpinBox()
        box_sigmas_131_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_131_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_131_4 =  QHBoxLayout()
        label_sigmas_131_4 = QLabel("                        sigmas[5]")
        label_sigmas_131_4.setPalette(palette_object)
        label_sigmas_131_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_131_4.addWidget(label_sigmas_131_4)
        box_sigmas_131_4 = QDoubleSpinBox()
        box_sigmas_131_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_131_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_131_5 =  QHBoxLayout()
        label_sigmas_131_5 = QLabel("                        sigmas[6]")
        label_sigmas_131_5.setPalette(palette_object)
        label_sigmas_131_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_131_5.addWidget(label_sigmas_131_5)
        box_sigmas_131_5 = QDoubleSpinBox()
        box_sigmas_131_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_131_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_131_0.addWidget(box_sigmas_131_0)
        bg_box.addLayout(hbox_lay_sigmas_131_0)
        hbox_lay_sigmas_131_1.addWidget(box_sigmas_131_1)
        bg_box.addLayout(hbox_lay_sigmas_131_1)
        hbox_lay_sigmas_131_2.addWidget(box_sigmas_131_2)
        bg_box.addLayout(hbox_lay_sigmas_131_2)
        hbox_lay_sigmas_131_3.addWidget(box_sigmas_131_3)
        bg_box.addLayout(hbox_lay_sigmas_131_3)
        hbox_lay_sigmas_131_4.addWidget(box_sigmas_131_4)
        bg_box.addLayout(hbox_lay_sigmas_131_4)
        hbox_lay_sigmas_131_5.addWidget(box_sigmas_131_5)
        bg_box.addLayout(hbox_lay_sigmas_131_5)


        hbox_lay_apply_to_all_133 =  QHBoxLayout()
        label_apply_to_all_133 = QLabel("                        apply_to_all")
        label_apply_to_all_133.setPalette(palette_object)
        label_apply_to_all_133.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_133.addWidget(label_apply_to_all_133)

        box_apply_to_all_133 = QComboBox()
        box_apply_to_all_133.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.apply_to_all"
        box_apply_to_all_133.tmp_lst=[]
        box_apply_to_all_133.tmp_lst.append("True")
        box_apply_to_all_133.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_133.tmp_lst:
            box_apply_to_all_133.addItem(lst_itm)
        box_apply_to_all_133.setCurrentIndex(1)
        box_apply_to_all_133.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_133.addWidget(box_apply_to_all_133)
        bg_box.addLayout(hbox_lay_apply_to_all_133)

        hbox_lay_force_static_134 =  QHBoxLayout()
        label_force_static_134 = QLabel("                force_static")
        label_force_static_134.setPalette(palette_object)
        label_force_static_134.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_134.addWidget(label_force_static_134)

        box_force_static_134 = QComboBox()
        box_force_static_134.local_path = "refinement.parameterisation.crystal.unit_cell.force_static"
        box_force_static_134.tmp_lst=[]
        box_force_static_134.tmp_lst.append("True")
        box_force_static_134.tmp_lst.append("False")
        for lst_itm in box_force_static_134.tmp_lst:
            box_force_static_134.addItem(lst_itm)
        box_force_static_134.setCurrentIndex(1)
        box_force_static_134.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_134.addWidget(box_force_static_134)
        bg_box.addLayout(hbox_lay_force_static_134)

        label_135 = QLabel("                smoother")
        label_135.setPalette(palette_scope)
        label_135.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_135)

        hbox_lay_num_intervals_136 =  QHBoxLayout()
        label_num_intervals_136 = QLabel("                    num_intervals")
        label_num_intervals_136.setPalette(palette_object)
        label_num_intervals_136.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_136.addWidget(label_num_intervals_136)

        box_num_intervals_136 = QComboBox()
        box_num_intervals_136.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.num_intervals"
        box_num_intervals_136.tmp_lst=[]
        box_num_intervals_136.tmp_lst.append("fixed_width")
        box_num_intervals_136.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_136.tmp_lst:
            box_num_intervals_136.addItem(lst_itm)
        box_num_intervals_136.setCurrentIndex(0)
        box_num_intervals_136.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_136.addWidget(box_num_intervals_136)
        bg_box.addLayout(hbox_lay_num_intervals_136)

        hbox_lay_interval_width_degrees_137 =  QHBoxLayout()
        label_interval_width_degrees_137 = QLabel("                    interval_width_degrees")
        label_interval_width_degrees_137.setPalette(palette_object)
        label_interval_width_degrees_137.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_137.addWidget(label_interval_width_degrees_137)

        box_interval_width_degrees_137 = QDoubleSpinBox()
        box_interval_width_degrees_137.setValue(36.0)
        box_interval_width_degrees_137.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.interval_width_degrees"
        box_interval_width_degrees_137.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_137.addWidget(box_interval_width_degrees_137)
        bg_box.addLayout(hbox_lay_interval_width_degrees_137)

        hbox_lay_absolute_num_intervals_138 =  QHBoxLayout()
        label_absolute_num_intervals_138 = QLabel("                    absolute_num_intervals")
        label_absolute_num_intervals_138.setPalette(palette_object)
        label_absolute_num_intervals_138.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_138.addWidget(label_absolute_num_intervals_138)

        box_absolute_num_intervals_138 = QSpinBox()
        box_absolute_num_intervals_138.setValue(5)
        box_absolute_num_intervals_138.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.absolute_num_intervals"
        box_absolute_num_intervals_138.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_138.addWidget(box_absolute_num_intervals_138)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_138)

        label_139 = QLabel("            orientation")
        label_139.setPalette(palette_scope)
        label_139.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_139)


        hbox_lay_force_static_141 =  QHBoxLayout()
        label_force_static_141 = QLabel("                force_static")
        label_force_static_141.setPalette(palette_object)
        label_force_static_141.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_141.addWidget(label_force_static_141)

        box_force_static_141 = QComboBox()
        box_force_static_141.local_path = "refinement.parameterisation.crystal.orientation.force_static"
        box_force_static_141.tmp_lst=[]
        box_force_static_141.tmp_lst.append("True")
        box_force_static_141.tmp_lst.append("False")
        for lst_itm in box_force_static_141.tmp_lst:
            box_force_static_141.addItem(lst_itm)
        box_force_static_141.setCurrentIndex(1)
        box_force_static_141.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_141.addWidget(box_force_static_141)
        bg_box.addLayout(hbox_lay_force_static_141)

        label_142 = QLabel("                smoother")
        label_142.setPalette(palette_scope)
        label_142.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_142)

        hbox_lay_num_intervals_143 =  QHBoxLayout()
        label_num_intervals_143 = QLabel("                    num_intervals")
        label_num_intervals_143.setPalette(palette_object)
        label_num_intervals_143.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_143.addWidget(label_num_intervals_143)

        box_num_intervals_143 = QComboBox()
        box_num_intervals_143.local_path = "refinement.parameterisation.crystal.orientation.smoother.num_intervals"
        box_num_intervals_143.tmp_lst=[]
        box_num_intervals_143.tmp_lst.append("fixed_width")
        box_num_intervals_143.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_143.tmp_lst:
            box_num_intervals_143.addItem(lst_itm)
        box_num_intervals_143.setCurrentIndex(0)
        box_num_intervals_143.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_143.addWidget(box_num_intervals_143)
        bg_box.addLayout(hbox_lay_num_intervals_143)

        hbox_lay_interval_width_degrees_144 =  QHBoxLayout()
        label_interval_width_degrees_144 = QLabel("                    interval_width_degrees")
        label_interval_width_degrees_144.setPalette(palette_object)
        label_interval_width_degrees_144.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_144.addWidget(label_interval_width_degrees_144)

        box_interval_width_degrees_144 = QDoubleSpinBox()
        box_interval_width_degrees_144.setValue(36.0)
        box_interval_width_degrees_144.local_path = "refinement.parameterisation.crystal.orientation.smoother.interval_width_degrees"
        box_interval_width_degrees_144.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_144.addWidget(box_interval_width_degrees_144)
        bg_box.addLayout(hbox_lay_interval_width_degrees_144)

        hbox_lay_absolute_num_intervals_145 =  QHBoxLayout()
        label_absolute_num_intervals_145 = QLabel("                    absolute_num_intervals")
        label_absolute_num_intervals_145.setPalette(palette_object)
        label_absolute_num_intervals_145.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_145.addWidget(label_absolute_num_intervals_145)

        box_absolute_num_intervals_145 = QSpinBox()
        box_absolute_num_intervals_145.setValue(5)
        box_absolute_num_intervals_145.local_path = "refinement.parameterisation.crystal.orientation.smoother.absolute_num_intervals"
        box_absolute_num_intervals_145.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_145.addWidget(box_absolute_num_intervals_145)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_145)

        label_146 = QLabel("        detector")
        label_146.setPalette(palette_scope)
        label_146.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_146)

        hbox_lay_panels_147 =  QHBoxLayout()
        label_panels_147 = QLabel("            panels")
        label_panels_147.setPalette(palette_object)
        label_panels_147.setFont(QFont("Monospace", 10))
        hbox_lay_panels_147.addWidget(label_panels_147)

        box_panels_147 = QComboBox()
        box_panels_147.local_path = "refinement.parameterisation.detector.panels"
        box_panels_147.tmp_lst=[]
        box_panels_147.tmp_lst.append("automatic")
        box_panels_147.tmp_lst.append("single")
        box_panels_147.tmp_lst.append("multiple")
        box_panels_147.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_147.tmp_lst:
            box_panels_147.addItem(lst_itm)
        box_panels_147.setCurrentIndex(0)
        box_panels_147.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_147.addWidget(box_panels_147)
        bg_box.addLayout(hbox_lay_panels_147)

        hbox_lay_hierarchy_level_148 =  QHBoxLayout()
        label_hierarchy_level_148 = QLabel("            hierarchy_level")
        label_hierarchy_level_148.setPalette(palette_object)
        label_hierarchy_level_148.setFont(QFont("Monospace", 10))
        hbox_lay_hierarchy_level_148.addWidget(label_hierarchy_level_148)

        box_hierarchy_level_148 = QSpinBox()
        box_hierarchy_level_148.setValue(0)
        box_hierarchy_level_148.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_148.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_148.addWidget(box_hierarchy_level_148)
        bg_box.addLayout(hbox_lay_hierarchy_level_148)

        hbox_lay_fix_149 =  QHBoxLayout()
        label_fix_149 = QLabel("            fix")
        label_fix_149.setPalette(palette_object)
        label_fix_149.setFont(QFont("Monospace", 10))
        hbox_lay_fix_149.addWidget(label_fix_149)

        box_fix_149 = QComboBox()
        box_fix_149.local_path = "refinement.parameterisation.detector.fix"
        box_fix_149.tmp_lst=[]
        box_fix_149.tmp_lst.append("all")
        box_fix_149.tmp_lst.append("position")
        box_fix_149.tmp_lst.append("orientation")
        for lst_itm in box_fix_149.tmp_lst:
            box_fix_149.addItem(lst_itm)
        box_fix_149.setCurrentIndex(0)
        box_fix_149.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_149.addWidget(box_fix_149)
        bg_box.addLayout(hbox_lay_fix_149)


        hbox_lay_force_static_151 =  QHBoxLayout()
        label_force_static_151 = QLabel("            force_static")
        label_force_static_151.setPalette(palette_object)
        label_force_static_151.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_151.addWidget(label_force_static_151)

        box_force_static_151 = QComboBox()
        box_force_static_151.local_path = "refinement.parameterisation.detector.force_static"
        box_force_static_151.tmp_lst=[]
        box_force_static_151.tmp_lst.append("True")
        box_force_static_151.tmp_lst.append("False")
        for lst_itm in box_force_static_151.tmp_lst:
            box_force_static_151.addItem(lst_itm)
        box_force_static_151.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_151.addWidget(box_force_static_151)
        bg_box.addLayout(hbox_lay_force_static_151)

        label_152 = QLabel("            smoother")
        label_152.setPalette(palette_scope)
        label_152.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_152)

        hbox_lay_num_intervals_153 =  QHBoxLayout()
        label_num_intervals_153 = QLabel("                num_intervals")
        label_num_intervals_153.setPalette(palette_object)
        label_num_intervals_153.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_153.addWidget(label_num_intervals_153)

        box_num_intervals_153 = QComboBox()
        box_num_intervals_153.local_path = "refinement.parameterisation.detector.smoother.num_intervals"
        box_num_intervals_153.tmp_lst=[]
        box_num_intervals_153.tmp_lst.append("fixed_width")
        box_num_intervals_153.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_153.tmp_lst:
            box_num_intervals_153.addItem(lst_itm)
        box_num_intervals_153.setCurrentIndex(0)
        box_num_intervals_153.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_153.addWidget(box_num_intervals_153)
        bg_box.addLayout(hbox_lay_num_intervals_153)

        hbox_lay_interval_width_degrees_154 =  QHBoxLayout()
        label_interval_width_degrees_154 = QLabel("                interval_width_degrees")
        label_interval_width_degrees_154.setPalette(palette_object)
        label_interval_width_degrees_154.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_154.addWidget(label_interval_width_degrees_154)

        box_interval_width_degrees_154 = QDoubleSpinBox()
        box_interval_width_degrees_154.setValue(36.0)
        box_interval_width_degrees_154.local_path = "refinement.parameterisation.detector.smoother.interval_width_degrees"
        box_interval_width_degrees_154.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_154.addWidget(box_interval_width_degrees_154)
        bg_box.addLayout(hbox_lay_interval_width_degrees_154)

        hbox_lay_absolute_num_intervals_155 =  QHBoxLayout()
        label_absolute_num_intervals_155 = QLabel("                absolute_num_intervals")
        label_absolute_num_intervals_155.setPalette(palette_object)
        label_absolute_num_intervals_155.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_155.addWidget(label_absolute_num_intervals_155)

        box_absolute_num_intervals_155 = QSpinBox()
        box_absolute_num_intervals_155.setValue(5)
        box_absolute_num_intervals_155.local_path = "refinement.parameterisation.detector.smoother.absolute_num_intervals"
        box_absolute_num_intervals_155.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_155.addWidget(box_absolute_num_intervals_155)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_155)

        hbox_lay_sparse_156 =  QHBoxLayout()
        label_sparse_156 = QLabel("        sparse")
        label_sparse_156.setPalette(palette_object)
        label_sparse_156.setFont(QFont("Monospace", 10))
        hbox_lay_sparse_156.addWidget(label_sparse_156)

        box_sparse_156 = QComboBox()
        box_sparse_156.local_path = "refinement.parameterisation.sparse"
        box_sparse_156.tmp_lst=[]
        box_sparse_156.tmp_lst.append("True")
        box_sparse_156.tmp_lst.append("False")
        for lst_itm in box_sparse_156.tmp_lst:
            box_sparse_156.addItem(lst_itm)
        box_sparse_156.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_156.addWidget(box_sparse_156)
        bg_box.addLayout(hbox_lay_sparse_156)

        hbox_lay_treat_single_image_as_still_157 =  QHBoxLayout()
        label_treat_single_image_as_still_157 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_157.setPalette(palette_object)
        label_treat_single_image_as_still_157.setFont(QFont("Monospace", 10))
        hbox_lay_treat_single_image_as_still_157.addWidget(label_treat_single_image_as_still_157)

        box_treat_single_image_as_still_157 = QComboBox()
        box_treat_single_image_as_still_157.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_157.tmp_lst=[]
        box_treat_single_image_as_still_157.tmp_lst.append("True")
        box_treat_single_image_as_still_157.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_157.tmp_lst:
            box_treat_single_image_as_still_157.addItem(lst_itm)
        box_treat_single_image_as_still_157.setCurrentIndex(1)
        box_treat_single_image_as_still_157.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_157.addWidget(box_treat_single_image_as_still_157)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_157)

        hbox_lay_spherical_relp_model_158 =  QHBoxLayout()
        label_spherical_relp_model_158 = QLabel("        spherical_relp_model")
        label_spherical_relp_model_158.setPalette(palette_object)
        label_spherical_relp_model_158.setFont(QFont("Monospace", 10))
        hbox_lay_spherical_relp_model_158.addWidget(label_spherical_relp_model_158)

        box_spherical_relp_model_158 = QComboBox()
        box_spherical_relp_model_158.local_path = "refinement.parameterisation.spherical_relp_model"
        box_spherical_relp_model_158.tmp_lst=[]
        box_spherical_relp_model_158.tmp_lst.append("True")
        box_spherical_relp_model_158.tmp_lst.append("False")
        for lst_itm in box_spherical_relp_model_158.tmp_lst:
            box_spherical_relp_model_158.addItem(lst_itm)
        box_spherical_relp_model_158.setCurrentIndex(1)
        box_spherical_relp_model_158.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_spherical_relp_model_158.addWidget(box_spherical_relp_model_158)
        bg_box.addLayout(hbox_lay_spherical_relp_model_158)

        label_159 = QLabel("    refinery")
        label_159.setPalette(palette_scope)
        label_159.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_159)

        hbox_lay_engine_160 =  QHBoxLayout()
        label_engine_160 = QLabel("        engine")
        label_engine_160.setPalette(palette_object)
        label_engine_160.setFont(QFont("Monospace", 10))
        hbox_lay_engine_160.addWidget(label_engine_160)

        box_engine_160 = QComboBox()
        box_engine_160.local_path = "refinement.refinery.engine"
        box_engine_160.tmp_lst=[]
        box_engine_160.tmp_lst.append("SimpleLBFGS")
        box_engine_160.tmp_lst.append("LBFGScurvs")
        box_engine_160.tmp_lst.append("GaussNewton")
        box_engine_160.tmp_lst.append("LevMar")
        box_engine_160.tmp_lst.append("SparseLevMar")
        for lst_itm in box_engine_160.tmp_lst:
            box_engine_160.addItem(lst_itm)
        box_engine_160.setCurrentIndex(3)
        box_engine_160.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_160.addWidget(box_engine_160)
        bg_box.addLayout(hbox_lay_engine_160)

        hbox_lay_track_step_161 =  QHBoxLayout()
        label_track_step_161 = QLabel("        track_step")
        label_track_step_161.setPalette(palette_object)
        label_track_step_161.setFont(QFont("Monospace", 10))
        hbox_lay_track_step_161.addWidget(label_track_step_161)

        box_track_step_161 = QComboBox()
        box_track_step_161.local_path = "refinement.refinery.track_step"
        box_track_step_161.tmp_lst=[]
        box_track_step_161.tmp_lst.append("True")
        box_track_step_161.tmp_lst.append("False")
        for lst_itm in box_track_step_161.tmp_lst:
            box_track_step_161.addItem(lst_itm)
        box_track_step_161.setCurrentIndex(1)
        box_track_step_161.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_161.addWidget(box_track_step_161)
        bg_box.addLayout(hbox_lay_track_step_161)

        hbox_lay_track_gradient_162 =  QHBoxLayout()
        label_track_gradient_162 = QLabel("        track_gradient")
        label_track_gradient_162.setPalette(palette_object)
        label_track_gradient_162.setFont(QFont("Monospace", 10))
        hbox_lay_track_gradient_162.addWidget(label_track_gradient_162)

        box_track_gradient_162 = QComboBox()
        box_track_gradient_162.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_162.tmp_lst=[]
        box_track_gradient_162.tmp_lst.append("True")
        box_track_gradient_162.tmp_lst.append("False")
        for lst_itm in box_track_gradient_162.tmp_lst:
            box_track_gradient_162.addItem(lst_itm)
        box_track_gradient_162.setCurrentIndex(1)
        box_track_gradient_162.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_162.addWidget(box_track_gradient_162)
        bg_box.addLayout(hbox_lay_track_gradient_162)

        hbox_lay_track_parameter_correlation_163 =  QHBoxLayout()
        label_track_parameter_correlation_163 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_163.setPalette(palette_object)
        label_track_parameter_correlation_163.setFont(QFont("Monospace", 10))
        hbox_lay_track_parameter_correlation_163.addWidget(label_track_parameter_correlation_163)

        box_track_parameter_correlation_163 = QComboBox()
        box_track_parameter_correlation_163.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_163.tmp_lst=[]
        box_track_parameter_correlation_163.tmp_lst.append("True")
        box_track_parameter_correlation_163.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_163.tmp_lst:
            box_track_parameter_correlation_163.addItem(lst_itm)
        box_track_parameter_correlation_163.setCurrentIndex(1)
        box_track_parameter_correlation_163.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_163.addWidget(box_track_parameter_correlation_163)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_163)

        hbox_lay_track_out_of_sample_rmsd_164 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_164 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_164.setPalette(palette_object)
        label_track_out_of_sample_rmsd_164.setFont(QFont("Monospace", 10))
        hbox_lay_track_out_of_sample_rmsd_164.addWidget(label_track_out_of_sample_rmsd_164)

        box_track_out_of_sample_rmsd_164 = QComboBox()
        box_track_out_of_sample_rmsd_164.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_164.tmp_lst=[]
        box_track_out_of_sample_rmsd_164.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_164.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_164.tmp_lst:
            box_track_out_of_sample_rmsd_164.addItem(lst_itm)
        box_track_out_of_sample_rmsd_164.setCurrentIndex(1)
        box_track_out_of_sample_rmsd_164.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_164.addWidget(box_track_out_of_sample_rmsd_164)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_164)


        hbox_lay_max_iterations_166 =  QHBoxLayout()
        label_max_iterations_166 = QLabel("        max_iterations")
        label_max_iterations_166.setPalette(palette_object)
        label_max_iterations_166.setFont(QFont("Monospace", 10))
        hbox_lay_max_iterations_166.addWidget(label_max_iterations_166)

        box_max_iterations_166 = QSpinBox()
        box_max_iterations_166.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_166.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_166.addWidget(box_max_iterations_166)
        bg_box.addLayout(hbox_lay_max_iterations_166)

        label_167 = QLabel("    target")
        label_167.setPalette(palette_scope)
        label_167.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_167)

        hbox_lay_rmsd_cutoff_168 =  QHBoxLayout()
        label_rmsd_cutoff_168 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_168.setPalette(palette_object)
        label_rmsd_cutoff_168.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_168.addWidget(label_rmsd_cutoff_168)

        box_rmsd_cutoff_168 = QComboBox()
        box_rmsd_cutoff_168.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_168.tmp_lst=[]
        box_rmsd_cutoff_168.tmp_lst.append("fraction_of_bin_size")
        box_rmsd_cutoff_168.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_168.tmp_lst:
            box_rmsd_cutoff_168.addItem(lst_itm)
        box_rmsd_cutoff_168.setCurrentIndex(0)
        box_rmsd_cutoff_168.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_168.addWidget(box_rmsd_cutoff_168)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_168)

        hbox_lay_bin_size_fraction_169 =  QHBoxLayout()
        label_bin_size_fraction_169 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_169.setPalette(palette_object)
        label_bin_size_fraction_169.setFont(QFont("Monospace", 10))
        hbox_lay_bin_size_fraction_169.addWidget(label_bin_size_fraction_169)

        box_bin_size_fraction_169 = QDoubleSpinBox()
        box_bin_size_fraction_169.setValue(0.0)
        box_bin_size_fraction_169.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_169.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_169.addWidget(box_bin_size_fraction_169)
        bg_box.addLayout(hbox_lay_bin_size_fraction_169)

        hbox_lay_absolute_cutoffs_170_0 =  QHBoxLayout()
        label_absolute_cutoffs_170_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_170_0.setPalette(palette_object)
        label_absolute_cutoffs_170_0.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_170_0.addWidget(label_absolute_cutoffs_170_0)
        box_absolute_cutoffs_170_0 = QDoubleSpinBox()
        box_absolute_cutoffs_170_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_170_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_170_1 =  QHBoxLayout()
        label_absolute_cutoffs_170_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_170_1.setPalette(palette_object)
        label_absolute_cutoffs_170_1.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_170_1.addWidget(label_absolute_cutoffs_170_1)
        box_absolute_cutoffs_170_1 = QDoubleSpinBox()
        box_absolute_cutoffs_170_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_170_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_170_2 =  QHBoxLayout()
        label_absolute_cutoffs_170_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_170_2.setPalette(palette_object)
        label_absolute_cutoffs_170_2.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_170_2.addWidget(label_absolute_cutoffs_170_2)
        box_absolute_cutoffs_170_2 = QDoubleSpinBox()
        box_absolute_cutoffs_170_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_170_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_170_0.addWidget(box_absolute_cutoffs_170_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_170_0)
        hbox_lay_absolute_cutoffs_170_1.addWidget(box_absolute_cutoffs_170_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_170_1)
        hbox_lay_absolute_cutoffs_170_2.addWidget(box_absolute_cutoffs_170_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_170_2)

        hbox_lay_gradient_calculation_blocksize_171 =  QHBoxLayout()
        label_gradient_calculation_blocksize_171 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_171.setPalette(palette_object)
        label_gradient_calculation_blocksize_171.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_calculation_blocksize_171.addWidget(label_gradient_calculation_blocksize_171)

        box_gradient_calculation_blocksize_171 = QSpinBox()
        box_gradient_calculation_blocksize_171.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_171.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_171.addWidget(box_gradient_calculation_blocksize_171)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_171)

        label_172 = QLabel("    reflections")
        label_172.setPalette(palette_scope)
        label_172.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_172)

        hbox_lay_reflections_per_degree_173 =  QHBoxLayout()
        label_reflections_per_degree_173 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_173.setPalette(palette_object)
        label_reflections_per_degree_173.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_173.addWidget(label_reflections_per_degree_173)

        box_reflections_per_degree_173 = QDoubleSpinBox()
        box_reflections_per_degree_173.setValue(100.0)
        box_reflections_per_degree_173.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_173.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_173.addWidget(box_reflections_per_degree_173)
        bg_box.addLayout(hbox_lay_reflections_per_degree_173)

        hbox_lay_minimum_sample_size_174 =  QHBoxLayout()
        label_minimum_sample_size_174 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_174.setPalette(palette_object)
        label_minimum_sample_size_174.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_174.addWidget(label_minimum_sample_size_174)

        box_minimum_sample_size_174 = QSpinBox()
        box_minimum_sample_size_174.setValue(1000)
        box_minimum_sample_size_174.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_174.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_174.addWidget(box_minimum_sample_size_174)
        bg_box.addLayout(hbox_lay_minimum_sample_size_174)

        hbox_lay_maximum_sample_size_175 =  QHBoxLayout()
        label_maximum_sample_size_175 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_175.setPalette(palette_object)
        label_maximum_sample_size_175.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_175.addWidget(label_maximum_sample_size_175)

        box_maximum_sample_size_175 = QSpinBox()
        box_maximum_sample_size_175.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_175.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_175.addWidget(box_maximum_sample_size_175)
        bg_box.addLayout(hbox_lay_maximum_sample_size_175)

        hbox_lay_random_seed_176 =  QHBoxLayout()
        label_random_seed_176 = QLabel("        random_seed")
        label_random_seed_176.setPalette(palette_object)
        label_random_seed_176.setFont(QFont("Monospace", 10))
        hbox_lay_random_seed_176.addWidget(label_random_seed_176)

        box_random_seed_176 = QSpinBox()
        box_random_seed_176.setValue(42)
        box_random_seed_176.local_path = "refinement.reflections.random_seed"
        box_random_seed_176.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_176.addWidget(box_random_seed_176)
        bg_box.addLayout(hbox_lay_random_seed_176)

        hbox_lay_close_to_spindle_cutoff_177 =  QHBoxLayout()
        label_close_to_spindle_cutoff_177 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_177.setPalette(palette_object)
        label_close_to_spindle_cutoff_177.setFont(QFont("Monospace", 10))
        hbox_lay_close_to_spindle_cutoff_177.addWidget(label_close_to_spindle_cutoff_177)

        box_close_to_spindle_cutoff_177 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_177.setValue(0.02)
        box_close_to_spindle_cutoff_177.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_177.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_177.addWidget(box_close_to_spindle_cutoff_177)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_177)

        hbox_lay_block_width_178 =  QHBoxLayout()
        label_block_width_178 = QLabel("        block_width")
        label_block_width_178.setPalette(palette_object)
        label_block_width_178.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_178.addWidget(label_block_width_178)

        box_block_width_178 = QDoubleSpinBox()
        box_block_width_178.setValue(1.0)
        box_block_width_178.local_path = "refinement.reflections.block_width"
        box_block_width_178.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_178.addWidget(box_block_width_178)
        bg_box.addLayout(hbox_lay_block_width_178)

        label_179 = QLabel("        weighting_strategy")
        label_179.setPalette(palette_scope)
        label_179.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_179)

        hbox_lay_override_180 =  QHBoxLayout()
        label_override_180 = QLabel("            override")
        label_override_180.setPalette(palette_object)
        label_override_180.setFont(QFont("Monospace", 10))
        hbox_lay_override_180.addWidget(label_override_180)

        box_override_180 = QComboBox()
        box_override_180.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_180.tmp_lst=[]
        box_override_180.tmp_lst.append("statistical")
        box_override_180.tmp_lst.append("stills")
        box_override_180.tmp_lst.append("constant")
        box_override_180.tmp_lst.append("external_deltapsi")
        for lst_itm in box_override_180.tmp_lst:
            box_override_180.addItem(lst_itm)
        box_override_180.setCurrentIndex(0)
        box_override_180.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_180.addWidget(box_override_180)
        bg_box.addLayout(hbox_lay_override_180)

        hbox_lay_delpsi_constant_181 =  QHBoxLayout()
        label_delpsi_constant_181 = QLabel("            delpsi_constant")
        label_delpsi_constant_181.setPalette(palette_object)
        label_delpsi_constant_181.setFont(QFont("Monospace", 10))
        hbox_lay_delpsi_constant_181.addWidget(label_delpsi_constant_181)

        box_delpsi_constant_181 = QDoubleSpinBox()
        box_delpsi_constant_181.setValue(1000000.0)
        box_delpsi_constant_181.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_181.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_181.addWidget(box_delpsi_constant_181)
        bg_box.addLayout(hbox_lay_delpsi_constant_181)

        hbox_lay_constants_182_0 =  QHBoxLayout()
        label_constants_182_0 = QLabel("            constants[1]")
        label_constants_182_0.setPalette(palette_object)
        label_constants_182_0.setFont(QFont("Monospace", 10))
        hbox_lay_constants_182_0.addWidget(label_constants_182_0)
        box_constants_182_0 = QDoubleSpinBox()
        box_constants_182_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_182_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_182_1 =  QHBoxLayout()
        label_constants_182_1 = QLabel("            constants[2]")
        label_constants_182_1.setPalette(palette_object)
        label_constants_182_1.setFont(QFont("Monospace", 10))
        hbox_lay_constants_182_1.addWidget(label_constants_182_1)
        box_constants_182_1 = QDoubleSpinBox()
        box_constants_182_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_182_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_182_2 =  QHBoxLayout()
        label_constants_182_2 = QLabel("            constants[3]")
        label_constants_182_2.setPalette(palette_object)
        label_constants_182_2.setFont(QFont("Monospace", 10))
        hbox_lay_constants_182_2.addWidget(label_constants_182_2)
        box_constants_182_2 = QDoubleSpinBox()
        box_constants_182_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_182_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_182_0.addWidget(box_constants_182_0)
        bg_box.addLayout(hbox_lay_constants_182_0)
        hbox_lay_constants_182_1.addWidget(box_constants_182_1)
        bg_box.addLayout(hbox_lay_constants_182_1)
        hbox_lay_constants_182_2.addWidget(box_constants_182_2)
        bg_box.addLayout(hbox_lay_constants_182_2)

        label_183 = QLabel("        outlier")
        label_183.setPalette(palette_scope)
        label_183.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_183)

        hbox_lay_algorithm_184 =  QHBoxLayout()
        label_algorithm_184 = QLabel("            algorithm")
        label_algorithm_184.setPalette(palette_object)
        label_algorithm_184.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_184.addWidget(label_algorithm_184)

        box_algorithm_184 = QComboBox()
        box_algorithm_184.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_184.tmp_lst=[]
        box_algorithm_184.tmp_lst.append("null")
        box_algorithm_184.tmp_lst.append("auto")
        box_algorithm_184.tmp_lst.append("mcd")
        box_algorithm_184.tmp_lst.append("tukey")
        box_algorithm_184.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_184.tmp_lst:
            box_algorithm_184.addItem(lst_itm)
        box_algorithm_184.setCurrentIndex(1)
        box_algorithm_184.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_184.addWidget(box_algorithm_184)
        bg_box.addLayout(hbox_lay_algorithm_184)

        hbox_lay_minimum_number_of_reflections_185 =  QHBoxLayout()
        label_minimum_number_of_reflections_185 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_185.setPalette(palette_object)
        label_minimum_number_of_reflections_185.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_number_of_reflections_185.addWidget(label_minimum_number_of_reflections_185)

        box_minimum_number_of_reflections_185 = QSpinBox()
        box_minimum_number_of_reflections_185.setValue(20)
        box_minimum_number_of_reflections_185.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_185.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_185.addWidget(box_minimum_number_of_reflections_185)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_185)

        hbox_lay_separate_experiments_186 =  QHBoxLayout()
        label_separate_experiments_186 = QLabel("            separate_experiments")
        label_separate_experiments_186.setPalette(palette_object)
        label_separate_experiments_186.setFont(QFont("Monospace", 10))
        hbox_lay_separate_experiments_186.addWidget(label_separate_experiments_186)

        box_separate_experiments_186 = QComboBox()
        box_separate_experiments_186.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_186.tmp_lst=[]
        box_separate_experiments_186.tmp_lst.append("True")
        box_separate_experiments_186.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_186.tmp_lst:
            box_separate_experiments_186.addItem(lst_itm)
        box_separate_experiments_186.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_186.addWidget(box_separate_experiments_186)
        bg_box.addLayout(hbox_lay_separate_experiments_186)

        hbox_lay_separate_panels_187 =  QHBoxLayout()
        label_separate_panels_187 = QLabel("            separate_panels")
        label_separate_panels_187.setPalette(palette_object)
        label_separate_panels_187.setFont(QFont("Monospace", 10))
        hbox_lay_separate_panels_187.addWidget(label_separate_panels_187)

        box_separate_panels_187 = QComboBox()
        box_separate_panels_187.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_187.tmp_lst=[]
        box_separate_panels_187.tmp_lst.append("True")
        box_separate_panels_187.tmp_lst.append("False")
        for lst_itm in box_separate_panels_187.tmp_lst:
            box_separate_panels_187.addItem(lst_itm)
        box_separate_panels_187.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_187.addWidget(box_separate_panels_187)
        bg_box.addLayout(hbox_lay_separate_panels_187)

        hbox_lay_separate_blocks_188 =  QHBoxLayout()
        label_separate_blocks_188 = QLabel("            separate_blocks")
        label_separate_blocks_188.setPalette(palette_object)
        label_separate_blocks_188.setFont(QFont("Monospace", 10))
        hbox_lay_separate_blocks_188.addWidget(label_separate_blocks_188)

        box_separate_blocks_188 = QComboBox()
        box_separate_blocks_188.local_path = "refinement.reflections.outlier.separate_blocks"
        box_separate_blocks_188.tmp_lst=[]
        box_separate_blocks_188.tmp_lst.append("True")
        box_separate_blocks_188.tmp_lst.append("False")
        for lst_itm in box_separate_blocks_188.tmp_lst:
            box_separate_blocks_188.addItem(lst_itm)
        box_separate_blocks_188.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_blocks_188.addWidget(box_separate_blocks_188)
        bg_box.addLayout(hbox_lay_separate_blocks_188)

        hbox_lay_block_width_189 =  QHBoxLayout()
        label_block_width_189 = QLabel("            block_width")
        label_block_width_189.setPalette(palette_object)
        label_block_width_189.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_189.addWidget(label_block_width_189)

        box_block_width_189 = QDoubleSpinBox()
        box_block_width_189.local_path = "refinement.reflections.outlier.block_width"
        box_block_width_189.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_189.addWidget(box_block_width_189)
        bg_box.addLayout(hbox_lay_block_width_189)

        label_190 = QLabel("            tukey")
        label_190.setPalette(palette_scope)
        label_190.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_190)

        hbox_lay_iqr_multiplier_191 =  QHBoxLayout()
        label_iqr_multiplier_191 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_191.setPalette(palette_object)
        label_iqr_multiplier_191.setFont(QFont("Monospace", 10))
        hbox_lay_iqr_multiplier_191.addWidget(label_iqr_multiplier_191)

        box_iqr_multiplier_191 = QDoubleSpinBox()
        box_iqr_multiplier_191.setValue(1.5)
        box_iqr_multiplier_191.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_191.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_191.addWidget(box_iqr_multiplier_191)
        bg_box.addLayout(hbox_lay_iqr_multiplier_191)

        label_192 = QLabel("            mcd")
        label_192.setPalette(palette_scope)
        label_192.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_192)

        hbox_lay_alpha_193 =  QHBoxLayout()
        label_alpha_193 = QLabel("                alpha")
        label_alpha_193.setPalette(palette_object)
        label_alpha_193.setFont(QFont("Monospace", 10))
        hbox_lay_alpha_193.addWidget(label_alpha_193)

        box_alpha_193 = QDoubleSpinBox()
        box_alpha_193.setValue(0.5)
        box_alpha_193.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_193.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_193.addWidget(box_alpha_193)
        bg_box.addLayout(hbox_lay_alpha_193)

        hbox_lay_max_n_groups_194 =  QHBoxLayout()
        label_max_n_groups_194 = QLabel("                max_n_groups")
        label_max_n_groups_194.setPalette(palette_object)
        label_max_n_groups_194.setFont(QFont("Monospace", 10))
        hbox_lay_max_n_groups_194.addWidget(label_max_n_groups_194)

        box_max_n_groups_194 = QSpinBox()
        box_max_n_groups_194.setValue(5)
        box_max_n_groups_194.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_194.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_194.addWidget(box_max_n_groups_194)
        bg_box.addLayout(hbox_lay_max_n_groups_194)

        hbox_lay_min_group_size_195 =  QHBoxLayout()
        label_min_group_size_195 = QLabel("                min_group_size")
        label_min_group_size_195.setPalette(palette_object)
        label_min_group_size_195.setFont(QFont("Monospace", 10))
        hbox_lay_min_group_size_195.addWidget(label_min_group_size_195)

        box_min_group_size_195 = QSpinBox()
        box_min_group_size_195.setValue(300)
        box_min_group_size_195.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_195.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_195.addWidget(box_min_group_size_195)
        bg_box.addLayout(hbox_lay_min_group_size_195)

        hbox_lay_n_trials_196 =  QHBoxLayout()
        label_n_trials_196 = QLabel("                n_trials")
        label_n_trials_196.setPalette(palette_object)
        label_n_trials_196.setFont(QFont("Monospace", 10))
        hbox_lay_n_trials_196.addWidget(label_n_trials_196)

        box_n_trials_196 = QSpinBox()
        box_n_trials_196.setValue(500)
        box_n_trials_196.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_196.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_196.addWidget(box_n_trials_196)
        bg_box.addLayout(hbox_lay_n_trials_196)

        hbox_lay_k1_197 =  QHBoxLayout()
        label_k1_197 = QLabel("                k1")
        label_k1_197.setPalette(palette_object)
        label_k1_197.setFont(QFont("Monospace", 10))
        hbox_lay_k1_197.addWidget(label_k1_197)

        box_k1_197 = QSpinBox()
        box_k1_197.setValue(2)
        box_k1_197.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_197.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_197.addWidget(box_k1_197)
        bg_box.addLayout(hbox_lay_k1_197)

        hbox_lay_k2_198 =  QHBoxLayout()
        label_k2_198 = QLabel("                k2")
        label_k2_198.setPalette(palette_object)
        label_k2_198.setFont(QFont("Monospace", 10))
        hbox_lay_k2_198.addWidget(label_k2_198)

        box_k2_198 = QSpinBox()
        box_k2_198.setValue(2)
        box_k2_198.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_198.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_198.addWidget(box_k2_198)
        bg_box.addLayout(hbox_lay_k2_198)

        hbox_lay_k3_199 =  QHBoxLayout()
        label_k3_199 = QLabel("                k3")
        label_k3_199.setPalette(palette_object)
        label_k3_199.setFont(QFont("Monospace", 10))
        hbox_lay_k3_199.addWidget(label_k3_199)

        box_k3_199 = QSpinBox()
        box_k3_199.setValue(100)
        box_k3_199.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_199.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_199.addWidget(box_k3_199)
        bg_box.addLayout(hbox_lay_k3_199)

        hbox_lay_threshold_probability_200 =  QHBoxLayout()
        label_threshold_probability_200 = QLabel("                threshold_probability")
        label_threshold_probability_200.setPalette(palette_object)
        label_threshold_probability_200.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_probability_200.addWidget(label_threshold_probability_200)

        box_threshold_probability_200 = QDoubleSpinBox()
        box_threshold_probability_200.setValue(0.975)
        box_threshold_probability_200.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_200.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_200.addWidget(box_threshold_probability_200)
        bg_box.addLayout(hbox_lay_threshold_probability_200)

        label_201 = QLabel("            sauter_poon")
        label_201.setPalette(palette_scope)
        label_201.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_201)

        hbox_lay_px_sz_202_0 =  QHBoxLayout()
        label_px_sz_202_0 = QLabel("                px_sz[1]")
        label_px_sz_202_0.setPalette(palette_object)
        label_px_sz_202_0.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_202_0.addWidget(label_px_sz_202_0)
        box_px_sz_202_0 = QDoubleSpinBox()
        box_px_sz_202_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_202_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_202_1 =  QHBoxLayout()
        label_px_sz_202_1 = QLabel("                px_sz[2]")
        label_px_sz_202_1.setPalette(palette_object)
        label_px_sz_202_1.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_202_1.addWidget(label_px_sz_202_1)
        box_px_sz_202_1 = QDoubleSpinBox()
        box_px_sz_202_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_202_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_202_0.addWidget(box_px_sz_202_0)
        bg_box.addLayout(hbox_lay_px_sz_202_0)
        hbox_lay_px_sz_202_1.addWidget(box_px_sz_202_1)
        bg_box.addLayout(hbox_lay_px_sz_202_1)

        hbox_lay_verbose_203 =  QHBoxLayout()
        label_verbose_203 = QLabel("                verbose")
        label_verbose_203.setPalette(palette_object)
        label_verbose_203.setFont(QFont("Monospace", 10))
        hbox_lay_verbose_203.addWidget(label_verbose_203)

        box_verbose_203 = QComboBox()
        box_verbose_203.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_203.tmp_lst=[]
        box_verbose_203.tmp_lst.append("True")
        box_verbose_203.tmp_lst.append("False")
        for lst_itm in box_verbose_203.tmp_lst:
            box_verbose_203.addItem(lst_itm)
        box_verbose_203.setCurrentIndex(1)
        box_verbose_203.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_203.addWidget(box_verbose_203)
        bg_box.addLayout(hbox_lay_verbose_203)

        hbox_lay_pdf_204 =  QHBoxLayout()
        label_pdf_204 = QLabel("                pdf")
        label_pdf_204.setPalette(palette_object)
        label_pdf_204.setFont(QFont("Monospace", 10))
        hbox_lay_pdf_204.addWidget(label_pdf_204)

        box_pdf_204 = QLineEdit()
        box_pdf_204.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_204.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_204.addWidget(box_pdf_204)
        bg_box.addLayout(hbox_lay_pdf_204)

        label_205 = QLabel("output")
        label_205.setPalette(palette_scope)
        label_205.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_205)




        hbox_lay_log_209 =  QHBoxLayout()
        label_log_209 = QLabel("    log")
        label_log_209.setPalette(palette_object)
        label_log_209.setFont(QFont("Monospace", 10))
        hbox_lay_log_209.addWidget(label_log_209)

        box_log_209 = QLineEdit()
        box_log_209.local_path = "output.log"
        box_log_209.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_209.addWidget(box_log_209)
        bg_box.addLayout(hbox_lay_log_209)

        hbox_lay_debug_log_210 =  QHBoxLayout()
        label_debug_log_210 = QLabel("    debug_log")
        label_debug_log_210.setPalette(palette_object)
        label_debug_log_210.setFont(QFont("Monospace", 10))
        hbox_lay_debug_log_210.addWidget(label_debug_log_210)

        box_debug_log_210 = QLineEdit()
        box_debug_log_210.local_path = "output.debug_log"
        box_debug_log_210.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_210.addWidget(box_debug_log_210)
        bg_box.addLayout(hbox_lay_debug_log_210)

        hbox_lay_verbosity_211 =  QHBoxLayout()
        label_verbosity_211 = QLabel("verbosity")
        label_verbosity_211.setPalette(palette_object)
        label_verbosity_211.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_211.addWidget(label_verbosity_211)

        box_verbosity_211 = QSpinBox()
        box_verbosity_211.setValue(1)
        box_verbosity_211.local_path = "verbosity"
        box_verbosity_211.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_211.addWidget(box_verbosity_211)
        bg_box.addLayout(hbox_lay_verbosity_211)

 
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
