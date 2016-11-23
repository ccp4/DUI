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

        hbox_lay_detector_reduce_22 =  QHBoxLayout()
        label_detector_reduce_22 = QLabel("            detector_reduce")
        label_detector_reduce_22.setPalette(palette_object)
        label_detector_reduce_22.setFont(QFont("Monospace", 10))
        hbox_lay_detector_reduce_22.addWidget(label_detector_reduce_22)

        box_detector_reduce_22 = QComboBox()
        box_detector_reduce_22.local_path = "refinement.parameterisation.auto_reduction.detector_reduce"
        box_detector_reduce_22.tmp_lst=[]
        box_detector_reduce_22.tmp_lst.append("True")
        box_detector_reduce_22.tmp_lst.append("False")
        for lst_itm in box_detector_reduce_22.tmp_lst:
            box_detector_reduce_22.addItem(lst_itm)
        box_detector_reduce_22.setCurrentIndex(1)
        box_detector_reduce_22.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_detector_reduce_22.addWidget(box_detector_reduce_22)
        bg_box.addLayout(hbox_lay_detector_reduce_22)


        hbox_lay_scan_varying_24 =  QHBoxLayout()
        label_scan_varying_24 = QLabel("        scan_varying")
        label_scan_varying_24.setPalette(palette_object)
        label_scan_varying_24.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_24.addWidget(label_scan_varying_24)

        box_scan_varying_24 = QComboBox()
        box_scan_varying_24.local_path = "refinement.parameterisation.scan_varying"
        box_scan_varying_24.tmp_lst=[]
        box_scan_varying_24.tmp_lst.append("True")
        box_scan_varying_24.tmp_lst.append("False")
        for lst_itm in box_scan_varying_24.tmp_lst:
            box_scan_varying_24.addItem(lst_itm)
        box_scan_varying_24.setCurrentIndex(1)
        box_scan_varying_24.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_24.addWidget(box_scan_varying_24)
        bg_box.addLayout(hbox_lay_scan_varying_24)

        hbox_lay_compose_model_per_25 =  QHBoxLayout()
        label_compose_model_per_25 = QLabel("        compose_model_per")
        label_compose_model_per_25.setPalette(palette_object)
        label_compose_model_per_25.setFont(QFont("Monospace", 10))
        hbox_lay_compose_model_per_25.addWidget(label_compose_model_per_25)

        box_compose_model_per_25 = QComboBox()
        box_compose_model_per_25.local_path = "refinement.parameterisation.compose_model_per"
        box_compose_model_per_25.tmp_lst=[]
        box_compose_model_per_25.tmp_lst.append("reflection")
        box_compose_model_per_25.tmp_lst.append("image")
        box_compose_model_per_25.tmp_lst.append("block")
        for lst_itm in box_compose_model_per_25.tmp_lst:
            box_compose_model_per_25.addItem(lst_itm)
        box_compose_model_per_25.setCurrentIndex(2)
        box_compose_model_per_25.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_compose_model_per_25.addWidget(box_compose_model_per_25)
        bg_box.addLayout(hbox_lay_compose_model_per_25)

        label_26 = QLabel("        beam")
        label_26.setPalette(palette_scope)
        label_26.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_26)

        hbox_lay_fix_27 =  QHBoxLayout()
        label_fix_27 = QLabel("            fix")
        label_fix_27.setPalette(palette_object)
        label_fix_27.setFont(QFont("Monospace", 10))
        hbox_lay_fix_27.addWidget(label_fix_27)

        box_fix_27 = QComboBox()
        box_fix_27.local_path = "refinement.parameterisation.beam.fix"
        box_fix_27.tmp_lst=[]
        box_fix_27.tmp_lst.append("all")
        box_fix_27.tmp_lst.append("in_spindle_plane")
        box_fix_27.tmp_lst.append("out_spindle_plane")
        box_fix_27.tmp_lst.append("wavelength")
        for lst_itm in box_fix_27.tmp_lst:
            box_fix_27.addItem(lst_itm)
        box_fix_27.setCurrentIndex(3)
        box_fix_27.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_27.addWidget(box_fix_27)
        bg_box.addLayout(hbox_lay_fix_27)


        hbox_lay_force_static_29 =  QHBoxLayout()
        label_force_static_29 = QLabel("            force_static")
        label_force_static_29.setPalette(palette_object)
        label_force_static_29.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_29.addWidget(label_force_static_29)

        box_force_static_29 = QComboBox()
        box_force_static_29.local_path = "refinement.parameterisation.beam.force_static"
        box_force_static_29.tmp_lst=[]
        box_force_static_29.tmp_lst.append("True")
        box_force_static_29.tmp_lst.append("False")
        for lst_itm in box_force_static_29.tmp_lst:
            box_force_static_29.addItem(lst_itm)
        box_force_static_29.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_29.addWidget(box_force_static_29)
        bg_box.addLayout(hbox_lay_force_static_29)

        label_30 = QLabel("            smoother")
        label_30.setPalette(palette_scope)
        label_30.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_30)

        hbox_lay_num_intervals_31 =  QHBoxLayout()
        label_num_intervals_31 = QLabel("                num_intervals")
        label_num_intervals_31.setPalette(palette_object)
        label_num_intervals_31.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_31.addWidget(label_num_intervals_31)

        box_num_intervals_31 = QComboBox()
        box_num_intervals_31.local_path = "refinement.parameterisation.beam.smoother.num_intervals"
        box_num_intervals_31.tmp_lst=[]
        box_num_intervals_31.tmp_lst.append("fixed_width")
        box_num_intervals_31.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_31.tmp_lst:
            box_num_intervals_31.addItem(lst_itm)
        box_num_intervals_31.setCurrentIndex(0)
        box_num_intervals_31.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_31.addWidget(box_num_intervals_31)
        bg_box.addLayout(hbox_lay_num_intervals_31)

        hbox_lay_interval_width_degrees_32 =  QHBoxLayout()
        label_interval_width_degrees_32 = QLabel("                interval_width_degrees")
        label_interval_width_degrees_32.setPalette(palette_object)
        label_interval_width_degrees_32.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_32.addWidget(label_interval_width_degrees_32)

        box_interval_width_degrees_32 = QDoubleSpinBox()
        box_interval_width_degrees_32.setValue(36.0)
        box_interval_width_degrees_32.local_path = "refinement.parameterisation.beam.smoother.interval_width_degrees"
        box_interval_width_degrees_32.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_32.addWidget(box_interval_width_degrees_32)
        bg_box.addLayout(hbox_lay_interval_width_degrees_32)

        hbox_lay_absolute_num_intervals_33 =  QHBoxLayout()
        label_absolute_num_intervals_33 = QLabel("                absolute_num_intervals")
        label_absolute_num_intervals_33.setPalette(palette_object)
        label_absolute_num_intervals_33.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_33.addWidget(label_absolute_num_intervals_33)

        box_absolute_num_intervals_33 = QSpinBox()
        box_absolute_num_intervals_33.setValue(5)
        box_absolute_num_intervals_33.local_path = "refinement.parameterisation.beam.smoother.absolute_num_intervals"
        box_absolute_num_intervals_33.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_33.addWidget(box_absolute_num_intervals_33)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_33)

        label_34 = QLabel("        crystal")
        label_34.setPalette(palette_scope)
        label_34.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_34)

        hbox_lay_fix_35 =  QHBoxLayout()
        label_fix_35 = QLabel("            fix")
        label_fix_35.setPalette(palette_object)
        label_fix_35.setFont(QFont("Monospace", 10))
        hbox_lay_fix_35.addWidget(label_fix_35)

        box_fix_35 = QComboBox()
        box_fix_35.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_35.tmp_lst=[]
        box_fix_35.tmp_lst.append("all")
        box_fix_35.tmp_lst.append("cell")
        box_fix_35.tmp_lst.append("orientation")
        for lst_itm in box_fix_35.tmp_lst:
            box_fix_35.addItem(lst_itm)
        box_fix_35.setCurrentIndex(0)
        box_fix_35.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_35.addWidget(box_fix_35)
        bg_box.addLayout(hbox_lay_fix_35)

        label_36 = QLabel("            unit_cell")
        label_36.setPalette(palette_scope)
        label_36.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_36)


        label_38 = QLabel("                restraints")
        label_38.setPalette(palette_scope)
        label_38.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_38)

        label_39 = QLabel("                    tie_to_target")
        label_39.setPalette(palette_scope)
        label_39.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_39)

        hbox_lay_values_40_0 =  QHBoxLayout()
        label_values_40_0 = QLabel("                        values[1]")
        label_values_40_0.setPalette(palette_object)
        label_values_40_0.setFont(QFont("Monospace", 10))
        hbox_lay_values_40_0.addWidget(label_values_40_0)
        box_values_40_0 = QDoubleSpinBox()
        box_values_40_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_40_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_40_1 =  QHBoxLayout()
        label_values_40_1 = QLabel("                        values[2]")
        label_values_40_1.setPalette(palette_object)
        label_values_40_1.setFont(QFont("Monospace", 10))
        hbox_lay_values_40_1.addWidget(label_values_40_1)
        box_values_40_1 = QDoubleSpinBox()
        box_values_40_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_40_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_40_2 =  QHBoxLayout()
        label_values_40_2 = QLabel("                        values[3]")
        label_values_40_2.setPalette(palette_object)
        label_values_40_2.setFont(QFont("Monospace", 10))
        hbox_lay_values_40_2.addWidget(label_values_40_2)
        box_values_40_2 = QDoubleSpinBox()
        box_values_40_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_40_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_40_3 =  QHBoxLayout()
        label_values_40_3 = QLabel("                        values[4]")
        label_values_40_3.setPalette(palette_object)
        label_values_40_3.setFont(QFont("Monospace", 10))
        hbox_lay_values_40_3.addWidget(label_values_40_3)
        box_values_40_3 = QDoubleSpinBox()
        box_values_40_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_40_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_40_4 =  QHBoxLayout()
        label_values_40_4 = QLabel("                        values[5]")
        label_values_40_4.setPalette(palette_object)
        label_values_40_4.setFont(QFont("Monospace", 10))
        hbox_lay_values_40_4.addWidget(label_values_40_4)
        box_values_40_4 = QDoubleSpinBox()
        box_values_40_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_40_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_40_5 =  QHBoxLayout()
        label_values_40_5 = QLabel("                        values[6]")
        label_values_40_5.setPalette(palette_object)
        label_values_40_5.setFont(QFont("Monospace", 10))
        hbox_lay_values_40_5.addWidget(label_values_40_5)
        box_values_40_5 = QDoubleSpinBox()
        box_values_40_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_40_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_sigmas_41_0 =  QHBoxLayout()
        label_sigmas_41_0 = QLabel("                        sigmas[1]")
        label_sigmas_41_0.setPalette(palette_object)
        label_sigmas_41_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_41_0.addWidget(label_sigmas_41_0)
        box_sigmas_41_0 = QDoubleSpinBox()
        box_sigmas_41_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_41_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_41_1 =  QHBoxLayout()
        label_sigmas_41_1 = QLabel("                        sigmas[2]")
        label_sigmas_41_1.setPalette(palette_object)
        label_sigmas_41_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_41_1.addWidget(label_sigmas_41_1)
        box_sigmas_41_1 = QDoubleSpinBox()
        box_sigmas_41_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_41_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_41_2 =  QHBoxLayout()
        label_sigmas_41_2 = QLabel("                        sigmas[3]")
        label_sigmas_41_2.setPalette(palette_object)
        label_sigmas_41_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_41_2.addWidget(label_sigmas_41_2)
        box_sigmas_41_2 = QDoubleSpinBox()
        box_sigmas_41_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_41_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_41_3 =  QHBoxLayout()
        label_sigmas_41_3 = QLabel("                        sigmas[4]")
        label_sigmas_41_3.setPalette(palette_object)
        label_sigmas_41_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_41_3.addWidget(label_sigmas_41_3)
        box_sigmas_41_3 = QDoubleSpinBox()
        box_sigmas_41_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_41_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_41_4 =  QHBoxLayout()
        label_sigmas_41_4 = QLabel("                        sigmas[5]")
        label_sigmas_41_4.setPalette(palette_object)
        label_sigmas_41_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_41_4.addWidget(label_sigmas_41_4)
        box_sigmas_41_4 = QDoubleSpinBox()
        box_sigmas_41_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_41_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_41_5 =  QHBoxLayout()
        label_sigmas_41_5 = QLabel("                        sigmas[6]")
        label_sigmas_41_5.setPalette(palette_object)
        label_sigmas_41_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_41_5.addWidget(label_sigmas_41_5)
        box_sigmas_41_5 = QDoubleSpinBox()
        box_sigmas_41_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_41_5.valueChanged.connect(self.spnbox_changed)


        hbox_lay_apply_to_all_43 =  QHBoxLayout()
        label_apply_to_all_43 = QLabel("                        apply_to_all")
        label_apply_to_all_43.setPalette(palette_object)
        label_apply_to_all_43.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_43.addWidget(label_apply_to_all_43)

        box_apply_to_all_43 = QComboBox()
        box_apply_to_all_43.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.apply_to_all"
        box_apply_to_all_43.tmp_lst=[]
        box_apply_to_all_43.tmp_lst.append("True")
        box_apply_to_all_43.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_43.tmp_lst:
            box_apply_to_all_43.addItem(lst_itm)
        box_apply_to_all_43.setCurrentIndex(1)
        box_apply_to_all_43.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_43.addWidget(box_apply_to_all_43)
        bg_box.addLayout(hbox_lay_apply_to_all_43)

        label_44 = QLabel("                    tie_to_group")
        label_44.setPalette(palette_scope)
        label_44.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_44)

        hbox_lay_target_45 =  QHBoxLayout()
        label_target_45 = QLabel("                        target")
        label_target_45.setPalette(palette_object)
        label_target_45.setFont(QFont("Monospace", 10))
        hbox_lay_target_45.addWidget(label_target_45)

        box_target_45 = QComboBox()
        box_target_45.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_45.tmp_lst=[]
        box_target_45.tmp_lst.append("mean")
        box_target_45.tmp_lst.append("low_memory_mean")
        box_target_45.tmp_lst.append("median")
        for lst_itm in box_target_45.tmp_lst:
            box_target_45.addItem(lst_itm)
        box_target_45.setCurrentIndex(0)
        box_target_45.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_45.addWidget(box_target_45)
        bg_box.addLayout(hbox_lay_target_45)

        hbox_lay_sigmas_46_0 =  QHBoxLayout()
        label_sigmas_46_0 = QLabel("                        sigmas[1]")
        label_sigmas_46_0.setPalette(palette_object)
        label_sigmas_46_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_46_0.addWidget(label_sigmas_46_0)
        box_sigmas_46_0 = QDoubleSpinBox()
        box_sigmas_46_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_46_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_46_1 =  QHBoxLayout()
        label_sigmas_46_1 = QLabel("                        sigmas[2]")
        label_sigmas_46_1.setPalette(palette_object)
        label_sigmas_46_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_46_1.addWidget(label_sigmas_46_1)
        box_sigmas_46_1 = QDoubleSpinBox()
        box_sigmas_46_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_46_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_46_2 =  QHBoxLayout()
        label_sigmas_46_2 = QLabel("                        sigmas[3]")
        label_sigmas_46_2.setPalette(palette_object)
        label_sigmas_46_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_46_2.addWidget(label_sigmas_46_2)
        box_sigmas_46_2 = QDoubleSpinBox()
        box_sigmas_46_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_46_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_46_3 =  QHBoxLayout()
        label_sigmas_46_3 = QLabel("                        sigmas[4]")
        label_sigmas_46_3.setPalette(palette_object)
        label_sigmas_46_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_46_3.addWidget(label_sigmas_46_3)
        box_sigmas_46_3 = QDoubleSpinBox()
        box_sigmas_46_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_46_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_46_4 =  QHBoxLayout()
        label_sigmas_46_4 = QLabel("                        sigmas[5]")
        label_sigmas_46_4.setPalette(palette_object)
        label_sigmas_46_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_46_4.addWidget(label_sigmas_46_4)
        box_sigmas_46_4 = QDoubleSpinBox()
        box_sigmas_46_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_46_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_46_5 =  QHBoxLayout()
        label_sigmas_46_5 = QLabel("                        sigmas[6]")
        label_sigmas_46_5.setPalette(palette_object)
        label_sigmas_46_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_46_5.addWidget(label_sigmas_46_5)
        box_sigmas_46_5 = QDoubleSpinBox()
        box_sigmas_46_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_46_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_46_0.addWidget(box_sigmas_46_0)
        bg_box.addLayout(hbox_lay_sigmas_46_0)
        hbox_lay_sigmas_46_1.addWidget(box_sigmas_46_1)
        bg_box.addLayout(hbox_lay_sigmas_46_1)
        hbox_lay_sigmas_46_2.addWidget(box_sigmas_46_2)
        bg_box.addLayout(hbox_lay_sigmas_46_2)
        hbox_lay_sigmas_46_3.addWidget(box_sigmas_46_3)
        bg_box.addLayout(hbox_lay_sigmas_46_3)
        hbox_lay_sigmas_46_4.addWidget(box_sigmas_46_4)
        bg_box.addLayout(hbox_lay_sigmas_46_4)
        hbox_lay_sigmas_46_5.addWidget(box_sigmas_46_5)
        bg_box.addLayout(hbox_lay_sigmas_46_5)


        hbox_lay_apply_to_all_48 =  QHBoxLayout()
        label_apply_to_all_48 = QLabel("                        apply_to_all")
        label_apply_to_all_48.setPalette(palette_object)
        label_apply_to_all_48.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_48.addWidget(label_apply_to_all_48)

        box_apply_to_all_48 = QComboBox()
        box_apply_to_all_48.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.apply_to_all"
        box_apply_to_all_48.tmp_lst=[]
        box_apply_to_all_48.tmp_lst.append("True")
        box_apply_to_all_48.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_48.tmp_lst:
            box_apply_to_all_48.addItem(lst_itm)
        box_apply_to_all_48.setCurrentIndex(1)
        box_apply_to_all_48.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_48.addWidget(box_apply_to_all_48)
        bg_box.addLayout(hbox_lay_apply_to_all_48)

        hbox_lay_force_static_49 =  QHBoxLayout()
        label_force_static_49 = QLabel("                force_static")
        label_force_static_49.setPalette(palette_object)
        label_force_static_49.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_49.addWidget(label_force_static_49)

        box_force_static_49 = QComboBox()
        box_force_static_49.local_path = "refinement.parameterisation.crystal.unit_cell.force_static"
        box_force_static_49.tmp_lst=[]
        box_force_static_49.tmp_lst.append("True")
        box_force_static_49.tmp_lst.append("False")
        for lst_itm in box_force_static_49.tmp_lst:
            box_force_static_49.addItem(lst_itm)
        box_force_static_49.setCurrentIndex(1)
        box_force_static_49.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_49.addWidget(box_force_static_49)
        bg_box.addLayout(hbox_lay_force_static_49)

        label_50 = QLabel("                smoother")
        label_50.setPalette(palette_scope)
        label_50.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_50)

        hbox_lay_num_intervals_51 =  QHBoxLayout()
        label_num_intervals_51 = QLabel("                    num_intervals")
        label_num_intervals_51.setPalette(palette_object)
        label_num_intervals_51.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_51.addWidget(label_num_intervals_51)

        box_num_intervals_51 = QComboBox()
        box_num_intervals_51.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.num_intervals"
        box_num_intervals_51.tmp_lst=[]
        box_num_intervals_51.tmp_lst.append("fixed_width")
        box_num_intervals_51.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_51.tmp_lst:
            box_num_intervals_51.addItem(lst_itm)
        box_num_intervals_51.setCurrentIndex(0)
        box_num_intervals_51.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_51.addWidget(box_num_intervals_51)
        bg_box.addLayout(hbox_lay_num_intervals_51)

        hbox_lay_interval_width_degrees_52 =  QHBoxLayout()
        label_interval_width_degrees_52 = QLabel("                    interval_width_degrees")
        label_interval_width_degrees_52.setPalette(palette_object)
        label_interval_width_degrees_52.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_52.addWidget(label_interval_width_degrees_52)

        box_interval_width_degrees_52 = QDoubleSpinBox()
        box_interval_width_degrees_52.setValue(36.0)
        box_interval_width_degrees_52.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.interval_width_degrees"
        box_interval_width_degrees_52.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_52.addWidget(box_interval_width_degrees_52)
        bg_box.addLayout(hbox_lay_interval_width_degrees_52)

        hbox_lay_absolute_num_intervals_53 =  QHBoxLayout()
        label_absolute_num_intervals_53 = QLabel("                    absolute_num_intervals")
        label_absolute_num_intervals_53.setPalette(palette_object)
        label_absolute_num_intervals_53.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_53.addWidget(label_absolute_num_intervals_53)

        box_absolute_num_intervals_53 = QSpinBox()
        box_absolute_num_intervals_53.setValue(5)
        box_absolute_num_intervals_53.local_path = "refinement.parameterisation.crystal.unit_cell.smoother.absolute_num_intervals"
        box_absolute_num_intervals_53.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_53.addWidget(box_absolute_num_intervals_53)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_53)

        label_54 = QLabel("            orientation")
        label_54.setPalette(palette_scope)
        label_54.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_54)


        hbox_lay_force_static_56 =  QHBoxLayout()
        label_force_static_56 = QLabel("                force_static")
        label_force_static_56.setPalette(palette_object)
        label_force_static_56.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_56.addWidget(label_force_static_56)

        box_force_static_56 = QComboBox()
        box_force_static_56.local_path = "refinement.parameterisation.crystal.orientation.force_static"
        box_force_static_56.tmp_lst=[]
        box_force_static_56.tmp_lst.append("True")
        box_force_static_56.tmp_lst.append("False")
        for lst_itm in box_force_static_56.tmp_lst:
            box_force_static_56.addItem(lst_itm)
        box_force_static_56.setCurrentIndex(1)
        box_force_static_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_56.addWidget(box_force_static_56)
        bg_box.addLayout(hbox_lay_force_static_56)

        label_57 = QLabel("                smoother")
        label_57.setPalette(palette_scope)
        label_57.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_57)

        hbox_lay_num_intervals_58 =  QHBoxLayout()
        label_num_intervals_58 = QLabel("                    num_intervals")
        label_num_intervals_58.setPalette(palette_object)
        label_num_intervals_58.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_58.addWidget(label_num_intervals_58)

        box_num_intervals_58 = QComboBox()
        box_num_intervals_58.local_path = "refinement.parameterisation.crystal.orientation.smoother.num_intervals"
        box_num_intervals_58.tmp_lst=[]
        box_num_intervals_58.tmp_lst.append("fixed_width")
        box_num_intervals_58.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_58.tmp_lst:
            box_num_intervals_58.addItem(lst_itm)
        box_num_intervals_58.setCurrentIndex(0)
        box_num_intervals_58.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_58.addWidget(box_num_intervals_58)
        bg_box.addLayout(hbox_lay_num_intervals_58)

        hbox_lay_interval_width_degrees_59 =  QHBoxLayout()
        label_interval_width_degrees_59 = QLabel("                    interval_width_degrees")
        label_interval_width_degrees_59.setPalette(palette_object)
        label_interval_width_degrees_59.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_59.addWidget(label_interval_width_degrees_59)

        box_interval_width_degrees_59 = QDoubleSpinBox()
        box_interval_width_degrees_59.setValue(36.0)
        box_interval_width_degrees_59.local_path = "refinement.parameterisation.crystal.orientation.smoother.interval_width_degrees"
        box_interval_width_degrees_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_59.addWidget(box_interval_width_degrees_59)
        bg_box.addLayout(hbox_lay_interval_width_degrees_59)

        hbox_lay_absolute_num_intervals_60 =  QHBoxLayout()
        label_absolute_num_intervals_60 = QLabel("                    absolute_num_intervals")
        label_absolute_num_intervals_60.setPalette(palette_object)
        label_absolute_num_intervals_60.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_60.addWidget(label_absolute_num_intervals_60)

        box_absolute_num_intervals_60 = QSpinBox()
        box_absolute_num_intervals_60.setValue(5)
        box_absolute_num_intervals_60.local_path = "refinement.parameterisation.crystal.orientation.smoother.absolute_num_intervals"
        box_absolute_num_intervals_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_60.addWidget(box_absolute_num_intervals_60)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_60)

        label_61 = QLabel("        detector")
        label_61.setPalette(palette_scope)
        label_61.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_61)

        hbox_lay_panels_62 =  QHBoxLayout()
        label_panels_62 = QLabel("            panels")
        label_panels_62.setPalette(palette_object)
        label_panels_62.setFont(QFont("Monospace", 10))
        hbox_lay_panels_62.addWidget(label_panels_62)

        box_panels_62 = QComboBox()
        box_panels_62.local_path = "refinement.parameterisation.detector.panels"
        box_panels_62.tmp_lst=[]
        box_panels_62.tmp_lst.append("automatic")
        box_panels_62.tmp_lst.append("single")
        box_panels_62.tmp_lst.append("multiple")
        box_panels_62.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_62.tmp_lst:
            box_panels_62.addItem(lst_itm)
        box_panels_62.setCurrentIndex(0)
        box_panels_62.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_62.addWidget(box_panels_62)
        bg_box.addLayout(hbox_lay_panels_62)

        hbox_lay_hierarchy_level_63 =  QHBoxLayout()
        label_hierarchy_level_63 = QLabel("            hierarchy_level")
        label_hierarchy_level_63.setPalette(palette_object)
        label_hierarchy_level_63.setFont(QFont("Monospace", 10))
        hbox_lay_hierarchy_level_63.addWidget(label_hierarchy_level_63)

        box_hierarchy_level_63 = QSpinBox()
        box_hierarchy_level_63.setValue(0)
        box_hierarchy_level_63.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_63.addWidget(box_hierarchy_level_63)
        bg_box.addLayout(hbox_lay_hierarchy_level_63)

        hbox_lay_fix_64 =  QHBoxLayout()
        label_fix_64 = QLabel("            fix")
        label_fix_64.setPalette(palette_object)
        label_fix_64.setFont(QFont("Monospace", 10))
        hbox_lay_fix_64.addWidget(label_fix_64)

        box_fix_64 = QComboBox()
        box_fix_64.local_path = "refinement.parameterisation.detector.fix"
        box_fix_64.tmp_lst=[]
        box_fix_64.tmp_lst.append("all")
        box_fix_64.tmp_lst.append("position")
        box_fix_64.tmp_lst.append("orientation")
        for lst_itm in box_fix_64.tmp_lst:
            box_fix_64.addItem(lst_itm)
        box_fix_64.setCurrentIndex(0)
        box_fix_64.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_64.addWidget(box_fix_64)
        bg_box.addLayout(hbox_lay_fix_64)


        hbox_lay_force_static_66 =  QHBoxLayout()
        label_force_static_66 = QLabel("            force_static")
        label_force_static_66.setPalette(palette_object)
        label_force_static_66.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_66.addWidget(label_force_static_66)

        box_force_static_66 = QComboBox()
        box_force_static_66.local_path = "refinement.parameterisation.detector.force_static"
        box_force_static_66.tmp_lst=[]
        box_force_static_66.tmp_lst.append("True")
        box_force_static_66.tmp_lst.append("False")
        for lst_itm in box_force_static_66.tmp_lst:
            box_force_static_66.addItem(lst_itm)
        box_force_static_66.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_66.addWidget(box_force_static_66)
        bg_box.addLayout(hbox_lay_force_static_66)

        label_67 = QLabel("            smoother")
        label_67.setPalette(palette_scope)
        label_67.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_67)

        hbox_lay_num_intervals_68 =  QHBoxLayout()
        label_num_intervals_68 = QLabel("                num_intervals")
        label_num_intervals_68.setPalette(palette_object)
        label_num_intervals_68.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_68.addWidget(label_num_intervals_68)

        box_num_intervals_68 = QComboBox()
        box_num_intervals_68.local_path = "refinement.parameterisation.detector.smoother.num_intervals"
        box_num_intervals_68.tmp_lst=[]
        box_num_intervals_68.tmp_lst.append("fixed_width")
        box_num_intervals_68.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_68.tmp_lst:
            box_num_intervals_68.addItem(lst_itm)
        box_num_intervals_68.setCurrentIndex(0)
        box_num_intervals_68.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_68.addWidget(box_num_intervals_68)
        bg_box.addLayout(hbox_lay_num_intervals_68)

        hbox_lay_interval_width_degrees_69 =  QHBoxLayout()
        label_interval_width_degrees_69 = QLabel("                interval_width_degrees")
        label_interval_width_degrees_69.setPalette(palette_object)
        label_interval_width_degrees_69.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_69.addWidget(label_interval_width_degrees_69)

        box_interval_width_degrees_69 = QDoubleSpinBox()
        box_interval_width_degrees_69.setValue(36.0)
        box_interval_width_degrees_69.local_path = "refinement.parameterisation.detector.smoother.interval_width_degrees"
        box_interval_width_degrees_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_69.addWidget(box_interval_width_degrees_69)
        bg_box.addLayout(hbox_lay_interval_width_degrees_69)

        hbox_lay_absolute_num_intervals_70 =  QHBoxLayout()
        label_absolute_num_intervals_70 = QLabel("                absolute_num_intervals")
        label_absolute_num_intervals_70.setPalette(palette_object)
        label_absolute_num_intervals_70.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_70.addWidget(label_absolute_num_intervals_70)

        box_absolute_num_intervals_70 = QSpinBox()
        box_absolute_num_intervals_70.setValue(5)
        box_absolute_num_intervals_70.local_path = "refinement.parameterisation.detector.smoother.absolute_num_intervals"
        box_absolute_num_intervals_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_70.addWidget(box_absolute_num_intervals_70)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_70)

        hbox_lay_sparse_71 =  QHBoxLayout()
        label_sparse_71 = QLabel("        sparse")
        label_sparse_71.setPalette(palette_object)
        label_sparse_71.setFont(QFont("Monospace", 10))
        hbox_lay_sparse_71.addWidget(label_sparse_71)

        box_sparse_71 = QComboBox()
        box_sparse_71.local_path = "refinement.parameterisation.sparse"
        box_sparse_71.tmp_lst=[]
        box_sparse_71.tmp_lst.append("True")
        box_sparse_71.tmp_lst.append("False")
        for lst_itm in box_sparse_71.tmp_lst:
            box_sparse_71.addItem(lst_itm)
        box_sparse_71.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_71.addWidget(box_sparse_71)
        bg_box.addLayout(hbox_lay_sparse_71)

        hbox_lay_treat_single_image_as_still_72 =  QHBoxLayout()
        label_treat_single_image_as_still_72 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_72.setPalette(palette_object)
        label_treat_single_image_as_still_72.setFont(QFont("Monospace", 10))
        hbox_lay_treat_single_image_as_still_72.addWidget(label_treat_single_image_as_still_72)

        box_treat_single_image_as_still_72 = QComboBox()
        box_treat_single_image_as_still_72.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_72.tmp_lst=[]
        box_treat_single_image_as_still_72.tmp_lst.append("True")
        box_treat_single_image_as_still_72.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_72.tmp_lst:
            box_treat_single_image_as_still_72.addItem(lst_itm)
        box_treat_single_image_as_still_72.setCurrentIndex(1)
        box_treat_single_image_as_still_72.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_72.addWidget(box_treat_single_image_as_still_72)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_72)

        hbox_lay_spherical_relp_model_73 =  QHBoxLayout()
        label_spherical_relp_model_73 = QLabel("        spherical_relp_model")
        label_spherical_relp_model_73.setPalette(palette_object)
        label_spherical_relp_model_73.setFont(QFont("Monospace", 10))
        hbox_lay_spherical_relp_model_73.addWidget(label_spherical_relp_model_73)

        box_spherical_relp_model_73 = QComboBox()
        box_spherical_relp_model_73.local_path = "refinement.parameterisation.spherical_relp_model"
        box_spherical_relp_model_73.tmp_lst=[]
        box_spherical_relp_model_73.tmp_lst.append("True")
        box_spherical_relp_model_73.tmp_lst.append("False")
        for lst_itm in box_spherical_relp_model_73.tmp_lst:
            box_spherical_relp_model_73.addItem(lst_itm)
        box_spherical_relp_model_73.setCurrentIndex(1)
        box_spherical_relp_model_73.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_spherical_relp_model_73.addWidget(box_spherical_relp_model_73)
        bg_box.addLayout(hbox_lay_spherical_relp_model_73)

        label_74 = QLabel("    refinery")
        label_74.setPalette(palette_scope)
        label_74.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_74)

        hbox_lay_engine_75 =  QHBoxLayout()
        label_engine_75 = QLabel("        engine")
        label_engine_75.setPalette(palette_object)
        label_engine_75.setFont(QFont("Monospace", 10))
        hbox_lay_engine_75.addWidget(label_engine_75)

        box_engine_75 = QComboBox()
        box_engine_75.local_path = "refinement.refinery.engine"
        box_engine_75.tmp_lst=[]
        box_engine_75.tmp_lst.append("SimpleLBFGS")
        box_engine_75.tmp_lst.append("LBFGScurvs")
        box_engine_75.tmp_lst.append("GaussNewton")
        box_engine_75.tmp_lst.append("LevMar")
        box_engine_75.tmp_lst.append("SparseLevMar")
        for lst_itm in box_engine_75.tmp_lst:
            box_engine_75.addItem(lst_itm)
        box_engine_75.setCurrentIndex(3)
        box_engine_75.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_75.addWidget(box_engine_75)
        bg_box.addLayout(hbox_lay_engine_75)

        hbox_lay_track_step_76 =  QHBoxLayout()
        label_track_step_76 = QLabel("        track_step")
        label_track_step_76.setPalette(palette_object)
        label_track_step_76.setFont(QFont("Monospace", 10))
        hbox_lay_track_step_76.addWidget(label_track_step_76)

        box_track_step_76 = QComboBox()
        box_track_step_76.local_path = "refinement.refinery.track_step"
        box_track_step_76.tmp_lst=[]
        box_track_step_76.tmp_lst.append("True")
        box_track_step_76.tmp_lst.append("False")
        for lst_itm in box_track_step_76.tmp_lst:
            box_track_step_76.addItem(lst_itm)
        box_track_step_76.setCurrentIndex(1)
        box_track_step_76.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_76.addWidget(box_track_step_76)
        bg_box.addLayout(hbox_lay_track_step_76)

        hbox_lay_track_gradient_77 =  QHBoxLayout()
        label_track_gradient_77 = QLabel("        track_gradient")
        label_track_gradient_77.setPalette(palette_object)
        label_track_gradient_77.setFont(QFont("Monospace", 10))
        hbox_lay_track_gradient_77.addWidget(label_track_gradient_77)

        box_track_gradient_77 = QComboBox()
        box_track_gradient_77.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_77.tmp_lst=[]
        box_track_gradient_77.tmp_lst.append("True")
        box_track_gradient_77.tmp_lst.append("False")
        for lst_itm in box_track_gradient_77.tmp_lst:
            box_track_gradient_77.addItem(lst_itm)
        box_track_gradient_77.setCurrentIndex(1)
        box_track_gradient_77.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_77.addWidget(box_track_gradient_77)
        bg_box.addLayout(hbox_lay_track_gradient_77)

        hbox_lay_track_parameter_correlation_78 =  QHBoxLayout()
        label_track_parameter_correlation_78 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_78.setPalette(palette_object)
        label_track_parameter_correlation_78.setFont(QFont("Monospace", 10))
        hbox_lay_track_parameter_correlation_78.addWidget(label_track_parameter_correlation_78)

        box_track_parameter_correlation_78 = QComboBox()
        box_track_parameter_correlation_78.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_78.tmp_lst=[]
        box_track_parameter_correlation_78.tmp_lst.append("True")
        box_track_parameter_correlation_78.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_78.tmp_lst:
            box_track_parameter_correlation_78.addItem(lst_itm)
        box_track_parameter_correlation_78.setCurrentIndex(1)
        box_track_parameter_correlation_78.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_78.addWidget(box_track_parameter_correlation_78)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_78)

        hbox_lay_track_out_of_sample_rmsd_79 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_79 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_79.setPalette(palette_object)
        label_track_out_of_sample_rmsd_79.setFont(QFont("Monospace", 10))
        hbox_lay_track_out_of_sample_rmsd_79.addWidget(label_track_out_of_sample_rmsd_79)

        box_track_out_of_sample_rmsd_79 = QComboBox()
        box_track_out_of_sample_rmsd_79.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_79.tmp_lst=[]
        box_track_out_of_sample_rmsd_79.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_79.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_79.tmp_lst:
            box_track_out_of_sample_rmsd_79.addItem(lst_itm)
        box_track_out_of_sample_rmsd_79.setCurrentIndex(1)
        box_track_out_of_sample_rmsd_79.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_79.addWidget(box_track_out_of_sample_rmsd_79)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_79)


        hbox_lay_max_iterations_81 =  QHBoxLayout()
        label_max_iterations_81 = QLabel("        max_iterations")
        label_max_iterations_81.setPalette(palette_object)
        label_max_iterations_81.setFont(QFont("Monospace", 10))
        hbox_lay_max_iterations_81.addWidget(label_max_iterations_81)

        box_max_iterations_81 = QSpinBox()
        box_max_iterations_81.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_81.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_81.addWidget(box_max_iterations_81)
        bg_box.addLayout(hbox_lay_max_iterations_81)

        label_82 = QLabel("    target")
        label_82.setPalette(palette_scope)
        label_82.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_82)

        hbox_lay_rmsd_cutoff_83 =  QHBoxLayout()
        label_rmsd_cutoff_83 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_83.setPalette(palette_object)
        label_rmsd_cutoff_83.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_83.addWidget(label_rmsd_cutoff_83)

        box_rmsd_cutoff_83 = QComboBox()
        box_rmsd_cutoff_83.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_83.tmp_lst=[]
        box_rmsd_cutoff_83.tmp_lst.append("fraction_of_bin_size")
        box_rmsd_cutoff_83.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_83.tmp_lst:
            box_rmsd_cutoff_83.addItem(lst_itm)
        box_rmsd_cutoff_83.setCurrentIndex(0)
        box_rmsd_cutoff_83.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_83.addWidget(box_rmsd_cutoff_83)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_83)

        hbox_lay_bin_size_fraction_84 =  QHBoxLayout()
        label_bin_size_fraction_84 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_84.setPalette(palette_object)
        label_bin_size_fraction_84.setFont(QFont("Monospace", 10))
        hbox_lay_bin_size_fraction_84.addWidget(label_bin_size_fraction_84)

        box_bin_size_fraction_84 = QDoubleSpinBox()
        box_bin_size_fraction_84.setValue(0.0)
        box_bin_size_fraction_84.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_84.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_84.addWidget(box_bin_size_fraction_84)
        bg_box.addLayout(hbox_lay_bin_size_fraction_84)

        hbox_lay_absolute_cutoffs_85_0 =  QHBoxLayout()
        label_absolute_cutoffs_85_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_85_0.setPalette(palette_object)
        label_absolute_cutoffs_85_0.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_85_0.addWidget(label_absolute_cutoffs_85_0)
        box_absolute_cutoffs_85_0 = QDoubleSpinBox()
        box_absolute_cutoffs_85_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_85_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_85_1 =  QHBoxLayout()
        label_absolute_cutoffs_85_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_85_1.setPalette(palette_object)
        label_absolute_cutoffs_85_1.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_85_1.addWidget(label_absolute_cutoffs_85_1)
        box_absolute_cutoffs_85_1 = QDoubleSpinBox()
        box_absolute_cutoffs_85_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_85_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_85_2 =  QHBoxLayout()
        label_absolute_cutoffs_85_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_85_2.setPalette(palette_object)
        label_absolute_cutoffs_85_2.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_85_2.addWidget(label_absolute_cutoffs_85_2)
        box_absolute_cutoffs_85_2 = QDoubleSpinBox()
        box_absolute_cutoffs_85_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_85_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_85_0.addWidget(box_absolute_cutoffs_85_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_85_0)
        hbox_lay_absolute_cutoffs_85_1.addWidget(box_absolute_cutoffs_85_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_85_1)
        hbox_lay_absolute_cutoffs_85_2.addWidget(box_absolute_cutoffs_85_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_85_2)

        hbox_lay_gradient_calculation_blocksize_86 =  QHBoxLayout()
        label_gradient_calculation_blocksize_86 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_86.setPalette(palette_object)
        label_gradient_calculation_blocksize_86.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_calculation_blocksize_86.addWidget(label_gradient_calculation_blocksize_86)

        box_gradient_calculation_blocksize_86 = QSpinBox()
        box_gradient_calculation_blocksize_86.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_86.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_86.addWidget(box_gradient_calculation_blocksize_86)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_86)

        label_87 = QLabel("    reflections")
        label_87.setPalette(palette_scope)
        label_87.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_87)

        hbox_lay_reflections_per_degree_88 =  QHBoxLayout()
        label_reflections_per_degree_88 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_88.setPalette(palette_object)
        label_reflections_per_degree_88.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_88.addWidget(label_reflections_per_degree_88)

        box_reflections_per_degree_88 = QDoubleSpinBox()
        box_reflections_per_degree_88.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_88.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_88.addWidget(box_reflections_per_degree_88)
        bg_box.addLayout(hbox_lay_reflections_per_degree_88)

        hbox_lay_minimum_sample_size_89 =  QHBoxLayout()
        label_minimum_sample_size_89 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_89.setPalette(palette_object)
        label_minimum_sample_size_89.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_89.addWidget(label_minimum_sample_size_89)

        box_minimum_sample_size_89 = QSpinBox()
        box_minimum_sample_size_89.setValue(1000)
        box_minimum_sample_size_89.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_89.addWidget(box_minimum_sample_size_89)
        bg_box.addLayout(hbox_lay_minimum_sample_size_89)

        hbox_lay_maximum_sample_size_90 =  QHBoxLayout()
        label_maximum_sample_size_90 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_90.setPalette(palette_object)
        label_maximum_sample_size_90.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_90.addWidget(label_maximum_sample_size_90)

        box_maximum_sample_size_90 = QSpinBox()
        box_maximum_sample_size_90.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_90.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_90.addWidget(box_maximum_sample_size_90)
        bg_box.addLayout(hbox_lay_maximum_sample_size_90)

        hbox_lay_random_seed_91 =  QHBoxLayout()
        label_random_seed_91 = QLabel("        random_seed")
        label_random_seed_91.setPalette(palette_object)
        label_random_seed_91.setFont(QFont("Monospace", 10))
        hbox_lay_random_seed_91.addWidget(label_random_seed_91)

        box_random_seed_91 = QSpinBox()
        box_random_seed_91.setValue(42)
        box_random_seed_91.local_path = "refinement.reflections.random_seed"
        box_random_seed_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_91.addWidget(box_random_seed_91)
        bg_box.addLayout(hbox_lay_random_seed_91)

        hbox_lay_close_to_spindle_cutoff_92 =  QHBoxLayout()
        label_close_to_spindle_cutoff_92 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_92.setPalette(palette_object)
        label_close_to_spindle_cutoff_92.setFont(QFont("Monospace", 10))
        hbox_lay_close_to_spindle_cutoff_92.addWidget(label_close_to_spindle_cutoff_92)

        box_close_to_spindle_cutoff_92 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_92.setValue(0.02)
        box_close_to_spindle_cutoff_92.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_92.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_92.addWidget(box_close_to_spindle_cutoff_92)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_92)

        hbox_lay_block_width_93 =  QHBoxLayout()
        label_block_width_93 = QLabel("        block_width")
        label_block_width_93.setPalette(palette_object)
        label_block_width_93.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_93.addWidget(label_block_width_93)

        box_block_width_93 = QDoubleSpinBox()
        box_block_width_93.setValue(1.0)
        box_block_width_93.local_path = "refinement.reflections.block_width"
        box_block_width_93.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_93.addWidget(box_block_width_93)
        bg_box.addLayout(hbox_lay_block_width_93)

        label_94 = QLabel("        weighting_strategy")
        label_94.setPalette(palette_scope)
        label_94.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_94)

        hbox_lay_override_95 =  QHBoxLayout()
        label_override_95 = QLabel("            override")
        label_override_95.setPalette(palette_object)
        label_override_95.setFont(QFont("Monospace", 10))
        hbox_lay_override_95.addWidget(label_override_95)

        box_override_95 = QComboBox()
        box_override_95.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_95.tmp_lst=[]
        box_override_95.tmp_lst.append("statistical")
        box_override_95.tmp_lst.append("stills")
        box_override_95.tmp_lst.append("constant")
        box_override_95.tmp_lst.append("external_deltapsi")
        for lst_itm in box_override_95.tmp_lst:
            box_override_95.addItem(lst_itm)
        box_override_95.setCurrentIndex(0)
        box_override_95.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_95.addWidget(box_override_95)
        bg_box.addLayout(hbox_lay_override_95)

        hbox_lay_delpsi_constant_96 =  QHBoxLayout()
        label_delpsi_constant_96 = QLabel("            delpsi_constant")
        label_delpsi_constant_96.setPalette(palette_object)
        label_delpsi_constant_96.setFont(QFont("Monospace", 10))
        hbox_lay_delpsi_constant_96.addWidget(label_delpsi_constant_96)

        box_delpsi_constant_96 = QDoubleSpinBox()
        box_delpsi_constant_96.setValue(1000000.0)
        box_delpsi_constant_96.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_96.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_96.addWidget(box_delpsi_constant_96)
        bg_box.addLayout(hbox_lay_delpsi_constant_96)

        hbox_lay_constants_97_0 =  QHBoxLayout()
        label_constants_97_0 = QLabel("            constants[1]")
        label_constants_97_0.setPalette(palette_object)
        label_constants_97_0.setFont(QFont("Monospace", 10))
        hbox_lay_constants_97_0.addWidget(label_constants_97_0)
        box_constants_97_0 = QDoubleSpinBox()
        box_constants_97_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_97_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_97_1 =  QHBoxLayout()
        label_constants_97_1 = QLabel("            constants[2]")
        label_constants_97_1.setPalette(palette_object)
        label_constants_97_1.setFont(QFont("Monospace", 10))
        hbox_lay_constants_97_1.addWidget(label_constants_97_1)
        box_constants_97_1 = QDoubleSpinBox()
        box_constants_97_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_97_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_97_2 =  QHBoxLayout()
        label_constants_97_2 = QLabel("            constants[3]")
        label_constants_97_2.setPalette(palette_object)
        label_constants_97_2.setFont(QFont("Monospace", 10))
        hbox_lay_constants_97_2.addWidget(label_constants_97_2)
        box_constants_97_2 = QDoubleSpinBox()
        box_constants_97_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_97_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_97_0.addWidget(box_constants_97_0)
        bg_box.addLayout(hbox_lay_constants_97_0)
        hbox_lay_constants_97_1.addWidget(box_constants_97_1)
        bg_box.addLayout(hbox_lay_constants_97_1)
        hbox_lay_constants_97_2.addWidget(box_constants_97_2)
        bg_box.addLayout(hbox_lay_constants_97_2)

        label_98 = QLabel("        outlier")
        label_98.setPalette(palette_scope)
        label_98.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_98)

        hbox_lay_algorithm_99 =  QHBoxLayout()
        label_algorithm_99 = QLabel("            algorithm")
        label_algorithm_99.setPalette(palette_object)
        label_algorithm_99.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_99.addWidget(label_algorithm_99)

        box_algorithm_99 = QComboBox()
        box_algorithm_99.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_99.tmp_lst=[]
        box_algorithm_99.tmp_lst.append("null")
        box_algorithm_99.tmp_lst.append("auto")
        box_algorithm_99.tmp_lst.append("mcd")
        box_algorithm_99.tmp_lst.append("tukey")
        box_algorithm_99.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_99.tmp_lst:
            box_algorithm_99.addItem(lst_itm)
        box_algorithm_99.setCurrentIndex(1)
        box_algorithm_99.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_99.addWidget(box_algorithm_99)
        bg_box.addLayout(hbox_lay_algorithm_99)

        hbox_lay_minimum_number_of_reflections_100 =  QHBoxLayout()
        label_minimum_number_of_reflections_100 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_100.setPalette(palette_object)
        label_minimum_number_of_reflections_100.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_number_of_reflections_100.addWidget(label_minimum_number_of_reflections_100)

        box_minimum_number_of_reflections_100 = QSpinBox()
        box_minimum_number_of_reflections_100.setValue(20)
        box_minimum_number_of_reflections_100.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_100.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_100.addWidget(box_minimum_number_of_reflections_100)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_100)

        hbox_lay_separate_experiments_101 =  QHBoxLayout()
        label_separate_experiments_101 = QLabel("            separate_experiments")
        label_separate_experiments_101.setPalette(palette_object)
        label_separate_experiments_101.setFont(QFont("Monospace", 10))
        hbox_lay_separate_experiments_101.addWidget(label_separate_experiments_101)

        box_separate_experiments_101 = QComboBox()
        box_separate_experiments_101.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_101.tmp_lst=[]
        box_separate_experiments_101.tmp_lst.append("True")
        box_separate_experiments_101.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_101.tmp_lst:
            box_separate_experiments_101.addItem(lst_itm)
        box_separate_experiments_101.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_101.addWidget(box_separate_experiments_101)
        bg_box.addLayout(hbox_lay_separate_experiments_101)

        hbox_lay_separate_panels_102 =  QHBoxLayout()
        label_separate_panels_102 = QLabel("            separate_panels")
        label_separate_panels_102.setPalette(palette_object)
        label_separate_panels_102.setFont(QFont("Monospace", 10))
        hbox_lay_separate_panels_102.addWidget(label_separate_panels_102)

        box_separate_panels_102 = QComboBox()
        box_separate_panels_102.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_102.tmp_lst=[]
        box_separate_panels_102.tmp_lst.append("True")
        box_separate_panels_102.tmp_lst.append("False")
        for lst_itm in box_separate_panels_102.tmp_lst:
            box_separate_panels_102.addItem(lst_itm)
        box_separate_panels_102.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_102.addWidget(box_separate_panels_102)
        bg_box.addLayout(hbox_lay_separate_panels_102)

        hbox_lay_separate_blocks_103 =  QHBoxLayout()
        label_separate_blocks_103 = QLabel("            separate_blocks")
        label_separate_blocks_103.setPalette(palette_object)
        label_separate_blocks_103.setFont(QFont("Monospace", 10))
        hbox_lay_separate_blocks_103.addWidget(label_separate_blocks_103)

        box_separate_blocks_103 = QComboBox()
        box_separate_blocks_103.local_path = "refinement.reflections.outlier.separate_blocks"
        box_separate_blocks_103.tmp_lst=[]
        box_separate_blocks_103.tmp_lst.append("True")
        box_separate_blocks_103.tmp_lst.append("False")
        for lst_itm in box_separate_blocks_103.tmp_lst:
            box_separate_blocks_103.addItem(lst_itm)
        box_separate_blocks_103.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_blocks_103.addWidget(box_separate_blocks_103)
        bg_box.addLayout(hbox_lay_separate_blocks_103)

        hbox_lay_block_width_104 =  QHBoxLayout()
        label_block_width_104 = QLabel("            block_width")
        label_block_width_104.setPalette(palette_object)
        label_block_width_104.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_104.addWidget(label_block_width_104)

        box_block_width_104 = QDoubleSpinBox()
        box_block_width_104.local_path = "refinement.reflections.outlier.block_width"
        box_block_width_104.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_104.addWidget(box_block_width_104)
        bg_box.addLayout(hbox_lay_block_width_104)

        label_105 = QLabel("            tukey")
        label_105.setPalette(palette_scope)
        label_105.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_105)

        hbox_lay_iqr_multiplier_106 =  QHBoxLayout()
        label_iqr_multiplier_106 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_106.setPalette(palette_object)
        label_iqr_multiplier_106.setFont(QFont("Monospace", 10))
        hbox_lay_iqr_multiplier_106.addWidget(label_iqr_multiplier_106)

        box_iqr_multiplier_106 = QDoubleSpinBox()
        box_iqr_multiplier_106.setValue(1.5)
        box_iqr_multiplier_106.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_106.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_106.addWidget(box_iqr_multiplier_106)
        bg_box.addLayout(hbox_lay_iqr_multiplier_106)

        label_107 = QLabel("            mcd")
        label_107.setPalette(palette_scope)
        label_107.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_107)

        hbox_lay_alpha_108 =  QHBoxLayout()
        label_alpha_108 = QLabel("                alpha")
        label_alpha_108.setPalette(palette_object)
        label_alpha_108.setFont(QFont("Monospace", 10))
        hbox_lay_alpha_108.addWidget(label_alpha_108)

        box_alpha_108 = QDoubleSpinBox()
        box_alpha_108.setValue(0.5)
        box_alpha_108.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_108.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_108.addWidget(box_alpha_108)
        bg_box.addLayout(hbox_lay_alpha_108)

        hbox_lay_max_n_groups_109 =  QHBoxLayout()
        label_max_n_groups_109 = QLabel("                max_n_groups")
        label_max_n_groups_109.setPalette(palette_object)
        label_max_n_groups_109.setFont(QFont("Monospace", 10))
        hbox_lay_max_n_groups_109.addWidget(label_max_n_groups_109)

        box_max_n_groups_109 = QSpinBox()
        box_max_n_groups_109.setValue(5)
        box_max_n_groups_109.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_109.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_109.addWidget(box_max_n_groups_109)
        bg_box.addLayout(hbox_lay_max_n_groups_109)

        hbox_lay_min_group_size_110 =  QHBoxLayout()
        label_min_group_size_110 = QLabel("                min_group_size")
        label_min_group_size_110.setPalette(palette_object)
        label_min_group_size_110.setFont(QFont("Monospace", 10))
        hbox_lay_min_group_size_110.addWidget(label_min_group_size_110)

        box_min_group_size_110 = QSpinBox()
        box_min_group_size_110.setValue(300)
        box_min_group_size_110.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_110.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_110.addWidget(box_min_group_size_110)
        bg_box.addLayout(hbox_lay_min_group_size_110)

        hbox_lay_n_trials_111 =  QHBoxLayout()
        label_n_trials_111 = QLabel("                n_trials")
        label_n_trials_111.setPalette(palette_object)
        label_n_trials_111.setFont(QFont("Monospace", 10))
        hbox_lay_n_trials_111.addWidget(label_n_trials_111)

        box_n_trials_111 = QSpinBox()
        box_n_trials_111.setValue(500)
        box_n_trials_111.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_111.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_111.addWidget(box_n_trials_111)
        bg_box.addLayout(hbox_lay_n_trials_111)

        hbox_lay_k1_112 =  QHBoxLayout()
        label_k1_112 = QLabel("                k1")
        label_k1_112.setPalette(palette_object)
        label_k1_112.setFont(QFont("Monospace", 10))
        hbox_lay_k1_112.addWidget(label_k1_112)

        box_k1_112 = QSpinBox()
        box_k1_112.setValue(2)
        box_k1_112.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_112.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_112.addWidget(box_k1_112)
        bg_box.addLayout(hbox_lay_k1_112)

        hbox_lay_k2_113 =  QHBoxLayout()
        label_k2_113 = QLabel("                k2")
        label_k2_113.setPalette(palette_object)
        label_k2_113.setFont(QFont("Monospace", 10))
        hbox_lay_k2_113.addWidget(label_k2_113)

        box_k2_113 = QSpinBox()
        box_k2_113.setValue(2)
        box_k2_113.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_113.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_113.addWidget(box_k2_113)
        bg_box.addLayout(hbox_lay_k2_113)

        hbox_lay_k3_114 =  QHBoxLayout()
        label_k3_114 = QLabel("                k3")
        label_k3_114.setPalette(palette_object)
        label_k3_114.setFont(QFont("Monospace", 10))
        hbox_lay_k3_114.addWidget(label_k3_114)

        box_k3_114 = QSpinBox()
        box_k3_114.setValue(100)
        box_k3_114.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_114.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_114.addWidget(box_k3_114)
        bg_box.addLayout(hbox_lay_k3_114)

        hbox_lay_threshold_probability_115 =  QHBoxLayout()
        label_threshold_probability_115 = QLabel("                threshold_probability")
        label_threshold_probability_115.setPalette(palette_object)
        label_threshold_probability_115.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_probability_115.addWidget(label_threshold_probability_115)

        box_threshold_probability_115 = QDoubleSpinBox()
        box_threshold_probability_115.setValue(0.975)
        box_threshold_probability_115.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_115.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_115.addWidget(box_threshold_probability_115)
        bg_box.addLayout(hbox_lay_threshold_probability_115)

        label_116 = QLabel("            sauter_poon")
        label_116.setPalette(palette_scope)
        label_116.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_116)

        hbox_lay_px_sz_117_0 =  QHBoxLayout()
        label_px_sz_117_0 = QLabel("                px_sz[1]")
        label_px_sz_117_0.setPalette(palette_object)
        label_px_sz_117_0.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_117_0.addWidget(label_px_sz_117_0)
        box_px_sz_117_0 = QDoubleSpinBox()
        box_px_sz_117_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_117_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_117_1 =  QHBoxLayout()
        label_px_sz_117_1 = QLabel("                px_sz[2]")
        label_px_sz_117_1.setPalette(palette_object)
        label_px_sz_117_1.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_117_1.addWidget(label_px_sz_117_1)
        box_px_sz_117_1 = QDoubleSpinBox()
        box_px_sz_117_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_117_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_117_0.addWidget(box_px_sz_117_0)
        bg_box.addLayout(hbox_lay_px_sz_117_0)
        hbox_lay_px_sz_117_1.addWidget(box_px_sz_117_1)
        bg_box.addLayout(hbox_lay_px_sz_117_1)

        hbox_lay_verbose_118 =  QHBoxLayout()
        label_verbose_118 = QLabel("                verbose")
        label_verbose_118.setPalette(palette_object)
        label_verbose_118.setFont(QFont("Monospace", 10))
        hbox_lay_verbose_118.addWidget(label_verbose_118)

        box_verbose_118 = QComboBox()
        box_verbose_118.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_118.tmp_lst=[]
        box_verbose_118.tmp_lst.append("True")
        box_verbose_118.tmp_lst.append("False")
        for lst_itm in box_verbose_118.tmp_lst:
            box_verbose_118.addItem(lst_itm)
        box_verbose_118.setCurrentIndex(1)
        box_verbose_118.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_118.addWidget(box_verbose_118)
        bg_box.addLayout(hbox_lay_verbose_118)

        hbox_lay_pdf_119 =  QHBoxLayout()
        label_pdf_119 = QLabel("                pdf")
        label_pdf_119.setPalette(palette_object)
        label_pdf_119.setFont(QFont("Monospace", 10))
        hbox_lay_pdf_119.addWidget(label_pdf_119)

        box_pdf_119 = QLineEdit()
        box_pdf_119.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_119.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_119.addWidget(box_pdf_119)
        bg_box.addLayout(hbox_lay_pdf_119)

 
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
