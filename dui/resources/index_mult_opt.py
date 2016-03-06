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
        box_nproc_1.setValue(1)
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
        box_mm_search_scope_3.setValue(4.0)
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
        box_wide_search_binning_4.setValue(2.0)
        box_wide_search_binning_4.local_path = "indexing.wide_search_binning"
        box_wide_search_binning_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_wide_search_binning_4.addWidget(box_wide_search_binning_4)
        bg_box.addLayout(hbox_lay_wide_search_binning_4)


        hbox_lay_min_cell_5 =  QHBoxLayout()
        label_min_cell_5 = QLabel("    min_cell")
        label_min_cell_5.setPalette(palette_object)
        label_min_cell_5.setFont(QFont("Monospace"))
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
        label_max_cell_6.setFont(QFont("Monospace"))
        hbox_lay_max_cell_6.addWidget(label_max_cell_6)

        box_max_cell_6 = QDoubleSpinBox()
        box_max_cell_6.local_path = "indexing.max_cell"
        box_max_cell_6.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_cell_6.addWidget(box_max_cell_6)
        bg_box.addLayout(hbox_lay_max_cell_6)


        hbox_lay_max_cell_multiplier_7 =  QHBoxLayout()
        label_max_cell_multiplier_7 = QLabel("    max_cell_multiplier")
        label_max_cell_multiplier_7.setPalette(palette_object)
        label_max_cell_multiplier_7.setFont(QFont("Monospace"))
        hbox_lay_max_cell_multiplier_7.addWidget(label_max_cell_multiplier_7)

        box_max_cell_multiplier_7 = QDoubleSpinBox()
        box_max_cell_multiplier_7.setValue(1.3)
        box_max_cell_multiplier_7.local_path = "indexing.max_cell_multiplier"
        box_max_cell_multiplier_7.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_cell_multiplier_7.addWidget(box_max_cell_multiplier_7)
        bg_box.addLayout(hbox_lay_max_cell_multiplier_7)


        hbox_lay_max_cell_step_size_8 =  QHBoxLayout()
        label_max_cell_step_size_8 = QLabel("    max_cell_step_size")
        label_max_cell_step_size_8.setPalette(palette_object)
        label_max_cell_step_size_8.setFont(QFont("Monospace"))
        hbox_lay_max_cell_step_size_8.addWidget(label_max_cell_step_size_8)

        box_max_cell_step_size_8 = QDoubleSpinBox()
        box_max_cell_step_size_8.setValue(45.0)
        box_max_cell_step_size_8.local_path = "indexing.max_cell_step_size"
        box_max_cell_step_size_8.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_cell_step_size_8.addWidget(box_max_cell_step_size_8)
        bg_box.addLayout(hbox_lay_max_cell_step_size_8)


        hbox_lay_nearest_neighbor_percentile_9 =  QHBoxLayout()
        label_nearest_neighbor_percentile_9 = QLabel("    nearest_neighbor_percentile")
        label_nearest_neighbor_percentile_9.setPalette(palette_object)
        label_nearest_neighbor_percentile_9.setFont(QFont("Monospace"))
        hbox_lay_nearest_neighbor_percentile_9.addWidget(label_nearest_neighbor_percentile_9)

        box_nearest_neighbor_percentile_9 = QDoubleSpinBox()
        box_nearest_neighbor_percentile_9.setValue(0.05)
        box_nearest_neighbor_percentile_9.local_path = "indexing.nearest_neighbor_percentile"
        box_nearest_neighbor_percentile_9.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbor_percentile_9.addWidget(box_nearest_neighbor_percentile_9)
        bg_box.addLayout(hbox_lay_nearest_neighbor_percentile_9)


        hbox_lay_filter_ice_10 =  QHBoxLayout()
        label_filter_ice_10 = QLabel("    filter_ice")
        label_filter_ice_10.setPalette(palette_object)
        label_filter_ice_10.setFont(QFont("Monospace"))
        hbox_lay_filter_ice_10.addWidget(label_filter_ice_10)

        box_filter_ice_10 = QComboBox()
        box_filter_ice_10.local_path = "indexing.filter_ice"
        box_filter_ice_10.tmp_lst=[]
        box_filter_ice_10.tmp_lst.append("True")
        box_filter_ice_10.tmp_lst.append("False")
        for lst_itm in box_filter_ice_10.tmp_lst:
            box_filter_ice_10.addItem(lst_itm)
        box_filter_ice_10.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_filter_ice_10.addWidget(box_filter_ice_10)
        bg_box.addLayout(hbox_lay_filter_ice_10)


        label_11 = QLabel("    fft3d")
        label_11.setPalette(palette_scope)
        label_11.setFont(QFont("Monospace"))
        bg_box.addWidget(label_11)

        hbox_lay_peak_search_12 =  QHBoxLayout()
        label_peak_search_12 = QLabel("        peak_search")
        label_peak_search_12.setPalette(palette_object)
        label_peak_search_12.setFont(QFont("Monospace"))
        hbox_lay_peak_search_12.addWidget(label_peak_search_12)

        box_peak_search_12 = QComboBox()
        box_peak_search_12.local_path = "indexing.fft3d.peak_search"
        box_peak_search_12.tmp_lst=[]
        box_peak_search_12.tmp_lst.append("flood_fill")
        box_peak_search_12.tmp_lst.append("clean")
        for lst_itm in box_peak_search_12.tmp_lst:
            box_peak_search_12.addItem(lst_itm)
        box_peak_search_12.setCurrentIndex(0)
        box_peak_search_12.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_peak_search_12.addWidget(box_peak_search_12)
        bg_box.addLayout(hbox_lay_peak_search_12)


        hbox_lay_peak_volume_cutoff_13 =  QHBoxLayout()
        label_peak_volume_cutoff_13 = QLabel("        peak_volume_cutoff")
        label_peak_volume_cutoff_13.setPalette(palette_object)
        label_peak_volume_cutoff_13.setFont(QFont("Monospace"))
        hbox_lay_peak_volume_cutoff_13.addWidget(label_peak_volume_cutoff_13)

        box_peak_volume_cutoff_13 = QDoubleSpinBox()
        box_peak_volume_cutoff_13.setValue(0.15)
        box_peak_volume_cutoff_13.local_path = "indexing.fft3d.peak_volume_cutoff"
        box_peak_volume_cutoff_13.valueChanged.connect(self.spnbox_changed)
        hbox_lay_peak_volume_cutoff_13.addWidget(box_peak_volume_cutoff_13)
        bg_box.addLayout(hbox_lay_peak_volume_cutoff_13)


        label_14 = QLabel("        reciprocal_space_grid")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace"))
        bg_box.addWidget(label_14)

        hbox_lay_n_points_15 =  QHBoxLayout()
        label_n_points_15 = QLabel("            n_points")
        label_n_points_15.setPalette(palette_object)
        label_n_points_15.setFont(QFont("Monospace"))
        hbox_lay_n_points_15.addWidget(label_n_points_15)

        box_n_points_15 = QSpinBox()
        box_n_points_15.setValue(256)
        box_n_points_15.local_path = "indexing.fft3d.reciprocal_space_grid.n_points"
        box_n_points_15.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_points_15.addWidget(box_n_points_15)
        bg_box.addLayout(hbox_lay_n_points_15)


        hbox_lay_d_min_16 =  QHBoxLayout()
        label_d_min_16 = QLabel("            d_min")
        label_d_min_16.setPalette(palette_object)
        label_d_min_16.setFont(QFont("Monospace"))
        hbox_lay_d_min_16.addWidget(label_d_min_16)

        box_d_min_16 = QDoubleSpinBox()
        box_d_min_16.local_path = "indexing.fft3d.reciprocal_space_grid.d_min"
        box_d_min_16.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_16.addWidget(box_d_min_16)
        bg_box.addLayout(hbox_lay_d_min_16)


        hbox_lay_sigma_phi_deg_17 =  QHBoxLayout()
        label_sigma_phi_deg_17 = QLabel("    sigma_phi_deg")
        label_sigma_phi_deg_17.setPalette(palette_object)
        label_sigma_phi_deg_17.setFont(QFont("Monospace"))
        hbox_lay_sigma_phi_deg_17.addWidget(label_sigma_phi_deg_17)

        box_sigma_phi_deg_17 = QDoubleSpinBox()
        box_sigma_phi_deg_17.local_path = "indexing.sigma_phi_deg"
        box_sigma_phi_deg_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigma_phi_deg_17.addWidget(box_sigma_phi_deg_17)
        bg_box.addLayout(hbox_lay_sigma_phi_deg_17)


        hbox_lay_b_iso_18 =  QHBoxLayout()
        label_b_iso_18 = QLabel("    b_iso")
        label_b_iso_18.setPalette(palette_object)
        label_b_iso_18.setFont(QFont("Monospace"))
        hbox_lay_b_iso_18.addWidget(label_b_iso_18)

        box_b_iso_18 = QDoubleSpinBox()
        box_b_iso_18.local_path = "indexing.b_iso"
        box_b_iso_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_b_iso_18.addWidget(box_b_iso_18)
        bg_box.addLayout(hbox_lay_b_iso_18)


        hbox_lay_rmsd_cutoff_19 =  QHBoxLayout()
        label_rmsd_cutoff_19 = QLabel("    rmsd_cutoff")
        label_rmsd_cutoff_19.setPalette(palette_object)
        label_rmsd_cutoff_19.setFont(QFont("Monospace"))
        hbox_lay_rmsd_cutoff_19.addWidget(label_rmsd_cutoff_19)

        box_rmsd_cutoff_19 = QDoubleSpinBox()
        box_rmsd_cutoff_19.setValue(15.0)
        box_rmsd_cutoff_19.local_path = "indexing.rmsd_cutoff"
        box_rmsd_cutoff_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_cutoff_19.addWidget(box_rmsd_cutoff_19)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_19)


        hbox_lay_scan_range_20_0 =  QHBoxLayout()
        label_scan_range_20_0 = QLabel("    scan_range[1]")
        label_scan_range_20_0.setPalette(palette_object)
        label_scan_range_20_0.setFont(QFont("Monospace"))
        hbox_lay_scan_range_20_0.addWidget(label_scan_range_20_0)
        box_scan_range_20_0 = QSpinBox()
        box_scan_range_20_0.local_path = "indexing.scan_range"
        #box_scan_range_20_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_20_1 =  QHBoxLayout()
        label_scan_range_20_1 = QLabel("    scan_range[2]")
        label_scan_range_20_1.setPalette(palette_object)
        label_scan_range_20_1.setFont(QFont("Monospace"))
        hbox_lay_scan_range_20_1.addWidget(label_scan_range_20_1)
        box_scan_range_20_1 = QSpinBox()
        box_scan_range_20_1.local_path = "indexing.scan_range"
        #box_scan_range_20_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_20_0.addWidget(box_scan_range_20_0)
        bg_box.addLayout(hbox_lay_scan_range_20_0)

        hbox_lay_scan_range_20_1.addWidget(box_scan_range_20_1)
        bg_box.addLayout(hbox_lay_scan_range_20_1)


        label_21 = QLabel("    known_symmetry")
        label_21.setPalette(palette_scope)
        label_21.setFont(QFont("Monospace"))
        bg_box.addWidget(label_21)



        hbox_lay_relative_length_tolerance_24 =  QHBoxLayout()
        label_relative_length_tolerance_24 = QLabel("        relative_length_tolerance")
        label_relative_length_tolerance_24.setPalette(palette_object)
        label_relative_length_tolerance_24.setFont(QFont("Monospace"))
        hbox_lay_relative_length_tolerance_24.addWidget(label_relative_length_tolerance_24)

        box_relative_length_tolerance_24 = QDoubleSpinBox()
        box_relative_length_tolerance_24.setValue(0.1)
        box_relative_length_tolerance_24.local_path = "indexing.known_symmetry.relative_length_tolerance"
        box_relative_length_tolerance_24.valueChanged.connect(self.spnbox_changed)
        hbox_lay_relative_length_tolerance_24.addWidget(box_relative_length_tolerance_24)
        bg_box.addLayout(hbox_lay_relative_length_tolerance_24)


        hbox_lay_absolute_angle_tolerance_25 =  QHBoxLayout()
        label_absolute_angle_tolerance_25 = QLabel("        absolute_angle_tolerance")
        label_absolute_angle_tolerance_25.setPalette(palette_object)
        label_absolute_angle_tolerance_25.setFont(QFont("Monospace"))
        hbox_lay_absolute_angle_tolerance_25.addWidget(label_absolute_angle_tolerance_25)

        box_absolute_angle_tolerance_25 = QDoubleSpinBox()
        box_absolute_angle_tolerance_25.setValue(5.0)
        box_absolute_angle_tolerance_25.local_path = "indexing.known_symmetry.absolute_angle_tolerance"
        box_absolute_angle_tolerance_25.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_angle_tolerance_25.addWidget(box_absolute_angle_tolerance_25)
        bg_box.addLayout(hbox_lay_absolute_angle_tolerance_25)


        hbox_lay_max_delta_26 =  QHBoxLayout()
        label_max_delta_26 = QLabel("        max_delta")
        label_max_delta_26.setPalette(palette_object)
        label_max_delta_26.setFont(QFont("Monospace"))
        hbox_lay_max_delta_26.addWidget(label_max_delta_26)

        box_max_delta_26 = QDoubleSpinBox()
        box_max_delta_26.setValue(5.0)
        box_max_delta_26.local_path = "indexing.known_symmetry.max_delta"
        box_max_delta_26.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_delta_26.addWidget(box_max_delta_26)
        bg_box.addLayout(hbox_lay_max_delta_26)


        label_27 = QLabel("    basis_vector_combinations")
        label_27.setPalette(palette_scope)
        label_27.setFont(QFont("Monospace"))
        bg_box.addWidget(label_27)

        hbox_lay_max_try_28 =  QHBoxLayout()
        label_max_try_28 = QLabel("        max_try")
        label_max_try_28.setPalette(palette_object)
        label_max_try_28.setFont(QFont("Monospace"))
        hbox_lay_max_try_28.addWidget(label_max_try_28)

        box_max_try_28 = QSpinBox()
        box_max_try_28.setValue(50)
        box_max_try_28.local_path = "indexing.basis_vector_combinations.max_try"
        box_max_try_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_try_28.addWidget(box_max_try_28)
        bg_box.addLayout(hbox_lay_max_try_28)


        hbox_lay_sys_absent_threshold_29 =  QHBoxLayout()
        label_sys_absent_threshold_29 = QLabel("        sys_absent_threshold")
        label_sys_absent_threshold_29.setPalette(palette_object)
        label_sys_absent_threshold_29.setFont(QFont("Monospace"))
        hbox_lay_sys_absent_threshold_29.addWidget(label_sys_absent_threshold_29)

        box_sys_absent_threshold_29 = QDoubleSpinBox()
        box_sys_absent_threshold_29.setValue(0.9)
        box_sys_absent_threshold_29.local_path = "indexing.basis_vector_combinations.sys_absent_threshold"
        box_sys_absent_threshold_29.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sys_absent_threshold_29.addWidget(box_sys_absent_threshold_29)
        bg_box.addLayout(hbox_lay_sys_absent_threshold_29)


        hbox_lay_solution_scorer_30 =  QHBoxLayout()
        label_solution_scorer_30 = QLabel("        solution_scorer")
        label_solution_scorer_30.setPalette(palette_object)
        label_solution_scorer_30.setFont(QFont("Monospace"))
        hbox_lay_solution_scorer_30.addWidget(label_solution_scorer_30)

        box_solution_scorer_30 = QComboBox()
        box_solution_scorer_30.local_path = "indexing.basis_vector_combinations.solution_scorer"
        box_solution_scorer_30.tmp_lst=[]
        box_solution_scorer_30.tmp_lst.append("filter")
        box_solution_scorer_30.tmp_lst.append("weighted")
        for lst_itm in box_solution_scorer_30.tmp_lst:
            box_solution_scorer_30.addItem(lst_itm)
        box_solution_scorer_30.setCurrentIndex(1)
        box_solution_scorer_30.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_solution_scorer_30.addWidget(box_solution_scorer_30)
        bg_box.addLayout(hbox_lay_solution_scorer_30)


        label_31 = QLabel("        filter")
        label_31.setPalette(palette_scope)
        label_31.setFont(QFont("Monospace"))
        bg_box.addWidget(label_31)

        hbox_lay_check_doubled_cell_32 =  QHBoxLayout()
        label_check_doubled_cell_32 = QLabel("            check_doubled_cell")
        label_check_doubled_cell_32.setPalette(palette_object)
        label_check_doubled_cell_32.setFont(QFont("Monospace"))
        hbox_lay_check_doubled_cell_32.addWidget(label_check_doubled_cell_32)

        box_check_doubled_cell_32 = QComboBox()
        box_check_doubled_cell_32.local_path = "indexing.basis_vector_combinations.filter.check_doubled_cell"
        box_check_doubled_cell_32.tmp_lst=[]
        box_check_doubled_cell_32.tmp_lst.append("True")
        box_check_doubled_cell_32.tmp_lst.append("False")
        for lst_itm in box_check_doubled_cell_32.tmp_lst:
            box_check_doubled_cell_32.addItem(lst_itm)
        box_check_doubled_cell_32.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_check_doubled_cell_32.addWidget(box_check_doubled_cell_32)
        bg_box.addLayout(hbox_lay_check_doubled_cell_32)


        hbox_lay_likelihood_cutoff_33 =  QHBoxLayout()
        label_likelihood_cutoff_33 = QLabel("            likelihood_cutoff")
        label_likelihood_cutoff_33.setPalette(palette_object)
        label_likelihood_cutoff_33.setFont(QFont("Monospace"))
        hbox_lay_likelihood_cutoff_33.addWidget(label_likelihood_cutoff_33)

        box_likelihood_cutoff_33 = QDoubleSpinBox()
        box_likelihood_cutoff_33.setValue(0.8)
        box_likelihood_cutoff_33.local_path = "indexing.basis_vector_combinations.filter.likelihood_cutoff"
        box_likelihood_cutoff_33.valueChanged.connect(self.spnbox_changed)
        hbox_lay_likelihood_cutoff_33.addWidget(box_likelihood_cutoff_33)
        bg_box.addLayout(hbox_lay_likelihood_cutoff_33)


        hbox_lay_volume_cutoff_34 =  QHBoxLayout()
        label_volume_cutoff_34 = QLabel("            volume_cutoff")
        label_volume_cutoff_34.setPalette(palette_object)
        label_volume_cutoff_34.setFont(QFont("Monospace"))
        hbox_lay_volume_cutoff_34.addWidget(label_volume_cutoff_34)

        box_volume_cutoff_34 = QDoubleSpinBox()
        box_volume_cutoff_34.setValue(1.25)
        box_volume_cutoff_34.local_path = "indexing.basis_vector_combinations.filter.volume_cutoff"
        box_volume_cutoff_34.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_cutoff_34.addWidget(box_volume_cutoff_34)
        bg_box.addLayout(hbox_lay_volume_cutoff_34)


        hbox_lay_n_indexed_cutoff_35 =  QHBoxLayout()
        label_n_indexed_cutoff_35 = QLabel("            n_indexed_cutoff")
        label_n_indexed_cutoff_35.setPalette(palette_object)
        label_n_indexed_cutoff_35.setFont(QFont("Monospace"))
        hbox_lay_n_indexed_cutoff_35.addWidget(label_n_indexed_cutoff_35)

        box_n_indexed_cutoff_35 = QDoubleSpinBox()
        box_n_indexed_cutoff_35.setValue(0.9)
        box_n_indexed_cutoff_35.local_path = "indexing.basis_vector_combinations.filter.n_indexed_cutoff"
        box_n_indexed_cutoff_35.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_cutoff_35.addWidget(box_n_indexed_cutoff_35)
        bg_box.addLayout(hbox_lay_n_indexed_cutoff_35)


        label_36 = QLabel("        weighted")
        label_36.setPalette(palette_scope)
        label_36.setFont(QFont("Monospace"))
        bg_box.addWidget(label_36)

        hbox_lay_power_37 =  QHBoxLayout()
        label_power_37 = QLabel("            power")
        label_power_37.setPalette(palette_object)
        label_power_37.setFont(QFont("Monospace"))
        hbox_lay_power_37.addWidget(label_power_37)

        box_power_37 = QSpinBox()
        box_power_37.setValue(1)
        box_power_37.local_path = "indexing.basis_vector_combinations.weighted.power"
        box_power_37.valueChanged.connect(self.spnbox_changed)
        hbox_lay_power_37.addWidget(box_power_37)
        bg_box.addLayout(hbox_lay_power_37)


        hbox_lay_volume_weight_38 =  QHBoxLayout()
        label_volume_weight_38 = QLabel("            volume_weight")
        label_volume_weight_38.setPalette(palette_object)
        label_volume_weight_38.setFont(QFont("Monospace"))
        hbox_lay_volume_weight_38.addWidget(label_volume_weight_38)

        box_volume_weight_38 = QDoubleSpinBox()
        box_volume_weight_38.setValue(1.0)
        box_volume_weight_38.local_path = "indexing.basis_vector_combinations.weighted.volume_weight"
        box_volume_weight_38.valueChanged.connect(self.spnbox_changed)
        hbox_lay_volume_weight_38.addWidget(box_volume_weight_38)
        bg_box.addLayout(hbox_lay_volume_weight_38)


        hbox_lay_n_indexed_weight_39 =  QHBoxLayout()
        label_n_indexed_weight_39 = QLabel("            n_indexed_weight")
        label_n_indexed_weight_39.setPalette(palette_object)
        label_n_indexed_weight_39.setFont(QFont("Monospace"))
        hbox_lay_n_indexed_weight_39.addWidget(label_n_indexed_weight_39)

        box_n_indexed_weight_39 = QDoubleSpinBox()
        box_n_indexed_weight_39.setValue(1.0)
        box_n_indexed_weight_39.local_path = "indexing.basis_vector_combinations.weighted.n_indexed_weight"
        box_n_indexed_weight_39.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_indexed_weight_39.addWidget(box_n_indexed_weight_39)
        bg_box.addLayout(hbox_lay_n_indexed_weight_39)


        hbox_lay_rmsd_weight_40 =  QHBoxLayout()
        label_rmsd_weight_40 = QLabel("            rmsd_weight")
        label_rmsd_weight_40.setPalette(palette_object)
        label_rmsd_weight_40.setFont(QFont("Monospace"))
        hbox_lay_rmsd_weight_40.addWidget(label_rmsd_weight_40)

        box_rmsd_weight_40 = QDoubleSpinBox()
        box_rmsd_weight_40.setValue(1.0)
        box_rmsd_weight_40.local_path = "indexing.basis_vector_combinations.weighted.rmsd_weight"
        box_rmsd_weight_40.valueChanged.connect(self.spnbox_changed)
        hbox_lay_rmsd_weight_40.addWidget(box_rmsd_weight_40)
        bg_box.addLayout(hbox_lay_rmsd_weight_40)


        label_41 = QLabel("    index_assignment")
        label_41.setPalette(palette_scope)
        label_41.setFont(QFont("Monospace"))
        bg_box.addWidget(label_41)

        hbox_lay_method_42 =  QHBoxLayout()
        label_method_42 = QLabel("        method")
        label_method_42.setPalette(palette_object)
        label_method_42.setFont(QFont("Monospace"))
        hbox_lay_method_42.addWidget(label_method_42)

        box_method_42 = QComboBox()
        box_method_42.local_path = "indexing.index_assignment.method"
        box_method_42.tmp_lst=[]
        box_method_42.tmp_lst.append("simple")
        box_method_42.tmp_lst.append("local")
        for lst_itm in box_method_42.tmp_lst:
            box_method_42.addItem(lst_itm)
        box_method_42.setCurrentIndex(0)
        box_method_42.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_42.addWidget(box_method_42)
        bg_box.addLayout(hbox_lay_method_42)


        label_43 = QLabel("        simple")
        label_43.setPalette(palette_scope)
        label_43.setFont(QFont("Monospace"))
        bg_box.addWidget(label_43)

        hbox_lay_hkl_tolerance_44 =  QHBoxLayout()
        label_hkl_tolerance_44 = QLabel("            hkl_tolerance")
        label_hkl_tolerance_44.setPalette(palette_object)
        label_hkl_tolerance_44.setFont(QFont("Monospace"))
        hbox_lay_hkl_tolerance_44.addWidget(label_hkl_tolerance_44)

        box_hkl_tolerance_44 = QDoubleSpinBox()
        box_hkl_tolerance_44.setValue(0.3)
        box_hkl_tolerance_44.local_path = "indexing.index_assignment.simple.hkl_tolerance"
        box_hkl_tolerance_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hkl_tolerance_44.addWidget(box_hkl_tolerance_44)
        bg_box.addLayout(hbox_lay_hkl_tolerance_44)


        label_45 = QLabel("        local")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace"))
        bg_box.addWidget(label_45)

        hbox_lay_epsilon_46 =  QHBoxLayout()
        label_epsilon_46 = QLabel("            epsilon")
        label_epsilon_46.setPalette(palette_object)
        label_epsilon_46.setFont(QFont("Monospace"))
        hbox_lay_epsilon_46.addWidget(label_epsilon_46)

        box_epsilon_46 = QDoubleSpinBox()
        box_epsilon_46.setValue(0.05)
        box_epsilon_46.local_path = "indexing.index_assignment.local.epsilon"
        box_epsilon_46.valueChanged.connect(self.spnbox_changed)
        hbox_lay_epsilon_46.addWidget(box_epsilon_46)
        bg_box.addLayout(hbox_lay_epsilon_46)


        hbox_lay_delta_47 =  QHBoxLayout()
        label_delta_47 = QLabel("            delta")
        label_delta_47.setPalette(palette_object)
        label_delta_47.setFont(QFont("Monospace"))
        hbox_lay_delta_47.addWidget(label_delta_47)

        box_delta_47 = QSpinBox()
        box_delta_47.setValue(8)
        box_delta_47.local_path = "indexing.index_assignment.local.delta"
        box_delta_47.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delta_47.addWidget(box_delta_47)
        bg_box.addLayout(hbox_lay_delta_47)


        hbox_lay_l_min_48 =  QHBoxLayout()
        label_l_min_48 = QLabel("            l_min")
        label_l_min_48.setPalette(palette_object)
        label_l_min_48.setFont(QFont("Monospace"))
        hbox_lay_l_min_48.addWidget(label_l_min_48)

        box_l_min_48 = QDoubleSpinBox()
        box_l_min_48.setValue(0.8)
        box_l_min_48.local_path = "indexing.index_assignment.local.l_min"
        box_l_min_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_l_min_48.addWidget(box_l_min_48)
        bg_box.addLayout(hbox_lay_l_min_48)


        hbox_lay_nearest_neighbours_49 =  QHBoxLayout()
        label_nearest_neighbours_49 = QLabel("            nearest_neighbours")
        label_nearest_neighbours_49.setPalette(palette_object)
        label_nearest_neighbours_49.setFont(QFont("Monospace"))
        hbox_lay_nearest_neighbours_49.addWidget(label_nearest_neighbours_49)

        box_nearest_neighbours_49 = QSpinBox()
        box_nearest_neighbours_49.setValue(20)
        box_nearest_neighbours_49.local_path = "indexing.index_assignment.local.nearest_neighbours"
        box_nearest_neighbours_49.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nearest_neighbours_49.addWidget(box_nearest_neighbours_49)
        bg_box.addLayout(hbox_lay_nearest_neighbours_49)


        hbox_lay_optimise_initial_basis_vectors_50 =  QHBoxLayout()
        label_optimise_initial_basis_vectors_50 = QLabel("    optimise_initial_basis_vectors")
        label_optimise_initial_basis_vectors_50.setPalette(palette_object)
        label_optimise_initial_basis_vectors_50.setFont(QFont("Monospace"))
        hbox_lay_optimise_initial_basis_vectors_50.addWidget(label_optimise_initial_basis_vectors_50)

        box_optimise_initial_basis_vectors_50 = QComboBox()
        box_optimise_initial_basis_vectors_50.local_path = "indexing.optimise_initial_basis_vectors"
        box_optimise_initial_basis_vectors_50.tmp_lst=[]
        box_optimise_initial_basis_vectors_50.tmp_lst.append("True")
        box_optimise_initial_basis_vectors_50.tmp_lst.append("False")
        for lst_itm in box_optimise_initial_basis_vectors_50.tmp_lst:
            box_optimise_initial_basis_vectors_50.addItem(lst_itm)
        box_optimise_initial_basis_vectors_50.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_optimise_initial_basis_vectors_50.addWidget(box_optimise_initial_basis_vectors_50)
        bg_box.addLayout(hbox_lay_optimise_initial_basis_vectors_50)


        hbox_lay_debug_51 =  QHBoxLayout()
        label_debug_51 = QLabel("    debug")
        label_debug_51.setPalette(palette_object)
        label_debug_51.setFont(QFont("Monospace"))
        hbox_lay_debug_51.addWidget(label_debug_51)

        box_debug_51 = QComboBox()
        box_debug_51.local_path = "indexing.debug"
        box_debug_51.tmp_lst=[]
        box_debug_51.tmp_lst.append("True")
        box_debug_51.tmp_lst.append("False")
        for lst_itm in box_debug_51.tmp_lst:
            box_debug_51.addItem(lst_itm)
        box_debug_51.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_51.addWidget(box_debug_51)
        bg_box.addLayout(hbox_lay_debug_51)


        hbox_lay_debug_plots_52 =  QHBoxLayout()
        label_debug_plots_52 = QLabel("    debug_plots")
        label_debug_plots_52.setPalette(palette_object)
        label_debug_plots_52.setFont(QFont("Monospace"))
        hbox_lay_debug_plots_52.addWidget(label_debug_plots_52)

        box_debug_plots_52 = QComboBox()
        box_debug_plots_52.local_path = "indexing.debug_plots"
        box_debug_plots_52.tmp_lst=[]
        box_debug_plots_52.tmp_lst.append("True")
        box_debug_plots_52.tmp_lst.append("False")
        for lst_itm in box_debug_plots_52.tmp_lst:
            box_debug_plots_52.addItem(lst_itm)
        box_debug_plots_52.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_debug_plots_52.addWidget(box_debug_plots_52)
        bg_box.addLayout(hbox_lay_debug_plots_52)


        hbox_lay_combine_scans_53 =  QHBoxLayout()
        label_combine_scans_53 = QLabel("    combine_scans")
        label_combine_scans_53.setPalette(palette_object)
        label_combine_scans_53.setFont(QFont("Monospace"))
        hbox_lay_combine_scans_53.addWidget(label_combine_scans_53)

        box_combine_scans_53 = QComboBox()
        box_combine_scans_53.local_path = "indexing.combine_scans"
        box_combine_scans_53.tmp_lst=[]
        box_combine_scans_53.tmp_lst.append("True")
        box_combine_scans_53.tmp_lst.append("False")
        for lst_itm in box_combine_scans_53.tmp_lst:
            box_combine_scans_53.addItem(lst_itm)
        box_combine_scans_53.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_combine_scans_53.addWidget(box_combine_scans_53)
        bg_box.addLayout(hbox_lay_combine_scans_53)


        label_54 = QLabel("    refinement_protocol")
        label_54.setPalette(palette_scope)
        label_54.setFont(QFont("Monospace"))
        bg_box.addWidget(label_54)

        hbox_lay_n_macro_cycles_55 =  QHBoxLayout()
        label_n_macro_cycles_55 = QLabel("        n_macro_cycles")
        label_n_macro_cycles_55.setPalette(palette_object)
        label_n_macro_cycles_55.setFont(QFont("Monospace"))
        hbox_lay_n_macro_cycles_55.addWidget(label_n_macro_cycles_55)

        box_n_macro_cycles_55 = QSpinBox()
        box_n_macro_cycles_55.setValue(5)
        box_n_macro_cycles_55.local_path = "indexing.refinement_protocol.n_macro_cycles"
        box_n_macro_cycles_55.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_macro_cycles_55.addWidget(box_n_macro_cycles_55)
        bg_box.addLayout(hbox_lay_n_macro_cycles_55)


        hbox_lay_d_min_step_56 =  QHBoxLayout()
        label_d_min_step_56 = QLabel("        d_min_step")
        label_d_min_step_56.setPalette(palette_object)
        label_d_min_step_56.setFont(QFont("Monospace"))
        hbox_lay_d_min_step_56.addWidget(label_d_min_step_56)

        box_d_min_step_56 = QDoubleSpinBox()
        box_d_min_step_56.local_path = "indexing.refinement_protocol.d_min_step"
        box_d_min_step_56.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_step_56.addWidget(box_d_min_step_56)
        bg_box.addLayout(hbox_lay_d_min_step_56)


        hbox_lay_d_min_start_57 =  QHBoxLayout()
        label_d_min_start_57 = QLabel("        d_min_start")
        label_d_min_start_57.setPalette(palette_object)
        label_d_min_start_57.setFont(QFont("Monospace"))
        hbox_lay_d_min_start_57.addWidget(label_d_min_start_57)

        box_d_min_start_57 = QDoubleSpinBox()
        box_d_min_start_57.local_path = "indexing.refinement_protocol.d_min_start"
        box_d_min_start_57.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_start_57.addWidget(box_d_min_start_57)
        bg_box.addLayout(hbox_lay_d_min_start_57)


        hbox_lay_d_min_final_58 =  QHBoxLayout()
        label_d_min_final_58 = QLabel("        d_min_final")
        label_d_min_final_58.setPalette(palette_object)
        label_d_min_final_58.setFont(QFont("Monospace"))
        hbox_lay_d_min_final_58.addWidget(label_d_min_final_58)

        box_d_min_final_58 = QDoubleSpinBox()
        box_d_min_final_58.local_path = "indexing.refinement_protocol.d_min_final"
        box_d_min_final_58.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_final_58.addWidget(box_d_min_final_58)
        bg_box.addLayout(hbox_lay_d_min_final_58)


        hbox_lay_verbosity_59 =  QHBoxLayout()
        label_verbosity_59 = QLabel("        verbosity")
        label_verbosity_59.setPalette(palette_object)
        label_verbosity_59.setFont(QFont("Monospace"))
        hbox_lay_verbosity_59.addWidget(label_verbosity_59)

        box_verbosity_59 = QSpinBox()
        box_verbosity_59.setValue(1)
        box_verbosity_59.local_path = "indexing.refinement_protocol.verbosity"
        box_verbosity_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_59.addWidget(box_verbosity_59)
        bg_box.addLayout(hbox_lay_verbosity_59)


        hbox_lay_disable_unit_cell_volume_sanity_check_60 =  QHBoxLayout()
        label_disable_unit_cell_volume_sanity_check_60 = QLabel("        disable_unit_cell_volume_sanity_check")
        label_disable_unit_cell_volume_sanity_check_60.setPalette(palette_object)
        label_disable_unit_cell_volume_sanity_check_60.setFont(QFont("Monospace"))
        hbox_lay_disable_unit_cell_volume_sanity_check_60.addWidget(label_disable_unit_cell_volume_sanity_check_60)

        box_disable_unit_cell_volume_sanity_check_60 = QComboBox()
        box_disable_unit_cell_volume_sanity_check_60.local_path = "indexing.refinement_protocol.disable_unit_cell_volume_sanity_check"
        box_disable_unit_cell_volume_sanity_check_60.tmp_lst=[]
        box_disable_unit_cell_volume_sanity_check_60.tmp_lst.append("True")
        box_disable_unit_cell_volume_sanity_check_60.tmp_lst.append("False")
        for lst_itm in box_disable_unit_cell_volume_sanity_check_60.tmp_lst:
            box_disable_unit_cell_volume_sanity_check_60.addItem(lst_itm)
        box_disable_unit_cell_volume_sanity_check_60.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_disable_unit_cell_volume_sanity_check_60.addWidget(box_disable_unit_cell_volume_sanity_check_60)
        bg_box.addLayout(hbox_lay_disable_unit_cell_volume_sanity_check_60)


        label_61 = QLabel("        outlier_rejection")
        label_61.setPalette(palette_scope)
        label_61.setFont(QFont("Monospace"))
        bg_box.addWidget(label_61)

        hbox_lay_maximum_spot_error_62 =  QHBoxLayout()
        label_maximum_spot_error_62 = QLabel("            maximum_spot_error")
        label_maximum_spot_error_62.setPalette(palette_object)
        label_maximum_spot_error_62.setFont(QFont("Monospace"))
        hbox_lay_maximum_spot_error_62.addWidget(label_maximum_spot_error_62)

        box_maximum_spot_error_62 = QDoubleSpinBox()
        box_maximum_spot_error_62.local_path = "indexing.refinement_protocol.outlier_rejection.maximum_spot_error"
        box_maximum_spot_error_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_spot_error_62.addWidget(box_maximum_spot_error_62)
        bg_box.addLayout(hbox_lay_maximum_spot_error_62)


        hbox_lay_maximum_phi_error_63 =  QHBoxLayout()
        label_maximum_phi_error_63 = QLabel("            maximum_phi_error")
        label_maximum_phi_error_63.setPalette(palette_object)
        label_maximum_phi_error_63.setFont(QFont("Monospace"))
        hbox_lay_maximum_phi_error_63.addWidget(label_maximum_phi_error_63)

        box_maximum_phi_error_63 = QDoubleSpinBox()
        box_maximum_phi_error_63.local_path = "indexing.refinement_protocol.outlier_rejection.maximum_phi_error"
        box_maximum_phi_error_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_phi_error_63.addWidget(box_maximum_phi_error_63)
        bg_box.addLayout(hbox_lay_maximum_phi_error_63)


        hbox_lay_method_64 =  QHBoxLayout()
        label_method_64 = QLabel("    method")
        label_method_64.setPalette(palette_object)
        label_method_64.setFont(QFont("Monospace"))
        hbox_lay_method_64.addWidget(label_method_64)

        box_method_64 = QComboBox()
        box_method_64.local_path = "indexing.method"
        box_method_64.tmp_lst=[]
        box_method_64.tmp_lst.append("fft3d")
        box_method_64.tmp_lst.append("fft1d")
        box_method_64.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_64.tmp_lst:
            box_method_64.addItem(lst_itm)
        box_method_64.setCurrentIndex(0)
        box_method_64.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_64.addWidget(box_method_64)
        bg_box.addLayout(hbox_lay_method_64)


        label_65 = QLabel("    multiple_lattice_search")
        label_65.setPalette(palette_scope)
        label_65.setFont(QFont("Monospace"))
        bg_box.addWidget(label_65)

        hbox_lay_cluster_analysis_search_66 =  QHBoxLayout()
        label_cluster_analysis_search_66 = QLabel("        cluster_analysis_search")
        label_cluster_analysis_search_66.setPalette(palette_object)
        label_cluster_analysis_search_66.setFont(QFont("Monospace"))
        hbox_lay_cluster_analysis_search_66.addWidget(label_cluster_analysis_search_66)

        box_cluster_analysis_search_66 = QComboBox()
        box_cluster_analysis_search_66.local_path = "indexing.multiple_lattice_search.cluster_analysis_search"
        box_cluster_analysis_search_66.tmp_lst=[]
        box_cluster_analysis_search_66.tmp_lst.append("True")
        box_cluster_analysis_search_66.tmp_lst.append("False")
        for lst_itm in box_cluster_analysis_search_66.tmp_lst:
            box_cluster_analysis_search_66.addItem(lst_itm)
        box_cluster_analysis_search_66.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cluster_analysis_search_66.addWidget(box_cluster_analysis_search_66)
        bg_box.addLayout(hbox_lay_cluster_analysis_search_66)


        hbox_lay_recycle_unindexed_reflections_cutoff_67 =  QHBoxLayout()
        label_recycle_unindexed_reflections_cutoff_67 = QLabel("        recycle_unindexed_reflections_cutoff")
        label_recycle_unindexed_reflections_cutoff_67.setPalette(palette_object)
        label_recycle_unindexed_reflections_cutoff_67.setFont(QFont("Monospace"))
        hbox_lay_recycle_unindexed_reflections_cutoff_67.addWidget(label_recycle_unindexed_reflections_cutoff_67)

        box_recycle_unindexed_reflections_cutoff_67 = QDoubleSpinBox()
        box_recycle_unindexed_reflections_cutoff_67.setValue(0.1)
        box_recycle_unindexed_reflections_cutoff_67.local_path = "indexing.multiple_lattice_search.recycle_unindexed_reflections_cutoff"
        box_recycle_unindexed_reflections_cutoff_67.valueChanged.connect(self.spnbox_changed)
        hbox_lay_recycle_unindexed_reflections_cutoff_67.addWidget(box_recycle_unindexed_reflections_cutoff_67)
        bg_box.addLayout(hbox_lay_recycle_unindexed_reflections_cutoff_67)


        hbox_lay_minimum_angular_separation_68 =  QHBoxLayout()
        label_minimum_angular_separation_68 = QLabel("        minimum_angular_separation")
        label_minimum_angular_separation_68.setPalette(palette_object)
        label_minimum_angular_separation_68.setFont(QFont("Monospace"))
        hbox_lay_minimum_angular_separation_68.addWidget(label_minimum_angular_separation_68)

        box_minimum_angular_separation_68 = QDoubleSpinBox()
        box_minimum_angular_separation_68.setValue(5.0)
        box_minimum_angular_separation_68.local_path = "indexing.multiple_lattice_search.minimum_angular_separation"
        box_minimum_angular_separation_68.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_angular_separation_68.addWidget(box_minimum_angular_separation_68)
        bg_box.addLayout(hbox_lay_minimum_angular_separation_68)


        hbox_lay_max_lattices_69 =  QHBoxLayout()
        label_max_lattices_69 = QLabel("        max_lattices")
        label_max_lattices_69.setPalette(palette_object)
        label_max_lattices_69.setFont(QFont("Monospace"))
        hbox_lay_max_lattices_69.addWidget(label_max_lattices_69)

        box_max_lattices_69 = QSpinBox()
        box_max_lattices_69.setValue(1)
        box_max_lattices_69.local_path = "indexing.multiple_lattice_search.max_lattices"
        box_max_lattices_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_lattices_69.addWidget(box_max_lattices_69)
        bg_box.addLayout(hbox_lay_max_lattices_69)


        label_70 = QLabel("        cluster_analysis")
        label_70.setPalette(palette_scope)
        label_70.setFont(QFont("Monospace"))
        bg_box.addWidget(label_70)

        hbox_lay_method_71 =  QHBoxLayout()
        label_method_71 = QLabel("            method")
        label_method_71.setPalette(palette_object)
        label_method_71.setFont(QFont("Monospace"))
        hbox_lay_method_71.addWidget(label_method_71)

        box_method_71 = QComboBox()
        box_method_71.local_path = "indexing.multiple_lattice_search.cluster_analysis.method"
        box_method_71.tmp_lst=[]
        box_method_71.tmp_lst.append("dbscan")
        box_method_71.tmp_lst.append("hcluster")
        for lst_itm in box_method_71.tmp_lst:
            box_method_71.addItem(lst_itm)
        box_method_71.setCurrentIndex(0)
        box_method_71.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_71.addWidget(box_method_71)
        bg_box.addLayout(hbox_lay_method_71)


        label_72 = QLabel("            hcluster")
        label_72.setPalette(palette_scope)
        label_72.setFont(QFont("Monospace"))
        bg_box.addWidget(label_72)

        label_73 = QLabel("                linkage")
        label_73.setPalette(palette_scope)
        label_73.setFont(QFont("Monospace"))
        bg_box.addWidget(label_73)

        hbox_lay_method_74 =  QHBoxLayout()
        label_method_74 = QLabel("                    method")
        label_method_74.setPalette(palette_object)
        label_method_74.setFont(QFont("Monospace"))
        hbox_lay_method_74.addWidget(label_method_74)

        box_method_74 = QComboBox()
        box_method_74.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.method"
        box_method_74.tmp_lst=[]
        box_method_74.tmp_lst.append("ward")
        for lst_itm in box_method_74.tmp_lst:
            box_method_74.addItem(lst_itm)
        box_method_74.setCurrentIndex(0)
        box_method_74.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_74.addWidget(box_method_74)
        bg_box.addLayout(hbox_lay_method_74)


        hbox_lay_metric_75 =  QHBoxLayout()
        label_metric_75 = QLabel("                    metric")
        label_metric_75.setPalette(palette_object)
        label_metric_75.setFont(QFont("Monospace"))
        hbox_lay_metric_75.addWidget(label_metric_75)

        box_metric_75 = QComboBox()
        box_metric_75.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.linkage.metric"
        box_metric_75.tmp_lst=[]
        box_metric_75.tmp_lst.append("euclidean")
        for lst_itm in box_metric_75.tmp_lst:
            box_metric_75.addItem(lst_itm)
        box_metric_75.setCurrentIndex(0)
        box_metric_75.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_metric_75.addWidget(box_metric_75)
        bg_box.addLayout(hbox_lay_metric_75)


        hbox_lay_cutoff_76 =  QHBoxLayout()
        label_cutoff_76 = QLabel("                cutoff")
        label_cutoff_76.setPalette(palette_object)
        label_cutoff_76.setFont(QFont("Monospace"))
        hbox_lay_cutoff_76.addWidget(label_cutoff_76)

        box_cutoff_76 = QDoubleSpinBox()
        box_cutoff_76.setValue(15.0)
        box_cutoff_76.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff"
        box_cutoff_76.valueChanged.connect(self.spnbox_changed)
        hbox_lay_cutoff_76.addWidget(box_cutoff_76)
        bg_box.addLayout(hbox_lay_cutoff_76)


        hbox_lay_cutoff_criterion_77 =  QHBoxLayout()
        label_cutoff_criterion_77 = QLabel("                cutoff_criterion")
        label_cutoff_criterion_77.setPalette(palette_object)
        label_cutoff_criterion_77.setFont(QFont("Monospace"))
        hbox_lay_cutoff_criterion_77.addWidget(label_cutoff_criterion_77)

        box_cutoff_criterion_77 = QComboBox()
        box_cutoff_criterion_77.local_path = "indexing.multiple_lattice_search.cluster_analysis.hcluster.cutoff_criterion"
        box_cutoff_criterion_77.tmp_lst=[]
        box_cutoff_criterion_77.tmp_lst.append("distance")
        box_cutoff_criterion_77.tmp_lst.append("inconsistent")
        for lst_itm in box_cutoff_criterion_77.tmp_lst:
            box_cutoff_criterion_77.addItem(lst_itm)
        box_cutoff_criterion_77.setCurrentIndex(0)
        box_cutoff_criterion_77.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_cutoff_criterion_77.addWidget(box_cutoff_criterion_77)
        bg_box.addLayout(hbox_lay_cutoff_criterion_77)


        label_78 = QLabel("            dbscan")
        label_78.setPalette(palette_scope)
        label_78.setFont(QFont("Monospace"))
        bg_box.addWidget(label_78)

        hbox_lay_eps_79 =  QHBoxLayout()
        label_eps_79 = QLabel("                eps")
        label_eps_79.setPalette(palette_object)
        label_eps_79.setFont(QFont("Monospace"))
        hbox_lay_eps_79.addWidget(label_eps_79)

        box_eps_79 = QDoubleSpinBox()
        box_eps_79.setValue(0.05)
        box_eps_79.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.eps"
        box_eps_79.valueChanged.connect(self.spnbox_changed)
        hbox_lay_eps_79.addWidget(box_eps_79)
        bg_box.addLayout(hbox_lay_eps_79)


        hbox_lay_min_samples_80 =  QHBoxLayout()
        label_min_samples_80 = QLabel("                min_samples")
        label_min_samples_80.setPalette(palette_object)
        label_min_samples_80.setFont(QFont("Monospace"))
        hbox_lay_min_samples_80.addWidget(label_min_samples_80)

        box_min_samples_80 = QSpinBox()
        box_min_samples_80.setValue(30)
        box_min_samples_80.local_path = "indexing.multiple_lattice_search.cluster_analysis.dbscan.min_samples"
        box_min_samples_80.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_samples_80.addWidget(box_min_samples_80)
        bg_box.addLayout(hbox_lay_min_samples_80)


        hbox_lay_min_cluster_size_81 =  QHBoxLayout()
        label_min_cluster_size_81 = QLabel("            min_cluster_size")
        label_min_cluster_size_81.setPalette(palette_object)
        label_min_cluster_size_81.setFont(QFont("Monospace"))
        hbox_lay_min_cluster_size_81.addWidget(label_min_cluster_size_81)

        box_min_cluster_size_81 = QSpinBox()
        box_min_cluster_size_81.setValue(20)
        box_min_cluster_size_81.local_path = "indexing.multiple_lattice_search.cluster_analysis.min_cluster_size"
        box_min_cluster_size_81.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_cluster_size_81.addWidget(box_min_cluster_size_81)
        bg_box.addLayout(hbox_lay_min_cluster_size_81)


        hbox_lay_intersection_union_ratio_cutoff_82 =  QHBoxLayout()
        label_intersection_union_ratio_cutoff_82 = QLabel("            intersection_union_ratio_cutoff")
        label_intersection_union_ratio_cutoff_82.setPalette(palette_object)
        label_intersection_union_ratio_cutoff_82.setFont(QFont("Monospace"))
        hbox_lay_intersection_union_ratio_cutoff_82.addWidget(label_intersection_union_ratio_cutoff_82)

        box_intersection_union_ratio_cutoff_82 = QDoubleSpinBox()
        box_intersection_union_ratio_cutoff_82.setValue(0.4)
        box_intersection_union_ratio_cutoff_82.local_path = "indexing.multiple_lattice_search.cluster_analysis.intersection_union_ratio_cutoff"
        box_intersection_union_ratio_cutoff_82.valueChanged.connect(self.spnbox_changed)
        hbox_lay_intersection_union_ratio_cutoff_82.addWidget(box_intersection_union_ratio_cutoff_82)
        bg_box.addLayout(hbox_lay_intersection_union_ratio_cutoff_82)


        label_83 = QLabel("    real_space_grid_search")
        label_83.setPalette(palette_scope)
        label_83.setFont(QFont("Monospace"))
        bg_box.addWidget(label_83)

        hbox_lay_characteristic_grid_84 =  QHBoxLayout()
        label_characteristic_grid_84 = QLabel("        characteristic_grid")
        label_characteristic_grid_84.setPalette(palette_object)
        label_characteristic_grid_84.setFont(QFont("Monospace"))
        hbox_lay_characteristic_grid_84.addWidget(label_characteristic_grid_84)

        box_characteristic_grid_84 = QDoubleSpinBox()
        box_characteristic_grid_84.setValue(0.02)
        box_characteristic_grid_84.local_path = "indexing.real_space_grid_search.characteristic_grid"
        box_characteristic_grid_84.valueChanged.connect(self.spnbox_changed)
        hbox_lay_characteristic_grid_84.addWidget(box_characteristic_grid_84)
        bg_box.addLayout(hbox_lay_characteristic_grid_84)


        label_85 = QLabel("refinement")
        label_85.setPalette(palette_scope)
        label_85.setFont(QFont("Monospace"))
        bg_box.addWidget(label_85)

        label_86 = QLabel("    mp")
        label_86.setPalette(palette_scope)
        label_86.setFont(QFont("Monospace"))
        bg_box.addWidget(label_86)

        hbox_lay_nproc_87 =  QHBoxLayout()
        label_nproc_87 = QLabel("        nproc")
        label_nproc_87.setPalette(palette_object)
        label_nproc_87.setFont(QFont("Monospace"))
        hbox_lay_nproc_87.addWidget(label_nproc_87)

        box_nproc_87 = QSpinBox()
        box_nproc_87.setValue(1)
        box_nproc_87.local_path = "refinement.mp.nproc"
        box_nproc_87.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_87.addWidget(box_nproc_87)
        bg_box.addLayout(hbox_lay_nproc_87)


        hbox_lay_verbosity_88 =  QHBoxLayout()
        label_verbosity_88 = QLabel("    verbosity")
        label_verbosity_88.setPalette(palette_object)
        label_verbosity_88.setFont(QFont("Monospace"))
        hbox_lay_verbosity_88.addWidget(label_verbosity_88)

        box_verbosity_88 = QSpinBox()
        box_verbosity_88.setValue(1)
        box_verbosity_88.local_path = "refinement.verbosity"
        box_verbosity_88.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_88.addWidget(box_verbosity_88)
        bg_box.addLayout(hbox_lay_verbosity_88)


        label_89 = QLabel("    parameterisation")
        label_89.setPalette(palette_scope)
        label_89.setFont(QFont("Monospace"))
        bg_box.addWidget(label_89)

        label_90 = QLabel("        auto_reduction")
        label_90.setPalette(palette_scope)
        label_90.setFont(QFont("Monospace"))
        bg_box.addWidget(label_90)

        hbox_lay_min_nref_per_parameter_91 =  QHBoxLayout()
        label_min_nref_per_parameter_91 = QLabel("            min_nref_per_parameter")
        label_min_nref_per_parameter_91.setPalette(palette_object)
        label_min_nref_per_parameter_91.setFont(QFont("Monospace"))
        hbox_lay_min_nref_per_parameter_91.addWidget(label_min_nref_per_parameter_91)

        box_min_nref_per_parameter_91 = QSpinBox()
        box_min_nref_per_parameter_91.setValue(5)
        box_min_nref_per_parameter_91.local_path = "refinement.parameterisation.auto_reduction.min_nref_per_parameter"
        box_min_nref_per_parameter_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_nref_per_parameter_91.addWidget(box_min_nref_per_parameter_91)
        bg_box.addLayout(hbox_lay_min_nref_per_parameter_91)


        hbox_lay_action_92 =  QHBoxLayout()
        label_action_92 = QLabel("            action")
        label_action_92.setPalette(palette_object)
        label_action_92.setFont(QFont("Monospace"))
        hbox_lay_action_92.addWidget(label_action_92)

        box_action_92 = QComboBox()
        box_action_92.local_path = "refinement.parameterisation.auto_reduction.action"
        box_action_92.tmp_lst=[]
        box_action_92.tmp_lst.append("fail")
        box_action_92.tmp_lst.append("fix")
        box_action_92.tmp_lst.append("remove")
        for lst_itm in box_action_92.tmp_lst:
            box_action_92.addItem(lst_itm)
        box_action_92.setCurrentIndex(0)
        box_action_92.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_action_92.addWidget(box_action_92)
        bg_box.addLayout(hbox_lay_action_92)


        label_93 = QLabel("        beam")
        label_93.setPalette(palette_scope)
        label_93.setFont(QFont("Monospace"))
        bg_box.addWidget(label_93)

        hbox_lay_fix_94 =  QHBoxLayout()
        label_fix_94 = QLabel("            fix")
        label_fix_94.setPalette(palette_object)
        label_fix_94.setFont(QFont("Monospace"))
        hbox_lay_fix_94.addWidget(label_fix_94)

        box_fix_94 = QComboBox()
        box_fix_94.local_path = "refinement.parameterisation.beam.fix"
        box_fix_94.tmp_lst=[]
        box_fix_94.tmp_lst.append("all")
        box_fix_94.tmp_lst.append("in_spindle_plane")
        box_fix_94.tmp_lst.append("out_spindle_plane")
        box_fix_94.tmp_lst.append("wavelength")
        for lst_itm in box_fix_94.tmp_lst:
            box_fix_94.addItem(lst_itm)
        box_fix_94.setCurrentIndex(3)
        box_fix_94.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_94.addWidget(box_fix_94)
        bg_box.addLayout(hbox_lay_fix_94)



        label_96 = QLabel("        crystal")
        label_96.setPalette(palette_scope)
        label_96.setFont(QFont("Monospace"))
        bg_box.addWidget(label_96)

        hbox_lay_fix_97 =  QHBoxLayout()
        label_fix_97 = QLabel("            fix")
        label_fix_97.setPalette(palette_object)
        label_fix_97.setFont(QFont("Monospace"))
        hbox_lay_fix_97.addWidget(label_fix_97)

        box_fix_97 = QComboBox()
        box_fix_97.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_97.tmp_lst=[]
        box_fix_97.tmp_lst.append("all")
        box_fix_97.tmp_lst.append("cell")
        box_fix_97.tmp_lst.append("orientation")
        for lst_itm in box_fix_97.tmp_lst:
            box_fix_97.addItem(lst_itm)
        box_fix_97.setCurrentIndex(0)
        box_fix_97.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_97.addWidget(box_fix_97)
        bg_box.addLayout(hbox_lay_fix_97)


        label_98 = QLabel("            unit_cell")
        label_98.setPalette(palette_scope)
        label_98.setFont(QFont("Monospace"))
        bg_box.addWidget(label_98)


        label_100 = QLabel("                restraints")
        label_100.setPalette(palette_scope)
        label_100.setFont(QFont("Monospace"))
        bg_box.addWidget(label_100)

        label_101 = QLabel("                    tie_to_target")
        label_101.setPalette(palette_scope)
        label_101.setFont(QFont("Monospace"))
        bg_box.addWidget(label_101)

        hbox_lay_values_102_0 =  QHBoxLayout()
        label_values_102_0 = QLabel("                        values[1]")
        label_values_102_0.setPalette(palette_object)
        label_values_102_0.setFont(QFont("Monospace"))
        hbox_lay_values_102_0.addWidget(label_values_102_0)
        box_values_102_0 = QDoubleSpinBox()
        box_values_102_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_102_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_102_1 =  QHBoxLayout()
        label_values_102_1 = QLabel("                        values[2]")
        label_values_102_1.setPalette(palette_object)
        label_values_102_1.setFont(QFont("Monospace"))
        hbox_lay_values_102_1.addWidget(label_values_102_1)
        box_values_102_1 = QDoubleSpinBox()
        box_values_102_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_102_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_102_2 =  QHBoxLayout()
        label_values_102_2 = QLabel("                        values[3]")
        label_values_102_2.setPalette(palette_object)
        label_values_102_2.setFont(QFont("Monospace"))
        hbox_lay_values_102_2.addWidget(label_values_102_2)
        box_values_102_2 = QDoubleSpinBox()
        box_values_102_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_102_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_102_3 =  QHBoxLayout()
        label_values_102_3 = QLabel("                        values[4]")
        label_values_102_3.setPalette(palette_object)
        label_values_102_3.setFont(QFont("Monospace"))
        hbox_lay_values_102_3.addWidget(label_values_102_3)
        box_values_102_3 = QDoubleSpinBox()
        box_values_102_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_102_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_102_4 =  QHBoxLayout()
        label_values_102_4 = QLabel("                        values[5]")
        label_values_102_4.setPalette(palette_object)
        label_values_102_4.setFont(QFont("Monospace"))
        hbox_lay_values_102_4.addWidget(label_values_102_4)
        box_values_102_4 = QDoubleSpinBox()
        box_values_102_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_102_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_102_5 =  QHBoxLayout()
        label_values_102_5 = QLabel("                        values[6]")
        label_values_102_5.setPalette(palette_object)
        label_values_102_5.setFont(QFont("Monospace"))
        hbox_lay_values_102_5.addWidget(label_values_102_5)
        box_values_102_5 = QDoubleSpinBox()
        box_values_102_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_102_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_sigmas_103_0 =  QHBoxLayout()
        label_sigmas_103_0 = QLabel("                        sigmas[1]")
        label_sigmas_103_0.setPalette(palette_object)
        label_sigmas_103_0.setFont(QFont("Monospace"))
        hbox_lay_sigmas_103_0.addWidget(label_sigmas_103_0)
        box_sigmas_103_0 = QDoubleSpinBox()
        box_sigmas_103_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_103_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_103_1 =  QHBoxLayout()
        label_sigmas_103_1 = QLabel("                        sigmas[2]")
        label_sigmas_103_1.setPalette(palette_object)
        label_sigmas_103_1.setFont(QFont("Monospace"))
        hbox_lay_sigmas_103_1.addWidget(label_sigmas_103_1)
        box_sigmas_103_1 = QDoubleSpinBox()
        box_sigmas_103_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_103_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_103_2 =  QHBoxLayout()
        label_sigmas_103_2 = QLabel("                        sigmas[3]")
        label_sigmas_103_2.setPalette(palette_object)
        label_sigmas_103_2.setFont(QFont("Monospace"))
        hbox_lay_sigmas_103_2.addWidget(label_sigmas_103_2)
        box_sigmas_103_2 = QDoubleSpinBox()
        box_sigmas_103_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_103_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_103_3 =  QHBoxLayout()
        label_sigmas_103_3 = QLabel("                        sigmas[4]")
        label_sigmas_103_3.setPalette(palette_object)
        label_sigmas_103_3.setFont(QFont("Monospace"))
        hbox_lay_sigmas_103_3.addWidget(label_sigmas_103_3)
        box_sigmas_103_3 = QDoubleSpinBox()
        box_sigmas_103_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_103_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_103_4 =  QHBoxLayout()
        label_sigmas_103_4 = QLabel("                        sigmas[5]")
        label_sigmas_103_4.setPalette(palette_object)
        label_sigmas_103_4.setFont(QFont("Monospace"))
        hbox_lay_sigmas_103_4.addWidget(label_sigmas_103_4)
        box_sigmas_103_4 = QDoubleSpinBox()
        box_sigmas_103_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_103_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_103_5 =  QHBoxLayout()
        label_sigmas_103_5 = QLabel("                        sigmas[6]")
        label_sigmas_103_5.setPalette(palette_object)
        label_sigmas_103_5.setFont(QFont("Monospace"))
        hbox_lay_sigmas_103_5.addWidget(label_sigmas_103_5)
        box_sigmas_103_5 = QDoubleSpinBox()
        box_sigmas_103_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_103_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_id_104 =  QHBoxLayout()
        label_id_104 = QLabel("                        id")
        label_id_104.setPalette(palette_object)
        label_id_104.setFont(QFont("Monospace"))
        hbox_lay_id_104.addWidget(label_id_104)

        box_id_104 = QSpinBox()
        box_id_104.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.id"
        box_id_104.valueChanged.connect(self.spnbox_changed)
        hbox_lay_id_104.addWidget(box_id_104)
        bg_box.addLayout(hbox_lay_id_104)


        label_105 = QLabel("                    tie_to_group")
        label_105.setPalette(palette_scope)
        label_105.setFont(QFont("Monospace"))
        bg_box.addWidget(label_105)

        hbox_lay_target_106 =  QHBoxLayout()
        label_target_106 = QLabel("                        target")
        label_target_106.setPalette(palette_object)
        label_target_106.setFont(QFont("Monospace"))
        hbox_lay_target_106.addWidget(label_target_106)

        box_target_106 = QComboBox()
        box_target_106.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_106.tmp_lst=[]
        box_target_106.tmp_lst.append("mean")
        box_target_106.tmp_lst.append("median")
        for lst_itm in box_target_106.tmp_lst:
            box_target_106.addItem(lst_itm)
        box_target_106.setCurrentIndex(0)
        box_target_106.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_106.addWidget(box_target_106)
        bg_box.addLayout(hbox_lay_target_106)




        label_109 = QLabel("            orientation")
        label_109.setPalette(palette_scope)
        label_109.setFont(QFont("Monospace"))
        bg_box.addWidget(label_109)


        hbox_lay_scan_varying_111 =  QHBoxLayout()
        label_scan_varying_111 = QLabel("            scan_varying")
        label_scan_varying_111.setPalette(palette_object)
        label_scan_varying_111.setFont(QFont("Monospace"))
        hbox_lay_scan_varying_111.addWidget(label_scan_varying_111)

        box_scan_varying_111 = QComboBox()
        box_scan_varying_111.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_111.tmp_lst=[]
        box_scan_varying_111.tmp_lst.append("True")
        box_scan_varying_111.tmp_lst.append("False")
        for lst_itm in box_scan_varying_111.tmp_lst:
            box_scan_varying_111.addItem(lst_itm)
        box_scan_varying_111.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_111.addWidget(box_scan_varying_111)
        bg_box.addLayout(hbox_lay_scan_varying_111)


        hbox_lay_num_intervals_112 =  QHBoxLayout()
        label_num_intervals_112 = QLabel("            num_intervals")
        label_num_intervals_112.setPalette(palette_object)
        label_num_intervals_112.setFont(QFont("Monospace"))
        hbox_lay_num_intervals_112.addWidget(label_num_intervals_112)

        box_num_intervals_112 = QComboBox()
        box_num_intervals_112.local_path = "refinement.parameterisation.crystal.num_intervals"
        box_num_intervals_112.tmp_lst=[]
        box_num_intervals_112.tmp_lst.append("fixed_width")
        box_num_intervals_112.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_112.tmp_lst:
            box_num_intervals_112.addItem(lst_itm)
        box_num_intervals_112.setCurrentIndex(0)
        box_num_intervals_112.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_112.addWidget(box_num_intervals_112)
        bg_box.addLayout(hbox_lay_num_intervals_112)


        hbox_lay_interval_width_degrees_113 =  QHBoxLayout()
        label_interval_width_degrees_113 = QLabel("            interval_width_degrees")
        label_interval_width_degrees_113.setPalette(palette_object)
        label_interval_width_degrees_113.setFont(QFont("Monospace"))
        hbox_lay_interval_width_degrees_113.addWidget(label_interval_width_degrees_113)

        box_interval_width_degrees_113 = QDoubleSpinBox()
        box_interval_width_degrees_113.setValue(36.0)
        box_interval_width_degrees_113.local_path = "refinement.parameterisation.crystal.interval_width_degrees"
        box_interval_width_degrees_113.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_113.addWidget(box_interval_width_degrees_113)
        bg_box.addLayout(hbox_lay_interval_width_degrees_113)


        hbox_lay_absolute_num_intervals_114 =  QHBoxLayout()
        label_absolute_num_intervals_114 = QLabel("            absolute_num_intervals")
        label_absolute_num_intervals_114.setPalette(palette_object)
        label_absolute_num_intervals_114.setFont(QFont("Monospace"))
        hbox_lay_absolute_num_intervals_114.addWidget(label_absolute_num_intervals_114)

        box_absolute_num_intervals_114 = QSpinBox()
        box_absolute_num_intervals_114.setValue(5)
        box_absolute_num_intervals_114.local_path = "refinement.parameterisation.crystal.absolute_num_intervals"
        box_absolute_num_intervals_114.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_114.addWidget(box_absolute_num_intervals_114)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_114)


        hbox_lay_UB_model_per_115 =  QHBoxLayout()
        label_UB_model_per_115 = QLabel("            UB_model_per")
        label_UB_model_per_115.setPalette(palette_object)
        label_UB_model_per_115.setFont(QFont("Monospace"))
        hbox_lay_UB_model_per_115.addWidget(label_UB_model_per_115)

        box_UB_model_per_115 = QComboBox()
        box_UB_model_per_115.local_path = "refinement.parameterisation.crystal.UB_model_per"
        box_UB_model_per_115.tmp_lst=[]
        box_UB_model_per_115.tmp_lst.append("reflection")
        box_UB_model_per_115.tmp_lst.append("image")
        box_UB_model_per_115.tmp_lst.append("block")
        for lst_itm in box_UB_model_per_115.tmp_lst:
            box_UB_model_per_115.addItem(lst_itm)
        box_UB_model_per_115.setCurrentIndex(2)
        box_UB_model_per_115.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_UB_model_per_115.addWidget(box_UB_model_per_115)
        bg_box.addLayout(hbox_lay_UB_model_per_115)


        label_116 = QLabel("        detector")
        label_116.setPalette(palette_scope)
        label_116.setFont(QFont("Monospace"))
        bg_box.addWidget(label_116)

        hbox_lay_panels_117 =  QHBoxLayout()
        label_panels_117 = QLabel("            panels")
        label_panels_117.setPalette(palette_object)
        label_panels_117.setFont(QFont("Monospace"))
        hbox_lay_panels_117.addWidget(label_panels_117)

        box_panels_117 = QComboBox()
        box_panels_117.local_path = "refinement.parameterisation.detector.panels"
        box_panels_117.tmp_lst=[]
        box_panels_117.tmp_lst.append("automatic")
        box_panels_117.tmp_lst.append("single")
        box_panels_117.tmp_lst.append("multiple")
        box_panels_117.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_117.tmp_lst:
            box_panels_117.addItem(lst_itm)
        box_panels_117.setCurrentIndex(0)
        box_panels_117.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_117.addWidget(box_panels_117)
        bg_box.addLayout(hbox_lay_panels_117)


        hbox_lay_hierarchy_level_118 =  QHBoxLayout()
        label_hierarchy_level_118 = QLabel("            hierarchy_level")
        label_hierarchy_level_118.setPalette(palette_object)
        label_hierarchy_level_118.setFont(QFont("Monospace"))
        hbox_lay_hierarchy_level_118.addWidget(label_hierarchy_level_118)

        box_hierarchy_level_118 = QSpinBox()
        box_hierarchy_level_118.setValue(0)
        box_hierarchy_level_118.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_118.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_118.addWidget(box_hierarchy_level_118)
        bg_box.addLayout(hbox_lay_hierarchy_level_118)


        hbox_lay_fix_119 =  QHBoxLayout()
        label_fix_119 = QLabel("            fix")
        label_fix_119.setPalette(palette_object)
        label_fix_119.setFont(QFont("Monospace"))
        hbox_lay_fix_119.addWidget(label_fix_119)

        box_fix_119 = QComboBox()
        box_fix_119.local_path = "refinement.parameterisation.detector.fix"
        box_fix_119.tmp_lst=[]
        box_fix_119.tmp_lst.append("all")
        box_fix_119.tmp_lst.append("position")
        box_fix_119.tmp_lst.append("orientation")
        for lst_itm in box_fix_119.tmp_lst:
            box_fix_119.addItem(lst_itm)
        box_fix_119.setCurrentIndex(0)
        box_fix_119.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_119.addWidget(box_fix_119)
        bg_box.addLayout(hbox_lay_fix_119)



        hbox_lay_sparse_121 =  QHBoxLayout()
        label_sparse_121 = QLabel("        sparse")
        label_sparse_121.setPalette(palette_object)
        label_sparse_121.setFont(QFont("Monospace"))
        hbox_lay_sparse_121.addWidget(label_sparse_121)

        box_sparse_121 = QComboBox()
        box_sparse_121.local_path = "refinement.parameterisation.sparse"
        box_sparse_121.tmp_lst=[]
        box_sparse_121.tmp_lst.append("True")
        box_sparse_121.tmp_lst.append("False")
        for lst_itm in box_sparse_121.tmp_lst:
            box_sparse_121.addItem(lst_itm)
        box_sparse_121.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_121.addWidget(box_sparse_121)
        bg_box.addLayout(hbox_lay_sparse_121)


        hbox_lay_treat_single_image_as_still_122 =  QHBoxLayout()
        label_treat_single_image_as_still_122 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_122.setPalette(palette_object)
        label_treat_single_image_as_still_122.setFont(QFont("Monospace"))
        hbox_lay_treat_single_image_as_still_122.addWidget(label_treat_single_image_as_still_122)

        box_treat_single_image_as_still_122 = QComboBox()
        box_treat_single_image_as_still_122.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_122.tmp_lst=[]
        box_treat_single_image_as_still_122.tmp_lst.append("True")
        box_treat_single_image_as_still_122.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_122.tmp_lst:
            box_treat_single_image_as_still_122.addItem(lst_itm)
        box_treat_single_image_as_still_122.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_122.addWidget(box_treat_single_image_as_still_122)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_122)


        label_123 = QLabel("    refinery")
        label_123.setPalette(palette_scope)
        label_123.setFont(QFont("Monospace"))
        bg_box.addWidget(label_123)

        hbox_lay_engine_124 =  QHBoxLayout()
        label_engine_124 = QLabel("        engine")
        label_engine_124.setPalette(palette_object)
        label_engine_124.setFont(QFont("Monospace"))
        hbox_lay_engine_124.addWidget(label_engine_124)

        box_engine_124 = QComboBox()
        box_engine_124.local_path = "refinement.refinery.engine"
        box_engine_124.tmp_lst=[]
        box_engine_124.tmp_lst.append("SimpleLBFGS")
        box_engine_124.tmp_lst.append("LBFGScurvs")
        box_engine_124.tmp_lst.append("GaussNewton")
        box_engine_124.tmp_lst.append("LevMar")
        for lst_itm in box_engine_124.tmp_lst:
            box_engine_124.addItem(lst_itm)
        box_engine_124.setCurrentIndex(3)
        box_engine_124.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_124.addWidget(box_engine_124)
        bg_box.addLayout(hbox_lay_engine_124)


        hbox_lay_track_step_125 =  QHBoxLayout()
        label_track_step_125 = QLabel("        track_step")
        label_track_step_125.setPalette(palette_object)
        label_track_step_125.setFont(QFont("Monospace"))
        hbox_lay_track_step_125.addWidget(label_track_step_125)

        box_track_step_125 = QComboBox()
        box_track_step_125.local_path = "refinement.refinery.track_step"
        box_track_step_125.tmp_lst=[]
        box_track_step_125.tmp_lst.append("True")
        box_track_step_125.tmp_lst.append("False")
        for lst_itm in box_track_step_125.tmp_lst:
            box_track_step_125.addItem(lst_itm)
        box_track_step_125.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_125.addWidget(box_track_step_125)
        bg_box.addLayout(hbox_lay_track_step_125)


        hbox_lay_track_gradient_126 =  QHBoxLayout()
        label_track_gradient_126 = QLabel("        track_gradient")
        label_track_gradient_126.setPalette(palette_object)
        label_track_gradient_126.setFont(QFont("Monospace"))
        hbox_lay_track_gradient_126.addWidget(label_track_gradient_126)

        box_track_gradient_126 = QComboBox()
        box_track_gradient_126.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_126.tmp_lst=[]
        box_track_gradient_126.tmp_lst.append("True")
        box_track_gradient_126.tmp_lst.append("False")
        for lst_itm in box_track_gradient_126.tmp_lst:
            box_track_gradient_126.addItem(lst_itm)
        box_track_gradient_126.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_126.addWidget(box_track_gradient_126)
        bg_box.addLayout(hbox_lay_track_gradient_126)


        hbox_lay_track_parameter_correlation_127 =  QHBoxLayout()
        label_track_parameter_correlation_127 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_127.setPalette(palette_object)
        label_track_parameter_correlation_127.setFont(QFont("Monospace"))
        hbox_lay_track_parameter_correlation_127.addWidget(label_track_parameter_correlation_127)

        box_track_parameter_correlation_127 = QComboBox()
        box_track_parameter_correlation_127.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_127.tmp_lst=[]
        box_track_parameter_correlation_127.tmp_lst.append("True")
        box_track_parameter_correlation_127.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_127.tmp_lst:
            box_track_parameter_correlation_127.addItem(lst_itm)
        box_track_parameter_correlation_127.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_127.addWidget(box_track_parameter_correlation_127)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_127)


        hbox_lay_track_out_of_sample_rmsd_128 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_128 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_128.setPalette(palette_object)
        label_track_out_of_sample_rmsd_128.setFont(QFont("Monospace"))
        hbox_lay_track_out_of_sample_rmsd_128.addWidget(label_track_out_of_sample_rmsd_128)

        box_track_out_of_sample_rmsd_128 = QComboBox()
        box_track_out_of_sample_rmsd_128.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_128.tmp_lst=[]
        box_track_out_of_sample_rmsd_128.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_128.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_128.tmp_lst:
            box_track_out_of_sample_rmsd_128.addItem(lst_itm)
        box_track_out_of_sample_rmsd_128.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_128.addWidget(box_track_out_of_sample_rmsd_128)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_128)



        hbox_lay_max_iterations_130 =  QHBoxLayout()
        label_max_iterations_130 = QLabel("        max_iterations")
        label_max_iterations_130.setPalette(palette_object)
        label_max_iterations_130.setFont(QFont("Monospace"))
        hbox_lay_max_iterations_130.addWidget(label_max_iterations_130)

        box_max_iterations_130 = QSpinBox()
        box_max_iterations_130.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_130.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_130.addWidget(box_max_iterations_130)
        bg_box.addLayout(hbox_lay_max_iterations_130)


        label_131 = QLabel("    target")
        label_131.setPalette(palette_scope)
        label_131.setFont(QFont("Monospace"))
        bg_box.addWidget(label_131)

        hbox_lay_rmsd_cutoff_132 =  QHBoxLayout()
        label_rmsd_cutoff_132 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_132.setPalette(palette_object)
        label_rmsd_cutoff_132.setFont(QFont("Monospace"))
        hbox_lay_rmsd_cutoff_132.addWidget(label_rmsd_cutoff_132)

        box_rmsd_cutoff_132 = QComboBox()
        box_rmsd_cutoff_132.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_132.tmp_lst=[]
        box_rmsd_cutoff_132.tmp_lst.append("fraction_of_bin_size")
        box_rmsd_cutoff_132.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_132.tmp_lst:
            box_rmsd_cutoff_132.addItem(lst_itm)
        box_rmsd_cutoff_132.setCurrentIndex(0)
        box_rmsd_cutoff_132.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_132.addWidget(box_rmsd_cutoff_132)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_132)


        hbox_lay_bin_size_fraction_133 =  QHBoxLayout()
        label_bin_size_fraction_133 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_133.setPalette(palette_object)
        label_bin_size_fraction_133.setFont(QFont("Monospace"))
        hbox_lay_bin_size_fraction_133.addWidget(label_bin_size_fraction_133)

        box_bin_size_fraction_133 = QDoubleSpinBox()
        box_bin_size_fraction_133.setValue(0.2)
        box_bin_size_fraction_133.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_133.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_133.addWidget(box_bin_size_fraction_133)
        bg_box.addLayout(hbox_lay_bin_size_fraction_133)


        hbox_lay_absolute_cutoffs_134_0 =  QHBoxLayout()
        label_absolute_cutoffs_134_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_134_0.setPalette(palette_object)
        label_absolute_cutoffs_134_0.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_134_0.addWidget(label_absolute_cutoffs_134_0)
        box_absolute_cutoffs_134_0 = QDoubleSpinBox()
        box_absolute_cutoffs_134_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_134_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_134_1 =  QHBoxLayout()
        label_absolute_cutoffs_134_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_134_1.setPalette(palette_object)
        label_absolute_cutoffs_134_1.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_134_1.addWidget(label_absolute_cutoffs_134_1)
        box_absolute_cutoffs_134_1 = QDoubleSpinBox()
        box_absolute_cutoffs_134_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_134_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_134_2 =  QHBoxLayout()
        label_absolute_cutoffs_134_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_134_2.setPalette(palette_object)
        label_absolute_cutoffs_134_2.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_134_2.addWidget(label_absolute_cutoffs_134_2)
        box_absolute_cutoffs_134_2 = QDoubleSpinBox()
        box_absolute_cutoffs_134_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_134_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_134_0.addWidget(box_absolute_cutoffs_134_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_134_0)

        hbox_lay_absolute_cutoffs_134_1.addWidget(box_absolute_cutoffs_134_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_134_1)

        hbox_lay_absolute_cutoffs_134_2.addWidget(box_absolute_cutoffs_134_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_134_2)


        hbox_lay_gradient_calculation_blocksize_135 =  QHBoxLayout()
        label_gradient_calculation_blocksize_135 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_135.setPalette(palette_object)
        label_gradient_calculation_blocksize_135.setFont(QFont("Monospace"))
        hbox_lay_gradient_calculation_blocksize_135.addWidget(label_gradient_calculation_blocksize_135)

        box_gradient_calculation_blocksize_135 = QSpinBox()
        box_gradient_calculation_blocksize_135.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_135.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_135.addWidget(box_gradient_calculation_blocksize_135)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_135)


        label_136 = QLabel("    reflections")
        label_136.setPalette(palette_scope)
        label_136.setFont(QFont("Monospace"))
        bg_box.addWidget(label_136)

        hbox_lay_reflections_per_degree_137 =  QHBoxLayout()
        label_reflections_per_degree_137 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_137.setPalette(palette_object)
        label_reflections_per_degree_137.setFont(QFont("Monospace"))
        hbox_lay_reflections_per_degree_137.addWidget(label_reflections_per_degree_137)

        box_reflections_per_degree_137 = QDoubleSpinBox()
        box_reflections_per_degree_137.setValue(100.0)
        box_reflections_per_degree_137.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_137.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_137.addWidget(box_reflections_per_degree_137)
        bg_box.addLayout(hbox_lay_reflections_per_degree_137)


        hbox_lay_minimum_sample_size_138 =  QHBoxLayout()
        label_minimum_sample_size_138 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_138.setPalette(palette_object)
        label_minimum_sample_size_138.setFont(QFont("Monospace"))
        hbox_lay_minimum_sample_size_138.addWidget(label_minimum_sample_size_138)

        box_minimum_sample_size_138 = QSpinBox()
        box_minimum_sample_size_138.setValue(1000)
        box_minimum_sample_size_138.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_138.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_138.addWidget(box_minimum_sample_size_138)
        bg_box.addLayout(hbox_lay_minimum_sample_size_138)


        hbox_lay_maximum_sample_size_139 =  QHBoxLayout()
        label_maximum_sample_size_139 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_139.setPalette(palette_object)
        label_maximum_sample_size_139.setFont(QFont("Monospace"))
        hbox_lay_maximum_sample_size_139.addWidget(label_maximum_sample_size_139)

        box_maximum_sample_size_139 = QSpinBox()
        box_maximum_sample_size_139.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_139.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_139.addWidget(box_maximum_sample_size_139)
        bg_box.addLayout(hbox_lay_maximum_sample_size_139)


        hbox_lay_use_all_reflections_140 =  QHBoxLayout()
        label_use_all_reflections_140 = QLabel("        use_all_reflections")
        label_use_all_reflections_140.setPalette(palette_object)
        label_use_all_reflections_140.setFont(QFont("Monospace"))
        hbox_lay_use_all_reflections_140.addWidget(label_use_all_reflections_140)

        box_use_all_reflections_140 = QComboBox()
        box_use_all_reflections_140.local_path = "refinement.reflections.use_all_reflections"
        box_use_all_reflections_140.tmp_lst=[]
        box_use_all_reflections_140.tmp_lst.append("True")
        box_use_all_reflections_140.tmp_lst.append("False")
        for lst_itm in box_use_all_reflections_140.tmp_lst:
            box_use_all_reflections_140.addItem(lst_itm)
        box_use_all_reflections_140.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_use_all_reflections_140.addWidget(box_use_all_reflections_140)
        bg_box.addLayout(hbox_lay_use_all_reflections_140)


        hbox_lay_random_seed_141 =  QHBoxLayout()
        label_random_seed_141 = QLabel("        random_seed")
        label_random_seed_141.setPalette(palette_object)
        label_random_seed_141.setFont(QFont("Monospace"))
        hbox_lay_random_seed_141.addWidget(label_random_seed_141)

        box_random_seed_141 = QSpinBox()
        box_random_seed_141.setValue(42)
        box_random_seed_141.local_path = "refinement.reflections.random_seed"
        box_random_seed_141.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_141.addWidget(box_random_seed_141)
        bg_box.addLayout(hbox_lay_random_seed_141)


        hbox_lay_close_to_spindle_cutoff_142 =  QHBoxLayout()
        label_close_to_spindle_cutoff_142 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_142.setPalette(palette_object)
        label_close_to_spindle_cutoff_142.setFont(QFont("Monospace"))
        hbox_lay_close_to_spindle_cutoff_142.addWidget(label_close_to_spindle_cutoff_142)

        box_close_to_spindle_cutoff_142 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_142.setValue(0.02)
        box_close_to_spindle_cutoff_142.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_142.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_142.addWidget(box_close_to_spindle_cutoff_142)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_142)


        hbox_lay_block_width_143 =  QHBoxLayout()
        label_block_width_143 = QLabel("        block_width")
        label_block_width_143.setPalette(palette_object)
        label_block_width_143.setFont(QFont("Monospace"))
        hbox_lay_block_width_143.addWidget(label_block_width_143)

        box_block_width_143 = QDoubleSpinBox()
        box_block_width_143.setValue(1.0)
        box_block_width_143.local_path = "refinement.reflections.block_width"
        box_block_width_143.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_143.addWidget(box_block_width_143)
        bg_box.addLayout(hbox_lay_block_width_143)


        label_144 = QLabel("        weighting_strategy")
        label_144.setPalette(palette_scope)
        label_144.setFont(QFont("Monospace"))
        bg_box.addWidget(label_144)

        hbox_lay_override_145 =  QHBoxLayout()
        label_override_145 = QLabel("            override")
        label_override_145.setPalette(palette_object)
        label_override_145.setFont(QFont("Monospace"))
        hbox_lay_override_145.addWidget(label_override_145)

        box_override_145 = QComboBox()
        box_override_145.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_145.tmp_lst=[]
        box_override_145.tmp_lst.append("statistical")
        box_override_145.tmp_lst.append("stills")
        box_override_145.tmp_lst.append("constant")
        for lst_itm in box_override_145.tmp_lst:
            box_override_145.addItem(lst_itm)
        box_override_145.setCurrentIndex(0)
        box_override_145.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_145.addWidget(box_override_145)
        bg_box.addLayout(hbox_lay_override_145)


        hbox_lay_delpsi_constant_146 =  QHBoxLayout()
        label_delpsi_constant_146 = QLabel("            delpsi_constant")
        label_delpsi_constant_146.setPalette(palette_object)
        label_delpsi_constant_146.setFont(QFont("Monospace"))
        hbox_lay_delpsi_constant_146.addWidget(label_delpsi_constant_146)

        box_delpsi_constant_146 = QDoubleSpinBox()
        box_delpsi_constant_146.setValue(10000.0)
        box_delpsi_constant_146.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_146.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_146.addWidget(box_delpsi_constant_146)
        bg_box.addLayout(hbox_lay_delpsi_constant_146)


        hbox_lay_constants_147_0 =  QHBoxLayout()
        label_constants_147_0 = QLabel("            constants[1]")
        label_constants_147_0.setPalette(palette_object)
        label_constants_147_0.setFont(QFont("Monospace"))
        hbox_lay_constants_147_0.addWidget(label_constants_147_0)
        box_constants_147_0 = QDoubleSpinBox()
        box_constants_147_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_147_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_147_1 =  QHBoxLayout()
        label_constants_147_1 = QLabel("            constants[2]")
        label_constants_147_1.setPalette(palette_object)
        label_constants_147_1.setFont(QFont("Monospace"))
        hbox_lay_constants_147_1.addWidget(label_constants_147_1)
        box_constants_147_1 = QDoubleSpinBox()
        box_constants_147_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_147_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_147_2 =  QHBoxLayout()
        label_constants_147_2 = QLabel("            constants[3]")
        label_constants_147_2.setPalette(palette_object)
        label_constants_147_2.setFont(QFont("Monospace"))
        hbox_lay_constants_147_2.addWidget(label_constants_147_2)
        box_constants_147_2 = QDoubleSpinBox()
        box_constants_147_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_147_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_147_0.addWidget(box_constants_147_0)
        bg_box.addLayout(hbox_lay_constants_147_0)

        hbox_lay_constants_147_1.addWidget(box_constants_147_1)
        bg_box.addLayout(hbox_lay_constants_147_1)

        hbox_lay_constants_147_2.addWidget(box_constants_147_2)
        bg_box.addLayout(hbox_lay_constants_147_2)


        label_148 = QLabel("        outlier")
        label_148.setPalette(palette_scope)
        label_148.setFont(QFont("Monospace"))
        bg_box.addWidget(label_148)

        hbox_lay_algorithm_149 =  QHBoxLayout()
        label_algorithm_149 = QLabel("            algorithm")
        label_algorithm_149.setPalette(palette_object)
        label_algorithm_149.setFont(QFont("Monospace"))
        hbox_lay_algorithm_149.addWidget(label_algorithm_149)

        box_algorithm_149 = QComboBox()
        box_algorithm_149.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_149.tmp_lst=[]
        box_algorithm_149.tmp_lst.append("null")
        box_algorithm_149.tmp_lst.append("auto")
        box_algorithm_149.tmp_lst.append("mcd")
        box_algorithm_149.tmp_lst.append("tukey")
        box_algorithm_149.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_149.tmp_lst:
            box_algorithm_149.addItem(lst_itm)
        box_algorithm_149.setCurrentIndex(1)
        box_algorithm_149.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_149.addWidget(box_algorithm_149)
        bg_box.addLayout(hbox_lay_algorithm_149)


        hbox_lay_minimum_number_of_reflections_150 =  QHBoxLayout()
        label_minimum_number_of_reflections_150 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_150.setPalette(palette_object)
        label_minimum_number_of_reflections_150.setFont(QFont("Monospace"))
        hbox_lay_minimum_number_of_reflections_150.addWidget(label_minimum_number_of_reflections_150)

        box_minimum_number_of_reflections_150 = QSpinBox()
        box_minimum_number_of_reflections_150.setValue(20)
        box_minimum_number_of_reflections_150.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_150.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_150.addWidget(box_minimum_number_of_reflections_150)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_150)


        hbox_lay_separate_experiments_151 =  QHBoxLayout()
        label_separate_experiments_151 = QLabel("            separate_experiments")
        label_separate_experiments_151.setPalette(palette_object)
        label_separate_experiments_151.setFont(QFont("Monospace"))
        hbox_lay_separate_experiments_151.addWidget(label_separate_experiments_151)

        box_separate_experiments_151 = QComboBox()
        box_separate_experiments_151.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_151.tmp_lst=[]
        box_separate_experiments_151.tmp_lst.append("True")
        box_separate_experiments_151.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_151.tmp_lst:
            box_separate_experiments_151.addItem(lst_itm)
        box_separate_experiments_151.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_151.addWidget(box_separate_experiments_151)
        bg_box.addLayout(hbox_lay_separate_experiments_151)


        hbox_lay_separate_panels_152 =  QHBoxLayout()
        label_separate_panels_152 = QLabel("            separate_panels")
        label_separate_panels_152.setPalette(palette_object)
        label_separate_panels_152.setFont(QFont("Monospace"))
        hbox_lay_separate_panels_152.addWidget(label_separate_panels_152)

        box_separate_panels_152 = QComboBox()
        box_separate_panels_152.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_152.tmp_lst=[]
        box_separate_panels_152.tmp_lst.append("True")
        box_separate_panels_152.tmp_lst.append("False")
        for lst_itm in box_separate_panels_152.tmp_lst:
            box_separate_panels_152.addItem(lst_itm)
        box_separate_panels_152.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_152.addWidget(box_separate_panels_152)
        bg_box.addLayout(hbox_lay_separate_panels_152)


        label_153 = QLabel("            tukey")
        label_153.setPalette(palette_scope)
        label_153.setFont(QFont("Monospace"))
        bg_box.addWidget(label_153)

        hbox_lay_iqr_multiplier_154 =  QHBoxLayout()
        label_iqr_multiplier_154 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_154.setPalette(palette_object)
        label_iqr_multiplier_154.setFont(QFont("Monospace"))
        hbox_lay_iqr_multiplier_154.addWidget(label_iqr_multiplier_154)

        box_iqr_multiplier_154 = QDoubleSpinBox()
        box_iqr_multiplier_154.setValue(1.5)
        box_iqr_multiplier_154.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_154.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_154.addWidget(box_iqr_multiplier_154)
        bg_box.addLayout(hbox_lay_iqr_multiplier_154)


        label_155 = QLabel("            mcd")
        label_155.setPalette(palette_scope)
        label_155.setFont(QFont("Monospace"))
        bg_box.addWidget(label_155)

        hbox_lay_alpha_156 =  QHBoxLayout()
        label_alpha_156 = QLabel("                alpha")
        label_alpha_156.setPalette(palette_object)
        label_alpha_156.setFont(QFont("Monospace"))
        hbox_lay_alpha_156.addWidget(label_alpha_156)

        box_alpha_156 = QDoubleSpinBox()
        box_alpha_156.setValue(0.5)
        box_alpha_156.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_156.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_156.addWidget(box_alpha_156)
        bg_box.addLayout(hbox_lay_alpha_156)


        hbox_lay_max_n_groups_157 =  QHBoxLayout()
        label_max_n_groups_157 = QLabel("                max_n_groups")
        label_max_n_groups_157.setPalette(palette_object)
        label_max_n_groups_157.setFont(QFont("Monospace"))
        hbox_lay_max_n_groups_157.addWidget(label_max_n_groups_157)

        box_max_n_groups_157 = QSpinBox()
        box_max_n_groups_157.setValue(5)
        box_max_n_groups_157.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_157.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_157.addWidget(box_max_n_groups_157)
        bg_box.addLayout(hbox_lay_max_n_groups_157)


        hbox_lay_min_group_size_158 =  QHBoxLayout()
        label_min_group_size_158 = QLabel("                min_group_size")
        label_min_group_size_158.setPalette(palette_object)
        label_min_group_size_158.setFont(QFont("Monospace"))
        hbox_lay_min_group_size_158.addWidget(label_min_group_size_158)

        box_min_group_size_158 = QSpinBox()
        box_min_group_size_158.setValue(300)
        box_min_group_size_158.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_158.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_158.addWidget(box_min_group_size_158)
        bg_box.addLayout(hbox_lay_min_group_size_158)


        hbox_lay_n_trials_159 =  QHBoxLayout()
        label_n_trials_159 = QLabel("                n_trials")
        label_n_trials_159.setPalette(palette_object)
        label_n_trials_159.setFont(QFont("Monospace"))
        hbox_lay_n_trials_159.addWidget(label_n_trials_159)

        box_n_trials_159 = QSpinBox()
        box_n_trials_159.setValue(500)
        box_n_trials_159.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_159.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_159.addWidget(box_n_trials_159)
        bg_box.addLayout(hbox_lay_n_trials_159)


        hbox_lay_k1_160 =  QHBoxLayout()
        label_k1_160 = QLabel("                k1")
        label_k1_160.setPalette(palette_object)
        label_k1_160.setFont(QFont("Monospace"))
        hbox_lay_k1_160.addWidget(label_k1_160)

        box_k1_160 = QSpinBox()
        box_k1_160.setValue(2)
        box_k1_160.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_160.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_160.addWidget(box_k1_160)
        bg_box.addLayout(hbox_lay_k1_160)


        hbox_lay_k2_161 =  QHBoxLayout()
        label_k2_161 = QLabel("                k2")
        label_k2_161.setPalette(palette_object)
        label_k2_161.setFont(QFont("Monospace"))
        hbox_lay_k2_161.addWidget(label_k2_161)

        box_k2_161 = QSpinBox()
        box_k2_161.setValue(2)
        box_k2_161.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_161.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_161.addWidget(box_k2_161)
        bg_box.addLayout(hbox_lay_k2_161)


        hbox_lay_k3_162 =  QHBoxLayout()
        label_k3_162 = QLabel("                k3")
        label_k3_162.setPalette(palette_object)
        label_k3_162.setFont(QFont("Monospace"))
        hbox_lay_k3_162.addWidget(label_k3_162)

        box_k3_162 = QSpinBox()
        box_k3_162.setValue(100)
        box_k3_162.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_162.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_162.addWidget(box_k3_162)
        bg_box.addLayout(hbox_lay_k3_162)


        hbox_lay_threshold_probability_163 =  QHBoxLayout()
        label_threshold_probability_163 = QLabel("                threshold_probability")
        label_threshold_probability_163.setPalette(palette_object)
        label_threshold_probability_163.setFont(QFont("Monospace"))
        hbox_lay_threshold_probability_163.addWidget(label_threshold_probability_163)

        box_threshold_probability_163 = QDoubleSpinBox()
        box_threshold_probability_163.setValue(0.975)
        box_threshold_probability_163.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_163.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_163.addWidget(box_threshold_probability_163)
        bg_box.addLayout(hbox_lay_threshold_probability_163)


        label_164 = QLabel("            sauter_poon")
        label_164.setPalette(palette_scope)
        label_164.setFont(QFont("Monospace"))
        bg_box.addWidget(label_164)

        hbox_lay_px_sz_165_0 =  QHBoxLayout()
        label_px_sz_165_0 = QLabel("                px_sz[1]")
        label_px_sz_165_0.setPalette(palette_object)
        label_px_sz_165_0.setFont(QFont("Monospace"))
        hbox_lay_px_sz_165_0.addWidget(label_px_sz_165_0)
        box_px_sz_165_0 = QDoubleSpinBox()
        box_px_sz_165_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_165_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_165_1 =  QHBoxLayout()
        label_px_sz_165_1 = QLabel("                px_sz[2]")
        label_px_sz_165_1.setPalette(palette_object)
        label_px_sz_165_1.setFont(QFont("Monospace"))
        hbox_lay_px_sz_165_1.addWidget(label_px_sz_165_1)
        box_px_sz_165_1 = QDoubleSpinBox()
        box_px_sz_165_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_165_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_165_0.addWidget(box_px_sz_165_0)
        bg_box.addLayout(hbox_lay_px_sz_165_0)

        hbox_lay_px_sz_165_1.addWidget(box_px_sz_165_1)
        bg_box.addLayout(hbox_lay_px_sz_165_1)


        hbox_lay_verbose_166 =  QHBoxLayout()
        label_verbose_166 = QLabel("                verbose")
        label_verbose_166.setPalette(palette_object)
        label_verbose_166.setFont(QFont("Monospace"))
        hbox_lay_verbose_166.addWidget(label_verbose_166)

        box_verbose_166 = QComboBox()
        box_verbose_166.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_166.tmp_lst=[]
        box_verbose_166.tmp_lst.append("True")
        box_verbose_166.tmp_lst.append("False")
        for lst_itm in box_verbose_166.tmp_lst:
            box_verbose_166.addItem(lst_itm)
        box_verbose_166.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_166.addWidget(box_verbose_166)
        bg_box.addLayout(hbox_lay_verbose_166)


        hbox_lay_pdf_167 =  QHBoxLayout()
        label_pdf_167 = QLabel("                pdf")
        label_pdf_167.setPalette(palette_object)
        label_pdf_167.setFont(QFont("Monospace"))
        hbox_lay_pdf_167.addWidget(label_pdf_167)

        box_pdf_167 = QLineEdit()
        box_pdf_167.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_167.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_167.addWidget(box_pdf_167)
        bg_box.addLayout(hbox_lay_pdf_167)


        label_168 = QLabel("output")
        label_168.setPalette(palette_scope)
        label_168.setFont(QFont("Monospace"))
        bg_box.addWidget(label_168)




        hbox_lay_log_172 =  QHBoxLayout()
        label_log_172 = QLabel("    log")
        label_log_172.setPalette(palette_object)
        label_log_172.setFont(QFont("Monospace"))
        hbox_lay_log_172.addWidget(label_log_172)

        box_log_172 = QLineEdit()
        box_log_172.local_path = "output.log"
        box_log_172.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_172.addWidget(box_log_172)
        bg_box.addLayout(hbox_lay_log_172)


        hbox_lay_debug_log_173 =  QHBoxLayout()
        label_debug_log_173 = QLabel("    debug_log")
        label_debug_log_173.setPalette(palette_object)
        label_debug_log_173.setFont(QFont("Monospace"))
        hbox_lay_debug_log_173.addWidget(label_debug_log_173)

        box_debug_log_173 = QLineEdit()
        box_debug_log_173.local_path = "output.debug_log"
        box_debug_log_173.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_173.addWidget(box_debug_log_173)
        bg_box.addLayout(hbox_lay_debug_log_173)


        hbox_lay_verbosity_174 =  QHBoxLayout()
        label_verbosity_174 = QLabel("verbosity")
        label_verbosity_174.setPalette(palette_object)
        label_verbosity_174.setFont(QFont("Monospace"))
        hbox_lay_verbosity_174.addWidget(label_verbosity_174)

        box_verbosity_174 = QSpinBox()
        box_verbosity_174.setValue(1)
        box_verbosity_174.local_path = "verbosity"
        box_verbosity_174.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_174.addWidget(box_verbosity_174)
        bg_box.addLayout(hbox_lay_verbosity_174)


 
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
