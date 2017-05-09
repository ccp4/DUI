'''
DUI's command line control stacked widgets

Author: Luis Fuentes-Montero (Luiso)
With strong help from DIALS and CCP4 teams

copyright (c) CCP4 - DLS
'''

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from python_qt_bind import *
import os, sys

import libtbx.introspection


class FindspotsSimplerParameterTab( QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the spot-finder, this widget is the first to appear once the button
    "Find Sots" at the left side of the GUI is clicked
    '''
    def __init__(self, parent = None):
        super(FindspotsSimplerParameterTab, self).__init__()
        self.param_widget_parent = parent.param_widget_parent

        xds_gain_label = QLabel("spotfinder.threshold.xds.gain")
        xds_gain_spn_bx = QDoubleSpinBox()
        xds_gain_spn_bx.local_path = "spotfinder.threshold.xds.gain"
        xds_gain_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_sigma_background_label = QLabel("spotfinder.threshold.xds.sigma_background")
        xds_sigma_background_spn_bx = QDoubleSpinBox()
        xds_sigma_background_spn_bx.setValue(6.0)
        xds_sigma_background_spn_bx.local_path = "spotfinder.threshold.xds.sigma_background"
        xds_sigma_background_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_sigma_strong_label = QLabel("spotfinder.threshold.xds.sigma_strong")
        xds_sigma_strong_spn_bx = QDoubleSpinBox()
        xds_sigma_strong_spn_bx.setValue(3.0)
        xds_sigma_strong_spn_bx.local_path = "spotfinder.threshold.xds.sigma_strong"
        xds_sigma_strong_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_global_threshold_label = QLabel("spotfinder.threshold.xds.global_threshold")
        xds_global_threshold_spn_bx = QDoubleSpinBox()
        xds_global_threshold_spn_bx.local_path = "spotfinder.threshold.xds.global_threshold"
        xds_global_threshold_spn_bx.valueChanged.connect(self.spnbox_changed)

        localLayout = QVBoxLayout()

        xds_gain_hb = QHBoxLayout()
        xds_gain_hb.addWidget(xds_gain_label)
        xds_gain_hb.addWidget(xds_gain_spn_bx)
        localLayout.addLayout(xds_gain_hb)

        xds_sigma_background_hb = QHBoxLayout()
        xds_sigma_background_hb.addWidget(xds_sigma_background_label)
        xds_sigma_background_hb.addWidget(xds_sigma_background_spn_bx)
        localLayout.addLayout(xds_sigma_background_hb)

        xds_sigma_strong_hb = QHBoxLayout()
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_label)
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_spn_bx)
        localLayout.addLayout(xds_sigma_strong_hb)

        xds_global_threshold_hb = QHBoxLayout()
        xds_global_threshold_hb.addWidget(xds_global_threshold_label)
        xds_global_threshold_hb.addWidget(xds_global_threshold_spn_bx)
        localLayout.addLayout(xds_global_threshold_hb)


        hbox_lay_nproc =  QHBoxLayout()
        label_nproc = QLabel("spotfinder.mp.nproc")
        #label_nproc.setPalette(palette_object)
        #label_nproc.setFont( QFont("Monospace", 10))
        hbox_lay_nproc.addWidget(label_nproc)


        self.box_nproc = QSpinBox()
        self.box_nproc.local_path = "spotfinder.mp.nproc"

        cpu_max_proc = libtbx.introspection.number_of_processors()
        self.box_nproc.setValue(int(cpu_max_proc))

        self.box_nproc.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc.addWidget(self.box_nproc)
        localLayout.addLayout(hbox_lay_nproc)

        localLayout.addStretch(1)

        self.setLayout(localLayout)

        self.lst_wgs = []
        self.lst_wgs.append(xds_gain_spn_bx)
        self.lst_wgs.append(xds_sigma_background_spn_bx)
        self.lst_wgs.append(xds_sigma_strong_spn_bx)
        self.lst_wgs.append(xds_global_threshold_spn_bx)
        self.lst_wgs.append(self.box_nproc)

        for wgdt in self.lst_wgs:
            wgdt.tmp_lst = None


    def spnbox_changed(self, value):
        sender = self.sender()
        str_value = str(value)
        print value
        str_path = str(sender.local_path)
        self.param_widget_parent.update_lin_txt(str_path, str_value)


class IndexSimplerParamTab( QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the indexer, this widget is the first to appear once the button
    "Index" at the left side of the GUI is clicked
    '''
    def __init__(self, phl_obj = None, parent=None):
        super(IndexSimplerParamTab, self).__init__()
        self.param_widget_parent = parent.param_widget_parent

        hbox_lay_scan_varying =  QHBoxLayout()
        label_scan_varying = QLabel("refinement.parameterisation.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.setCurrentIndex(1)
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)

        #indexing_method_check = QCheckBox("indexing.method")
        hbox_method =  QHBoxLayout()
        label_method_62 = QLabel("indexing.method")
        hbox_method.addWidget(label_method_62)
        box_method_62 = QComboBox()
        box_method_62.tmp_lst=[]
        box_method_62.local_path = "indexing.method"
        box_method_62.tmp_lst.append("fft3d")
        box_method_62.tmp_lst.append("fft1d")
        box_method_62.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_62.tmp_lst:
            box_method_62.addItem(lst_itm)
        box_method_62.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(box_method_62)

        localLayout = QVBoxLayout()
        localLayout.addLayout(hbox_lay_scan_varying)
        localLayout.addLayout(hbox_method)
        localLayout.addStretch(1)

        self.setLayout(localLayout)

        self.lst_wgs = []
        self.lst_wgs.append(box_scan_varying)
        self.lst_wgs.append(box_method_62)

    def combobox_changed(self, value):
        sender = self.sender()
        str_value = str(sender.tmp_lst[value])
        str_path = str(sender.local_path)
        self.param_widget_parent.update_lin_txt(str_path, str_value)


class RefineSimplerParamTab( QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the refiner, this widget is the first to appear once the button
    "Refine" at the left side of the GUI is clicked
    '''
    def __init__(self, parent=None):
        super(RefineSimplerParamTab, self).__init__()
        self.param_widget_parent = parent.param_widget_parent

        hbox_lay_scan_varying =  QHBoxLayout()
        localLayout = QVBoxLayout()
        label_scan_varying = QLabel("refinement.parameterisation.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.setCurrentIndex(1)

        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)
        localLayout.addLayout(hbox_lay_scan_varying)
        localLayout.addStretch(1)
        self.setLayout(localLayout)

        self.lst_wgs = []
        self.lst_wgs.append(box_scan_varying)

    def combobox_changed(self, value):
        sender = self.sender()
        str_value = str(sender.tmp_lst[value])
        str_path = str(sender.local_path)
        self.param_widget_parent.update_lin_txt(str_path, str_value)


class IntegrateSimplerParamTab( QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the integrate algorithm, this widget is the first to appear once the button
    "Integrate" at the left side of the GUI is clicked
    '''
    def __init__(self, parent=None):
        super(IntegrateSimplerParamTab, self).__init__()
        self.param_widget_parent = parent.param_widget_parent

        localLayout = QVBoxLayout()
        PrFit_lay_out =  QHBoxLayout()
        label_PrFit = QLabel("integration.profile.fitting")
        PrFit_lay_out.addWidget(label_PrFit)

        PrFit_comb_bx = QComboBox()
        PrFit_comb_bx.local_path = "integration.profile.fitting"
        PrFit_comb_bx.tmp_lst=[]
        PrFit_comb_bx.tmp_lst.append("True")
        PrFit_comb_bx.tmp_lst.append("False")

        for lst_itm in PrFit_comb_bx.tmp_lst:
            PrFit_comb_bx.addItem(lst_itm)
        PrFit_comb_bx.currentIndexChanged.connect(self.combobox_changed)
        PrFit_lay_out.addWidget(PrFit_comb_bx)
        localLayout.addLayout(PrFit_lay_out)

        hbox_lay_algorithm_53 =  QHBoxLayout()
        label_algorithm_53 = QLabel("integration.background.algorithm")
        hbox_lay_algorithm_53.addWidget(label_algorithm_53)

        box_algorithm_53 = QComboBox()
        box_algorithm_53.local_path = "integration.background.algorithm"
        box_algorithm_53.tmp_lst=[]
        box_algorithm_53.tmp_lst.append("simple")
        box_algorithm_53.tmp_lst.append("null")
        box_algorithm_53.tmp_lst.append("median")
        box_algorithm_53.tmp_lst.append("gmodel")
        box_algorithm_53.tmp_lst.append("glm")

        for lst_itm in box_algorithm_53.tmp_lst:
            box_algorithm_53.addItem(lst_itm)
        box_algorithm_53.setCurrentIndex(4)
        box_algorithm_53.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_algorithm_53.addWidget(box_algorithm_53)
        localLayout.addLayout(hbox_lay_algorithm_53)

        hbox_lay_nproc =  QHBoxLayout()
        label_nproc = QLabel("integration.mp.nproc")
        #label_nproc.setFont( QFont("Monospace", 10))
        hbox_lay_nproc.addWidget(label_nproc)

        self.box_nproc = QSpinBox()



        #self.box_nproc.setValue(1)

        cpu_max_proc = libtbx.introspection.number_of_processors()
        self.box_nproc.setValue(int(cpu_max_proc))



        self.box_nproc.local_path = "integration.mp.nproc"
        self.box_nproc.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc.addWidget(self.box_nproc)
        localLayout.addLayout(hbox_lay_nproc)

        localLayout.addStretch(1)
        self.setLayout(localLayout)

        self.lst_wgs = []
        self.lst_wgs.append(PrFit_comb_bx)
        self.lst_wgs.append(box_algorithm_53)
        self.box_nproc.tmp_lst = None
        self.lst_wgs.append(self.box_nproc)

    def combobox_changed(self, value):
        sender = self.sender()
        str_value = str(sender.tmp_lst[value])
        str_path = str(sender.local_path)
        self.param_widget_parent.update_lin_txt(str_path, str_value)

    def spnbox_changed(self, value):
        sender = self.sender()
        str_value = str(value)
        print value
        str_path = str(sender.local_path)
        self.param_widget_parent.update_lin_txt(str_path, str_value)



class TmpTstWidget( QWidget):

    def __init__(self, parent = None):
        super(TmpTstWidget, self).__init__()
        self.param_widget_parent = self
        my_widget = FindspotsSimplerParameterTab(self)

        my_box = QVBoxLayout()
        my_box.addWidget(my_widget)
        self.setLayout(my_box)
        self.show()

if( __name__ == "__main__" ):
    app =  QApplication(sys.argv)
    ex = TmpTstWidget()
    sys.exit(app.exec_())
