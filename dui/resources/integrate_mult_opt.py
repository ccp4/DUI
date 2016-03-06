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

        hbox_lay_phil_3 =  QHBoxLayout()
        label_phil_3 = QLabel("    phil")
        label_phil_3.setPalette(palette_object)
        label_phil_3.setFont(QFont("Monospace"))
        hbox_lay_phil_3.addWidget(label_phil_3)

        box_phil_3 = QLineEdit()
        box_phil_3.local_path = "output.phil"
        box_phil_3.textChanged.connect(self.spnbox_changed)
        hbox_lay_phil_3.addWidget(box_phil_3)
        bg_box.addLayout(hbox_lay_phil_3)

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

        hbox_lay_report_6 =  QHBoxLayout()
        label_report_6 = QLabel("    report")
        label_report_6.setPalette(palette_object)
        label_report_6.setFont(QFont("Monospace"))
        hbox_lay_report_6.addWidget(label_report_6)

        box_report_6 = QLineEdit()
        box_report_6.local_path = "output.report"
        box_report_6.textChanged.connect(self.spnbox_changed)
        hbox_lay_report_6.addWidget(box_report_6)
        bg_box.addLayout(hbox_lay_report_6)

        hbox_lay_scan_range_7_0 =  QHBoxLayout()
        label_scan_range_7_0 = QLabel("scan_range[1]")
        label_scan_range_7_0.setPalette(palette_object)
        label_scan_range_7_0.setFont(QFont("Monospace"))
        hbox_lay_scan_range_7_0.addWidget(label_scan_range_7_0)
        box_scan_range_7_0 = QSpinBox()
        box_scan_range_7_0.local_path = "scan_range"
        #box_scan_range_7_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_7_1 =  QHBoxLayout()
        label_scan_range_7_1 = QLabel("scan_range[2]")
        label_scan_range_7_1.setPalette(palette_object)
        label_scan_range_7_1.setFont(QFont("Monospace"))
        hbox_lay_scan_range_7_1.addWidget(label_scan_range_7_1)
        box_scan_range_7_1 = QSpinBox()
        box_scan_range_7_1.local_path = "scan_range"
        #box_scan_range_7_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_7_0.addWidget(box_scan_range_7_0)
        bg_box.addLayout(hbox_lay_scan_range_7_0)
        hbox_lay_scan_range_7_1.addWidget(box_scan_range_7_1)
        bg_box.addLayout(hbox_lay_scan_range_7_1)

        label_8 = QLabel("sampling")
        label_8.setPalette(palette_scope)
        label_8.setFont(QFont("Monospace"))
        bg_box.addWidget(label_8)

        hbox_lay_reflections_per_degree_9 =  QHBoxLayout()
        label_reflections_per_degree_9 = QLabel("    reflections_per_degree")
        label_reflections_per_degree_9.setPalette(palette_object)
        label_reflections_per_degree_9.setFont(QFont("Monospace"))
        hbox_lay_reflections_per_degree_9.addWidget(label_reflections_per_degree_9)

        box_reflections_per_degree_9 = QDoubleSpinBox()
        box_reflections_per_degree_9.setValue(50.0)
        box_reflections_per_degree_9.local_path = "sampling.reflections_per_degree"
        box_reflections_per_degree_9.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_9.addWidget(box_reflections_per_degree_9)
        bg_box.addLayout(hbox_lay_reflections_per_degree_9)

        hbox_lay_minimum_sample_size_10 =  QHBoxLayout()
        label_minimum_sample_size_10 = QLabel("    minimum_sample_size")
        label_minimum_sample_size_10.setPalette(palette_object)
        label_minimum_sample_size_10.setFont(QFont("Monospace"))
        hbox_lay_minimum_sample_size_10.addWidget(label_minimum_sample_size_10)

        box_minimum_sample_size_10 = QSpinBox()
        box_minimum_sample_size_10.setValue(1000)
        box_minimum_sample_size_10.local_path = "sampling.minimum_sample_size"
        box_minimum_sample_size_10.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_10.addWidget(box_minimum_sample_size_10)
        bg_box.addLayout(hbox_lay_minimum_sample_size_10)

        hbox_lay_maximum_sample_size_11 =  QHBoxLayout()
        label_maximum_sample_size_11 = QLabel("    maximum_sample_size")
        label_maximum_sample_size_11.setPalette(palette_object)
        label_maximum_sample_size_11.setFont(QFont("Monospace"))
        hbox_lay_maximum_sample_size_11.addWidget(label_maximum_sample_size_11)

        box_maximum_sample_size_11 = QSpinBox()
        box_maximum_sample_size_11.local_path = "sampling.maximum_sample_size"
        box_maximum_sample_size_11.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_11.addWidget(box_maximum_sample_size_11)
        bg_box.addLayout(hbox_lay_maximum_sample_size_11)

        hbox_lay_integrate_all_reflections_12 =  QHBoxLayout()
        label_integrate_all_reflections_12 = QLabel("    integrate_all_reflections")
        label_integrate_all_reflections_12.setPalette(palette_object)
        label_integrate_all_reflections_12.setFont(QFont("Monospace"))
        hbox_lay_integrate_all_reflections_12.addWidget(label_integrate_all_reflections_12)

        box_integrate_all_reflections_12 = QComboBox()
        box_integrate_all_reflections_12.local_path = "sampling.integrate_all_reflections"
        box_integrate_all_reflections_12.tmp_lst=[]
        box_integrate_all_reflections_12.tmp_lst.append("True")
        box_integrate_all_reflections_12.tmp_lst.append("False")
        for lst_itm in box_integrate_all_reflections_12.tmp_lst:
            box_integrate_all_reflections_12.addItem(lst_itm)
        box_integrate_all_reflections_12.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_integrate_all_reflections_12.addWidget(box_integrate_all_reflections_12)
        bg_box.addLayout(hbox_lay_integrate_all_reflections_12)

        hbox_lay_verbosity_13 =  QHBoxLayout()
        label_verbosity_13 = QLabel("verbosity")
        label_verbosity_13.setPalette(palette_object)
        label_verbosity_13.setFont(QFont("Monospace"))
        hbox_lay_verbosity_13.addWidget(label_verbosity_13)

        box_verbosity_13 = QSpinBox()
        box_verbosity_13.setValue(1)
        box_verbosity_13.local_path = "verbosity"
        box_verbosity_13.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_13.addWidget(box_verbosity_13)
        bg_box.addLayout(hbox_lay_verbosity_13)

        label_14 = QLabel("integration")
        label_14.setPalette(palette_scope)
        label_14.setFont(QFont("Monospace"))
        bg_box.addWidget(label_14)

        label_15 = QLabel("    mp")
        label_15.setPalette(palette_scope)
        label_15.setFont(QFont("Monospace"))
        bg_box.addWidget(label_15)

        hbox_lay_method_16 =  QHBoxLayout()
        label_method_16 = QLabel("        method")
        label_method_16.setPalette(palette_object)
        label_method_16.setFont(QFont("Monospace"))
        hbox_lay_method_16.addWidget(label_method_16)

        box_method_16 = QComboBox()
        box_method_16.local_path = "integration.mp.method"
        box_method_16.tmp_lst=[]
        box_method_16.tmp_lst.append("multiprocessing")
        box_method_16.tmp_lst.append("sge")
        box_method_16.tmp_lst.append("lsf")
        box_method_16.tmp_lst.append("pbs")
        for lst_itm in box_method_16.tmp_lst:
            box_method_16.addItem(lst_itm)
        box_method_16.setCurrentIndex(0)
        box_method_16.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_16.addWidget(box_method_16)
        bg_box.addLayout(hbox_lay_method_16)

        hbox_lay_nproc_17 =  QHBoxLayout()
        label_nproc_17 = QLabel("        nproc")
        label_nproc_17.setPalette(palette_object)
        label_nproc_17.setFont(QFont("Monospace"))
        hbox_lay_nproc_17.addWidget(label_nproc_17)

        box_nproc_17 = QSpinBox()
        box_nproc_17.setValue(1)
        box_nproc_17.local_path = "integration.mp.nproc"
        box_nproc_17.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_17.addWidget(box_nproc_17)
        bg_box.addLayout(hbox_lay_nproc_17)

        hbox_lay_nthreads_18 =  QHBoxLayout()
        label_nthreads_18 = QLabel("        nthreads")
        label_nthreads_18.setPalette(palette_object)
        label_nthreads_18.setFont(QFont("Monospace"))
        hbox_lay_nthreads_18.addWidget(label_nthreads_18)

        box_nthreads_18 = QSpinBox()
        box_nthreads_18.setValue(1)
        box_nthreads_18.local_path = "integration.mp.nthreads"
        box_nthreads_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nthreads_18.addWidget(box_nthreads_18)
        bg_box.addLayout(hbox_lay_nthreads_18)

        label_19 = QLabel("    lookup")
        label_19.setPalette(palette_scope)
        label_19.setFont(QFont("Monospace"))
        bg_box.addWidget(label_19)

        hbox_lay_mask_20 =  QHBoxLayout()
        label_mask_20 = QLabel("        mask")
        label_mask_20.setPalette(palette_object)
        label_mask_20.setFont(QFont("Monospace"))
        hbox_lay_mask_20.addWidget(label_mask_20)

        box_mask_20 = QLineEdit()
        box_mask_20.local_path = "integration.lookup.mask"
        box_mask_20.textChanged.connect(self.spnbox_changed)
        hbox_lay_mask_20.addWidget(box_mask_20)
        bg_box.addLayout(hbox_lay_mask_20)

        label_21 = QLabel("    block")
        label_21.setPalette(palette_scope)
        label_21.setFont(QFont("Monospace"))
        bg_box.addWidget(label_21)

        hbox_lay_size_22 =  QHBoxLayout()
        label_size_22 = QLabel("        size")
        label_size_22.setPalette(palette_object)
        label_size_22.setFont(QFont("Monospace"))
        hbox_lay_size_22.addWidget(label_size_22)

        box_size_22 = QDoubleSpinBox()
        box_size_22.local_path = "integration.block.size"
        box_size_22.valueChanged.connect(self.spnbox_changed)
        hbox_lay_size_22.addWidget(box_size_22)
        bg_box.addLayout(hbox_lay_size_22)

        hbox_lay_units_23 =  QHBoxLayout()
        label_units_23 = QLabel("        units")
        label_units_23.setPalette(palette_object)
        label_units_23.setFont(QFont("Monospace"))
        hbox_lay_units_23.addWidget(label_units_23)

        box_units_23 = QComboBox()
        box_units_23.local_path = "integration.block.units"
        box_units_23.tmp_lst=[]
        box_units_23.tmp_lst.append("degrees")
        box_units_23.tmp_lst.append("radians")
        box_units_23.tmp_lst.append("frames")
        for lst_itm in box_units_23.tmp_lst:
            box_units_23.addItem(lst_itm)
        box_units_23.setCurrentIndex(0)
        box_units_23.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_units_23.addWidget(box_units_23)
        bg_box.addLayout(hbox_lay_units_23)

        hbox_lay_threshold_24 =  QHBoxLayout()
        label_threshold_24 = QLabel("        threshold")
        label_threshold_24.setPalette(palette_object)
        label_threshold_24.setFont(QFont("Monospace"))
        hbox_lay_threshold_24.addWidget(label_threshold_24)

        box_threshold_24 = QDoubleSpinBox()
        box_threshold_24.setValue(0.99)
        box_threshold_24.local_path = "integration.block.threshold"
        box_threshold_24.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_24.addWidget(box_threshold_24)
        bg_box.addLayout(hbox_lay_threshold_24)

        hbox_lay_force_25 =  QHBoxLayout()
        label_force_25 = QLabel("        force")
        label_force_25.setPalette(palette_object)
        label_force_25.setFont(QFont("Monospace"))
        hbox_lay_force_25.addWidget(label_force_25)

        box_force_25 = QComboBox()
        box_force_25.local_path = "integration.block.force"
        box_force_25.tmp_lst=[]
        box_force_25.tmp_lst.append("True")
        box_force_25.tmp_lst.append("False")
        for lst_itm in box_force_25.tmp_lst:
            box_force_25.addItem(lst_itm)
        box_force_25.setCurrentIndex(1)
        box_force_25.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_25.addWidget(box_force_25)
        bg_box.addLayout(hbox_lay_force_25)

        hbox_lay_max_memory_usage_26 =  QHBoxLayout()
        label_max_memory_usage_26 = QLabel("        max_memory_usage")
        label_max_memory_usage_26.setPalette(palette_object)
        label_max_memory_usage_26.setFont(QFont("Monospace"))
        hbox_lay_max_memory_usage_26.addWidget(label_max_memory_usage_26)

        box_max_memory_usage_26 = QDoubleSpinBox()
        box_max_memory_usage_26.setValue(0.75)
        box_max_memory_usage_26.local_path = "integration.block.max_memory_usage"
        box_max_memory_usage_26.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_memory_usage_26.addWidget(box_max_memory_usage_26)
        bg_box.addLayout(hbox_lay_max_memory_usage_26)

        label_27 = QLabel("    debug")
        label_27.setPalette(palette_scope)
        label_27.setFont(QFont("Monospace"))
        bg_box.addWidget(label_27)

        label_28 = QLabel("        reference")
        label_28.setPalette(palette_scope)
        label_28.setFont(QFont("Monospace"))
        bg_box.addWidget(label_28)

        hbox_lay_output_29 =  QHBoxLayout()
        label_output_29 = QLabel("            output")
        label_output_29.setPalette(palette_object)
        label_output_29.setFont(QFont("Monospace"))
        hbox_lay_output_29.addWidget(label_output_29)

        box_output_29 = QComboBox()
        box_output_29.local_path = "integration.debug.reference.output"
        box_output_29.tmp_lst=[]
        box_output_29.tmp_lst.append("True")
        box_output_29.tmp_lst.append("False")
        for lst_itm in box_output_29.tmp_lst:
            box_output_29.addItem(lst_itm)
        box_output_29.setCurrentIndex(1)
        box_output_29.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_output_29.addWidget(box_output_29)
        bg_box.addLayout(hbox_lay_output_29)

        hbox_lay_during_30 =  QHBoxLayout()
        label_during_30 = QLabel("        during")
        label_during_30.setPalette(palette_object)
        label_during_30.setFont(QFont("Monospace"))
        hbox_lay_during_30.addWidget(label_during_30)

        box_during_30 = QComboBox()
        box_during_30.local_path = "integration.debug.during"
        box_during_30.tmp_lst=[]
        box_during_30.tmp_lst.append("modelling")
        box_during_30.tmp_lst.append("integration")
        for lst_itm in box_during_30.tmp_lst:
            box_during_30.addItem(lst_itm)
        box_during_30.setCurrentIndex(1)
        box_during_30.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_during_30.addWidget(box_during_30)
        bg_box.addLayout(hbox_lay_during_30)

        hbox_lay_output_31 =  QHBoxLayout()
        label_output_31 = QLabel("        output")
        label_output_31.setPalette(palette_object)
        label_output_31.setFont(QFont("Monospace"))
        hbox_lay_output_31.addWidget(label_output_31)

        box_output_31 = QComboBox()
        box_output_31.local_path = "integration.debug.output"
        box_output_31.tmp_lst=[]
        box_output_31.tmp_lst.append("True")
        box_output_31.tmp_lst.append("False")
        for lst_itm in box_output_31.tmp_lst:
            box_output_31.addItem(lst_itm)
        box_output_31.setCurrentIndex(1)
        box_output_31.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_output_31.addWidget(box_output_31)
        bg_box.addLayout(hbox_lay_output_31)

        hbox_lay_separate_files_32 =  QHBoxLayout()
        label_separate_files_32 = QLabel("        separate_files")
        label_separate_files_32.setPalette(palette_object)
        label_separate_files_32.setFont(QFont("Monospace"))
        hbox_lay_separate_files_32.addWidget(label_separate_files_32)

        box_separate_files_32 = QComboBox()
        box_separate_files_32.local_path = "integration.debug.separate_files"
        box_separate_files_32.tmp_lst=[]
        box_separate_files_32.tmp_lst.append("True")
        box_separate_files_32.tmp_lst.append("False")
        for lst_itm in box_separate_files_32.tmp_lst:
            box_separate_files_32.addItem(lst_itm)
        box_separate_files_32.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_files_32.addWidget(box_separate_files_32)
        bg_box.addLayout(hbox_lay_separate_files_32)


        hbox_lay_split_experiments_34 =  QHBoxLayout()
        label_split_experiments_34 = QLabel("        split_experiments")
        label_split_experiments_34.setPalette(palette_object)
        label_split_experiments_34.setFont(QFont("Monospace"))
        hbox_lay_split_experiments_34.addWidget(label_split_experiments_34)

        box_split_experiments_34 = QComboBox()
        box_split_experiments_34.local_path = "integration.debug.split_experiments"
        box_split_experiments_34.tmp_lst=[]
        box_split_experiments_34.tmp_lst.append("True")
        box_split_experiments_34.tmp_lst.append("False")
        for lst_itm in box_split_experiments_34.tmp_lst:
            box_split_experiments_34.addItem(lst_itm)
        box_split_experiments_34.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_split_experiments_34.addWidget(box_split_experiments_34)
        bg_box.addLayout(hbox_lay_split_experiments_34)

        hbox_lay_integrator_35 =  QHBoxLayout()
        label_integrator_35 = QLabel("    integrator")
        label_integrator_35.setPalette(palette_object)
        label_integrator_35.setFont(QFont("Monospace"))
        hbox_lay_integrator_35.addWidget(label_integrator_35)

        box_integrator_35 = QComboBox()
        box_integrator_35.local_path = "integration.integrator"
        box_integrator_35.tmp_lst=[]
        box_integrator_35.tmp_lst.append("auto")
        box_integrator_35.tmp_lst.append("3d")
        box_integrator_35.tmp_lst.append("flat3d")
        box_integrator_35.tmp_lst.append("2d")
        box_integrator_35.tmp_lst.append("single2d")
        box_integrator_35.tmp_lst.append("stills")
        for lst_itm in box_integrator_35.tmp_lst:
            box_integrator_35.addItem(lst_itm)
        box_integrator_35.setCurrentIndex(0)
        box_integrator_35.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_integrator_35.addWidget(box_integrator_35)
        bg_box.addLayout(hbox_lay_integrator_35)

        label_36 = QLabel("    profile")
        label_36.setPalette(palette_scope)
        label_36.setFont(QFont("Monospace"))
        bg_box.addWidget(label_36)

        hbox_lay_fitting_37 =  QHBoxLayout()
        label_fitting_37 = QLabel("        fitting")
        label_fitting_37.setPalette(palette_object)
        label_fitting_37.setFont(QFont("Monospace"))
        hbox_lay_fitting_37.addWidget(label_fitting_37)

        box_fitting_37 = QComboBox()
        box_fitting_37.local_path = "integration.profile.fitting"
        box_fitting_37.tmp_lst=[]
        box_fitting_37.tmp_lst.append("True")
        box_fitting_37.tmp_lst.append("False")
        for lst_itm in box_fitting_37.tmp_lst:
            box_fitting_37.addItem(lst_itm)
        box_fitting_37.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fitting_37.addWidget(box_fitting_37)
        bg_box.addLayout(hbox_lay_fitting_37)

        label_38 = QLabel("        validation")
        label_38.setPalette(palette_scope)
        label_38.setFont(QFont("Monospace"))
        bg_box.addWidget(label_38)

        hbox_lay_number_of_partitions_39 =  QHBoxLayout()
        label_number_of_partitions_39 = QLabel("            number_of_partitions")
        label_number_of_partitions_39.setPalette(palette_object)
        label_number_of_partitions_39.setFont(QFont("Monospace"))
        hbox_lay_number_of_partitions_39.addWidget(label_number_of_partitions_39)

        box_number_of_partitions_39 = QSpinBox()
        box_number_of_partitions_39.setValue(1)
        box_number_of_partitions_39.local_path = "integration.profile.validation.number_of_partitions"
        box_number_of_partitions_39.valueChanged.connect(self.spnbox_changed)
        hbox_lay_number_of_partitions_39.addWidget(box_number_of_partitions_39)
        bg_box.addLayout(hbox_lay_number_of_partitions_39)

        hbox_lay_min_partition_size_40 =  QHBoxLayout()
        label_min_partition_size_40 = QLabel("            min_partition_size")
        label_min_partition_size_40.setPalette(palette_object)
        label_min_partition_size_40.setFont(QFont("Monospace"))
        hbox_lay_min_partition_size_40.addWidget(label_min_partition_size_40)

        box_min_partition_size_40 = QSpinBox()
        box_min_partition_size_40.setValue(100)
        box_min_partition_size_40.local_path = "integration.profile.validation.min_partition_size"
        box_min_partition_size_40.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_partition_size_40.addWidget(box_min_partition_size_40)
        bg_box.addLayout(hbox_lay_min_partition_size_40)

        label_41 = QLabel("    filter")
        label_41.setPalette(palette_scope)
        label_41.setFont(QFont("Monospace"))
        bg_box.addWidget(label_41)

        hbox_lay_min_zeta_42 =  QHBoxLayout()
        label_min_zeta_42 = QLabel("        min_zeta")
        label_min_zeta_42.setPalette(palette_object)
        label_min_zeta_42.setFont(QFont("Monospace"))
        hbox_lay_min_zeta_42.addWidget(label_min_zeta_42)

        box_min_zeta_42 = QDoubleSpinBox()
        box_min_zeta_42.setValue(0.05)
        box_min_zeta_42.local_path = "integration.filter.min_zeta"
        box_min_zeta_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_zeta_42.addWidget(box_min_zeta_42)
        bg_box.addLayout(hbox_lay_min_zeta_42)

        hbox_lay_max_shoebox_overlap_43 =  QHBoxLayout()
        label_max_shoebox_overlap_43 = QLabel("        max_shoebox_overlap")
        label_max_shoebox_overlap_43.setPalette(palette_object)
        label_max_shoebox_overlap_43.setFont(QFont("Monospace"))
        hbox_lay_max_shoebox_overlap_43.addWidget(label_max_shoebox_overlap_43)

        box_max_shoebox_overlap_43 = QDoubleSpinBox()
        box_max_shoebox_overlap_43.setValue(1.0)
        box_max_shoebox_overlap_43.local_path = "integration.filter.max_shoebox_overlap"
        box_max_shoebox_overlap_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_shoebox_overlap_43.addWidget(box_max_shoebox_overlap_43)
        bg_box.addLayout(hbox_lay_max_shoebox_overlap_43)

        label_44 = QLabel("        powder")
        label_44.setPalette(palette_scope)
        label_44.setFont(QFont("Monospace"))
        bg_box.addWidget(label_44)

        label_45 = QLabel("            water_ice")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace"))
        bg_box.addWidget(label_45)



        hbox_lay_d_min_48 =  QHBoxLayout()
        label_d_min_48 = QLabel("                d_min")
        label_d_min_48.setPalette(palette_object)
        label_d_min_48.setFont(QFont("Monospace"))
        hbox_lay_d_min_48.addWidget(label_d_min_48)

        box_d_min_48 = QDoubleSpinBox()
        box_d_min_48.setValue(1.0)
        box_d_min_48.local_path = "integration.filter.powder.water_ice.d_min"
        box_d_min_48.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_48.addWidget(box_d_min_48)
        bg_box.addLayout(hbox_lay_d_min_48)

        hbox_lay_width_49 =  QHBoxLayout()
        label_width_49 = QLabel("                width")
        label_width_49.setPalette(palette_object)
        label_width_49.setFont(QFont("Monospace"))
        hbox_lay_width_49.addWidget(label_width_49)

        box_width_49 = QDoubleSpinBox()
        box_width_49.setValue(0.06)
        box_width_49.local_path = "integration.filter.powder.water_ice.width"
        box_width_49.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_49.addWidget(box_width_49)
        bg_box.addLayout(hbox_lay_width_49)

        hbox_lay_apply_50 =  QHBoxLayout()
        label_apply_50 = QLabel("            apply")
        label_apply_50.setPalette(palette_object)
        label_apply_50.setFont(QFont("Monospace"))
        hbox_lay_apply_50.addWidget(label_apply_50)

        box_apply_50 = QComboBox()
        box_apply_50.local_path = "integration.filter.powder.apply"
        box_apply_50.tmp_lst=[]
        box_apply_50.tmp_lst.append("none")
        box_apply_50.tmp_lst.append("water_ice")
        for lst_itm in box_apply_50.tmp_lst:
            box_apply_50.addItem(lst_itm)
        box_apply_50.setCurrentIndex(0)
        box_apply_50.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_50.addWidget(box_apply_50)
        bg_box.addLayout(hbox_lay_apply_50)

        label_51 = QLabel("    background")
        label_51.setPalette(palette_scope)
        label_51.setFont(QFont("Monospace"))
        bg_box.addWidget(label_51)

        hbox_lay_algorithm_52 =  QHBoxLayout()
        label_algorithm_52 = QLabel("        algorithm")
        label_algorithm_52.setPalette(palette_object)
        label_algorithm_52.setFont(QFont("Monospace"))
        hbox_lay_algorithm_52.addWidget(label_algorithm_52)

        box_algorithm_52 = QComboBox()
        box_algorithm_52.local_path = "integration.background.algorithm"
        box_algorithm_52.tmp_lst=[]
        box_algorithm_52.tmp_lst.append("simple")
        box_algorithm_52.tmp_lst.append("null")
        box_algorithm_52.tmp_lst.append("glm")
        box_algorithm_52.tmp_lst.append("const_d")
        for lst_itm in box_algorithm_52.tmp_lst:
            box_algorithm_52.addItem(lst_itm)
        box_algorithm_52.setCurrentIndex(2)
        box_algorithm_52.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_52.addWidget(box_algorithm_52)
        bg_box.addLayout(hbox_lay_algorithm_52)

        label_53 = QLabel("        simple")
        label_53.setPalette(palette_scope)
        label_53.setFont(QFont("Monospace"))
        bg_box.addWidget(label_53)

        label_54 = QLabel("            outlier")
        label_54.setPalette(palette_scope)
        label_54.setFont(QFont("Monospace"))
        bg_box.addWidget(label_54)

        hbox_lay_algorithm_55 =  QHBoxLayout()
        label_algorithm_55 = QLabel("                algorithm")
        label_algorithm_55.setPalette(palette_object)
        label_algorithm_55.setFont(QFont("Monospace"))
        hbox_lay_algorithm_55.addWidget(label_algorithm_55)

        box_algorithm_55 = QComboBox()
        box_algorithm_55.local_path = "integration.background.simple.outlier.algorithm"
        box_algorithm_55.tmp_lst=[]
        box_algorithm_55.tmp_lst.append("null")
        box_algorithm_55.tmp_lst.append("nsigma")
        box_algorithm_55.tmp_lst.append("truncated")
        box_algorithm_55.tmp_lst.append("normal")
        box_algorithm_55.tmp_lst.append("mosflm")
        box_algorithm_55.tmp_lst.append("tukey")
        for lst_itm in box_algorithm_55.tmp_lst:
            box_algorithm_55.addItem(lst_itm)
        box_algorithm_55.setCurrentIndex(1)
        box_algorithm_55.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_55.addWidget(box_algorithm_55)
        bg_box.addLayout(hbox_lay_algorithm_55)

        label_56 = QLabel("                nsigma")
        label_56.setPalette(palette_scope)
        label_56.setFont(QFont("Monospace"))
        bg_box.addWidget(label_56)

        hbox_lay_lower_57 =  QHBoxLayout()
        label_lower_57 = QLabel("                    lower")
        label_lower_57.setPalette(palette_object)
        label_lower_57.setFont(QFont("Monospace"))
        hbox_lay_lower_57.addWidget(label_lower_57)

        box_lower_57 = QDoubleSpinBox()
        box_lower_57.setValue(3.0)
        box_lower_57.local_path = "integration.background.simple.outlier.nsigma.lower"
        box_lower_57.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_57.addWidget(box_lower_57)
        bg_box.addLayout(hbox_lay_lower_57)

        hbox_lay_upper_58 =  QHBoxLayout()
        label_upper_58 = QLabel("                    upper")
        label_upper_58.setPalette(palette_object)
        label_upper_58.setFont(QFont("Monospace"))
        hbox_lay_upper_58.addWidget(label_upper_58)

        box_upper_58 = QDoubleSpinBox()
        box_upper_58.setValue(3.0)
        box_upper_58.local_path = "integration.background.simple.outlier.nsigma.upper"
        box_upper_58.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_58.addWidget(box_upper_58)
        bg_box.addLayout(hbox_lay_upper_58)

        label_59 = QLabel("                truncated")
        label_59.setPalette(palette_scope)
        label_59.setFont(QFont("Monospace"))
        bg_box.addWidget(label_59)

        hbox_lay_lower_60 =  QHBoxLayout()
        label_lower_60 = QLabel("                    lower")
        label_lower_60.setPalette(palette_object)
        label_lower_60.setFont(QFont("Monospace"))
        hbox_lay_lower_60.addWidget(label_lower_60)

        box_lower_60 = QDoubleSpinBox()
        box_lower_60.setValue(0.01)
        box_lower_60.local_path = "integration.background.simple.outlier.truncated.lower"
        box_lower_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_60.addWidget(box_lower_60)
        bg_box.addLayout(hbox_lay_lower_60)

        hbox_lay_upper_61 =  QHBoxLayout()
        label_upper_61 = QLabel("                    upper")
        label_upper_61.setPalette(palette_object)
        label_upper_61.setFont(QFont("Monospace"))
        hbox_lay_upper_61.addWidget(label_upper_61)

        box_upper_61 = QDoubleSpinBox()
        box_upper_61.setValue(0.01)
        box_upper_61.local_path = "integration.background.simple.outlier.truncated.upper"
        box_upper_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_61.addWidget(box_upper_61)
        bg_box.addLayout(hbox_lay_upper_61)

        label_62 = QLabel("                normal")
        label_62.setPalette(palette_scope)
        label_62.setFont(QFont("Monospace"))
        bg_box.addWidget(label_62)

        hbox_lay_min_pixels_63 =  QHBoxLayout()
        label_min_pixels_63 = QLabel("                    min_pixels")
        label_min_pixels_63.setPalette(palette_object)
        label_min_pixels_63.setFont(QFont("Monospace"))
        hbox_lay_min_pixels_63.addWidget(label_min_pixels_63)

        box_min_pixels_63 = QSpinBox()
        box_min_pixels_63.setValue(10)
        box_min_pixels_63.local_path = "integration.background.simple.outlier.normal.min_pixels"
        box_min_pixels_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_pixels_63.addWidget(box_min_pixels_63)
        bg_box.addLayout(hbox_lay_min_pixels_63)

        label_64 = QLabel("                mosflm")
        label_64.setPalette(palette_scope)
        label_64.setFont(QFont("Monospace"))
        bg_box.addWidget(label_64)

        hbox_lay_fraction_65 =  QHBoxLayout()
        label_fraction_65 = QLabel("                    fraction")
        label_fraction_65.setPalette(palette_object)
        label_fraction_65.setFont(QFont("Monospace"))
        hbox_lay_fraction_65.addWidget(label_fraction_65)

        box_fraction_65 = QDoubleSpinBox()
        box_fraction_65.setValue(1.0)
        box_fraction_65.local_path = "integration.background.simple.outlier.mosflm.fraction"
        box_fraction_65.valueChanged.connect(self.spnbox_changed)
        hbox_lay_fraction_65.addWidget(box_fraction_65)
        bg_box.addLayout(hbox_lay_fraction_65)

        hbox_lay_n_sigma_66 =  QHBoxLayout()
        label_n_sigma_66 = QLabel("                    n_sigma")
        label_n_sigma_66.setPalette(palette_object)
        label_n_sigma_66.setFont(QFont("Monospace"))
        hbox_lay_n_sigma_66.addWidget(label_n_sigma_66)

        box_n_sigma_66 = QDoubleSpinBox()
        box_n_sigma_66.setValue(4.0)
        box_n_sigma_66.local_path = "integration.background.simple.outlier.mosflm.n_sigma"
        box_n_sigma_66.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_sigma_66.addWidget(box_n_sigma_66)
        bg_box.addLayout(hbox_lay_n_sigma_66)

        label_67 = QLabel("                tukey")
        label_67.setPalette(palette_scope)
        label_67.setFont(QFont("Monospace"))
        bg_box.addWidget(label_67)

        hbox_lay_lower_68 =  QHBoxLayout()
        label_lower_68 = QLabel("                    lower")
        label_lower_68.setPalette(palette_object)
        label_lower_68.setFont(QFont("Monospace"))
        hbox_lay_lower_68.addWidget(label_lower_68)

        box_lower_68 = QDoubleSpinBox()
        box_lower_68.setValue(1.5)
        box_lower_68.local_path = "integration.background.simple.outlier.tukey.lower"
        box_lower_68.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_68.addWidget(box_lower_68)
        bg_box.addLayout(hbox_lay_lower_68)

        hbox_lay_upper_69 =  QHBoxLayout()
        label_upper_69 = QLabel("                    upper")
        label_upper_69.setPalette(palette_object)
        label_upper_69.setFont(QFont("Monospace"))
        hbox_lay_upper_69.addWidget(label_upper_69)

        box_upper_69 = QDoubleSpinBox()
        box_upper_69.setValue(1.5)
        box_upper_69.local_path = "integration.background.simple.outlier.tukey.upper"
        box_upper_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_69.addWidget(box_upper_69)
        bg_box.addLayout(hbox_lay_upper_69)

        label_70 = QLabel("            model")
        label_70.setPalette(palette_scope)
        label_70.setFont(QFont("Monospace"))
        bg_box.addWidget(label_70)

        hbox_lay_algorithm_71 =  QHBoxLayout()
        label_algorithm_71 = QLabel("                algorithm")
        label_algorithm_71.setPalette(palette_object)
        label_algorithm_71.setFont(QFont("Monospace"))
        hbox_lay_algorithm_71.addWidget(label_algorithm_71)

        box_algorithm_71 = QComboBox()
        box_algorithm_71.local_path = "integration.background.simple.model.algorithm"
        box_algorithm_71.tmp_lst=[]
        box_algorithm_71.tmp_lst.append("constant2d")
        box_algorithm_71.tmp_lst.append("constant3d")
        box_algorithm_71.tmp_lst.append("linear2d")
        box_algorithm_71.tmp_lst.append("linear3d")
        for lst_itm in box_algorithm_71.tmp_lst:
            box_algorithm_71.addItem(lst_itm)
        box_algorithm_71.setCurrentIndex(1)
        box_algorithm_71.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_71.addWidget(box_algorithm_71)
        bg_box.addLayout(hbox_lay_algorithm_71)

        label_72 = QLabel("        glm")
        label_72.setPalette(palette_scope)
        label_72.setFont(QFont("Monospace"))
        bg_box.addWidget(label_72)

        label_73 = QLabel("            robust")
        label_73.setPalette(palette_scope)
        label_73.setFont(QFont("Monospace"))
        bg_box.addWidget(label_73)

        hbox_lay_tuning_constant_74 =  QHBoxLayout()
        label_tuning_constant_74 = QLabel("                tuning_constant")
        label_tuning_constant_74.setPalette(palette_object)
        label_tuning_constant_74.setFont(QFont("Monospace"))
        hbox_lay_tuning_constant_74.addWidget(label_tuning_constant_74)

        box_tuning_constant_74 = QDoubleSpinBox()
        box_tuning_constant_74.setValue(1.345)
        box_tuning_constant_74.local_path = "integration.background.glm.robust.tuning_constant"
        box_tuning_constant_74.valueChanged.connect(self.spnbox_changed)
        hbox_lay_tuning_constant_74.addWidget(box_tuning_constant_74)
        bg_box.addLayout(hbox_lay_tuning_constant_74)

        label_75 = QLabel("            model")
        label_75.setPalette(palette_scope)
        label_75.setFont(QFont("Monospace"))
        bg_box.addWidget(label_75)

        hbox_lay_algorithm_76 =  QHBoxLayout()
        label_algorithm_76 = QLabel("                algorithm")
        label_algorithm_76.setPalette(palette_object)
        label_algorithm_76.setFont(QFont("Monospace"))
        hbox_lay_algorithm_76.addWidget(label_algorithm_76)

        box_algorithm_76 = QComboBox()
        box_algorithm_76.local_path = "integration.background.glm.model.algorithm"
        box_algorithm_76.tmp_lst=[]
        box_algorithm_76.tmp_lst.append("constant2d")
        box_algorithm_76.tmp_lst.append("constant3d")
        box_algorithm_76.tmp_lst.append("loglinear2d")
        box_algorithm_76.tmp_lst.append("loglinear3d")
        for lst_itm in box_algorithm_76.tmp_lst:
            box_algorithm_76.addItem(lst_itm)
        box_algorithm_76.setCurrentIndex(1)
        box_algorithm_76.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_76.addWidget(box_algorithm_76)
        bg_box.addLayout(hbox_lay_algorithm_76)

        label_77 = QLabel("        const_d")
        label_77.setPalette(palette_scope)
        label_77.setFont(QFont("Monospace"))
        bg_box.addWidget(label_77)

        label_78 = QLabel("    centroid")
        label_78.setPalette(palette_scope)
        label_78.setFont(QFont("Monospace"))
        bg_box.addWidget(label_78)

        hbox_lay_algorithm_79 =  QHBoxLayout()
        label_algorithm_79 = QLabel("        algorithm")
        label_algorithm_79.setPalette(palette_object)
        label_algorithm_79.setFont(QFont("Monospace"))
        hbox_lay_algorithm_79.addWidget(label_algorithm_79)

        box_algorithm_79 = QComboBox()
        box_algorithm_79.local_path = "integration.centroid.algorithm"
        box_algorithm_79.tmp_lst=[]
        box_algorithm_79.tmp_lst.append("simple")
        for lst_itm in box_algorithm_79.tmp_lst:
            box_algorithm_79.addItem(lst_itm)
        box_algorithm_79.setCurrentIndex(0)
        box_algorithm_79.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_79.addWidget(box_algorithm_79)
        bg_box.addLayout(hbox_lay_algorithm_79)

        label_80 = QLabel("profile")
        label_80.setPalette(palette_scope)
        label_80.setFont(QFont("Monospace"))
        bg_box.addWidget(label_80)

        hbox_lay_algorithm_81 =  QHBoxLayout()
        label_algorithm_81 = QLabel("    algorithm")
        label_algorithm_81.setPalette(palette_object)
        label_algorithm_81.setFont(QFont("Monospace"))
        hbox_lay_algorithm_81.addWidget(label_algorithm_81)

        box_algorithm_81 = QComboBox()
        box_algorithm_81.local_path = "profile.algorithm"
        box_algorithm_81.tmp_lst=[]
        box_algorithm_81.tmp_lst.append("gaussian_rs")
        for lst_itm in box_algorithm_81.tmp_lst:
            box_algorithm_81.addItem(lst_itm)
        box_algorithm_81.setCurrentIndex(0)
        box_algorithm_81.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_81.addWidget(box_algorithm_81)
        bg_box.addLayout(hbox_lay_algorithm_81)

        label_82 = QLabel("    gaussian_rs")
        label_82.setPalette(palette_scope)
        label_82.setFont(QFont("Monospace"))
        bg_box.addWidget(label_82)

        hbox_lay_scan_varying_83 =  QHBoxLayout()
        label_scan_varying_83 = QLabel("        scan_varying")
        label_scan_varying_83.setPalette(palette_object)
        label_scan_varying_83.setFont(QFont("Monospace"))
        hbox_lay_scan_varying_83.addWidget(label_scan_varying_83)

        box_scan_varying_83 = QComboBox()
        box_scan_varying_83.local_path = "profile.gaussian_rs.scan_varying"
        box_scan_varying_83.tmp_lst=[]
        box_scan_varying_83.tmp_lst.append("True")
        box_scan_varying_83.tmp_lst.append("False")
        for lst_itm in box_scan_varying_83.tmp_lst:
            box_scan_varying_83.addItem(lst_itm)
        box_scan_varying_83.setCurrentIndex(1)
        box_scan_varying_83.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_83.addWidget(box_scan_varying_83)
        bg_box.addLayout(hbox_lay_scan_varying_83)

        hbox_lay_min_spots_84 =  QHBoxLayout()
        label_min_spots_84 = QLabel("        min_spots")
        label_min_spots_84.setPalette(palette_object)
        label_min_spots_84.setFont(QFont("Monospace"))
        hbox_lay_min_spots_84.addWidget(label_min_spots_84)

        box_min_spots_84 = QSpinBox()
        box_min_spots_84.setValue(100)
        box_min_spots_84.local_path = "profile.gaussian_rs.min_spots"
        box_min_spots_84.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_spots_84.addWidget(box_min_spots_84)
        bg_box.addLayout(hbox_lay_min_spots_84)

        label_85 = QLabel("        filter")
        label_85.setPalette(palette_scope)
        label_85.setFont(QFont("Monospace"))
        bg_box.addWidget(label_85)

        hbox_lay_min_zeta_86 =  QHBoxLayout()
        label_min_zeta_86 = QLabel("            min_zeta")
        label_min_zeta_86.setPalette(palette_object)
        label_min_zeta_86.setFont(QFont("Monospace"))
        hbox_lay_min_zeta_86.addWidget(label_min_zeta_86)

        box_min_zeta_86 = QDoubleSpinBox()
        box_min_zeta_86.setValue(0.05)
        box_min_zeta_86.local_path = "profile.gaussian_rs.filter.min_zeta"
        box_min_zeta_86.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_zeta_86.addWidget(box_min_zeta_86)
        bg_box.addLayout(hbox_lay_min_zeta_86)

        label_87 = QLabel("        fitting")
        label_87.setPalette(palette_scope)
        label_87.setFont(QFont("Monospace"))
        bg_box.addWidget(label_87)

        hbox_lay_scan_step_88 =  QHBoxLayout()
        label_scan_step_88 = QLabel("            scan_step")
        label_scan_step_88.setPalette(palette_object)
        label_scan_step_88.setFont(QFont("Monospace"))
        hbox_lay_scan_step_88.addWidget(label_scan_step_88)

        box_scan_step_88 = QDoubleSpinBox()
        box_scan_step_88.setValue(5.0)
        box_scan_step_88.local_path = "profile.gaussian_rs.fitting.scan_step"
        box_scan_step_88.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_step_88.addWidget(box_scan_step_88)
        bg_box.addLayout(hbox_lay_scan_step_88)

        hbox_lay_grid_size_89 =  QHBoxLayout()
        label_grid_size_89 = QLabel("            grid_size")
        label_grid_size_89.setPalette(palette_object)
        label_grid_size_89.setFont(QFont("Monospace"))
        hbox_lay_grid_size_89.addWidget(label_grid_size_89)

        box_grid_size_89 = QSpinBox()
        box_grid_size_89.setValue(5)
        box_grid_size_89.local_path = "profile.gaussian_rs.fitting.grid_size"
        box_grid_size_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_grid_size_89.addWidget(box_grid_size_89)
        bg_box.addLayout(hbox_lay_grid_size_89)

        hbox_lay_threshold_90 =  QHBoxLayout()
        label_threshold_90 = QLabel("            threshold")
        label_threshold_90.setPalette(palette_object)
        label_threshold_90.setFont(QFont("Monospace"))
        hbox_lay_threshold_90.addWidget(label_threshold_90)

        box_threshold_90 = QDoubleSpinBox()
        box_threshold_90.setValue(0.02)
        box_threshold_90.local_path = "profile.gaussian_rs.fitting.threshold"
        box_threshold_90.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_90.addWidget(box_threshold_90)
        bg_box.addLayout(hbox_lay_threshold_90)

        hbox_lay_grid_method_91 =  QHBoxLayout()
        label_grid_method_91 = QLabel("            grid_method")
        label_grid_method_91.setPalette(palette_object)
        label_grid_method_91.setFont(QFont("Monospace"))
        hbox_lay_grid_method_91.addWidget(label_grid_method_91)

        box_grid_method_91 = QComboBox()
        box_grid_method_91.local_path = "profile.gaussian_rs.fitting.grid_method"
        box_grid_method_91.tmp_lst=[]
        box_grid_method_91.tmp_lst.append("single")
        box_grid_method_91.tmp_lst.append("regular_grid")
        box_grid_method_91.tmp_lst.append("circular_grid")
        for lst_itm in box_grid_method_91.tmp_lst:
            box_grid_method_91.addItem(lst_itm)
        box_grid_method_91.setCurrentIndex(1)
        box_grid_method_91.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_grid_method_91.addWidget(box_grid_method_91)
        bg_box.addLayout(hbox_lay_grid_method_91)

        hbox_lay_fit_method_92 =  QHBoxLayout()
        label_fit_method_92 = QLabel("            fit_method")
        label_fit_method_92.setPalette(palette_object)
        label_fit_method_92.setFont(QFont("Monospace"))
        hbox_lay_fit_method_92.addWidget(label_fit_method_92)

        box_fit_method_92 = QComboBox()
        box_fit_method_92.local_path = "profile.gaussian_rs.fitting.fit_method"
        box_fit_method_92.tmp_lst=[]
        box_fit_method_92.tmp_lst.append("reciprocal_space")
        box_fit_method_92.tmp_lst.append("detector_space")
        for lst_itm in box_fit_method_92.tmp_lst:
            box_fit_method_92.addItem(lst_itm)
        box_fit_method_92.setCurrentIndex(0)
        box_fit_method_92.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fit_method_92.addWidget(box_fit_method_92)
        bg_box.addLayout(hbox_lay_fit_method_92)

        label_93 = QLabel("prediction")
        label_93.setPalette(palette_scope)
        label_93.setFont(QFont("Monospace"))
        bg_box.addWidget(label_93)

        hbox_lay_d_min_94 =  QHBoxLayout()
        label_d_min_94 = QLabel("    d_min")
        label_d_min_94.setPalette(palette_object)
        label_d_min_94.setFont(QFont("Monospace"))
        hbox_lay_d_min_94.addWidget(label_d_min_94)

        box_d_min_94 = QDoubleSpinBox()
        box_d_min_94.local_path = "prediction.d_min"
        box_d_min_94.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_94.addWidget(box_d_min_94)
        bg_box.addLayout(hbox_lay_d_min_94)

        hbox_lay_d_max_95 =  QHBoxLayout()
        label_d_max_95 = QLabel("    d_max")
        label_d_max_95.setPalette(palette_object)
        label_d_max_95.setFont(QFont("Monospace"))
        hbox_lay_d_max_95.addWidget(label_d_max_95)

        box_d_max_95 = QDoubleSpinBox()
        box_d_max_95.local_path = "prediction.d_max"
        box_d_max_95.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_95.addWidget(box_d_max_95)
        bg_box.addLayout(hbox_lay_d_max_95)

        hbox_lay_margin_96 =  QHBoxLayout()
        label_margin_96 = QLabel("    margin")
        label_margin_96.setPalette(palette_object)
        label_margin_96.setFont(QFont("Monospace"))
        hbox_lay_margin_96.addWidget(label_margin_96)

        box_margin_96 = QSpinBox()
        box_margin_96.setValue(1)
        box_margin_96.local_path = "prediction.margin"
        box_margin_96.valueChanged.connect(self.spnbox_changed)
        hbox_lay_margin_96.addWidget(box_margin_96)
        bg_box.addLayout(hbox_lay_margin_96)

        hbox_lay_force_static_97 =  QHBoxLayout()
        label_force_static_97 = QLabel("    force_static")
        label_force_static_97.setPalette(palette_object)
        label_force_static_97.setFont(QFont("Monospace"))
        hbox_lay_force_static_97.addWidget(label_force_static_97)

        box_force_static_97 = QComboBox()
        box_force_static_97.local_path = "prediction.force_static"
        box_force_static_97.tmp_lst=[]
        box_force_static_97.tmp_lst.append("True")
        box_force_static_97.tmp_lst.append("False")
        for lst_itm in box_force_static_97.tmp_lst:
            box_force_static_97.addItem(lst_itm)
        box_force_static_97.setCurrentIndex(1)
        box_force_static_97.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_97.addWidget(box_force_static_97)
        bg_box.addLayout(hbox_lay_force_static_97)

 
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
