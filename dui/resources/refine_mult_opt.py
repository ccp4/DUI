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

        hbox_lay_experiments_1 =  QHBoxLayout()
        label_experiments_1 = QLabel("    experiments")
        label_experiments_1.setPalette(palette_object)
        label_experiments_1.setFont(QFont("Monospace", 10))
        hbox_lay_experiments_1.addWidget(label_experiments_1)

        box_experiments_1 = QLineEdit()
        box_experiments_1.local_path = "output.experiments"
        box_experiments_1.textChanged.connect(self.spnbox_changed)
        hbox_lay_experiments_1.addWidget(box_experiments_1)
        bg_box.addLayout(hbox_lay_experiments_1)

        hbox_lay_reflections_2 =  QHBoxLayout()
        label_reflections_2 = QLabel("    reflections")
        label_reflections_2.setPalette(palette_object)
        label_reflections_2.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_2.addWidget(label_reflections_2)

        box_reflections_2 = QLineEdit()
        box_reflections_2.local_path = "output.reflections"
        box_reflections_2.textChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_2.addWidget(box_reflections_2)
        bg_box.addLayout(hbox_lay_reflections_2)

        hbox_lay_include_unused_reflections_3 =  QHBoxLayout()
        label_include_unused_reflections_3 = QLabel("    include_unused_reflections")
        label_include_unused_reflections_3.setPalette(palette_object)
        label_include_unused_reflections_3.setFont(QFont("Monospace", 10))
        hbox_lay_include_unused_reflections_3.addWidget(label_include_unused_reflections_3)

        box_include_unused_reflections_3 = QComboBox()
        box_include_unused_reflections_3.local_path = "output.include_unused_reflections"
        box_include_unused_reflections_3.tmp_lst=[]
        box_include_unused_reflections_3.tmp_lst.append("True")
        box_include_unused_reflections_3.tmp_lst.append("False")
        for lst_itm in box_include_unused_reflections_3.tmp_lst:
            box_include_unused_reflections_3.addItem(lst_itm)
        box_include_unused_reflections_3.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_include_unused_reflections_3.addWidget(box_include_unused_reflections_3)
        bg_box.addLayout(hbox_lay_include_unused_reflections_3)

        hbox_lay_matches_4 =  QHBoxLayout()
        label_matches_4 = QLabel("    matches")
        label_matches_4.setPalette(palette_object)
        label_matches_4.setFont(QFont("Monospace", 10))
        hbox_lay_matches_4.addWidget(label_matches_4)

        box_matches_4 = QLineEdit()
        box_matches_4.local_path = "output.matches"
        box_matches_4.textChanged.connect(self.spnbox_changed)
        hbox_lay_matches_4.addWidget(box_matches_4)
        bg_box.addLayout(hbox_lay_matches_4)

        hbox_lay_centroids_5 =  QHBoxLayout()
        label_centroids_5 = QLabel("    centroids")
        label_centroids_5.setPalette(palette_object)
        label_centroids_5.setFont(QFont("Monospace", 10))
        hbox_lay_centroids_5.addWidget(label_centroids_5)

        box_centroids_5 = QLineEdit()
        box_centroids_5.local_path = "output.centroids"
        box_centroids_5.textChanged.connect(self.spnbox_changed)
        hbox_lay_centroids_5.addWidget(box_centroids_5)
        bg_box.addLayout(hbox_lay_centroids_5)

        hbox_lay_parameter_table_6 =  QHBoxLayout()
        label_parameter_table_6 = QLabel("    parameter_table")
        label_parameter_table_6.setPalette(palette_object)
        label_parameter_table_6.setFont(QFont("Monospace", 10))
        hbox_lay_parameter_table_6.addWidget(label_parameter_table_6)

        box_parameter_table_6 = QLineEdit()
        box_parameter_table_6.local_path = "output.parameter_table"
        box_parameter_table_6.textChanged.connect(self.spnbox_changed)
        hbox_lay_parameter_table_6.addWidget(box_parameter_table_6)
        bg_box.addLayout(hbox_lay_parameter_table_6)

        hbox_lay_log_7 =  QHBoxLayout()
        label_log_7 = QLabel("    log")
        label_log_7.setPalette(palette_object)
        label_log_7.setFont(QFont("Monospace", 10))
        hbox_lay_log_7.addWidget(label_log_7)

        box_log_7 = QLineEdit()
        box_log_7.local_path = "output.log"
        box_log_7.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_7.addWidget(box_log_7)
        bg_box.addLayout(hbox_lay_log_7)

        hbox_lay_debug_log_8 =  QHBoxLayout()
        label_debug_log_8 = QLabel("    debug_log")
        label_debug_log_8.setPalette(palette_object)
        label_debug_log_8.setFont(QFont("Monospace", 10))
        hbox_lay_debug_log_8.addWidget(label_debug_log_8)

        box_debug_log_8 = QLineEdit()
        box_debug_log_8.local_path = "output.debug_log"
        box_debug_log_8.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_8.addWidget(box_debug_log_8)
        bg_box.addLayout(hbox_lay_debug_log_8)

        label_9 = QLabel("    correlation_plot")
        label_9.setPalette(palette_scope)
        label_9.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_9)

        hbox_lay_filename_10 =  QHBoxLayout()
        label_filename_10 = QLabel("        filename")
        label_filename_10.setPalette(palette_object)
        label_filename_10.setFont(QFont("Monospace", 10))
        hbox_lay_filename_10.addWidget(label_filename_10)

        box_filename_10 = QLineEdit()
        box_filename_10.local_path = "output.correlation_plot.filename"
        box_filename_10.textChanged.connect(self.spnbox_changed)
        hbox_lay_filename_10.addWidget(box_filename_10)
        bg_box.addLayout(hbox_lay_filename_10)



        hbox_lay_history_13 =  QHBoxLayout()
        label_history_13 = QLabel("    history")
        label_history_13.setPalette(palette_object)
        label_history_13.setFont(QFont("Monospace", 10))
        hbox_lay_history_13.addWidget(label_history_13)

        box_history_13 = QLineEdit()
        box_history_13.local_path = "output.history"
        box_history_13.textChanged.connect(self.spnbox_changed)
        hbox_lay_history_13.addWidget(box_history_13)
        bg_box.addLayout(hbox_lay_history_13)

        label_14 = QLabel("refinement")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_14)

        label_15 = QLabel("    mp")
        label_15.setPalette(palette_scope)
        label_15.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_15)

        hbox_lay_nproc_16 =  QHBoxLayout()
        label_nproc_16 = QLabel("        nproc")
        label_nproc_16.setPalette(palette_object)
        label_nproc_16.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_16.addWidget(label_nproc_16)

        box_nproc_16 = QSpinBox()
        box_nproc_16.setValue(1)
        box_nproc_16.local_path = "refinement.mp.nproc"
        box_nproc_16.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_16.addWidget(box_nproc_16)
        bg_box.addLayout(hbox_lay_nproc_16)

        hbox_lay_verbosity_17 =  QHBoxLayout()
        label_verbosity_17 = QLabel("    verbosity")
        label_verbosity_17.setPalette(palette_object)
        label_verbosity_17.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_17.addWidget(label_verbosity_17)

        box_verbosity_17 = QSpinBox()
        box_verbosity_17.setValue(0)
        box_verbosity_17.local_path = "refinement.verbosity"
        box_verbosity_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_17.addWidget(box_verbosity_17)
        bg_box.addLayout(hbox_lay_verbosity_17)

        label_18 = QLabel("    parameterisation")
        label_18.setPalette(palette_scope)
        label_18.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_18)

        label_19 = QLabel("        auto_reduction")
        label_19.setPalette(palette_scope)
        label_19.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_19)

        hbox_lay_min_nref_per_parameter_20 =  QHBoxLayout()
        label_min_nref_per_parameter_20 = QLabel("            min_nref_per_parameter")
        label_min_nref_per_parameter_20.setPalette(palette_object)
        label_min_nref_per_parameter_20.setFont(QFont("Monospace", 10))
        hbox_lay_min_nref_per_parameter_20.addWidget(label_min_nref_per_parameter_20)

        box_min_nref_per_parameter_20 = QSpinBox()
        box_min_nref_per_parameter_20.setValue(5)
        box_min_nref_per_parameter_20.local_path = "refinement.parameterisation.auto_reduction.min_nref_per_parameter"
        box_min_nref_per_parameter_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_nref_per_parameter_20.addWidget(box_min_nref_per_parameter_20)
        bg_box.addLayout(hbox_lay_min_nref_per_parameter_20)

        hbox_lay_action_21 =  QHBoxLayout()
        label_action_21 = QLabel("            action")
        label_action_21.setPalette(palette_object)
        label_action_21.setFont(QFont("Monospace", 10))
        hbox_lay_action_21.addWidget(label_action_21)

        box_action_21 = QComboBox()
        box_action_21.local_path = "refinement.parameterisation.auto_reduction.action"
        box_action_21.tmp_lst=[]
        box_action_21.tmp_lst.append("fail")
        box_action_21.tmp_lst.append("fix")
        box_action_21.tmp_lst.append("remove")
        for lst_itm in box_action_21.tmp_lst:
            box_action_21.addItem(lst_itm)
        box_action_21.setCurrentIndex(0)
        box_action_21.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_action_21.addWidget(box_action_21)
        bg_box.addLayout(hbox_lay_action_21)

        hbox_lay_scan_varying_22 =  QHBoxLayout()
        label_scan_varying_22 = QLabel("        scan_varying")
        label_scan_varying_22.setPalette(palette_object)
        label_scan_varying_22.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_22.addWidget(label_scan_varying_22)

        box_scan_varying_22 = QComboBox()
        box_scan_varying_22.local_path = "refinement.parameterisation.scan_varying"
        box_scan_varying_22.tmp_lst=[]
        box_scan_varying_22.tmp_lst.append("True")
        box_scan_varying_22.tmp_lst.append("False")
        for lst_itm in box_scan_varying_22.tmp_lst:
            box_scan_varying_22.addItem(lst_itm)
        box_scan_varying_22.setCurrentIndex(1)
        box_scan_varying_22.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_22.addWidget(box_scan_varying_22)
        bg_box.addLayout(hbox_lay_scan_varying_22)

        hbox_lay_compose_model_per_23 =  QHBoxLayout()
        label_compose_model_per_23 = QLabel("        compose_model_per")
        label_compose_model_per_23.setPalette(palette_object)
        label_compose_model_per_23.setFont(QFont("Monospace", 10))
        hbox_lay_compose_model_per_23.addWidget(label_compose_model_per_23)

        box_compose_model_per_23 = QComboBox()
        box_compose_model_per_23.local_path = "refinement.parameterisation.compose_model_per"
        box_compose_model_per_23.tmp_lst=[]
        box_compose_model_per_23.tmp_lst.append("reflection")
        box_compose_model_per_23.tmp_lst.append("image")
        box_compose_model_per_23.tmp_lst.append("block")
        for lst_itm in box_compose_model_per_23.tmp_lst:
            box_compose_model_per_23.addItem(lst_itm)
        box_compose_model_per_23.setCurrentIndex(2)
        box_compose_model_per_23.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_compose_model_per_23.addWidget(box_compose_model_per_23)
        bg_box.addLayout(hbox_lay_compose_model_per_23)

        label_24 = QLabel("        beam")
        label_24.setPalette(palette_scope)
        label_24.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_24)

        hbox_lay_fix_25 =  QHBoxLayout()
        label_fix_25 = QLabel("            fix")
        label_fix_25.setPalette(palette_object)
        label_fix_25.setFont(QFont("Monospace", 10))
        hbox_lay_fix_25.addWidget(label_fix_25)

        box_fix_25 = QComboBox()
        box_fix_25.local_path = "refinement.parameterisation.beam.fix"
        box_fix_25.tmp_lst=[]
        box_fix_25.tmp_lst.append("all")
        box_fix_25.tmp_lst.append("in_spindle_plane")
        box_fix_25.tmp_lst.append("out_spindle_plane")
        box_fix_25.tmp_lst.append("wavelength")
        for lst_itm in box_fix_25.tmp_lst:
            box_fix_25.addItem(lst_itm)
        box_fix_25.setCurrentIndex(3)
        box_fix_25.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_25.addWidget(box_fix_25)
        bg_box.addLayout(hbox_lay_fix_25)


        hbox_lay_force_static_27 =  QHBoxLayout()
        label_force_static_27 = QLabel("            force_static")
        label_force_static_27.setPalette(palette_object)
        label_force_static_27.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_27.addWidget(label_force_static_27)

        box_force_static_27 = QComboBox()
        box_force_static_27.local_path = "refinement.parameterisation.beam.force_static"
        box_force_static_27.tmp_lst=[]
        box_force_static_27.tmp_lst.append("True")
        box_force_static_27.tmp_lst.append("False")
        for lst_itm in box_force_static_27.tmp_lst:
            box_force_static_27.addItem(lst_itm)
        box_force_static_27.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_27.addWidget(box_force_static_27)
        bg_box.addLayout(hbox_lay_force_static_27)

        label_28 = QLabel("            smoother")
        label_28.setPalette(palette_scope)
        label_28.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_28)

        hbox_lay_num_intervals_29 =  QHBoxLayout()
        label_num_intervals_29 = QLabel("                num_intervals")
        label_num_intervals_29.setPalette(palette_object)
        label_num_intervals_29.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_29.addWidget(label_num_intervals_29)

        box_num_intervals_29 = QComboBox()
        box_num_intervals_29.local_path = "refinement.parameterisation.beam.smoother.num_intervals"
        box_num_intervals_29.tmp_lst=[]
        box_num_intervals_29.tmp_lst.append("fixed_width")
        box_num_intervals_29.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_29.tmp_lst:
            box_num_intervals_29.addItem(lst_itm)
        box_num_intervals_29.setCurrentIndex(0)
        box_num_intervals_29.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_29.addWidget(box_num_intervals_29)
        bg_box.addLayout(hbox_lay_num_intervals_29)

        hbox_lay_interval_width_degrees_30 =  QHBoxLayout()
        label_interval_width_degrees_30 = QLabel("                interval_width_degrees")
        label_interval_width_degrees_30.setPalette(palette_object)
        label_interval_width_degrees_30.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_30.addWidget(label_interval_width_degrees_30)

        box_interval_width_degrees_30 = QDoubleSpinBox()
        box_interval_width_degrees_30.setValue(36.0)
        box_interval_width_degrees_30.local_path = "refinement.parameterisation.beam.smoother.interval_width_degrees"
        box_interval_width_degrees_30.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_30.addWidget(box_interval_width_degrees_30)
        bg_box.addLayout(hbox_lay_interval_width_degrees_30)

        hbox_lay_absolute_num_intervals_31 =  QHBoxLayout()
        label_absolute_num_intervals_31 = QLabel("                absolute_num_intervals")
        label_absolute_num_intervals_31.setPalette(palette_object)
        label_absolute_num_intervals_31.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_31.addWidget(label_absolute_num_intervals_31)

        box_absolute_num_intervals_31 = QSpinBox()
        box_absolute_num_intervals_31.setValue(5)
        box_absolute_num_intervals_31.local_path = "refinement.parameterisation.beam.smoother.absolute_num_intervals"
        box_absolute_num_intervals_31.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_31.addWidget(box_absolute_num_intervals_31)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_31)

        label_32 = QLabel("        crystal")
        label_32.setPalette(palette_scope)
        label_32.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_32)

        hbox_lay_fix_33 =  QHBoxLayout()
        label_fix_33 = QLabel("            fix")
        label_fix_33.setPalette(palette_object)
        label_fix_33.setFont(QFont("Monospace", 10))
        hbox_lay_fix_33.addWidget(label_fix_33)

        box_fix_33 = QComboBox()
        box_fix_33.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_33.tmp_lst=[]
        box_fix_33.tmp_lst.append("all")
        box_fix_33.tmp_lst.append("cell")
        box_fix_33.tmp_lst.append("orientation")
        for lst_itm in box_fix_33.tmp_lst:
            box_fix_33.addItem(lst_itm)
        box_fix_33.setCurrentIndex(0)
        box_fix_33.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_33.addWidget(box_fix_33)
        bg_box.addLayout(hbox_lay_fix_33)

        label_34 = QLabel("            unit_cell")
        label_34.setPalette(palette_scope)
        label_34.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_34)


        label_36 = QLabel("                restraints")
        label_36.setPalette(palette_scope)
        label_36.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_36)

        label_37 = QLabel("                    tie_to_target")
        label_37.setPalette(palette_scope)
        label_37.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_37)

        hbox_lay_values_38_0 =  QHBoxLayout()
        label_values_38_0 = QLabel("                        values[1]")
        label_values_38_0.setPalette(palette_object)
        label_values_38_0.setFont(QFont("Monospace", 10))
        hbox_lay_values_38_0.addWidget(label_values_38_0)
        box_values_38_0 = QDoubleSpinBox()
        box_values_38_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_38_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_38_1 =  QHBoxLayout()
        label_values_38_1 = QLabel("                        values[2]")
        label_values_38_1.setPalette(palette_object)
        label_values_38_1.setFont(QFont("Monospace", 10))
        hbox_lay_values_38_1.addWidget(label_values_38_1)
        box_values_38_1 = QDoubleSpinBox()
        box_values_38_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_38_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_38_2 =  QHBoxLayout()
        label_values_38_2 = QLabel("                        values[3]")
        label_values_38_2.setPalette(palette_object)
        label_values_38_2.setFont(QFont("Monospace", 10))
        hbox_lay_values_38_2.addWidget(label_values_38_2)
        box_values_38_2 = QDoubleSpinBox()
        box_values_38_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_38_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_38_3 =  QHBoxLayout()
        label_values_38_3 = QLabel("                        values[4]")
        label_values_38_3.setPalette(palette_object)
        label_values_38_3.setFont(QFont("Monospace", 10))
        hbox_lay_values_38_3.addWidget(label_values_38_3)
        box_values_38_3 = QDoubleSpinBox()
        box_values_38_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_38_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_38_4 =  QHBoxLayout()
        label_values_38_4 = QLabel("                        values[5]")
        label_values_38_4.setPalette(palette_object)
        label_values_38_4.setFont(QFont("Monospace", 10))
        hbox_lay_values_38_4.addWidget(label_values_38_4)
        box_values_38_4 = QDoubleSpinBox()
        box_values_38_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_38_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_38_5 =  QHBoxLayout()
        label_values_38_5 = QLabel("                        values[6]")
        label_values_38_5.setPalette(palette_object)
        label_values_38_5.setFont(QFont("Monospace", 10))
        hbox_lay_values_38_5.addWidget(label_values_38_5)
        box_values_38_5 = QDoubleSpinBox()
        box_values_38_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_38_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_sigmas_39_0 =  QHBoxLayout()
        label_sigmas_39_0 = QLabel("                        sigmas[1]")
        label_sigmas_39_0.setPalette(palette_object)
        label_sigmas_39_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_39_0.addWidget(label_sigmas_39_0)
        box_sigmas_39_0 = QDoubleSpinBox()
        box_sigmas_39_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_39_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_39_1 =  QHBoxLayout()
        label_sigmas_39_1 = QLabel("                        sigmas[2]")
        label_sigmas_39_1.setPalette(palette_object)
        label_sigmas_39_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_39_1.addWidget(label_sigmas_39_1)
        box_sigmas_39_1 = QDoubleSpinBox()
        box_sigmas_39_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_39_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_39_2 =  QHBoxLayout()
        label_sigmas_39_2 = QLabel("                        sigmas[3]")
        label_sigmas_39_2.setPalette(palette_object)
        label_sigmas_39_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_39_2.addWidget(label_sigmas_39_2)
        box_sigmas_39_2 = QDoubleSpinBox()
        box_sigmas_39_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_39_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_39_3 =  QHBoxLayout()
        label_sigmas_39_3 = QLabel("                        sigmas[4]")
        label_sigmas_39_3.setPalette(palette_object)
        label_sigmas_39_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_39_3.addWidget(label_sigmas_39_3)
        box_sigmas_39_3 = QDoubleSpinBox()
        box_sigmas_39_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_39_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_39_4 =  QHBoxLayout()
        label_sigmas_39_4 = QLabel("                        sigmas[5]")
        label_sigmas_39_4.setPalette(palette_object)
        label_sigmas_39_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_39_4.addWidget(label_sigmas_39_4)
        box_sigmas_39_4 = QDoubleSpinBox()
        box_sigmas_39_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_39_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_39_5 =  QHBoxLayout()
        label_sigmas_39_5 = QLabel("                        sigmas[6]")
        label_sigmas_39_5.setPalette(palette_object)
        label_sigmas_39_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_39_5.addWidget(label_sigmas_39_5)
        box_sigmas_39_5 = QDoubleSpinBox()
        box_sigmas_39_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_39_5.valueChanged.connect(self.spnbox_changed)


        hbox_lay_apply_to_all_41 =  QHBoxLayout()
        label_apply_to_all_41 = QLabel("                        apply_to_all")
        label_apply_to_all_41.setPalette(palette_object)
        label_apply_to_all_41.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_41.addWidget(label_apply_to_all_41)

        box_apply_to_all_41 = QComboBox()
        box_apply_to_all_41.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.apply_to_all"
        box_apply_to_all_41.tmp_lst=[]
        box_apply_to_all_41.tmp_lst.append("True")
        box_apply_to_all_41.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_41.tmp_lst:
            box_apply_to_all_41.addItem(lst_itm)
        box_apply_to_all_41.setCurrentIndex(1)
        box_apply_to_all_41.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_41.addWidget(box_apply_to_all_41)
        bg_box.addLayout(hbox_lay_apply_to_all_41)

        label_42 = QLabel("                    tie_to_group")
        label_42.setPalette(palette_scope)
        label_42.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_42)

        hbox_lay_target_43 =  QHBoxLayout()
        label_target_43 = QLabel("                        target")
        label_target_43.setPalette(palette_object)
        label_target_43.setFont(QFont("Monospace", 10))
        hbox_lay_target_43.addWidget(label_target_43)

        box_target_43 = QComboBox()
        box_target_43.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_43.tmp_lst=[]
        box_target_43.tmp_lst.append("mean")
        box_target_43.tmp_lst.append("low_memory_mean")
        box_target_43.tmp_lst.append("median")
        for lst_itm in box_target_43.tmp_lst:
            box_target_43.addItem(lst_itm)
        box_target_43.setCurrentIndex(0)
        box_target_43.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_43.addWidget(box_target_43)
        bg_box.addLayout(hbox_lay_target_43)

        hbox_lay_sigmas_44_0 =  QHBoxLayout()
        label_sigmas_44_0 = QLabel("                        sigmas[1]")
        label_sigmas_44_0.setPalette(palette_object)
        label_sigmas_44_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_44_0.addWidget(label_sigmas_44_0)
        box_sigmas_44_0 = QDoubleSpinBox()
        box_sigmas_44_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_44_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_44_1 =  QHBoxLayout()
        label_sigmas_44_1 = QLabel("                        sigmas[2]")
        label_sigmas_44_1.setPalette(palette_object)
        label_sigmas_44_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_44_1.addWidget(label_sigmas_44_1)
        box_sigmas_44_1 = QDoubleSpinBox()
        box_sigmas_44_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_44_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_44_2 =  QHBoxLayout()
        label_sigmas_44_2 = QLabel("                        sigmas[3]")
        label_sigmas_44_2.setPalette(palette_object)
        label_sigmas_44_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_44_2.addWidget(label_sigmas_44_2)
        box_sigmas_44_2 = QDoubleSpinBox()
        box_sigmas_44_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_44_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_44_3 =  QHBoxLayout()
        label_sigmas_44_3 = QLabel("                        sigmas[4]")
        label_sigmas_44_3.setPalette(palette_object)
        label_sigmas_44_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_44_3.addWidget(label_sigmas_44_3)
        box_sigmas_44_3 = QDoubleSpinBox()
        box_sigmas_44_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_44_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_44_4 =  QHBoxLayout()
        label_sigmas_44_4 = QLabel("                        sigmas[5]")
        label_sigmas_44_4.setPalette(palette_object)
        label_sigmas_44_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_44_4.addWidget(label_sigmas_44_4)
        box_sigmas_44_4 = QDoubleSpinBox()
        box_sigmas_44_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_44_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_44_5 =  QHBoxLayout()
        label_sigmas_44_5 = QLabel("                        sigmas[6]")
        label_sigmas_44_5.setPalette(palette_object)
        label_sigmas_44_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_44_5.addWidget(label_sigmas_44_5)
        box_sigmas_44_5 = QDoubleSpinBox()
        box_sigmas_44_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_44_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_44_0.addWidget(box_sigmas_44_0)
        bg_box.addLayout(hbox_lay_sigmas_44_0)
        hbox_lay_sigmas_44_1.addWidget(box_sigmas_44_1)
        bg_box.addLayout(hbox_lay_sigmas_44_1)
        hbox_lay_sigmas_44_2.addWidget(box_sigmas_44_2)
        bg_box.addLayout(hbox_lay_sigmas_44_2)
        hbox_lay_sigmas_44_3.addWidget(box_sigmas_44_3)
        bg_box.addLayout(hbox_lay_sigmas_44_3)
        hbox_lay_sigmas_44_4.addWidget(box_sigmas_44_4)
        bg_box.addLayout(hbox_lay_sigmas_44_4)
        hbox_lay_sigmas_44_5.addWidget(box_sigmas_44_5)
        bg_box.addLayout(hbox_lay_sigmas_44_5)


        hbox_lay_apply_to_all_46 =  QHBoxLayout()
        label_apply_to_all_46 = QLabel("                        apply_to_all")
        label_apply_to_all_46.setPalette(palette_object)
        label_apply_to_all_46.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_46.addWidget(label_apply_to_all_46)

        box_apply_to_all_46 = QComboBox()
        box_apply_to_all_46.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.apply_to_all"
        box_apply_to_all_46.tmp_lst=[]
        box_apply_to_all_46.tmp_lst.append("True")
        box_apply_to_all_46.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_46.tmp_lst:
            box_apply_to_all_46.addItem(lst_itm)
        box_apply_to_all_46.setCurrentIndex(1)
        box_apply_to_all_46.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_46.addWidget(box_apply_to_all_46)
        bg_box.addLayout(hbox_lay_apply_to_all_46)

        hbox_lay_force_static_47 =  QHBoxLayout()
        label_force_static_47 = QLabel("                force_static")
        label_force_static_47.setPalette(palette_object)
        label_force_static_47.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_47.addWidget(label_force_static_47)

        box_force_static_47 = QComboBox()
        box_force_static_47.local_path = "refinement.parameterisation.crystal.unit_cell.force_static"
        box_force_static_47.tmp_lst=[]
        box_force_static_47.tmp_lst.append("True")
        box_force_static_47.tmp_lst.append("False")
        for lst_itm in box_force_static_47.tmp_lst:
            box_force_static_47.addItem(lst_itm)
        box_force_static_47.setCurrentIndex(1)
        box_force_static_47.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_47.addWidget(box_force_static_47)
        bg_box.addLayout(hbox_lay_force_static_47)

        label_48 = QLabel("                smoother")
        label_48.setPalette(palette_scope)
        label_48.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_48)

        hbox_lay_num_intervals_49 =  QHBoxLayout()
        label_num_intervals_49 = QLabel("                    num_intervals")
        label_num_intervals_49.setPalette(palette_object)
        label_num_intervals_49.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_49.addWidget(label_num_intervals_49)

        box_num_intervals_49 = QComboBox()
        box_num_intervals_49.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.num_intervals"
        box_num_intervals_49.tmp_lst=[]
        box_num_intervals_49.tmp_lst.append("fixed_width")
        box_num_intervals_49.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_49.tmp_lst:
            box_num_intervals_49.addItem(lst_itm)
        box_num_intervals_49.setCurrentIndex(0)
        box_num_intervals_49.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_49.addWidget(box_num_intervals_49)
        bg_box.addLayout(hbox_lay_num_intervals_49)

        hbox_lay_interval_width_degrees_50 =  QHBoxLayout()
        label_interval_width_degrees_50 = QLabel("                    interval_width_degrees")
        label_interval_width_degrees_50.setPalette(palette_object)
        label_interval_width_degrees_50.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_50.addWidget(label_interval_width_degrees_50)

        box_interval_width_degrees_50 = QDoubleSpinBox()
        box_interval_width_degrees_50.setValue(36.0)
        box_interval_width_degrees_50.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.interval_width_degrees"
        box_interval_width_degrees_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_50.addWidget(box_interval_width_degrees_50)
        bg_box.addLayout(hbox_lay_interval_width_degrees_50)

        hbox_lay_absolute_num_intervals_51 =  QHBoxLayout()
        label_absolute_num_intervals_51 = QLabel("                    absolute_num_intervals")
        label_absolute_num_intervals_51.setPalette(palette_object)
        label_absolute_num_intervals_51.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_51.addWidget(label_absolute_num_intervals_51)

        box_absolute_num_intervals_51 = QSpinBox()
        box_absolute_num_intervals_51.setValue(5)
        box_absolute_num_intervals_51.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.absolute_num_intervals"
        box_absolute_num_intervals_51.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_51.addWidget(box_absolute_num_intervals_51)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_51)

        label_52 = QLabel("            orientation")
        label_52.setPalette(palette_scope)
        label_52.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_52)


        hbox_lay_force_static_54 =  QHBoxLayout()
        label_force_static_54 = QLabel("                force_static")
        label_force_static_54.setPalette(palette_object)
        label_force_static_54.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_54.addWidget(label_force_static_54)

        box_force_static_54 = QComboBox()
        box_force_static_54.local_path = "refinement.parameterisation.crystal.orientation.force_static"
        box_force_static_54.tmp_lst=[]
        box_force_static_54.tmp_lst.append("True")
        box_force_static_54.tmp_lst.append("False")
        for lst_itm in box_force_static_54.tmp_lst:
            box_force_static_54.addItem(lst_itm)
        box_force_static_54.setCurrentIndex(1)
        box_force_static_54.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_54.addWidget(box_force_static_54)
        bg_box.addLayout(hbox_lay_force_static_54)

        label_55 = QLabel("                smoother")
        label_55.setPalette(palette_scope)
        label_55.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_55)

        hbox_lay_num_intervals_56 =  QHBoxLayout()
        label_num_intervals_56 = QLabel("                    num_intervals")
        label_num_intervals_56.setPalette(palette_object)
        label_num_intervals_56.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_56.addWidget(label_num_intervals_56)

        box_num_intervals_56 = QComboBox()
        box_num_intervals_56.local_path = "refinement.parameterisation.crystal.orientation.smoother.num_intervals"
        box_num_intervals_56.tmp_lst=[]
        box_num_intervals_56.tmp_lst.append("fixed_width")
        box_num_intervals_56.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_56.tmp_lst:
            box_num_intervals_56.addItem(lst_itm)
        box_num_intervals_56.setCurrentIndex(0)
        box_num_intervals_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_56.addWidget(box_num_intervals_56)
        bg_box.addLayout(hbox_lay_num_intervals_56)

        hbox_lay_interval_width_degrees_57 =  QHBoxLayout()
        label_interval_width_degrees_57 = QLabel("                    interval_width_degrees")
        label_interval_width_degrees_57.setPalette(palette_object)
        label_interval_width_degrees_57.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_57.addWidget(label_interval_width_degrees_57)

        box_interval_width_degrees_57 = QDoubleSpinBox()
        box_interval_width_degrees_57.setValue(36.0)
        box_interval_width_degrees_57.local_path = "refinement.parameterisation.crystal.orientation.smoother.interval_width_degrees"
        box_interval_width_degrees_57.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_57.addWidget(box_interval_width_degrees_57)
        bg_box.addLayout(hbox_lay_interval_width_degrees_57)

        hbox_lay_absolute_num_intervals_58 =  QHBoxLayout()
        label_absolute_num_intervals_58 = QLabel("                    absolute_num_intervals")
        label_absolute_num_intervals_58.setPalette(palette_object)
        label_absolute_num_intervals_58.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_58.addWidget(label_absolute_num_intervals_58)

        box_absolute_num_intervals_58 = QSpinBox()
        box_absolute_num_intervals_58.setValue(5)
        box_absolute_num_intervals_58.local_path = "refinement.parameterisation.crystal.orientation.smoother.absolute_num_intervals"
        box_absolute_num_intervals_58.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_58.addWidget(box_absolute_num_intervals_58)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_58)

        label_59 = QLabel("        detector")
        label_59.setPalette(palette_scope)
        label_59.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_59)

        hbox_lay_panels_60 =  QHBoxLayout()
        label_panels_60 = QLabel("            panels")
        label_panels_60.setPalette(palette_object)
        label_panels_60.setFont(QFont("Monospace", 10))
        hbox_lay_panels_60.addWidget(label_panels_60)

        box_panels_60 = QComboBox()
        box_panels_60.local_path = "refinement.parameterisation.detector.panels"
        box_panels_60.tmp_lst=[]
        box_panels_60.tmp_lst.append("automatic")
        box_panels_60.tmp_lst.append("single")
        box_panels_60.tmp_lst.append("multiple")
        box_panels_60.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_60.tmp_lst:
            box_panels_60.addItem(lst_itm)
        box_panels_60.setCurrentIndex(0)
        box_panels_60.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_60.addWidget(box_panels_60)
        bg_box.addLayout(hbox_lay_panels_60)

        hbox_lay_hierarchy_level_61 =  QHBoxLayout()
        label_hierarchy_level_61 = QLabel("            hierarchy_level")
        label_hierarchy_level_61.setPalette(palette_object)
        label_hierarchy_level_61.setFont(QFont("Monospace", 10))
        hbox_lay_hierarchy_level_61.addWidget(label_hierarchy_level_61)

        box_hierarchy_level_61 = QSpinBox()
        box_hierarchy_level_61.setValue(0)
        box_hierarchy_level_61.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_61.addWidget(box_hierarchy_level_61)
        bg_box.addLayout(hbox_lay_hierarchy_level_61)

        hbox_lay_fix_62 =  QHBoxLayout()
        label_fix_62 = QLabel("            fix")
        label_fix_62.setPalette(palette_object)
        label_fix_62.setFont(QFont("Monospace", 10))
        hbox_lay_fix_62.addWidget(label_fix_62)

        box_fix_62 = QComboBox()
        box_fix_62.local_path = "refinement.parameterisation.detector.fix"
        box_fix_62.tmp_lst=[]
        box_fix_62.tmp_lst.append("all")
        box_fix_62.tmp_lst.append("position")
        box_fix_62.tmp_lst.append("orientation")
        for lst_itm in box_fix_62.tmp_lst:
            box_fix_62.addItem(lst_itm)
        box_fix_62.setCurrentIndex(0)
        box_fix_62.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_62.addWidget(box_fix_62)
        bg_box.addLayout(hbox_lay_fix_62)


        hbox_lay_sparse_64 =  QHBoxLayout()
        label_sparse_64 = QLabel("        sparse")
        label_sparse_64.setPalette(palette_object)
        label_sparse_64.setFont(QFont("Monospace", 10))
        hbox_lay_sparse_64.addWidget(label_sparse_64)

        box_sparse_64 = QComboBox()
        box_sparse_64.local_path = "refinement.parameterisation.sparse"
        box_sparse_64.tmp_lst=[]
        box_sparse_64.tmp_lst.append("True")
        box_sparse_64.tmp_lst.append("False")
        for lst_itm in box_sparse_64.tmp_lst:
            box_sparse_64.addItem(lst_itm)
        box_sparse_64.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_64.addWidget(box_sparse_64)
        bg_box.addLayout(hbox_lay_sparse_64)

        hbox_lay_treat_single_image_as_still_65 =  QHBoxLayout()
        label_treat_single_image_as_still_65 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_65.setPalette(palette_object)
        label_treat_single_image_as_still_65.setFont(QFont("Monospace", 10))
        hbox_lay_treat_single_image_as_still_65.addWidget(label_treat_single_image_as_still_65)

        box_treat_single_image_as_still_65 = QComboBox()
        box_treat_single_image_as_still_65.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_65.tmp_lst=[]
        box_treat_single_image_as_still_65.tmp_lst.append("True")
        box_treat_single_image_as_still_65.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_65.tmp_lst:
            box_treat_single_image_as_still_65.addItem(lst_itm)
        box_treat_single_image_as_still_65.setCurrentIndex(1)
        box_treat_single_image_as_still_65.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_65.addWidget(box_treat_single_image_as_still_65)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_65)

        hbox_lay_spherical_relp_model_66 =  QHBoxLayout()
        label_spherical_relp_model_66 = QLabel("        spherical_relp_model")
        label_spherical_relp_model_66.setPalette(palette_object)
        label_spherical_relp_model_66.setFont(QFont("Monospace", 10))
        hbox_lay_spherical_relp_model_66.addWidget(label_spherical_relp_model_66)

        box_spherical_relp_model_66 = QComboBox()
        box_spherical_relp_model_66.local_path = "refinement.parameterisation.spherical_relp_model"
        box_spherical_relp_model_66.tmp_lst=[]
        box_spherical_relp_model_66.tmp_lst.append("True")
        box_spherical_relp_model_66.tmp_lst.append("False")
        for lst_itm in box_spherical_relp_model_66.tmp_lst:
            box_spherical_relp_model_66.addItem(lst_itm)
        box_spherical_relp_model_66.setCurrentIndex(1)
        box_spherical_relp_model_66.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_spherical_relp_model_66.addWidget(box_spherical_relp_model_66)
        bg_box.addLayout(hbox_lay_spherical_relp_model_66)

        label_67 = QLabel("    refinery")
        label_67.setPalette(palette_scope)
        label_67.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_67)

        hbox_lay_engine_68 =  QHBoxLayout()
        label_engine_68 = QLabel("        engine")
        label_engine_68.setPalette(palette_object)
        label_engine_68.setFont(QFont("Monospace", 10))
        hbox_lay_engine_68.addWidget(label_engine_68)

        box_engine_68 = QComboBox()
        box_engine_68.local_path = "refinement.refinery.engine"
        box_engine_68.tmp_lst=[]
        box_engine_68.tmp_lst.append("SimpleLBFGS")
        box_engine_68.tmp_lst.append("LBFGScurvs")
        box_engine_68.tmp_lst.append("GaussNewton")
        box_engine_68.tmp_lst.append("LevMar")
        box_engine_68.tmp_lst.append("SparseLevMar")
        for lst_itm in box_engine_68.tmp_lst:
            box_engine_68.addItem(lst_itm)
        box_engine_68.setCurrentIndex(3)
        box_engine_68.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_68.addWidget(box_engine_68)
        bg_box.addLayout(hbox_lay_engine_68)

        hbox_lay_track_step_69 =  QHBoxLayout()
        label_track_step_69 = QLabel("        track_step")
        label_track_step_69.setPalette(palette_object)
        label_track_step_69.setFont(QFont("Monospace", 10))
        hbox_lay_track_step_69.addWidget(label_track_step_69)

        box_track_step_69 = QComboBox()
        box_track_step_69.local_path = "refinement.refinery.track_step"
        box_track_step_69.tmp_lst=[]
        box_track_step_69.tmp_lst.append("True")
        box_track_step_69.tmp_lst.append("False")
        for lst_itm in box_track_step_69.tmp_lst:
            box_track_step_69.addItem(lst_itm)
        box_track_step_69.setCurrentIndex(1)
        box_track_step_69.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_69.addWidget(box_track_step_69)
        bg_box.addLayout(hbox_lay_track_step_69)

        hbox_lay_track_gradient_70 =  QHBoxLayout()
        label_track_gradient_70 = QLabel("        track_gradient")
        label_track_gradient_70.setPalette(palette_object)
        label_track_gradient_70.setFont(QFont("Monospace", 10))
        hbox_lay_track_gradient_70.addWidget(label_track_gradient_70)

        box_track_gradient_70 = QComboBox()
        box_track_gradient_70.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_70.tmp_lst=[]
        box_track_gradient_70.tmp_lst.append("True")
        box_track_gradient_70.tmp_lst.append("False")
        for lst_itm in box_track_gradient_70.tmp_lst:
            box_track_gradient_70.addItem(lst_itm)
        box_track_gradient_70.setCurrentIndex(1)
        box_track_gradient_70.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_70.addWidget(box_track_gradient_70)
        bg_box.addLayout(hbox_lay_track_gradient_70)

        hbox_lay_track_parameter_correlation_71 =  QHBoxLayout()
        label_track_parameter_correlation_71 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_71.setPalette(palette_object)
        label_track_parameter_correlation_71.setFont(QFont("Monospace", 10))
        hbox_lay_track_parameter_correlation_71.addWidget(label_track_parameter_correlation_71)

        box_track_parameter_correlation_71 = QComboBox()
        box_track_parameter_correlation_71.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_71.tmp_lst=[]
        box_track_parameter_correlation_71.tmp_lst.append("True")
        box_track_parameter_correlation_71.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_71.tmp_lst:
            box_track_parameter_correlation_71.addItem(lst_itm)
        box_track_parameter_correlation_71.setCurrentIndex(1)
        box_track_parameter_correlation_71.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_71.addWidget(box_track_parameter_correlation_71)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_71)

        hbox_lay_track_out_of_sample_rmsd_72 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_72 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_72.setPalette(palette_object)
        label_track_out_of_sample_rmsd_72.setFont(QFont("Monospace", 10))
        hbox_lay_track_out_of_sample_rmsd_72.addWidget(label_track_out_of_sample_rmsd_72)

        box_track_out_of_sample_rmsd_72 = QComboBox()
        box_track_out_of_sample_rmsd_72.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_72.tmp_lst=[]
        box_track_out_of_sample_rmsd_72.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_72.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_72.tmp_lst:
            box_track_out_of_sample_rmsd_72.addItem(lst_itm)
        box_track_out_of_sample_rmsd_72.setCurrentIndex(1)
        box_track_out_of_sample_rmsd_72.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_72.addWidget(box_track_out_of_sample_rmsd_72)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_72)


        hbox_lay_max_iterations_74 =  QHBoxLayout()
        label_max_iterations_74 = QLabel("        max_iterations")
        label_max_iterations_74.setPalette(palette_object)
        label_max_iterations_74.setFont(QFont("Monospace", 10))
        hbox_lay_max_iterations_74.addWidget(label_max_iterations_74)

        box_max_iterations_74 = QSpinBox()
        box_max_iterations_74.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_74.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_74.addWidget(box_max_iterations_74)
        bg_box.addLayout(hbox_lay_max_iterations_74)

        label_75 = QLabel("    target")
        label_75.setPalette(palette_scope)
        label_75.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_75)

        hbox_lay_rmsd_cutoff_76 =  QHBoxLayout()
        label_rmsd_cutoff_76 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_76.setPalette(palette_object)
        label_rmsd_cutoff_76.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_76.addWidget(label_rmsd_cutoff_76)

        box_rmsd_cutoff_76 = QComboBox()
        box_rmsd_cutoff_76.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_76.tmp_lst=[]
        box_rmsd_cutoff_76.tmp_lst.append("fraction_of_bin_size")
        box_rmsd_cutoff_76.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_76.tmp_lst:
            box_rmsd_cutoff_76.addItem(lst_itm)
        box_rmsd_cutoff_76.setCurrentIndex(0)
        box_rmsd_cutoff_76.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_76.addWidget(box_rmsd_cutoff_76)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_76)

        hbox_lay_bin_size_fraction_77 =  QHBoxLayout()
        label_bin_size_fraction_77 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_77.setPalette(palette_object)
        label_bin_size_fraction_77.setFont(QFont("Monospace", 10))
        hbox_lay_bin_size_fraction_77.addWidget(label_bin_size_fraction_77)

        box_bin_size_fraction_77 = QDoubleSpinBox()
        box_bin_size_fraction_77.setValue(0.2)
        box_bin_size_fraction_77.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_77.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_77.addWidget(box_bin_size_fraction_77)
        bg_box.addLayout(hbox_lay_bin_size_fraction_77)

        hbox_lay_absolute_cutoffs_78_0 =  QHBoxLayout()
        label_absolute_cutoffs_78_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_78_0.setPalette(palette_object)
        label_absolute_cutoffs_78_0.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_78_0.addWidget(label_absolute_cutoffs_78_0)
        box_absolute_cutoffs_78_0 = QDoubleSpinBox()
        box_absolute_cutoffs_78_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_78_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_78_1 =  QHBoxLayout()
        label_absolute_cutoffs_78_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_78_1.setPalette(palette_object)
        label_absolute_cutoffs_78_1.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_78_1.addWidget(label_absolute_cutoffs_78_1)
        box_absolute_cutoffs_78_1 = QDoubleSpinBox()
        box_absolute_cutoffs_78_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_78_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_78_2 =  QHBoxLayout()
        label_absolute_cutoffs_78_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_78_2.setPalette(palette_object)
        label_absolute_cutoffs_78_2.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_78_2.addWidget(label_absolute_cutoffs_78_2)
        box_absolute_cutoffs_78_2 = QDoubleSpinBox()
        box_absolute_cutoffs_78_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_78_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_78_0.addWidget(box_absolute_cutoffs_78_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_78_0)
        hbox_lay_absolute_cutoffs_78_1.addWidget(box_absolute_cutoffs_78_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_78_1)
        hbox_lay_absolute_cutoffs_78_2.addWidget(box_absolute_cutoffs_78_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_78_2)

        hbox_lay_gradient_calculation_blocksize_79 =  QHBoxLayout()
        label_gradient_calculation_blocksize_79 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_79.setPalette(palette_object)
        label_gradient_calculation_blocksize_79.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_calculation_blocksize_79.addWidget(label_gradient_calculation_blocksize_79)

        box_gradient_calculation_blocksize_79 = QSpinBox()
        box_gradient_calculation_blocksize_79.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_79.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_79.addWidget(box_gradient_calculation_blocksize_79)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_79)

        label_80 = QLabel("    reflections")
        label_80.setPalette(palette_scope)
        label_80.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_80)

        hbox_lay_reflections_per_degree_81 =  QHBoxLayout()
        label_reflections_per_degree_81 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_81.setPalette(palette_object)
        label_reflections_per_degree_81.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_81.addWidget(label_reflections_per_degree_81)

        box_reflections_per_degree_81 = QDoubleSpinBox()
        box_reflections_per_degree_81.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_81.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_81.addWidget(box_reflections_per_degree_81)
        bg_box.addLayout(hbox_lay_reflections_per_degree_81)

        hbox_lay_minimum_sample_size_82 =  QHBoxLayout()
        label_minimum_sample_size_82 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_82.setPalette(palette_object)
        label_minimum_sample_size_82.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_82.addWidget(label_minimum_sample_size_82)

        box_minimum_sample_size_82 = QSpinBox()
        box_minimum_sample_size_82.setValue(1000)
        box_minimum_sample_size_82.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_82.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_82.addWidget(box_minimum_sample_size_82)
        bg_box.addLayout(hbox_lay_minimum_sample_size_82)

        hbox_lay_maximum_sample_size_83 =  QHBoxLayout()
        label_maximum_sample_size_83 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_83.setPalette(palette_object)
        label_maximum_sample_size_83.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_83.addWidget(label_maximum_sample_size_83)

        box_maximum_sample_size_83 = QSpinBox()
        box_maximum_sample_size_83.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_83.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_83.addWidget(box_maximum_sample_size_83)
        bg_box.addLayout(hbox_lay_maximum_sample_size_83)

        hbox_lay_random_seed_84 =  QHBoxLayout()
        label_random_seed_84 = QLabel("        random_seed")
        label_random_seed_84.setPalette(palette_object)
        label_random_seed_84.setFont(QFont("Monospace", 10))
        hbox_lay_random_seed_84.addWidget(label_random_seed_84)

        box_random_seed_84 = QSpinBox()
        box_random_seed_84.setValue(42)
        box_random_seed_84.local_path = "refinement.reflections.random_seed"
        box_random_seed_84.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_84.addWidget(box_random_seed_84)
        bg_box.addLayout(hbox_lay_random_seed_84)

        hbox_lay_close_to_spindle_cutoff_85 =  QHBoxLayout()
        label_close_to_spindle_cutoff_85 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_85.setPalette(palette_object)
        label_close_to_spindle_cutoff_85.setFont(QFont("Monospace", 10))
        hbox_lay_close_to_spindle_cutoff_85.addWidget(label_close_to_spindle_cutoff_85)

        box_close_to_spindle_cutoff_85 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_85.setValue(0.02)
        box_close_to_spindle_cutoff_85.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_85.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_85.addWidget(box_close_to_spindle_cutoff_85)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_85)

        hbox_lay_block_width_86 =  QHBoxLayout()
        label_block_width_86 = QLabel("        block_width")
        label_block_width_86.setPalette(palette_object)
        label_block_width_86.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_86.addWidget(label_block_width_86)

        box_block_width_86 = QDoubleSpinBox()
        box_block_width_86.setValue(1.0)
        box_block_width_86.local_path = "refinement.reflections.block_width"
        box_block_width_86.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_86.addWidget(box_block_width_86)
        bg_box.addLayout(hbox_lay_block_width_86)

        label_87 = QLabel("        weighting_strategy")
        label_87.setPalette(palette_scope)
        label_87.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_87)

        hbox_lay_override_88 =  QHBoxLayout()
        label_override_88 = QLabel("            override")
        label_override_88.setPalette(palette_object)
        label_override_88.setFont(QFont("Monospace", 10))
        hbox_lay_override_88.addWidget(label_override_88)

        box_override_88 = QComboBox()
        box_override_88.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_88.tmp_lst=[]
        box_override_88.tmp_lst.append("statistical")
        box_override_88.tmp_lst.append("stills")
        box_override_88.tmp_lst.append("constant")
        for lst_itm in box_override_88.tmp_lst:
            box_override_88.addItem(lst_itm)
        box_override_88.setCurrentIndex(0)
        box_override_88.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_88.addWidget(box_override_88)
        bg_box.addLayout(hbox_lay_override_88)

        hbox_lay_delpsi_constant_89 =  QHBoxLayout()
        label_delpsi_constant_89 = QLabel("            delpsi_constant")
        label_delpsi_constant_89.setPalette(palette_object)
        label_delpsi_constant_89.setFont(QFont("Monospace", 10))
        hbox_lay_delpsi_constant_89.addWidget(label_delpsi_constant_89)

        box_delpsi_constant_89 = QDoubleSpinBox()
        box_delpsi_constant_89.setValue(1000000.0)
        box_delpsi_constant_89.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_89.addWidget(box_delpsi_constant_89)
        bg_box.addLayout(hbox_lay_delpsi_constant_89)

        hbox_lay_constants_90_0 =  QHBoxLayout()
        label_constants_90_0 = QLabel("            constants[1]")
        label_constants_90_0.setPalette(palette_object)
        label_constants_90_0.setFont(QFont("Monospace", 10))
        hbox_lay_constants_90_0.addWidget(label_constants_90_0)
        box_constants_90_0 = QDoubleSpinBox()
        box_constants_90_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_90_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_90_1 =  QHBoxLayout()
        label_constants_90_1 = QLabel("            constants[2]")
        label_constants_90_1.setPalette(palette_object)
        label_constants_90_1.setFont(QFont("Monospace", 10))
        hbox_lay_constants_90_1.addWidget(label_constants_90_1)
        box_constants_90_1 = QDoubleSpinBox()
        box_constants_90_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_90_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_90_2 =  QHBoxLayout()
        label_constants_90_2 = QLabel("            constants[3]")
        label_constants_90_2.setPalette(palette_object)
        label_constants_90_2.setFont(QFont("Monospace", 10))
        hbox_lay_constants_90_2.addWidget(label_constants_90_2)
        box_constants_90_2 = QDoubleSpinBox()
        box_constants_90_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_90_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_90_0.addWidget(box_constants_90_0)
        bg_box.addLayout(hbox_lay_constants_90_0)
        hbox_lay_constants_90_1.addWidget(box_constants_90_1)
        bg_box.addLayout(hbox_lay_constants_90_1)
        hbox_lay_constants_90_2.addWidget(box_constants_90_2)
        bg_box.addLayout(hbox_lay_constants_90_2)

        label_91 = QLabel("        outlier")
        label_91.setPalette(palette_scope)
        label_91.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_91)

        hbox_lay_algorithm_92 =  QHBoxLayout()
        label_algorithm_92 = QLabel("            algorithm")
        label_algorithm_92.setPalette(palette_object)
        label_algorithm_92.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_92.addWidget(label_algorithm_92)

        box_algorithm_92 = QComboBox()
        box_algorithm_92.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_92.tmp_lst=[]
        box_algorithm_92.tmp_lst.append("null")
        box_algorithm_92.tmp_lst.append("auto")
        box_algorithm_92.tmp_lst.append("mcd")
        box_algorithm_92.tmp_lst.append("tukey")
        box_algorithm_92.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_92.tmp_lst:
            box_algorithm_92.addItem(lst_itm)
        box_algorithm_92.setCurrentIndex(1)
        box_algorithm_92.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_92.addWidget(box_algorithm_92)
        bg_box.addLayout(hbox_lay_algorithm_92)

        hbox_lay_minimum_number_of_reflections_93 =  QHBoxLayout()
        label_minimum_number_of_reflections_93 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_93.setPalette(palette_object)
        label_minimum_number_of_reflections_93.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_number_of_reflections_93.addWidget(label_minimum_number_of_reflections_93)

        box_minimum_number_of_reflections_93 = QSpinBox()
        box_minimum_number_of_reflections_93.setValue(20)
        box_minimum_number_of_reflections_93.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_93.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_93.addWidget(box_minimum_number_of_reflections_93)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_93)

        hbox_lay_separate_experiments_94 =  QHBoxLayout()
        label_separate_experiments_94 = QLabel("            separate_experiments")
        label_separate_experiments_94.setPalette(palette_object)
        label_separate_experiments_94.setFont(QFont("Monospace", 10))
        hbox_lay_separate_experiments_94.addWidget(label_separate_experiments_94)

        box_separate_experiments_94 = QComboBox()
        box_separate_experiments_94.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_94.tmp_lst=[]
        box_separate_experiments_94.tmp_lst.append("True")
        box_separate_experiments_94.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_94.tmp_lst:
            box_separate_experiments_94.addItem(lst_itm)
        box_separate_experiments_94.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_94.addWidget(box_separate_experiments_94)
        bg_box.addLayout(hbox_lay_separate_experiments_94)

        hbox_lay_separate_panels_95 =  QHBoxLayout()
        label_separate_panels_95 = QLabel("            separate_panels")
        label_separate_panels_95.setPalette(palette_object)
        label_separate_panels_95.setFont(QFont("Monospace", 10))
        hbox_lay_separate_panels_95.addWidget(label_separate_panels_95)

        box_separate_panels_95 = QComboBox()
        box_separate_panels_95.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_95.tmp_lst=[]
        box_separate_panels_95.tmp_lst.append("True")
        box_separate_panels_95.tmp_lst.append("False")
        for lst_itm in box_separate_panels_95.tmp_lst:
            box_separate_panels_95.addItem(lst_itm)
        box_separate_panels_95.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_95.addWidget(box_separate_panels_95)
        bg_box.addLayout(hbox_lay_separate_panels_95)

        hbox_lay_separate_blocks_96 =  QHBoxLayout()
        label_separate_blocks_96 = QLabel("            separate_blocks")
        label_separate_blocks_96.setPalette(palette_object)
        label_separate_blocks_96.setFont(QFont("Monospace", 10))
        hbox_lay_separate_blocks_96.addWidget(label_separate_blocks_96)

        box_separate_blocks_96 = QComboBox()
        box_separate_blocks_96.local_path = "refinement.reflections.outlier.separate_blocks"
        box_separate_blocks_96.tmp_lst=[]
        box_separate_blocks_96.tmp_lst.append("True")
        box_separate_blocks_96.tmp_lst.append("False")
        for lst_itm in box_separate_blocks_96.tmp_lst:
            box_separate_blocks_96.addItem(lst_itm)
        box_separate_blocks_96.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_blocks_96.addWidget(box_separate_blocks_96)
        bg_box.addLayout(hbox_lay_separate_blocks_96)

        hbox_lay_block_width_97 =  QHBoxLayout()
        label_block_width_97 = QLabel("            block_width")
        label_block_width_97.setPalette(palette_object)
        label_block_width_97.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_97.addWidget(label_block_width_97)

        box_block_width_97 = QDoubleSpinBox()
        box_block_width_97.setValue(18.0)
        box_block_width_97.local_path = "refinement.reflections.outlier.block_width"
        box_block_width_97.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_97.addWidget(box_block_width_97)
        bg_box.addLayout(hbox_lay_block_width_97)

        label_98 = QLabel("            tukey")
        label_98.setPalette(palette_scope)
        label_98.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_98)

        hbox_lay_iqr_multiplier_99 =  QHBoxLayout()
        label_iqr_multiplier_99 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_99.setPalette(palette_object)
        label_iqr_multiplier_99.setFont(QFont("Monospace", 10))
        hbox_lay_iqr_multiplier_99.addWidget(label_iqr_multiplier_99)

        box_iqr_multiplier_99 = QDoubleSpinBox()
        box_iqr_multiplier_99.setValue(1.5)
        box_iqr_multiplier_99.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_99.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_99.addWidget(box_iqr_multiplier_99)
        bg_box.addLayout(hbox_lay_iqr_multiplier_99)

        label_100 = QLabel("            mcd")
        label_100.setPalette(palette_scope)
        label_100.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_100)

        hbox_lay_alpha_101 =  QHBoxLayout()
        label_alpha_101 = QLabel("                alpha")
        label_alpha_101.setPalette(palette_object)
        label_alpha_101.setFont(QFont("Monospace", 10))
        hbox_lay_alpha_101.addWidget(label_alpha_101)

        box_alpha_101 = QDoubleSpinBox()
        box_alpha_101.setValue(0.5)
        box_alpha_101.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_101.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_101.addWidget(box_alpha_101)
        bg_box.addLayout(hbox_lay_alpha_101)

        hbox_lay_max_n_groups_102 =  QHBoxLayout()
        label_max_n_groups_102 = QLabel("                max_n_groups")
        label_max_n_groups_102.setPalette(palette_object)
        label_max_n_groups_102.setFont(QFont("Monospace", 10))
        hbox_lay_max_n_groups_102.addWidget(label_max_n_groups_102)

        box_max_n_groups_102 = QSpinBox()
        box_max_n_groups_102.setValue(5)
        box_max_n_groups_102.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_102.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_102.addWidget(box_max_n_groups_102)
        bg_box.addLayout(hbox_lay_max_n_groups_102)

        hbox_lay_min_group_size_103 =  QHBoxLayout()
        label_min_group_size_103 = QLabel("                min_group_size")
        label_min_group_size_103.setPalette(palette_object)
        label_min_group_size_103.setFont(QFont("Monospace", 10))
        hbox_lay_min_group_size_103.addWidget(label_min_group_size_103)

        box_min_group_size_103 = QSpinBox()
        box_min_group_size_103.setValue(300)
        box_min_group_size_103.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_103.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_103.addWidget(box_min_group_size_103)
        bg_box.addLayout(hbox_lay_min_group_size_103)

        hbox_lay_n_trials_104 =  QHBoxLayout()
        label_n_trials_104 = QLabel("                n_trials")
        label_n_trials_104.setPalette(palette_object)
        label_n_trials_104.setFont(QFont("Monospace", 10))
        hbox_lay_n_trials_104.addWidget(label_n_trials_104)

        box_n_trials_104 = QSpinBox()
        box_n_trials_104.setValue(500)
        box_n_trials_104.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_104.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_104.addWidget(box_n_trials_104)
        bg_box.addLayout(hbox_lay_n_trials_104)

        hbox_lay_k1_105 =  QHBoxLayout()
        label_k1_105 = QLabel("                k1")
        label_k1_105.setPalette(palette_object)
        label_k1_105.setFont(QFont("Monospace", 10))
        hbox_lay_k1_105.addWidget(label_k1_105)

        box_k1_105 = QSpinBox()
        box_k1_105.setValue(2)
        box_k1_105.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_105.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_105.addWidget(box_k1_105)
        bg_box.addLayout(hbox_lay_k1_105)

        hbox_lay_k2_106 =  QHBoxLayout()
        label_k2_106 = QLabel("                k2")
        label_k2_106.setPalette(palette_object)
        label_k2_106.setFont(QFont("Monospace", 10))
        hbox_lay_k2_106.addWidget(label_k2_106)

        box_k2_106 = QSpinBox()
        box_k2_106.setValue(2)
        box_k2_106.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_106.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_106.addWidget(box_k2_106)
        bg_box.addLayout(hbox_lay_k2_106)

        hbox_lay_k3_107 =  QHBoxLayout()
        label_k3_107 = QLabel("                k3")
        label_k3_107.setPalette(palette_object)
        label_k3_107.setFont(QFont("Monospace", 10))
        hbox_lay_k3_107.addWidget(label_k3_107)

        box_k3_107 = QSpinBox()
        box_k3_107.setValue(100)
        box_k3_107.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_107.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_107.addWidget(box_k3_107)
        bg_box.addLayout(hbox_lay_k3_107)

        hbox_lay_threshold_probability_108 =  QHBoxLayout()
        label_threshold_probability_108 = QLabel("                threshold_probability")
        label_threshold_probability_108.setPalette(palette_object)
        label_threshold_probability_108.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_probability_108.addWidget(label_threshold_probability_108)

        box_threshold_probability_108 = QDoubleSpinBox()
        box_threshold_probability_108.setValue(0.975)
        box_threshold_probability_108.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_108.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_108.addWidget(box_threshold_probability_108)
        bg_box.addLayout(hbox_lay_threshold_probability_108)

        label_109 = QLabel("            sauter_poon")
        label_109.setPalette(palette_scope)
        label_109.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_109)

        hbox_lay_px_sz_110_0 =  QHBoxLayout()
        label_px_sz_110_0 = QLabel("                px_sz[1]")
        label_px_sz_110_0.setPalette(palette_object)
        label_px_sz_110_0.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_110_0.addWidget(label_px_sz_110_0)
        box_px_sz_110_0 = QDoubleSpinBox()
        box_px_sz_110_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_110_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_110_1 =  QHBoxLayout()
        label_px_sz_110_1 = QLabel("                px_sz[2]")
        label_px_sz_110_1.setPalette(palette_object)
        label_px_sz_110_1.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_110_1.addWidget(label_px_sz_110_1)
        box_px_sz_110_1 = QDoubleSpinBox()
        box_px_sz_110_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_110_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_110_0.addWidget(box_px_sz_110_0)
        bg_box.addLayout(hbox_lay_px_sz_110_0)
        hbox_lay_px_sz_110_1.addWidget(box_px_sz_110_1)
        bg_box.addLayout(hbox_lay_px_sz_110_1)

        hbox_lay_verbose_111 =  QHBoxLayout()
        label_verbose_111 = QLabel("                verbose")
        label_verbose_111.setPalette(palette_object)
        label_verbose_111.setFont(QFont("Monospace", 10))
        hbox_lay_verbose_111.addWidget(label_verbose_111)

        box_verbose_111 = QComboBox()
        box_verbose_111.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_111.tmp_lst=[]
        box_verbose_111.tmp_lst.append("True")
        box_verbose_111.tmp_lst.append("False")
        for lst_itm in box_verbose_111.tmp_lst:
            box_verbose_111.addItem(lst_itm)
        box_verbose_111.setCurrentIndex(1)
        box_verbose_111.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_111.addWidget(box_verbose_111)
        bg_box.addLayout(hbox_lay_verbose_111)

        hbox_lay_pdf_112 =  QHBoxLayout()
        label_pdf_112 = QLabel("                pdf")
        label_pdf_112.setPalette(palette_object)
        label_pdf_112.setFont(QFont("Monospace", 10))
        hbox_lay_pdf_112.addWidget(label_pdf_112)

        box_pdf_112 = QLineEdit()
        box_pdf_112.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_112.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_112.addWidget(box_pdf_112)
        bg_box.addLayout(hbox_lay_pdf_112)

 
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
