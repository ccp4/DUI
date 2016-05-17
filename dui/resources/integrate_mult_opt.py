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

        hbox_lay_phil_3 =  QHBoxLayout()
        label_phil_3 = QLabel("    phil")
        label_phil_3.setPalette(palette_object)
        label_phil_3.setFont(QFont("Monospace", 10))
        hbox_lay_phil_3.addWidget(label_phil_3)

        box_phil_3 = QLineEdit()
        box_phil_3.local_path = "output.phil"
        box_phil_3.textChanged.connect(self.spnbox_changed)
        hbox_lay_phil_3.addWidget(box_phil_3)
        bg_box.addLayout(hbox_lay_phil_3)

        hbox_lay_log_4 =  QHBoxLayout()
        label_log_4 = QLabel("    log")
        label_log_4.setPalette(palette_object)
        label_log_4.setFont(QFont("Monospace", 10))
        hbox_lay_log_4.addWidget(label_log_4)

        box_log_4 = QLineEdit()
        box_log_4.local_path = "output.log"
        box_log_4.textChanged.connect(self.spnbox_changed)
        hbox_lay_log_4.addWidget(box_log_4)
        bg_box.addLayout(hbox_lay_log_4)

        hbox_lay_debug_log_5 =  QHBoxLayout()
        label_debug_log_5 = QLabel("    debug_log")
        label_debug_log_5.setPalette(palette_object)
        label_debug_log_5.setFont(QFont("Monospace", 10))
        hbox_lay_debug_log_5.addWidget(label_debug_log_5)

        box_debug_log_5 = QLineEdit()
        box_debug_log_5.local_path = "output.debug_log"
        box_debug_log_5.textChanged.connect(self.spnbox_changed)
        hbox_lay_debug_log_5.addWidget(box_debug_log_5)
        bg_box.addLayout(hbox_lay_debug_log_5)

        hbox_lay_report_6 =  QHBoxLayout()
        label_report_6 = QLabel("    report")
        label_report_6.setPalette(palette_object)
        label_report_6.setFont(QFont("Monospace", 10))
        hbox_lay_report_6.addWidget(label_report_6)

        box_report_6 = QLineEdit()
        box_report_6.local_path = "output.report"
        box_report_6.textChanged.connect(self.spnbox_changed)
        hbox_lay_report_6.addWidget(box_report_6)
        bg_box.addLayout(hbox_lay_report_6)

        hbox_lay_include_bad_reference_7 =  QHBoxLayout()
        label_include_bad_reference_7 = QLabel("    include_bad_reference")
        label_include_bad_reference_7.setPalette(palette_object)
        label_include_bad_reference_7.setFont(QFont("Monospace", 10))
        hbox_lay_include_bad_reference_7.addWidget(label_include_bad_reference_7)

        box_include_bad_reference_7 = QComboBox()
        box_include_bad_reference_7.local_path = "output.include_bad_reference"
        box_include_bad_reference_7.tmp_lst=[]
        box_include_bad_reference_7.tmp_lst.append("True")
        box_include_bad_reference_7.tmp_lst.append("False")
        for lst_itm in box_include_bad_reference_7.tmp_lst:
            box_include_bad_reference_7.addItem(lst_itm)
        box_include_bad_reference_7.setCurrentIndex(1)
        box_include_bad_reference_7.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_include_bad_reference_7.addWidget(box_include_bad_reference_7)
        bg_box.addLayout(hbox_lay_include_bad_reference_7)

        hbox_lay_scan_range_8_0 =  QHBoxLayout()
        label_scan_range_8_0 = QLabel("scan_range[1]")
        label_scan_range_8_0.setPalette(palette_object)
        label_scan_range_8_0.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_8_0.addWidget(label_scan_range_8_0)
        box_scan_range_8_0 = QSpinBox()
        box_scan_range_8_0.local_path = "scan_range"
        #box_scan_range_8_0.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_8_1 =  QHBoxLayout()
        label_scan_range_8_1 = QLabel("scan_range[2]")
        label_scan_range_8_1.setPalette(palette_object)
        label_scan_range_8_1.setFont(QFont("Monospace", 10))
        hbox_lay_scan_range_8_1.addWidget(label_scan_range_8_1)
        box_scan_range_8_1 = QSpinBox()
        box_scan_range_8_1.local_path = "scan_range"
        #box_scan_range_8_1.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_range_8_0.addWidget(box_scan_range_8_0)
        bg_box.addLayout(hbox_lay_scan_range_8_0)
        hbox_lay_scan_range_8_1.addWidget(box_scan_range_8_1)
        bg_box.addLayout(hbox_lay_scan_range_8_1)

        hbox_lay_create_profile_model_9 =  QHBoxLayout()
        label_create_profile_model_9 = QLabel("create_profile_model")
        label_create_profile_model_9.setPalette(palette_object)
        label_create_profile_model_9.setFont(QFont("Monospace", 10))
        hbox_lay_create_profile_model_9.addWidget(label_create_profile_model_9)

        box_create_profile_model_9 = QComboBox()
        box_create_profile_model_9.local_path = "create_profile_model"
        box_create_profile_model_9.tmp_lst=[]
        box_create_profile_model_9.tmp_lst.append("True")
        box_create_profile_model_9.tmp_lst.append("False")
        for lst_itm in box_create_profile_model_9.tmp_lst:
            box_create_profile_model_9.addItem(lst_itm)
        box_create_profile_model_9.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_create_profile_model_9.addWidget(box_create_profile_model_9)
        bg_box.addLayout(hbox_lay_create_profile_model_9)

        label_10 = QLabel("sampling")
        label_10.setPalette(palette_scope)
        label_10.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_10)

        hbox_lay_reflections_per_degree_11 =  QHBoxLayout()
        label_reflections_per_degree_11 = QLabel("    reflections_per_degree")
        label_reflections_per_degree_11.setPalette(palette_object)
        label_reflections_per_degree_11.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_11.addWidget(label_reflections_per_degree_11)

        box_reflections_per_degree_11 = QDoubleSpinBox()
        box_reflections_per_degree_11.setValue(50.0)
        box_reflections_per_degree_11.local_path = "sampling.reflections_per_degree"
        box_reflections_per_degree_11.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_11.addWidget(box_reflections_per_degree_11)
        bg_box.addLayout(hbox_lay_reflections_per_degree_11)

        hbox_lay_minimum_sample_size_12 =  QHBoxLayout()
        label_minimum_sample_size_12 = QLabel("    minimum_sample_size")
        label_minimum_sample_size_12.setPalette(palette_object)
        label_minimum_sample_size_12.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_12.addWidget(label_minimum_sample_size_12)

        box_minimum_sample_size_12 = QSpinBox()
        box_minimum_sample_size_12.setValue(1000)
        box_minimum_sample_size_12.local_path = "sampling.minimum_sample_size"
        box_minimum_sample_size_12.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_12.addWidget(box_minimum_sample_size_12)
        bg_box.addLayout(hbox_lay_minimum_sample_size_12)

        hbox_lay_maximum_sample_size_13 =  QHBoxLayout()
        label_maximum_sample_size_13 = QLabel("    maximum_sample_size")
        label_maximum_sample_size_13.setPalette(palette_object)
        label_maximum_sample_size_13.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_13.addWidget(label_maximum_sample_size_13)

        box_maximum_sample_size_13 = QSpinBox()
        box_maximum_sample_size_13.local_path = "sampling.maximum_sample_size"
        box_maximum_sample_size_13.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_13.addWidget(box_maximum_sample_size_13)
        bg_box.addLayout(hbox_lay_maximum_sample_size_13)

        hbox_lay_integrate_all_reflections_14 =  QHBoxLayout()
        label_integrate_all_reflections_14 = QLabel("    integrate_all_reflections")
        label_integrate_all_reflections_14.setPalette(palette_object)
        label_integrate_all_reflections_14.setFont(QFont("Monospace", 10))
        hbox_lay_integrate_all_reflections_14.addWidget(label_integrate_all_reflections_14)

        box_integrate_all_reflections_14 = QComboBox()
        box_integrate_all_reflections_14.local_path = "sampling.integrate_all_reflections"
        box_integrate_all_reflections_14.tmp_lst=[]
        box_integrate_all_reflections_14.tmp_lst.append("True")
        box_integrate_all_reflections_14.tmp_lst.append("False")
        for lst_itm in box_integrate_all_reflections_14.tmp_lst:
            box_integrate_all_reflections_14.addItem(lst_itm)
        box_integrate_all_reflections_14.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_integrate_all_reflections_14.addWidget(box_integrate_all_reflections_14)
        bg_box.addLayout(hbox_lay_integrate_all_reflections_14)

        hbox_lay_verbosity_15 =  QHBoxLayout()
        label_verbosity_15 = QLabel("verbosity")
        label_verbosity_15.setPalette(palette_object)
        label_verbosity_15.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_15.addWidget(label_verbosity_15)

        box_verbosity_15 = QSpinBox()
        box_verbosity_15.setValue(1)
        box_verbosity_15.local_path = "verbosity"
        box_verbosity_15.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_15.addWidget(box_verbosity_15)
        bg_box.addLayout(hbox_lay_verbosity_15)

        label_16 = QLabel("integration")
        label_16.setPalette(palette_scope)
        label_16.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_16)

        label_17 = QLabel("    mp")
        label_17.setPalette(palette_scope)
        label_17.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_17)

        hbox_lay_method_18 =  QHBoxLayout()
        label_method_18 = QLabel("        method")
        label_method_18.setPalette(palette_object)
        label_method_18.setFont(QFont("Monospace", 10))
        hbox_lay_method_18.addWidget(label_method_18)

        box_method_18 = QComboBox()
        box_method_18.local_path = "integration.mp.method"
        box_method_18.tmp_lst=[]
        box_method_18.tmp_lst.append("multiprocessing")
        box_method_18.tmp_lst.append("sge")
        box_method_18.tmp_lst.append("lsf")
        box_method_18.tmp_lst.append("pbs")
        for lst_itm in box_method_18.tmp_lst:
            box_method_18.addItem(lst_itm)
        box_method_18.setCurrentIndex(0)
        box_method_18.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_18.addWidget(box_method_18)
        bg_box.addLayout(hbox_lay_method_18)

        hbox_lay_nproc_19 =  QHBoxLayout()
        label_nproc_19 = QLabel("        nproc")
        label_nproc_19.setPalette(palette_object)
        label_nproc_19.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_19.addWidget(label_nproc_19)

        box_nproc_19 = QSpinBox()
        box_nproc_19.setValue(1)
        box_nproc_19.local_path = "integration.mp.nproc"
        box_nproc_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_19.addWidget(box_nproc_19)
        bg_box.addLayout(hbox_lay_nproc_19)

        hbox_lay_nthreads_20 =  QHBoxLayout()
        label_nthreads_20 = QLabel("        nthreads")
        label_nthreads_20.setPalette(palette_object)
        label_nthreads_20.setFont(QFont("Monospace", 10))
        hbox_lay_nthreads_20.addWidget(label_nthreads_20)

        box_nthreads_20 = QSpinBox()
        box_nthreads_20.setValue(1)
        box_nthreads_20.local_path = "integration.mp.nthreads"
        box_nthreads_20.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nthreads_20.addWidget(box_nthreads_20)
        bg_box.addLayout(hbox_lay_nthreads_20)

        label_21 = QLabel("    lookup")
        label_21.setPalette(palette_scope)
        label_21.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_21)

        hbox_lay_mask_22 =  QHBoxLayout()
        label_mask_22 = QLabel("        mask")
        label_mask_22.setPalette(palette_object)
        label_mask_22.setFont(QFont("Monospace", 10))
        hbox_lay_mask_22.addWidget(label_mask_22)

        box_mask_22 = QLineEdit()
        box_mask_22.local_path = "integration.lookup.mask"
        box_mask_22.textChanged.connect(self.spnbox_changed)
        hbox_lay_mask_22.addWidget(box_mask_22)
        bg_box.addLayout(hbox_lay_mask_22)

        label_23 = QLabel("    block")
        label_23.setPalette(palette_scope)
        label_23.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_23)

        hbox_lay_size_24 =  QHBoxLayout()
        label_size_24 = QLabel("        size")
        label_size_24.setPalette(palette_object)
        label_size_24.setFont(QFont("Monospace", 10))
        hbox_lay_size_24.addWidget(label_size_24)

        box_size_24 = QDoubleSpinBox()
        box_size_24.local_path = "integration.block.size"
        box_size_24.valueChanged.connect(self.spnbox_changed)
        hbox_lay_size_24.addWidget(box_size_24)
        bg_box.addLayout(hbox_lay_size_24)

        hbox_lay_units_25 =  QHBoxLayout()
        label_units_25 = QLabel("        units")
        label_units_25.setPalette(palette_object)
        label_units_25.setFont(QFont("Monospace", 10))
        hbox_lay_units_25.addWidget(label_units_25)

        box_units_25 = QComboBox()
        box_units_25.local_path = "integration.block.units"
        box_units_25.tmp_lst=[]
        box_units_25.tmp_lst.append("degrees")
        box_units_25.tmp_lst.append("radians")
        box_units_25.tmp_lst.append("frames")
        for lst_itm in box_units_25.tmp_lst:
            box_units_25.addItem(lst_itm)
        box_units_25.setCurrentIndex(0)
        box_units_25.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_units_25.addWidget(box_units_25)
        bg_box.addLayout(hbox_lay_units_25)

        hbox_lay_threshold_26 =  QHBoxLayout()
        label_threshold_26 = QLabel("        threshold")
        label_threshold_26.setPalette(palette_object)
        label_threshold_26.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_26.addWidget(label_threshold_26)

        box_threshold_26 = QDoubleSpinBox()
        box_threshold_26.setValue(0.99)
        box_threshold_26.local_path = "integration.block.threshold"
        box_threshold_26.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_26.addWidget(box_threshold_26)
        bg_box.addLayout(hbox_lay_threshold_26)

        hbox_lay_force_27 =  QHBoxLayout()
        label_force_27 = QLabel("        force")
        label_force_27.setPalette(palette_object)
        label_force_27.setFont(QFont("Monospace", 10))
        hbox_lay_force_27.addWidget(label_force_27)

        box_force_27 = QComboBox()
        box_force_27.local_path = "integration.block.force"
        box_force_27.tmp_lst=[]
        box_force_27.tmp_lst.append("True")
        box_force_27.tmp_lst.append("False")
        for lst_itm in box_force_27.tmp_lst:
            box_force_27.addItem(lst_itm)
        box_force_27.setCurrentIndex(1)
        box_force_27.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_27.addWidget(box_force_27)
        bg_box.addLayout(hbox_lay_force_27)

        hbox_lay_max_memory_usage_28 =  QHBoxLayout()
        label_max_memory_usage_28 = QLabel("        max_memory_usage")
        label_max_memory_usage_28.setPalette(palette_object)
        label_max_memory_usage_28.setFont(QFont("Monospace", 10))
        hbox_lay_max_memory_usage_28.addWidget(label_max_memory_usage_28)

        box_max_memory_usage_28 = QDoubleSpinBox()
        box_max_memory_usage_28.setValue(0.75)
        box_max_memory_usage_28.local_path = "integration.block.max_memory_usage"
        box_max_memory_usage_28.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_memory_usage_28.addWidget(box_max_memory_usage_28)
        bg_box.addLayout(hbox_lay_max_memory_usage_28)

        label_29 = QLabel("    debug")
        label_29.setPalette(palette_scope)
        label_29.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_29)

        label_30 = QLabel("        reference")
        label_30.setPalette(palette_scope)
        label_30.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_30)

        hbox_lay_output_31 =  QHBoxLayout()
        label_output_31 = QLabel("            output")
        label_output_31.setPalette(palette_object)
        label_output_31.setFont(QFont("Monospace", 10))
        hbox_lay_output_31.addWidget(label_output_31)

        box_output_31 = QComboBox()
        box_output_31.local_path = "integration.debug.reference.output"
        box_output_31.tmp_lst=[]
        box_output_31.tmp_lst.append("True")
        box_output_31.tmp_lst.append("False")
        for lst_itm in box_output_31.tmp_lst:
            box_output_31.addItem(lst_itm)
        box_output_31.setCurrentIndex(1)
        box_output_31.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_output_31.addWidget(box_output_31)
        bg_box.addLayout(hbox_lay_output_31)

        hbox_lay_during_32 =  QHBoxLayout()
        label_during_32 = QLabel("        during")
        label_during_32.setPalette(palette_object)
        label_during_32.setFont(QFont("Monospace", 10))
        hbox_lay_during_32.addWidget(label_during_32)

        box_during_32 = QComboBox()
        box_during_32.local_path = "integration.debug.during"
        box_during_32.tmp_lst=[]
        box_during_32.tmp_lst.append("modelling")
        box_during_32.tmp_lst.append("integration")
        for lst_itm in box_during_32.tmp_lst:
            box_during_32.addItem(lst_itm)
        box_during_32.setCurrentIndex(1)
        box_during_32.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_during_32.addWidget(box_during_32)
        bg_box.addLayout(hbox_lay_during_32)

        hbox_lay_output_33 =  QHBoxLayout()
        label_output_33 = QLabel("        output")
        label_output_33.setPalette(palette_object)
        label_output_33.setFont(QFont("Monospace", 10))
        hbox_lay_output_33.addWidget(label_output_33)

        box_output_33 = QComboBox()
        box_output_33.local_path = "integration.debug.output"
        box_output_33.tmp_lst=[]
        box_output_33.tmp_lst.append("True")
        box_output_33.tmp_lst.append("False")
        for lst_itm in box_output_33.tmp_lst:
            box_output_33.addItem(lst_itm)
        box_output_33.setCurrentIndex(1)
        box_output_33.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_output_33.addWidget(box_output_33)
        bg_box.addLayout(hbox_lay_output_33)

        hbox_lay_separate_files_34 =  QHBoxLayout()
        label_separate_files_34 = QLabel("        separate_files")
        label_separate_files_34.setPalette(palette_object)
        label_separate_files_34.setFont(QFont("Monospace", 10))
        hbox_lay_separate_files_34.addWidget(label_separate_files_34)

        box_separate_files_34 = QComboBox()
        box_separate_files_34.local_path = "integration.debug.separate_files"
        box_separate_files_34.tmp_lst=[]
        box_separate_files_34.tmp_lst.append("True")
        box_separate_files_34.tmp_lst.append("False")
        for lst_itm in box_separate_files_34.tmp_lst:
            box_separate_files_34.addItem(lst_itm)
        box_separate_files_34.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_files_34.addWidget(box_separate_files_34)
        bg_box.addLayout(hbox_lay_separate_files_34)


        hbox_lay_split_experiments_36 =  QHBoxLayout()
        label_split_experiments_36 = QLabel("        split_experiments")
        label_split_experiments_36.setPalette(palette_object)
        label_split_experiments_36.setFont(QFont("Monospace", 10))
        hbox_lay_split_experiments_36.addWidget(label_split_experiments_36)

        box_split_experiments_36 = QComboBox()
        box_split_experiments_36.local_path = "integration.debug.split_experiments"
        box_split_experiments_36.tmp_lst=[]
        box_split_experiments_36.tmp_lst.append("True")
        box_split_experiments_36.tmp_lst.append("False")
        for lst_itm in box_split_experiments_36.tmp_lst:
            box_split_experiments_36.addItem(lst_itm)
        box_split_experiments_36.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_split_experiments_36.addWidget(box_split_experiments_36)
        bg_box.addLayout(hbox_lay_split_experiments_36)

        hbox_lay_integrator_37 =  QHBoxLayout()
        label_integrator_37 = QLabel("    integrator")
        label_integrator_37.setPalette(palette_object)
        label_integrator_37.setFont(QFont("Monospace", 10))
        hbox_lay_integrator_37.addWidget(label_integrator_37)

        box_integrator_37 = QComboBox()
        box_integrator_37.local_path = "integration.integrator"
        box_integrator_37.tmp_lst=[]
        box_integrator_37.tmp_lst.append("auto")
        box_integrator_37.tmp_lst.append("3d")
        box_integrator_37.tmp_lst.append("flat3d")
        box_integrator_37.tmp_lst.append("2d")
        box_integrator_37.tmp_lst.append("single2d")
        box_integrator_37.tmp_lst.append("stills")
        box_integrator_37.tmp_lst.append("volume")
        for lst_itm in box_integrator_37.tmp_lst:
            box_integrator_37.addItem(lst_itm)
        box_integrator_37.setCurrentIndex(0)
        box_integrator_37.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_integrator_37.addWidget(box_integrator_37)
        bg_box.addLayout(hbox_lay_integrator_37)

        label_38 = QLabel("    profile")
        label_38.setPalette(palette_scope)
        label_38.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_38)

        hbox_lay_fitting_39 =  QHBoxLayout()
        label_fitting_39 = QLabel("        fitting")
        label_fitting_39.setPalette(palette_object)
        label_fitting_39.setFont(QFont("Monospace", 10))
        hbox_lay_fitting_39.addWidget(label_fitting_39)

        box_fitting_39 = QComboBox()
        box_fitting_39.local_path = "integration.profile.fitting"
        box_fitting_39.tmp_lst=[]
        box_fitting_39.tmp_lst.append("True")
        box_fitting_39.tmp_lst.append("False")
        for lst_itm in box_fitting_39.tmp_lst:
            box_fitting_39.addItem(lst_itm)
        box_fitting_39.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fitting_39.addWidget(box_fitting_39)
        bg_box.addLayout(hbox_lay_fitting_39)

        label_40 = QLabel("        validation")
        label_40.setPalette(palette_scope)
        label_40.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_40)

        hbox_lay_number_of_partitions_41 =  QHBoxLayout()
        label_number_of_partitions_41 = QLabel("            number_of_partitions")
        label_number_of_partitions_41.setPalette(palette_object)
        label_number_of_partitions_41.setFont(QFont("Monospace", 10))
        hbox_lay_number_of_partitions_41.addWidget(label_number_of_partitions_41)

        box_number_of_partitions_41 = QSpinBox()
        box_number_of_partitions_41.setValue(1)
        box_number_of_partitions_41.local_path = "integration.profile.validation.number_of_partitions"
        box_number_of_partitions_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_number_of_partitions_41.addWidget(box_number_of_partitions_41)
        bg_box.addLayout(hbox_lay_number_of_partitions_41)

        hbox_lay_min_partition_size_42 =  QHBoxLayout()
        label_min_partition_size_42 = QLabel("            min_partition_size")
        label_min_partition_size_42.setPalette(palette_object)
        label_min_partition_size_42.setFont(QFont("Monospace", 10))
        hbox_lay_min_partition_size_42.addWidget(label_min_partition_size_42)

        box_min_partition_size_42 = QSpinBox()
        box_min_partition_size_42.setValue(100)
        box_min_partition_size_42.local_path = "integration.profile.validation.min_partition_size"
        box_min_partition_size_42.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_partition_size_42.addWidget(box_min_partition_size_42)
        bg_box.addLayout(hbox_lay_min_partition_size_42)

        label_43 = QLabel("    filter")
        label_43.setPalette(palette_scope)
        label_43.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_43)

        hbox_lay_min_zeta_44 =  QHBoxLayout()
        label_min_zeta_44 = QLabel("        min_zeta")
        label_min_zeta_44.setPalette(palette_object)
        label_min_zeta_44.setFont(QFont("Monospace", 10))
        hbox_lay_min_zeta_44.addWidget(label_min_zeta_44)

        box_min_zeta_44 = QDoubleSpinBox()
        box_min_zeta_44.setValue(0.05)
        box_min_zeta_44.local_path = "integration.filter.min_zeta"
        box_min_zeta_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_zeta_44.addWidget(box_min_zeta_44)
        bg_box.addLayout(hbox_lay_min_zeta_44)

        hbox_lay_max_shoebox_overlap_45 =  QHBoxLayout()
        label_max_shoebox_overlap_45 = QLabel("        max_shoebox_overlap")
        label_max_shoebox_overlap_45.setPalette(palette_object)
        label_max_shoebox_overlap_45.setFont(QFont("Monospace", 10))
        hbox_lay_max_shoebox_overlap_45.addWidget(label_max_shoebox_overlap_45)

        box_max_shoebox_overlap_45 = QDoubleSpinBox()
        box_max_shoebox_overlap_45.setValue(1.0)
        box_max_shoebox_overlap_45.local_path = "integration.filter.max_shoebox_overlap"
        box_max_shoebox_overlap_45.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_shoebox_overlap_45.addWidget(box_max_shoebox_overlap_45)
        bg_box.addLayout(hbox_lay_max_shoebox_overlap_45)

        label_46 = QLabel("        powder")
        label_46.setPalette(palette_scope)
        label_46.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_46)

        label_47 = QLabel("            water_ice")
        label_47.setPalette(palette_scope)
        label_47.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_47)



        hbox_lay_d_min_50 =  QHBoxLayout()
        label_d_min_50 = QLabel("                d_min")
        label_d_min_50.setPalette(palette_object)
        label_d_min_50.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_50.addWidget(label_d_min_50)

        box_d_min_50 = QDoubleSpinBox()
        box_d_min_50.setValue(1.0)
        box_d_min_50.local_path = "integration.filter.powder.water_ice.d_min"
        box_d_min_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_50.addWidget(box_d_min_50)
        bg_box.addLayout(hbox_lay_d_min_50)

        hbox_lay_width_51 =  QHBoxLayout()
        label_width_51 = QLabel("                width")
        label_width_51.setPalette(palette_object)
        label_width_51.setFont(QFont("Monospace", 10))
        hbox_lay_width_51.addWidget(label_width_51)

        box_width_51 = QDoubleSpinBox()
        box_width_51.setValue(0.06)
        box_width_51.local_path = "integration.filter.powder.water_ice.width"
        box_width_51.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_51.addWidget(box_width_51)
        bg_box.addLayout(hbox_lay_width_51)

        hbox_lay_apply_52 =  QHBoxLayout()
        label_apply_52 = QLabel("            apply")
        label_apply_52.setPalette(palette_object)
        label_apply_52.setFont(QFont("Monospace", 10))
        hbox_lay_apply_52.addWidget(label_apply_52)

        box_apply_52 = QComboBox()
        box_apply_52.local_path = "integration.filter.powder.apply"
        box_apply_52.tmp_lst=[]
        box_apply_52.tmp_lst.append("none")
        box_apply_52.tmp_lst.append("water_ice")
        for lst_itm in box_apply_52.tmp_lst:
            box_apply_52.addItem(lst_itm)
        box_apply_52.setCurrentIndex(0)
        box_apply_52.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_52.addWidget(box_apply_52)
        bg_box.addLayout(hbox_lay_apply_52)

        label_53 = QLabel("    background")
        label_53.setPalette(palette_scope)
        label_53.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_53)

        hbox_lay_algorithm_54 =  QHBoxLayout()
        label_algorithm_54 = QLabel("        algorithm")
        label_algorithm_54.setPalette(palette_object)
        label_algorithm_54.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_54.addWidget(label_algorithm_54)

        box_algorithm_54 = QComboBox()
        box_algorithm_54.local_path = "integration.background.algorithm"
        box_algorithm_54.tmp_lst=[]
        box_algorithm_54.tmp_lst.append("simple")
        box_algorithm_54.tmp_lst.append("null")
        box_algorithm_54.tmp_lst.append("median")
        box_algorithm_54.tmp_lst.append("glm")
        box_algorithm_54.tmp_lst.append("const_d")
        for lst_itm in box_algorithm_54.tmp_lst:
            box_algorithm_54.addItem(lst_itm)
        box_algorithm_54.setCurrentIndex(3)
        box_algorithm_54.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_54.addWidget(box_algorithm_54)
        bg_box.addLayout(hbox_lay_algorithm_54)

        label_55 = QLabel("        simple")
        label_55.setPalette(palette_scope)
        label_55.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_55)

        label_56 = QLabel("            outlier")
        label_56.setPalette(palette_scope)
        label_56.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_56)

        hbox_lay_algorithm_57 =  QHBoxLayout()
        label_algorithm_57 = QLabel("                algorithm")
        label_algorithm_57.setPalette(palette_object)
        label_algorithm_57.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_57.addWidget(label_algorithm_57)

        box_algorithm_57 = QComboBox()
        box_algorithm_57.local_path = "integration.background.simple.outlier.algorithm"
        box_algorithm_57.tmp_lst=[]
        box_algorithm_57.tmp_lst.append("null")
        box_algorithm_57.tmp_lst.append("nsigma")
        box_algorithm_57.tmp_lst.append("truncated")
        box_algorithm_57.tmp_lst.append("normal")
        box_algorithm_57.tmp_lst.append("mosflm")
        box_algorithm_57.tmp_lst.append("tukey")
        for lst_itm in box_algorithm_57.tmp_lst:
            box_algorithm_57.addItem(lst_itm)
        box_algorithm_57.setCurrentIndex(1)
        box_algorithm_57.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_57.addWidget(box_algorithm_57)
        bg_box.addLayout(hbox_lay_algorithm_57)

        label_58 = QLabel("                nsigma")
        label_58.setPalette(palette_scope)
        label_58.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_58)

        hbox_lay_lower_59 =  QHBoxLayout()
        label_lower_59 = QLabel("                    lower")
        label_lower_59.setPalette(palette_object)
        label_lower_59.setFont(QFont("Monospace", 10))
        hbox_lay_lower_59.addWidget(label_lower_59)

        box_lower_59 = QDoubleSpinBox()
        box_lower_59.setValue(3.0)
        box_lower_59.local_path = "integration.background.simple.outlier.nsigma.lower"
        box_lower_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_59.addWidget(box_lower_59)
        bg_box.addLayout(hbox_lay_lower_59)

        hbox_lay_upper_60 =  QHBoxLayout()
        label_upper_60 = QLabel("                    upper")
        label_upper_60.setPalette(palette_object)
        label_upper_60.setFont(QFont("Monospace", 10))
        hbox_lay_upper_60.addWidget(label_upper_60)

        box_upper_60 = QDoubleSpinBox()
        box_upper_60.setValue(3.0)
        box_upper_60.local_path = "integration.background.simple.outlier.nsigma.upper"
        box_upper_60.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_60.addWidget(box_upper_60)
        bg_box.addLayout(hbox_lay_upper_60)

        label_61 = QLabel("                truncated")
        label_61.setPalette(palette_scope)
        label_61.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_61)

        hbox_lay_lower_62 =  QHBoxLayout()
        label_lower_62 = QLabel("                    lower")
        label_lower_62.setPalette(palette_object)
        label_lower_62.setFont(QFont("Monospace", 10))
        hbox_lay_lower_62.addWidget(label_lower_62)

        box_lower_62 = QDoubleSpinBox()
        box_lower_62.setValue(0.01)
        box_lower_62.local_path = "integration.background.simple.outlier.truncated.lower"
        box_lower_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_62.addWidget(box_lower_62)
        bg_box.addLayout(hbox_lay_lower_62)

        hbox_lay_upper_63 =  QHBoxLayout()
        label_upper_63 = QLabel("                    upper")
        label_upper_63.setPalette(palette_object)
        label_upper_63.setFont(QFont("Monospace", 10))
        hbox_lay_upper_63.addWidget(label_upper_63)

        box_upper_63 = QDoubleSpinBox()
        box_upper_63.setValue(0.01)
        box_upper_63.local_path = "integration.background.simple.outlier.truncated.upper"
        box_upper_63.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_63.addWidget(box_upper_63)
        bg_box.addLayout(hbox_lay_upper_63)

        label_64 = QLabel("                normal")
        label_64.setPalette(palette_scope)
        label_64.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_64)

        hbox_lay_min_pixels_65 =  QHBoxLayout()
        label_min_pixels_65 = QLabel("                    min_pixels")
        label_min_pixels_65.setPalette(palette_object)
        label_min_pixels_65.setFont(QFont("Monospace", 10))
        hbox_lay_min_pixels_65.addWidget(label_min_pixels_65)

        box_min_pixels_65 = QSpinBox()
        box_min_pixels_65.setValue(10)
        box_min_pixels_65.local_path = "integration.background.simple.outlier.normal.min_pixels"
        box_min_pixels_65.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_pixels_65.addWidget(box_min_pixels_65)
        bg_box.addLayout(hbox_lay_min_pixels_65)

        label_66 = QLabel("                mosflm")
        label_66.setPalette(palette_scope)
        label_66.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_66)

        hbox_lay_fraction_67 =  QHBoxLayout()
        label_fraction_67 = QLabel("                    fraction")
        label_fraction_67.setPalette(palette_object)
        label_fraction_67.setFont(QFont("Monospace", 10))
        hbox_lay_fraction_67.addWidget(label_fraction_67)

        box_fraction_67 = QDoubleSpinBox()
        box_fraction_67.setValue(1.0)
        box_fraction_67.local_path = "integration.background.simple.outlier.mosflm.fraction"
        box_fraction_67.valueChanged.connect(self.spnbox_changed)
        hbox_lay_fraction_67.addWidget(box_fraction_67)
        bg_box.addLayout(hbox_lay_fraction_67)

        hbox_lay_n_sigma_68 =  QHBoxLayout()
        label_n_sigma_68 = QLabel("                    n_sigma")
        label_n_sigma_68.setPalette(palette_object)
        label_n_sigma_68.setFont(QFont("Monospace", 10))
        hbox_lay_n_sigma_68.addWidget(label_n_sigma_68)

        box_n_sigma_68 = QDoubleSpinBox()
        box_n_sigma_68.setValue(4.0)
        box_n_sigma_68.local_path = "integration.background.simple.outlier.mosflm.n_sigma"
        box_n_sigma_68.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_sigma_68.addWidget(box_n_sigma_68)
        bg_box.addLayout(hbox_lay_n_sigma_68)

        label_69 = QLabel("                tukey")
        label_69.setPalette(palette_scope)
        label_69.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_69)

        hbox_lay_lower_70 =  QHBoxLayout()
        label_lower_70 = QLabel("                    lower")
        label_lower_70.setPalette(palette_object)
        label_lower_70.setFont(QFont("Monospace", 10))
        hbox_lay_lower_70.addWidget(label_lower_70)

        box_lower_70 = QDoubleSpinBox()
        box_lower_70.setValue(1.5)
        box_lower_70.local_path = "integration.background.simple.outlier.tukey.lower"
        box_lower_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_70.addWidget(box_lower_70)
        bg_box.addLayout(hbox_lay_lower_70)

        hbox_lay_upper_71 =  QHBoxLayout()
        label_upper_71 = QLabel("                    upper")
        label_upper_71.setPalette(palette_object)
        label_upper_71.setFont(QFont("Monospace", 10))
        hbox_lay_upper_71.addWidget(label_upper_71)

        box_upper_71 = QDoubleSpinBox()
        box_upper_71.setValue(1.5)
        box_upper_71.local_path = "integration.background.simple.outlier.tukey.upper"
        box_upper_71.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_71.addWidget(box_upper_71)
        bg_box.addLayout(hbox_lay_upper_71)

        label_72 = QLabel("            model")
        label_72.setPalette(palette_scope)
        label_72.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_72)

        hbox_lay_algorithm_73 =  QHBoxLayout()
        label_algorithm_73 = QLabel("                algorithm")
        label_algorithm_73.setPalette(palette_object)
        label_algorithm_73.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_73.addWidget(label_algorithm_73)

        box_algorithm_73 = QComboBox()
        box_algorithm_73.local_path = "integration.background.simple.model.algorithm"
        box_algorithm_73.tmp_lst=[]
        box_algorithm_73.tmp_lst.append("constant2d")
        box_algorithm_73.tmp_lst.append("constant3d")
        box_algorithm_73.tmp_lst.append("linear2d")
        box_algorithm_73.tmp_lst.append("linear3d")
        for lst_itm in box_algorithm_73.tmp_lst:
            box_algorithm_73.addItem(lst_itm)
        box_algorithm_73.setCurrentIndex(1)
        box_algorithm_73.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_73.addWidget(box_algorithm_73)
        bg_box.addLayout(hbox_lay_algorithm_73)

        label_74 = QLabel("        median")
        label_74.setPalette(palette_scope)
        label_74.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_74)

        label_75 = QLabel("        glm")
        label_75.setPalette(palette_scope)
        label_75.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_75)

        label_76 = QLabel("            robust")
        label_76.setPalette(palette_scope)
        label_76.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_76)

        hbox_lay_tuning_constant_77 =  QHBoxLayout()
        label_tuning_constant_77 = QLabel("                tuning_constant")
        label_tuning_constant_77.setPalette(palette_object)
        label_tuning_constant_77.setFont(QFont("Monospace", 10))
        hbox_lay_tuning_constant_77.addWidget(label_tuning_constant_77)

        box_tuning_constant_77 = QDoubleSpinBox()
        box_tuning_constant_77.setValue(1.345)
        box_tuning_constant_77.local_path = "integration.background.glm.robust.tuning_constant"
        box_tuning_constant_77.valueChanged.connect(self.spnbox_changed)
        hbox_lay_tuning_constant_77.addWidget(box_tuning_constant_77)
        bg_box.addLayout(hbox_lay_tuning_constant_77)

        label_78 = QLabel("            model")
        label_78.setPalette(palette_scope)
        label_78.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_78)

        hbox_lay_algorithm_79 =  QHBoxLayout()
        label_algorithm_79 = QLabel("                algorithm")
        label_algorithm_79.setPalette(palette_object)
        label_algorithm_79.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_79.addWidget(label_algorithm_79)

        box_algorithm_79 = QComboBox()
        box_algorithm_79.local_path = "integration.background.glm.model.algorithm"
        box_algorithm_79.tmp_lst=[]
        box_algorithm_79.tmp_lst.append("constant2d")
        box_algorithm_79.tmp_lst.append("constant3d")
        box_algorithm_79.tmp_lst.append("loglinear2d")
        box_algorithm_79.tmp_lst.append("loglinear3d")
        for lst_itm in box_algorithm_79.tmp_lst:
            box_algorithm_79.addItem(lst_itm)
        box_algorithm_79.setCurrentIndex(1)
        box_algorithm_79.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_79.addWidget(box_algorithm_79)
        bg_box.addLayout(hbox_lay_algorithm_79)

        label_80 = QLabel("        const_d")
        label_80.setPalette(palette_scope)
        label_80.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_80)

        label_81 = QLabel("    centroid")
        label_81.setPalette(palette_scope)
        label_81.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_81)

        hbox_lay_algorithm_82 =  QHBoxLayout()
        label_algorithm_82 = QLabel("        algorithm")
        label_algorithm_82.setPalette(palette_object)
        label_algorithm_82.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_82.addWidget(label_algorithm_82)

        box_algorithm_82 = QComboBox()
        box_algorithm_82.local_path = "integration.centroid.algorithm"
        box_algorithm_82.tmp_lst=[]
        box_algorithm_82.tmp_lst.append("simple")
        for lst_itm in box_algorithm_82.tmp_lst:
            box_algorithm_82.addItem(lst_itm)
        box_algorithm_82.setCurrentIndex(0)
        box_algorithm_82.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_82.addWidget(box_algorithm_82)
        bg_box.addLayout(hbox_lay_algorithm_82)

        label_83 = QLabel("profile")
        label_83.setPalette(palette_scope)
        label_83.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_83)

        hbox_lay_algorithm_84 =  QHBoxLayout()
        label_algorithm_84 = QLabel("    algorithm")
        label_algorithm_84.setPalette(palette_object)
        label_algorithm_84.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_84.addWidget(label_algorithm_84)

        box_algorithm_84 = QComboBox()
        box_algorithm_84.local_path = "profile.algorithm"
        box_algorithm_84.tmp_lst=[]
        box_algorithm_84.tmp_lst.append("gaussian_rs")
        for lst_itm in box_algorithm_84.tmp_lst:
            box_algorithm_84.addItem(lst_itm)
        box_algorithm_84.setCurrentIndex(0)
        box_algorithm_84.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_84.addWidget(box_algorithm_84)
        bg_box.addLayout(hbox_lay_algorithm_84)

        label_85 = QLabel("    gaussian_rs")
        label_85.setPalette(palette_scope)
        label_85.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_85)

        hbox_lay_scan_varying_86 =  QHBoxLayout()
        label_scan_varying_86 = QLabel("        scan_varying")
        label_scan_varying_86.setPalette(palette_object)
        label_scan_varying_86.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_86.addWidget(label_scan_varying_86)

        box_scan_varying_86 = QComboBox()
        box_scan_varying_86.local_path = "profile.gaussian_rs.scan_varying"
        box_scan_varying_86.tmp_lst=[]
        box_scan_varying_86.tmp_lst.append("True")
        box_scan_varying_86.tmp_lst.append("False")
        for lst_itm in box_scan_varying_86.tmp_lst:
            box_scan_varying_86.addItem(lst_itm)
        box_scan_varying_86.setCurrentIndex(1)
        box_scan_varying_86.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_86.addWidget(box_scan_varying_86)
        bg_box.addLayout(hbox_lay_scan_varying_86)

        label_87 = QLabel("        min_spots")
        label_87.setPalette(palette_scope)
        label_87.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_87)

        hbox_lay_overall_88 =  QHBoxLayout()
        label_overall_88 = QLabel("            overall")
        label_overall_88.setPalette(palette_object)
        label_overall_88.setFont(QFont("Monospace", 10))
        hbox_lay_overall_88.addWidget(label_overall_88)

        box_overall_88 = QSpinBox()
        box_overall_88.setValue(100)
        box_overall_88.local_path = "profile.gaussian_rs.min_spots.overall"
        box_overall_88.valueChanged.connect(self.spnbox_changed)
        hbox_lay_overall_88.addWidget(box_overall_88)
        bg_box.addLayout(hbox_lay_overall_88)

        hbox_lay_per_degree_89 =  QHBoxLayout()
        label_per_degree_89 = QLabel("            per_degree")
        label_per_degree_89.setPalette(palette_object)
        label_per_degree_89.setFont(QFont("Monospace", 10))
        hbox_lay_per_degree_89.addWidget(label_per_degree_89)

        box_per_degree_89 = QSpinBox()
        box_per_degree_89.setValue(50)
        box_per_degree_89.local_path = "profile.gaussian_rs.min_spots.per_degree"
        box_per_degree_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_per_degree_89.addWidget(box_per_degree_89)
        bg_box.addLayout(hbox_lay_per_degree_89)

        label_90 = QLabel("        filter")
        label_90.setPalette(palette_scope)
        label_90.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_90)

        hbox_lay_min_zeta_91 =  QHBoxLayout()
        label_min_zeta_91 = QLabel("            min_zeta")
        label_min_zeta_91.setPalette(palette_object)
        label_min_zeta_91.setFont(QFont("Monospace", 10))
        hbox_lay_min_zeta_91.addWidget(label_min_zeta_91)

        box_min_zeta_91 = QDoubleSpinBox()
        box_min_zeta_91.setValue(0.05)
        box_min_zeta_91.local_path = "profile.gaussian_rs.filter.min_zeta"
        box_min_zeta_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_zeta_91.addWidget(box_min_zeta_91)
        bg_box.addLayout(hbox_lay_min_zeta_91)

        label_92 = QLabel("        fitting")
        label_92.setPalette(palette_scope)
        label_92.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_92)

        hbox_lay_scan_step_93 =  QHBoxLayout()
        label_scan_step_93 = QLabel("            scan_step")
        label_scan_step_93.setPalette(palette_object)
        label_scan_step_93.setFont(QFont("Monospace", 10))
        hbox_lay_scan_step_93.addWidget(label_scan_step_93)

        box_scan_step_93 = QDoubleSpinBox()
        box_scan_step_93.setValue(5.0)
        box_scan_step_93.local_path = "profile.gaussian_rs.fitting.scan_step"
        box_scan_step_93.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_step_93.addWidget(box_scan_step_93)
        bg_box.addLayout(hbox_lay_scan_step_93)

        hbox_lay_grid_size_94 =  QHBoxLayout()
        label_grid_size_94 = QLabel("            grid_size")
        label_grid_size_94.setPalette(palette_object)
        label_grid_size_94.setFont(QFont("Monospace", 10))
        hbox_lay_grid_size_94.addWidget(label_grid_size_94)

        box_grid_size_94 = QSpinBox()
        box_grid_size_94.setValue(5)
        box_grid_size_94.local_path = "profile.gaussian_rs.fitting.grid_size"
        box_grid_size_94.valueChanged.connect(self.spnbox_changed)
        hbox_lay_grid_size_94.addWidget(box_grid_size_94)
        bg_box.addLayout(hbox_lay_grid_size_94)

        hbox_lay_threshold_95 =  QHBoxLayout()
        label_threshold_95 = QLabel("            threshold")
        label_threshold_95.setPalette(palette_object)
        label_threshold_95.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_95.addWidget(label_threshold_95)

        box_threshold_95 = QDoubleSpinBox()
        box_threshold_95.setValue(0.02)
        box_threshold_95.local_path = "profile.gaussian_rs.fitting.threshold"
        box_threshold_95.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_95.addWidget(box_threshold_95)
        bg_box.addLayout(hbox_lay_threshold_95)

        hbox_lay_grid_method_96 =  QHBoxLayout()
        label_grid_method_96 = QLabel("            grid_method")
        label_grid_method_96.setPalette(palette_object)
        label_grid_method_96.setFont(QFont("Monospace", 10))
        hbox_lay_grid_method_96.addWidget(label_grid_method_96)

        box_grid_method_96 = QComboBox()
        box_grid_method_96.local_path = "profile.gaussian_rs.fitting.grid_method"
        box_grid_method_96.tmp_lst=[]
        box_grid_method_96.tmp_lst.append("single")
        box_grid_method_96.tmp_lst.append("regular_grid")
        box_grid_method_96.tmp_lst.append("circular_grid")
        for lst_itm in box_grid_method_96.tmp_lst:
            box_grid_method_96.addItem(lst_itm)
        box_grid_method_96.setCurrentIndex(1)
        box_grid_method_96.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_grid_method_96.addWidget(box_grid_method_96)
        bg_box.addLayout(hbox_lay_grid_method_96)

        hbox_lay_fit_method_97 =  QHBoxLayout()
        label_fit_method_97 = QLabel("            fit_method")
        label_fit_method_97.setPalette(palette_object)
        label_fit_method_97.setFont(QFont("Monospace", 10))
        hbox_lay_fit_method_97.addWidget(label_fit_method_97)

        box_fit_method_97 = QComboBox()
        box_fit_method_97.local_path = "profile.gaussian_rs.fitting.fit_method"
        box_fit_method_97.tmp_lst=[]
        box_fit_method_97.tmp_lst.append("reciprocal_space")
        box_fit_method_97.tmp_lst.append("detector_space")
        for lst_itm in box_fit_method_97.tmp_lst:
            box_fit_method_97.addItem(lst_itm)
        box_fit_method_97.setCurrentIndex(0)
        box_fit_method_97.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fit_method_97.addWidget(box_fit_method_97)
        bg_box.addLayout(hbox_lay_fit_method_97)

        label_98 = QLabel("prediction")
        label_98.setPalette(palette_scope)
        label_98.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_98)

        hbox_lay_d_min_99 =  QHBoxLayout()
        label_d_min_99 = QLabel("    d_min")
        label_d_min_99.setPalette(palette_object)
        label_d_min_99.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_99.addWidget(label_d_min_99)

        box_d_min_99 = QDoubleSpinBox()
        box_d_min_99.local_path = "prediction.d_min"
        box_d_min_99.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_99.addWidget(box_d_min_99)
        bg_box.addLayout(hbox_lay_d_min_99)

        hbox_lay_d_max_100 =  QHBoxLayout()
        label_d_max_100 = QLabel("    d_max")
        label_d_max_100.setPalette(palette_object)
        label_d_max_100.setFont(QFont("Monospace", 10))
        hbox_lay_d_max_100.addWidget(label_d_max_100)

        box_d_max_100 = QDoubleSpinBox()
        box_d_max_100.local_path = "prediction.d_max"
        box_d_max_100.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_100.addWidget(box_d_max_100)
        bg_box.addLayout(hbox_lay_d_max_100)

        hbox_lay_margin_101 =  QHBoxLayout()
        label_margin_101 = QLabel("    margin")
        label_margin_101.setPalette(palette_object)
        label_margin_101.setFont(QFont("Monospace", 10))
        hbox_lay_margin_101.addWidget(label_margin_101)

        box_margin_101 = QSpinBox()
        box_margin_101.setValue(1)
        box_margin_101.local_path = "prediction.margin"
        box_margin_101.valueChanged.connect(self.spnbox_changed)
        hbox_lay_margin_101.addWidget(box_margin_101)
        bg_box.addLayout(hbox_lay_margin_101)

        hbox_lay_force_static_102 =  QHBoxLayout()
        label_force_static_102 = QLabel("    force_static")
        label_force_static_102.setPalette(palette_object)
        label_force_static_102.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_102.addWidget(label_force_static_102)

        box_force_static_102 = QComboBox()
        box_force_static_102.local_path = "prediction.force_static"
        box_force_static_102.tmp_lst=[]
        box_force_static_102.tmp_lst.append("True")
        box_force_static_102.tmp_lst.append("False")
        for lst_itm in box_force_static_102.tmp_lst:
            box_force_static_102.addItem(lst_itm)
        box_force_static_102.setCurrentIndex(1)
        box_force_static_102.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_102.addWidget(box_force_static_102)
        bg_box.addLayout(hbox_lay_force_static_102)

 
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
