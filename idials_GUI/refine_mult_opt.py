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

        label_22 = QLabel("        beam")
        label_22.setPalette(palette_scope)
        label_22.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_22)

        hbox_lay_fix_23 =  QHBoxLayout()
        label_fix_23 = QLabel("            fix")
        label_fix_23.setPalette(palette_object)
        label_fix_23.setFont(QFont("Monospace", 10))
        hbox_lay_fix_23.addWidget(label_fix_23)

        box_fix_23 = QComboBox()
        box_fix_23.local_path = "refinement.parameterisation.beam.fix"
        box_fix_23.tmp_lst=[]
        box_fix_23.tmp_lst.append("all")
        box_fix_23.tmp_lst.append("in_spindle_plane")
        box_fix_23.tmp_lst.append("out_spindle_plane")
        box_fix_23.tmp_lst.append("wavelength")
        for lst_itm in box_fix_23.tmp_lst:
            box_fix_23.addItem(lst_itm)
        box_fix_23.setCurrentIndex(3)
        box_fix_23.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_23.addWidget(box_fix_23)
        bg_box.addLayout(hbox_lay_fix_23)


        label_25 = QLabel("        crystal")
        label_25.setPalette(palette_scope)
        label_25.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_25)

        hbox_lay_fix_26 =  QHBoxLayout()
        label_fix_26 = QLabel("            fix")
        label_fix_26.setPalette(palette_object)
        label_fix_26.setFont(QFont("Monospace", 10))
        hbox_lay_fix_26.addWidget(label_fix_26)

        box_fix_26 = QComboBox()
        box_fix_26.local_path = "refinement.parameterisation.crystal.fix"
        box_fix_26.tmp_lst=[]
        box_fix_26.tmp_lst.append("all")
        box_fix_26.tmp_lst.append("cell")
        box_fix_26.tmp_lst.append("orientation")
        for lst_itm in box_fix_26.tmp_lst:
            box_fix_26.addItem(lst_itm)
        box_fix_26.setCurrentIndex(0)
        box_fix_26.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_26.addWidget(box_fix_26)
        bg_box.addLayout(hbox_lay_fix_26)

        label_27 = QLabel("            unit_cell")
        label_27.setPalette(palette_scope)
        label_27.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_27)


        label_29 = QLabel("                restraints")
        label_29.setPalette(palette_scope)
        label_29.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_29)

        label_30 = QLabel("                    tie_to_target")
        label_30.setPalette(palette_scope)
        label_30.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_30)

        hbox_lay_values_31_0 =  QHBoxLayout()
        label_values_31_0 = QLabel("                        values[1]")
        label_values_31_0.setPalette(palette_object)
        label_values_31_0.setFont(QFont("Monospace", 10))
        hbox_lay_values_31_0.addWidget(label_values_31_0)
        box_values_31_0 = QDoubleSpinBox()
        box_values_31_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_1 =  QHBoxLayout()
        label_values_31_1 = QLabel("                        values[2]")
        label_values_31_1.setPalette(palette_object)
        label_values_31_1.setFont(QFont("Monospace", 10))
        hbox_lay_values_31_1.addWidget(label_values_31_1)
        box_values_31_1 = QDoubleSpinBox()
        box_values_31_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_2 =  QHBoxLayout()
        label_values_31_2 = QLabel("                        values[3]")
        label_values_31_2.setPalette(palette_object)
        label_values_31_2.setFont(QFont("Monospace", 10))
        hbox_lay_values_31_2.addWidget(label_values_31_2)
        box_values_31_2 = QDoubleSpinBox()
        box_values_31_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_3 =  QHBoxLayout()
        label_values_31_3 = QLabel("                        values[4]")
        label_values_31_3.setPalette(palette_object)
        label_values_31_3.setFont(QFont("Monospace", 10))
        hbox_lay_values_31_3.addWidget(label_values_31_3)
        box_values_31_3 = QDoubleSpinBox()
        box_values_31_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_4 =  QHBoxLayout()
        label_values_31_4 = QLabel("                        values[5]")
        label_values_31_4.setPalette(palette_object)
        label_values_31_4.setFont(QFont("Monospace", 10))
        hbox_lay_values_31_4.addWidget(label_values_31_4)
        box_values_31_4 = QDoubleSpinBox()
        box_values_31_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_values_31_5 =  QHBoxLayout()
        label_values_31_5 = QLabel("                        values[6]")
        label_values_31_5.setPalette(palette_object)
        label_values_31_5.setFont(QFont("Monospace", 10))
        hbox_lay_values_31_5.addWidget(label_values_31_5)
        box_values_31_5 = QDoubleSpinBox()
        box_values_31_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.values"
        #box_values_31_5.valueChanged.connect(self.spnbox_changed)

        hbox_lay_sigmas_32_0 =  QHBoxLayout()
        label_sigmas_32_0 = QLabel("                        sigmas[1]")
        label_sigmas_32_0.setPalette(palette_object)
        label_sigmas_32_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_32_0.addWidget(label_sigmas_32_0)
        box_sigmas_32_0 = QDoubleSpinBox()
        box_sigmas_32_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_1 =  QHBoxLayout()
        label_sigmas_32_1 = QLabel("                        sigmas[2]")
        label_sigmas_32_1.setPalette(palette_object)
        label_sigmas_32_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_32_1.addWidget(label_sigmas_32_1)
        box_sigmas_32_1 = QDoubleSpinBox()
        box_sigmas_32_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_2 =  QHBoxLayout()
        label_sigmas_32_2 = QLabel("                        sigmas[3]")
        label_sigmas_32_2.setPalette(palette_object)
        label_sigmas_32_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_32_2.addWidget(label_sigmas_32_2)
        box_sigmas_32_2 = QDoubleSpinBox()
        box_sigmas_32_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_3 =  QHBoxLayout()
        label_sigmas_32_3 = QLabel("                        sigmas[4]")
        label_sigmas_32_3.setPalette(palette_object)
        label_sigmas_32_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_32_3.addWidget(label_sigmas_32_3)
        box_sigmas_32_3 = QDoubleSpinBox()
        box_sigmas_32_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_4 =  QHBoxLayout()
        label_sigmas_32_4 = QLabel("                        sigmas[5]")
        label_sigmas_32_4.setPalette(palette_object)
        label_sigmas_32_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_32_4.addWidget(label_sigmas_32_4)
        box_sigmas_32_4 = QDoubleSpinBox()
        box_sigmas_32_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_32_5 =  QHBoxLayout()
        label_sigmas_32_5 = QLabel("                        sigmas[6]")
        label_sigmas_32_5.setPalette(palette_object)
        label_sigmas_32_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_32_5.addWidget(label_sigmas_32_5)
        box_sigmas_32_5 = QDoubleSpinBox()
        box_sigmas_32_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.sigmas"
        #box_sigmas_32_5.valueChanged.connect(self.spnbox_changed)


        hbox_lay_apply_to_all_34 =  QHBoxLayout()
        label_apply_to_all_34 = QLabel("                        apply_to_all")
        label_apply_to_all_34.setPalette(palette_object)
        label_apply_to_all_34.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_34.addWidget(label_apply_to_all_34)

        box_apply_to_all_34 = QComboBox()
        box_apply_to_all_34.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_target.apply_to_all"
        box_apply_to_all_34.tmp_lst=[]
        box_apply_to_all_34.tmp_lst.append("True")
        box_apply_to_all_34.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_34.tmp_lst:
            box_apply_to_all_34.addItem(lst_itm)
        box_apply_to_all_34.setCurrentIndex(1)
        box_apply_to_all_34.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_34.addWidget(box_apply_to_all_34)
        bg_box.addLayout(hbox_lay_apply_to_all_34)

        label_35 = QLabel("                    tie_to_group")
        label_35.setPalette(palette_scope)
        label_35.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_35)

        hbox_lay_target_36 =  QHBoxLayout()
        label_target_36 = QLabel("                        target")
        label_target_36.setPalette(palette_object)
        label_target_36.setFont(QFont("Monospace", 10))
        hbox_lay_target_36.addWidget(label_target_36)

        box_target_36 = QComboBox()
        box_target_36.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.target"
        box_target_36.tmp_lst=[]
        box_target_36.tmp_lst.append("mean")
        box_target_36.tmp_lst.append("low_memory_mean")
        box_target_36.tmp_lst.append("median")
        for lst_itm in box_target_36.tmp_lst:
            box_target_36.addItem(lst_itm)
        box_target_36.setCurrentIndex(0)
        box_target_36.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_target_36.addWidget(box_target_36)
        bg_box.addLayout(hbox_lay_target_36)

        hbox_lay_sigmas_37_0 =  QHBoxLayout()
        label_sigmas_37_0 = QLabel("                        sigmas[1]")
        label_sigmas_37_0.setPalette(palette_object)
        label_sigmas_37_0.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_37_0.addWidget(label_sigmas_37_0)
        box_sigmas_37_0 = QDoubleSpinBox()
        box_sigmas_37_0.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_37_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_37_1 =  QHBoxLayout()
        label_sigmas_37_1 = QLabel("                        sigmas[2]")
        label_sigmas_37_1.setPalette(palette_object)
        label_sigmas_37_1.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_37_1.addWidget(label_sigmas_37_1)
        box_sigmas_37_1 = QDoubleSpinBox()
        box_sigmas_37_1.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_37_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_37_2 =  QHBoxLayout()
        label_sigmas_37_2 = QLabel("                        sigmas[3]")
        label_sigmas_37_2.setPalette(palette_object)
        label_sigmas_37_2.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_37_2.addWidget(label_sigmas_37_2)
        box_sigmas_37_2 = QDoubleSpinBox()
        box_sigmas_37_2.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_37_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_37_3 =  QHBoxLayout()
        label_sigmas_37_3 = QLabel("                        sigmas[4]")
        label_sigmas_37_3.setPalette(palette_object)
        label_sigmas_37_3.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_37_3.addWidget(label_sigmas_37_3)
        box_sigmas_37_3 = QDoubleSpinBox()
        box_sigmas_37_3.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_37_3.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_37_4 =  QHBoxLayout()
        label_sigmas_37_4 = QLabel("                        sigmas[5]")
        label_sigmas_37_4.setPalette(palette_object)
        label_sigmas_37_4.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_37_4.addWidget(label_sigmas_37_4)
        box_sigmas_37_4 = QDoubleSpinBox()
        box_sigmas_37_4.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_37_4.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_37_5 =  QHBoxLayout()
        label_sigmas_37_5 = QLabel("                        sigmas[6]")
        label_sigmas_37_5.setPalette(palette_object)
        label_sigmas_37_5.setFont(QFont("Monospace", 10))
        hbox_lay_sigmas_37_5.addWidget(label_sigmas_37_5)
        box_sigmas_37_5 = QDoubleSpinBox()
        box_sigmas_37_5.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.sigmas"
        #box_sigmas_37_5.valueChanged.connect(self.spnbox_changed)
        hbox_lay_sigmas_37_0.addWidget(box_sigmas_37_0)
        bg_box.addLayout(hbox_lay_sigmas_37_0)
        hbox_lay_sigmas_37_1.addWidget(box_sigmas_37_1)
        bg_box.addLayout(hbox_lay_sigmas_37_1)
        hbox_lay_sigmas_37_2.addWidget(box_sigmas_37_2)
        bg_box.addLayout(hbox_lay_sigmas_37_2)
        hbox_lay_sigmas_37_3.addWidget(box_sigmas_37_3)
        bg_box.addLayout(hbox_lay_sigmas_37_3)
        hbox_lay_sigmas_37_4.addWidget(box_sigmas_37_4)
        bg_box.addLayout(hbox_lay_sigmas_37_4)
        hbox_lay_sigmas_37_5.addWidget(box_sigmas_37_5)
        bg_box.addLayout(hbox_lay_sigmas_37_5)


        hbox_lay_apply_to_all_39 =  QHBoxLayout()
        label_apply_to_all_39 = QLabel("                        apply_to_all")
        label_apply_to_all_39.setPalette(palette_object)
        label_apply_to_all_39.setFont(QFont("Monospace", 10))
        hbox_lay_apply_to_all_39.addWidget(label_apply_to_all_39)

        box_apply_to_all_39 = QComboBox()
        box_apply_to_all_39.local_path = "refinement.parameterisation.crystal.unit_cell.restraints.tie_to_group.apply_to_all"
        box_apply_to_all_39.tmp_lst=[]
        box_apply_to_all_39.tmp_lst.append("True")
        box_apply_to_all_39.tmp_lst.append("False")
        for lst_itm in box_apply_to_all_39.tmp_lst:
            box_apply_to_all_39.addItem(lst_itm)
        box_apply_to_all_39.setCurrentIndex(1)
        box_apply_to_all_39.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_to_all_39.addWidget(box_apply_to_all_39)
        bg_box.addLayout(hbox_lay_apply_to_all_39)

        label_40 = QLabel("            orientation")
        label_40.setPalette(palette_scope)
        label_40.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_40)


        hbox_lay_scan_varying_42 =  QHBoxLayout()
        label_scan_varying_42 = QLabel("            scan_varying")
        label_scan_varying_42.setPalette(palette_object)
        label_scan_varying_42.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_42.addWidget(label_scan_varying_42)

        box_scan_varying_42 = QComboBox()
        box_scan_varying_42.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying_42.tmp_lst=[]
        box_scan_varying_42.tmp_lst.append("True")
        box_scan_varying_42.tmp_lst.append("False")
        for lst_itm in box_scan_varying_42.tmp_lst:
            box_scan_varying_42.addItem(lst_itm)
        box_scan_varying_42.setCurrentIndex(1)
        box_scan_varying_42.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_42.addWidget(box_scan_varying_42)
        bg_box.addLayout(hbox_lay_scan_varying_42)

        hbox_lay_num_intervals_43 =  QHBoxLayout()
        label_num_intervals_43 = QLabel("            num_intervals")
        label_num_intervals_43.setPalette(palette_object)
        label_num_intervals_43.setFont(QFont("Monospace", 10))
        hbox_lay_num_intervals_43.addWidget(label_num_intervals_43)

        box_num_intervals_43 = QComboBox()
        box_num_intervals_43.local_path = "refinement.parameterisation.crystal.num_intervals"
        box_num_intervals_43.tmp_lst=[]
        box_num_intervals_43.tmp_lst.append("fixed_width")
        box_num_intervals_43.tmp_lst.append("absolute")
        for lst_itm in box_num_intervals_43.tmp_lst:
            box_num_intervals_43.addItem(lst_itm)
        box_num_intervals_43.setCurrentIndex(0)
        box_num_intervals_43.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_num_intervals_43.addWidget(box_num_intervals_43)
        bg_box.addLayout(hbox_lay_num_intervals_43)

        hbox_lay_interval_width_degrees_44 =  QHBoxLayout()
        label_interval_width_degrees_44 = QLabel("            interval_width_degrees")
        label_interval_width_degrees_44.setPalette(palette_object)
        label_interval_width_degrees_44.setFont(QFont("Monospace", 10))
        hbox_lay_interval_width_degrees_44.addWidget(label_interval_width_degrees_44)

        box_interval_width_degrees_44 = QDoubleSpinBox()
        box_interval_width_degrees_44.setValue(36.0)
        box_interval_width_degrees_44.local_path = "refinement.parameterisation.crystal.interval_width_degrees"
        box_interval_width_degrees_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_interval_width_degrees_44.addWidget(box_interval_width_degrees_44)
        bg_box.addLayout(hbox_lay_interval_width_degrees_44)

        hbox_lay_absolute_num_intervals_45 =  QHBoxLayout()
        label_absolute_num_intervals_45 = QLabel("            absolute_num_intervals")
        label_absolute_num_intervals_45.setPalette(palette_object)
        label_absolute_num_intervals_45.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_num_intervals_45.addWidget(label_absolute_num_intervals_45)

        box_absolute_num_intervals_45 = QSpinBox()
        box_absolute_num_intervals_45.setValue(5)
        box_absolute_num_intervals_45.local_path = "refinement.parameterisation.crystal.absolute_num_intervals"
        box_absolute_num_intervals_45.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_num_intervals_45.addWidget(box_absolute_num_intervals_45)
        bg_box.addLayout(hbox_lay_absolute_num_intervals_45)

        hbox_lay_UB_model_per_46 =  QHBoxLayout()
        label_UB_model_per_46 = QLabel("            UB_model_per")
        label_UB_model_per_46.setPalette(palette_object)
        label_UB_model_per_46.setFont(QFont("Monospace", 10))
        hbox_lay_UB_model_per_46.addWidget(label_UB_model_per_46)

        box_UB_model_per_46 = QComboBox()
        box_UB_model_per_46.local_path = "refinement.parameterisation.crystal.UB_model_per"
        box_UB_model_per_46.tmp_lst=[]
        box_UB_model_per_46.tmp_lst.append("reflection")
        box_UB_model_per_46.tmp_lst.append("image")
        box_UB_model_per_46.tmp_lst.append("block")
        for lst_itm in box_UB_model_per_46.tmp_lst:
            box_UB_model_per_46.addItem(lst_itm)
        box_UB_model_per_46.setCurrentIndex(2)
        box_UB_model_per_46.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_UB_model_per_46.addWidget(box_UB_model_per_46)
        bg_box.addLayout(hbox_lay_UB_model_per_46)

        label_47 = QLabel("        detector")
        label_47.setPalette(palette_scope)
        label_47.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_47)

        hbox_lay_panels_48 =  QHBoxLayout()
        label_panels_48 = QLabel("            panels")
        label_panels_48.setPalette(palette_object)
        label_panels_48.setFont(QFont("Monospace", 10))
        hbox_lay_panels_48.addWidget(label_panels_48)

        box_panels_48 = QComboBox()
        box_panels_48.local_path = "refinement.parameterisation.detector.panels"
        box_panels_48.tmp_lst=[]
        box_panels_48.tmp_lst.append("automatic")
        box_panels_48.tmp_lst.append("single")
        box_panels_48.tmp_lst.append("multiple")
        box_panels_48.tmp_lst.append("hierarchical")
        for lst_itm in box_panels_48.tmp_lst:
            box_panels_48.addItem(lst_itm)
        box_panels_48.setCurrentIndex(0)
        box_panels_48.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_panels_48.addWidget(box_panels_48)
        bg_box.addLayout(hbox_lay_panels_48)

        hbox_lay_hierarchy_level_49 =  QHBoxLayout()
        label_hierarchy_level_49 = QLabel("            hierarchy_level")
        label_hierarchy_level_49.setPalette(palette_object)
        label_hierarchy_level_49.setFont(QFont("Monospace", 10))
        hbox_lay_hierarchy_level_49.addWidget(label_hierarchy_level_49)

        box_hierarchy_level_49 = QSpinBox()
        box_hierarchy_level_49.setValue(0)
        box_hierarchy_level_49.local_path = "refinement.parameterisation.detector.hierarchy_level"
        box_hierarchy_level_49.valueChanged.connect(self.spnbox_changed)
        hbox_lay_hierarchy_level_49.addWidget(box_hierarchy_level_49)
        bg_box.addLayout(hbox_lay_hierarchy_level_49)

        hbox_lay_fix_50 =  QHBoxLayout()
        label_fix_50 = QLabel("            fix")
        label_fix_50.setPalette(palette_object)
        label_fix_50.setFont(QFont("Monospace", 10))
        hbox_lay_fix_50.addWidget(label_fix_50)

        box_fix_50 = QComboBox()
        box_fix_50.local_path = "refinement.parameterisation.detector.fix"
        box_fix_50.tmp_lst=[]
        box_fix_50.tmp_lst.append("all")
        box_fix_50.tmp_lst.append("position")
        box_fix_50.tmp_lst.append("orientation")
        for lst_itm in box_fix_50.tmp_lst:
            box_fix_50.addItem(lst_itm)
        box_fix_50.setCurrentIndex(0)
        box_fix_50.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fix_50.addWidget(box_fix_50)
        bg_box.addLayout(hbox_lay_fix_50)


        hbox_lay_sparse_52 =  QHBoxLayout()
        label_sparse_52 = QLabel("        sparse")
        label_sparse_52.setPalette(palette_object)
        label_sparse_52.setFont(QFont("Monospace", 10))
        hbox_lay_sparse_52.addWidget(label_sparse_52)

        box_sparse_52 = QComboBox()
        box_sparse_52.local_path = "refinement.parameterisation.sparse"
        box_sparse_52.tmp_lst=[]
        box_sparse_52.tmp_lst.append("True")
        box_sparse_52.tmp_lst.append("False")
        for lst_itm in box_sparse_52.tmp_lst:
            box_sparse_52.addItem(lst_itm)
        box_sparse_52.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_sparse_52.addWidget(box_sparse_52)
        bg_box.addLayout(hbox_lay_sparse_52)

        hbox_lay_treat_single_image_as_still_53 =  QHBoxLayout()
        label_treat_single_image_as_still_53 = QLabel("        treat_single_image_as_still")
        label_treat_single_image_as_still_53.setPalette(palette_object)
        label_treat_single_image_as_still_53.setFont(QFont("Monospace", 10))
        hbox_lay_treat_single_image_as_still_53.addWidget(label_treat_single_image_as_still_53)

        box_treat_single_image_as_still_53 = QComboBox()
        box_treat_single_image_as_still_53.local_path = "refinement.parameterisation.treat_single_image_as_still"
        box_treat_single_image_as_still_53.tmp_lst=[]
        box_treat_single_image_as_still_53.tmp_lst.append("True")
        box_treat_single_image_as_still_53.tmp_lst.append("False")
        for lst_itm in box_treat_single_image_as_still_53.tmp_lst:
            box_treat_single_image_as_still_53.addItem(lst_itm)
        box_treat_single_image_as_still_53.setCurrentIndex(1)
        box_treat_single_image_as_still_53.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_treat_single_image_as_still_53.addWidget(box_treat_single_image_as_still_53)
        bg_box.addLayout(hbox_lay_treat_single_image_as_still_53)

        hbox_lay_spherical_relp_model_54 =  QHBoxLayout()
        label_spherical_relp_model_54 = QLabel("        spherical_relp_model")
        label_spherical_relp_model_54.setPalette(palette_object)
        label_spherical_relp_model_54.setFont(QFont("Monospace", 10))
        hbox_lay_spherical_relp_model_54.addWidget(label_spherical_relp_model_54)

        box_spherical_relp_model_54 = QComboBox()
        box_spherical_relp_model_54.local_path = "refinement.parameterisation.spherical_relp_model"
        box_spherical_relp_model_54.tmp_lst=[]
        box_spherical_relp_model_54.tmp_lst.append("True")
        box_spherical_relp_model_54.tmp_lst.append("False")
        for lst_itm in box_spherical_relp_model_54.tmp_lst:
            box_spherical_relp_model_54.addItem(lst_itm)
        box_spherical_relp_model_54.setCurrentIndex(1)
        box_spherical_relp_model_54.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_spherical_relp_model_54.addWidget(box_spherical_relp_model_54)
        bg_box.addLayout(hbox_lay_spherical_relp_model_54)

        label_55 = QLabel("    refinery")
        label_55.setPalette(palette_scope)
        label_55.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_55)

        hbox_lay_engine_56 =  QHBoxLayout()
        label_engine_56 = QLabel("        engine")
        label_engine_56.setPalette(palette_object)
        label_engine_56.setFont(QFont("Monospace", 10))
        hbox_lay_engine_56.addWidget(label_engine_56)

        box_engine_56 = QComboBox()
        box_engine_56.local_path = "refinement.refinery.engine"
        box_engine_56.tmp_lst=[]
        box_engine_56.tmp_lst.append("SimpleLBFGS")
        box_engine_56.tmp_lst.append("LBFGScurvs")
        box_engine_56.tmp_lst.append("GaussNewton")
        box_engine_56.tmp_lst.append("LevMar")
        box_engine_56.tmp_lst.append("SparseLevMar")
        for lst_itm in box_engine_56.tmp_lst:
            box_engine_56.addItem(lst_itm)
        box_engine_56.setCurrentIndex(3)
        box_engine_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_engine_56.addWidget(box_engine_56)
        bg_box.addLayout(hbox_lay_engine_56)

        hbox_lay_track_step_57 =  QHBoxLayout()
        label_track_step_57 = QLabel("        track_step")
        label_track_step_57.setPalette(palette_object)
        label_track_step_57.setFont(QFont("Monospace", 10))
        hbox_lay_track_step_57.addWidget(label_track_step_57)

        box_track_step_57 = QComboBox()
        box_track_step_57.local_path = "refinement.refinery.track_step"
        box_track_step_57.tmp_lst=[]
        box_track_step_57.tmp_lst.append("True")
        box_track_step_57.tmp_lst.append("False")
        for lst_itm in box_track_step_57.tmp_lst:
            box_track_step_57.addItem(lst_itm)
        box_track_step_57.setCurrentIndex(1)
        box_track_step_57.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_step_57.addWidget(box_track_step_57)
        bg_box.addLayout(hbox_lay_track_step_57)

        hbox_lay_track_gradient_58 =  QHBoxLayout()
        label_track_gradient_58 = QLabel("        track_gradient")
        label_track_gradient_58.setPalette(palette_object)
        label_track_gradient_58.setFont(QFont("Monospace", 10))
        hbox_lay_track_gradient_58.addWidget(label_track_gradient_58)

        box_track_gradient_58 = QComboBox()
        box_track_gradient_58.local_path = "refinement.refinery.track_gradient"
        box_track_gradient_58.tmp_lst=[]
        box_track_gradient_58.tmp_lst.append("True")
        box_track_gradient_58.tmp_lst.append("False")
        for lst_itm in box_track_gradient_58.tmp_lst:
            box_track_gradient_58.addItem(lst_itm)
        box_track_gradient_58.setCurrentIndex(1)
        box_track_gradient_58.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_gradient_58.addWidget(box_track_gradient_58)
        bg_box.addLayout(hbox_lay_track_gradient_58)

        hbox_lay_track_parameter_correlation_59 =  QHBoxLayout()
        label_track_parameter_correlation_59 = QLabel("        track_parameter_correlation")
        label_track_parameter_correlation_59.setPalette(palette_object)
        label_track_parameter_correlation_59.setFont(QFont("Monospace", 10))
        hbox_lay_track_parameter_correlation_59.addWidget(label_track_parameter_correlation_59)

        box_track_parameter_correlation_59 = QComboBox()
        box_track_parameter_correlation_59.local_path = "refinement.refinery.track_parameter_correlation"
        box_track_parameter_correlation_59.tmp_lst=[]
        box_track_parameter_correlation_59.tmp_lst.append("True")
        box_track_parameter_correlation_59.tmp_lst.append("False")
        for lst_itm in box_track_parameter_correlation_59.tmp_lst:
            box_track_parameter_correlation_59.addItem(lst_itm)
        box_track_parameter_correlation_59.setCurrentIndex(1)
        box_track_parameter_correlation_59.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_parameter_correlation_59.addWidget(box_track_parameter_correlation_59)
        bg_box.addLayout(hbox_lay_track_parameter_correlation_59)

        hbox_lay_track_out_of_sample_rmsd_60 =  QHBoxLayout()
        label_track_out_of_sample_rmsd_60 = QLabel("        track_out_of_sample_rmsd")
        label_track_out_of_sample_rmsd_60.setPalette(palette_object)
        label_track_out_of_sample_rmsd_60.setFont(QFont("Monospace", 10))
        hbox_lay_track_out_of_sample_rmsd_60.addWidget(label_track_out_of_sample_rmsd_60)

        box_track_out_of_sample_rmsd_60 = QComboBox()
        box_track_out_of_sample_rmsd_60.local_path = "refinement.refinery.track_out_of_sample_rmsd"
        box_track_out_of_sample_rmsd_60.tmp_lst=[]
        box_track_out_of_sample_rmsd_60.tmp_lst.append("True")
        box_track_out_of_sample_rmsd_60.tmp_lst.append("False")
        for lst_itm in box_track_out_of_sample_rmsd_60.tmp_lst:
            box_track_out_of_sample_rmsd_60.addItem(lst_itm)
        box_track_out_of_sample_rmsd_60.setCurrentIndex(1)
        box_track_out_of_sample_rmsd_60.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_track_out_of_sample_rmsd_60.addWidget(box_track_out_of_sample_rmsd_60)
        bg_box.addLayout(hbox_lay_track_out_of_sample_rmsd_60)


        hbox_lay_max_iterations_62 =  QHBoxLayout()
        label_max_iterations_62 = QLabel("        max_iterations")
        label_max_iterations_62.setPalette(palette_object)
        label_max_iterations_62.setFont(QFont("Monospace", 10))
        hbox_lay_max_iterations_62.addWidget(label_max_iterations_62)

        box_max_iterations_62 = QSpinBox()
        box_max_iterations_62.local_path = "refinement.refinery.max_iterations"
        box_max_iterations_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_iterations_62.addWidget(box_max_iterations_62)
        bg_box.addLayout(hbox_lay_max_iterations_62)

        label_63 = QLabel("    target")
        label_63.setPalette(palette_scope)
        label_63.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_63)

        hbox_lay_rmsd_cutoff_64 =  QHBoxLayout()
        label_rmsd_cutoff_64 = QLabel("        rmsd_cutoff")
        label_rmsd_cutoff_64.setPalette(palette_object)
        label_rmsd_cutoff_64.setFont(QFont("Monospace", 10))
        hbox_lay_rmsd_cutoff_64.addWidget(label_rmsd_cutoff_64)

        box_rmsd_cutoff_64 = QComboBox()
        box_rmsd_cutoff_64.local_path = "refinement.target.rmsd_cutoff"
        box_rmsd_cutoff_64.tmp_lst=[]
        box_rmsd_cutoff_64.tmp_lst.append("fraction_of_bin_size")
        box_rmsd_cutoff_64.tmp_lst.append("absolute")
        for lst_itm in box_rmsd_cutoff_64.tmp_lst:
            box_rmsd_cutoff_64.addItem(lst_itm)
        box_rmsd_cutoff_64.setCurrentIndex(0)
        box_rmsd_cutoff_64.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_rmsd_cutoff_64.addWidget(box_rmsd_cutoff_64)
        bg_box.addLayout(hbox_lay_rmsd_cutoff_64)

        hbox_lay_bin_size_fraction_65 =  QHBoxLayout()
        label_bin_size_fraction_65 = QLabel("        bin_size_fraction")
        label_bin_size_fraction_65.setPalette(palette_object)
        label_bin_size_fraction_65.setFont(QFont("Monospace", 10))
        hbox_lay_bin_size_fraction_65.addWidget(label_bin_size_fraction_65)

        box_bin_size_fraction_65 = QDoubleSpinBox()
        box_bin_size_fraction_65.setValue(0.2)
        box_bin_size_fraction_65.local_path = "refinement.target.bin_size_fraction"
        box_bin_size_fraction_65.valueChanged.connect(self.spnbox_changed)
        hbox_lay_bin_size_fraction_65.addWidget(box_bin_size_fraction_65)
        bg_box.addLayout(hbox_lay_bin_size_fraction_65)

        hbox_lay_absolute_cutoffs_66_0 =  QHBoxLayout()
        label_absolute_cutoffs_66_0 = QLabel("        absolute_cutoffs[1]")
        label_absolute_cutoffs_66_0.setPalette(palette_object)
        label_absolute_cutoffs_66_0.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_66_0.addWidget(label_absolute_cutoffs_66_0)
        box_absolute_cutoffs_66_0 = QDoubleSpinBox()
        box_absolute_cutoffs_66_0.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_66_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_66_1 =  QHBoxLayout()
        label_absolute_cutoffs_66_1 = QLabel("        absolute_cutoffs[2]")
        label_absolute_cutoffs_66_1.setPalette(palette_object)
        label_absolute_cutoffs_66_1.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_66_1.addWidget(label_absolute_cutoffs_66_1)
        box_absolute_cutoffs_66_1 = QDoubleSpinBox()
        box_absolute_cutoffs_66_1.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_66_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_66_2 =  QHBoxLayout()
        label_absolute_cutoffs_66_2 = QLabel("        absolute_cutoffs[3]")
        label_absolute_cutoffs_66_2.setPalette(palette_object)
        label_absolute_cutoffs_66_2.setFont(QFont("Monospace", 10))
        hbox_lay_absolute_cutoffs_66_2.addWidget(label_absolute_cutoffs_66_2)
        box_absolute_cutoffs_66_2 = QDoubleSpinBox()
        box_absolute_cutoffs_66_2.local_path = "refinement.target.absolute_cutoffs"
        #box_absolute_cutoffs_66_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_absolute_cutoffs_66_0.addWidget(box_absolute_cutoffs_66_0)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_66_0)
        hbox_lay_absolute_cutoffs_66_1.addWidget(box_absolute_cutoffs_66_1)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_66_1)
        hbox_lay_absolute_cutoffs_66_2.addWidget(box_absolute_cutoffs_66_2)
        bg_box.addLayout(hbox_lay_absolute_cutoffs_66_2)

        hbox_lay_gradient_calculation_blocksize_67 =  QHBoxLayout()
        label_gradient_calculation_blocksize_67 = QLabel("        gradient_calculation_blocksize")
        label_gradient_calculation_blocksize_67.setPalette(palette_object)
        label_gradient_calculation_blocksize_67.setFont(QFont("Monospace", 10))
        hbox_lay_gradient_calculation_blocksize_67.addWidget(label_gradient_calculation_blocksize_67)

        box_gradient_calculation_blocksize_67 = QSpinBox()
        box_gradient_calculation_blocksize_67.local_path = "refinement.target.gradient_calculation_blocksize"
        box_gradient_calculation_blocksize_67.valueChanged.connect(self.spnbox_changed)
        hbox_lay_gradient_calculation_blocksize_67.addWidget(box_gradient_calculation_blocksize_67)
        bg_box.addLayout(hbox_lay_gradient_calculation_blocksize_67)

        label_68 = QLabel("    reflections")
        label_68.setPalette(palette_scope)
        label_68.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_68)

        hbox_lay_reflections_per_degree_69 =  QHBoxLayout()
        label_reflections_per_degree_69 = QLabel("        reflections_per_degree")
        label_reflections_per_degree_69.setPalette(palette_object)
        label_reflections_per_degree_69.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_69.addWidget(label_reflections_per_degree_69)

        box_reflections_per_degree_69 = QDoubleSpinBox()
        box_reflections_per_degree_69.local_path = "refinement.reflections.reflections_per_degree"
        box_reflections_per_degree_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_69.addWidget(box_reflections_per_degree_69)
        bg_box.addLayout(hbox_lay_reflections_per_degree_69)

        hbox_lay_minimum_sample_size_70 =  QHBoxLayout()
        label_minimum_sample_size_70 = QLabel("        minimum_sample_size")
        label_minimum_sample_size_70.setPalette(palette_object)
        label_minimum_sample_size_70.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_70.addWidget(label_minimum_sample_size_70)

        box_minimum_sample_size_70 = QSpinBox()
        box_minimum_sample_size_70.setValue(1000)
        box_minimum_sample_size_70.local_path = "refinement.reflections.minimum_sample_size"
        box_minimum_sample_size_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_70.addWidget(box_minimum_sample_size_70)
        bg_box.addLayout(hbox_lay_minimum_sample_size_70)

        hbox_lay_maximum_sample_size_71 =  QHBoxLayout()
        label_maximum_sample_size_71 = QLabel("        maximum_sample_size")
        label_maximum_sample_size_71.setPalette(palette_object)
        label_maximum_sample_size_71.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_71.addWidget(label_maximum_sample_size_71)

        box_maximum_sample_size_71 = QSpinBox()
        box_maximum_sample_size_71.local_path = "refinement.reflections.maximum_sample_size"
        box_maximum_sample_size_71.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_71.addWidget(box_maximum_sample_size_71)
        bg_box.addLayout(hbox_lay_maximum_sample_size_71)

        hbox_lay_random_seed_72 =  QHBoxLayout()
        label_random_seed_72 = QLabel("        random_seed")
        label_random_seed_72.setPalette(palette_object)
        label_random_seed_72.setFont(QFont("Monospace", 10))
        hbox_lay_random_seed_72.addWidget(label_random_seed_72)

        box_random_seed_72 = QSpinBox()
        box_random_seed_72.setValue(42)
        box_random_seed_72.local_path = "refinement.reflections.random_seed"
        box_random_seed_72.valueChanged.connect(self.spnbox_changed)
        hbox_lay_random_seed_72.addWidget(box_random_seed_72)
        bg_box.addLayout(hbox_lay_random_seed_72)

        hbox_lay_close_to_spindle_cutoff_73 =  QHBoxLayout()
        label_close_to_spindle_cutoff_73 = QLabel("        close_to_spindle_cutoff")
        label_close_to_spindle_cutoff_73.setPalette(palette_object)
        label_close_to_spindle_cutoff_73.setFont(QFont("Monospace", 10))
        hbox_lay_close_to_spindle_cutoff_73.addWidget(label_close_to_spindle_cutoff_73)

        box_close_to_spindle_cutoff_73 = QDoubleSpinBox()
        box_close_to_spindle_cutoff_73.setValue(0.02)
        box_close_to_spindle_cutoff_73.local_path = "refinement.reflections.close_to_spindle_cutoff"
        box_close_to_spindle_cutoff_73.valueChanged.connect(self.spnbox_changed)
        hbox_lay_close_to_spindle_cutoff_73.addWidget(box_close_to_spindle_cutoff_73)
        bg_box.addLayout(hbox_lay_close_to_spindle_cutoff_73)

        hbox_lay_block_width_74 =  QHBoxLayout()
        label_block_width_74 = QLabel("        block_width")
        label_block_width_74.setPalette(palette_object)
        label_block_width_74.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_74.addWidget(label_block_width_74)

        box_block_width_74 = QDoubleSpinBox()
        box_block_width_74.setValue(1.0)
        box_block_width_74.local_path = "refinement.reflections.block_width"
        box_block_width_74.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_74.addWidget(box_block_width_74)
        bg_box.addLayout(hbox_lay_block_width_74)

        label_75 = QLabel("        weighting_strategy")
        label_75.setPalette(palette_scope)
        label_75.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_75)

        hbox_lay_override_76 =  QHBoxLayout()
        label_override_76 = QLabel("            override")
        label_override_76.setPalette(palette_object)
        label_override_76.setFont(QFont("Monospace", 10))
        hbox_lay_override_76.addWidget(label_override_76)

        box_override_76 = QComboBox()
        box_override_76.local_path = "refinement.reflections.weighting_strategy.override"
        box_override_76.tmp_lst=[]
        box_override_76.tmp_lst.append("statistical")
        box_override_76.tmp_lst.append("stills")
        box_override_76.tmp_lst.append("constant")
        for lst_itm in box_override_76.tmp_lst:
            box_override_76.addItem(lst_itm)
        box_override_76.setCurrentIndex(0)
        box_override_76.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_override_76.addWidget(box_override_76)
        bg_box.addLayout(hbox_lay_override_76)

        hbox_lay_delpsi_constant_77 =  QHBoxLayout()
        label_delpsi_constant_77 = QLabel("            delpsi_constant")
        label_delpsi_constant_77.setPalette(palette_object)
        label_delpsi_constant_77.setFont(QFont("Monospace", 10))
        hbox_lay_delpsi_constant_77.addWidget(label_delpsi_constant_77)

        box_delpsi_constant_77 = QDoubleSpinBox()
        box_delpsi_constant_77.setValue(1000000.0)
        box_delpsi_constant_77.local_path = "refinement.reflections.weighting_strategy.delpsi_constant"
        box_delpsi_constant_77.valueChanged.connect(self.spnbox_changed)
        hbox_lay_delpsi_constant_77.addWidget(box_delpsi_constant_77)
        bg_box.addLayout(hbox_lay_delpsi_constant_77)

        hbox_lay_constants_78_0 =  QHBoxLayout()
        label_constants_78_0 = QLabel("            constants[1]")
        label_constants_78_0.setPalette(palette_object)
        label_constants_78_0.setFont(QFont("Monospace", 10))
        hbox_lay_constants_78_0.addWidget(label_constants_78_0)
        box_constants_78_0 = QDoubleSpinBox()
        box_constants_78_0.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_78_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_78_1 =  QHBoxLayout()
        label_constants_78_1 = QLabel("            constants[2]")
        label_constants_78_1.setPalette(palette_object)
        label_constants_78_1.setFont(QFont("Monospace", 10))
        hbox_lay_constants_78_1.addWidget(label_constants_78_1)
        box_constants_78_1 = QDoubleSpinBox()
        box_constants_78_1.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_78_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_78_2 =  QHBoxLayout()
        label_constants_78_2 = QLabel("            constants[3]")
        label_constants_78_2.setPalette(palette_object)
        label_constants_78_2.setFont(QFont("Monospace", 10))
        hbox_lay_constants_78_2.addWidget(label_constants_78_2)
        box_constants_78_2 = QDoubleSpinBox()
        box_constants_78_2.local_path = "refinement.reflections.weighting_strategy.constants"
        #box_constants_78_2.valueChanged.connect(self.spnbox_changed)
        hbox_lay_constants_78_0.addWidget(box_constants_78_0)
        bg_box.addLayout(hbox_lay_constants_78_0)
        hbox_lay_constants_78_1.addWidget(box_constants_78_1)
        bg_box.addLayout(hbox_lay_constants_78_1)
        hbox_lay_constants_78_2.addWidget(box_constants_78_2)
        bg_box.addLayout(hbox_lay_constants_78_2)

        label_79 = QLabel("        outlier")
        label_79.setPalette(palette_scope)
        label_79.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_79)

        hbox_lay_algorithm_80 =  QHBoxLayout()
        label_algorithm_80 = QLabel("            algorithm")
        label_algorithm_80.setPalette(palette_object)
        label_algorithm_80.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_80.addWidget(label_algorithm_80)

        box_algorithm_80 = QComboBox()
        box_algorithm_80.local_path = "refinement.reflections.outlier.algorithm"
        box_algorithm_80.tmp_lst=[]
        box_algorithm_80.tmp_lst.append("null")
        box_algorithm_80.tmp_lst.append("auto")
        box_algorithm_80.tmp_lst.append("mcd")
        box_algorithm_80.tmp_lst.append("tukey")
        box_algorithm_80.tmp_lst.append("sauter_poon")
        for lst_itm in box_algorithm_80.tmp_lst:
            box_algorithm_80.addItem(lst_itm)
        box_algorithm_80.setCurrentIndex(1)
        box_algorithm_80.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_80.addWidget(box_algorithm_80)
        bg_box.addLayout(hbox_lay_algorithm_80)

        hbox_lay_minimum_number_of_reflections_81 =  QHBoxLayout()
        label_minimum_number_of_reflections_81 = QLabel("            minimum_number_of_reflections")
        label_minimum_number_of_reflections_81.setPalette(palette_object)
        label_minimum_number_of_reflections_81.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_number_of_reflections_81.addWidget(label_minimum_number_of_reflections_81)

        box_minimum_number_of_reflections_81 = QSpinBox()
        box_minimum_number_of_reflections_81.setValue(20)
        box_minimum_number_of_reflections_81.local_path = "refinement.reflections.outlier.minimum_number_of_reflections"
        box_minimum_number_of_reflections_81.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_number_of_reflections_81.addWidget(box_minimum_number_of_reflections_81)
        bg_box.addLayout(hbox_lay_minimum_number_of_reflections_81)

        hbox_lay_separate_experiments_82 =  QHBoxLayout()
        label_separate_experiments_82 = QLabel("            separate_experiments")
        label_separate_experiments_82.setPalette(palette_object)
        label_separate_experiments_82.setFont(QFont("Monospace", 10))
        hbox_lay_separate_experiments_82.addWidget(label_separate_experiments_82)

        box_separate_experiments_82 = QComboBox()
        box_separate_experiments_82.local_path = "refinement.reflections.outlier.separate_experiments"
        box_separate_experiments_82.tmp_lst=[]
        box_separate_experiments_82.tmp_lst.append("True")
        box_separate_experiments_82.tmp_lst.append("False")
        for lst_itm in box_separate_experiments_82.tmp_lst:
            box_separate_experiments_82.addItem(lst_itm)
        box_separate_experiments_82.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_experiments_82.addWidget(box_separate_experiments_82)
        bg_box.addLayout(hbox_lay_separate_experiments_82)

        hbox_lay_separate_panels_83 =  QHBoxLayout()
        label_separate_panels_83 = QLabel("            separate_panels")
        label_separate_panels_83.setPalette(palette_object)
        label_separate_panels_83.setFont(QFont("Monospace", 10))
        hbox_lay_separate_panels_83.addWidget(label_separate_panels_83)

        box_separate_panels_83 = QComboBox()
        box_separate_panels_83.local_path = "refinement.reflections.outlier.separate_panels"
        box_separate_panels_83.tmp_lst=[]
        box_separate_panels_83.tmp_lst.append("True")
        box_separate_panels_83.tmp_lst.append("False")
        for lst_itm in box_separate_panels_83.tmp_lst:
            box_separate_panels_83.addItem(lst_itm)
        box_separate_panels_83.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_panels_83.addWidget(box_separate_panels_83)
        bg_box.addLayout(hbox_lay_separate_panels_83)

        hbox_lay_separate_blocks_84 =  QHBoxLayout()
        label_separate_blocks_84 = QLabel("            separate_blocks")
        label_separate_blocks_84.setPalette(palette_object)
        label_separate_blocks_84.setFont(QFont("Monospace", 10))
        hbox_lay_separate_blocks_84.addWidget(label_separate_blocks_84)

        box_separate_blocks_84 = QComboBox()
        box_separate_blocks_84.local_path = "refinement.reflections.outlier.separate_blocks"
        box_separate_blocks_84.tmp_lst=[]
        box_separate_blocks_84.tmp_lst.append("True")
        box_separate_blocks_84.tmp_lst.append("False")
        for lst_itm in box_separate_blocks_84.tmp_lst:
            box_separate_blocks_84.addItem(lst_itm)
        box_separate_blocks_84.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_blocks_84.addWidget(box_separate_blocks_84)
        bg_box.addLayout(hbox_lay_separate_blocks_84)

        hbox_lay_block_width_85 =  QHBoxLayout()
        label_block_width_85 = QLabel("            block_width")
        label_block_width_85.setPalette(palette_object)
        label_block_width_85.setFont(QFont("Monospace", 10))
        hbox_lay_block_width_85.addWidget(label_block_width_85)

        box_block_width_85 = QDoubleSpinBox()
        box_block_width_85.setValue(18.0)
        box_block_width_85.local_path = "refinement.reflections.outlier.block_width"
        box_block_width_85.valueChanged.connect(self.spnbox_changed)
        hbox_lay_block_width_85.addWidget(box_block_width_85)
        bg_box.addLayout(hbox_lay_block_width_85)

        label_86 = QLabel("            tukey")
        label_86.setPalette(palette_scope)
        label_86.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_86)

        hbox_lay_iqr_multiplier_87 =  QHBoxLayout()
        label_iqr_multiplier_87 = QLabel("                iqr_multiplier")
        label_iqr_multiplier_87.setPalette(palette_object)
        label_iqr_multiplier_87.setFont(QFont("Monospace", 10))
        hbox_lay_iqr_multiplier_87.addWidget(label_iqr_multiplier_87)

        box_iqr_multiplier_87 = QDoubleSpinBox()
        box_iqr_multiplier_87.setValue(1.5)
        box_iqr_multiplier_87.local_path = "refinement.reflections.outlier.tukey.iqr_multiplier"
        box_iqr_multiplier_87.valueChanged.connect(self.spnbox_changed)
        hbox_lay_iqr_multiplier_87.addWidget(box_iqr_multiplier_87)
        bg_box.addLayout(hbox_lay_iqr_multiplier_87)

        label_88 = QLabel("            mcd")
        label_88.setPalette(palette_scope)
        label_88.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_88)

        hbox_lay_alpha_89 =  QHBoxLayout()
        label_alpha_89 = QLabel("                alpha")
        label_alpha_89.setPalette(palette_object)
        label_alpha_89.setFont(QFont("Monospace", 10))
        hbox_lay_alpha_89.addWidget(label_alpha_89)

        box_alpha_89 = QDoubleSpinBox()
        box_alpha_89.setValue(0.5)
        box_alpha_89.local_path = "refinement.reflections.outlier.mcd.alpha"
        box_alpha_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_alpha_89.addWidget(box_alpha_89)
        bg_box.addLayout(hbox_lay_alpha_89)

        hbox_lay_max_n_groups_90 =  QHBoxLayout()
        label_max_n_groups_90 = QLabel("                max_n_groups")
        label_max_n_groups_90.setPalette(palette_object)
        label_max_n_groups_90.setFont(QFont("Monospace", 10))
        hbox_lay_max_n_groups_90.addWidget(label_max_n_groups_90)

        box_max_n_groups_90 = QSpinBox()
        box_max_n_groups_90.setValue(5)
        box_max_n_groups_90.local_path = "refinement.reflections.outlier.mcd.max_n_groups"
        box_max_n_groups_90.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_n_groups_90.addWidget(box_max_n_groups_90)
        bg_box.addLayout(hbox_lay_max_n_groups_90)

        hbox_lay_min_group_size_91 =  QHBoxLayout()
        label_min_group_size_91 = QLabel("                min_group_size")
        label_min_group_size_91.setPalette(palette_object)
        label_min_group_size_91.setFont(QFont("Monospace", 10))
        hbox_lay_min_group_size_91.addWidget(label_min_group_size_91)

        box_min_group_size_91 = QSpinBox()
        box_min_group_size_91.setValue(300)
        box_min_group_size_91.local_path = "refinement.reflections.outlier.mcd.min_group_size"
        box_min_group_size_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_group_size_91.addWidget(box_min_group_size_91)
        bg_box.addLayout(hbox_lay_min_group_size_91)

        hbox_lay_n_trials_92 =  QHBoxLayout()
        label_n_trials_92 = QLabel("                n_trials")
        label_n_trials_92.setPalette(palette_object)
        label_n_trials_92.setFont(QFont("Monospace", 10))
        hbox_lay_n_trials_92.addWidget(label_n_trials_92)

        box_n_trials_92 = QSpinBox()
        box_n_trials_92.setValue(500)
        box_n_trials_92.local_path = "refinement.reflections.outlier.mcd.n_trials"
        box_n_trials_92.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_trials_92.addWidget(box_n_trials_92)
        bg_box.addLayout(hbox_lay_n_trials_92)

        hbox_lay_k1_93 =  QHBoxLayout()
        label_k1_93 = QLabel("                k1")
        label_k1_93.setPalette(palette_object)
        label_k1_93.setFont(QFont("Monospace", 10))
        hbox_lay_k1_93.addWidget(label_k1_93)

        box_k1_93 = QSpinBox()
        box_k1_93.setValue(2)
        box_k1_93.local_path = "refinement.reflections.outlier.mcd.k1"
        box_k1_93.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k1_93.addWidget(box_k1_93)
        bg_box.addLayout(hbox_lay_k1_93)

        hbox_lay_k2_94 =  QHBoxLayout()
        label_k2_94 = QLabel("                k2")
        label_k2_94.setPalette(palette_object)
        label_k2_94.setFont(QFont("Monospace", 10))
        hbox_lay_k2_94.addWidget(label_k2_94)

        box_k2_94 = QSpinBox()
        box_k2_94.setValue(2)
        box_k2_94.local_path = "refinement.reflections.outlier.mcd.k2"
        box_k2_94.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k2_94.addWidget(box_k2_94)
        bg_box.addLayout(hbox_lay_k2_94)

        hbox_lay_k3_95 =  QHBoxLayout()
        label_k3_95 = QLabel("                k3")
        label_k3_95.setPalette(palette_object)
        label_k3_95.setFont(QFont("Monospace", 10))
        hbox_lay_k3_95.addWidget(label_k3_95)

        box_k3_95 = QSpinBox()
        box_k3_95.setValue(100)
        box_k3_95.local_path = "refinement.reflections.outlier.mcd.k3"
        box_k3_95.valueChanged.connect(self.spnbox_changed)
        hbox_lay_k3_95.addWidget(box_k3_95)
        bg_box.addLayout(hbox_lay_k3_95)

        hbox_lay_threshold_probability_96 =  QHBoxLayout()
        label_threshold_probability_96 = QLabel("                threshold_probability")
        label_threshold_probability_96.setPalette(palette_object)
        label_threshold_probability_96.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_probability_96.addWidget(label_threshold_probability_96)

        box_threshold_probability_96 = QDoubleSpinBox()
        box_threshold_probability_96.setValue(0.975)
        box_threshold_probability_96.local_path = "refinement.reflections.outlier.mcd.threshold_probability"
        box_threshold_probability_96.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_probability_96.addWidget(box_threshold_probability_96)
        bg_box.addLayout(hbox_lay_threshold_probability_96)

        label_97 = QLabel("            sauter_poon")
        label_97.setPalette(palette_scope)
        label_97.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_97)

        hbox_lay_px_sz_98_0 =  QHBoxLayout()
        label_px_sz_98_0 = QLabel("                px_sz[1]")
        label_px_sz_98_0.setPalette(palette_object)
        label_px_sz_98_0.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_98_0.addWidget(label_px_sz_98_0)
        box_px_sz_98_0 = QDoubleSpinBox()
        box_px_sz_98_0.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_98_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_98_1 =  QHBoxLayout()
        label_px_sz_98_1 = QLabel("                px_sz[2]")
        label_px_sz_98_1.setPalette(palette_object)
        label_px_sz_98_1.setFont(QFont("Monospace", 10))
        hbox_lay_px_sz_98_1.addWidget(label_px_sz_98_1)
        box_px_sz_98_1 = QDoubleSpinBox()
        box_px_sz_98_1.local_path = "refinement.reflections.outlier.sauter_poon.px_sz"
        #box_px_sz_98_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_px_sz_98_0.addWidget(box_px_sz_98_0)
        bg_box.addLayout(hbox_lay_px_sz_98_0)
        hbox_lay_px_sz_98_1.addWidget(box_px_sz_98_1)
        bg_box.addLayout(hbox_lay_px_sz_98_1)

        hbox_lay_verbose_99 =  QHBoxLayout()
        label_verbose_99 = QLabel("                verbose")
        label_verbose_99.setPalette(palette_object)
        label_verbose_99.setFont(QFont("Monospace", 10))
        hbox_lay_verbose_99.addWidget(label_verbose_99)

        box_verbose_99 = QComboBox()
        box_verbose_99.local_path = "refinement.reflections.outlier.sauter_poon.verbose"
        box_verbose_99.tmp_lst=[]
        box_verbose_99.tmp_lst.append("True")
        box_verbose_99.tmp_lst.append("False")
        for lst_itm in box_verbose_99.tmp_lst:
            box_verbose_99.addItem(lst_itm)
        box_verbose_99.setCurrentIndex(1)
        box_verbose_99.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_verbose_99.addWidget(box_verbose_99)
        bg_box.addLayout(hbox_lay_verbose_99)

        hbox_lay_pdf_100 =  QHBoxLayout()
        label_pdf_100 = QLabel("                pdf")
        label_pdf_100.setPalette(palette_object)
        label_pdf_100.setFont(QFont("Monospace", 10))
        hbox_lay_pdf_100.addWidget(label_pdf_100)

        box_pdf_100 = QLineEdit()
        box_pdf_100.local_path = "refinement.reflections.outlier.sauter_poon.pdf"
        box_pdf_100.textChanged.connect(self.spnbox_changed)
        hbox_lay_pdf_100.addWidget(box_pdf_100)
        bg_box.addLayout(hbox_lay_pdf_100)


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


