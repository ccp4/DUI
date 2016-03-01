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


        label_0 = QLabel("output")
        label_0.setPalette(palette_scope)
        label_0.setFont(QFont("Monospace"))
        bg_box.addWidget(label_0)
        hbox_lay_experiments_1 =  QHBoxLayout()
        label_experiments_1 = QLabel("    experiments")
        label_experiments_1.setPalette(palette_object)
        label_experiments_1.setFont(QFont("Monospace"))
        hbox_lay_experiments_1.addWidget(label_experiments_1)

        box_experiments_1 = QLineEdit()
        box_experiments_1.local_path = "output.experiments"
        box_experiments_1.textChanged.connect(self.spnbox_changed)
        hbox_lay_experiments_1.addWidget(box_experiments_1)
        bg_box.addLayout(hbox_lay_experiments_1)

        hbox_lay_reflections_2 =  QHBoxLayout()
        label_reflections_2 = QLabel("    reflections")
        label_reflections_2.setPalette(palette_object)
        label_reflections_2.setFont(QFont("Monospace"))
        hbox_lay_reflections_2.addWidget(label_reflections_2)

        box_reflections_2 = QLineEdit()
        box_reflections_2.local_path = "output.reflections"
        box_reflections_2.textChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_2.addWidget(box_reflections_2)
        bg_box.addLayout(hbox_lay_reflections_2)

        hbox_lay_matches_3 =  QHBoxLayout()
        label_matches_3 = QLabel("    matches")
        label_matches_3.setPalette(palette_object)
        label_matches_3.setFont(QFont("Monospace"))
        hbox_lay_matches_3.addWidget(label_matches_3)

        box_matches_3 = QLineEdit()
        box_matches_3.local_path = "output.matches"
        box_matches_3.textChanged.connect(self.spnbox_changed)
        hbox_lay_matches_3.addWidget(box_matches_3)
        bg_box.addLayout(hbox_lay_matches_3)

        hbox_lay_centroids_4 =  QHBoxLayout()
        label_centroids_4 = QLabel("    centroids")
        label_centroids_4.setPalette(palette_object)
        label_centroids_4.setFont(QFont("Monospace"))
        hbox_lay_centroids_4.addWidget(label_centroids_4)

        box_centroids_4 = QLineEdit()
        box_centroids_4.local_path = "output.centroids"
        box_centroids_4.textChanged.connect(self.spnbox_changed)
        hbox_lay_centroids_4.addWidget(box_centroids_4)
        bg_box.addLayout(hbox_lay_centroids_4)

        hbox_lay_parameter_table_5 =  QHBoxLayout()
        label_parameter_table_5 = QLabel("    parameter_table")
        label_parameter_table_5.setPalette(palette_object)
        label_parameter_table_5.setFont(QFont("Monospace"))
        hbox_lay_parameter_table_5.addWidget(label_parameter_table_5)

        box_parameter_table_5 = QLineEdit()
        box_parameter_table_5.local_path = "output.parameter_table"
        box_parameter_table_5.textChanged.connect(self.spnbox_changed)
        hbox_lay_parameter_table_5.addWidget(box_parameter_table_5)
        bg_box.addLayout(hbox_lay_parameter_table_5)

        hbox_lay_log_6 =  QHBoxLayout()
        label_log_6 = QLabel("    log")
        label_log_6.setPalette(palette_object)
        label_log_6.setFont(QFont("Monospace"))
        hbox_lay_log_6.addWidget(label_log_6)

        box_log_6 = QLineEdit()
        box_log_6.local_path = "output.log"
        box_log_6.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_6.addWidget(box_log_6)
        bg_box.addLayout(hbox_lay_log_6)

        hbox_lay_debug_log_7 =  QHBoxLayout()
        label_debug_log_7 = QLabel("    debug_log")
        label_debug_log_7.setPalette(palette_object)
        label_debug_log_7.setFont(QFont("Monospace"))
        hbox_lay_debug_log_7.addWidget(label_debug_log_7)

        box_debug_log_7 = QLineEdit()
        box_debug_log_7.local_path = "output.debug_log"
        box_debug_log_7.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_7.addWidget(box_debug_log_7)
        bg_box.addLayout(hbox_lay_debug_log_7)

        label_8 = QLabel("    correlation_plot")
        label_8.setPalette(palette_scope)
        label_8.setFont(QFont("Monospace"))
        bg_box.addWidget(label_8)
        hbox_lay_filename_9 =  QHBoxLayout()
        label_filename_9 = QLabel("        filename")
        label_filename_9.setPalette(palette_object)
        label_filename_9.setFont(QFont("Monospace"))
        hbox_lay_filename_9.addWidget(label_filename_9)

        box_filename_9 = QLineEdit()
        box_filename_9.local_path = "output.correlation_plot.filename"
        box_filename_9.textChanged.connect(self.spnbox_changed)
        hbox_lay_filename_9.addWidget(box_filename_9)
        bg_box.addLayout(hbox_lay_filename_9)

        hbox_lay_save_matrix_10 =  QHBoxLayout()
        label_save_matrix_10 = QLabel("        save_matrix")
        label_save_matrix_10.setPalette(palette_object)
        label_save_matrix_10.setFont(QFont("Monospace"))
        hbox_lay_save_matrix_10.addWidget(label_save_matrix_10)

        box_save_matrix_10 = QComboBox()
        box_save_matrix_10.local_path = "output.correlation_plot.save_matrix"
        box_save_matrix_10.tmp_lst=[]
        box_save_matrix_10.tmp_lst.append("True")
        box_save_matrix_10.tmp_lst.append("False")
        for lst_itm in box_save_matrix_10.tmp_lst:
            box_save_matrix_10.addItem(lst_itm)
        box_save_matrix_10.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_save_matrix_10.addWidget(box_save_matrix_10)
        bg_box.addLayout(hbox_lay_save_matrix_10)

        hbox_lay_col_select_11 =  QHBoxLayout()
        label_col_select_11 = QLabel("        col_select")
        label_col_select_11.setPalette(palette_object)
        label_col_select_11.setFont(QFont("Monospace"))
        hbox_lay_col_select_11.addWidget(label_col_select_11)

        box_col_select_11 = QLineEdit()
        box_col_select_11.local_path = "output.correlation_plot.col_select"
        box_col_select_11.textChanged.connect(self.spnbox_changed)
        hbox_lay_col_select_11.addWidget(box_col_select_11)
        bg_box.addLayout(hbox_lay_col_select_11)

        hbox_lay_history_13 =  QHBoxLayout()
        label_history_13 = QLabel("    history")
        label_history_13.setPalette(palette_object)
        label_history_13.setFont(QFont("Monospace"))
        hbox_lay_history_13.addWidget(label_history_13)

        box_history_13 = QLineEdit()
        box_history_13.local_path = "output.history"
        box_history_13.textChanged.connect(self.spnbox_changed)
        hbox_lay_history_13.addWidget(box_history_13)
        bg_box.addLayout(hbox_lay_history_13)

        label_14 = QLabel("refinement")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace"))
        bg_box.addWidget(label_14)
        label_15 = QLabel("    mp")
        label_15.setPalette(palette_scope)
        label_15.setFont(QFont("Monospace"))
        bg_box.addWidget(label_15)
        hbox_lay_nproc_16 =  QHBoxLayout()
        label_nproc_16 = QLabel("        nproc")
        label_nproc_16.setPalette(palette_object)
        label_nproc_16.setFont(QFont("Monospace"))
        hbox_lay_nproc_16.addWidget(label_nproc_16)

        box_nproc_16 = QSpinBox()
        box_nproc_16.local_path = "refinement.mp.nproc"
        box_nproc_16.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_16.addWidget(box_nproc_16)
        bg_box.addLayout(hbox_lay_nproc_16)

        hbox_lay_verbosity_17 =  QHBoxLayout()
        label_verbosity_17 = QLabel("    verbosity")
        label_verbosity_17.setPalette(palette_object)
        label_verbosity_17.setFont(QFont("Monospace"))
        hbox_lay_verbosity_17.addWidget(label_verbosity_17)

        box_verbosity_17 = QSpinBox()
        box_verbosity_17.local_path = "refinement.verbosity"
        box_verbosity_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_17.addWidget(box_verbosity_17)
        bg_box.addLayout(hbox_lay_verbosity_17)

        label_18 = QLabel("    parameterisation")
        label_18.setPalette(palette_scope)
        label_18.setFont(QFont("Monospace"))
        bg_box.addWidget(label_18)
        label_19 = QLabel("        auto_reduction")
        label_19.setPalette(palette_scope)
        label_19.setFont(QFont("Monospace"))
        bg_box.addWidget(label_19)
        hbox_lay_min_nref_per_parameter_20 =  QHBoxLayout()
        label_min_nref_per_parameter_20 = QLabel("            min_nref_per_parameter")
        label_min_nref_per_parameter_20.setPalette(palette_object)
        label_min_nref_per_parameter_20.setFont(QFont("Monospace"))
        hbox_lay_min_nref_per_parameter_20.addWidget(label_min_nref_per_parameter_20)

        box_min_nref_per_parameter_20 = QSpinBox()
        box_min_nref_per_parameter_20.local_path = "refinement.parameterisation.auto_reduction.min_nref_per_parameter"
        box_min_nref_per_parameter_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_nref_per_parameter_20.addWidget(box_min_nref_per_parameter_20)
        bg_box.addLayout(hbox_lay_min_nref_per_parameter_20)

        hbox_lay_action_21 =  QHBoxLayout()
        label_action_21 = QLabel("            action")
        label_action_21.setPalette(palette_object)
        label_action_21.setFont(QFont("Monospace"))
        hbox_lay_action_21.addWidget(label_action_21)

        box_action_21 = QComboBox()
        box_action_21.local_path = "refinement.parameterisation.auto_reduction.action"
        box_action_21.tmp_lst=[]
        box_action_21.tmp_lst.append("*fail")
        box_action_21.tmp_lst.append("fix")
        box_action_21.tmp_lst.append("remove")
        for lst_itm in box_action_21.tmp_lst:
            box_action_21.addItem(lst_itm)
        box_action_21.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_action_21.addWidget(box_action_21)
        bg_box.addLayout(hbox_lay_action_21)

        label_22 = QLabel("        beam")
        label_22.setPalette(palette_scope)
        label_22.setFont(QFont("Monospace"))
        bg_box.addWidget(label_22)
        hbox_lay_fix_23 =  QHBoxLayout()
        label_fix_23 = QLabel("            fix")
        label_fix_23.setPalette(palette_object)
        label_fix_23.setFont(QFont("Monospace"))
        hbox_lay_fix_23.addWidget(label_fix_23)

        box_fix_23 = QComboBox()
        box_fix_23.local_path = "refinement.parameterisation.beam.fix"
        box_fix_23.tmp_lst=[]
        box_fix_23.tmp_lst.append("all")
        box_fix_23.tmp_lst.append("*in_spindle_plane")
        box_fix_23.tmp_lst.append("out_spindle_plane")
        box_fix_23.tmp_lst.append("*wavelength")
        for lst_itm in box_fix_23.tmp_lst:
            box_fix_23.addItem(lst_itm)
        box_fix_23.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_23.addWidget(box_fix_23)
        bg_box.addLayout(hbox_lay_fix_23)

        label_25 = QLabel("        crystal")
        label_25.setPalette(palette_scope)
        label_25.setFont(QFont("Monospace"))
        bg_box.addWidget(label_25)
        hbox_lay_fix_26 =  QHBoxLayout()
        label_fix_26 = QLabel("            fix")
        label_fix_26.setPalette(palette_object)
        label_fix_26.setFont(QFont("Monospace"))
        hbox_lay_fix_26.addWidget(label_fix_26)

        box_fix_26 = QComboBox()
        box_fix_26.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_26.tmp_lst=[]
        box_fix_26.tmp_lst.append("all")
        box_fix_26.tmp_lst.append("cell")
        box_fix_26.tmp_lst.append("orientation")
        for lst_itm in box_fix_26.tmp_lst:
            box_fix_26.addItem(lst_itm)
        box_fix_26.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_26.addWidget(box_fix_26)
        bg_box.addLayout(hbox_lay_fix_26)

        label_27 = QLabel("            unit_cell")
        label_27.setPalette(palette_scope)
        label_27.setFont(QFont("Monospace"))
        bg_box.addWidget(label_27)
        label_29 = QLabel("                restraints")
        label_29.setPalette(palette_scope)
        label_29.setFont(QFont("Monospace"))
        bg_box.addWidget(label_29)
        label_30 = QLabel("                    tie_to_target")
        label_30.setPalette(palette_scope)
        label_30.setFont(QFont("Monospace"))
        bg_box.addWidget(label_30)
        hbox_lay_values_31_0 =  QHBoxLayout()
        label_values_31_0 = QLabel("                        values[1]")
        label_values_31_0.setPalette(palette_object)
        label_values_31_0.setFont(QFont("Monospace"))
        hbox_lay_values_31_0.addWidget(label_values_31_0)
        box_values_31_0 = QDoubleSpinBox()
        box_values_31_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_1 =  QHBoxLayout()
        label_values_31_1 = QLabel("                        values[2]")
        label_values_31_1.setPalette(palette_object)
        label_values_31_1.setFont(QFont("Monospace"))
        hbox_lay_values_31_1.addWidget(label_values_31_1)
        box_values_31_1 = QDoubleSpinBox()
        box_values_31_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_2 =  QHBoxLayout()
        label_values_31_2 = QLabel("                        values[3]")
        label_values_31_2.setPalette(palette_object)
        label_values_31_2.setFont(QFont("Monospace"))
        hbox_lay_values_31_2.addWidget(label_values_31_2)
        box_values_31_2 = QDoubleSpinBox()
        box_values_31_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_3 =  QHBoxLayout()
        label_values_31_3 = QLabel("                        values[4]")
        label_values_31_3.setPalette(palette_object)
        label_values_31_3.setFont(QFont("Monospace"))
        hbox_lay_values_31_3.addWidget(label_values_31_3)
        box_values_31_3 = QDoubleSpinBox()
        box_values_31_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_4 =  QHBoxLayout()
        label_values_31_4 = QLabel("                        values[5]")
        label_values_31_4.setPalette(palette_object)
        label_values_31_4.setFont(QFont("Monospace"))
        hbox_lay_values_31_4.addWidget(label_values_31_4)
        box_values_31_4 = QDoubleSpinBox()
        box_values_31_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_5 =  QHBoxLayout()
        label_values_31_5 = QLabel("                        values[6]")
        label_values_31_5.setPalette(palette_object)
        label_values_31_5.setFont(QFont("Monospace"))
        hbox_lay_values_31_5.addWidget(label_values_31_5)
        box_values_31_5 = QDoubleSpinBox()
        box_values_31_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_0 =  QHBoxLayout()
        label_sigmas_32_0 = QLabel("                        sigmas[1]")
        label_sigmas_32_0.setPalette(palette_object)
        label_sigmas_32_0.setFont(QFont("Monospace"))
        hbox_lay_sigmas_32_0.addWidget(label_sigmas_32_0)
        box_sigmas_32_0 = QDoubleSpinBox()
        box_sigmas_32_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_1 =  QHBoxLayout()
        label_sigmas_32_1 = QLabel("                        sigmas[2]")
        label_sigmas_32_1.setPalette(palette_object)
        label_sigmas_32_1.setFont(QFont("Monospace"))
        hbox_lay_sigmas_32_1.addWidget(label_sigmas_32_1)
        box_sigmas_32_1 = QDoubleSpinBox()
        box_sigmas_32_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_2 =  QHBoxLayout()
        label_sigmas_32_2 = QLabel("                        sigmas[3]")
        label_sigmas_32_2.setPalette(palette_object)
        label_sigmas_32_2.setFont(QFont("Monospace"))
        hbox_lay_sigmas_32_2.addWidget(label_sigmas_32_2)
        box_sigmas_32_2 = QDoubleSpinBox()
        box_sigmas_32_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_3 =  QHBoxLayout()
        label_sigmas_32_3 = QLabel("                        sigmas[4]")
        label_sigmas_32_3.setPalette(palette_object)
        label_sigmas_32_3.setFont(QFont("Monospace"))
        hbox_lay_sigmas_32_3.addWidget(label_sigmas_32_3)
        box_sigmas_32_3 = QDoubleSpinBox()
        box_sigmas_32_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_4 =  QHBoxLayout()
        label_sigmas_32_4 = QLabel("                        sigmas[5]")
        label_sigmas_32_4.setPalette(palette_object)
        label_sigmas_32_4.setFont(QFont("Monospace"))
        hbox_lay_sigmas_32_4.addWidget(label_sigmas_32_4)
        box_sigmas_32_4 = QDoubleSpinBox()
        box_sigmas_32_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_5 =  QHBoxLayout()
        label_sigmas_32_5 = QLabel("                        sigmas[6]")
        label_sigmas_32_5.setPalette(palette_object)
        label_sigmas_32_5.setFont(QFont("Monospace"))
        hbox_lay_sigmas_32_5.addWidget(label_sigmas_32_5)
        box_sigmas_32_5 = QDoubleSpinBox()
        box_sigmas_32_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_id_33 =  QHBoxLayout()
        label_id_33 = QLabel("                        id")
        label_id_33.setPalette(palette_object)
        label_id_33.setFont(QFont("Monospace"))
        hbox_lay_id_33.addWidget(label_id_33)

        box_id_33 = QSpinBox()
        box_id_33.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.id"
        box_id_33.valueChanged.connect(self.spnbox_changed)
        hbox_lay_id_33.addWidget(box_id_33)
        bg_box.addLayout(hbox_lay_id_33)

        label_34 = QLabel("                    tie_to_group")
        label_34.setPalette(palette_scope)
        label_34.setFont(QFont("Monospace"))
        bg_box.addWidget(label_34)
        hbox_lay_target_35 =  QHBoxLayout()
        label_target_35 = QLabel("                        target")
        label_target_35.setPalette(palette_object)
        label_target_35.setFont(QFont("Monospace"))
        hbox_lay_target_35.addWidget(label_target_35)

        box_target_35 = QComboBox()
        box_target_35.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_35.tmp_lst=[]
        box_target_35.tmp_lst.append("*mean")
        box_target_35.tmp_lst.append("median")
        for lst_itm in box_target_35.tmp_lst:
            box_target_35.addItem(lst_itm)
        box_target_35.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_35.addWidget(box_target_35)
        bg_box.addLayout(hbox_lay_target_35)

        label_38 = QLabel("            orientation")
        label_38.setPalette(palette_scope)
        label_38.setFont(QFont("Monospace"))
        bg_box.addWidget(label_38)
        hbox_lay_scan_varying_40 =  QHBoxLayout()
        label_scan_varying_40 = QLabel("            scan_varying")
        label_scan_varying_40.setPalette(palette_object)
        label_scan_varying_40.setFont(QFont("Monospace"))
        hbox_lay_scan_varying_40.addWidget(label_scan_varying_40)

        box_scan_varying_40 = QComboBox()
        box_scan_varying_40.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_40.tmp_lst=[]
        box_scan_varying_40.tmp_lst.append("True")
        box_scan_varying_40.tmp_lst.append("False")
        for lst_itm in box_scan_varying_40.tmp_lst:
            box_scan_varying_40.addItem(lst_itm)
        box_scan_varying_40.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_40.addWidget(box_scan_varying_40)
        bg_box.addLayout(hbox_lay_scan_varying_40)

        hbox_lay_num_intervals_41 =  QHBoxLayout()
        label_num_intervals_41 = QLabel("            num_intervals")
        label_num_intervals_41.setPalette(palette_object)
        label_num_intervals_41.setFont(QFont("Monospace"))
        hbox_lay_num_intervals_41.addWidget(label_num_intervals_41)

        box_num_intervals_41 = QComboBox()
        box_num_intervals_41.local_path = "refinement.parameterisation.crystal.num_intervals"
        box_num_intervals_41.tmp_lst=[]
        box_num_intervals_41.tmp_lst.append("*fixed_width")
        box_num_intervals_41.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_41.tmp_lst:
            box_num_intervals_41.addItem(lst_itm)
        box_num_intervals_41.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_41.addWidget(box_num_intervals_41)
        bg_box.addLayout(hbox_lay_num_intervals_41)

        hbox_lay_interval_width_degrees_42 =  QHBoxLayout()
        label_interval_width_degrees_42 = QLabel("            interval_width_degrees")
        label_interval_width_degrees_42.setPalette(palette_object)
        label_interval_width_degrees_42.setFont(QFont("Monospace"))
        hbox_lay_interval_width_degrees_42.addWidget(label_interval_width_degrees_42)

        box_interval_width_degrees_42 = QDoubleSpinBox()
        box_interval_width_degrees_42.local_path = "refinement.parameterisation.crystal.interval_width_degrees"
        box_interval_width_degrees_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_42.addWidget(box_interval_width_degrees_42)
        bg_box.addLayout(hbox_lay_interval_width_degrees_42)

        hbox_lay_absolute_num_intervals_43 =  QHBoxLayout()
        label_absolute_num_intervals_43 = QLabel("            absolute_num_intervals")
        label_absolute_num_intervals_43.setPalette(palette_object)
        label_absolute_num_intervals_43.setFont(QFont("Monospace"))
        hbox_lay_absolute_num_intervals_43.addWidget(label_absolute_num_intervals_43)

        box_absolute_num_intervals_43 = QSpinBox()
        box_absolute_num_intervals_43.local_path = "refinement.parameterisation.crystal.absolute_num_intervals"
        box_absolute_num_intervals_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_43.addWidget(box_absolute_num_intervals_43)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_43)

        hbox_lay_UB_model_per_44 =  QHBoxLayout()
        label_UB_model_per_44 = QLabel("            UB_model_per")
        label_UB_model_per_44.setPalette(palette_object)
        label_UB_model_per_44.setFont(QFont("Monospace"))
        hbox_lay_UB_model_per_44.addWidget(label_UB_model_per_44)

        box_UB_model_per_44 = QComboBox()
        box_UB_model_per_44.local_path = "refinement.parameterisation.crystal.UB_model_per"
        box_UB_model_per_44.tmp_lst=[]
        box_UB_model_per_44.tmp_lst.append("reflection")
        box_UB_model_per_44.tmp_lst.append("image")
        box_UB_model_per_44.tmp_lst.append("*block")
        for lst_itm in box_UB_model_per_44.tmp_lst:
            box_UB_model_per_44.addItem(lst_itm)
        box_UB_model_per_44.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_UB_model_per_44.addWidget(box_UB_model_per_44)
        bg_box.addLayout(hbox_lay_UB_model_per_44)

        label_45 = QLabel("        detector")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace"))
        bg_box.addWidget(label_45)
        hbox_lay_panels_46 =  QHBoxLayout()
        label_panels_46 = QLabel("            panels")
        label_panels_46.setPalette(palette_object)
        label_panels_46.setFont(QFont("Monospace"))
        hbox_lay_panels_46.addWidget(label_panels_46)

        box_panels_46 = QComboBox()
        box_panels_46.local_path = "refinement.parameterisation.detector.panels"
        box_panels_46.tmp_lst=[]
        box_panels_46.tmp_lst.append("*automatic")
        box_panels_46.tmp_lst.append("single")
        box_panels_46.tmp_lst.append("multiple")
        box_panels_46.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_46.tmp_lst:
            box_panels_46.addItem(lst_itm)
        box_panels_46.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_46.addWidget(box_panels_46)
        bg_box.addLayout(hbox_lay_panels_46)

        hbox_lay_hierarchy_level_47 =  QHBoxLayout()
        label_hierarchy_level_47 = QLabel("            hierarchy_level")
        label_hierarchy_level_47.setPalette(palette_object)
        label_hierarchy_level_47.setFont(QFont("Monospace"))
        hbox_lay_hierarchy_level_47.addWidget(label_hierarchy_level_47)

        box_hierarchy_level_47 = QSpinBox()
        box_hierarchy_level_47.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_47.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_47.addWidget(box_hierarchy_level_47)
        bg_box.addLayout(hbox_lay_hierarchy_level_47)

        hbox_lay_fix_48 =  QHBoxLayout()
        label_fix_48 = QLabel("            fix")
        label_fix_48.setPalette(palette_object)
        label_fix_48.setFont(QFont("Monospace"))
        hbox_lay_fix_48.addWidget(label_fix_48)

        box_fix_48 = QComboBox()
        box_fix_48.local_path = "refinement.parameterisation.detector.fix"
        box_fix_48.tmp_lst=[]
        box_fix_48.tmp_lst.append("all")
        box_fix_48.tmp_lst.append("position")
        box_fix_48.tmp_lst.append("orientation")
        for lst_itm in box_fix_48.tmp_lst:
            box_fix_48.addItem(lst_itm)
        box_fix_48.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_48.addWidget(box_fix_48)
        bg_box.addLayout(hbox_lay_fix_48)

        hbox_lay_sparse_50 =  QHBoxLayout()
        label_sparse_50 = QLabel("        sparse")
        label_sparse_50.setPalette(palette_object)
        label_sparse_50.setFont(QFont("Monospace"))
        hbox_lay_sparse_50.addWidget(label_sparse_50)

        box_sparse_50 = QComboBox()
        box_sparse_50.local_path = "refinement.parameterisation.sparse"
        box_sparse_50.tmp_lst=[]
        box_sparse_50.tmp_lst.append("True")
        box_sparse_50.tmp_lst.append("False")
        for lst_itm in box_sparse_50.tmp_lst:
            box_sparse_50.addItem(lst_itm)
        box_sparse_50.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_50.addWidget(box_sparse_50)
        bg_box.addLayout(hbox_lay_sparse_50)

        hbox_lay_treat_single_image_as_still_51 =  QHBoxLayout()
        label_treat_single_image_as_still_51 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_51.setPalette(palette_object)
        label_treat_single_image_as_still_51.setFont(QFont("Monospace"))
        hbox_lay_treat_single_image_as_still_51.addWidget(label_treat_single_image_as_still_51)

        box_treat_single_image_as_still_51 = QComboBox()
        box_treat_single_image_as_still_51.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_51.tmp_lst=[]
        box_treat_single_image_as_still_51.tmp_lst.append("True")
        box_treat_single_image_as_still_51.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_51.tmp_lst:
            box_treat_single_image_as_still_51.addItem(lst_itm)
        box_treat_single_image_as_still_51.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_51.addWidget(box_treat_single_image_as_still_51)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_51)

        label_52 = QLabel("    refinery")
        label_52.setPalette(palette_scope)
        label_52.setFont(QFont("Monospace"))
        bg_box.addWidget(label_52)
        hbox_lay_engine_53 =  QHBoxLayout()
        label_engine_53 = QLabel("        engine")
        label_engine_53.setPalette(palette_object)
        label_engine_53.setFont(QFont("Monospace"))
        hbox_lay_engine_53.addWidget(label_engine_53)

        box_engine_53 = QComboBox()
        box_engine_53.local_path = "refinement.refinery.engine"
        box_engine_53.tmp_lst=[]
        box_engine_53.tmp_lst.append("SimpleLBFGS")
        box_engine_53.tmp_lst.append("LBFGScurvs")
        box_engine_53.tmp_lst.append("GaussNewton")
        box_engine_53.tmp_lst.append("*LevMar")
        for lst_itm in box_engine_53.tmp_lst:
            box_engine_53.addItem(lst_itm)
        box_engine_53.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_53.addWidget(box_engine_53)
        bg_box.addLayout(hbox_lay_engine_53)

        hbox_lay_track_step_54 =  QHBoxLayout()
        label_track_step_54 = QLabel("        track_step")
        label_track_step_54.setPalette(palette_object)
        label_track_step_54.setFont(QFont("Monospace"))
        hbox_lay_track_step_54.addWidget(label_track_step_54)

        box_track_step_54 = QComboBox()
        box_track_step_54.local_path = "refinement.refinery.track_step"
        box_track_step_54.tmp_lst=[]
        box_track_step_54.tmp_lst.append("True")
        box_track_step_54.tmp_lst.append("False")
        for lst_itm in box_track_step_54.tmp_lst:
            box_track_step_54.addItem(lst_itm)
        box_track_step_54.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_54.addWidget(box_track_step_54)
        bg_box.addLayout(hbox_lay_track_step_54)

        hbox_lay_track_gradient_55 =  QHBoxLayout()
        label_track_gradient_55 = QLabel("        track_gradient")
        label_track_gradient_55.setPalette(palette_object)
        label_track_gradient_55.setFont(QFont("Monospace"))
        hbox_lay_track_gradient_55.addWidget(label_track_gradient_55)

        box_track_gradient_55 = QComboBox()
        box_track_gradient_55.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_55.tmp_lst=[]
        box_track_gradient_55.tmp_lst.append("True")
        box_track_gradient_55.tmp_lst.append("False")
        for lst_itm in box_track_gradient_55.tmp_lst:
            box_track_gradient_55.addItem(lst_itm)
        box_track_gradient_55.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_55.addWidget(box_track_gradient_55)
        bg_box.addLayout(hbox_lay_track_gradient_55)

        hbox_lay_track_parameter_correlation_56 =  QHBoxLayout()
        label_track_parameter_correlation_56 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_56.setPalette(palette_object)
        label_track_parameter_correlation_56.setFont(QFont("Monospace"))
        hbox_lay_track_parameter_correlation_56.addWidget(label_track_parameter_correlation_56)

        box_track_parameter_correlation_56 = QComboBox()
        box_track_parameter_correlation_56.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_56.tmp_lst=[]
        box_track_parameter_correlation_56.tmp_lst.append("True")
        box_track_parameter_correlation_56.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_56.tmp_lst:
            box_track_parameter_correlation_56.addItem(lst_itm)
        box_track_parameter_correlation_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_56.addWidget(box_track_parameter_correlation_56)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_56)

        hbox_lay_track_out_of_sample_rmsd_57 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_57 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_57.setPalette(palette_object)
        label_track_out_of_sample_rmsd_57.setFont(QFont("Monospace"))
        hbox_lay_track_out_of_sample_rmsd_57.addWidget(label_track_out_of_sample_rmsd_57)

        box_track_out_of_sample_rmsd_57 = QComboBox()
        box_track_out_of_sample_rmsd_57.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_57.tmp_lst=[]
        box_track_out_of_sample_rmsd_57.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_57.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_57.tmp_lst:
            box_track_out_of_sample_rmsd_57.addItem(lst_itm)
        box_track_out_of_sample_rmsd_57.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_57.addWidget(box_track_out_of_sample_rmsd_57)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_57)

        hbox_lay_max_iterations_59 =  QHBoxLayout()
        label_max_iterations_59 = QLabel("        max_iterations")
        label_max_iterations_59.setPalette(palette_object)
        label_max_iterations_59.setFont(QFont("Monospace"))
        hbox_lay_max_iterations_59.addWidget(label_max_iterations_59)

        box_max_iterations_59 = QSpinBox()
        box_max_iterations_59.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_59.addWidget(box_max_iterations_59)
        bg_box.addLayout(hbox_lay_max_iterations_59)

        label_60 = QLabel("    target")
        label_60.setPalette(palette_scope)
        label_60.setFont(QFont("Monospace"))
        bg_box.addWidget(label_60)
        hbox_lay_rmsd_cutoff_61 =  QHBoxLayout()
        label_rmsd_cutoff_61 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_61.setPalette(palette_object)
        label_rmsd_cutoff_61.setFont(QFont("Monospace"))
        hbox_lay_rmsd_cutoff_61.addWidget(label_rmsd_cutoff_61)

        box_rmsd_cutoff_61 = QComboBox()
        box_rmsd_cutoff_61.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_61.tmp_lst=[]
        box_rmsd_cutoff_61.tmp_lst.append("*fraction_of_bin_size")
        box_rmsd_cutoff_61.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_61.tmp_lst:
            box_rmsd_cutoff_61.addItem(lst_itm)
        box_rmsd_cutoff_61.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_61.addWidget(box_rmsd_cutoff_61)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_61)

        hbox_lay_bin_size_fraction_62 =  QHBoxLayout()
        label_bin_size_fraction_62 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_62.setPalette(palette_object)
        label_bin_size_fraction_62.setFont(QFont("Monospace"))
        hbox_lay_bin_size_fraction_62.addWidget(label_bin_size_fraction_62)

        box_bin_size_fraction_62 = QDoubleSpinBox()
        box_bin_size_fraction_62.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_62.addWidget(box_bin_size_fraction_62)
        bg_box.addLayout(hbox_lay_bin_size_fraction_62)

        hbox_lay_absolute_cutoffs_63_0 =  QHBoxLayout()
        label_absolute_cutoffs_63_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_63_0.setPalette(palette_object)
        label_absolute_cutoffs_63_0.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_63_0.addWidget(label_absolute_cutoffs_63_0)
        box_absolute_cutoffs_63_0 = QDoubleSpinBox()
        box_absolute_cutoffs_63_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_63_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_63_1 =  QHBoxLayout()
        label_absolute_cutoffs_63_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_63_1.setPalette(palette_object)
        label_absolute_cutoffs_63_1.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_63_1.addWidget(label_absolute_cutoffs_63_1)
        box_absolute_cutoffs_63_1 = QDoubleSpinBox()
        box_absolute_cutoffs_63_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_63_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_63_2 =  QHBoxLayout()
        label_absolute_cutoffs_63_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_63_2.setPalette(palette_object)
        label_absolute_cutoffs_63_2.setFont(QFont("Monospace"))
        hbox_lay_absolute_cutoffs_63_2.addWidget(label_absolute_cutoffs_63_2)
        box_absolute_cutoffs_63_2 = QDoubleSpinBox()
        box_absolute_cutoffs_63_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_63_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_63_0.addWidget(box_absolute_cutoffs_63_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_63_0)

        hbox_lay_absolute_cutoffs_63_1.addWidget(box_absolute_cutoffs_63_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_63_1)

        hbox_lay_absolute_cutoffs_63_2.addWidget(box_absolute_cutoffs_63_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_63_2)

        hbox_lay_gradient_calculation_blocksize_64 =  QHBoxLayout()
        label_gradient_calculation_blocksize_64 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_64.setPalette(palette_object)
        label_gradient_calculation_blocksize_64.setFont(QFont("Monospace"))
        hbox_lay_gradient_calculation_blocksize_64.addWidget(label_gradient_calculation_blocksize_64)

        box_gradient_calculation_blocksize_64 = QSpinBox()
        box_gradient_calculation_blocksize_64.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_64.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_64.addWidget(box_gradient_calculation_blocksize_64)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_64)

        label_65 = QLabel("    reflections")
        label_65.setPalette(palette_scope)
        label_65.setFont(QFont("Monospace"))
        bg_box.addWidget(label_65)
        hbox_lay_reflections_per_degree_66 =  QHBoxLayout()
        label_reflections_per_degree_66 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_66.setPalette(palette_object)
        label_reflections_per_degree_66.setFont(QFont("Monospace"))
        hbox_lay_reflections_per_degree_66.addWidget(label_reflections_per_degree_66)

        box_reflections_per_degree_66 = QDoubleSpinBox()
        box_reflections_per_degree_66.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_66.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_66.addWidget(box_reflections_per_degree_66)
        bg_box.addLayout(hbox_lay_reflections_per_degree_66)

        hbox_lay_minimum_sample_size_67 =  QHBoxLayout()
        label_minimum_sample_size_67 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_67.setPalette(palette_object)
        label_minimum_sample_size_67.setFont(QFont("Monospace"))
        hbox_lay_minimum_sample_size_67.addWidget(label_minimum_sample_size_67)

        box_minimum_sample_size_67 = QSpinBox()
        box_minimum_sample_size_67.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_67.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_67.addWidget(box_minimum_sample_size_67)
        bg_box.addLayout(hbox_lay_minimum_sample_size_67)

        hbox_lay_maximum_sample_size_68 =  QHBoxLayout()
        label_maximum_sample_size_68 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_68.setPalette(palette_object)
        label_maximum_sample_size_68.setFont(QFont("Monospace"))
        hbox_lay_maximum_sample_size_68.addWidget(label_maximum_sample_size_68)

        box_maximum_sample_size_68 = QSpinBox()
        box_maximum_sample_size_68.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_68.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_68.addWidget(box_maximum_sample_size_68)
        bg_box.addLayout(hbox_lay_maximum_sample_size_68)

        hbox_lay_use_all_reflections_69 =  QHBoxLayout()
        label_use_all_reflections_69 = QLabel("        use_all_reflections")
        label_use_all_reflections_69.setPalette(palette_object)
        label_use_all_reflections_69.setFont(QFont("Monospace"))
        hbox_lay_use_all_reflections_69.addWidget(label_use_all_reflections_69)

        box_use_all_reflections_69 = QComboBox()
        box_use_all_reflections_69.local_path = "refinement.reflections.use_all_reflections"
        box_use_all_reflections_69.tmp_lst=[]
        box_use_all_reflections_69.tmp_lst.append("True")
        box_use_all_reflections_69.tmp_lst.append("False")
        for lst_itm in box_use_all_reflections_69.tmp_lst:
            box_use_all_reflections_69.addItem(lst_itm)
        box_use_all_reflections_69.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_use_all_reflections_69.addWidget(box_use_all_reflections_69)
        bg_box.addLayout(hbox_lay_use_all_reflections_69)

        hbox_lay_random_seed_70 =  QHBoxLayout()
        label_random_seed_70 = QLabel("        random_seed")
        label_random_seed_70.setPalette(palette_object)
        label_random_seed_70.setFont(QFont("Monospace"))
        hbox_lay_random_seed_70.addWidget(label_random_seed_70)

        box_random_seed_70 = QSpinBox()
        box_random_seed_70.local_path = "refinement.reflections.random_seed"
        box_random_seed_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_70.addWidget(box_random_seed_70)
        bg_box.addLayout(hbox_lay_random_seed_70)

        hbox_lay_close_to_spindle_cutoff_71 =  QHBoxLayout()
        label_close_to_spindle_cutoff_71 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_71.setPalette(palette_object)
        label_close_to_spindle_cutoff_71.setFont(QFont("Monospace"))
        hbox_lay_close_to_spindle_cutoff_71.addWidget(label_close_to_spindle_cutoff_71)

        box_close_to_spindle_cutoff_71 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_71.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_71.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_71.addWidget(box_close_to_spindle_cutoff_71)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_71)

        hbox_lay_block_width_72 =  QHBoxLayout()
        label_block_width_72 = QLabel("        block_width")
        label_block_width_72.setPalette(palette_object)
        label_block_width_72.setFont(QFont("Monospace"))
        hbox_lay_block_width_72.addWidget(label_block_width_72)

        box_block_width_72 = QDoubleSpinBox()
        box_block_width_72.local_path = "refinement.reflections.block_width"
        box_block_width_72.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_72.addWidget(box_block_width_72)
        bg_box.addLayout(hbox_lay_block_width_72)

        label_73 = QLabel("        weighting_strategy")
        label_73.setPalette(palette_scope)
        label_73.setFont(QFont("Monospace"))
        bg_box.addWidget(label_73)
        hbox_lay_override_74 =  QHBoxLayout()
        label_override_74 = QLabel("            override")
        label_override_74.setPalette(palette_object)
        label_override_74.setFont(QFont("Monospace"))
        hbox_lay_override_74.addWidget(label_override_74)

        box_override_74 = QComboBox()
        box_override_74.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_74.tmp_lst=[]
        box_override_74.tmp_lst.append("statistical")
        box_override_74.tmp_lst.append("stills")
        box_override_74.tmp_lst.append("constant")
        for lst_itm in box_override_74.tmp_lst:
            box_override_74.addItem(lst_itm)
        box_override_74.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_74.addWidget(box_override_74)
        bg_box.addLayout(hbox_lay_override_74)

        hbox_lay_delpsi_constant_75 =  QHBoxLayout()
        label_delpsi_constant_75 = QLabel("            delpsi_constant")
        label_delpsi_constant_75.setPalette(palette_object)
        label_delpsi_constant_75.setFont(QFont("Monospace"))
        hbox_lay_delpsi_constant_75.addWidget(label_delpsi_constant_75)

        box_delpsi_constant_75 = QDoubleSpinBox()
        box_delpsi_constant_75.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_75.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_75.addWidget(box_delpsi_constant_75)
        bg_box.addLayout(hbox_lay_delpsi_constant_75)

        hbox_lay_constants_76_0 =  QHBoxLayout()
        label_constants_76_0 = QLabel("            constants[1]")
        label_constants_76_0.setPalette(palette_object)
        label_constants_76_0.setFont(QFont("Monospace"))
        hbox_lay_constants_76_0.addWidget(label_constants_76_0)
        box_constants_76_0 = QDoubleSpinBox()
        box_constants_76_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_76_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_76_1 =  QHBoxLayout()
        label_constants_76_1 = QLabel("            constants[2]")
        label_constants_76_1.setPalette(palette_object)
        label_constants_76_1.setFont(QFont("Monospace"))
        hbox_lay_constants_76_1.addWidget(label_constants_76_1)
        box_constants_76_1 = QDoubleSpinBox()
        box_constants_76_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_76_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_76_2 =  QHBoxLayout()
        label_constants_76_2 = QLabel("            constants[3]")
        label_constants_76_2.setPalette(palette_object)
        label_constants_76_2.setFont(QFont("Monospace"))
        hbox_lay_constants_76_2.addWidget(label_constants_76_2)
        box_constants_76_2 = QDoubleSpinBox()
        box_constants_76_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_76_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_76_0.addWidget(box_constants_76_0)
        bg_box.addLayout(hbox_lay_constants_76_0)

        hbox_lay_constants_76_1.addWidget(box_constants_76_1)
        bg_box.addLayout(hbox_lay_constants_76_1)

        hbox_lay_constants_76_2.addWidget(box_constants_76_2)
        bg_box.addLayout(hbox_lay_constants_76_2)

        label_77 = QLabel("        outlier")
        label_77.setPalette(palette_scope)
        label_77.setFont(QFont("Monospace"))
        bg_box.addWidget(label_77)
        hbox_lay_algorithm_78 =  QHBoxLayout()
        label_algorithm_78 = QLabel("            algorithm")
        label_algorithm_78.setPalette(palette_object)
        label_algorithm_78.setFont(QFont("Monospace"))
        hbox_lay_algorithm_78.addWidget(label_algorithm_78)

        box_algorithm_78 = QComboBox()
        box_algorithm_78.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_78.tmp_lst=[]
        box_algorithm_78.tmp_lst.append("null")
        box_algorithm_78.tmp_lst.append("*auto")
        box_algorithm_78.tmp_lst.append("mcd")
        box_algorithm_78.tmp_lst.append("tukey")
        box_algorithm_78.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_78.tmp_lst:
            box_algorithm_78.addItem(lst_itm)
        box_algorithm_78.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_78.addWidget(box_algorithm_78)
        bg_box.addLayout(hbox_lay_algorithm_78)

        hbox_lay_minimum_number_of_reflections_79 =  QHBoxLayout()
        label_minimum_number_of_reflections_79 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_79.setPalette(palette_object)
        label_minimum_number_of_reflections_79.setFont(QFont("Monospace"))
        hbox_lay_minimum_number_of_reflections_79.addWidget(label_minimum_number_of_reflections_79)

        box_minimum_number_of_reflections_79 = QSpinBox()
        box_minimum_number_of_reflections_79.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_79.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_79.addWidget(box_minimum_number_of_reflections_79)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_79)

        hbox_lay_separate_experiments_80 =  QHBoxLayout()
        label_separate_experiments_80 = QLabel("            separate_experiments")
        label_separate_experiments_80.setPalette(palette_object)
        label_separate_experiments_80.setFont(QFont("Monospace"))
        hbox_lay_separate_experiments_80.addWidget(label_separate_experiments_80)

        box_separate_experiments_80 = QComboBox()
        box_separate_experiments_80.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_80.tmp_lst=[]
        box_separate_experiments_80.tmp_lst.append("True")
        box_separate_experiments_80.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_80.tmp_lst:
            box_separate_experiments_80.addItem(lst_itm)
        box_separate_experiments_80.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_80.addWidget(box_separate_experiments_80)
        bg_box.addLayout(hbox_lay_separate_experiments_80)

        hbox_lay_separate_panels_81 =  QHBoxLayout()
        label_separate_panels_81 = QLabel("            separate_panels")
        label_separate_panels_81.setPalette(palette_object)
        label_separate_panels_81.setFont(QFont("Monospace"))
        hbox_lay_separate_panels_81.addWidget(label_separate_panels_81)

        box_separate_panels_81 = QComboBox()
        box_separate_panels_81.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_81.tmp_lst=[]
        box_separate_panels_81.tmp_lst.append("True")
        box_separate_panels_81.tmp_lst.append("False")
        for lst_itm in box_separate_panels_81.tmp_lst:
            box_separate_panels_81.addItem(lst_itm)
        box_separate_panels_81.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_81.addWidget(box_separate_panels_81)
        bg_box.addLayout(hbox_lay_separate_panels_81)

        label_82 = QLabel("            tukey")
        label_82.setPalette(palette_scope)
        label_82.setFont(QFont("Monospace"))
        bg_box.addWidget(label_82)
        hbox_lay_iqr_multiplier_83 =  QHBoxLayout()
        label_iqr_multiplier_83 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_83.setPalette(palette_object)
        label_iqr_multiplier_83.setFont(QFont("Monospace"))
        hbox_lay_iqr_multiplier_83.addWidget(label_iqr_multiplier_83)

        box_iqr_multiplier_83 = QDoubleSpinBox()
        box_iqr_multiplier_83.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_83.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_83.addWidget(box_iqr_multiplier_83)
        bg_box.addLayout(hbox_lay_iqr_multiplier_83)

        label_84 = QLabel("            mcd")
        label_84.setPalette(palette_scope)
        label_84.setFont(QFont("Monospace"))
        bg_box.addWidget(label_84)
        hbox_lay_alpha_85 =  QHBoxLayout()
        label_alpha_85 = QLabel("                alpha")
        label_alpha_85.setPalette(palette_object)
        label_alpha_85.setFont(QFont("Monospace"))
        hbox_lay_alpha_85.addWidget(label_alpha_85)

        box_alpha_85 = QDoubleSpinBox()
        box_alpha_85.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_85.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_85.addWidget(box_alpha_85)
        bg_box.addLayout(hbox_lay_alpha_85)

        hbox_lay_max_n_groups_86 =  QHBoxLayout()
        label_max_n_groups_86 = QLabel("                max_n_groups")
        label_max_n_groups_86.setPalette(palette_object)
        label_max_n_groups_86.setFont(QFont("Monospace"))
        hbox_lay_max_n_groups_86.addWidget(label_max_n_groups_86)

        box_max_n_groups_86 = QSpinBox()
        box_max_n_groups_86.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_86.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_86.addWidget(box_max_n_groups_86)
        bg_box.addLayout(hbox_lay_max_n_groups_86)

        hbox_lay_min_group_size_87 =  QHBoxLayout()
        label_min_group_size_87 = QLabel("                min_group_size")
        label_min_group_size_87.setPalette(palette_object)
        label_min_group_size_87.setFont(QFont("Monospace"))
        hbox_lay_min_group_size_87.addWidget(label_min_group_size_87)

        box_min_group_size_87 = QSpinBox()
        box_min_group_size_87.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_87.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_87.addWidget(box_min_group_size_87)
        bg_box.addLayout(hbox_lay_min_group_size_87)

        hbox_lay_n_trials_88 =  QHBoxLayout()
        label_n_trials_88 = QLabel("                n_trials")
        label_n_trials_88.setPalette(palette_object)
        label_n_trials_88.setFont(QFont("Monospace"))
        hbox_lay_n_trials_88.addWidget(label_n_trials_88)

        box_n_trials_88 = QSpinBox()
        box_n_trials_88.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_88.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_88.addWidget(box_n_trials_88)
        bg_box.addLayout(hbox_lay_n_trials_88)

        hbox_lay_k1_89 =  QHBoxLayout()
        label_k1_89 = QLabel("                k1")
        label_k1_89.setPalette(palette_object)
        label_k1_89.setFont(QFont("Monospace"))
        hbox_lay_k1_89.addWidget(label_k1_89)

        box_k1_89 = QSpinBox()
        box_k1_89.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_89.addWidget(box_k1_89)
        bg_box.addLayout(hbox_lay_k1_89)

        hbox_lay_k2_90 =  QHBoxLayout()
        label_k2_90 = QLabel("                k2")
        label_k2_90.setPalette(palette_object)
        label_k2_90.setFont(QFont("Monospace"))
        hbox_lay_k2_90.addWidget(label_k2_90)

        box_k2_90 = QSpinBox()
        box_k2_90.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_90.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_90.addWidget(box_k2_90)
        bg_box.addLayout(hbox_lay_k2_90)

        hbox_lay_k3_91 =  QHBoxLayout()
        label_k3_91 = QLabel("                k3")
        label_k3_91.setPalette(palette_object)
        label_k3_91.setFont(QFont("Monospace"))
        hbox_lay_k3_91.addWidget(label_k3_91)

        box_k3_91 = QSpinBox()
        box_k3_91.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_91.addWidget(box_k3_91)
        bg_box.addLayout(hbox_lay_k3_91)

        hbox_lay_threshold_probability_92 =  QHBoxLayout()
        label_threshold_probability_92 = QLabel("                threshold_probability")
        label_threshold_probability_92.setPalette(palette_object)
        label_threshold_probability_92.setFont(QFont("Monospace"))
        hbox_lay_threshold_probability_92.addWidget(label_threshold_probability_92)

        box_threshold_probability_92 = QDoubleSpinBox()
        box_threshold_probability_92.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_92.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_92.addWidget(box_threshold_probability_92)
        bg_box.addLayout(hbox_lay_threshold_probability_92)

        label_93 = QLabel("            sauter_poon")
        label_93.setPalette(palette_scope)
        label_93.setFont(QFont("Monospace"))
        bg_box.addWidget(label_93)
        hbox_lay_px_sz_94_0 =  QHBoxLayout()
        label_px_sz_94_0 = QLabel("                px_sz[1]")
        label_px_sz_94_0.setPalette(palette_object)
        label_px_sz_94_0.setFont(QFont("Monospace"))
        hbox_lay_px_sz_94_0.addWidget(label_px_sz_94_0)
        box_px_sz_94_0 = QDoubleSpinBox()
        box_px_sz_94_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_94_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_94_1 =  QHBoxLayout()
        label_px_sz_94_1 = QLabel("                px_sz[2]")
        label_px_sz_94_1.setPalette(palette_object)
        label_px_sz_94_1.setFont(QFont("Monospace"))
        hbox_lay_px_sz_94_1.addWidget(label_px_sz_94_1)
        box_px_sz_94_1 = QDoubleSpinBox()
        box_px_sz_94_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_94_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_94_0.addWidget(box_px_sz_94_0)
        bg_box.addLayout(hbox_lay_px_sz_94_0)

        hbox_lay_px_sz_94_1.addWidget(box_px_sz_94_1)
        bg_box.addLayout(hbox_lay_px_sz_94_1)

        hbox_lay_verbose_95 =  QHBoxLayout()
        label_verbose_95 = QLabel("                verbose")
        label_verbose_95.setPalette(palette_object)
        label_verbose_95.setFont(QFont("Monospace"))
        hbox_lay_verbose_95.addWidget(label_verbose_95)

        box_verbose_95 = QComboBox()
        box_verbose_95.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_95.tmp_lst=[]
        box_verbose_95.tmp_lst.append("True")
        box_verbose_95.tmp_lst.append("False")
        for lst_itm in box_verbose_95.tmp_lst:
            box_verbose_95.addItem(lst_itm)
        box_verbose_95.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_95.addWidget(box_verbose_95)
        bg_box.addLayout(hbox_lay_verbose_95)

        hbox_lay_pdf_96 =  QHBoxLayout()
        label_pdf_96 = QLabel("                pdf")
        label_pdf_96.setPalette(palette_object)
        label_pdf_96.setFont(QFont("Monospace"))
        hbox_lay_pdf_96.addWidget(label_pdf_96)

        box_pdf_96 = QLineEdit()
        box_pdf_96.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_96.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_96.addWidget(box_pdf_96)
        bg_box.addLayout(hbox_lay_pdf_96)

 
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
