import sys
#PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
print "using PyQt4"
#'''
PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
pyqtSignal = Signal
print "using PySide"
#'''


class inner_widg( QWidget):
    item_changed = pyqtSignal()
    def __init__(self, parent):
        super(inner_widg, self).__init__()
        bg_box =  QVBoxLayout(self)


        label_0 = QLabel("indexing")
        label_0.setFont(QFont("Monospace", 14, QFont.Bold))
        bg_box.addWidget(label_0)
        hbox_nproc_1 =  QHBoxLayout()
        label_nproc_1 = QLabel("        nproc")
        label_nproc_1.setFont(QFont("Times",16, QFont.Bold))
        hbox_nproc_1.addWidget(label_nproc_1)

        box_nproc_1 = QSpinBox()
        box_nproc_1.local_path = "dummy path"
        box_nproc_1.valueChanged.connect(self.spnbox_changed)

        hbox_nproc_1.addWidget(box_nproc_1)
        bg_box.addLayout(hbox_nproc_1)
        hbox_discover_better_experimental_model_2 =  QHBoxLayout()
        label_discover_better_experimental_model_2 = QLabel("        discover_better_experimental_model")
        label_discover_better_experimental_model_2.setFont(QFont("Times",16, QFont.Bold))
        hbox_discover_better_experimental_model_2.addWidget(label_discover_better_experimental_model_2)

        box_discover_better_experimental_model_2 = QComboBox()
        box_discover_better_experimental_model_2.tmp_lst=[]
        box_discover_better_experimental_model_2.tmp_lst.append("True")
        box_discover_better_experimental_model_2.tmp_lst.append("False")
        for lst_itm in box_discover_better_experimental_model_2.tmp_lst:
            box_discover_better_experimental_model_2.addItem(lst_itm)
        box_discover_better_experimental_model_2.currentIndexChanged.connect(self.combobox_changed)

        hbox_discover_better_experimental_model_2.addWidget(box_discover_better_experimental_model_2)
        bg_box.addLayout(hbox_discover_better_experimental_model_2)
        hbox_mm_search_scope_3 =  QHBoxLayout()
        label_mm_search_scope_3 = QLabel("        mm_search_scope")
        label_mm_search_scope_3.setFont(QFont("Times",16, QFont.Bold))
        hbox_mm_search_scope_3.addWidget(label_mm_search_scope_3)

        box_mm_search_scope_3 = QDoubleSpinBox()
        box_mm_search_scope_3.local_path = "dummy path"
        box_mm_search_scope_3.valueChanged.connect(self.spnbox_changed)

        hbox_mm_search_scope_3.addWidget(box_mm_search_scope_3)
        bg_box.addLayout(hbox_mm_search_scope_3)
        hbox_wide_search_binning_4 =  QHBoxLayout()
        label_wide_search_binning_4 = QLabel("        wide_search_binning")
        label_wide_search_binning_4.setFont(QFont("Times",16, QFont.Bold))
        hbox_wide_search_binning_4.addWidget(label_wide_search_binning_4)

        box_wide_search_binning_4 = QDoubleSpinBox()
        box_wide_search_binning_4.local_path = "dummy path"
        box_wide_search_binning_4.valueChanged.connect(self.spnbox_changed)

        hbox_wide_search_binning_4.addWidget(box_wide_search_binning_4)
        bg_box.addLayout(hbox_wide_search_binning_4)
        hbox_min_cell_5 =  QHBoxLayout()
        label_min_cell_5 = QLabel("        min_cell")
        label_min_cell_5.setFont(QFont("Times",16, QFont.Bold))
        hbox_min_cell_5.addWidget(label_min_cell_5)

        box_min_cell_5 = QDoubleSpinBox()
        box_min_cell_5.local_path = "dummy path"
        box_min_cell_5.valueChanged.connect(self.spnbox_changed)

        hbox_min_cell_5.addWidget(box_min_cell_5)
        bg_box.addLayout(hbox_min_cell_5)
        hbox_max_cell_6 =  QHBoxLayout()
        label_max_cell_6 = QLabel("        max_cell")
        label_max_cell_6.setFont(QFont("Times",16, QFont.Bold))
        hbox_max_cell_6.addWidget(label_max_cell_6)

        box_max_cell_6 = QDoubleSpinBox()
        box_max_cell_6.local_path = "dummy path"
        box_max_cell_6.valueChanged.connect(self.spnbox_changed)

        hbox_max_cell_6.addWidget(box_max_cell_6)
        bg_box.addLayout(hbox_max_cell_6)
        hbox_max_cell_multiplier_7 =  QHBoxLayout()
        label_max_cell_multiplier_7 = QLabel("        max_cell_multiplier")
        label_max_cell_multiplier_7.setFont(QFont("Times",16, QFont.Bold))
        hbox_max_cell_multiplier_7.addWidget(label_max_cell_multiplier_7)

        box_max_cell_multiplier_7 = QDoubleSpinBox()
        box_max_cell_multiplier_7.local_path = "dummy path"
        box_max_cell_multiplier_7.valueChanged.connect(self.spnbox_changed)

        hbox_max_cell_multiplier_7.addWidget(box_max_cell_multiplier_7)
        bg_box.addLayout(hbox_max_cell_multiplier_7)
        hbox_nearest_neighbor_percentile_8 =  QHBoxLayout()
        label_nearest_neighbor_percentile_8 = QLabel("        nearest_neighbor_percentile")
        label_nearest_neighbor_percentile_8.setFont(QFont("Times",16, QFont.Bold))
        hbox_nearest_neighbor_percentile_8.addWidget(label_nearest_neighbor_percentile_8)

        box_nearest_neighbor_percentile_8 = QDoubleSpinBox()
        box_nearest_neighbor_percentile_8.local_path = "dummy path"
        box_nearest_neighbor_percentile_8.valueChanged.connect(self.spnbox_changed)

        hbox_nearest_neighbor_percentile_8.addWidget(box_nearest_neighbor_percentile_8)
        bg_box.addLayout(hbox_nearest_neighbor_percentile_8)
        hbox_filter_ice_9 =  QHBoxLayout()
        label_filter_ice_9 = QLabel("        filter_ice")
        label_filter_ice_9.setFont(QFont("Times",16, QFont.Bold))
        hbox_filter_ice_9.addWidget(label_filter_ice_9)

        box_filter_ice_9 = QComboBox()
        box_filter_ice_9.tmp_lst=[]
        box_filter_ice_9.tmp_lst.append("True")
        box_filter_ice_9.tmp_lst.append("False")
        for lst_itm in box_filter_ice_9.tmp_lst:
            box_filter_ice_9.addItem(lst_itm)
        box_filter_ice_9.currentIndexChanged.connect(self.combobox_changed)

        hbox_filter_ice_9.addWidget(box_filter_ice_9)
        bg_box.addLayout(hbox_filter_ice_9)
        label_10 = QLabel("    fft3d")
        label_10.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_10)
        hbox_peak_search_11 =  QHBoxLayout()
        label_peak_search_11 = QLabel("                peak_search")
        label_peak_search_11.setFont(QFont("Times",15, QFont.Bold))
        hbox_peak_search_11.addWidget(label_peak_search_11)

        box_peak_search_11 = QComboBox()
        box_peak_search_11.tmp_lst=[]
        box_peak_search_11.tmp_lst.append("*flood_fill")
        box_peak_search_11.tmp_lst.append("clean")
        for lst_itm in box_peak_search_11.tmp_lst:
            box_peak_search_11.addItem(lst_itm)
        box_peak_search_11.currentIndexChanged.connect(self.combobox_changed)

        hbox_peak_search_11.addWidget(box_peak_search_11)
        bg_box.addLayout(hbox_peak_search_11)
        hbox_peak_volume_cutoff_12 =  QHBoxLayout()
        label_peak_volume_cutoff_12 = QLabel("                peak_volume_cutoff")
        label_peak_volume_cutoff_12.setFont(QFont("Times",15, QFont.Bold))
        hbox_peak_volume_cutoff_12.addWidget(label_peak_volume_cutoff_12)

        box_peak_volume_cutoff_12 = QDoubleSpinBox()
        box_peak_volume_cutoff_12.local_path = "dummy path"
        box_peak_volume_cutoff_12.valueChanged.connect(self.spnbox_changed)

        hbox_peak_volume_cutoff_12.addWidget(box_peak_volume_cutoff_12)
        bg_box.addLayout(hbox_peak_volume_cutoff_12)
        label_13 = QLabel("        reciprocal_space_grid")
        label_13.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_13)
        hbox_n_points_14 =  QHBoxLayout()
        label_n_points_14 = QLabel("                        n_points")
        label_n_points_14.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_points_14.addWidget(label_n_points_14)

        box_n_points_14 = QSpinBox()
        box_n_points_14.local_path = "dummy path"
        box_n_points_14.valueChanged.connect(self.spnbox_changed)

        hbox_n_points_14.addWidget(box_n_points_14)
        bg_box.addLayout(hbox_n_points_14)
        hbox_d_min_15 =  QHBoxLayout()
        label_d_min_15 = QLabel("                        d_min")
        label_d_min_15.setFont(QFont("Times",14, QFont.Bold))
        hbox_d_min_15.addWidget(label_d_min_15)

        box_d_min_15 = QDoubleSpinBox()
        box_d_min_15.local_path = "dummy path"
        box_d_min_15.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_15.addWidget(box_d_min_15)
        bg_box.addLayout(hbox_d_min_15)
        hbox_sigma_phi_deg_16 =  QHBoxLayout()
        label_sigma_phi_deg_16 = QLabel("        sigma_phi_deg")
        label_sigma_phi_deg_16.setFont(QFont("Times",16, QFont.Bold))
        hbox_sigma_phi_deg_16.addWidget(label_sigma_phi_deg_16)

        box_sigma_phi_deg_16 = QDoubleSpinBox()
        box_sigma_phi_deg_16.local_path = "dummy path"
        box_sigma_phi_deg_16.valueChanged.connect(self.spnbox_changed)

        hbox_sigma_phi_deg_16.addWidget(box_sigma_phi_deg_16)
        bg_box.addLayout(hbox_sigma_phi_deg_16)
        hbox_b_iso_17 =  QHBoxLayout()
        label_b_iso_17 = QLabel("        b_iso")
        label_b_iso_17.setFont(QFont("Times",16, QFont.Bold))
        hbox_b_iso_17.addWidget(label_b_iso_17)

        box_b_iso_17 = QDoubleSpinBox()
        box_b_iso_17.local_path = "dummy path"
        box_b_iso_17.valueChanged.connect(self.spnbox_changed)

        hbox_b_iso_17.addWidget(box_b_iso_17)
        bg_box.addLayout(hbox_b_iso_17)
        hbox_rmsd_cutoff_18 =  QHBoxLayout()
        label_rmsd_cutoff_18 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_18.setFont(QFont("Times",16, QFont.Bold))
        hbox_rmsd_cutoff_18.addWidget(label_rmsd_cutoff_18)

        box_rmsd_cutoff_18 = QDoubleSpinBox()
        box_rmsd_cutoff_18.local_path = "dummy path"
        box_rmsd_cutoff_18.valueChanged.connect(self.spnbox_changed)

        hbox_rmsd_cutoff_18.addWidget(box_rmsd_cutoff_18)
        bg_box.addLayout(hbox_rmsd_cutoff_18)
        hbox_scan_range_19 =  QHBoxLayout()
        label_scan_range_19 = QLabel("        scan_range")
        label_scan_range_19.setFont(QFont("Times",16, QFont.Bold))
        hbox_scan_range_19.addWidget(label_scan_range_19)
        label_20 = QLabel("    known_symmetry")
        label_20.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_20)
        hbox_space_group_21 =  QHBoxLayout()
        label_space_group_21 = QLabel("                space_group")
        label_space_group_21.setFont(QFont("Times",15, QFont.Bold))
        hbox_space_group_21.addWidget(label_space_group_21)
        hbox_unit_cell_22 =  QHBoxLayout()
        label_unit_cell_22 = QLabel("                unit_cell")
        label_unit_cell_22.setFont(QFont("Times",15, QFont.Bold))
        hbox_unit_cell_22.addWidget(label_unit_cell_22)
        hbox_relative_length_tolerance_23 =  QHBoxLayout()
        label_relative_length_tolerance_23 = QLabel("                relative_length_tolerance")
        label_relative_length_tolerance_23.setFont(QFont("Times",15, QFont.Bold))
        hbox_relative_length_tolerance_23.addWidget(label_relative_length_tolerance_23)

        box_relative_length_tolerance_23 = QDoubleSpinBox()
        box_relative_length_tolerance_23.local_path = "dummy path"
        box_relative_length_tolerance_23.valueChanged.connect(self.spnbox_changed)

        hbox_relative_length_tolerance_23.addWidget(box_relative_length_tolerance_23)
        bg_box.addLayout(hbox_relative_length_tolerance_23)
        hbox_absolute_angle_tolerance_24 =  QHBoxLayout()
        label_absolute_angle_tolerance_24 = QLabel("                absolute_angle_tolerance")
        label_absolute_angle_tolerance_24.setFont(QFont("Times",15, QFont.Bold))
        hbox_absolute_angle_tolerance_24.addWidget(label_absolute_angle_tolerance_24)

        box_absolute_angle_tolerance_24 = QDoubleSpinBox()
        box_absolute_angle_tolerance_24.local_path = "dummy path"
        box_absolute_angle_tolerance_24.valueChanged.connect(self.spnbox_changed)

        hbox_absolute_angle_tolerance_24.addWidget(box_absolute_angle_tolerance_24)
        bg_box.addLayout(hbox_absolute_angle_tolerance_24)
        hbox_max_delta_25 =  QHBoxLayout()
        label_max_delta_25 = QLabel("                max_delta")
        label_max_delta_25.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_delta_25.addWidget(label_max_delta_25)

        box_max_delta_25 = QDoubleSpinBox()
        box_max_delta_25.local_path = "dummy path"
        box_max_delta_25.valueChanged.connect(self.spnbox_changed)

        hbox_max_delta_25.addWidget(box_max_delta_25)
        bg_box.addLayout(hbox_max_delta_25)
        label_26 = QLabel("    basis_vector_combinations")
        label_26.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_26)
        hbox_max_try_27 =  QHBoxLayout()
        label_max_try_27 = QLabel("                max_try")
        label_max_try_27.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_try_27.addWidget(label_max_try_27)

        box_max_try_27 = QSpinBox()
        box_max_try_27.local_path = "dummy path"
        box_max_try_27.valueChanged.connect(self.spnbox_changed)

        hbox_max_try_27.addWidget(box_max_try_27)
        bg_box.addLayout(hbox_max_try_27)
        hbox_solution_scorer_28 =  QHBoxLayout()
        label_solution_scorer_28 = QLabel("                solution_scorer")
        label_solution_scorer_28.setFont(QFont("Times",15, QFont.Bold))
        hbox_solution_scorer_28.addWidget(label_solution_scorer_28)

        box_solution_scorer_28 = QComboBox()
        box_solution_scorer_28.tmp_lst=[]
        box_solution_scorer_28.tmp_lst.append("filter")
        box_solution_scorer_28.tmp_lst.append("*weighted")
        for lst_itm in box_solution_scorer_28.tmp_lst:
            box_solution_scorer_28.addItem(lst_itm)
        box_solution_scorer_28.currentIndexChanged.connect(self.combobox_changed)

        hbox_solution_scorer_28.addWidget(box_solution_scorer_28)
        bg_box.addLayout(hbox_solution_scorer_28)
        label_29 = QLabel("        filter")
        label_29.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_29)
        hbox_check_doubled_cell_30 =  QHBoxLayout()
        label_check_doubled_cell_30 = QLabel("                        check_doubled_cell")
        label_check_doubled_cell_30.setFont(QFont("Times",14, QFont.Bold))
        hbox_check_doubled_cell_30.addWidget(label_check_doubled_cell_30)

        box_check_doubled_cell_30 = QComboBox()
        box_check_doubled_cell_30.tmp_lst=[]
        box_check_doubled_cell_30.tmp_lst.append("True")
        box_check_doubled_cell_30.tmp_lst.append("False")
        for lst_itm in box_check_doubled_cell_30.tmp_lst:
            box_check_doubled_cell_30.addItem(lst_itm)
        box_check_doubled_cell_30.currentIndexChanged.connect(self.combobox_changed)

        hbox_check_doubled_cell_30.addWidget(box_check_doubled_cell_30)
        bg_box.addLayout(hbox_check_doubled_cell_30)
        hbox_likelihood_cutoff_31 =  QHBoxLayout()
        label_likelihood_cutoff_31 = QLabel("                        likelihood_cutoff")
        label_likelihood_cutoff_31.setFont(QFont("Times",14, QFont.Bold))
        hbox_likelihood_cutoff_31.addWidget(label_likelihood_cutoff_31)

        box_likelihood_cutoff_31 = QDoubleSpinBox()
        box_likelihood_cutoff_31.local_path = "dummy path"
        box_likelihood_cutoff_31.valueChanged.connect(self.spnbox_changed)

        hbox_likelihood_cutoff_31.addWidget(box_likelihood_cutoff_31)
        bg_box.addLayout(hbox_likelihood_cutoff_31)
        hbox_volume_cutoff_32 =  QHBoxLayout()
        label_volume_cutoff_32 = QLabel("                        volume_cutoff")
        label_volume_cutoff_32.setFont(QFont("Times",14, QFont.Bold))
        hbox_volume_cutoff_32.addWidget(label_volume_cutoff_32)

        box_volume_cutoff_32 = QDoubleSpinBox()
        box_volume_cutoff_32.local_path = "dummy path"
        box_volume_cutoff_32.valueChanged.connect(self.spnbox_changed)

        hbox_volume_cutoff_32.addWidget(box_volume_cutoff_32)
        bg_box.addLayout(hbox_volume_cutoff_32)
        hbox_n_indexed_cutoff_33 =  QHBoxLayout()
        label_n_indexed_cutoff_33 = QLabel("                        n_indexed_cutoff")
        label_n_indexed_cutoff_33.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_indexed_cutoff_33.addWidget(label_n_indexed_cutoff_33)

        box_n_indexed_cutoff_33 = QDoubleSpinBox()
        box_n_indexed_cutoff_33.local_path = "dummy path"
        box_n_indexed_cutoff_33.valueChanged.connect(self.spnbox_changed)

        hbox_n_indexed_cutoff_33.addWidget(box_n_indexed_cutoff_33)
        bg_box.addLayout(hbox_n_indexed_cutoff_33)
        label_34 = QLabel("        weighted")
        label_34.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_34)
        hbox_power_35 =  QHBoxLayout()
        label_power_35 = QLabel("                        power")
        label_power_35.setFont(QFont("Times",14, QFont.Bold))
        hbox_power_35.addWidget(label_power_35)

        box_power_35 = QSpinBox()
        box_power_35.local_path = "dummy path"
        box_power_35.valueChanged.connect(self.spnbox_changed)

        hbox_power_35.addWidget(box_power_35)
        bg_box.addLayout(hbox_power_35)
        hbox_volume_weight_36 =  QHBoxLayout()
        label_volume_weight_36 = QLabel("                        volume_weight")
        label_volume_weight_36.setFont(QFont("Times",14, QFont.Bold))
        hbox_volume_weight_36.addWidget(label_volume_weight_36)

        box_volume_weight_36 = QDoubleSpinBox()
        box_volume_weight_36.local_path = "dummy path"
        box_volume_weight_36.valueChanged.connect(self.spnbox_changed)

        hbox_volume_weight_36.addWidget(box_volume_weight_36)
        bg_box.addLayout(hbox_volume_weight_36)
        hbox_n_indexed_weight_37 =  QHBoxLayout()
        label_n_indexed_weight_37 = QLabel("                        n_indexed_weight")
        label_n_indexed_weight_37.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_indexed_weight_37.addWidget(label_n_indexed_weight_37)

        box_n_indexed_weight_37 = QDoubleSpinBox()
        box_n_indexed_weight_37.local_path = "dummy path"
        box_n_indexed_weight_37.valueChanged.connect(self.spnbox_changed)

        hbox_n_indexed_weight_37.addWidget(box_n_indexed_weight_37)
        bg_box.addLayout(hbox_n_indexed_weight_37)
        hbox_rmsd_weight_38 =  QHBoxLayout()
        label_rmsd_weight_38 = QLabel("                        rmsd_weight")
        label_rmsd_weight_38.setFont(QFont("Times",14, QFont.Bold))
        hbox_rmsd_weight_38.addWidget(label_rmsd_weight_38)

        box_rmsd_weight_38 = QDoubleSpinBox()
        box_rmsd_weight_38.local_path = "dummy path"
        box_rmsd_weight_38.valueChanged.connect(self.spnbox_changed)

        hbox_rmsd_weight_38.addWidget(box_rmsd_weight_38)
        bg_box.addLayout(hbox_rmsd_weight_38)
        label_39 = QLabel("    index_assignment")
        label_39.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_39)
        hbox_method_40 =  QHBoxLayout()
        label_method_40 = QLabel("                method")
        label_method_40.setFont(QFont("Times",15, QFont.Bold))
        hbox_method_40.addWidget(label_method_40)

        box_method_40 = QComboBox()
        box_method_40.tmp_lst=[]
        box_method_40.tmp_lst.append("*simple")
        box_method_40.tmp_lst.append("local")
        for lst_itm in box_method_40.tmp_lst:
            box_method_40.addItem(lst_itm)
        box_method_40.currentIndexChanged.connect(self.combobox_changed)

        hbox_method_40.addWidget(box_method_40)
        bg_box.addLayout(hbox_method_40)
        label_41 = QLabel("        simple")
        label_41.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_41)
        hbox_hkl_tolerance_42 =  QHBoxLayout()
        label_hkl_tolerance_42 = QLabel("                        hkl_tolerance")
        label_hkl_tolerance_42.setFont(QFont("Times",14, QFont.Bold))
        hbox_hkl_tolerance_42.addWidget(label_hkl_tolerance_42)

        box_hkl_tolerance_42 = QDoubleSpinBox()
        box_hkl_tolerance_42.local_path = "dummy path"
        box_hkl_tolerance_42.valueChanged.connect(self.spnbox_changed)

        hbox_hkl_tolerance_42.addWidget(box_hkl_tolerance_42)
        bg_box.addLayout(hbox_hkl_tolerance_42)
        label_43 = QLabel("        local")
        label_43.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_43)
        hbox_epsilon_44 =  QHBoxLayout()
        label_epsilon_44 = QLabel("                        epsilon")
        label_epsilon_44.setFont(QFont("Times",14, QFont.Bold))
        hbox_epsilon_44.addWidget(label_epsilon_44)

        box_epsilon_44 = QDoubleSpinBox()
        box_epsilon_44.local_path = "dummy path"
        box_epsilon_44.valueChanged.connect(self.spnbox_changed)

        hbox_epsilon_44.addWidget(box_epsilon_44)
        bg_box.addLayout(hbox_epsilon_44)
        hbox_delta_45 =  QHBoxLayout()
        label_delta_45 = QLabel("                        delta")
        label_delta_45.setFont(QFont("Times",14, QFont.Bold))
        hbox_delta_45.addWidget(label_delta_45)

        box_delta_45 = QSpinBox()
        box_delta_45.local_path = "dummy path"
        box_delta_45.valueChanged.connect(self.spnbox_changed)

        hbox_delta_45.addWidget(box_delta_45)
        bg_box.addLayout(hbox_delta_45)
        hbox_l_min_46 =  QHBoxLayout()
        label_l_min_46 = QLabel("                        l_min")
        label_l_min_46.setFont(QFont("Times",14, QFont.Bold))
        hbox_l_min_46.addWidget(label_l_min_46)

        box_l_min_46 = QDoubleSpinBox()
        box_l_min_46.local_path = "dummy path"
        box_l_min_46.valueChanged.connect(self.spnbox_changed)

        hbox_l_min_46.addWidget(box_l_min_46)
        bg_box.addLayout(hbox_l_min_46)
        hbox_nearest_neighbours_47 =  QHBoxLayout()
        label_nearest_neighbours_47 = QLabel("                        nearest_neighbours")
        label_nearest_neighbours_47.setFont(QFont("Times",14, QFont.Bold))
        hbox_nearest_neighbours_47.addWidget(label_nearest_neighbours_47)

        box_nearest_neighbours_47 = QSpinBox()
        box_nearest_neighbours_47.local_path = "dummy path"
        box_nearest_neighbours_47.valueChanged.connect(self.spnbox_changed)

        hbox_nearest_neighbours_47.addWidget(box_nearest_neighbours_47)
        bg_box.addLayout(hbox_nearest_neighbours_47)
        hbox_optimise_initial_basis_vectors_48 =  QHBoxLayout()
        label_optimise_initial_basis_vectors_48 = QLabel("        optimise_initial_basis_vectors")
        label_optimise_initial_basis_vectors_48.setFont(QFont("Times",16, QFont.Bold))
        hbox_optimise_initial_basis_vectors_48.addWidget(label_optimise_initial_basis_vectors_48)

        box_optimise_initial_basis_vectors_48 = QComboBox()
        box_optimise_initial_basis_vectors_48.tmp_lst=[]
        box_optimise_initial_basis_vectors_48.tmp_lst.append("True")
        box_optimise_initial_basis_vectors_48.tmp_lst.append("False")
        for lst_itm in box_optimise_initial_basis_vectors_48.tmp_lst:
            box_optimise_initial_basis_vectors_48.addItem(lst_itm)
        box_optimise_initial_basis_vectors_48.currentIndexChanged.connect(self.combobox_changed)

        hbox_optimise_initial_basis_vectors_48.addWidget(box_optimise_initial_basis_vectors_48)
        bg_box.addLayout(hbox_optimise_initial_basis_vectors_48)
        hbox_debug_49 =  QHBoxLayout()
        label_debug_49 = QLabel("        debug")
        label_debug_49.setFont(QFont("Times",16, QFont.Bold))
        hbox_debug_49.addWidget(label_debug_49)

        box_debug_49 = QComboBox()
        box_debug_49.tmp_lst=[]
        box_debug_49.tmp_lst.append("True")
        box_debug_49.tmp_lst.append("False")
        for lst_itm in box_debug_49.tmp_lst:
            box_debug_49.addItem(lst_itm)
        box_debug_49.currentIndexChanged.connect(self.combobox_changed)

        hbox_debug_49.addWidget(box_debug_49)
        bg_box.addLayout(hbox_debug_49)
        hbox_debug_plots_50 =  QHBoxLayout()
        label_debug_plots_50 = QLabel("        debug_plots")
        label_debug_plots_50.setFont(QFont("Times",16, QFont.Bold))
        hbox_debug_plots_50.addWidget(label_debug_plots_50)

        box_debug_plots_50 = QComboBox()
        box_debug_plots_50.tmp_lst=[]
        box_debug_plots_50.tmp_lst.append("True")
        box_debug_plots_50.tmp_lst.append("False")
        for lst_itm in box_debug_plots_50.tmp_lst:
            box_debug_plots_50.addItem(lst_itm)
        box_debug_plots_50.currentIndexChanged.connect(self.combobox_changed)

        hbox_debug_plots_50.addWidget(box_debug_plots_50)
        bg_box.addLayout(hbox_debug_plots_50)
        hbox_combine_scans_51 =  QHBoxLayout()
        label_combine_scans_51 = QLabel("        combine_scans")
        label_combine_scans_51.setFont(QFont("Times",16, QFont.Bold))
        hbox_combine_scans_51.addWidget(label_combine_scans_51)

        box_combine_scans_51 = QComboBox()
        box_combine_scans_51.tmp_lst=[]
        box_combine_scans_51.tmp_lst.append("True")
        box_combine_scans_51.tmp_lst.append("False")
        for lst_itm in box_combine_scans_51.tmp_lst:
            box_combine_scans_51.addItem(lst_itm)
        box_combine_scans_51.currentIndexChanged.connect(self.combobox_changed)

        hbox_combine_scans_51.addWidget(box_combine_scans_51)
        bg_box.addLayout(hbox_combine_scans_51)
        label_52 = QLabel("    refinement_protocol")
        label_52.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_52)
        hbox_n_macro_cycles_53 =  QHBoxLayout()
        label_n_macro_cycles_53 = QLabel("                n_macro_cycles")
        label_n_macro_cycles_53.setFont(QFont("Times",15, QFont.Bold))
        hbox_n_macro_cycles_53.addWidget(label_n_macro_cycles_53)

        box_n_macro_cycles_53 = QSpinBox()
        box_n_macro_cycles_53.local_path = "dummy path"
        box_n_macro_cycles_53.valueChanged.connect(self.spnbox_changed)

        hbox_n_macro_cycles_53.addWidget(box_n_macro_cycles_53)
        bg_box.addLayout(hbox_n_macro_cycles_53)
        hbox_d_min_step_54 =  QHBoxLayout()
        label_d_min_step_54 = QLabel("                d_min_step")
        label_d_min_step_54.setFont(QFont("Times",15, QFont.Bold))
        hbox_d_min_step_54.addWidget(label_d_min_step_54)

        box_d_min_step_54 = QDoubleSpinBox()
        box_d_min_step_54.local_path = "dummy path"
        box_d_min_step_54.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_step_54.addWidget(box_d_min_step_54)
        bg_box.addLayout(hbox_d_min_step_54)
        hbox_d_min_start_55 =  QHBoxLayout()
        label_d_min_start_55 = QLabel("                d_min_start")
        label_d_min_start_55.setFont(QFont("Times",15, QFont.Bold))
        hbox_d_min_start_55.addWidget(label_d_min_start_55)

        box_d_min_start_55 = QDoubleSpinBox()
        box_d_min_start_55.local_path = "dummy path"
        box_d_min_start_55.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_start_55.addWidget(box_d_min_start_55)
        bg_box.addLayout(hbox_d_min_start_55)
        hbox_d_min_final_56 =  QHBoxLayout()
        label_d_min_final_56 = QLabel("                d_min_final")
        label_d_min_final_56.setFont(QFont("Times",15, QFont.Bold))
        hbox_d_min_final_56.addWidget(label_d_min_final_56)

        box_d_min_final_56 = QDoubleSpinBox()
        box_d_min_final_56.local_path = "dummy path"
        box_d_min_final_56.valueChanged.connect(self.spnbox_changed)

        hbox_d_min_final_56.addWidget(box_d_min_final_56)
        bg_box.addLayout(hbox_d_min_final_56)
        hbox_verbosity_57 =  QHBoxLayout()
        label_verbosity_57 = QLabel("                verbosity")
        label_verbosity_57.setFont(QFont("Times",15, QFont.Bold))
        hbox_verbosity_57.addWidget(label_verbosity_57)

        box_verbosity_57 = QSpinBox()
        box_verbosity_57.local_path = "dummy path"
        box_verbosity_57.valueChanged.connect(self.spnbox_changed)

        hbox_verbosity_57.addWidget(box_verbosity_57)
        bg_box.addLayout(hbox_verbosity_57)
        hbox_disable_unit_cell_volume_sanity_check_58 =  QHBoxLayout()
        label_disable_unit_cell_volume_sanity_check_58 = QLabel("                disable_unit_cell_volume_sanity_check")
        label_disable_unit_cell_volume_sanity_check_58.setFont(QFont("Times",15, QFont.Bold))
        hbox_disable_unit_cell_volume_sanity_check_58.addWidget(label_disable_unit_cell_volume_sanity_check_58)

        box_disable_unit_cell_volume_sanity_check_58 = QComboBox()
        box_disable_unit_cell_volume_sanity_check_58.tmp_lst=[]
        box_disable_unit_cell_volume_sanity_check_58.tmp_lst.append("True")
        box_disable_unit_cell_volume_sanity_check_58.tmp_lst.append("False")
        for lst_itm in box_disable_unit_cell_volume_sanity_check_58.tmp_lst:
            box_disable_unit_cell_volume_sanity_check_58.addItem(lst_itm)
        box_disable_unit_cell_volume_sanity_check_58.currentIndexChanged.connect(self.combobox_changed)

        hbox_disable_unit_cell_volume_sanity_check_58.addWidget(box_disable_unit_cell_volume_sanity_check_58)
        bg_box.addLayout(hbox_disable_unit_cell_volume_sanity_check_58)
        label_59 = QLabel("        outlier_rejection")
        label_59.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_59)
        hbox_maximum_spot_error_60 =  QHBoxLayout()
        label_maximum_spot_error_60 = QLabel("                        maximum_spot_error")
        label_maximum_spot_error_60.setFont(QFont("Times",14, QFont.Bold))
        hbox_maximum_spot_error_60.addWidget(label_maximum_spot_error_60)

        box_maximum_spot_error_60 = QDoubleSpinBox()
        box_maximum_spot_error_60.local_path = "dummy path"
        box_maximum_spot_error_60.valueChanged.connect(self.spnbox_changed)

        hbox_maximum_spot_error_60.addWidget(box_maximum_spot_error_60)
        bg_box.addLayout(hbox_maximum_spot_error_60)
        hbox_maximum_phi_error_61 =  QHBoxLayout()
        label_maximum_phi_error_61 = QLabel("                        maximum_phi_error")
        label_maximum_phi_error_61.setFont(QFont("Times",14, QFont.Bold))
        hbox_maximum_phi_error_61.addWidget(label_maximum_phi_error_61)

        box_maximum_phi_error_61 = QDoubleSpinBox()
        box_maximum_phi_error_61.local_path = "dummy path"
        box_maximum_phi_error_61.valueChanged.connect(self.spnbox_changed)

        hbox_maximum_phi_error_61.addWidget(box_maximum_phi_error_61)
        bg_box.addLayout(hbox_maximum_phi_error_61)
        hbox_method_62 =  QHBoxLayout()
        label_method_62 = QLabel("        method")
        label_method_62.setFont(QFont("Times",16, QFont.Bold))
        hbox_method_62.addWidget(label_method_62)

        box_method_62 = QComboBox()
        box_method_62.tmp_lst=[]
        box_method_62.tmp_lst.append("*fft3d")
        box_method_62.tmp_lst.append("fft1d")
        box_method_62.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_62.tmp_lst:
            box_method_62.addItem(lst_itm)
        box_method_62.currentIndexChanged.connect(self.combobox_changed)

        hbox_method_62.addWidget(box_method_62)
        bg_box.addLayout(hbox_method_62)
        label_63 = QLabel("    multiple_lattice_search")
        label_63.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_63)
        hbox_cluster_analysis_search_64 =  QHBoxLayout()
        label_cluster_analysis_search_64 = QLabel("                cluster_analysis_search")
        label_cluster_analysis_search_64.setFont(QFont("Times",15, QFont.Bold))
        hbox_cluster_analysis_search_64.addWidget(label_cluster_analysis_search_64)

        box_cluster_analysis_search_64 = QComboBox()
        box_cluster_analysis_search_64.tmp_lst=[]
        box_cluster_analysis_search_64.tmp_lst.append("True")
        box_cluster_analysis_search_64.tmp_lst.append("False")
        for lst_itm in box_cluster_analysis_search_64.tmp_lst:
            box_cluster_analysis_search_64.addItem(lst_itm)
        box_cluster_analysis_search_64.currentIndexChanged.connect(self.combobox_changed)

        hbox_cluster_analysis_search_64.addWidget(box_cluster_analysis_search_64)
        bg_box.addLayout(hbox_cluster_analysis_search_64)
        hbox_recycle_unindexed_reflections_65 =  QHBoxLayout()
        label_recycle_unindexed_reflections_65 = QLabel("                recycle_unindexed_reflections")
        label_recycle_unindexed_reflections_65.setFont(QFont("Times",15, QFont.Bold))
        hbox_recycle_unindexed_reflections_65.addWidget(label_recycle_unindexed_reflections_65)

        box_recycle_unindexed_reflections_65 = QComboBox()
        box_recycle_unindexed_reflections_65.tmp_lst=[]
        box_recycle_unindexed_reflections_65.tmp_lst.append("True")
        box_recycle_unindexed_reflections_65.tmp_lst.append("False")
        for lst_itm in box_recycle_unindexed_reflections_65.tmp_lst:
            box_recycle_unindexed_reflections_65.addItem(lst_itm)
        box_recycle_unindexed_reflections_65.currentIndexChanged.connect(self.combobox_changed)

        hbox_recycle_unindexed_reflections_65.addWidget(box_recycle_unindexed_reflections_65)
        bg_box.addLayout(hbox_recycle_unindexed_reflections_65)
        hbox_recycle_unindexed_reflections_cutoff_66 =  QHBoxLayout()
        label_recycle_unindexed_reflections_cutoff_66 = QLabel("                recycle_unindexed_reflections_cutoff")
        label_recycle_unindexed_reflections_cutoff_66.setFont(QFont("Times",15, QFont.Bold))
        hbox_recycle_unindexed_reflections_cutoff_66.addWidget(label_recycle_unindexed_reflections_cutoff_66)

        box_recycle_unindexed_reflections_cutoff_66 = QDoubleSpinBox()
        box_recycle_unindexed_reflections_cutoff_66.local_path = "dummy path"
        box_recycle_unindexed_reflections_cutoff_66.valueChanged.connect(self.spnbox_changed)

        hbox_recycle_unindexed_reflections_cutoff_66.addWidget(box_recycle_unindexed_reflections_cutoff_66)
        bg_box.addLayout(hbox_recycle_unindexed_reflections_cutoff_66)
        hbox_minimum_angular_separation_67 =  QHBoxLayout()
        label_minimum_angular_separation_67 = QLabel("                minimum_angular_separation")
        label_minimum_angular_separation_67.setFont(QFont("Times",15, QFont.Bold))
        hbox_minimum_angular_separation_67.addWidget(label_minimum_angular_separation_67)

        box_minimum_angular_separation_67 = QDoubleSpinBox()
        box_minimum_angular_separation_67.local_path = "dummy path"
        box_minimum_angular_separation_67.valueChanged.connect(self.spnbox_changed)

        hbox_minimum_angular_separation_67.addWidget(box_minimum_angular_separation_67)
        bg_box.addLayout(hbox_minimum_angular_separation_67)
        hbox_max_lattices_68 =  QHBoxLayout()
        label_max_lattices_68 = QLabel("                max_lattices")
        label_max_lattices_68.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_lattices_68.addWidget(label_max_lattices_68)

        box_max_lattices_68 = QSpinBox()
        box_max_lattices_68.local_path = "dummy path"
        box_max_lattices_68.valueChanged.connect(self.spnbox_changed)

        hbox_max_lattices_68.addWidget(box_max_lattices_68)
        bg_box.addLayout(hbox_max_lattices_68)
        label_69 = QLabel("        cluster_analysis")
        label_69.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_69)
        hbox_method_70 =  QHBoxLayout()
        label_method_70 = QLabel("                        method")
        label_method_70.setFont(QFont("Times",14, QFont.Bold))
        hbox_method_70.addWidget(label_method_70)

        box_method_70 = QComboBox()
        box_method_70.tmp_lst=[]
        box_method_70.tmp_lst.append("*dbscan")
        box_method_70.tmp_lst.append("hcluster")
        for lst_itm in box_method_70.tmp_lst:
            box_method_70.addItem(lst_itm)
        box_method_70.currentIndexChanged.connect(self.combobox_changed)

        hbox_method_70.addWidget(box_method_70)
        bg_box.addLayout(hbox_method_70)
        label_71 = QLabel("            hcluster")
        label_71.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_71)
        label_72 = QLabel("                linkage")
        label_72.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_72)
        hbox_method_73 =  QHBoxLayout()
        label_method_73 = QLabel("                                        method")
        label_method_73.setFont(QFont("Times",14, QFont.Bold))
        hbox_method_73.addWidget(label_method_73)

        box_method_73 = QComboBox()
        box_method_73.tmp_lst=[]
        box_method_73.tmp_lst.append("*ward")
        for lst_itm in box_method_73.tmp_lst:
            box_method_73.addItem(lst_itm)
        box_method_73.currentIndexChanged.connect(self.combobox_changed)

        hbox_method_73.addWidget(box_method_73)
        bg_box.addLayout(hbox_method_73)
        hbox_metric_74 =  QHBoxLayout()
        label_metric_74 = QLabel("                                        metric")
        label_metric_74.setFont(QFont("Times",14, QFont.Bold))
        hbox_metric_74.addWidget(label_metric_74)

        box_metric_74 = QComboBox()
        box_metric_74.tmp_lst=[]
        box_metric_74.tmp_lst.append("*euclidean")
        for lst_itm in box_metric_74.tmp_lst:
            box_metric_74.addItem(lst_itm)
        box_metric_74.currentIndexChanged.connect(self.combobox_changed)

        hbox_metric_74.addWidget(box_metric_74)
        bg_box.addLayout(hbox_metric_74)
        hbox_cutoff_75 =  QHBoxLayout()
        label_cutoff_75 = QLabel("                                cutoff")
        label_cutoff_75.setFont(QFont("Times",14, QFont.Bold))
        hbox_cutoff_75.addWidget(label_cutoff_75)

        box_cutoff_75 = QDoubleSpinBox()
        box_cutoff_75.local_path = "dummy path"
        box_cutoff_75.valueChanged.connect(self.spnbox_changed)

        hbox_cutoff_75.addWidget(box_cutoff_75)
        bg_box.addLayout(hbox_cutoff_75)
        hbox_cutoff_criterion_76 =  QHBoxLayout()
        label_cutoff_criterion_76 = QLabel("                                cutoff_criterion")
        label_cutoff_criterion_76.setFont(QFont("Times",14, QFont.Bold))
        hbox_cutoff_criterion_76.addWidget(label_cutoff_criterion_76)

        box_cutoff_criterion_76 = QComboBox()
        box_cutoff_criterion_76.tmp_lst=[]
        box_cutoff_criterion_76.tmp_lst.append("*distance")
        box_cutoff_criterion_76.tmp_lst.append("inconsistent")
        for lst_itm in box_cutoff_criterion_76.tmp_lst:
            box_cutoff_criterion_76.addItem(lst_itm)
        box_cutoff_criterion_76.currentIndexChanged.connect(self.combobox_changed)

        hbox_cutoff_criterion_76.addWidget(box_cutoff_criterion_76)
        bg_box.addLayout(hbox_cutoff_criterion_76)
        label_77 = QLabel("            dbscan")
        label_77.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_77)
        hbox_eps_78 =  QHBoxLayout()
        label_eps_78 = QLabel("                                eps")
        label_eps_78.setFont(QFont("Times",14, QFont.Bold))
        hbox_eps_78.addWidget(label_eps_78)

        box_eps_78 = QDoubleSpinBox()
        box_eps_78.local_path = "dummy path"
        box_eps_78.valueChanged.connect(self.spnbox_changed)

        hbox_eps_78.addWidget(box_eps_78)
        bg_box.addLayout(hbox_eps_78)
        hbox_min_samples_79 =  QHBoxLayout()
        label_min_samples_79 = QLabel("                                min_samples")
        label_min_samples_79.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_samples_79.addWidget(label_min_samples_79)

        box_min_samples_79 = QSpinBox()
        box_min_samples_79.local_path = "dummy path"
        box_min_samples_79.valueChanged.connect(self.spnbox_changed)

        hbox_min_samples_79.addWidget(box_min_samples_79)
        bg_box.addLayout(hbox_min_samples_79)
        hbox_min_cluster_size_80 =  QHBoxLayout()
        label_min_cluster_size_80 = QLabel("                        min_cluster_size")
        label_min_cluster_size_80.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_cluster_size_80.addWidget(label_min_cluster_size_80)

        box_min_cluster_size_80 = QSpinBox()
        box_min_cluster_size_80.local_path = "dummy path"
        box_min_cluster_size_80.valueChanged.connect(self.spnbox_changed)

        hbox_min_cluster_size_80.addWidget(box_min_cluster_size_80)
        bg_box.addLayout(hbox_min_cluster_size_80)
        hbox_intersection_union_ratio_cutoff_81 =  QHBoxLayout()
        label_intersection_union_ratio_cutoff_81 = QLabel("                        intersection_union_ratio_cutoff")
        label_intersection_union_ratio_cutoff_81.setFont(QFont("Times",14, QFont.Bold))
        hbox_intersection_union_ratio_cutoff_81.addWidget(label_intersection_union_ratio_cutoff_81)

        box_intersection_union_ratio_cutoff_81 = QDoubleSpinBox()
        box_intersection_union_ratio_cutoff_81.local_path = "dummy path"
        box_intersection_union_ratio_cutoff_81.valueChanged.connect(self.spnbox_changed)

        hbox_intersection_union_ratio_cutoff_81.addWidget(box_intersection_union_ratio_cutoff_81)
        bg_box.addLayout(hbox_intersection_union_ratio_cutoff_81)
        label_82 = QLabel("    real_space_grid_search")
        label_82.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_82)
        hbox_characteristic_grid_83 =  QHBoxLayout()
        label_characteristic_grid_83 = QLabel("                characteristic_grid")
        label_characteristic_grid_83.setFont(QFont("Times",15, QFont.Bold))
        hbox_characteristic_grid_83.addWidget(label_characteristic_grid_83)

        box_characteristic_grid_83 = QDoubleSpinBox()
        box_characteristic_grid_83.local_path = "dummy path"
        box_characteristic_grid_83.valueChanged.connect(self.spnbox_changed)

        hbox_characteristic_grid_83.addWidget(box_characteristic_grid_83)
        bg_box.addLayout(hbox_characteristic_grid_83)
        label_84 = QLabel("refinement")
        label_84.setFont(QFont("Monospace", 14, QFont.Bold))
        bg_box.addWidget(label_84)
        label_85 = QLabel("    mp")
        label_85.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_85)
        hbox_nproc_86 =  QHBoxLayout()
        label_nproc_86 = QLabel("                nproc")
        label_nproc_86.setFont(QFont("Times",15, QFont.Bold))
        hbox_nproc_86.addWidget(label_nproc_86)

        box_nproc_86 = QSpinBox()
        box_nproc_86.local_path = "dummy path"
        box_nproc_86.valueChanged.connect(self.spnbox_changed)

        hbox_nproc_86.addWidget(box_nproc_86)
        bg_box.addLayout(hbox_nproc_86)
        hbox_verbosity_87 =  QHBoxLayout()
        label_verbosity_87 = QLabel("        verbosity")
        label_verbosity_87.setFont(QFont("Times",16, QFont.Bold))
        hbox_verbosity_87.addWidget(label_verbosity_87)

        box_verbosity_87 = QSpinBox()
        box_verbosity_87.local_path = "dummy path"
        box_verbosity_87.valueChanged.connect(self.spnbox_changed)

        hbox_verbosity_87.addWidget(box_verbosity_87)
        bg_box.addLayout(hbox_verbosity_87)
        label_88 = QLabel("    parameterisation")
        label_88.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_88)
        label_89 = QLabel("        auto_reduction")
        label_89.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_89)
        hbox_min_nref_per_parameter_90 =  QHBoxLayout()
        label_min_nref_per_parameter_90 = QLabel("                        min_nref_per_parameter")
        label_min_nref_per_parameter_90.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_nref_per_parameter_90.addWidget(label_min_nref_per_parameter_90)

        box_min_nref_per_parameter_90 = QSpinBox()
        box_min_nref_per_parameter_90.local_path = "dummy path"
        box_min_nref_per_parameter_90.valueChanged.connect(self.spnbox_changed)

        hbox_min_nref_per_parameter_90.addWidget(box_min_nref_per_parameter_90)
        bg_box.addLayout(hbox_min_nref_per_parameter_90)
        hbox_action_91 =  QHBoxLayout()
        label_action_91 = QLabel("                        action")
        label_action_91.setFont(QFont("Times",14, QFont.Bold))
        hbox_action_91.addWidget(label_action_91)

        box_action_91 = QComboBox()
        box_action_91.tmp_lst=[]
        box_action_91.tmp_lst.append("*fail")
        box_action_91.tmp_lst.append("fix")
        box_action_91.tmp_lst.append("remove")
        for lst_itm in box_action_91.tmp_lst:
            box_action_91.addItem(lst_itm)
        box_action_91.currentIndexChanged.connect(self.combobox_changed)

        hbox_action_91.addWidget(box_action_91)
        bg_box.addLayout(hbox_action_91)
        label_92 = QLabel("        beam")
        label_92.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_92)
        hbox_fix_93 =  QHBoxLayout()
        label_fix_93 = QLabel("                        fix")
        label_fix_93.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_93.addWidget(label_fix_93)

        box_fix_93 = QComboBox()
        box_fix_93.tmp_lst=[]
        box_fix_93.tmp_lst.append("all")
        box_fix_93.tmp_lst.append("*in_spindle_plane")
        box_fix_93.tmp_lst.append("out_spindle_plane")
        box_fix_93.tmp_lst.append("*wavelength")
        for lst_itm in box_fix_93.tmp_lst:
            box_fix_93.addItem(lst_itm)
        box_fix_93.currentIndexChanged.connect(self.combobox_changed)

        hbox_fix_93.addWidget(box_fix_93)
        bg_box.addLayout(hbox_fix_93)
        hbox_fix_list_94 =  QHBoxLayout()
        label_fix_list_94 = QLabel("                        fix_list")
        label_fix_list_94.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_list_94.addWidget(label_fix_list_94)
        label_95 = QLabel("        crystal")
        label_95.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_95)
        hbox_fix_96 =  QHBoxLayout()
        label_fix_96 = QLabel("                        fix")
        label_fix_96.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_96.addWidget(label_fix_96)

        box_fix_96 = QComboBox()
        box_fix_96.tmp_lst=[]
        box_fix_96.tmp_lst.append("all")
        box_fix_96.tmp_lst.append("cell")
        box_fix_96.tmp_lst.append("orientation")
        for lst_itm in box_fix_96.tmp_lst:
            box_fix_96.addItem(lst_itm)
        box_fix_96.currentIndexChanged.connect(self.combobox_changed)

        hbox_fix_96.addWidget(box_fix_96)
        bg_box.addLayout(hbox_fix_96)
        hbox_cell_fix_list_97 =  QHBoxLayout()
        label_cell_fix_list_97 = QLabel("                        cell_fix_list")
        label_cell_fix_list_97.setFont(QFont("Times",14, QFont.Bold))
        hbox_cell_fix_list_97.addWidget(label_cell_fix_list_97)
        hbox_orientation_fix_list_98 =  QHBoxLayout()
        label_orientation_fix_list_98 = QLabel("                        orientation_fix_list")
        label_orientation_fix_list_98.setFont(QFont("Times",14, QFont.Bold))
        hbox_orientation_fix_list_98.addWidget(label_orientation_fix_list_98)
        hbox_scan_varying_99 =  QHBoxLayout()
        label_scan_varying_99 = QLabel("                        scan_varying")
        label_scan_varying_99.setFont(QFont("Times",14, QFont.Bold))
        hbox_scan_varying_99.addWidget(label_scan_varying_99)

        box_scan_varying_99 = QComboBox()
        box_scan_varying_99.tmp_lst=[]
        box_scan_varying_99.tmp_lst.append("True")
        box_scan_varying_99.tmp_lst.append("False")
        for lst_itm in box_scan_varying_99.tmp_lst:
            box_scan_varying_99.addItem(lst_itm)
        box_scan_varying_99.currentIndexChanged.connect(self.combobox_changed)

        hbox_scan_varying_99.addWidget(box_scan_varying_99)
        bg_box.addLayout(hbox_scan_varying_99)
        hbox_num_intervals_100 =  QHBoxLayout()
        label_num_intervals_100 = QLabel("                        num_intervals")
        label_num_intervals_100.setFont(QFont("Times",14, QFont.Bold))
        hbox_num_intervals_100.addWidget(label_num_intervals_100)

        box_num_intervals_100 = QComboBox()
        box_num_intervals_100.tmp_lst=[]
        box_num_intervals_100.tmp_lst.append("*fixed_width")
        box_num_intervals_100.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_100.tmp_lst:
            box_num_intervals_100.addItem(lst_itm)
        box_num_intervals_100.currentIndexChanged.connect(self.combobox_changed)

        hbox_num_intervals_100.addWidget(box_num_intervals_100)
        bg_box.addLayout(hbox_num_intervals_100)
        hbox_interval_width_degrees_101 =  QHBoxLayout()
        label_interval_width_degrees_101 = QLabel("                        interval_width_degrees")
        label_interval_width_degrees_101.setFont(QFont("Times",14, QFont.Bold))
        hbox_interval_width_degrees_101.addWidget(label_interval_width_degrees_101)

        box_interval_width_degrees_101 = QDoubleSpinBox()
        box_interval_width_degrees_101.local_path = "dummy path"
        box_interval_width_degrees_101.valueChanged.connect(self.spnbox_changed)

        hbox_interval_width_degrees_101.addWidget(box_interval_width_degrees_101)
        bg_box.addLayout(hbox_interval_width_degrees_101)
        hbox_absolute_num_intervals_102 =  QHBoxLayout()
        label_absolute_num_intervals_102 = QLabel("                        absolute_num_intervals")
        label_absolute_num_intervals_102.setFont(QFont("Times",14, QFont.Bold))
        hbox_absolute_num_intervals_102.addWidget(label_absolute_num_intervals_102)

        box_absolute_num_intervals_102 = QSpinBox()
        box_absolute_num_intervals_102.local_path = "dummy path"
        box_absolute_num_intervals_102.valueChanged.connect(self.spnbox_changed)

        hbox_absolute_num_intervals_102.addWidget(box_absolute_num_intervals_102)
        bg_box.addLayout(hbox_absolute_num_intervals_102)
        hbox_UB_model_per_103 =  QHBoxLayout()
        label_UB_model_per_103 = QLabel("                        UB_model_per")
        label_UB_model_per_103.setFont(QFont("Times",14, QFont.Bold))
        hbox_UB_model_per_103.addWidget(label_UB_model_per_103)

        box_UB_model_per_103 = QComboBox()
        box_UB_model_per_103.tmp_lst=[]
        box_UB_model_per_103.tmp_lst.append("reflection")
        box_UB_model_per_103.tmp_lst.append("image")
        box_UB_model_per_103.tmp_lst.append("*block")
        for lst_itm in box_UB_model_per_103.tmp_lst:
            box_UB_model_per_103.addItem(lst_itm)
        box_UB_model_per_103.currentIndexChanged.connect(self.combobox_changed)

        hbox_UB_model_per_103.addWidget(box_UB_model_per_103)
        bg_box.addLayout(hbox_UB_model_per_103)
        label_104 = QLabel("        detector")
        label_104.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_104)
        hbox_panels_105 =  QHBoxLayout()
        label_panels_105 = QLabel("                        panels")
        label_panels_105.setFont(QFont("Times",14, QFont.Bold))
        hbox_panels_105.addWidget(label_panels_105)

        box_panels_105 = QComboBox()
        box_panels_105.tmp_lst=[]
        box_panels_105.tmp_lst.append("*automatic")
        box_panels_105.tmp_lst.append("single")
        box_panels_105.tmp_lst.append("multiple")
        box_panels_105.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_105.tmp_lst:
            box_panels_105.addItem(lst_itm)
        box_panels_105.currentIndexChanged.connect(self.combobox_changed)

        hbox_panels_105.addWidget(box_panels_105)
        bg_box.addLayout(hbox_panels_105)
        hbox_hierarchy_level_106 =  QHBoxLayout()
        label_hierarchy_level_106 = QLabel("                        hierarchy_level")
        label_hierarchy_level_106.setFont(QFont("Times",14, QFont.Bold))
        hbox_hierarchy_level_106.addWidget(label_hierarchy_level_106)

        box_hierarchy_level_106 = QSpinBox()
        box_hierarchy_level_106.local_path = "dummy path"
        box_hierarchy_level_106.valueChanged.connect(self.spnbox_changed)

        hbox_hierarchy_level_106.addWidget(box_hierarchy_level_106)
        bg_box.addLayout(hbox_hierarchy_level_106)
        hbox_fix_107 =  QHBoxLayout()
        label_fix_107 = QLabel("                        fix")
        label_fix_107.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_107.addWidget(label_fix_107)

        box_fix_107 = QComboBox()
        box_fix_107.tmp_lst=[]
        box_fix_107.tmp_lst.append("all")
        box_fix_107.tmp_lst.append("position")
        box_fix_107.tmp_lst.append("orientation")
        for lst_itm in box_fix_107.tmp_lst:
            box_fix_107.addItem(lst_itm)
        box_fix_107.currentIndexChanged.connect(self.combobox_changed)

        hbox_fix_107.addWidget(box_fix_107)
        bg_box.addLayout(hbox_fix_107)
        hbox_fix_list_108 =  QHBoxLayout()
        label_fix_list_108 = QLabel("                        fix_list")
        label_fix_list_108.setFont(QFont("Times",14, QFont.Bold))
        hbox_fix_list_108.addWidget(label_fix_list_108)
        hbox_sparse_109 =  QHBoxLayout()
        label_sparse_109 = QLabel("                sparse")
        label_sparse_109.setFont(QFont("Times",15, QFont.Bold))
        hbox_sparse_109.addWidget(label_sparse_109)

        box_sparse_109 = QComboBox()
        box_sparse_109.tmp_lst=[]
        box_sparse_109.tmp_lst.append("True")
        box_sparse_109.tmp_lst.append("False")
        for lst_itm in box_sparse_109.tmp_lst:
            box_sparse_109.addItem(lst_itm)
        box_sparse_109.currentIndexChanged.connect(self.combobox_changed)

        hbox_sparse_109.addWidget(box_sparse_109)
        bg_box.addLayout(hbox_sparse_109)
        hbox_treat_single_image_as_still_110 =  QHBoxLayout()
        label_treat_single_image_as_still_110 = QLabel("                treat_single_image_as_still")
        label_treat_single_image_as_still_110.setFont(QFont("Times",15, QFont.Bold))
        hbox_treat_single_image_as_still_110.addWidget(label_treat_single_image_as_still_110)

        box_treat_single_image_as_still_110 = QComboBox()
        box_treat_single_image_as_still_110.tmp_lst=[]
        box_treat_single_image_as_still_110.tmp_lst.append("True")
        box_treat_single_image_as_still_110.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_110.tmp_lst:
            box_treat_single_image_as_still_110.addItem(lst_itm)
        box_treat_single_image_as_still_110.currentIndexChanged.connect(self.combobox_changed)

        hbox_treat_single_image_as_still_110.addWidget(box_treat_single_image_as_still_110)
        bg_box.addLayout(hbox_treat_single_image_as_still_110)
        label_111 = QLabel("    refinery")
        label_111.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_111)
        hbox_engine_112 =  QHBoxLayout()
        label_engine_112 = QLabel("                engine")
        label_engine_112.setFont(QFont("Times",15, QFont.Bold))
        hbox_engine_112.addWidget(label_engine_112)

        box_engine_112 = QComboBox()
        box_engine_112.tmp_lst=[]
        box_engine_112.tmp_lst.append("SimpleLBFGS")
        box_engine_112.tmp_lst.append("LBFGScurvs")
        box_engine_112.tmp_lst.append("GaussNewton")
        box_engine_112.tmp_lst.append("*LevMar")
        for lst_itm in box_engine_112.tmp_lst:
            box_engine_112.addItem(lst_itm)
        box_engine_112.currentIndexChanged.connect(self.combobox_changed)

        hbox_engine_112.addWidget(box_engine_112)
        bg_box.addLayout(hbox_engine_112)
        hbox_track_step_113 =  QHBoxLayout()
        label_track_step_113 = QLabel("                track_step")
        label_track_step_113.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_step_113.addWidget(label_track_step_113)

        box_track_step_113 = QComboBox()
        box_track_step_113.tmp_lst=[]
        box_track_step_113.tmp_lst.append("True")
        box_track_step_113.tmp_lst.append("False")
        for lst_itm in box_track_step_113.tmp_lst:
            box_track_step_113.addItem(lst_itm)
        box_track_step_113.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_step_113.addWidget(box_track_step_113)
        bg_box.addLayout(hbox_track_step_113)
        hbox_track_gradient_114 =  QHBoxLayout()
        label_track_gradient_114 = QLabel("                track_gradient")
        label_track_gradient_114.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_gradient_114.addWidget(label_track_gradient_114)

        box_track_gradient_114 = QComboBox()
        box_track_gradient_114.tmp_lst=[]
        box_track_gradient_114.tmp_lst.append("True")
        box_track_gradient_114.tmp_lst.append("False")
        for lst_itm in box_track_gradient_114.tmp_lst:
            box_track_gradient_114.addItem(lst_itm)
        box_track_gradient_114.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_gradient_114.addWidget(box_track_gradient_114)
        bg_box.addLayout(hbox_track_gradient_114)
        hbox_track_parameter_correlation_115 =  QHBoxLayout()
        label_track_parameter_correlation_115 = QLabel("                track_parameter_correlation")
        label_track_parameter_correlation_115.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_parameter_correlation_115.addWidget(label_track_parameter_correlation_115)

        box_track_parameter_correlation_115 = QComboBox()
        box_track_parameter_correlation_115.tmp_lst=[]
        box_track_parameter_correlation_115.tmp_lst.append("True")
        box_track_parameter_correlation_115.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_115.tmp_lst:
            box_track_parameter_correlation_115.addItem(lst_itm)
        box_track_parameter_correlation_115.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_parameter_correlation_115.addWidget(box_track_parameter_correlation_115)
        bg_box.addLayout(hbox_track_parameter_correlation_115)
        hbox_track_out_of_sample_rmsd_116 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_116 = QLabel("                track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_116.setFont(QFont("Times",15, QFont.Bold))
        hbox_track_out_of_sample_rmsd_116.addWidget(label_track_out_of_sample_rmsd_116)

        box_track_out_of_sample_rmsd_116 = QComboBox()
        box_track_out_of_sample_rmsd_116.tmp_lst=[]
        box_track_out_of_sample_rmsd_116.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_116.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_116.tmp_lst:
            box_track_out_of_sample_rmsd_116.addItem(lst_itm)
        box_track_out_of_sample_rmsd_116.currentIndexChanged.connect(self.combobox_changed)

        hbox_track_out_of_sample_rmsd_116.addWidget(box_track_out_of_sample_rmsd_116)
        bg_box.addLayout(hbox_track_out_of_sample_rmsd_116)
        hbox_log_117 =  QHBoxLayout()
        label_log_117 = QLabel("                log")
        label_log_117.setFont(QFont("Times",15, QFont.Bold))
        hbox_log_117.addWidget(label_log_117)
        hbox_max_iterations_118 =  QHBoxLayout()
        label_max_iterations_118 = QLabel("                max_iterations")
        label_max_iterations_118.setFont(QFont("Times",15, QFont.Bold))
        hbox_max_iterations_118.addWidget(label_max_iterations_118)

        box_max_iterations_118 = QSpinBox()
        box_max_iterations_118.local_path = "dummy path"
        box_max_iterations_118.valueChanged.connect(self.spnbox_changed)

        hbox_max_iterations_118.addWidget(box_max_iterations_118)
        bg_box.addLayout(hbox_max_iterations_118)
        label_119 = QLabel("    target")
        label_119.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_119)
        hbox_rmsd_cutoff_120 =  QHBoxLayout()
        label_rmsd_cutoff_120 = QLabel("                rmsd_cutoff")
        label_rmsd_cutoff_120.setFont(QFont("Times",15, QFont.Bold))
        hbox_rmsd_cutoff_120.addWidget(label_rmsd_cutoff_120)

        box_rmsd_cutoff_120 = QComboBox()
        box_rmsd_cutoff_120.tmp_lst=[]
        box_rmsd_cutoff_120.tmp_lst.append("*fraction_of_bin_size")
        box_rmsd_cutoff_120.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_120.tmp_lst:
            box_rmsd_cutoff_120.addItem(lst_itm)
        box_rmsd_cutoff_120.currentIndexChanged.connect(self.combobox_changed)

        hbox_rmsd_cutoff_120.addWidget(box_rmsd_cutoff_120)
        bg_box.addLayout(hbox_rmsd_cutoff_120)
        hbox_bin_size_fraction_121 =  QHBoxLayout()
        label_bin_size_fraction_121 = QLabel("                bin_size_fraction")
        label_bin_size_fraction_121.setFont(QFont("Times",15, QFont.Bold))
        hbox_bin_size_fraction_121.addWidget(label_bin_size_fraction_121)

        box_bin_size_fraction_121 = QDoubleSpinBox()
        box_bin_size_fraction_121.local_path = "dummy path"
        box_bin_size_fraction_121.valueChanged.connect(self.spnbox_changed)

        hbox_bin_size_fraction_121.addWidget(box_bin_size_fraction_121)
        bg_box.addLayout(hbox_bin_size_fraction_121)
        hbox_absolute_cutoffs_122 =  QHBoxLayout()
        label_absolute_cutoffs_122 = QLabel("                absolute_cutoffs")
        label_absolute_cutoffs_122.setFont(QFont("Times",15, QFont.Bold))
        hbox_absolute_cutoffs_122.addWidget(label_absolute_cutoffs_122)
        hbox_gradient_calculation_blocksize_123 =  QHBoxLayout()
        label_gradient_calculation_blocksize_123 = QLabel("                gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_123.setFont(QFont("Times",15, QFont.Bold))
        hbox_gradient_calculation_blocksize_123.addWidget(label_gradient_calculation_blocksize_123)

        box_gradient_calculation_blocksize_123 = QSpinBox()
        box_gradient_calculation_blocksize_123.local_path = "dummy path"
        box_gradient_calculation_blocksize_123.valueChanged.connect(self.spnbox_changed)

        hbox_gradient_calculation_blocksize_123.addWidget(box_gradient_calculation_blocksize_123)
        bg_box.addLayout(hbox_gradient_calculation_blocksize_123)
        label_124 = QLabel("    reflections")
        label_124.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_124)
        hbox_reflections_per_degree_125 =  QHBoxLayout()
        label_reflections_per_degree_125 = QLabel("                reflections_per_degree")
        label_reflections_per_degree_125.setFont(QFont("Times",15, QFont.Bold))
        hbox_reflections_per_degree_125.addWidget(label_reflections_per_degree_125)

        box_reflections_per_degree_125 = QDoubleSpinBox()
        box_reflections_per_degree_125.local_path = "dummy path"
        box_reflections_per_degree_125.valueChanged.connect(self.spnbox_changed)

        hbox_reflections_per_degree_125.addWidget(box_reflections_per_degree_125)
        bg_box.addLayout(hbox_reflections_per_degree_125)
        hbox_minimum_sample_size_126 =  QHBoxLayout()
        label_minimum_sample_size_126 = QLabel("                minimum_sample_size")
        label_minimum_sample_size_126.setFont(QFont("Times",15, QFont.Bold))
        hbox_minimum_sample_size_126.addWidget(label_minimum_sample_size_126)

        box_minimum_sample_size_126 = QSpinBox()
        box_minimum_sample_size_126.local_path = "dummy path"
        box_minimum_sample_size_126.valueChanged.connect(self.spnbox_changed)

        hbox_minimum_sample_size_126.addWidget(box_minimum_sample_size_126)
        bg_box.addLayout(hbox_minimum_sample_size_126)
        hbox_maximum_sample_size_127 =  QHBoxLayout()
        label_maximum_sample_size_127 = QLabel("                maximum_sample_size")
        label_maximum_sample_size_127.setFont(QFont("Times",15, QFont.Bold))
        hbox_maximum_sample_size_127.addWidget(label_maximum_sample_size_127)

        box_maximum_sample_size_127 = QSpinBox()
        box_maximum_sample_size_127.local_path = "dummy path"
        box_maximum_sample_size_127.valueChanged.connect(self.spnbox_changed)

        hbox_maximum_sample_size_127.addWidget(box_maximum_sample_size_127)
        bg_box.addLayout(hbox_maximum_sample_size_127)
        hbox_use_all_reflections_128 =  QHBoxLayout()
        label_use_all_reflections_128 = QLabel("                use_all_reflections")
        label_use_all_reflections_128.setFont(QFont("Times",15, QFont.Bold))
        hbox_use_all_reflections_128.addWidget(label_use_all_reflections_128)

        box_use_all_reflections_128 = QComboBox()
        box_use_all_reflections_128.tmp_lst=[]
        box_use_all_reflections_128.tmp_lst.append("True")
        box_use_all_reflections_128.tmp_lst.append("False")
        for lst_itm in box_use_all_reflections_128.tmp_lst:
            box_use_all_reflections_128.addItem(lst_itm)
        box_use_all_reflections_128.currentIndexChanged.connect(self.combobox_changed)

        hbox_use_all_reflections_128.addWidget(box_use_all_reflections_128)
        bg_box.addLayout(hbox_use_all_reflections_128)
        hbox_random_seed_129 =  QHBoxLayout()
        label_random_seed_129 = QLabel("                random_seed")
        label_random_seed_129.setFont(QFont("Times",15, QFont.Bold))
        hbox_random_seed_129.addWidget(label_random_seed_129)

        box_random_seed_129 = QSpinBox()
        box_random_seed_129.local_path = "dummy path"
        box_random_seed_129.valueChanged.connect(self.spnbox_changed)

        hbox_random_seed_129.addWidget(box_random_seed_129)
        bg_box.addLayout(hbox_random_seed_129)
        hbox_close_to_spindle_cutoff_130 =  QHBoxLayout()
        label_close_to_spindle_cutoff_130 = QLabel("                close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_130.setFont(QFont("Times",15, QFont.Bold))
        hbox_close_to_spindle_cutoff_130.addWidget(label_close_to_spindle_cutoff_130)

        box_close_to_spindle_cutoff_130 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_130.local_path = "dummy path"
        box_close_to_spindle_cutoff_130.valueChanged.connect(self.spnbox_changed)

        hbox_close_to_spindle_cutoff_130.addWidget(box_close_to_spindle_cutoff_130)
        bg_box.addLayout(hbox_close_to_spindle_cutoff_130)
        hbox_block_width_131 =  QHBoxLayout()
        label_block_width_131 = QLabel("                block_width")
        label_block_width_131.setFont(QFont("Times",15, QFont.Bold))
        hbox_block_width_131.addWidget(label_block_width_131)

        box_block_width_131 = QDoubleSpinBox()
        box_block_width_131.local_path = "dummy path"
        box_block_width_131.valueChanged.connect(self.spnbox_changed)

        hbox_block_width_131.addWidget(box_block_width_131)
        bg_box.addLayout(hbox_block_width_131)
        label_132 = QLabel("        weighting_strategy")
        label_132.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_132)
        hbox_override_133 =  QHBoxLayout()
        label_override_133 = QLabel("                        override")
        label_override_133.setFont(QFont("Times",14, QFont.Bold))
        hbox_override_133.addWidget(label_override_133)

        box_override_133 = QComboBox()
        box_override_133.tmp_lst=[]
        box_override_133.tmp_lst.append("statistical")
        box_override_133.tmp_lst.append("stills")
        box_override_133.tmp_lst.append("constant")
        for lst_itm in box_override_133.tmp_lst:
            box_override_133.addItem(lst_itm)
        box_override_133.currentIndexChanged.connect(self.combobox_changed)

        hbox_override_133.addWidget(box_override_133)
        bg_box.addLayout(hbox_override_133)
        hbox_delpsi_constant_134 =  QHBoxLayout()
        label_delpsi_constant_134 = QLabel("                        delpsi_constant")
        label_delpsi_constant_134.setFont(QFont("Times",14, QFont.Bold))
        hbox_delpsi_constant_134.addWidget(label_delpsi_constant_134)

        box_delpsi_constant_134 = QDoubleSpinBox()
        box_delpsi_constant_134.local_path = "dummy path"
        box_delpsi_constant_134.valueChanged.connect(self.spnbox_changed)

        hbox_delpsi_constant_134.addWidget(box_delpsi_constant_134)
        bg_box.addLayout(hbox_delpsi_constant_134)
        hbox_constants_135 =  QHBoxLayout()
        label_constants_135 = QLabel("                        constants")
        label_constants_135.setFont(QFont("Times",14, QFont.Bold))
        hbox_constants_135.addWidget(label_constants_135)
        label_136 = QLabel("        outlier")
        label_136.setFont(QFont("Monospace", 12, QFont.Bold))
        bg_box.addWidget(label_136)
        hbox_algorithm_137 =  QHBoxLayout()
        label_algorithm_137 = QLabel("                        algorithm")
        label_algorithm_137.setFont(QFont("Times",14, QFont.Bold))
        hbox_algorithm_137.addWidget(label_algorithm_137)

        box_algorithm_137 = QComboBox()
        box_algorithm_137.tmp_lst=[]
        box_algorithm_137.tmp_lst.append("null")
        box_algorithm_137.tmp_lst.append("*auto")
        box_algorithm_137.tmp_lst.append("mcd")
        box_algorithm_137.tmp_lst.append("tukey")
        box_algorithm_137.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_137.tmp_lst:
            box_algorithm_137.addItem(lst_itm)
        box_algorithm_137.currentIndexChanged.connect(self.combobox_changed)

        hbox_algorithm_137.addWidget(box_algorithm_137)
        bg_box.addLayout(hbox_algorithm_137)
        hbox_minimum_number_of_reflections_138 =  QHBoxLayout()
        label_minimum_number_of_reflections_138 = QLabel("                        minimum_number_of_reflections")
        label_minimum_number_of_reflections_138.setFont(QFont("Times",14, QFont.Bold))
        hbox_minimum_number_of_reflections_138.addWidget(label_minimum_number_of_reflections_138)

        box_minimum_number_of_reflections_138 = QSpinBox()
        box_minimum_number_of_reflections_138.local_path = "dummy path"
        box_minimum_number_of_reflections_138.valueChanged.connect(self.spnbox_changed)

        hbox_minimum_number_of_reflections_138.addWidget(box_minimum_number_of_reflections_138)
        bg_box.addLayout(hbox_minimum_number_of_reflections_138)
        hbox_separate_experiments_139 =  QHBoxLayout()
        label_separate_experiments_139 = QLabel("                        separate_experiments")
        label_separate_experiments_139.setFont(QFont("Times",14, QFont.Bold))
        hbox_separate_experiments_139.addWidget(label_separate_experiments_139)

        box_separate_experiments_139 = QComboBox()
        box_separate_experiments_139.tmp_lst=[]
        box_separate_experiments_139.tmp_lst.append("True")
        box_separate_experiments_139.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_139.tmp_lst:
            box_separate_experiments_139.addItem(lst_itm)
        box_separate_experiments_139.currentIndexChanged.connect(self.combobox_changed)

        hbox_separate_experiments_139.addWidget(box_separate_experiments_139)
        bg_box.addLayout(hbox_separate_experiments_139)
        hbox_separate_panels_140 =  QHBoxLayout()
        label_separate_panels_140 = QLabel("                        separate_panels")
        label_separate_panels_140.setFont(QFont("Times",14, QFont.Bold))
        hbox_separate_panels_140.addWidget(label_separate_panels_140)

        box_separate_panels_140 = QComboBox()
        box_separate_panels_140.tmp_lst=[]
        box_separate_panels_140.tmp_lst.append("True")
        box_separate_panels_140.tmp_lst.append("False")
        for lst_itm in box_separate_panels_140.tmp_lst:
            box_separate_panels_140.addItem(lst_itm)
        box_separate_panels_140.currentIndexChanged.connect(self.combobox_changed)

        hbox_separate_panels_140.addWidget(box_separate_panels_140)
        bg_box.addLayout(hbox_separate_panels_140)
        label_141 = QLabel("            tukey")
        label_141.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_141)
        hbox_iqr_multiplier_142 =  QHBoxLayout()
        label_iqr_multiplier_142 = QLabel("                                iqr_multiplier")
        label_iqr_multiplier_142.setFont(QFont("Times",14, QFont.Bold))
        hbox_iqr_multiplier_142.addWidget(label_iqr_multiplier_142)

        box_iqr_multiplier_142 = QDoubleSpinBox()
        box_iqr_multiplier_142.local_path = "dummy path"
        box_iqr_multiplier_142.valueChanged.connect(self.spnbox_changed)

        hbox_iqr_multiplier_142.addWidget(box_iqr_multiplier_142)
        bg_box.addLayout(hbox_iqr_multiplier_142)
        label_143 = QLabel("            mcd")
        label_143.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_143)
        hbox_alpha_144 =  QHBoxLayout()
        label_alpha_144 = QLabel("                                alpha")
        label_alpha_144.setFont(QFont("Times",14, QFont.Bold))
        hbox_alpha_144.addWidget(label_alpha_144)

        box_alpha_144 = QDoubleSpinBox()
        box_alpha_144.local_path = "dummy path"
        box_alpha_144.valueChanged.connect(self.spnbox_changed)

        hbox_alpha_144.addWidget(box_alpha_144)
        bg_box.addLayout(hbox_alpha_144)
        hbox_max_n_groups_145 =  QHBoxLayout()
        label_max_n_groups_145 = QLabel("                                max_n_groups")
        label_max_n_groups_145.setFont(QFont("Times",14, QFont.Bold))
        hbox_max_n_groups_145.addWidget(label_max_n_groups_145)

        box_max_n_groups_145 = QSpinBox()
        box_max_n_groups_145.local_path = "dummy path"
        box_max_n_groups_145.valueChanged.connect(self.spnbox_changed)

        hbox_max_n_groups_145.addWidget(box_max_n_groups_145)
        bg_box.addLayout(hbox_max_n_groups_145)
        hbox_min_group_size_146 =  QHBoxLayout()
        label_min_group_size_146 = QLabel("                                min_group_size")
        label_min_group_size_146.setFont(QFont("Times",14, QFont.Bold))
        hbox_min_group_size_146.addWidget(label_min_group_size_146)

        box_min_group_size_146 = QSpinBox()
        box_min_group_size_146.local_path = "dummy path"
        box_min_group_size_146.valueChanged.connect(self.spnbox_changed)

        hbox_min_group_size_146.addWidget(box_min_group_size_146)
        bg_box.addLayout(hbox_min_group_size_146)
        hbox_n_trials_147 =  QHBoxLayout()
        label_n_trials_147 = QLabel("                                n_trials")
        label_n_trials_147.setFont(QFont("Times",14, QFont.Bold))
        hbox_n_trials_147.addWidget(label_n_trials_147)

        box_n_trials_147 = QSpinBox()
        box_n_trials_147.local_path = "dummy path"
        box_n_trials_147.valueChanged.connect(self.spnbox_changed)

        hbox_n_trials_147.addWidget(box_n_trials_147)
        bg_box.addLayout(hbox_n_trials_147)
        hbox_k1_148 =  QHBoxLayout()
        label_k1_148 = QLabel("                                k1")
        label_k1_148.setFont(QFont("Times",14, QFont.Bold))
        hbox_k1_148.addWidget(label_k1_148)

        box_k1_148 = QSpinBox()
        box_k1_148.local_path = "dummy path"
        box_k1_148.valueChanged.connect(self.spnbox_changed)

        hbox_k1_148.addWidget(box_k1_148)
        bg_box.addLayout(hbox_k1_148)
        hbox_k2_149 =  QHBoxLayout()
        label_k2_149 = QLabel("                                k2")
        label_k2_149.setFont(QFont("Times",14, QFont.Bold))
        hbox_k2_149.addWidget(label_k2_149)

        box_k2_149 = QSpinBox()
        box_k2_149.local_path = "dummy path"
        box_k2_149.valueChanged.connect(self.spnbox_changed)

        hbox_k2_149.addWidget(box_k2_149)
        bg_box.addLayout(hbox_k2_149)
        hbox_k3_150 =  QHBoxLayout()
        label_k3_150 = QLabel("                                k3")
        label_k3_150.setFont(QFont("Times",14, QFont.Bold))
        hbox_k3_150.addWidget(label_k3_150)

        box_k3_150 = QSpinBox()
        box_k3_150.local_path = "dummy path"
        box_k3_150.valueChanged.connect(self.spnbox_changed)

        hbox_k3_150.addWidget(box_k3_150)
        bg_box.addLayout(hbox_k3_150)
        hbox_threshold_probability_151 =  QHBoxLayout()
        label_threshold_probability_151 = QLabel("                                threshold_probability")
        label_threshold_probability_151.setFont(QFont("Times",14, QFont.Bold))
        hbox_threshold_probability_151.addWidget(label_threshold_probability_151)

        box_threshold_probability_151 = QDoubleSpinBox()
        box_threshold_probability_151.local_path = "dummy path"
        box_threshold_probability_151.valueChanged.connect(self.spnbox_changed)

        hbox_threshold_probability_151.addWidget(box_threshold_probability_151)
        bg_box.addLayout(hbox_threshold_probability_151)
        label_152 = QLabel("            sauter_poon")
        label_152.setFont(QFont("Monospace", 13, QFont.Bold))
        bg_box.addWidget(label_152)
        hbox_px_sz_153 =  QHBoxLayout()
        label_px_sz_153 = QLabel("                                px_sz")
        label_px_sz_153.setFont(QFont("Times",14, QFont.Bold))
        hbox_px_sz_153.addWidget(label_px_sz_153)
        hbox_verbose_154 =  QHBoxLayout()
        label_verbose_154 = QLabel("                                verbose")
        label_verbose_154.setFont(QFont("Times",14, QFont.Bold))
        hbox_verbose_154.addWidget(label_verbose_154)

        box_verbose_154 = QComboBox()
        box_verbose_154.tmp_lst=[]
        box_verbose_154.tmp_lst.append("True")
        box_verbose_154.tmp_lst.append("False")
        for lst_itm in box_verbose_154.tmp_lst:
            box_verbose_154.addItem(lst_itm)
        box_verbose_154.currentIndexChanged.connect(self.combobox_changed)

        hbox_verbose_154.addWidget(box_verbose_154)
        bg_box.addLayout(hbox_verbose_154)
        hbox_pdf_155 =  QHBoxLayout()
        label_pdf_155 = QLabel("                                pdf")
        label_pdf_155.setFont(QFont("Times",14, QFont.Bold))
        hbox_pdf_155.addWidget(label_pdf_155)

        box_pdf_155 = QLineEdit()
        box_pdf_155.local_path = "dummy path"
        box_pdf_155.textChanged.connect(self.spnbox_changed)

        hbox_pdf_155.addWidget(box_pdf_155)
        bg_box.addLayout(hbox_pdf_155)
        label_156 = QLabel("output")
        label_156.setFont(QFont("Monospace", 14, QFont.Bold))
        bg_box.addWidget(label_156)
        hbox_experiments_157 =  QHBoxLayout()
        label_experiments_157 = QLabel("        experiments")
        label_experiments_157.setFont(QFont("Times",16, QFont.Bold))
        hbox_experiments_157.addWidget(label_experiments_157)
        hbox_reflections_158 =  QHBoxLayout()
        label_reflections_158 = QLabel("        reflections")
        label_reflections_158.setFont(QFont("Times",16, QFont.Bold))
        hbox_reflections_158.addWidget(label_reflections_158)
        hbox_unindexed_reflections_159 =  QHBoxLayout()
        label_unindexed_reflections_159 = QLabel("        unindexed_reflections")
        label_unindexed_reflections_159.setFont(QFont("Times",16, QFont.Bold))
        hbox_unindexed_reflections_159.addWidget(label_unindexed_reflections_159)
        hbox_verbosity_160 =  QHBoxLayout()
        label_verbosity_160 = QLabel("verbosity")
        label_verbosity_160.setFont(QFont("Times",18, QFont.Bold))
        hbox_verbosity_160.addWidget(label_verbosity_160)

        box_verbosity_160 = QSpinBox()
        box_verbosity_160.local_path = "dummy path"
        box_verbosity_160.valueChanged.connect(self.spnbox_changed)

        hbox_verbosity_160.addWidget(box_verbosity_160)
        bg_box.addLayout(hbox_verbosity_160)

        self.setLayout(bg_box)
        self.show()


    def spnbox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "spnbox_changed to:", value


    def combobox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "combobox_changed to:"
        print sender.tmp_lst[value]


class ParamMainWidget( QWidget):
    def __init__(self):
        super(ParamMainWidget, self).__init__()
        self.scrollable_widget = inner_widg(self)
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
