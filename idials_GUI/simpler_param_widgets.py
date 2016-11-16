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


class IndexSimplerParamTab( QWidget):


    '''
    This widget is the tool for tunning the simpler and most common parameters
    in the indexer, this widget is the first to appear once the button
    "Index" at the left side of the GUI is clicked
    '''


    def __init__(self, parent=None):
        super(IndexSimplerParamTab, self).__init__(parent)
        self.super_parent = parent # reference across the hole GUI to MyMainDialog

        hbox_lay_scan_varying =  QHBoxLayout()
        label_scan_varying = QLabel("refinement.parameterisation.crystal.scan_varying")

        hbox_lay_scan_varying.addWidget(label_scan_varying)

        box_scan_varying = QComboBox()
        box_scan_varying.local_path = "refinement.parameterisation.crystal.scan_varying"
        box_scan_varying.tmp_lst=[]
        box_scan_varying.tmp_lst.append("True")
        box_scan_varying.tmp_lst.append("False")
        for lst_itm in box_scan_varying.tmp_lst:
            box_scan_varying.addItem(lst_itm)
        box_scan_varying.currentIndexChanged.connect(self.combobox_changed)
        hbox_lay_scan_varying.addWidget(box_scan_varying)

        indexing_method_check = QCheckBox("indexing.method")
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


    def combobox_changed(self, value):
        sender = self.sender()
        print "combobox_changed to: ",
        str_value = str(sender.tmp_lst[value])
        print str_value
        str_path = str(sender.local_path)
        print str_path
        #self.super_parent.update_lin_txt(str_path, str_value, from_simple = True)
