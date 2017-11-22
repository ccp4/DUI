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




# FIXME Copied from dials.index.py. This is needed here because scipy needs to
# be imported before cctbx otherwise there will be a segmentation fault. This
# should be fixed in dials.index so that we don't need to import here.
try:
  # try importing scipy.linalg before any cctbx modules, otherwise we
  # sometimes get a segmentation fault/core dump if it is imported after
  # scipy.linalg is a dependency of sklearn.cluster.DBSCAN
  import scipy.linalg # import dependency
except ImportError, e:
  pass


from resources.python_qt_bind import GuiBinding
gui_lib = GuiBinding()
print "using ", gui_lib.pyhon_binding
qt_tool = gui_lib.pyhon_binding

if( qt_tool == "PyQt4" ):
    from PyQt4 import QtCore, QtGui, QtWebKit

else:
    from PySide import QtCore, QtGui, QtWebKit

import os



class FindspotsSimplerParameterTab(QtGui.QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the spot-finder, this widget is the first to appear once the button
    "Find Sots" at the left side of the GUI is clicked

    '''
    def __init__(self, parent = None):
        super(FindspotsSimplerParameterTab, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog


        xds_gain_label = QtGui.QLabel("spotfinder.threshold.xds.gain")
        xds_gain_spn_bx = QtGui.QDoubleSpinBox()
        xds_gain_spn_bx.local_path = "spotfinder.threshold.xds.gain"
        xds_gain_spn_bx.valueChanged.connect(self.spnbox_changed)
        temp_disable = '''
        xds_kernel_size_label_x = QtGui.QLabel("spotfinder.threshold.xds.kernel_size(X)")
        xds_kernel_size_spn_bx_x = QtGui.QSpinBox()
        xds_kernel_size_spn_bx_x.local_path = "spotfinder.threshold.xds.kernel_size(X)"
        xds_kernel_size_spn_bx_x.valueChanged.connect(self.spnbox_changed)

        xds_kernel_size_label_y = QtGui.QLabel("spotfinder.threshold.xds.kernel_size(Y)")
        xds_kernel_size_spn_bx_y = QtGui.QSpinBox()
        xds_kernel_size_spn_bx_y.local_path = "spotfinder.threshold.xds.kernel_size(Y)"
        xds_kernel_size_spn_bx_y.valueChanged.connect(self.spnbox_changed)
        '''

        xds_sigma_background_label = QtGui.QLabel("spotfinder.threshold.xds.sigma_background")
        xds_sigma_background_spn_bx = QtGui.QDoubleSpinBox()
        xds_sigma_background_spn_bx.setValue(6.0)
        xds_sigma_background_spn_bx.local_path = "spotfinder.threshold.xds.sigma_background"
        xds_sigma_background_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_sigma_strong_label = QtGui.QLabel("spotfinder.threshold.xds.sigma_strong")
        xds_sigma_strong_spn_bx = QtGui.QDoubleSpinBox()
        xds_sigma_strong_spn_bx.setValue(3.0)
        xds_sigma_strong_spn_bx.local_path = "spotfinder.threshold.xds.sigma_strong"
        xds_sigma_strong_spn_bx.valueChanged.connect(self.spnbox_changed)

        xds_global_threshold_label = QtGui.QLabel("spotfinder.threshold.xds.global_threshold")
        xds_global_threshold_spn_bx = QtGui.QDoubleSpinBox()
        xds_global_threshold_spn_bx.local_path = "spotfinder.threshold.xds.global_threshold"
        xds_global_threshold_spn_bx.valueChanged.connect(self.spnbox_changed)

        localLayout = QtGui.QVBoxLayout()

        xds_gain_hb = QtGui.QHBoxLayout()
        xds_gain_hb.addWidget(xds_gain_label)
        xds_gain_hb.addWidget(xds_gain_spn_bx)
        localLayout.addLayout(xds_gain_hb)

        temp_disable = '''
        xds_kernel_size_hb_x = QtGui.QHBoxLayout()
        xds_kernel_size_hb_x.addWidget(xds_kernel_size_label_x)
        xds_kernel_size_hb_x.addWidget(xds_kernel_size_spn_bx_x)
        localLayout.addLayout(xds_kernel_size_hb_x)

        xds_kernel_size_hb_y = QtGui.QHBoxLayout()
        xds_kernel_size_hb_y.addWidget(xds_kernel_size_label_y)
        xds_kernel_size_hb_y.addWidget(xds_kernel_size_spn_bx_y)
        localLayout.addLayout(xds_kernel_size_hb_y)
        '''

        xds_sigma_background_hb = QtGui.QHBoxLayout()
        xds_sigma_background_hb.addWidget(xds_sigma_background_label)
        xds_sigma_background_hb.addWidget(xds_sigma_background_spn_bx)
        localLayout.addLayout(xds_sigma_background_hb)

        xds_sigma_strong_hb = QtGui.QHBoxLayout()
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_label)
        xds_sigma_strong_hb.addWidget(xds_sigma_strong_spn_bx)
        localLayout.addLayout(xds_sigma_strong_hb)

        xds_global_threshold_hb = QtGui.QHBoxLayout()
        xds_global_threshold_hb.addWidget(xds_global_threshold_label)
        xds_global_threshold_hb.addWidget(xds_global_threshold_spn_bx)
        localLayout.addLayout(xds_global_threshold_hb)




        hbox_lay_nproc =  QtGui.QHBoxLayout()
        label_nproc = QtGui.QLabel("spotfinder.mp.nproc")
        #label_nproc.setPalette(palette_object)
        #label_nproc.setFont(QtGui.QFont("Monospace", 10))
        hbox_lay_nproc.addWidget(label_nproc)

        box_nproc = QtGui.QSpinBox()
        box_nproc.setValue(1)
        box_nproc.local_path = "spotfinder.mp.nproc"
        box_nproc.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc.addWidget(box_nproc)
        localLayout.addLayout(hbox_lay_nproc)


        localLayout.addStretch(1)

        self.setLayout(localLayout)


    def spnbox_changed(self, value):
        sender = self.sender()
        str_value = str(value)
        print value
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)
        #self.super_parent.update_lin_txt(sender.local_path, value)


    def update_a_param(self):
        print "from update_a_param"


class IndexSimplerParamTab(QtGui.QWidget):


    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the indexer, this widget is the first to appear once the button
    "Index" at the left side of the GUI is clicked

    '''

    def __init__(self, parent=None):
        super(IndexSimplerParamTab, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        hbox_lay_scan_varying =  QtGui.QHBoxLayout()
        label_scan_varying = QtGui.QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QtGui.QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)

        indexing_method_check = QtGui.QCheckBox("indexing.method")
        hbox_method =  QtGui.QHBoxLayout()
        label_method_62 = QtGui.QLabel("indexing.method")
        hbox_method.addWidget(label_method_62)
        box_method_62 = QtGui.QComboBox()
        box_method_62.tmp_lst=[]
        box_method_62.local_path = "indexing.method"
        box_method_62.tmp_lst.append("fft3d")
        box_method_62.tmp_lst.append("fft1d")
        box_method_62.tmp_lst.append("real_space_grid_search")
        for lst_itm in box_method_62.tmp_lst:
            box_method_62.addItem(lst_itm)
        box_method_62.currentIndexChanged.connect(self.combobox_changed)

        hbox_method.addWidget(box_method_62)

        localLayout = QtGui.QVBoxLayout()
        localLayout.addLayout(hbox_lay_scan_varying)

        localLayout.addLayout(hbox_method)

        localLayout.addStretch(1)

        self.setLayout(localLayout)


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)



class RefineSimplerParamTab(QtGui.QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the refiner, this widget is the first to appear once the button
    "Refine" at the left side of the GUI is clicked
    '''

    def __init__(self, parent=None):
        super(RefineSimplerParamTab, self).__init__(parent)

        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        hbox_lay_scan_varying =  QtGui.QHBoxLayout()
        localLayout = QtGui.QVBoxLayout()
        label_scan_varying = QtGui.QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QtGui.QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)
        localLayout.addLayout(hbox_lay_scan_varying)
        localLayout.addStretch(1)
        self.setLayout(localLayout)


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)


class IntegrateSimplerParamTab(QtGui.QWidget):
    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the integrate algorithm, this widget is the first to appear once the button
    "Integrate" at the left side of the GUI is clicked

    '''
    def __init__(self, parent=None):
        super(IntegrateSimplerParamTab, self).__init__(parent)
        localLayout = QtGui.QVBoxLayout()
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        PrFit_lay_out =  QtGui.QHBoxLayout()
        label_PrFit = QtGui.QLabel("integration.profile.fitting")
        PrFit_lay_out.addWidget(label_PrFit)

        PrFit_comb_bx = QtGui.QComboBox()
        PrFit_comb_bx.local_path = "integration.profile.fitting"
        PrFit_comb_bx.tmp_lst=[]
        PrFit_comb_bx.tmp_lst.append("True")
        PrFit_comb_bx.tmp_lst.append("False")

        for lst_itm in PrFit_comb_bx.tmp_lst:
            PrFit_comb_bx.addItem(lst_itm)
        PrFit_comb_bx.currentIndexChanged.connect(self.combobox_changed)
        PrFit_lay_out.addWidget(PrFit_comb_bx)
        localLayout.addLayout(PrFit_lay_out)

        hbox_lay_algorithm_53 =  QtGui.QHBoxLayout()
        label_algorithm_53 = QtGui.QLabel("integration.background.algorithm")
        hbox_lay_algorithm_53.addWidget(label_algorithm_53)

        box_algorithm_53 = QtGui.QComboBox()
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
        localLayout.addLayout(hbox_lay_algorithm_53)

        hbox_lay_nproc =  QtGui.QHBoxLayout()
        label_nproc = QtGui.QLabel("integration.mp.nproc")
        #label_nproc.setFont(QtGui.QFont("Monospace", 10))
        hbox_lay_nproc.addWidget(label_nproc)

        box_nproc = QtGui.QSpinBox()
        box_nproc.setValue(1)
        box_nproc.local_path = "integration.mp.nproc"
        box_nproc.valueChanged.connect(self.spnbox_changed)
        hbox_lay_nproc.addWidget(box_nproc)
        localLayout.addLayout(hbox_lay_nproc)

        localLayout.addStretch(1)
        self.setLayout(localLayout)


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        str_path = str(sender.local_path)
        print str_path
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)


    def spnbox_changed(self, value):
        sender = self.sender()
        str_value = str(value)
        print value
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)
        #self.super_parent.update_lin_txt(sender.local_path, value)

class ExportSimplerParameterWidget(QtGui.QWidget):
    '''
    This widget like the import one has no multiple tabs, but it does have
    auto generated code on it
    '''

    def __init__(self, parent=None):
        from resources.export_mult_opt import ParamMainWidget
        super(ExportSimplerParameterWidget, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog


        hbox_lay_hklout_6 = QtGui.QHBoxLayout()
        label_hklout_6 = QtGui.QLabel("    hklout")
        label_hklout_6.setFont(QtGui.QFont("Monospace"))
        hbox_lay_hklout_6.addWidget(label_hklout_6)

        box_hklout_6 = QtGui.QLineEdit()
        box_hklout_6.setText("hklout.mtz")
        box_hklout_6.local_path = "mtz.hklout"
        box_hklout_6.textChanged.connect(self.spnbox_changed)

        hbox_lay_hklout_6.addWidget(box_hklout_6)
        bg_box = QtGui.QVBoxLayout()
        bg_box.addLayout(hbox_lay_hklout_6)

        self.run_pointless_check = QtGui.QCheckBox("Run Pointless")
        bg_box.addWidget(self.run_pointless_check)

        self.run_aimless_check = QtGui.QCheckBox("Run Aimless")
        bg_box.addWidget(self.run_aimless_check)

        bg_box.addStretch()
        self.setLayout(bg_box)


    def spnbox_changed(self, value):
        sender = self.sender()
        print "sender =", sender
        print "spnbox_changed to:",
        str_value = str(value)
        print value
        str_path = str(sender.local_path)
        self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)


