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

        label_9 = QLabel("sampling")
        label_9.setPalette(palette_scope)
        label_9.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_9)

        hbox_lay_reflections_per_degree_10 =  QHBoxLayout()
        label_reflections_per_degree_10 = QLabel("    reflections_per_degree")
        label_reflections_per_degree_10.setPalette(palette_object)
        label_reflections_per_degree_10.setFont(QFont("Monospace", 10))
        hbox_lay_reflections_per_degree_10.addWidget(label_reflections_per_degree_10)

        box_reflections_per_degree_10 = QDoubleSpinBox()
        box_reflections_per_degree_10.setValue(50.0)
        box_reflections_per_degree_10.local_path = "sampling.reflections_per_degree"
        box_reflections_per_degree_10.valueChanged.connect(self.spnbox_changed)
        hbox_lay_reflections_per_degree_10.addWidget(box_reflections_per_degree_10)
        bg_box.addLayout(hbox_lay_reflections_per_degree_10)

        hbox_lay_minimum_sample_size_11 =  QHBoxLayout()
        label_minimum_sample_size_11 = QLabel("    minimum_sample_size")
        label_minimum_sample_size_11.setPalette(palette_object)
        label_minimum_sample_size_11.setFont(QFont("Monospace", 10))
        hbox_lay_minimum_sample_size_11.addWidget(label_minimum_sample_size_11)

        box_minimum_sample_size_11 = QSpinBox()
        box_minimum_sample_size_11.setValue(1000)
        box_minimum_sample_size_11.local_path = "sampling.minimum_sample_size"
        box_minimum_sample_size_11.valueChanged.connect(self.spnbox_changed)
        hbox_lay_minimum_sample_size_11.addWidget(box_minimum_sample_size_11)
        bg_box.addLayout(hbox_lay_minimum_sample_size_11)

        hbox_lay_maximum_sample_size_12 =  QHBoxLayout()
        label_maximum_sample_size_12 = QLabel("    maximum_sample_size")
        label_maximum_sample_size_12.setPalette(palette_object)
        label_maximum_sample_size_12.setFont(QFont("Monospace", 10))
        hbox_lay_maximum_sample_size_12.addWidget(label_maximum_sample_size_12)

        box_maximum_sample_size_12 = QSpinBox()
        box_maximum_sample_size_12.local_path = "sampling.maximum_sample_size"
        box_maximum_sample_size_12.valueChanged.connect(self.spnbox_changed)
        hbox_lay_maximum_sample_size_12.addWidget(box_maximum_sample_size_12)
        bg_box.addLayout(hbox_lay_maximum_sample_size_12)

        hbox_lay_integrate_all_reflections_13 =  QHBoxLayout()
        label_integrate_all_reflections_13 = QLabel("    integrate_all_reflections")
        label_integrate_all_reflections_13.setPalette(palette_object)
        label_integrate_all_reflections_13.setFont(QFont("Monospace", 10))
        hbox_lay_integrate_all_reflections_13.addWidget(label_integrate_all_reflections_13)

        box_integrate_all_reflections_13 = QComboBox()
        box_integrate_all_reflections_13.local_path = "sampling.integrate_all_reflections"
        box_integrate_all_reflections_13.tmp_lst=[]
        box_integrate_all_reflections_13.tmp_lst.append("True")
        box_integrate_all_reflections_13.tmp_lst.append("False")
        for lst_itm in box_integrate_all_reflections_13.tmp_lst:
            box_integrate_all_reflections_13.addItem(lst_itm)
        box_integrate_all_reflections_13.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_integrate_all_reflections_13.addWidget(box_integrate_all_reflections_13)
        bg_box.addLayout(hbox_lay_integrate_all_reflections_13)

        hbox_lay_verbosity_14 =  QHBoxLayout()
        label_verbosity_14 = QLabel("verbosity")
        label_verbosity_14.setPalette(palette_object)
        label_verbosity_14.setFont(QFont("Monospace", 10))
        hbox_lay_verbosity_14.addWidget(label_verbosity_14)

        box_verbosity_14 = QSpinBox()
        box_verbosity_14.setValue(1)
        box_verbosity_14.local_path = "verbosity"
        box_verbosity_14.valueChanged.connect(self.spnbox_changed)
        hbox_lay_verbosity_14.addWidget(box_verbosity_14)
        bg_box.addLayout(hbox_lay_verbosity_14)

        label_15 = QLabel("integration")
        label_15.setPalette(palette_scope)
        label_15.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_15)

        label_16 = QLabel("    mp")
        label_16.setPalette(palette_scope)
        label_16.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_16)

        hbox_lay_method_17 =  QHBoxLayout()
        label_method_17 = QLabel("        method")
        label_method_17.setPalette(palette_object)
        label_method_17.setFont(QFont("Monospace", 10))
        hbox_lay_method_17.addWidget(label_method_17)

        box_method_17 = QComboBox()
        box_method_17.local_path = "integration.mp.method"
        box_method_17.tmp_lst=[]
        box_method_17.tmp_lst.append("multiprocessing")
        box_method_17.tmp_lst.append("sge")
        box_method_17.tmp_lst.append("lsf")
        box_method_17.tmp_lst.append("pbs")
        for lst_itm in box_method_17.tmp_lst:
            box_method_17.addItem(lst_itm)
        box_method_17.setCurrentIndex(0)
        box_method_17.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_method_17.addWidget(box_method_17)
        bg_box.addLayout(hbox_lay_method_17)

        hbox_lay_nproc_18 =  QHBoxLayout()
        label_nproc_18 = QLabel("        nproc")
        label_nproc_18.setPalette(palette_object)
        label_nproc_18.setFont(QFont("Monospace", 10))
        hbox_lay_nproc_18.addWidget(label_nproc_18)

        box_nproc_18 = QSpinBox()
        box_nproc_18.setValue(1)
        box_nproc_18.local_path = "integration.mp.nproc"
        box_nproc_18.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc_18.addWidget(box_nproc_18)
        bg_box.addLayout(hbox_lay_nproc_18)

        hbox_lay_nthreads_19 =  QHBoxLayout()
        label_nthreads_19 = QLabel("        nthreads")
        label_nthreads_19.setPalette(palette_object)
        label_nthreads_19.setFont(QFont("Monospace", 10))
        hbox_lay_nthreads_19.addWidget(label_nthreads_19)

        box_nthreads_19 = QSpinBox()
        box_nthreads_19.setValue(1)
        box_nthreads_19.local_path = "integration.mp.nthreads"
        box_nthreads_19.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nthreads_19.addWidget(box_nthreads_19)
        bg_box.addLayout(hbox_lay_nthreads_19)

        label_20 = QLabel("    lookup")
        label_20.setPalette(palette_scope)
        label_20.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_20)

        hbox_lay_mask_21 =  QHBoxLayout()
        label_mask_21 = QLabel("        mask")
        label_mask_21.setPalette(palette_object)
        label_mask_21.setFont(QFont("Monospace", 10))
        hbox_lay_mask_21.addWidget(label_mask_21)

        box_mask_21 = QLineEdit()
        box_mask_21.local_path = "integration.lookup.mask"
        box_mask_21.textChanged.connect(self.spnbox_changed)
        hbox_lay_mask_21.addWidget(box_mask_21)
        bg_box.addLayout(hbox_lay_mask_21)

        label_22 = QLabel("    block")
        label_22.setPalette(palette_scope)
        label_22.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_22)

        hbox_lay_size_23 =  QHBoxLayout()
        label_size_23 = QLabel("        size")
        label_size_23.setPalette(palette_object)
        label_size_23.setFont(QFont("Monospace", 10))
        hbox_lay_size_23.addWidget(label_size_23)

        box_size_23 = QDoubleSpinBox()
        box_size_23.local_path = "integration.block.size"
        box_size_23.valueChanged.connect(self.spnbox_changed)
        hbox_lay_size_23.addWidget(box_size_23)
        bg_box.addLayout(hbox_lay_size_23)

        hbox_lay_units_24 =  QHBoxLayout()
        label_units_24 = QLabel("        units")
        label_units_24.setPalette(palette_object)
        label_units_24.setFont(QFont("Monospace", 10))
        hbox_lay_units_24.addWidget(label_units_24)

        box_units_24 = QComboBox()
        box_units_24.local_path = "integration.block.units"
        box_units_24.tmp_lst=[]
        box_units_24.tmp_lst.append("degrees")
        box_units_24.tmp_lst.append("radians")
        box_units_24.tmp_lst.append("frames")
        for lst_itm in box_units_24.tmp_lst:
            box_units_24.addItem(lst_itm)
        box_units_24.setCurrentIndex(0)
        box_units_24.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_units_24.addWidget(box_units_24)
        bg_box.addLayout(hbox_lay_units_24)

        hbox_lay_threshold_25 =  QHBoxLayout()
        label_threshold_25 = QLabel("        threshold")
        label_threshold_25.setPalette(palette_object)
        label_threshold_25.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_25.addWidget(label_threshold_25)

        box_threshold_25 = QDoubleSpinBox()
        box_threshold_25.setValue(0.99)
        box_threshold_25.local_path = "integration.block.threshold"
        box_threshold_25.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_25.addWidget(box_threshold_25)
        bg_box.addLayout(hbox_lay_threshold_25)

        hbox_lay_force_26 =  QHBoxLayout()
        label_force_26 = QLabel("        force")
        label_force_26.setPalette(palette_object)
        label_force_26.setFont(QFont("Monospace", 10))
        hbox_lay_force_26.addWidget(label_force_26)

        box_force_26 = QComboBox()
        box_force_26.local_path = "integration.block.force"
        box_force_26.tmp_lst=[]
        box_force_26.tmp_lst.append("True")
        box_force_26.tmp_lst.append("False")
        for lst_itm in box_force_26.tmp_lst:
            box_force_26.addItem(lst_itm)
        box_force_26.setCurrentIndex(1)
        box_force_26.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_26.addWidget(box_force_26)
        bg_box.addLayout(hbox_lay_force_26)

        hbox_lay_max_memory_usage_27 =  QHBoxLayout()
        label_max_memory_usage_27 = QLabel("        max_memory_usage")
        label_max_memory_usage_27.setPalette(palette_object)
        label_max_memory_usage_27.setFont(QFont("Monospace", 10))
        hbox_lay_max_memory_usage_27.addWidget(label_max_memory_usage_27)

        box_max_memory_usage_27 = QDoubleSpinBox()
        box_max_memory_usage_27.setValue(0.75)
        box_max_memory_usage_27.local_path = "integration.block.max_memory_usage"
        box_max_memory_usage_27.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_memory_usage_27.addWidget(box_max_memory_usage_27)
        bg_box.addLayout(hbox_lay_max_memory_usage_27)

        label_28 = QLabel("    debug")
        label_28.setPalette(palette_scope)
        label_28.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_28)

        label_29 = QLabel("        reference")
        label_29.setPalette(palette_scope)
        label_29.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_29)

        hbox_lay_output_30 =  QHBoxLayout()
        label_output_30 = QLabel("            output")
        label_output_30.setPalette(palette_object)
        label_output_30.setFont(QFont("Monospace", 10))
        hbox_lay_output_30.addWidget(label_output_30)

        box_output_30 = QComboBox()
        box_output_30.local_path = "integration.debug.reference.output"
        box_output_30.tmp_lst=[]
        box_output_30.tmp_lst.append("True")
        box_output_30.tmp_lst.append("False")
        for lst_itm in box_output_30.tmp_lst:
            box_output_30.addItem(lst_itm)
        box_output_30.setCurrentIndex(1)
        box_output_30.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_output_30.addWidget(box_output_30)
        bg_box.addLayout(hbox_lay_output_30)

        hbox_lay_during_31 =  QHBoxLayout()
        label_during_31 = QLabel("        during")
        label_during_31.setPalette(palette_object)
        label_during_31.setFont(QFont("Monospace", 10))
        hbox_lay_during_31.addWidget(label_during_31)

        box_during_31 = QComboBox()
        box_during_31.local_path = "integration.debug.during"
        box_during_31.tmp_lst=[]
        box_during_31.tmp_lst.append("modelling")
        box_during_31.tmp_lst.append("integration")
        for lst_itm in box_during_31.tmp_lst:
            box_during_31.addItem(lst_itm)
        box_during_31.setCurrentIndex(1)
        box_during_31.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_during_31.addWidget(box_during_31)
        bg_box.addLayout(hbox_lay_during_31)

        hbox_lay_output_32 =  QHBoxLayout()
        label_output_32 = QLabel("        output")
        label_output_32.setPalette(palette_object)
        label_output_32.setFont(QFont("Monospace", 10))
        hbox_lay_output_32.addWidget(label_output_32)

        box_output_32 = QComboBox()
        box_output_32.local_path = "integration.debug.output"
        box_output_32.tmp_lst=[]
        box_output_32.tmp_lst.append("True")
        box_output_32.tmp_lst.append("False")
        for lst_itm in box_output_32.tmp_lst:
            box_output_32.addItem(lst_itm)
        box_output_32.setCurrentIndex(1)
        box_output_32.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_output_32.addWidget(box_output_32)
        bg_box.addLayout(hbox_lay_output_32)

        hbox_lay_separate_files_33 =  QHBoxLayout()
        label_separate_files_33 = QLabel("        separate_files")
        label_separate_files_33.setPalette(palette_object)
        label_separate_files_33.setFont(QFont("Monospace", 10))
        hbox_lay_separate_files_33.addWidget(label_separate_files_33)

        box_separate_files_33 = QComboBox()
        box_separate_files_33.local_path = "integration.debug.separate_files"
        box_separate_files_33.tmp_lst=[]
        box_separate_files_33.tmp_lst.append("True")
        box_separate_files_33.tmp_lst.append("False")
        for lst_itm in box_separate_files_33.tmp_lst:
            box_separate_files_33.addItem(lst_itm)
        box_separate_files_33.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_separate_files_33.addWidget(box_separate_files_33)
        bg_box.addLayout(hbox_lay_separate_files_33)


        hbox_lay_split_experiments_35 =  QHBoxLayout()
        label_split_experiments_35 = QLabel("        split_experiments")
        label_split_experiments_35.setPalette(palette_object)
        label_split_experiments_35.setFont(QFont("Monospace", 10))
        hbox_lay_split_experiments_35.addWidget(label_split_experiments_35)

        box_split_experiments_35 = QComboBox()
        box_split_experiments_35.local_path = "integration.debug.split_experiments"
        box_split_experiments_35.tmp_lst=[]
        box_split_experiments_35.tmp_lst.append("True")
        box_split_experiments_35.tmp_lst.append("False")
        for lst_itm in box_split_experiments_35.tmp_lst:
            box_split_experiments_35.addItem(lst_itm)
        box_split_experiments_35.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_split_experiments_35.addWidget(box_split_experiments_35)
        bg_box.addLayout(hbox_lay_split_experiments_35)

        hbox_lay_integrator_36 =  QHBoxLayout()
        label_integrator_36 = QLabel("    integrator")
        label_integrator_36.setPalette(palette_object)
        label_integrator_36.setFont(QFont("Monospace", 10))
        hbox_lay_integrator_36.addWidget(label_integrator_36)

        box_integrator_36 = QComboBox()
        box_integrator_36.local_path = "integration.integrator"
        box_integrator_36.tmp_lst=[]
        box_integrator_36.tmp_lst.append("auto")
        box_integrator_36.tmp_lst.append("3d")
        box_integrator_36.tmp_lst.append("flat3d")
        box_integrator_36.tmp_lst.append("2d")
        box_integrator_36.tmp_lst.append("single2d")
        box_integrator_36.tmp_lst.append("stills")
        for lst_itm in box_integrator_36.tmp_lst:
            box_integrator_36.addItem(lst_itm)
        box_integrator_36.setCurrentIndex(0)
        box_integrator_36.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_integrator_36.addWidget(box_integrator_36)
        bg_box.addLayout(hbox_lay_integrator_36)

        label_37 = QLabel("    profile")
        label_37.setPalette(palette_scope)
        label_37.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_37)

        hbox_lay_fitting_38 =  QHBoxLayout()
        label_fitting_38 = QLabel("        fitting")
        label_fitting_38.setPalette(palette_object)
        label_fitting_38.setFont(QFont("Monospace", 10))
        hbox_lay_fitting_38.addWidget(label_fitting_38)

        box_fitting_38 = QComboBox()
        box_fitting_38.local_path = "integration.profile.fitting"
        box_fitting_38.tmp_lst=[]
        box_fitting_38.tmp_lst.append("True")
        box_fitting_38.tmp_lst.append("False")
        for lst_itm in box_fitting_38.tmp_lst:
            box_fitting_38.addItem(lst_itm)
        box_fitting_38.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fitting_38.addWidget(box_fitting_38)
        bg_box.addLayout(hbox_lay_fitting_38)

        label_39 = QLabel("        validation")
        label_39.setPalette(palette_scope)
        label_39.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_39)

        hbox_lay_number_of_partitions_40 =  QHBoxLayout()
        label_number_of_partitions_40 = QLabel("            number_of_partitions")
        label_number_of_partitions_40.setPalette(palette_object)
        label_number_of_partitions_40.setFont(QFont("Monospace", 10))
        hbox_lay_number_of_partitions_40.addWidget(label_number_of_partitions_40)

        box_number_of_partitions_40 = QSpinBox()
        box_number_of_partitions_40.setValue(1)
        box_number_of_partitions_40.local_path = "integration.profile.validation.number_of_partitions"
        box_number_of_partitions_40.valueChanged.connect(self.spnbox_changed)
        hbox_lay_number_of_partitions_40.addWidget(box_number_of_partitions_40)
        bg_box.addLayout(hbox_lay_number_of_partitions_40)

        hbox_lay_min_partition_size_41 =  QHBoxLayout()
        label_min_partition_size_41 = QLabel("            min_partition_size")
        label_min_partition_size_41.setPalette(palette_object)
        label_min_partition_size_41.setFont(QFont("Monospace", 10))
        hbox_lay_min_partition_size_41.addWidget(label_min_partition_size_41)

        box_min_partition_size_41 = QSpinBox()
        box_min_partition_size_41.setValue(100)
        box_min_partition_size_41.local_path = "integration.profile.validation.min_partition_size"
        box_min_partition_size_41.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_partition_size_41.addWidget(box_min_partition_size_41)
        bg_box.addLayout(hbox_lay_min_partition_size_41)

        label_42 = QLabel("    filter")
        label_42.setPalette(palette_scope)
        label_42.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_42)

        hbox_lay_min_zeta_43 =  QHBoxLayout()
        label_min_zeta_43 = QLabel("        min_zeta")
        label_min_zeta_43.setPalette(palette_object)
        label_min_zeta_43.setFont(QFont("Monospace", 10))
        hbox_lay_min_zeta_43.addWidget(label_min_zeta_43)

        box_min_zeta_43 = QDoubleSpinBox()
        box_min_zeta_43.setValue(0.05)
        box_min_zeta_43.local_path = "integration.filter.min_zeta"
        box_min_zeta_43.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_zeta_43.addWidget(box_min_zeta_43)
        bg_box.addLayout(hbox_lay_min_zeta_43)

        hbox_lay_max_shoebox_overlap_44 =  QHBoxLayout()
        label_max_shoebox_overlap_44 = QLabel("        max_shoebox_overlap")
        label_max_shoebox_overlap_44.setPalette(palette_object)
        label_max_shoebox_overlap_44.setFont(QFont("Monospace", 10))
        hbox_lay_max_shoebox_overlap_44.addWidget(label_max_shoebox_overlap_44)

        box_max_shoebox_overlap_44 = QDoubleSpinBox()
        box_max_shoebox_overlap_44.setValue(1.0)
        box_max_shoebox_overlap_44.local_path = "integration.filter.max_shoebox_overlap"
        box_max_shoebox_overlap_44.valueChanged.connect(self.spnbox_changed)
        hbox_lay_max_shoebox_overlap_44.addWidget(box_max_shoebox_overlap_44)
        bg_box.addLayout(hbox_lay_max_shoebox_overlap_44)

        label_45 = QLabel("        powder")
        label_45.setPalette(palette_scope)
        label_45.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_45)

        label_46 = QLabel("            water_ice")
        label_46.setPalette(palette_scope)
        label_46.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_46)



        hbox_lay_d_min_49 =  QHBoxLayout()
        label_d_min_49 = QLabel("                d_min")
        label_d_min_49.setPalette(palette_object)
        label_d_min_49.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_49.addWidget(label_d_min_49)

        box_d_min_49 = QDoubleSpinBox()
        box_d_min_49.setValue(1.0)
        box_d_min_49.local_path = "integration.filter.powder.water_ice.d_min"
        box_d_min_49.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_49.addWidget(box_d_min_49)
        bg_box.addLayout(hbox_lay_d_min_49)

        hbox_lay_width_50 =  QHBoxLayout()
        label_width_50 = QLabel("                width")
        label_width_50.setPalette(palette_object)
        label_width_50.setFont(QFont("Monospace", 10))
        hbox_lay_width_50.addWidget(label_width_50)

        box_width_50 = QDoubleSpinBox()
        box_width_50.setValue(0.06)
        box_width_50.local_path = "integration.filter.powder.water_ice.width"
        box_width_50.valueChanged.connect(self.spnbox_changed)
        hbox_lay_width_50.addWidget(box_width_50)
        bg_box.addLayout(hbox_lay_width_50)

        hbox_lay_apply_51 =  QHBoxLayout()
        label_apply_51 = QLabel("            apply")
        label_apply_51.setPalette(palette_object)
        label_apply_51.setFont(QFont("Monospace", 10))
        hbox_lay_apply_51.addWidget(label_apply_51)

        box_apply_51 = QComboBox()
        box_apply_51.local_path = "integration.filter.powder.apply"
        box_apply_51.tmp_lst=[]
        box_apply_51.tmp_lst.append("none")
        box_apply_51.tmp_lst.append("water_ice")
        for lst_itm in box_apply_51.tmp_lst:
            box_apply_51.addItem(lst_itm)
        box_apply_51.setCurrentIndex(0)
        box_apply_51.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_apply_51.addWidget(box_apply_51)
        bg_box.addLayout(hbox_lay_apply_51)

        label_52 = QLabel("    background")
        label_52.setPalette(palette_scope)
        label_52.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_52)

        hbox_lay_algorithm_53 =  QHBoxLayout()
        label_algorithm_53 = QLabel("        algorithm")
        label_algorithm_53.setPalette(palette_object)
        label_algorithm_53.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_53.addWidget(label_algorithm_53)

        box_algorithm_53 = QComboBox()
        box_algorithm_53.local_path = "integration.background.algorithm"
        box_algorithm_53.tmp_lst=[]
        box_algorithm_53.tmp_lst.append("simple")
        box_algorithm_53.tmp_lst.append("null")
        box_algorithm_53.tmp_lst.append("glm")
        box_algorithm_53.tmp_lst.append("const_d")
        for lst_itm in box_algorithm_53.tmp_lst:
            box_algorithm_53.addItem(lst_itm)
        box_algorithm_53.setCurrentIndex(2)
        box_algorithm_53.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_53.addWidget(box_algorithm_53)
        bg_box.addLayout(hbox_lay_algorithm_53)

        label_54 = QLabel("        simple")
        label_54.setPalette(palette_scope)
        label_54.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_54)

        label_55 = QLabel("            outlier")
        label_55.setPalette(palette_scope)
        label_55.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_55)

        hbox_lay_algorithm_56 =  QHBoxLayout()
        label_algorithm_56 = QLabel("                algorithm")
        label_algorithm_56.setPalette(palette_object)
        label_algorithm_56.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_56.addWidget(label_algorithm_56)

        box_algorithm_56 = QComboBox()
        box_algorithm_56.local_path = "integration.background.simple.outlier.algorithm"
        box_algorithm_56.tmp_lst=[]
        box_algorithm_56.tmp_lst.append("null")
        box_algorithm_56.tmp_lst.append("nsigma")
        box_algorithm_56.tmp_lst.append("truncated")
        box_algorithm_56.tmp_lst.append("normal")
        box_algorithm_56.tmp_lst.append("mosflm")
        box_algorithm_56.tmp_lst.append("tukey")
        for lst_itm in box_algorithm_56.tmp_lst:
            box_algorithm_56.addItem(lst_itm)
        box_algorithm_56.setCurrentIndex(1)
        box_algorithm_56.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_56.addWidget(box_algorithm_56)
        bg_box.addLayout(hbox_lay_algorithm_56)

        label_57 = QLabel("                nsigma")
        label_57.setPalette(palette_scope)
        label_57.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_57)

        hbox_lay_lower_58 =  QHBoxLayout()
        label_lower_58 = QLabel("                    lower")
        label_lower_58.setPalette(palette_object)
        label_lower_58.setFont(QFont("Monospace", 10))
        hbox_lay_lower_58.addWidget(label_lower_58)

        box_lower_58 = QDoubleSpinBox()
        box_lower_58.setValue(3.0)
        box_lower_58.local_path = "integration.background.simple.outlier.nsigma.lower"
        box_lower_58.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_58.addWidget(box_lower_58)
        bg_box.addLayout(hbox_lay_lower_58)

        hbox_lay_upper_59 =  QHBoxLayout()
        label_upper_59 = QLabel("                    upper")
        label_upper_59.setPalette(palette_object)
        label_upper_59.setFont(QFont("Monospace", 10))
        hbox_lay_upper_59.addWidget(label_upper_59)

        box_upper_59 = QDoubleSpinBox()
        box_upper_59.setValue(3.0)
        box_upper_59.local_path = "integration.background.simple.outlier.nsigma.upper"
        box_upper_59.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_59.addWidget(box_upper_59)
        bg_box.addLayout(hbox_lay_upper_59)

        label_60 = QLabel("                truncated")
        label_60.setPalette(palette_scope)
        label_60.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_60)

        hbox_lay_lower_61 =  QHBoxLayout()
        label_lower_61 = QLabel("                    lower")
        label_lower_61.setPalette(palette_object)
        label_lower_61.setFont(QFont("Monospace", 10))
        hbox_lay_lower_61.addWidget(label_lower_61)

        box_lower_61 = QDoubleSpinBox()
        box_lower_61.setValue(0.01)
        box_lower_61.local_path = "integration.background.simple.outlier.truncated.lower"
        box_lower_61.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_61.addWidget(box_lower_61)
        bg_box.addLayout(hbox_lay_lower_61)

        hbox_lay_upper_62 =  QHBoxLayout()
        label_upper_62 = QLabel("                    upper")
        label_upper_62.setPalette(palette_object)
        label_upper_62.setFont(QFont("Monospace", 10))
        hbox_lay_upper_62.addWidget(label_upper_62)

        box_upper_62 = QDoubleSpinBox()
        box_upper_62.setValue(0.01)
        box_upper_62.local_path = "integration.background.simple.outlier.truncated.upper"
        box_upper_62.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_62.addWidget(box_upper_62)
        bg_box.addLayout(hbox_lay_upper_62)

        label_63 = QLabel("                normal")
        label_63.setPalette(palette_scope)
        label_63.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_63)

        hbox_lay_min_pixels_64 =  QHBoxLayout()
        label_min_pixels_64 = QLabel("                    min_pixels")
        label_min_pixels_64.setPalette(palette_object)
        label_min_pixels_64.setFont(QFont("Monospace", 10))
        hbox_lay_min_pixels_64.addWidget(label_min_pixels_64)

        box_min_pixels_64 = QSpinBox()
        box_min_pixels_64.setValue(10)
        box_min_pixels_64.local_path = "integration.background.simple.outlier.normal.min_pixels"
        box_min_pixels_64.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_pixels_64.addWidget(box_min_pixels_64)
        bg_box.addLayout(hbox_lay_min_pixels_64)

        label_65 = QLabel("                mosflm")
        label_65.setPalette(palette_scope)
        label_65.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_65)

        hbox_lay_fraction_66 =  QHBoxLayout()
        label_fraction_66 = QLabel("                    fraction")
        label_fraction_66.setPalette(palette_object)
        label_fraction_66.setFont(QFont("Monospace", 10))
        hbox_lay_fraction_66.addWidget(label_fraction_66)

        box_fraction_66 = QDoubleSpinBox()
        box_fraction_66.setValue(1.0)
        box_fraction_66.local_path = "integration.background.simple.outlier.mosflm.fraction"
        box_fraction_66.valueChanged.connect(self.spnbox_changed)
        hbox_lay_fraction_66.addWidget(box_fraction_66)
        bg_box.addLayout(hbox_lay_fraction_66)

        hbox_lay_n_sigma_67 =  QHBoxLayout()
        label_n_sigma_67 = QLabel("                    n_sigma")
        label_n_sigma_67.setPalette(palette_object)
        label_n_sigma_67.setFont(QFont("Monospace", 10))
        hbox_lay_n_sigma_67.addWidget(label_n_sigma_67)

        box_n_sigma_67 = QDoubleSpinBox()
        box_n_sigma_67.setValue(4.0)
        box_n_sigma_67.local_path = "integration.background.simple.outlier.mosflm.n_sigma"
        box_n_sigma_67.valueChanged.connect(self.spnbox_changed)
        hbox_lay_n_sigma_67.addWidget(box_n_sigma_67)
        bg_box.addLayout(hbox_lay_n_sigma_67)

        label_68 = QLabel("                tukey")
        label_68.setPalette(palette_scope)
        label_68.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_68)

        hbox_lay_lower_69 =  QHBoxLayout()
        label_lower_69 = QLabel("                    lower")
        label_lower_69.setPalette(palette_object)
        label_lower_69.setFont(QFont("Monospace", 10))
        hbox_lay_lower_69.addWidget(label_lower_69)

        box_lower_69 = QDoubleSpinBox()
        box_lower_69.setValue(1.5)
        box_lower_69.local_path = "integration.background.simple.outlier.tukey.lower"
        box_lower_69.valueChanged.connect(self.spnbox_changed)
        hbox_lay_lower_69.addWidget(box_lower_69)
        bg_box.addLayout(hbox_lay_lower_69)

        hbox_lay_upper_70 =  QHBoxLayout()
        label_upper_70 = QLabel("                    upper")
        label_upper_70.setPalette(palette_object)
        label_upper_70.setFont(QFont("Monospace", 10))
        hbox_lay_upper_70.addWidget(label_upper_70)

        box_upper_70 = QDoubleSpinBox()
        box_upper_70.setValue(1.5)
        box_upper_70.local_path = "integration.background.simple.outlier.tukey.upper"
        box_upper_70.valueChanged.connect(self.spnbox_changed)
        hbox_lay_upper_70.addWidget(box_upper_70)
        bg_box.addLayout(hbox_lay_upper_70)

        label_71 = QLabel("            model")
        label_71.setPalette(palette_scope)
        label_71.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_71)

        hbox_lay_algorithm_72 =  QHBoxLayout()
        label_algorithm_72 = QLabel("                algorithm")
        label_algorithm_72.setPalette(palette_object)
        label_algorithm_72.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_72.addWidget(label_algorithm_72)

        box_algorithm_72 = QComboBox()
        box_algorithm_72.local_path = "integration.background.simple.model.algorithm"
        box_algorithm_72.tmp_lst=[]
        box_algorithm_72.tmp_lst.append("constant2d")
        box_algorithm_72.tmp_lst.append("constant3d")
        box_algorithm_72.tmp_lst.append("linear2d")
        box_algorithm_72.tmp_lst.append("linear3d")
        for lst_itm in box_algorithm_72.tmp_lst:
            box_algorithm_72.addItem(lst_itm)
        box_algorithm_72.setCurrentIndex(1)
        box_algorithm_72.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_72.addWidget(box_algorithm_72)
        bg_box.addLayout(hbox_lay_algorithm_72)

        label_73 = QLabel("        glm")
        label_73.setPalette(palette_scope)
        label_73.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_73)

        label_74 = QLabel("            robust")
        label_74.setPalette(palette_scope)
        label_74.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_74)

        hbox_lay_tuning_constant_75 =  QHBoxLayout()
        label_tuning_constant_75 = QLabel("                tuning_constant")
        label_tuning_constant_75.setPalette(palette_object)
        label_tuning_constant_75.setFont(QFont("Monospace", 10))
        hbox_lay_tuning_constant_75.addWidget(label_tuning_constant_75)

        box_tuning_constant_75 = QDoubleSpinBox()
        box_tuning_constant_75.setValue(1.345)
        box_tuning_constant_75.local_path = "integration.background.glm.robust.tuning_constant"
        box_tuning_constant_75.valueChanged.connect(self.spnbox_changed)
        hbox_lay_tuning_constant_75.addWidget(box_tuning_constant_75)
        bg_box.addLayout(hbox_lay_tuning_constant_75)

        label_76 = QLabel("            model")
        label_76.setPalette(palette_scope)
        label_76.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_76)

        hbox_lay_algorithm_77 =  QHBoxLayout()
        label_algorithm_77 = QLabel("                algorithm")
        label_algorithm_77.setPalette(palette_object)
        label_algorithm_77.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_77.addWidget(label_algorithm_77)

        box_algorithm_77 = QComboBox()
        box_algorithm_77.local_path = "integration.background.glm.model.algorithm"
        box_algorithm_77.tmp_lst=[]
        box_algorithm_77.tmp_lst.append("constant2d")
        box_algorithm_77.tmp_lst.append("constant3d")
        box_algorithm_77.tmp_lst.append("loglinear2d")
        box_algorithm_77.tmp_lst.append("loglinear3d")
        for lst_itm in box_algorithm_77.tmp_lst:
            box_algorithm_77.addItem(lst_itm)
        box_algorithm_77.setCurrentIndex(1)
        box_algorithm_77.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_77.addWidget(box_algorithm_77)
        bg_box.addLayout(hbox_lay_algorithm_77)

        label_78 = QLabel("        const_d")
        label_78.setPalette(palette_scope)
        label_78.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_78)

        label_79 = QLabel("    centroid")
        label_79.setPalette(palette_scope)
        label_79.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_79)

        hbox_lay_algorithm_80 =  QHBoxLayout()
        label_algorithm_80 = QLabel("        algorithm")
        label_algorithm_80.setPalette(palette_object)
        label_algorithm_80.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_80.addWidget(label_algorithm_80)

        box_algorithm_80 = QComboBox()
        box_algorithm_80.local_path = "integration.centroid.algorithm"
        box_algorithm_80.tmp_lst=[]
        box_algorithm_80.tmp_lst.append("simple")
        for lst_itm in box_algorithm_80.tmp_lst:
            box_algorithm_80.addItem(lst_itm)
        box_algorithm_80.setCurrentIndex(0)
        box_algorithm_80.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_80.addWidget(box_algorithm_80)
        bg_box.addLayout(hbox_lay_algorithm_80)

        label_81 = QLabel("profile")
        label_81.setPalette(palette_scope)
        label_81.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_81)

        hbox_lay_algorithm_82 =  QHBoxLayout()
        label_algorithm_82 = QLabel("    algorithm")
        label_algorithm_82.setPalette(palette_object)
        label_algorithm_82.setFont(QFont("Monospace", 10))
        hbox_lay_algorithm_82.addWidget(label_algorithm_82)

        box_algorithm_82 = QComboBox()
        box_algorithm_82.local_path = "profile.algorithm"
        box_algorithm_82.tmp_lst=[]
        box_algorithm_82.tmp_lst.append("gaussian_rs")
        for lst_itm in box_algorithm_82.tmp_lst:
            box_algorithm_82.addItem(lst_itm)
        box_algorithm_82.setCurrentIndex(0)
        box_algorithm_82.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_82.addWidget(box_algorithm_82)
        bg_box.addLayout(hbox_lay_algorithm_82)

        label_83 = QLabel("    gaussian_rs")
        label_83.setPalette(palette_scope)
        label_83.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_83)

        hbox_lay_scan_varying_84 =  QHBoxLayout()
        label_scan_varying_84 = QLabel("        scan_varying")
        label_scan_varying_84.setPalette(palette_object)
        label_scan_varying_84.setFont(QFont("Monospace", 10))
        hbox_lay_scan_varying_84.addWidget(label_scan_varying_84)

        box_scan_varying_84 = QComboBox()
        box_scan_varying_84.local_path = "profile.gaussian_rs.scan_varying"
        box_scan_varying_84.tmp_lst=[]
        box_scan_varying_84.tmp_lst.append("True")
        box_scan_varying_84.tmp_lst.append("False")
        for lst_itm in box_scan_varying_84.tmp_lst:
            box_scan_varying_84.addItem(lst_itm)
        box_scan_varying_84.setCurrentIndex(1)
        box_scan_varying_84.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying_84.addWidget(box_scan_varying_84)
        bg_box.addLayout(hbox_lay_scan_varying_84)

        label_85 = QLabel("        min_spots")
        label_85.setPalette(palette_scope)
        label_85.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_85)

        hbox_lay_overall_86 =  QHBoxLayout()
        label_overall_86 = QLabel("            overall")
        label_overall_86.setPalette(palette_object)
        label_overall_86.setFont(QFont("Monospace", 10))
        hbox_lay_overall_86.addWidget(label_overall_86)

        box_overall_86 = QSpinBox()
        box_overall_86.setValue(100)
        box_overall_86.local_path = "profile.gaussian_rs.min_spots.overall"
        box_overall_86.valueChanged.connect(self.spnbox_changed)
        hbox_lay_overall_86.addWidget(box_overall_86)
        bg_box.addLayout(hbox_lay_overall_86)

        hbox_lay_per_degree_87 =  QHBoxLayout()
        label_per_degree_87 = QLabel("            per_degree")
        label_per_degree_87.setPalette(palette_object)
        label_per_degree_87.setFont(QFont("Monospace", 10))
        hbox_lay_per_degree_87.addWidget(label_per_degree_87)

        box_per_degree_87 = QSpinBox()
        box_per_degree_87.setValue(50)
        box_per_degree_87.local_path = "profile.gaussian_rs.min_spots.per_degree"
        box_per_degree_87.valueChanged.connect(self.spnbox_changed)
        hbox_lay_per_degree_87.addWidget(box_per_degree_87)
        bg_box.addLayout(hbox_lay_per_degree_87)

        label_88 = QLabel("        filter")
        label_88.setPalette(palette_scope)
        label_88.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_88)

        hbox_lay_min_zeta_89 =  QHBoxLayout()
        label_min_zeta_89 = QLabel("            min_zeta")
        label_min_zeta_89.setPalette(palette_object)
        label_min_zeta_89.setFont(QFont("Monospace", 10))
        hbox_lay_min_zeta_89.addWidget(label_min_zeta_89)

        box_min_zeta_89 = QDoubleSpinBox()
        box_min_zeta_89.setValue(0.05)
        box_min_zeta_89.local_path = "profile.gaussian_rs.filter.min_zeta"
        box_min_zeta_89.valueChanged.connect(self.spnbox_changed)
        hbox_lay_min_zeta_89.addWidget(box_min_zeta_89)
        bg_box.addLayout(hbox_lay_min_zeta_89)

        label_90 = QLabel("        fitting")
        label_90.setPalette(palette_scope)
        label_90.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_90)

        hbox_lay_scan_step_91 =  QHBoxLayout()
        label_scan_step_91 = QLabel("            scan_step")
        label_scan_step_91.setPalette(palette_object)
        label_scan_step_91.setFont(QFont("Monospace", 10))
        hbox_lay_scan_step_91.addWidget(label_scan_step_91)

        box_scan_step_91 = QDoubleSpinBox()
        box_scan_step_91.setValue(5.0)
        box_scan_step_91.local_path = "profile.gaussian_rs.fitting.scan_step"
        box_scan_step_91.valueChanged.connect(self.spnbox_changed)
        hbox_lay_scan_step_91.addWidget(box_scan_step_91)
        bg_box.addLayout(hbox_lay_scan_step_91)

        hbox_lay_grid_size_92 =  QHBoxLayout()
        label_grid_size_92 = QLabel("            grid_size")
        label_grid_size_92.setPalette(palette_object)
        label_grid_size_92.setFont(QFont("Monospace", 10))
        hbox_lay_grid_size_92.addWidget(label_grid_size_92)

        box_grid_size_92 = QSpinBox()
        box_grid_size_92.setValue(5)
        box_grid_size_92.local_path = "profile.gaussian_rs.fitting.grid_size"
        box_grid_size_92.valueChanged.connect(self.spnbox_changed)
        hbox_lay_grid_size_92.addWidget(box_grid_size_92)
        bg_box.addLayout(hbox_lay_grid_size_92)

        hbox_lay_threshold_93 =  QHBoxLayout()
        label_threshold_93 = QLabel("            threshold")
        label_threshold_93.setPalette(palette_object)
        label_threshold_93.setFont(QFont("Monospace", 10))
        hbox_lay_threshold_93.addWidget(label_threshold_93)

        box_threshold_93 = QDoubleSpinBox()
        box_threshold_93.setValue(0.02)
        box_threshold_93.local_path = "profile.gaussian_rs.fitting.threshold"
        box_threshold_93.valueChanged.connect(self.spnbox_changed)
        hbox_lay_threshold_93.addWidget(box_threshold_93)
        bg_box.addLayout(hbox_lay_threshold_93)

        hbox_lay_grid_method_94 =  QHBoxLayout()
        label_grid_method_94 = QLabel("            grid_method")
        label_grid_method_94.setPalette(palette_object)
        label_grid_method_94.setFont(QFont("Monospace", 10))
        hbox_lay_grid_method_94.addWidget(label_grid_method_94)

        box_grid_method_94 = QComboBox()
        box_grid_method_94.local_path = "profile.gaussian_rs.fitting.grid_method"
        box_grid_method_94.tmp_lst=[]
        box_grid_method_94.tmp_lst.append("single")
        box_grid_method_94.tmp_lst.append("regular_grid")
        box_grid_method_94.tmp_lst.append("circular_grid")
        for lst_itm in box_grid_method_94.tmp_lst:
            box_grid_method_94.addItem(lst_itm)
        box_grid_method_94.setCurrentIndex(1)
        box_grid_method_94.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_grid_method_94.addWidget(box_grid_method_94)
        bg_box.addLayout(hbox_lay_grid_method_94)

        hbox_lay_fit_method_95 =  QHBoxLayout()
        label_fit_method_95 = QLabel("            fit_method")
        label_fit_method_95.setPalette(palette_object)
        label_fit_method_95.setFont(QFont("Monospace", 10))
        hbox_lay_fit_method_95.addWidget(label_fit_method_95)

        box_fit_method_95 = QComboBox()
        box_fit_method_95.local_path = "profile.gaussian_rs.fitting.fit_method"
        box_fit_method_95.tmp_lst=[]
        box_fit_method_95.tmp_lst.append("reciprocal_space")
        box_fit_method_95.tmp_lst.append("detector_space")
        for lst_itm in box_fit_method_95.tmp_lst:
            box_fit_method_95.addItem(lst_itm)
        box_fit_method_95.setCurrentIndex(0)
        box_fit_method_95.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_fit_method_95.addWidget(box_fit_method_95)
        bg_box.addLayout(hbox_lay_fit_method_95)

        label_96 = QLabel("prediction")
        label_96.setPalette(palette_scope)
        label_96.setFont(QFont("Monospace", 10, QFont.Bold))
        bg_box.addWidget(label_96)

        hbox_lay_d_min_97 =  QHBoxLayout()
        label_d_min_97 = QLabel("    d_min")
        label_d_min_97.setPalette(palette_object)
        label_d_min_97.setFont(QFont("Monospace", 10))
        hbox_lay_d_min_97.addWidget(label_d_min_97)

        box_d_min_97 = QDoubleSpinBox()
        box_d_min_97.local_path = "prediction.d_min"
        box_d_min_97.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_min_97.addWidget(box_d_min_97)
        bg_box.addLayout(hbox_lay_d_min_97)

        hbox_lay_d_max_98 =  QHBoxLayout()
        label_d_max_98 = QLabel("    d_max")
        label_d_max_98.setPalette(palette_object)
        label_d_max_98.setFont(QFont("Monospace", 10))
        hbox_lay_d_max_98.addWidget(label_d_max_98)

        box_d_max_98 = QDoubleSpinBox()
        box_d_max_98.local_path = "prediction.d_max"
        box_d_max_98.valueChanged.connect(self.spnbox_changed)
        hbox_lay_d_max_98.addWidget(box_d_max_98)
        bg_box.addLayout(hbox_lay_d_max_98)

        hbox_lay_margin_99 =  QHBoxLayout()
        label_margin_99 = QLabel("    margin")
        label_margin_99.setPalette(palette_object)
        label_margin_99.setFont(QFont("Monospace", 10))
        hbox_lay_margin_99.addWidget(label_margin_99)

        box_margin_99 = QSpinBox()
        box_margin_99.setValue(1)
        box_margin_99.local_path = "prediction.margin"
        box_margin_99.valueChanged.connect(self.spnbox_changed)
        hbox_lay_margin_99.addWidget(box_margin_99)
        bg_box.addLayout(hbox_lay_margin_99)

        hbox_lay_force_static_100 =  QHBoxLayout()
        label_force_static_100 = QLabel("    force_static")
        label_force_static_100.setPalette(palette_object)
        label_force_static_100.setFont(QFont("Monospace", 10))
        hbox_lay_force_static_100.addWidget(label_force_static_100)

        box_force_static_100 = QComboBox()
        box_force_static_100.local_path = "prediction.force_static"
        box_force_static_100.tmp_lst=[]
        box_force_static_100.tmp_lst.append("True")
        box_force_static_100.tmp_lst.append("False")
        for lst_itm in box_force_static_100.tmp_lst:
            box_force_static_100.addItem(lst_itm)
        box_force_static_100.setCurrentIndex(1)
        box_force_static_100.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_force_static_100.addWidget(box_force_static_100)
        bg_box.addLayout(hbox_lay_force_static_100)

 
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
