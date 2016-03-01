import sys
from PySide.QtGui import *
from PySide.QtCore import *
pyqtSignal = Signal
print "using PySide"


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


        label_0 = QLabel("indexing")
        label_0.setPalette(palette_scope)
        label_0.setFont(QFont("Monospace"))
        bg_box.addWidget(label_0)
        hbox_lay_nproc_1 =  QHBoxLayout()
        label_nproc_1 = QLabel("    nproc")
        label_nproc_1.setPalette(palette_object)
        label_nproc_1.setFont(QFont("Monospace"))
        hbox_lay_nproc_1.addWidget(label_nproc_1)

        box_nproc_1 = QSpinBox()
        box_nproc_1.local_path = "indexing.nproc"
        box_nproc_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_1.addWidget(box_nproc_1)
        bg_box.addLayout(hbox_lay_nproc_1)

        hbox_lay_discover_better_experimental_model_2 =  QHBoxLayout()
        label_discover_better_experimental_model_2 = QLabel("    discover_better_experimental_model")
        label_discover_better_experimental_model_2.setPalette(palette_object)
        label_discover_better_experimental_model_2.setFont(QFont("Monospace"))
        hbox_lay_discover_better_experimental_model_2.addWidget(label_discover_better_experimental_model_2)

        box_discover_better_experimental_model_2 = QComboBox()
        box_discover_better_experimental_model_2.local_path = "indexing.discover_better_experimental_model"
        box_discover_better_experimental_model_2.tmp_lst=[]
        box_discover_better_experimental_model_2.tmp_lst.append("True")
        box_discover_better_experimental_model_2.tmp_lst.append("False")
        for lst_itm in box_discover_better_experimental_model_2.tmp_lst:
            box_discover_better_experimental_model_2.addItem(lst_itm)
        box_discover_better_experimental_model_2.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_discover_better_experimental_model_2.addWidget(box_discover_better_experimental_model_2)
        bg_box.addLayout(hbox_lay_discover_better_experimental_model_2)

        hbox_lay_mm_search_scope_3 =  QHBoxLayout()
        label_mm_search_scope_3 = QLabel("    mm_search_scope")
        label_mm_search_scope_3.setPalette(palette_object)
        label_mm_search_scope_3.setFont(QFont("Monospace"))
        hbox_lay_mm_search_scope_3.addWidget(label_mm_search_scope_3)

        box_mm_search_scope_3 = QDoubleSpinBox()
        box_mm_search_scope_3.local_path = "indexing.mm_search_scope"
        box_mm_search_scope_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_mm_search_scope_3.addWidget(box_mm_search_scope_3)
        bg_box.addLayout(hbox_lay_mm_search_scope_3)

        hbox_lay_wide_search_binning_4 =  QHBoxLayout()
        label_wide_search_binning_4 = QLabel("    wide_search_binning")
        label_wide_search_binning_4.setPalette(palette_object)
        label_wide_search_binning_4.setFont(QFont("Monospace"))
        hbox_lay_wide_search_binning_4.addWidget(label_wide_search_binning_4)

        box_wide_search_binning_4 = QDoubleSpinBox()
        box_wide_search_binning_4.local_path = "indexing.wide_search_binning"
        box_wide_search_binning_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_wide_search_binning_4.addWidget(box_wide_search_binning_4)
        bg_box.addLayout(hbox_lay_wide_search_binning_4)

        hbox_lay_min_cell_volume_5 =  QHBoxLayout()
        label_min_cell_volume_5 = QLabel("    min_cell_volume")
        label_min_cell_volume_5.setPalette(palette_object)
        label_min_cell_volume_5.setFont(QFont("Monospace"))
        hbox_lay_min_cell_volume_5.addWidget(label_min_cell_volume_5)

        box_min_cell_volume_5 = QDoubleSpinBox()
        box_min_cell_volume_5.local_path = "indexing.min_cell_volume"
        box_min_cell_volume_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cell_volume_5.addWidget(box_min_cell_volume_5)
        bg_box.addLayout(hbox_lay_min_cell_volume_5)

        hbox_lay_min_cell_6 =  QHBoxLayout()
        label_min_cell_6 = QLabel("    min_cell")
        label_min_cell_6.setPalette(palette_object)
        label_min_cell_6.setFont(QFont("Monospace"))
        hbox_lay_min_cell_6.addWidget(label_min_cell_6)

        box_min_cell_6 = QDoubleSpinBox()
        box_min_cell_6.local_path = "indexing.min_cell"
        box_min_cell_6.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cell_6.addWidget(box_min_cell_6)
        bg_box.addLayout(hbox_lay_min_cell_6)

        hbox_lay_max_cell_7 =  QHBoxLayout()
        label_max_cell_7 = QLabel("    max_cell")
        label_max_cell_7.setPalette(palette_object)
        label_max_cell_7.setFont(QFont("Monospace"))
        hbox_lay_max_cell_7.addWidget(label_max_cell_7)

        box_max_cell_7 = QDoubleSpinBox()
        box_max_cell_7.local_path = "indexing.max_cell"
        box_max_cell_7.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_cell_7.addWidget(box_max_cell_7)
        bg_box.addLayout(hbox_lay_max_cell_7)

        label_8 = QLabel("    max_cell_estimation")
        label_8.setPalette(palette_scope)
        label_8.setFont(QFont("Monospace"))
        bg_box.addWidget(label_8)
        hbox_lay_filter_ice_9 =  QHBoxLayout()
        label_filter_ice_9 = QLabel("        filter_ice")
        label_filter_ice_9.setPalette(palette_object)
        label_filter_ice_9.setFont(QFont("Monospace"))
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
        label_filter_overlaps_10.setFont(QFont("Monospace"))
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
        label_overlaps_border_11.setFont(QFont("Monospace"))
        hbox_lay_overlaps_border_11.addWidget(label_overlaps_border_11)

        box_overlaps_border_11 = QSpinBox()
        box_overlaps_border_11.local_path = "indexing.max_cell_estimation.overlaps_border"
        box_overlaps_border_11.valueChanged.connect(self.spnbox_changed)
        hbox_lay_overlaps_border_11.addWidget(box_overlaps_border_11)
        bg_box.addLayout(hbox_lay_overlaps_border_11)

        hbox_lay_multiplier_12 =  QHBoxLayout()
        label_multiplier_12 = QLabel("        multiplier")
        label_multiplier_12.setPalette(palette_object)
        label_multiplier_12.setFont(QFont("Monospace"))
        hbox_lay_multiplier_12.addWidget(label_multiplier_12)

        box_multiplier_12 = QDoubleSpinBox()
        box_multiplier_12.local_path = "indexing.max_cell_estimation.multiplier"
        box_multiplier_12.valueChanged.connect(self.spnbox_changed)
        hbox_lay_multiplier_12.addWidget(box_multiplier_12)
        bg_box.addLayout(hbox_lay_multiplier_12)

        hbox_lay_step_size_13 =  QHBoxLayout()
        label_step_size_13 = QLabel("        step_size")
        label_step_size_13.setPalette(palette_object)
        label_step_size_13.setFont(QFont("Monospace"))
        hbox_lay_step_size_13.addWidget(label_step_size_13)

        box_step_size_13 = QDoubleSpinBox()
        box_step_size_13.local_path = "indexing.max_cell_estimation.step_size"
        box_step_size_13.valueChanged.connect(self.spnbox_changed)
        hbox_lay_step_size_13.addWidget(box_step_size_13)
        bg_box.addLayout(hbox_lay_step_size_13)

        hbox_lay_nearest_neighbor_percentile_14 =  QHBoxLayout()
        label_nearest_neighbor_percentile_14 = QLabel("        nearest_neighbor_percentile")
        label_nearest_neighbor_percentile_14.setPalette(palette_object)
        label_nearest_neighbor_percentile_14.setFont(QFont("Monospace"))
        hbox_lay_nearest_neighbor_percentile_14.addWidget(label_nearest_neighbor_percentile_14)

        box_nearest_neighbor_percentile_14 = QDoubleSpinBox()
        box_nearest_neighbor_percentile_14.local_path = "indexing.max_cell_estimation.nearest_neighbor_percentile"
        box_nearest_neighbor_percentile_14.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbor_percentile_14.addWidget(box_nearest_neighbor_percentile_14)
        bg_box.addLayout(hbox_lay_nearest_neighbor_percentile_14)

        label_15 = QLabel("    fft3d")
        label_15.setPalette(palette_scope)
        label_15.setFont(QFont("Monospace"))
        bg_box.addWidget(label_15)
        hbox_lay_peak_search_16 =  QHBoxLayout()
        label_peak_search_16 = QLabel("        peak_search")
        label_peak_search_16.setPalette(palette_object)
        label_peak_search_16.setFont(QFont("Monospace"))
        hbox_lay_peak_search_16.addWidget(label_peak_search_16)

        box_peak_search_16 = QComboBox()
        box_peak_search_16.local_path = "indexing.fft3d.peak_search"
        box_peak_search_16.tmp_lst=[]
        box_peak_search_16.tmp_lst.append("*flood_fill")
        box_peak_search_16.tmp_lst.append("clean")
        for lst_itm in box_peak_search_16.tmp_lst:
            box_peak_search_16.addItem(lst_itm)
        box_peak_search_16.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_peak_search_16.addWidget(box_peak_search_16)
        bg_box.addLayout(hbox_lay_peak_search_16)

        hbox_lay_peak_volume_cutoff_17 =  QHBoxLayout()
        label_peak_volume_cutoff_17 = QLabel("        peak_volume_cutoff")
        label_peak_volume_cutoff_17.setPalette(palette_object)
        label_peak_volume_cutoff_17.setFont(QFont("Monospace"))
        hbox_lay_peak_volume_cutoff_17.addWidget(label_peak_volume_cutoff_17)

        box_peak_volume_cutoff_17 = QDoubleSpinBox()
        box_peak_volume_cutoff_17.local_path = "indexing.fft3d.peak_volume_cutoff"
        box_peak_volume_cutoff_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_peak_volume_cutoff_17.addWidget(box_peak_volume_cutoff_17)
        bg_box.addLayout(hbox_lay_peak_volume_cutoff_17)

        label_18 = QLabel("        reciprocal_space_grid")
        label_18.setPalette(palette_scope)
        label_18.setFont(QFont("Monospace"))
        bg_box.addWidget(label_18)
        hbox_lay_n_points_19 =  QHBoxLayout()
        label_n_points_19 = QLabel("            n_points")
        label_n_points_19.setPalette(palette_object)
        label_n_points_19.setFont(QFont("Monospace"))
        hbox_lay_n_points_19.addWidget(label_n_points_19)

        box_n_points_19 = QSpinBox()
        box_n_points_19.local_path = "indexing.fft3d.reciprocal_space_grid.n_points"
        box_n_points_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_points_19.addWidget(box_n_points_19)
        bg_box.addLayout(hbox_lay_n_points_19)

        hbox_lay_d_min_20 =  QHBoxLayout()
        label_d_min_20 = QLabel("            d_min")
        label_d_min_20.setPalette(palette_object)
        label_d_min_20.setFont(QFont("Monospace"))
        hbox_lay_d_min_20.addWidget(label_d_min_20)

        box_d_min_20 = QDoubleSpinBox()
        box_d_min_20.local_path = "indexing.fft3d.reciprocal_space_grid.d_min"
        box_d_min_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_20.addWidget(box_d_min_20)
        bg_box.addLayout(hbox_lay_d_min_20)

        hbox_lay_sigma_phi_deg_21 =  QHBoxLayout()
        label_sigma_phi_deg_21 = QLabel("    sigma_phi_deg")
        label_sigma_phi_deg_21.setPalette(palette_object)
        label_sigma_phi_deg_21.setFont(QFont("Monospace"))
        hbox_lay_sigma_phi_deg_21.addWidget(label_sigma_phi_deg_21)

        box_sigma_phi_deg_21 = QDoubleSpinBox()
        box_sigma_phi_deg_21.local_path = "indexing.sigma_phi_deg"
        box_sigma_phi_deg_21.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_phi_deg_21.addWidget(box_sigma_phi_deg_21)
        bg_box.addLayout(hbox_lay_sigma_phi_deg_21)

        hbox_lay_b_iso_22 =  QHBoxLayout()
        label_b_iso_22 = QLabel("    b_iso")
        label_b_iso_22.setPalette(palette_object)
        label_b_iso_22.setFont(QFont("Monospace"))
        hbox_lay_b_iso_22.addWidget(label_b_iso_22)

        box_b_iso_22 = QDoubleSpinBox()
        box_b_iso_22.local_path = "indexing.b_iso"
        box_b_iso_22.valueChanged.connect(self.spnbox_changed)
        hbox_lay_b_iso_22.addWidget(box_b_iso_22)
        bg_box.addLayout(hbox_lay_b_iso_22)

        hbox_lay_rmsd_cutoff_23 =  QHBoxLayout()
        label_rmsd_cutoff_23 = QLabel("    rmsd_cutoff")
        label_rmsd_cutoff_23.setPalette(palette_object)
        label_rmsd_cutoff_23.setFont(QFont("Monospace"))
        hbox_lay_rmsd_cutoff_23.addWidget(label_rmsd_cutoff_23)

        box_rmsd_cutoff_23 = QDoubleSpinBox()
        box_rmsd_cutoff_23.local_path = "indexing.rmsd_cutoff"
        box_rmsd_cutoff_23.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_cutoff_23.addWidget(box_rmsd_cutoff_23)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_23)

        hbox_lay_scan_range_24_0 =  QHBoxLayout()
        label_scan_range_24_0 = QLabel("    scan_range[1]")
        label_scan_range_24_0.setPalette(palette_object)
        label_scan_range_24_0.setFont(QFont("Monospace"))
        hbox_lay_scan_range_24_0.addWidget(label_scan_range_24_0)
        box_scan_range_24_0 = QSpinBox()
        box_scan_range_24_0.local_path = "indexing.scan_range"
        #box_scan_range_24_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_24_1 =  QHBoxLayout()
        label_scan_range_24_1 = QLabel("    scan_range[2]")
        label_scan_range_24_1.setPalette(palette_object)
        label_scan_range_24_1.setFont(QFont("Monospace"))
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
        label_25.setFont(QFont("Monospace"))
        bg_box.addWidget(label_25)
        hbox_lay_relative_length_tolerance_28 =  QHBoxLayout()
        label_relative_length_tolerance_28 = QLabel("        relative_length_tolerance")
        label_relative_length_tolerance_28.setPalette(palette_object)
        label_relative_length_tolerance_28.setFont(QFont("Monospace"))
        hbox_lay_relative_length_tolerance_28.addWidget(label_relative_length_tolerance_28)

        box_relative_length_tolerance_28 = QDoubleSpinBox()
        box_relative_length_tolerance_28.local_path = "indexing.known_symmetry.relative_length_tolerance"
        box_relative_length_tolerance_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_relative_length_tolerance_28.addWidget(box_relative_length_tolerance_28)
        bg_box.addLayout(hbox_lay_relative_length_tolerance_28)

        hbox_lay_absolute_angle_tolerance_29 =  QHBoxLayout()
        label_absolute_angle_tolerance_29 = QLabel("        absolute_angle_tolerance")
        label_absolute_angle_tolerance_29.setPalette(palette_object)
        label_absolute_angle_tolerance_29.setFont(QFont("Monospace"))
        hbox_lay_absolute_angle_tolerance_29.addWidget(label_absolute_angle_tolerance_29)

        box_absolute_angle_tolerance_29 = QDoubleSpinBox()
        box_absolute_angle_tolerance_29.local_path = "indexing.known_symmetry.absolute_angle_tolerance"
        box_absolute_angle_tolerance_29.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_angle_tolerance_29.addWidget(box_absolute_angle_tolerance_29)
        bg_box.addLayout(hbox_lay_absolute_angle_tolerance_29)

        hbox_lay_max_delta_30 =  QHBoxLayout()
        label_max_delta_30 = QLabel("        max_delta")
        label_max_delta_30.setPalette(palette_object)
        label_max_delta_30.setFont(QFont("Monospace"))
        hbox_lay_max_delta_30.addWidget(label_max_delta_30)

        box_max_delta_30 = QDoubleSpinBox()
        box_max_delta_30.local_path = "indexing.known_symmetry.max_delta"
        box_max_delta_30.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_delta_30.addWidget(box_max_delta_30)
        bg_box.addLayout(hbox_lay_max_delta_30)

        label_31 = QLabel("    basis_vector_combinations")
        label_31.setPalette(palette_scope)
        label_31.setFont(QFont("Monospace"))
        bg_box.addWidget(label_31)
        hbox_lay_max_try_32 =  QHBoxLayout()
        label_max_try_32 = QLabel("        max_try")
        label_max_try_32.setPalette(palette_object)
        label_max_try_32.setFont(QFont("Monospace"))
        hbox_lay_max_try_32.addWidget(label_max_try_32)

        box_max_try_32 = QSpinBox()
        box_max_try_32.local_path = "indexing.basis_vector_combinations.max_try"
        box_max_try_32.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_try_32.addWidget(box_max_try_32)
        bg_box.addLayout(hbox_lay_max_try_32)

        hbox_lay_sys_absent_threshold_33 =  QHBoxLayout()
        label_sys_absent_threshold_33 = QLabel("        sys_absent_threshold")
        label_sys_absent_threshold_33.setPalette(palette_object)
        label_sys_absent_threshold_33.setFont(QFont("Monospace"))
        hbox_lay_sys_absent_threshold_33.addWidget(label_sys_absent_threshold_33)

        box_sys_absent_threshold_33 = QDoubleSpinBox()
        box_sys_absent_threshold_33.local_path = "indexing.basis_vector_combinations.sys_absent_threshold"
        box_sys_absent_threshold_33.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sys_absent_threshold_33.addWidget(box_sys_absent_threshold_33)
        bg_box.addLayout(hbox_lay_sys_absent_threshold_33)

        hbox_lay_solution_scorer_34 =  QHBoxLayout()
        label_solution_scorer_34 = QLabel("        solution_scorer")
        label_solution_scorer_34.setPalette(palette_object)
        label_solution_scorer_34.setFont(QFont("Monospace"))
        hbox_lay_solution_scorer_34.addWidget(label_solution_scorer_34)

        box_solution_scorer_34 = QComboBox()
        box_solution_scorer_34.local_path = "indexing.basis_vector_combinations.solution_scorer"
        box_solution_scorer_34.tmp_lst=[]
        box_solution_scorer_34.tmp_lst.append("filter")
        box_solution_scorer_34.tmp_lst.append("*weighted")
        for lst_itm in box_solution_scorer_34.tmp_lst:
            box_solution_scorer_34.addItem(lst_itm)
        box_solution_scorer_34.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_solution_scorer_34.addWidget(box_solution_scorer_34)
        bg_box.addLayout(hbox_lay_solution_scorer_34)

        label_35 = QLabel("        filter")
        label_35.setPalette(palette_scope)
        label_35.setFont(QFont("Monospace"))
        bg_box.addWidget(label_35)
        hbox_lay_check_doubled_cell_36 =  QHBoxLayout()
        label_check_doubled_cell_36 = QLabel("            check_doubled_cell")
        label_check_doubled_cell_36.setPalette(palette_object)
        label_check_doubled_cell_36.setFont(QFont("Monospace"))
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
        label_likelihood_cutoff_37.setFont(QFont("Monospace"))
        hbox_lay_likelihood_cutoff_37.addWidget(label_likelihood_cutoff_37)

        box_likelihood_cutoff_37 = QDoubleSpinBox()
        box_likelihood_cutoff_37.local_path = "indexing.basis_vector_combinations.filter.likelihood_cutoff"
        box_likelihood_cutoff_37.valueChanged.connect(self.spnbox_changed)
        hbox_lay_likelihood_cutoff_37.addWidget(box_likelihood_cutoff_37)
        bg_box.addLayout(hbox_lay_likelihood_cutoff_37)

        hbox_lay_volume_cutoff_38 =  QHBoxLayout()
        label_volume_cutoff_38 = QLabel("            volume_cutoff")
        label_volume_cutoff_38.setPalette(palette_object)
        label_volume_cutoff_38.setFont(QFont("Monospace"))
        hbox_lay_volume_cutoff_38.addWidget(label_volume_cutoff_38)

        box_volume_cutoff_38 = QDoubleSpinBox()
        box_volume_cutoff_38.local_path = "indexing.basis_vector_combinations.filter.volume_cutoff"
        box_volume_cutoff_38.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_cutoff_38.addWidget(box_volume_cutoff_38)
        bg_box.addLayout(hbox_lay_volume_cutoff_38)

        hbox_lay_n_indexed_cutoff_39 =  QHBoxLayout()
        label_n_indexed_cutoff_39 = QLabel("            n_indexed_cutoff")
        label_n_indexed_cutoff_39.setPalette(palette_object)
        label_n_indexed_cutoff_39.setFont(QFont("Monospace"))
        hbox_lay_n_indexed_cutoff_39.addWidget(label_n_indexed_cutoff_39)

        box_n_indexed_cutoff_39 = QDoubleSpinBox()
        box_n_indexed_cutoff_39.local_path = "indexing.basis_vector_combinations.filter.n_indexed_cutoff"
        box_n_indexed_cutoff_39.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_cutoff_39.addWidget(box_n_indexed_cutoff_39)
        bg_box.addLayout(hbox_lay_n_indexed_cutoff_39)

        label_40 = QLabel("        weighted")
        label_40.setPalette(palette_scope)
        label_40.setFont(QFont("Monospace"))
        bg_box.addWidget(label_40)
        hbox_lay_power_41 =  QHBoxLayout()
        label_power_41 = QLabel("            power")
        label_power_41.setPalette(palette_object)
        label_power_41.setFont(QFont("Monospace"))
        hbox_lay_power_41.addWidget(label_power_41)

        box_power_41 = QSpinBox()
        box_power_41.local_path = "indexing.basis_vector_combinations.weighted.power"
        box_power_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_power_41.addWidget(box_power_41)
        bg_box.addLayout(hbox_lay_power_41)

        hbox_lay_volume_weight_42 =  QHBoxLayout()
        label_volume_weight_42 = QLabel("            volume_weight")
        label_volume_weight_42.setPalette(palette_object)
        label_volume_weight_42.setFont(QFont("Monospace"))
        hbox_lay_volume_weight_42.addWidget(label_volume_weight_42)

        box_volume_weight_42 = QDoubleSpinBox()
        box_volume_weight_42.local_path = "indexing.basis_vector_combinations.weighted.volume_weight"
        box_volume_weight_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_weight_42.addWidget(box_volume_weight_42)
        bg_box.addLayout(hbox_lay_volume_weight_42)

        hbox_lay_n_indexed_weight_43 =  QHBoxLayout()
        label_n_indexed_weight_43 = QLabel("            n_indexed_weight")
        label_n_indexed_weight_43.setPalette(palette_object)
        label_n_indexed_weight_43.setFont(QFont("Monospace"))
        hbox_lay_n_indexed_weight_43.addWidget(label_n_indexed_weight_43)

        box_n_indexed_weight_43 = QDoubleSpinBox()
        box_n_indexed_weight_43.local_path = "indexing.basis_vector_combinations.weighted.n_indexed_weight"
        box_n_indexed_weight_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_weight_43.addWidget(box_n_indexed_weight_43)
        bg_box.addLayout(hbox_lay_n_indexed_weight_43)

        hbox_lay_rmsd_weight_44 =  QHBoxLayout()
        label_rmsd_weight_44 = QLabel("            rmsd_weight")
        label_rmsd_weight_44.setPalette(palette_object)
        label_rmsd_weight_44.setFont(QFont("Monospace"))
        hbox_lay_rmsd_weight_44.addWidget(label_rmsd_weight_44)

        box_rmsd_weight_44 = QDoubleSpinBox()
        box_rmsd_weight_44.local_path = "indexing.basis_vector_combinations.weighted.rmsd_weight"
        box_rmsd_weight_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_weight_44.addWidget(box_rmsd_weight_44)
        bg_box.addLayout(hbox_lay_rmsd_weight_44)

        label_45 = QLabel("    index_assignment")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace"))
        bg_box.addWidget(label_45)
        hbox_lay_method_46 =  QHBoxLayout()
        label_method_46 = QLabel("        method")
        label_method_46.setPalette(palette_object)
        label_method_46.setFont(QFont("Monospace"))
        hbox_lay_method_46.addWidget(label_method_46)

        box_method_46 = QComboBox()
        box_method_46.local_path = "indexing.index_assignment.method"
        box_method_46.tmp_lst=[]
        box_method_46.tmp_lst.append("*simple")
        box_method_46.tmp_lst.append("local")
        for lst_itm in box_method_46.tmp_lst:
            box_method_46.addItem(lst_itm)
        box_method_46.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_46.addWidget(box_method_46)
        bg_box.addLayout(hbox_lay_method_46)

        label_47 = QLabel("        simple")
        label_47.setPalette(palette_scope)
        label_47.setFont(QFont("Monospace"))
        bg_box.addWidget(label_47)
        hbox_lay_hkl_tolerance_48 =  QHBoxLayout()
        label_hkl_tolerance_48 = QLabel("            hkl_tolerance")
        label_hkl_tolerance_48.setPalette(palette_object)
        label_hkl_tolerance_48.setFont(QFont("Monospace"))
        hbox_lay_hkl_tolerance_48.addWidget(label_hkl_tolerance_48)

        box_hkl_tolerance_48 = QDoubleSpinBox()
        box_hkl_tolerance_48.local_path = "indexing.index_assignment.simple.hkl_tolerance"
        box_hkl_tolerance_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hkl_tolerance_48.addWidget(box_hkl_tolerance_48)
        bg_box.addLayout(hbox_lay_hkl_tolerance_48)

        label_49 = QLabel("        local")
        label_49.setPalette(palette_scope)
        label_49.setFont(QFont("Monospace"))
        bg_box.addWidget(label_49)
        hbox_lay_epsilon_50 =  QHBoxLayout()
        label_epsilon_50 = QLabel("            epsilon")
        label_epsilon_50.setPalette(palette_object)
        label_epsilon_50.setFont(QFont("Monospace"))
        hbox_lay_epsilon_50.addWidget(label_epsilon_50)

        box_epsilon_50 = QDoubleSpinBox()
        box_epsilon_50.local_path = "indexing.index_assignment.local.epsilon"
        box_epsilon_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_epsilon_50.addWidget(box_epsilon_50)
        bg_box.addLayout(hbox_lay_epsilon_50)

        hbox_lay_delta_51 =  QHBoxLayout()
        label_delta_51 = QLabel("            delta")
        label_delta_51.setPalette(palette_object)
        label_delta_51.setFont(QFont("Monospace"))
        hbox_lay_delta_51.addWidget(label_delta_51)

        box_delta_51 = QSpinBox()
        box_delta_51.local_path = "indexing.index_assignment.local.delta"
        box_delta_51.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delta_51.addWidget(box_delta_51)
        bg_box.addLayout(hbox_lay_delta_51)

        hbox_lay_l_min_52 =  QHBoxLayout()
        label_l_min_52 = QLabel("            l_min")
        label_l_min_52.setPalette(palette_object)
        label_l_min_52.setFont(QFont("Monospace"))
        hbox_lay_l_min_52.addWidget(label_l_min_52)

        box_l_min_52 = QDoubleSpinBox()
        box_l_min_52.local_path = "indexing.index_assignment.local.l_min"
        box_l_min_52.valueChanged.connect(self.spnbox_changed)
        hbox_lay_l_min_52.addWidget(box_l_min_52)
        bg_box.addLayout(hbox_lay_l_min_52)

        hbox_lay_nearest_neighbours_53 =  QHBoxLayout()
        label_nearest_neighbours_53 = QLabel("            nearest_neighbours")
        label_nearest_neighbours_53.setPalette(palette_object)
        label_nearest_neighbours_53.setFont(QFont("Monospace"))
        hbox_lay_nearest_neighbours_53.addWidget(label_nearest_neighbours_53)

        box_nearest_neighbours_53 = QSpinBox()
        box_nearest_neighbours_53.local_path = "indexing.index_assignment.local.nearest_neighbours"
        box_nearest_neighbours_53.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbours_53.addWidget(box_nearest_neighbours_53)
        bg_box.addLayout(hbox_lay_nearest_neighbours_53)

        hbox_lay_optimise_initial_basis_vectors_54 =  QHBoxLayout()
        label_optimise_initial_basis_vectors_54 = QLabel("    optimise_initial_basis_vectors")
        label_optimise_initial_basis_vectors_54.setPalette(palette_object)
        label_optimise_initial_basis_vectors_54.setFont(QFont("Monospace"))
        hbox_lay_optimise_initial_basis_vectors_54.addWidget(label_optimise_initial_basis_vectors_54)

        box_optimise_initial_basis_vectors_54 = QComboBox()
        box_optimise_initial_basis_vectors_54.local_path = "indexing.optimise_initial_basis_vectors"
        box_optimise_initial_basis_vectors_54.tmp_lst=[]
        box_optimise_initial_basis_vectors_54.tmp_lst.append("True")
        box_optimise_initial_basis_vectors_54.tmp_lst.append("False")
        for lst_itm in box_optimise_initial_basis_vectors_54.tmp_lst:
            box_optimise_initial_basis_vectors_54.addItem(lst_itm)
        box_optimise_initial_basis_vectors_54.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_optimise_initial_basis_vectors_54.addWidget(box_optimise_initial_basis_vectors_54)
        bg_box.addLayout(hbox_lay_optimise_initial_basis_vectors_54)

        hbox_lay_debug_55 =  QHBoxLayout()
        label_debug_55 = QLabel("    debug")
        label_debug_55.setPalette(palette_object)
        label_debug_55.setFont(QFont("Monospace"))
        hbox_lay_debug_55.addWidget(label_debug_55)

        box_debug_55 = QComboBox()
        box_debug_55.local_path = "indexing.debug"
        box_debug_55.tmp_lst=[]
        box_debug_55.tmp_lst.append("True")
        box_debug_55.tmp_lst.append("False")
        for lst_itm in box_debug_55.tmp_lst:
            box_debug_55.addItem(lst_itm)
        box_debug_55.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_55.addWidget(box_debug_55)
        bg_box.addLayout(hbox_lay_debug_55)

        hbox_lay_debug_plots_56 =  QHBoxLayout()
        label_debug_plots_56 = QLabel("    debug_plots")
        label_debug_plots_56.setPalette(palette_object)
        label_debug_plots_56.setFont(QFont("Monospace"))
        hbox_lay_debug_plots_56.addWidget(label_debug_plots_56)

        box_debug_plots_56 = QComboBox()
        box_debug_plots_56.local_path = "indexing.debug_plots"
        box_debug_plots_56.tmp_lst=[]
        box_debug_plots_56.tmp_lst.append("True")
        box_debug_plots_56.tmp_lst.append("False")
        for lst_itm in box_debug_plots_56.tmp_lst:
            box_debug_plots_56.addItem(lst_itm)
        box_debug_plots_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_plots_56.addWidget(box_debug_plots_56)
        bg_box.addLayout(hbox_lay_debug_plots_56)

        hbox_lay_combine_scans_57 =  QHBoxLayout()
        label_combine_scans_57 = QLabel("    combine_scans")
        label_combine_scans_57.setPalette(palette_object)
        label_combine_scans_57.setFont(QFont("Monospace"))
        hbox_lay_combine_scans_57.addWidget(label_combine_scans_57)

        box_combine_scans_57 = QComboBox()
        box_combine_scans_57.local_path = "indexing.combine_scans"
        box_combine_scans_57.tmp_lst=[]
        box_combine_scans_57.tmp_lst.append("True")
        box_combine_scans_57.tmp_lst.append("False")
        for lst_itm in box_combine_scans_57.tmp_lst:
            box_combine_scans_57.addItem(lst_itm)
        box_combine_scans_57.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_combine_scans_57.addWidget(box_combine_scans_57)
        bg_box.addLayout(hbox_lay_combine_scans_57)

        label_58 = QLabel("    refinement_protocol")
        label_58.setPalette(palette_scope)
        label_58.setFont(QFont("Monospace"))
        bg_box.addWidget(label_58)
        hbox_lay_n_macro_cycles_59 =  QHBoxLayout()
        label_n_macro_cycles_59 = QLabel("        n_macro_cycles")
        label_n_macro_cycles_59.setPalette(palette_object)
        label_n_macro_cycles_59.setFont(QFont("Monospace"))
        hbox_lay_n_macro_cycles_59.addWidget(label_n_macro_cycles_59)

        box_n_macro_cycles_59 = QSpinBox()
        box_n_macro_cycles_59.local_path = "indexing.refinement_protocol.n_macro_cycles"
        box_n_macro_cycles_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_macro_cycles_59.addWidget(box_n_macro_cycles_59)
        bg_box.addLayout(hbox_lay_n_macro_cycles_59)

        hbox_lay_d_min_step_60 =  QHBoxLayout()
        label_d_min_step_60 = QLabel("        d_min_step")
        label_d_min_step_60.setPalette(palette_object)
        label_d_min_step_60.setFont(QFont("Monospace"))
        hbox_lay_d_min_step_60.addWidget(label_d_min_step_60)

        box_d_min_step_60 = QDoubleSpinBox()
        box_d_min_step_60.local_path = "indexing.refinement_protocol.d_min_step"
        box_d_min_step_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_step_60.addWidget(box_d_min_step_60)
        bg_box.addLayout(hbox_lay_d_min_step_60)

        hbox_lay_d_min_start_61 =  QHBoxLayout()
        label_d_min_start_61 = QLabel("        d_min_start")
        label_d_min_start_61.setPalette(palette_object)
        label_d_min_start_61.setFont(QFont("Monospace"))
        hbox_lay_d_min_start_61.addWidget(label_d_min_start_61)

        box_d_min_start_61 = QDoubleSpinBox()
        box_d_min_start_61.local_path = "indexing.refinement_protocol.d_min_start"
        box_d_min_start_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_start_61.addWidget(box_d_min_start_61)
        bg_box.addLayout(hbox_lay_d_min_start_61)

        hbox_lay_d_min_final_62 =  QHBoxLayout()
        label_d_min_final_62 = QLabel("        d_min_final")
        label_d_min_final_62.setPalette(palette_object)
        label_d_min_final_62.setFont(QFont("Monospace"))
        hbox_lay_d_min_final_62.addWidget(label_d_min_final_62)

        box_d_min_final_62 = QDoubleSpinBox()
        box_d_min_final_62.local_path = "indexing.refinement_protocol.d_min_final"
        box_d_min_final_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_final_62.addWidget(box_d_min_final_62)
        bg_box.addLayout(hbox_lay_d_min_final_62)

        hbox_lay_verbosity_63 =  QHBoxLayout()
        label_verbosity_63 = QLabel("        verbosity")
        label_verbosity_63.setPalette(palette_object)
        label_verbosity_63.setFont(QFont("Monospace"))
        hbox_lay_verbosity_63.addWidget(label_verbosity_63)

        box_verbosity_63 = QSpinBox()
        box_verbosity_63.local_path = "indexing.refinement_protocol.verbosity"
        box_verbosity_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_63.addWidget(box_verbosity_63)
        bg_box.addLayout(hbox_lay_verbosity_63)

        hbox_lay_disable_unit_cell_volume_sanity_check_64 =  QHBoxLayout()
        label_disable_unit_cell_volume_sanity_check_64 = QLabel("        disable_unit_cell_volume_sanity_check")
        label_disable_unit_cell_volume_sanity_check_64.setPalette(palette_object)
        label_disable_unit_cell_volume_sanity_check_64.setFont(QFont("Monospace"))
        hbox_lay_disable_unit_cell_volume_sanity_check_64.addWidget(label_disable_unit_cell_volume_sanity_check_64)

        box_disable_unit_cell_volume_sanity_check_64 = QComboBox()
        box_disable_unit_cell_volume_sanity_check_64.local_path = "indexing.refinement_protocol.disable_unit_cell_volume_sanity_check"
        box_disable_unit_cell_volume_sanity_check_64.tmp_lst=[]
        box_disable_unit_cell_volume_sanity_check_64.tmp_lst.append("True")
        box_disable_unit_cell_volume_sanity_check_64.tmp_lst.append("False")
        for lst_itm in box_disable_unit_cell_volume_sanity_check_64.tmp_lst:
            box_disable_unit_cell_volume_sanity_check_64.addItem(lst_itm)
        box_disable_unit_cell_volume_sanity_check_64.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_disable_unit_cell_volume_sanity_check_64.addWidget(box_disable_unit_cell_volume_sanity_check_64)
        bg_box.addLayout(hbox_lay_disable_unit_cell_volume_sanity_check_64)

        hbox_lay_method_65 =  QHBoxLayout()
        label_method_65 = QLabel("    method")
        label_method_65.setPalette(palette_object)
        label_method_65.setFont(QFont("Monospace"))
        hbox_lay_method_65.addWidget(label_method_65)

        box_method_65 = QComboBox()
        box_method_65.local_path = "indexing.method"
        box_method_65.tmp_lst=[]
        box_method_65.tmp_lst.append("*fft3d")
        box_method_65.tmp_lst.append("fft1d")
        box_method_65.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_65.tmp_lst:
            box_method_65.addItem(lst_itm)
        box_method_65.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_65.addWidget(box_method_65)
        bg_box.addLayout(hbox_lay_method_65)

        label_66 = QLabel("    multiple_lattice_search")
        label_66.setPalette(palette_scope)
        label_66.setFont(QFont("Monospace"))
        bg_box.addWidget(label_66)
        hbox_lay_cluster_analysis_search_67 =  QHBoxLayout()
        label_cluster_analysis_search_67 = QLabel("        cluster_analysis_search")
        label_cluster_analysis_search_67.setPalette(palette_object)
        label_cluster_analysis_search_67.setFont(QFont("Monospace"))
        hbox_lay_cluster_analysis_search_67.addWidget(label_cluster_analysis_search_67)

        box_cluster_analysis_search_67 = QComboBox()
        box_cluster_analysis_search_67.local_path = "indexing.multiple_lattice_search.cluster_analysis_search"
        box_cluster_analysis_search_67.tmp_lst=[]
        box_cluster_analysis_search_67.tmp_lst.append("True")
        box_cluster_analysis_search_67.tmp_lst.append("False")
        for lst_itm in box_cluster_analysis_search_67.tmp_lst:
            box_cluster_analysis_search_67.addItem(lst_itm)
        box_cluster_analysis_search_67.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cluster_analysis_search_67.addWidget(box_cluster_analysis_search_67)
        bg_box.addLayout(hbox_lay_cluster_analysis_search_67)

        hbox_lay_recycle_unindexed_reflections_cutoff_68 =  QHBoxLayout()
        label_recycle_unindexed_reflections_cutoff_68 = QLabel("        recycle_unindexed_reflections_cutoff")
        label_recycle_unindexed_reflections_cutoff_68.setPalette(palette_object)
        label_recycle_unindexed_reflections_cutoff_68.setFont(QFont("Monospace"))
        hbox_lay_recycle_unindexed_reflections_cutoff_68.addWidget(label_recycle_unindexed_reflections_cutoff_68)

        box_recycle_unindexed_reflections_cutoff_68 = QDoubleSpinBox()
        box_recycle_unindexed_reflections_cutoff_68.local_path = "indexing.multiple_lattice_search.recycle_unindexed_reflections_cutoff"
        box_recycle_unindexed_reflections_cutoff_68.valueChanged.connect(self.spnbox_changed)
        hbox_lay_recycle_unindexed_reflections_cutoff_68.addWidget(box_recycle_unindexed_reflections_cutoff_68)
        bg_box.addLayout(hbox_lay_recycle_unindexed_reflections_cutoff_68)

        hbox_lay_minimum_angular_separation_69 =  QHBoxLayout()
        label_minimum_angular_separation_69 = QLabel("        minimum_angular_separation")
        label_minimum_angular_separation_69.setPalette(palette_object)
        label_minimum_angular_separation_69.setFont(QFont("Monospace"))
        hbox_lay_minimum_angular_separation_69.addWidget(label_minimum_angular_separation_69)

        box_minimum_angular_separation_69 = QDoubleSpinBox()
        box_minimum_angular_separation_69.local_path = "indexing.multiple_lattice_search.minimum_angular_separation"
        box_minimum_angular_separation_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_angular_separation_69.addWidget(box_minimum_angular_separation_69)
        bg_box.addLayout(hbox_lay_minimum_angular_separation_69)

        hbox_lay_max_lattices_70 =  QHBoxLayout()
        label_max_lattices_70 = QLabel("        max_lattices")
        label_max_lattices_70.setPalette(palette_object)
        label_max_lattices_70.setFont(QFont("Monospace"))
        hbox_lay_max_lattices_70.addWidget(label_max_lattices_70)

        box_max_lattices_70 = QSpinBox()
        box_max_lattices_70.local_path = "indexing.multiple_lattice_search.max_lattices"
        box_max_lattices_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_lattices_70.addWidget(box_max_lattices_70)
        bg_box.addLayout(hbox_lay_max_lattices_70)

        label_71 = QLabel("        cluster_analysis")
        label_71.setPalette(palette_scope)
        label_71.setFont(QFont("Monospace"))
        bg_box.addWidget(label_71)
        hbox_lay_method_72 =  QHBoxLayout()
        label_method_72 = QLabel("            method")
        label_method_72.setPalette(palette_object)
        label_method_72.setFont(QFont("Monospace"))
        hbox_lay_method_72.addWidget(label_method_72)

        box_method_72 = QComboBox()
        box_method_72.local_path = "indexing.multiple_lattice_search.cluster_analysis.method"
        box_method_72.tmp_lst=[]
        box_method_72.tmp_lst.append("*dbscan")
        box_method_72.tmp_lst.append("hcluster")
        for lst_itm in box_method_72.tmp_lst:
            box_method_72.addItem(lst_itm)
        box_method_72.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_72.addWidget(box_method_72)
        bg_box.addLayout(hbox_lay_method_72)

        label_73 = QLabel("            hcluster")
        label_73.setPalette(palette_scope)
        label_73.setFont(QFont("Monospace"))
        bg_box.addWidget(label_73)
        label_74 = QLabel("                linkage")
        label_74.setPalette(palette_scope)
        label_74.setFont(QFont("Monospace"))
        bg_box.addWidget(label_74)
        hbox_lay_method_75 =  QHBoxLayout()
        label_method_75 = QLabel("                    method")
        label_method_75.setPalette(palette_object)
        label_method_75.setFont(QFont("Monospace"))
        hbox_lay_method_75.addWidget(label_method_75)

        box_method_75 = QComboBox()
        box_method_75.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.method"
        box_method_75.tmp_lst=[]
        box_method_75.tmp_lst.append("*ward")
        for lst_itm in box_method_75.tmp_lst:
            box_method_75.addItem(lst_itm)
        box_method_75.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_75.addWidget(box_method_75)
        bg_box.addLayout(hbox_lay_method_75)

        hbox_lay_metric_76 =  QHBoxLayout()
        label_metric_76 = QLabel("                    metric")
        label_metric_76.setPalette(palette_object)
        label_metric_76.setFont(QFont("Monospace"))
        hbox_lay_metric_76.addWidget(label_metric_76)

        box_metric_76 = QComboBox()
        box_metric_76.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.metric"
        box_metric_76.tmp_lst=[]
        box_metric_76.tmp_lst.append("*euclidean")
        for lst_itm in box_metric_76.tmp_lst:
            box_metric_76.addItem(lst_itm)
        box_metric_76.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_metric_76.addWidget(box_metric_76)
        bg_box.addLayout(hbox_lay_metric_76)

        hbox_lay_cutoff_77 =  QHBoxLayout()
        label_cutoff_77 = QLabel("                cutoff")
        label_cutoff_77.setPalette(palette_object)
        label_cutoff_77.setFont(QFont("Monospace"))
        hbox_lay_cutoff_77.addWidget(label_cutoff_77)

        box_cutoff_77 = QDoubleSpinBox()
        box_cutoff_77.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff"
        box_cutoff_77.valueChanged.connect(self.spnbox_changed)
        hbox_lay_cutoff_77.addWidget(box_cutoff_77)
        bg_box.addLayout(hbox_lay_cutoff_77)

        hbox_lay_cutoff_criterion_78 =  QHBoxLayout()
        label_cutoff_criterion_78 = QLabel("                cutoff_criterion")
        label_cutoff_criterion_78.setPalette(palette_object)
        label_cutoff_criterion_78.setFont(QFont("Monospace"))
        hbox_lay_cutoff_criterion_78.addWidget(label_cutoff_criterion_78)

        box_cutoff_criterion_78 = QComboBox()
        box_cutoff_criterion_78.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff_criterion"
        box_cutoff_criterion_78.tmp_lst=[]
        box_cutoff_criterion_78.tmp_lst.append("*distance")
        box_cutoff_criterion_78.tmp_lst.append("inconsistent")
        for lst_itm in box_cutoff_criterion_78.tmp_lst:
            box_cutoff_criterion_78.addItem(lst_itm)
        box_cutoff_criterion_78.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cutoff_criterion_78.addWidget(box_cutoff_criterion_78)
        bg_box.addLayout(hbox_lay_cutoff_criterion_78)

        label_79 = QLabel("            dbscan")
        label_79.setPalette(palette_scope)
        label_79.setFont(QFont("Monospace"))
        bg_box.addWidget(label_79)
        hbox_lay_eps_80 =  QHBoxLayout()
        label_eps_80 = QLabel("                eps")
        label_eps_80.setPalette(palette_object)
        label_eps_80.setFont(QFont("Monospace"))
        hbox_lay_eps_80.addWidget(label_eps_80)

        box_eps_80 = QDoubleSpinBox()
        box_eps_80.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.eps"
        box_eps_80.valueChanged.connect(self.spnbox_changed)
        hbox_lay_eps_80.addWidget(box_eps_80)
        bg_box.addLayout(hbox_lay_eps_80)

        hbox_lay_min_samples_81 =  QHBoxLayout()
        label_min_samples_81 = QLabel("                min_samples")
        label_min_samples_81.setPalette(palette_object)
        label_min_samples_81.setFont(QFont("Monospace"))
        hbox_lay_min_samples_81.addWidget(label_min_samples_81)

        box_min_samples_81 = QSpinBox()
        box_min_samples_81.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.min_samples"
        box_min_samples_81.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_samples_81.addWidget(box_min_samples_81)
        bg_box.addLayout(hbox_lay_min_samples_81)

        hbox_lay_min_cluster_size_82 =  QHBoxLayout()
        label_min_cluster_size_82 = QLabel("            min_cluster_size")
        label_min_cluster_size_82.setPalette(palette_object)
        label_min_cluster_size_82.setFont(QFont("Monospace"))
        hbox_lay_min_cluster_size_82.addWidget(label_min_cluster_size_82)

        box_min_cluster_size_82 = QSpinBox()
        box_min_cluster_size_82.local_path = "indexing.multiple_lattice_search.cluster_analysis.min_cluster_size"
        box_min_cluster_size_82.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cluster_size_82.addWidget(box_min_cluster_size_82)
        bg_box.addLayout(hbox_lay_min_cluster_size_82)

        hbox_lay_intersection_union_ratio_cutoff_83 =  QHBoxLayout()
        label_intersection_union_ratio_cutoff_83 = QLabel("            intersection_union_ratio_cutoff")
        label_intersection_union_ratio_cutoff_83.setPalette(palette_object)
        label_intersection_union_ratio_cutoff_83.setFont(QFont("Monospace"))
        hbox_lay_intersection_union_ratio_cutoff_83.addWidget(label_intersection_union_ratio_cutoff_83)

        box_intersection_union_ratio_cutoff_83 = QDoubleSpinBox()
        box_intersection_union_ratio_cutoff_83.local_path = "indexing.multiple_lattice_search.cluster_analysis.intersection_union_ratio_cutoff"
        box_intersection_union_ratio_cutoff_83.valueChanged.connect(self.spnbox_changed)
        hbox_lay_intersection_union_ratio_cutoff_83.addWidget(box_intersection_union_ratio_cutoff_83)
        bg_box.addLayout(hbox_lay_intersection_union_ratio_cutoff_83)

        label_84 = QLabel("    real_space_grid_search")
        label_84.setPalette(palette_scope)
        label_84.setFont(QFont("Monospace"))
        bg_box.addWidget(label_84)
        hbox_lay_characteristic_grid_85 =  QHBoxLayout()
        label_characteristic_grid_85 = QLabel("        characteristic_grid")
        label_characteristic_grid_85.setPalette(palette_object)
        label_characteristic_grid_85.setFont(QFont("Monospace"))
        hbox_lay_characteristic_grid_85.addWidget(label_characteristic_grid_85)

        box_characteristic_grid_85 = QDoubleSpinBox()
        box_characteristic_grid_85.local_path = "indexing.real_space_grid_search.characteristic_grid"
        box_characteristic_grid_85.valueChanged.connect(self.spnbox_changed)
        hbox_lay_characteristic_grid_85.addWidget(box_characteristic_grid_85)
        bg_box.addLayout(hbox_lay_characteristic_grid_85)

        label_86 = QLabel("    stills")
        label_86.setPalette(palette_scope)
        label_86.setFont(QFont("Monospace"))
        bg_box.addWidget(label_86)
        hbox_lay_indexer_87 =  QHBoxLayout()
        label_indexer_87 = QLabel("        indexer")
        label_indexer_87.setPalette(palette_object)
        label_indexer_87.setFont(QFont("Monospace"))
        hbox_lay_indexer_87.addWidget(label_indexer_87)

        box_indexer_87 = QComboBox()
        box_indexer_87.local_path = "indexing.stills.indexer"
        box_indexer_87.tmp_lst=[]
        box_indexer_87.tmp_lst.append("*Auto")
        box_indexer_87.tmp_lst.append("stills")
        box_indexer_87.tmp_lst.append("sweeps")
        for lst_itm in box_indexer_87.tmp_lst:
            box_indexer_87.addItem(lst_itm)
        box_indexer_87.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_indexer_87.addWidget(box_indexer_87)
        bg_box.addLayout(hbox_lay_indexer_87)

        hbox_lay_ewald_proximity_resolution_cutoff_88 =  QHBoxLayout()
        label_ewald_proximity_resolution_cutoff_88 = QLabel("        ewald_proximity_resolution_cutoff")
        label_ewald_proximity_resolution_cutoff_88.setPalette(palette_object)
        label_ewald_proximity_resolution_cutoff_88.setFont(QFont("Monospace"))
        hbox_lay_ewald_proximity_resolution_cutoff_88.addWidget(label_ewald_proximity_resolution_cutoff_88)

        box_ewald_proximity_resolution_cutoff_88 = QDoubleSpinBox()
        box_ewald_proximity_resolution_cutoff_88.local_path = "indexing.stills.ewald_proximity_resolution_cutoff"
        box_ewald_proximity_resolution_cutoff_88.valueChanged.connect(self.spnbox_changed)
        hbox_lay_ewald_proximity_resolution_cutoff_88.addWidget(box_ewald_proximity_resolution_cutoff_88)
        bg_box.addLayout(hbox_lay_ewald_proximity_resolution_cutoff_88)

        label_89 = QLabel("refinement")
        label_89.setPalette(palette_scope)
        label_89.setFont(QFont("Monospace"))
        bg_box.addWidget(label_89)
        label_90 = QLabel("    mp")
        label_90.setPalette(palette_scope)
        label_90.setFont(QFont("Monospace"))
        bg_box.addWidget(label_90)
        hbox_lay_nproc_91 =  QHBoxLayout()
        label_nproc_91 = QLabel("        nproc")
        label_nproc_91.setPalette(palette_object)
        label_nproc_91.setFont(QFont("Monospace"))
        hbox_lay_nproc_91.addWidget(label_nproc_91)

        box_nproc_91 = QSpinBox()
        box_nproc_91.local_path = "refinement.mp.nproc"
        box_nproc_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_91.addWidget(box_nproc_91)
        bg_box.addLayout(hbox_lay_nproc_91)

        hbox_lay_verbosity_92 =  QHBoxLayout()
        label_verbosity_92 = QLabel("    verbosity")
        label_verbosity_92.setPalette(palette_object)
        label_verbosity_92.setFont(QFont("Monospace"))
        hbox_lay_verbosity_92.addWidget(label_verbosity_92)

        box_verbosity_92 = QSpinBox()
        box_verbosity_92.local_path = "refinement.verbosity"
        box_verbosity_92.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_92.addWidget(box_verbosity_92)
        bg_box.addLayout(hbox_lay_verbosity_92)

        label_93 = QLabel("    parameterisation")
        label_93.setPalette(palette_scope)
        label_93.setFont(QFont("Monospace"))
        bg_box.addWidget(label_93)
        label_94 = QLabel("        auto_reduction")
        label_94.setPalette(palette_scope)
        label_94.setFont(QFont("Monospace"))
        bg_box.addWidget(label_94)
        hbox_lay_min_nref_per_parameter_95 =  QHBoxLayout()
        label_min_nref_per_parameter_95 = QLabel("            min_nref_per_parameter")
        label_min_nref_per_parameter_95.setPalette(palette_object)
        label_min_nref_per_parameter_95.setFont(QFont("Monospace"))
        hbox_lay_min_nref_per_parameter_95.addWidget(label_min_nref_per_parameter_95)

        box_min_nref_per_parameter_95 = QSpinBox()
        box_min_nref_per_parameter_95.local_path = "refinement.parameterisation.auto_reduction.min_nref_per_parameter"
        box_min_nref_per_parameter_95.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_nref_per_parameter_95.addWidget(box_min_nref_per_parameter_95)
        bg_box.addLayout(hbox_lay_min_nref_per_parameter_95)

        hbox_lay_action_96 =  QHBoxLayout()
        label_action_96 = QLabel("            action")
        label_action_96.setPalette(palette_object)
        label_action_96.setFont(QFont("Monospace"))
        hbox_lay_action_96.addWidget(label_action_96)

        box_action_96 = QComboBox()
        box_action_96.local_path = "refinement.parameterisation.auto_reduction.action"
        box_action_96.tmp_lst=[]
        box_action_96.tmp_lst.append("*fail")
        box_action_96.tmp_lst.append("fix")
        box_action_96.tmp_lst.append("remove")
        for lst_itm in box_action_96.tmp_lst:
            box_action_96.addItem(lst_itm)
        box_action_96.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_action_96.addWidget(box_action_96)
        bg_box.addLayout(hbox_lay_action_96)

        label_97 = QLabel("        beam")
        label_97.setPalette(palette_scope)
        label_97.setFont(QFont("Monospace"))
        bg_box.addWidget(label_97)
        hbox_lay_fix_98 =  QHBoxLayout()
        label_fix_98 = QLabel("            fix")
        label_fix_98.setPalette(palette_object)
        label_fix_98.setFont(QFont("Monospace"))
        hbox_lay_fix_98.addWidget(label_fix_98)

        box_fix_98 = QComboBox()
        box_fix_98.local_path = "refinement.parameterisation.beam.fix"
        box_fix_98.tmp_lst=[]
        box_fix_98.tmp_lst.append("all")
        box_fix_98.tmp_lst.append("*in_spindle_plane")
        box_fix_98.tmp_lst.append("out_spindle_plane")
        box_fix_98.tmp_lst.append("*wavelength")
        for lst_itm in box_fix_98.tmp_lst:
            box_fix_98.addItem(lst_itm)
        box_fix_98.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_98.addWidget(box_fix_98)
        bg_box.addLayout(hbox_lay_fix_98)

        label_100 = QLabel("        crystal")
        label_100.setPalette(palette_scope)
        label_100.setFont(QFont("Monospace"))
        bg_box.addWidget(label_100)
        hbox_lay_fix_101 =  QHBoxLayout()
        label_fix_101 = QLabel("            fix")
        label_fix_101.setPalette(palette_object)
        label_fix_101.setFont(QFont("Monospace"))
        hbox_lay_fix_101.addWidget(label_fix_101)

        box_fix_101 = QComboBox()
        box_fix_101.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_101.tmp_lst=[]
        box_fix_101.tmp_lst.append("all")
        box_fix_101.tmp_lst.append("cell")
        box_fix_101.tmp_lst.append("orientation")
        for lst_itm in box_fix_101.tmp_lst:
            box_fix_101.addItem(lst_itm)
        box_fix_101.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_101.addWidget(box_fix_101)
        bg_box.addLayout(hbox_lay_fix_101)

        label_102 = QLabel("            unit_cell")
        label_102.setPalette(palette_scope)
        label_102.setFont(QFont("Monospace"))
        bg_box.addWidget(label_102)
        label_104 = QLabel("                restraints")
        label_104.setPalette(palette_scope)
        label_104.setFont(QFont("Monospace"))
        bg_box.addWidget(label_104)
        label_105 = QLabel("                    tie_to_target")
        label_105.setPalette(palette_scope)
        label_105.setFont(QFont("Monospace"))
        bg_box.addWidget(label_105)
        hbox_lay_values_106_0 =  QHBoxLayout()
        label_values_106_0 = QLabel("                        values[1]")
        label_values_106_0.setPalette(palette_object)
        label_values_106_0.setFont(QFont("Monospace"))
        hbox_lay_values_106_0.addWidget(label_values_106_0)
        box_values_106_0 = QDoubleSpinBox()
        box_values_106_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_106_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_106_1 =  QHBoxLayout()
        label_values_106_1 = QLabel("                        values[2]")
        label_values_106_1.setPalette(palette_object)
        label_values_106_1.setFont(QFont("Monospace"))
        hbox_lay_values_106_1.addWidget(label_values_106_1)
        box_values_106_1 = QDoubleSpinBox()
        box_values_106_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_106_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_106_2 =  QHBoxLayout()
        label_values_106_2 = QLabel("                        values[3]")
        label_values_106_2.setPalette(palette_object)
        label_values_106_2.setFont(QFont("Monospace"))
        hbox_lay_values_106_2.addWidget(label_values_106_2)
        box_values_106_2 = QDoubleSpinBox()
        box_values_106_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_106_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_106_3 =  QHBoxLayout()
        label_values_106_3 = QLabel("                        values[4]")
        label_values_106_3.setPalette(palette_object)
        label_values_106_3.setFont(QFont("Monospace"))
        hbox_lay_values_106_3.addWidget(label_values_106_3)
        box_values_106_3 = QDoubleSpinBox()
        box_values_106_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_106_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_106_4 =  QHBoxLayout()
        label_values_106_4 = QLabel("                        values[5]")
        label_values_106_4.setPalette(palette_object)
        label_values_106_4.setFont(QFont("Monospace"))
        hbox_lay_values_106_4.addWidget(label_values_106_4)
        box_values_106_4 = QDoubleSpinBox()
        box_values_106_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_106_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_106_5 =  QHBoxLayout()
        label_values_106_5 = QLabel("                        values[6]")
        label_values_106_5.setPalette(palette_object)
        label_values_106_5.setFont(QFont("Monospace"))
        hbox_lay_values_106_5.addWidget(label_values_106_5)
        box_values_106_5 = QDoubleSpinBox()
        box_values_106_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_106_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_107_0 =  QHBoxLayout()
        label_sigmas_107_0 = QLabel("                        sigmas[1]")
        label_sigmas_107_0.setPalette(palette_object)
        label_sigmas_107_0.setFont(QFont("Monospace"))
        hbox_lay_sigmas_107_0.addWidget(label_sigmas_107_0)
        box_sigmas_107_0 = QDoubleSpinBox()
        box_sigmas_107_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_107_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_107_1 =  QHBoxLayout()
        label_sigmas_107_1 = QLabel("                        sigmas[2]")
        label_sigmas_107_1.setPalette(palette_object)
        label_sigmas_107_1.setFont(QFont("Monospace"))
        hbox_lay_sigmas_107_1.addWidget(label_sigmas_107_1)
        box_sigmas_107_1 = QDoubleSpinBox()
        box_sigmas_107_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_107_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_107_2 =  QHBoxLayout()
        label_sigmas_107_2 = QLabel("                        sigmas[3]")
        label_sigmas_107_2.setPalette(palette_object)
        label_sigmas_107_2.setFont(QFont("Monospace"))
        hbox_lay_sigmas_107_2.addWidget(label_sigmas_107_2)
        box_sigmas_107_2 = QDoubleSpinBox()
        box_sigmas_107_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_107_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_107_3 =  QHBoxLayout()
        label_sigmas_107_3 = QLabel("                        sigmas[4]")
        label_sigmas_107_3.setPalette(palette_object)
        label_sigmas_107_3.setFont(QFont("Monospace"))
        hbox_lay_sigmas_107_3.addWidget(label_sigmas_107_3)
        box_sigmas_107_3 = QDoubleSpinBox()
        box_sigmas_107_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_107_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_107_4 =  QHBoxLayout()
        label_sigmas_107_4 = QLabel("                        sigmas[5]")
        label_sigmas_107_4.setPalette(palette_object)
        label_sigmas_107_4.setFont(QFont("Monospace"))
        hbox_lay_sigmas_107_4.addWidget(label_sigmas_107_4)
        box_sigmas_107_4 = QDoubleSpinBox()
        box_sigmas_107_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_107_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_107_5 =  QHBoxLayout()
        label_sigmas_107_5 = QLabel("                        sigmas[6]")
        label_sigmas_107_5.setPalette(palette_object)
        label_sigmas_107_5.setFont(QFont("Monospace"))
        hbox_lay_sigmas_107_5.addWidget(label_sigmas_107_5)
        box_sigmas_107_5 = QDoubleSpinBox()
        box_sigmas_107_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_107_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_apply_to_all_109 =  QHBoxLayout()
        label_apply_to_all_109 = QLabel("                        apply_to_all")
        label_apply_to_all_109.setPalette(palette_object)
        label_apply_to_all_109.setFont(QFont("Monospace"))
        hbox_lay_apply_to_all_109.addWidget(label_apply_to_all_109)

        box_apply_to_all_109 = QComboBox()
        box_apply_to_all_109.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.apply_to_all"
        box_apply_to_all_109.tmp_lst=[]
        box_apply_to_all_109.tmp_lst.append("True")
        box_apply_to_all_109.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_109.tmp_lst:
            box_apply_to_all_109.addItem(lst_itm)
        box_apply_to_all_109.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_109.addWidget(box_apply_to_all_109)
        bg_box.addLayout(hbox_lay_apply_to_all_109)

        label_110 = QLabel("                    tie_to_group")
        label_110.setPalette(palette_scope)
        label_110.setFont(QFont("Monospace"))
        bg_box.addWidget(label_110)
        hbox_lay_target_111 =  QHBoxLayout()
        label_target_111 = QLabel("                        target")
        label_target_111.setPalette(palette_object)
        label_target_111.setFont(QFont("Monospace"))
        hbox_lay_target_111.addWidget(label_target_111)

        box_target_111 = QComboBox()
        box_target_111.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_111.tmp_lst=[]
        box_target_111.tmp_lst.append("*mean")
        box_target_111.tmp_lst.append("median")
        for lst_itm in box_target_111.tmp_lst:
            box_target_111.addItem(lst_itm)
        box_target_111.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_111.addWidget(box_target_111)
        bg_box.addLayout(hbox_lay_target_111)

        hbox_lay_sigmas_112_0 =  QHBoxLayout()
        label_sigmas_112_0 = QLabel("                        sigmas[1]")
        label_sigmas_112_0.setPalette(palette_object)
        label_sigmas_112_0.setFont(QFont("Monospace"))
        hbox_lay_sigmas_112_0.addWidget(label_sigmas_112_0)
        box_sigmas_112_0 = QDoubleSpinBox()
        box_sigmas_112_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_112_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_112_1 =  QHBoxLayout()
        label_sigmas_112_1 = QLabel("                        sigmas[2]")
        label_sigmas_112_1.setPalette(palette_object)
        label_sigmas_112_1.setFont(QFont("Monospace"))
        hbox_lay_sigmas_112_1.addWidget(label_sigmas_112_1)
        box_sigmas_112_1 = QDoubleSpinBox()
        box_sigmas_112_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_112_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_112_2 =  QHBoxLayout()
        label_sigmas_112_2 = QLabel("                        sigmas[3]")
        label_sigmas_112_2.setPalette(palette_object)
        label_sigmas_112_2.setFont(QFont("Monospace"))
        hbox_lay_sigmas_112_2.addWidget(label_sigmas_112_2)
        box_sigmas_112_2 = QDoubleSpinBox()
        box_sigmas_112_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_112_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_112_3 =  QHBoxLayout()
        label_sigmas_112_3 = QLabel("                        sigmas[4]")
        label_sigmas_112_3.setPalette(palette_object)
        label_sigmas_112_3.setFont(QFont("Monospace"))
        hbox_lay_sigmas_112_3.addWidget(label_sigmas_112_3)
        box_sigmas_112_3 = QDoubleSpinBox()
        box_sigmas_112_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_112_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_112_4 =  QHBoxLayout()
        label_sigmas_112_4 = QLabel("                        sigmas[5]")
        label_sigmas_112_4.setPalette(palette_object)
        label_sigmas_112_4.setFont(QFont("Monospace"))
        hbox_lay_sigmas_112_4.addWidget(label_sigmas_112_4)
        box_sigmas_112_4 = QDoubleSpinBox()
        box_sigmas_112_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_112_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_112_5 =  QHBoxLayout()
        label_sigmas_112_5 = QLabel("                        sigmas[6]")
        label_sigmas_112_5.setPalette(palette_object)
        label_sigmas_112_5.setFont(QFont("Monospace"))
        hbox_lay_sigmas_112_5.addWidget(label_sigmas_112_5)
        box_sigmas_112_5 = QDoubleSpinBox()
        box_sigmas_112_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_112_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_112_0.addWidget(box_sigmas_112_0)
        bg_box.addLayout(hbox_lay_sigmas_112_0)

        hbox_lay_sigmas_112_1.addWidget(box_sigmas_112_1)
        bg_box.addLayout(hbox_lay_sigmas_112_1)

        hbox_lay_sigmas_112_2.addWidget(box_sigmas_112_2)
        bg_box.addLayout(hbox_lay_sigmas_112_2)

        hbox_lay_sigmas_112_3.addWidget(box_sigmas_112_3)
        bg_box.addLayout(hbox_lay_sigmas_112_3)

        hbox_lay_sigmas_112_4.addWidget(box_sigmas_112_4)
        bg_box.addLayout(hbox_lay_sigmas_112_4)

        hbox_lay_sigmas_112_5.addWidget(box_sigmas_112_5)
        bg_box.addLayout(hbox_lay_sigmas_112_5)

        hbox_lay_apply_to_all_114 =  QHBoxLayout()
        label_apply_to_all_114 = QLabel("                        apply_to_all")
        label_apply_to_all_114.setPalette(palette_object)
        label_apply_to_all_114.setFont(QFont("Monospace"))
        hbox_lay_apply_to_all_114.addWidget(label_apply_to_all_114)

        box_apply_to_all_114 = QComboBox()
        box_apply_to_all_114.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.apply_to_all"
        box_apply_to_all_114.tmp_lst=[]
        box_apply_to_all_114.tmp_lst.append("True")
        box_apply_to_all_114.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_114.tmp_lst:
            box_apply_to_all_114.addItem(lst_itm)
        box_apply_to_all_114.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_114.addWidget(box_apply_to_all_114)
        bg_box.addLayout(hbox_lay_apply_to_all_114)

        label_115 = QLabel("            orientation")
        label_115.setPalette(palette_scope)
        label_115.setFont(QFont("Monospace"))
        bg_box.addWidget(label_115)
        hbox_lay_scan_varying_117 =  QHBoxLayout()
        label_scan_varying_117 = QLabel("            scan_varying")
        label_scan_varying_117.setPalette(palette_object)
        label_scan_varying_117.setFont(QFont("Monospace"))
        hbox_lay_scan_varying_117.addWidget(label_scan_varying_117)

        box_scan_varying_117 = QComboBox()
        box_scan_varying_117.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_117.tmp_lst=[]
        box_scan_varying_117.tmp_lst.append("True")
        box_scan_varying_117.tmp_lst.append("False")
        for lst_itm in box_scan_varying_117.tmp_lst:
            box_scan_varying_117.addItem(lst_itm)
        box_scan_varying_117.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_117.addWidget(box_scan_varying_117)
        bg_box.addLayout(hbox_lay_scan_varying_117)

        hbox_lay_num_intervals_118 =  QHBoxLayout()
        label_num_intervals_118 = QLabel("            num_intervals")
        label_num_intervals_118.setPalette(palette_object)
        label_num_intervals_118.setFont(QFont("Monospace"))
        hbox_lay_num_intervals_118.addWidget(label_num_intervals_118)

        box_num_intervals_118 = QComboBox()
        box_num_intervals_118.local_path = "refinement.parameterisation.crystal.num_intervals"
        box_num_intervals_118.tmp_lst=[]
        box_num_intervals_118.tmp_lst.append("*fixed_width")
        box_num_intervals_118.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_118.tmp_lst:
            box_num_intervals_118.addItem(lst_itm)
        box_num_intervals_118.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_118.addWidget(box_num_intervals_118)
        bg_box.addLayout(hbox_lay_num_intervals_118)

        hbox_lay_interval_width_degrees_119 =  QHBoxLayout()
        label_interval_width_degrees_119 = QLabel("            interval_width_degrees")
        label_interval_width_degrees_119.setPalette(palette_object)
        label_interval_width_degrees_119.setFont(QFont("Monospace"))
        hbox_lay_interval_width_degrees_119.addWidget(label_interval_width_degrees_119)

        box_interval_width_degrees_119 = QDoubleSpinBox()
        box_interval_width_degrees_119.local_path = "refinement.parameterisation.crystal.interval_width_degrees"
        box_interval_width_degrees_119.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_119.addWidget(box_interval_width_degrees_119)
        bg_box.addLayout(hbox_lay_interval_width_degrees_119)

        hbox_lay_absolute_num_intervals_120 =  QHBoxLayout()
        label_absolute_num_intervals_120 = QLabel("            absolute_num_intervals")
        label_absolute_num_intervals_120.setPalette(palette_object)
        label_absolute_num_intervals_120.setFont(QFont("Monospace"))
        hbox_lay_absolute_num_intervals_120.addWidget(label_absolute_num_intervals_120)

        box_absolute_num_intervals_120 = QSpinBox()
        box_absolute_num_intervals_120.local_path = "refinement.parameterisation.crystal.absolute_num_intervals"
        box_absolute_num_intervals_120.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_120.addWidget(box_absolute_num_intervals_120)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_120)

        hbox_lay_UB_model_per_121 =  QHBoxLayout()
        label_UB_model_per_121 = QLabel("            UB_model_per")
        label_UB_model_per_121.setPalette(palette_object)
        label_UB_model_per_121.setFont(QFont("Monospace"))
        hbox_lay_UB_model_per_121.addWidget(label_UB_model_per_121)

        box_UB_model_per_121 = QComboBox()
        box_UB_model_per_121.local_path = "refinement.parameterisation.crystal.UB_model_per"
        box_UB_model_per_121.tmp_lst=[]
        box_UB_model_per_121.tmp_lst.append("reflection")
        box_UB_model_per_121.tmp_lst.append("image")
        box_UB_model_per_121.tmp_lst.append("*block")
        for lst_itm in box_UB_model_per_121.tmp_lst:
            box_UB_model_per_121.addItem(lst_itm)
        box_UB_model_per_121.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_UB_model_per_121.addWidget(box_UB_model_per_121)
        bg_box.addLayout(hbox_lay_UB_model_per_121)

        label_122 = QLabel("        detector")
        label_122.setPalette(palette_scope)
        label_122.setFont(QFont("Monospace"))
        bg_box.addWidget(label_122)
        hbox_lay_panels_123 =  QHBoxLayout()
        label_panels_123 = QLabel("            panels")
        label_panels_123.setPalette(palette_object)
        label_panels_123.setFont(QFont("Monospace"))
        hbox_lay_panels_123.addWidget(label_panels_123)

        box_panels_123 = QComboBox()
        box_panels_123.local_path = "refinement.parameterisation.detector.panels"
        box_panels_123.tmp_lst=[]
        box_panels_123.tmp_lst.append("*automatic")
        box_panels_123.tmp_lst.append("single")
        box_panels_123.tmp_lst.append("multiple")
        box_panels_123.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_123.tmp_lst:
            box_panels_123.addItem(lst_itm)
        box_panels_123.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_123.addWidget(box_panels_123)
        bg_box.addLayout(hbox_lay_panels_123)

        hbox_lay_hierarchy_level_124 =  QHBoxLayout()
        label_hierarchy_level_124 = QLabel("            hierarchy_level")
        label_hierarchy_level_124.setPalette(palette_object)
        label_hierarchy_level_124.setFont(QFont("Monospace"))
        hbox_lay_hierarchy_level_124.addWidget(label_hierarchy_level_124)

        box_hierarchy_level_124 = QSpinBox()
        box_hierarchy_level_124.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_124.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_124.addWidget(box_hierarchy_level_124)
        bg_box.addLayout(hbox_lay_hierarchy_level_124)

        hbox_lay_fix_125 =  QHBoxLayout()
        label_fix_125 = QLabel("            fix")
        label_fix_125.setPalette(palette_object)
        label_fix_125.setFont(QFont("Monospace"))
        hbox_lay_fix_125.addWidget(label_fix_125)

        box_fix_125 = QComboBox()
        box_fix_125.local_path = "refinement.parameterisation.detector.fix"
        box_fix_125.tmp_lst=[]
        box_fix_125.tmp_lst.append("all")
        box_fix_125.tmp_lst.append("position")
        box_fix_125.tmp_lst.append("orientation")
        for lst_itm in box_fix_125.tmp_lst:
            box_fix_125.addItem(lst_itm)
        box_fix_125.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_125.addWidget(box_fix_125)
        bg_box.addLayout(hbox_lay_fix_125)

        hbox_lay_sparse_127 =  QHBoxLayout()
        label_sparse_127 = QLabel("        sparse")
        label_sparse_127.setPalette(palette_object)
        label_sparse_127.setFont(QFont("Monospace"))
        hbox_lay_sparse_127.addWidget(label_sparse_127)

        box_sparse_127 = QComboBox()
        box_sparse_127.local_path = "refinement.parameterisation.sparse"
        box_sparse_127.tmp_lst=[]
        box_sparse_127.tmp_lst.append("True")
        box_sparse_127.tmp_lst.append("False")
        for lst_itm in box_sparse_127.tmp_lst:
            box_sparse_127.addItem(lst_itm)
        box_sparse_127.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_127.addWidget(box_sparse_127)
        bg_box.addLayout(hbox_lay_sparse_127)

        hbox_lay_treat_single_image_as_still_128 =  QHBoxLayout()
        label_treat_single_image_as_still_128 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_128.setPalette(palette_object)
        label_treat_single_image_as_still_128.setFont(QFont("Monospace"))
        hbox_lay_treat_single_image_as_still_128.addWidget(label_treat_single_image_as_still_128)

        box_treat_single_image_as_still_128 = QComboBox()
        box_treat_single_image_as_still_128.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_128.tmp_lst=[]
        box_treat_single_image_as_still_128.tmp_lst.append("True")
        box_treat_single_image_as_still_128.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_128.tmp_lst:
            box_treat_single_image_as_still_128.addItem(lst_itm)
        box_treat_single_image_as_still_128.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_128.addWidget(box_treat_single_image_as_still_128)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_128)

        label_129 = QLabel("    refinery")
        label_129.setPalette(palette_scope)
        label_129.setFont(QFont("Monospace"))
        bg_box.addWidget(label_129)
        hbox_lay_engine_130 =  QHBoxLayout()
        label_engine_130 = QLabel("        engine")
        label_engine_130.setPalette(palette_object)
        label_engine_130.setFont(QFont("Monospace"))
        hbox_lay_engine_130.addWidget(label_engine_130)

        box_engine_130 = QComboBox()
        box_engine_130.local_path = "refinement.refinery.engine"
        box_engine_130.tmp_lst=[]
        box_engine_130.tmp_lst.append("SimpleLBFGS")
        box_engine_130.tmp_lst.append("LBFGScurvs")
        box_engine_130.tmp_lst.append("GaussNewton")
        box_engine_130.tmp_lst.append("*LevMar")
        box_engine_130.tmp_lst.append("SparseLevMar")
        for lst_itm in box_engine_130.tmp_lst:
            box_engine_130.addItem(lst_itm)
        box_engine_130.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_130.addWidget(box_engine_130)
        bg_box.addLayout(hbox_lay_engine_130)

        hbox_lay_track_step_131 =  QHBoxLayout()
        label_track_step_131 = QLabel("        track_step")
        label_track_step_131.setPalette(palette_object)
        label_track_step_131.setFont(QFont("Monospace"))
        hbox_lay_track_step_131.addWidget(label_track_step_131)

        box_track_step_131 = QComboBox()
        box_track_step_131.local_path = "refinement.refinery.track_step"
        box_track_step_131.tmp_lst=[]
        box_track_step_131.tmp_lst.append("True")
        box_track_step_131.tmp_lst.append("False")
        for lst_itm in box_track_step_131.tmp_lst:
            box_track_step_131.addItem(lst_itm)
        box_track_step_131.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_131.addWidget(box_track_step_131)
        bg_box.addLayout(hbox_lay_track_step_131)

        hbox_lay_track_gradient_132 =  QHBoxLayout()
        label_track_gradient_132 = QLabel("        track_gradient")
        label_track_gradient_132.setPalette(palette_object)
        label_track_gradient_132.setFont(QFont("Monospace"))
        hbox_lay_track_gradient_132.addWidget(label_track_gradient_132)

        box_track_gradient_132 = QComboBox()
        box_track_gradient_132.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_132.tmp_lst=[]
        box_track_gradient_132.tmp_lst.append("True")
        box_track_gradient_132.tmp_lst.append("False")
        for lst_itm in box_track_gradient_132.tmp_lst:
            box_track_gradient_132.addItem(lst_itm)
        box_track_gradient_132.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_132.addWidget(box_track_gradient_132)
        bg_box.addLayout(hbox_lay_track_gradient_132)

        hbox_lay_track_parameter_correlation_133 =  QHBoxLayout()
        label_track_parameter_correlation_133 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_133.setPalette(palette_object)
        label_track_parameter_correlation_133.setFont(QFont("Monospace"))
        hbox_lay_track_parameter_correlation_133.addWidget(label_track_parameter_correlation_133)

        box_track_parameter_correlation_133 = QComboBox()
        box_track_parameter_correlation_133.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_133.tmp_lst=[]
        box_track_parameter_correlation_133.tmp_lst.append("True")
        box_track_parameter_correlation_133.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_133.tmp_lst:
            box_track_parameter_correlation_133.addItem(lst_itm)
        box_track_parameter_correlation_133.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_133.addWidget(box_track_parameter_correlation_133)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_133)

        hbox_lay_track_out_of_sample_rmsd_134 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_134 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_134.setPalette(palette_object)
        label_track_out_of_sample_rmsd_134.setFont(QFont("Monospace"))
        hbox_lay_track_out_of_sample_rmsd_134.addWidget(label_track_out_of_sample_rmsd_134)

        box_track_out_of_sample_rmsd_134 = QComboBox()
        box_track_out_of_sample_rmsd_134.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_134.tmp_lst=[]
        box_track_out_of_sample_rmsd_134.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_134.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_134.tmp_lst:
            box_track_out_of_sample_rmsd_134.addItem(lst_itm)
        box_track_out_of_sample_rmsd_134.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_134.addWidget(box_track_out_of_sample_rmsd_134)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_134)

        hbox_lay_max_iterations_136 =  QHBoxLayout()
        label_max_iterations_136 = QLabel("        max_iterations")
        label_max_iterations_136.setPalette(palette_object)
        label_max_iterations_136.setFont(QFont("Monospace"))
        hbox_lay_max_iterations_136.addWidget(label_max_iterations_136)

        box_max_iterations_136 = QSpinBox()
        box_max_iterations_136.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_136.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_136.addWidget(box_max_iterations_136)
        bg_box.addLayout(hbox_lay_max_iterations_136)

        label_137 = QLabel("    target")
        label_137.setPalette(palette_scope)
        label_137.setFont(QFont("Monospace"))
        bg_box.addWidget(label_137)
        hbox_lay_rmsd_cutoff_138 =  QHBoxLayout()
        label_rmsd_cutoff_138 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_138.setPalette(palette_object)
        label_rmsd_cutoff_138.setFont(QFont("Monospace"))
        hbox_lay_rmsd_cutoff_138.addWidget(label_rmsd_cutoff_138)

        box_rmsd_cutoff_138 = QComboBox()
        box_rmsd_cutoff_138.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_138.tmp_lst=[]
        box_rmsd_cutoff_138.tmp_lst.append("*fraction_of_bin_size")
        box_rmsd_cutoff_138.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_138.tmp_lst:
            box_rmsd_cutoff_138.addItem(lst_itm)
        box_rmsd_cutoff_138.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_138.addWidget(box_rmsd_cutoff_138)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_138)

        hbox_lay_bin_size_fraction_139 =  QHBoxLayout()
        label_bin_size_fraction_139 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_139.setPalette(palette_object)
        label_bin_size_fraction_139.setFont(QFont("Monospace"))
        hbox_lay_bin_size_fraction_139.addWidget(label_bin_size_fraction_139)

        box_bin_size_fraction_139 = QDoubleSpinBox()
        box_bin_size_fraction_139.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_139.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_139.addWidget(box_bin_size_fraction_139)
        bg_box.addLayout(hbox_lay_bin_size_fraction_139)

        hbox_lay_absolute_cutoffs_140_0 =  QHBoxLayout()
        label_absolute_cutoffs_140_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_140_0.setPalette(palette_object)
        label_absolute_cutoffs_140_0.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_140_0.addWidget(label_absolute_cutoffs_140_0)
        box_absolute_cutoffs_140_0 = QDoubleSpinBox()
        box_absolute_cutoffs_140_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_140_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_140_1 =  QHBoxLayout()
        label_absolute_cutoffs_140_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_140_1.setPalette(palette_object)
        label_absolute_cutoffs_140_1.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_140_1.addWidget(label_absolute_cutoffs_140_1)
        box_absolute_cutoffs_140_1 = QDoubleSpinBox()
        box_absolute_cutoffs_140_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_140_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_140_2 =  QHBoxLayout()
        label_absolute_cutoffs_140_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_140_2.setPalette(palette_object)
        label_absolute_cutoffs_140_2.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_140_2.addWidget(label_absolute_cutoffs_140_2)
        box_absolute_cutoffs_140_2 = QDoubleSpinBox()
        box_absolute_cutoffs_140_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_140_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_140_0.addWidget(box_absolute_cutoffs_140_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_140_0)

        hbox_lay_absolute_cutoffs_140_1.addWidget(box_absolute_cutoffs_140_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_140_1)

        hbox_lay_absolute_cutoffs_140_2.addWidget(box_absolute_cutoffs_140_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_140_2)

        hbox_lay_gradient_calculation_blocksize_141 =  QHBoxLayout()
        label_gradient_calculation_blocksize_141 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_141.setPalette(palette_object)
        label_gradient_calculation_blocksize_141.setFont(QFont("Monospace"))
        hbox_lay_gradient_calculation_blocksize_141.addWidget(label_gradient_calculation_blocksize_141)

        box_gradient_calculation_blocksize_141 = QSpinBox()
        box_gradient_calculation_blocksize_141.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_141.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_141.addWidget(box_gradient_calculation_blocksize_141)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_141)

        label_142 = QLabel("    reflections")
        label_142.setPalette(palette_scope)
        label_142.setFont(QFont("Monospace"))
        bg_box.addWidget(label_142)
        hbox_lay_reflections_per_degree_143 =  QHBoxLayout()
        label_reflections_per_degree_143 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_143.setPalette(palette_object)
        label_reflections_per_degree_143.setFont(QFont("Monospace"))
        hbox_lay_reflections_per_degree_143.addWidget(label_reflections_per_degree_143)

        box_reflections_per_degree_143 = QDoubleSpinBox()
        box_reflections_per_degree_143.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_143.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_143.addWidget(box_reflections_per_degree_143)
        bg_box.addLayout(hbox_lay_reflections_per_degree_143)

        hbox_lay_minimum_sample_size_144 =  QHBoxLayout()
        label_minimum_sample_size_144 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_144.setPalette(palette_object)
        label_minimum_sample_size_144.setFont(QFont("Monospace"))
        hbox_lay_minimum_sample_size_144.addWidget(label_minimum_sample_size_144)

        box_minimum_sample_size_144 = QSpinBox()
        box_minimum_sample_size_144.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_144.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_144.addWidget(box_minimum_sample_size_144)
        bg_box.addLayout(hbox_lay_minimum_sample_size_144)

        hbox_lay_maximum_sample_size_145 =  QHBoxLayout()
        label_maximum_sample_size_145 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_145.setPalette(palette_object)
        label_maximum_sample_size_145.setFont(QFont("Monospace"))
        hbox_lay_maximum_sample_size_145.addWidget(label_maximum_sample_size_145)

        box_maximum_sample_size_145 = QSpinBox()
        box_maximum_sample_size_145.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_145.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_145.addWidget(box_maximum_sample_size_145)
        bg_box.addLayout(hbox_lay_maximum_sample_size_145)

        hbox_lay_random_seed_146 =  QHBoxLayout()
        label_random_seed_146 = QLabel("        random_seed")
        label_random_seed_146.setPalette(palette_object)
        label_random_seed_146.setFont(QFont("Monospace"))
        hbox_lay_random_seed_146.addWidget(label_random_seed_146)

        box_random_seed_146 = QSpinBox()
        box_random_seed_146.local_path = "refinement.reflections.random_seed"
        box_random_seed_146.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_146.addWidget(box_random_seed_146)
        bg_box.addLayout(hbox_lay_random_seed_146)

        hbox_lay_close_to_spindle_cutoff_147 =  QHBoxLayout()
        label_close_to_spindle_cutoff_147 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_147.setPalette(palette_object)
        label_close_to_spindle_cutoff_147.setFont(QFont("Monospace"))
        hbox_lay_close_to_spindle_cutoff_147.addWidget(label_close_to_spindle_cutoff_147)

        box_close_to_spindle_cutoff_147 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_147.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_147.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_147.addWidget(box_close_to_spindle_cutoff_147)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_147)

        hbox_lay_block_width_148 =  QHBoxLayout()
        label_block_width_148 = QLabel("        block_width")
        label_block_width_148.setPalette(palette_object)
        label_block_width_148.setFont(QFont("Monospace"))
        hbox_lay_block_width_148.addWidget(label_block_width_148)

        box_block_width_148 = QDoubleSpinBox()
        box_block_width_148.local_path = "refinement.reflections.block_width"
        box_block_width_148.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_148.addWidget(box_block_width_148)
        bg_box.addLayout(hbox_lay_block_width_148)

        label_149 = QLabel("        weighting_strategy")
        label_149.setPalette(palette_scope)
        label_149.setFont(QFont("Monospace"))
        bg_box.addWidget(label_149)
        hbox_lay_override_150 =  QHBoxLayout()
        label_override_150 = QLabel("            override")
        label_override_150.setPalette(palette_object)
        label_override_150.setFont(QFont("Monospace"))
        hbox_lay_override_150.addWidget(label_override_150)

        box_override_150 = QComboBox()
        box_override_150.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_150.tmp_lst=[]
        box_override_150.tmp_lst.append("statistical")
        box_override_150.tmp_lst.append("stills")
        box_override_150.tmp_lst.append("constant")
        for lst_itm in box_override_150.tmp_lst:
            box_override_150.addItem(lst_itm)
        box_override_150.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_150.addWidget(box_override_150)
        bg_box.addLayout(hbox_lay_override_150)

        hbox_lay_delpsi_constant_151 =  QHBoxLayout()
        label_delpsi_constant_151 = QLabel("            delpsi_constant")
        label_delpsi_constant_151.setPalette(palette_object)
        label_delpsi_constant_151.setFont(QFont("Monospace"))
        hbox_lay_delpsi_constant_151.addWidget(label_delpsi_constant_151)

        box_delpsi_constant_151 = QDoubleSpinBox()
        box_delpsi_constant_151.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_151.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_151.addWidget(box_delpsi_constant_151)
        bg_box.addLayout(hbox_lay_delpsi_constant_151)

        hbox_lay_constants_152_0 =  QHBoxLayout()
        label_constants_152_0 = QLabel("            constants[1]")
        label_constants_152_0.setPalette(palette_object)
        label_constants_152_0.setFont(QFont("Monospace"))
        hbox_lay_constants_152_0.addWidget(label_constants_152_0)
        box_constants_152_0 = QDoubleSpinBox()
        box_constants_152_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_152_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_152_1 =  QHBoxLayout()
        label_constants_152_1 = QLabel("            constants[2]")
        label_constants_152_1.setPalette(palette_object)
        label_constants_152_1.setFont(QFont("Monospace"))
        hbox_lay_constants_152_1.addWidget(label_constants_152_1)
        box_constants_152_1 = QDoubleSpinBox()
        box_constants_152_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_152_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_152_2 =  QHBoxLayout()
        label_constants_152_2 = QLabel("            constants[3]")
        label_constants_152_2.setPalette(palette_object)
        label_constants_152_2.setFont(QFont("Monospace"))
        hbox_lay_constants_152_2.addWidget(label_constants_152_2)
        box_constants_152_2 = QDoubleSpinBox()
        box_constants_152_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_152_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_152_0.addWidget(box_constants_152_0)
        bg_box.addLayout(hbox_lay_constants_152_0)

        hbox_lay_constants_152_1.addWidget(box_constants_152_1)
        bg_box.addLayout(hbox_lay_constants_152_1)

        hbox_lay_constants_152_2.addWidget(box_constants_152_2)
        bg_box.addLayout(hbox_lay_constants_152_2)

        label_153 = QLabel("        outlier")
        label_153.setPalette(palette_scope)
        label_153.setFont(QFont("Monospace"))
        bg_box.addWidget(label_153)
        hbox_lay_algorithm_154 =  QHBoxLayout()
        label_algorithm_154 = QLabel("            algorithm")
        label_algorithm_154.setPalette(palette_object)
        label_algorithm_154.setFont(QFont("Monospace"))
        hbox_lay_algorithm_154.addWidget(label_algorithm_154)

        box_algorithm_154 = QComboBox()
        box_algorithm_154.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_154.tmp_lst=[]
        box_algorithm_154.tmp_lst.append("null")
        box_algorithm_154.tmp_lst.append("*auto")
        box_algorithm_154.tmp_lst.append("mcd")
        box_algorithm_154.tmp_lst.append("tukey")
        box_algorithm_154.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_154.tmp_lst:
            box_algorithm_154.addItem(lst_itm)
        box_algorithm_154.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_154.addWidget(box_algorithm_154)
        bg_box.addLayout(hbox_lay_algorithm_154)

        hbox_lay_minimum_number_of_reflections_155 =  QHBoxLayout()
        label_minimum_number_of_reflections_155 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_155.setPalette(palette_object)
        label_minimum_number_of_reflections_155.setFont(QFont("Monospace"))
        hbox_lay_minimum_number_of_reflections_155.addWidget(label_minimum_number_of_reflections_155)

        box_minimum_number_of_reflections_155 = QSpinBox()
        box_minimum_number_of_reflections_155.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_155.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_155.addWidget(box_minimum_number_of_reflections_155)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_155)

        hbox_lay_separate_experiments_156 =  QHBoxLayout()
        label_separate_experiments_156 = QLabel("            separate_experiments")
        label_separate_experiments_156.setPalette(palette_object)
        label_separate_experiments_156.setFont(QFont("Monospace"))
        hbox_lay_separate_experiments_156.addWidget(label_separate_experiments_156)

        box_separate_experiments_156 = QComboBox()
        box_separate_experiments_156.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_156.tmp_lst=[]
        box_separate_experiments_156.tmp_lst.append("True")
        box_separate_experiments_156.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_156.tmp_lst:
            box_separate_experiments_156.addItem(lst_itm)
        box_separate_experiments_156.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_156.addWidget(box_separate_experiments_156)
        bg_box.addLayout(hbox_lay_separate_experiments_156)

        hbox_lay_separate_panels_157 =  QHBoxLayout()
        label_separate_panels_157 = QLabel("            separate_panels")
        label_separate_panels_157.setPalette(palette_object)
        label_separate_panels_157.setFont(QFont("Monospace"))
        hbox_lay_separate_panels_157.addWidget(label_separate_panels_157)

        box_separate_panels_157 = QComboBox()
        box_separate_panels_157.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_157.tmp_lst=[]
        box_separate_panels_157.tmp_lst.append("True")
        box_separate_panels_157.tmp_lst.append("False")
        for lst_itm in box_separate_panels_157.tmp_lst:
            box_separate_panels_157.addItem(lst_itm)
        box_separate_panels_157.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_157.addWidget(box_separate_panels_157)
        bg_box.addLayout(hbox_lay_separate_panels_157)

        label_158 = QLabel("            tukey")
        label_158.setPalette(palette_scope)
        label_158.setFont(QFont("Monospace"))
        bg_box.addWidget(label_158)
        hbox_lay_iqr_multiplier_159 =  QHBoxLayout()
        label_iqr_multiplier_159 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_159.setPalette(palette_object)
        label_iqr_multiplier_159.setFont(QFont("Monospace"))
        hbox_lay_iqr_multiplier_159.addWidget(label_iqr_multiplier_159)

        box_iqr_multiplier_159 = QDoubleSpinBox()
        box_iqr_multiplier_159.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_159.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_159.addWidget(box_iqr_multiplier_159)
        bg_box.addLayout(hbox_lay_iqr_multiplier_159)

        label_160 = QLabel("            mcd")
        label_160.setPalette(palette_scope)
        label_160.setFont(QFont("Monospace"))
        bg_box.addWidget(label_160)
        hbox_lay_alpha_161 =  QHBoxLayout()
        label_alpha_161 = QLabel("                alpha")
        label_alpha_161.setPalette(palette_object)
        label_alpha_161.setFont(QFont("Monospace"))
        hbox_lay_alpha_161.addWidget(label_alpha_161)

        box_alpha_161 = QDoubleSpinBox()
        box_alpha_161.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_161.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_161.addWidget(box_alpha_161)
        bg_box.addLayout(hbox_lay_alpha_161)

        hbox_lay_max_n_groups_162 =  QHBoxLayout()
        label_max_n_groups_162 = QLabel("                max_n_groups")
        label_max_n_groups_162.setPalette(palette_object)
        label_max_n_groups_162.setFont(QFont("Monospace"))
        hbox_lay_max_n_groups_162.addWidget(label_max_n_groups_162)

        box_max_n_groups_162 = QSpinBox()
        box_max_n_groups_162.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_162.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_162.addWidget(box_max_n_groups_162)
        bg_box.addLayout(hbox_lay_max_n_groups_162)

        hbox_lay_min_group_size_163 =  QHBoxLayout()
        label_min_group_size_163 = QLabel("                min_group_size")
        label_min_group_size_163.setPalette(palette_object)
        label_min_group_size_163.setFont(QFont("Monospace"))
        hbox_lay_min_group_size_163.addWidget(label_min_group_size_163)

        box_min_group_size_163 = QSpinBox()
        box_min_group_size_163.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_163.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_163.addWidget(box_min_group_size_163)
        bg_box.addLayout(hbox_lay_min_group_size_163)

        hbox_lay_n_trials_164 =  QHBoxLayout()
        label_n_trials_164 = QLabel("                n_trials")
        label_n_trials_164.setPalette(palette_object)
        label_n_trials_164.setFont(QFont("Monospace"))
        hbox_lay_n_trials_164.addWidget(label_n_trials_164)

        box_n_trials_164 = QSpinBox()
        box_n_trials_164.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_164.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_164.addWidget(box_n_trials_164)
        bg_box.addLayout(hbox_lay_n_trials_164)

        hbox_lay_k1_165 =  QHBoxLayout()
        label_k1_165 = QLabel("                k1")
        label_k1_165.setPalette(palette_object)
        label_k1_165.setFont(QFont("Monospace"))
        hbox_lay_k1_165.addWidget(label_k1_165)

        box_k1_165 = QSpinBox()
        box_k1_165.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_165.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_165.addWidget(box_k1_165)
        bg_box.addLayout(hbox_lay_k1_165)

        hbox_lay_k2_166 =  QHBoxLayout()
        label_k2_166 = QLabel("                k2")
        label_k2_166.setPalette(palette_object)
        label_k2_166.setFont(QFont("Monospace"))
        hbox_lay_k2_166.addWidget(label_k2_166)

        box_k2_166 = QSpinBox()
        box_k2_166.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_166.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_166.addWidget(box_k2_166)
        bg_box.addLayout(hbox_lay_k2_166)

        hbox_lay_k3_167 =  QHBoxLayout()
        label_k3_167 = QLabel("                k3")
        label_k3_167.setPalette(palette_object)
        label_k3_167.setFont(QFont("Monospace"))
        hbox_lay_k3_167.addWidget(label_k3_167)

        box_k3_167 = QSpinBox()
        box_k3_167.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_167.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_167.addWidget(box_k3_167)
        bg_box.addLayout(hbox_lay_k3_167)

        hbox_lay_threshold_probability_168 =  QHBoxLayout()
        label_threshold_probability_168 = QLabel("                threshold_probability")
        label_threshold_probability_168.setPalette(palette_object)
        label_threshold_probability_168.setFont(QFont("Monospace"))
        hbox_lay_threshold_probability_168.addWidget(label_threshold_probability_168)

        box_threshold_probability_168 = QDoubleSpinBox()
        box_threshold_probability_168.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_168.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_168.addWidget(box_threshold_probability_168)
        bg_box.addLayout(hbox_lay_threshold_probability_168)

        label_169 = QLabel("            sauter_poon")
        label_169.setPalette(palette_scope)
        label_169.setFont(QFont("Monospace"))
        bg_box.addWidget(label_169)
        hbox_lay_px_sz_170_0 =  QHBoxLayout()
        label_px_sz_170_0 = QLabel("                px_sz[1]")
        label_px_sz_170_0.setPalette(palette_object)
        label_px_sz_170_0.setFont(QFont("Monospace"))
        hbox_lay_px_sz_170_0.addWidget(label_px_sz_170_0)
        box_px_sz_170_0 = QDoubleSpinBox()
        box_px_sz_170_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_170_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_170_1 =  QHBoxLayout()
        label_px_sz_170_1 = QLabel("                px_sz[2]")
        label_px_sz_170_1.setPalette(palette_object)
        label_px_sz_170_1.setFont(QFont("Monospace"))
        hbox_lay_px_sz_170_1.addWidget(label_px_sz_170_1)
        box_px_sz_170_1 = QDoubleSpinBox()
        box_px_sz_170_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_170_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_170_0.addWidget(box_px_sz_170_0)
        bg_box.addLayout(hbox_lay_px_sz_170_0)

        hbox_lay_px_sz_170_1.addWidget(box_px_sz_170_1)
        bg_box.addLayout(hbox_lay_px_sz_170_1)

        hbox_lay_verbose_171 =  QHBoxLayout()
        label_verbose_171 = QLabel("                verbose")
        label_verbose_171.setPalette(palette_object)
        label_verbose_171.setFont(QFont("Monospace"))
        hbox_lay_verbose_171.addWidget(label_verbose_171)

        box_verbose_171 = QComboBox()
        box_verbose_171.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_171.tmp_lst=[]
        box_verbose_171.tmp_lst.append("True")
        box_verbose_171.tmp_lst.append("False")
        for lst_itm in box_verbose_171.tmp_lst:
            box_verbose_171.addItem(lst_itm)
        box_verbose_171.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_171.addWidget(box_verbose_171)
        bg_box.addLayout(hbox_lay_verbose_171)

        hbox_lay_pdf_172 =  QHBoxLayout()
        label_pdf_172 = QLabel("                pdf")
        label_pdf_172.setPalette(palette_object)
        label_pdf_172.setFont(QFont("Monospace"))
        hbox_lay_pdf_172.addWidget(label_pdf_172)

        box_pdf_172 = QLineEdit()
        box_pdf_172.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_172.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_172.addWidget(box_pdf_172)
        bg_box.addLayout(hbox_lay_pdf_172)

        label_173 = QLabel("output")
        label_173.setPalette(palette_scope)
        label_173.setFont(QFont("Monospace"))
        bg_box.addWidget(label_173)
        hbox_lay_log_177 =  QHBoxLayout()
        label_log_177 = QLabel("    log")
        label_log_177.setPalette(palette_object)
        label_log_177.setFont(QFont("Monospace"))
        hbox_lay_log_177.addWidget(label_log_177)

        box_log_177 = QLineEdit()
        box_log_177.local_path = "output.log"
        box_log_177.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_177.addWidget(box_log_177)
        bg_box.addLayout(hbox_lay_log_177)

        hbox_lay_debug_log_178 =  QHBoxLayout()
        label_debug_log_178 = QLabel("    debug_log")
        label_debug_log_178.setPalette(palette_object)
        label_debug_log_178.setFont(QFont("Monospace"))
        hbox_lay_debug_log_178.addWidget(label_debug_log_178)

        box_debug_log_178 = QLineEdit()
        box_debug_log_178.local_path = "output.debug_log"
        box_debug_log_178.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_178.addWidget(box_debug_log_178)
        bg_box.addLayout(hbox_lay_debug_log_178)

        hbox_lay_verbosity_179 =  QHBoxLayout()
        label_verbosity_179 = QLabel("verbosity")
        label_verbosity_179.setPalette(palette_object)
        label_verbosity_179.setFont(QFont("Monospace"))
        hbox_lay_verbosity_179.addWidget(label_verbosity_179)

        box_verbosity_179 = QSpinBox()
        box_verbosity_179.local_path = "verbosity"
        box_verbosity_179.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_179.addWidget(box_verbosity_179)
        bg_box.addLayout(hbox_lay_verbosity_179)

 
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
