'''
iDIALS GUI's image viewer

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

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys, os
import numpy as np

from dxtbx.datablock import DataBlockFactory
from dials.array_family import flex
from dxtbx.datablock import DataBlockFactory

from img_view_tools import img_w_cpp, build_qimg, find_hkl_near, lst_arange
from time import time as time_now

QGLWidget_test = '''
try:
    from PyQt4.QtOpenGL import QGLWidget
    from OpenGL import GL
    MyQWidgetWithQPainter = QGLWidget

except:
    print "Failed to import OpenGL"
    MyQWidgetWithQPainter = QWidget
#'''

MyQWidgetWithQPainter = QWidget

class ImgPainter(MyQWidgetWithQPainter):

    def __init__(self, parent = None):
        super(ImgPainter, self).__init__()
        self.my_parent = parent

        self.img = None
        self.setMouseTracking(True)
        self.xb = None
        self.yb = None

        self.num_of_closer_ref = None
        self.my_scale = 1.0
        self.img_width = 247
        self.img_height = 253

        self.show()
        self.resize(self.img_width * self.my_scale, self.img_height * self.my_scale)

        self.p_h_svar = self.my_parent.my_scrollable.horizontalScrollBar
        self.p_v_svar = self.my_parent.my_scrollable.verticalScrollBar


    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.NoButton:
            self.x_pos, self.y_pos = event.x(), event.y()
            pix_col = int(self.x_pos / self.my_scale)
            pix_row = int(self.y_pos / self.my_scale)

            try:
                new_label_txt = " X : " + str(pix_col) + ", Y : " + str(pix_row) \
                                + ", I : " + str(self.my_parent.img_arr[pix_row, pix_col])

                self.my_parent.info_label.setText(new_label_txt)

            except:
                no_longer_needed = '''
                print "failed to update i(x,y) label"
                '''


            if( self.my_parent.rad_but_near_hkl.isChecked() == True ):
                self.find_closer_hkl(self.x_pos, self.y_pos)

            else:
                self.num_of_closer_ref = None

        elif event.buttons() == Qt.LeftButton:
            dx = event.x() - self.x_pos
            dy = event.y() - self.y_pos
            self.move_scrollbar(scrollBar = self.p_h_svar(), dst = dx)
            self.move_scrollbar(scrollBar = self.p_v_svar(), dst = dy)

        elif event.buttons() == Qt.RightButton:
            print "Right click drag"

        #TODO find out how does this works despite
        #               NOT updating
        #      self.x_pos and self.y_pos always


    def wheelEvent(self, event):

        if( event.delta() > 0.0 and self.my_scale < 100.0 ):
            scale_factor = 1.1

        elif( event.delta() < 0.0 and self.my_scale > 0.333 ):
            scale_factor = 0.9

        else:
            scale_factor = None
            print "reaching scale limit"

        if( scale_factor != None ):

            self.my_scale *= scale_factor

            h_scr_bar = float(self.p_h_svar().value())
            v_scr_bar = float(self.p_v_svar().value())

            h_new_pbar_pos = int(scale_factor * h_scr_bar
                             + ((scale_factor - 1) * self.p_h_svar().pageStep()/2))

            v_new_pbar_pos = int(scale_factor * v_scr_bar
                             + ((scale_factor - 1) * self.p_v_svar().pageStep()/2))

            self.update()

            self.move_scrollbar(scrollBar = self.p_h_svar(), new_pos = h_new_pbar_pos)
            self.move_scrollbar(scrollBar = self.p_v_svar(), new_pos = v_new_pbar_pos)


    def move_scrollbar(self, scrollBar = None, dst = None, new_pos = None):
        if( dst != None ):
            old_val = scrollBar.value()
            scrollBar.setValue(old_val - dst)

        if( new_pos != None ):
            scrollBar.setValue(new_pos)


    def find_closer_hkl(self, x_mouse, y_mouse):
        if( self.flat_data_lst != None ):
            x_mouse_scaled = float(x_mouse) / self.my_scale
            y_mouse_scaled = float(y_mouse) / self.my_scale
            closer_hkl = find_hkl_near(x_mouse_scaled, y_mouse_scaled, self.flat_data_lst)
            #print "closer_hkl =", self.flat_data_lst[closer_hkl][4]

            self.num_of_closer_ref = closer_hkl
            self.update()

    def set_img_pix(self, q_img = None, flat_data_lst_in = None):

        self.img = q_img
        self.flat_data_lst = flat_data_lst_in

        self.img_width = q_img.width()
        self.img_height = q_img.height()

        #replace <<update>> with <<paintEvent>> when [self] inherits from QGLWidget
        #print "self.__class__.__bases__[0].__name__ =", self.__class__.__bases__[0].__name__
        if( self.__class__.__bases__[0].__name__ == "QWidget" ):
            #print "inherits from QWidget"
            self.update()
        else:
            #print "inherits from QGLWidget"
            self.paintEvent(None)

        #in future consider *self.repaint()* for the video thing instead of *self.update()*

    def update_my_beam_centre(self, xb, yb):
        self.xb = xb
        self.yb = yb

    def paintEvent(self, event):
        if( self.img == None ):
            return

        else:
            scaled_width = int(self.img_width * self.my_scale)
            scaled_height = int(self.img_height * self.my_scale)
            self.resize(scaled_width, scaled_height)

            rect = QRect(0, 0, scaled_width, scaled_height)
            pixmap = QPixmap(self.img)
            painter = QPainter(self)

            indexed_pen = QPen()  # creates a default indexed_pen
            indexed_pen.setBrush(Qt.green)
            indexed_pen.setStyle(Qt.SolidLine)

            if( self.my_scale >= 5.0 ):
                indexed_pen.setWidth(self.my_scale / 3.5)

            else:
                indexed_pen.setWidth(0.0)

            non_indexed_pen = QPen()  # creates a default non_indexed_pen
            non_indexed_pen.setBrush(QColor(75, 150, 200))
            #non_indexed_pen.setBrush(Qt.magenta)

            if( self.my_scale >= 5.0 ):
                non_indexed_pen.setStyle(Qt.DotLine)
                non_indexed_pen.setWidth(self.my_scale / 3.5)

            else:
                non_indexed_pen.setStyle(Qt.SolidLine)
                non_indexed_pen.setWidth(0.0)

            painter.drawPixmap(rect, pixmap)
            #painter.setFont(QFont("Monospace", 22))
            #painter.setFont(QFont("FreeMono", 22))

            if( self.flat_data_lst != None and self.my_parent.chk_box_show.checkState()):
                tmp_font = QFont()
                tmp_font.setPixelSize(int(5.5 * self.my_scale))
                #TODO consider "tmp_font.setPointSize(..." instead of "tmp_font.setPixelSize(..."
                painter.setFont(tmp_font)

                for i, reflection in enumerate(self.flat_data_lst):
                    x = float(reflection[0])
                    y = float(reflection[1])
                    width = float(reflection[2])
                    height = float(reflection[3])
                    rectangle = QRectF(x * self.my_scale, y * self.my_scale,
                                       width * self.my_scale, height * self.my_scale)

                    if( reflection[4] == "NOT indexed" ):
                        painter.setPen(non_indexed_pen)

                    else:
                        painter.setPen(indexed_pen)

                    painter.drawRect(rectangle)

                    if( self.my_parent.rad_but_all_hkl.isChecked() == True and
                       reflection[4] != "" and reflection[4] != "NOT indexed" ):

                        painter.drawText( QPoint(int((x + width) * self.my_scale),
                                              int(y * self.my_scale)),  reflection[4])

                    elif( self.my_parent.rad_but_near_hkl.isChecked() == True and
                         self.num_of_closer_ref == i ):

                        painter.drawText( QPoint(int((x + width) * self.my_scale),
                                          int(y * self.my_scale)),  reflection[4])

                if( self.xb != None and self.yb != None ):

                    cen_siz = 40.0
                    painter.drawLine(int(self.xb * self.my_scale),
                                     int((self.yb - cen_siz) * self.my_scale),
                                     int(self.xb * self.my_scale),
                                     int((self.yb + cen_siz) * self.my_scale))

                    painter.drawLine(int((self.xb + cen_siz) * self.my_scale),
                                     int(self.yb * self.my_scale),
                                     int((self.xb - cen_siz) * self.my_scale),
                                     int(self.yb * self.my_scale))

                else:
                    no_longer_needed = '''
                    print "No xb,yb provided"
                    '''

            painter.end()


class PopImgChange(QMenu):
    def __init__(self, parent=None):
        super(PopImgChange, self).__init__(parent)
        self.my_parent = parent

        top_box = QHBoxLayout()

        #TODO try to be consistent with other two QMenus
        #     use << self.my_parent >> for new QPushButtons

        btn_first =  QPushButton(' I< ')
        btn_first.clicked.connect(self.my_parent.btn_first_clicked)
        btn_rev =  QPushButton(' << ')
        btn_rev.clicked.connect(self.my_parent.btn_rev_clicked)
        btn_prev = QPushButton('  < ')
        btn_prev.clicked.connect(self.my_parent.btn_prev_clicked)
        btn_next =  QPushButton(' >  ')
        btn_next.clicked.connect(self.my_parent.btn_next_clicked)
        btn_ffw =  QPushButton(' >> ')
        btn_ffw.clicked.connect(self.my_parent.btn_ffw_clicked)
        btn_last = QPushButton('  >I ')
        btn_last.clicked.connect(self.my_parent.btn_last_clicked)

        top_box.addWidget(btn_first)
        top_box.addWidget(btn_rev)
        top_box.addWidget(btn_prev)
        top_box.addWidget(self.my_parent.img_select)
        top_box.addWidget(btn_next)
        top_box.addWidget(btn_ffw)
        top_box.addWidget(btn_last)

        bot_box = QHBoxLayout()

        btn_play = QPushButton("Play IMGs Video")
        btn_play.clicked.connect(self.my_parent.btn_play_clicked)
        btn_stop = QPushButton("Stop IMGs Video")
        btn_stop.clicked.connect(self.my_parent.btn_stop_clicked)

        bot_box.addWidget(btn_play)
        bot_box.addWidget(btn_stop)

        mid_box = QHBoxLayout()

        mid_box.addWidget(QLabel("Image Jump Step"))
        mid_box.addWidget(self.my_parent.img_step)
        mid_box.addWidget(QLabel("Number of Images to Add"))
        mid_box.addWidget(self.my_parent.num_of_imgs_to_add)

        my_layout = QVBoxLayout()

        my_layout.addLayout(top_box)
        my_layout.addLayout(mid_box)
        my_layout.addLayout(bot_box)

        self.setLayout(my_layout)
        self.show()


class PopImgTreat(QMenu):
    def __init__(self, parent=None):
        super(PopImgTreat, self).__init__(parent)
        self.my_parent = parent

        top_box = QHBoxLayout()
        top_box.addWidget(QLabel("I min"))
        top_box.addWidget(self.my_parent.min_edit)
        top_box.addWidget(QLabel("I max"))
        top_box.addWidget(self.my_parent.max_edit)

        bot_box = QHBoxLayout()
        bot_box.addWidget(self.my_parent.palette_select)

        my_box = QVBoxLayout()
        my_box.addLayout(top_box)
        my_box.addLayout(bot_box)

        self.setLayout(my_box)
        self.show()


class PopInfoHandl(QMenu):
    def __init__(self, parent=None):
        super(PopInfoHandl, self).__init__(parent)
        self.my_parent = parent

        bot_box = QHBoxLayout()
        bot_box.addWidget(self.my_parent.chk_box_show)

        rb_group = QButtonGroup()
        rb_group_box = QGroupBox()
        rb_group_box_layout = QVBoxLayout()
        rb_group_box.setLayout(rb_group_box_layout)

        rb_group_box_layout.addWidget(self.my_parent.rad_but_all_hkl)
        rb_group.addButton(self.my_parent.rad_but_all_hkl)
        rb_group_box_layout.addWidget(self.my_parent.rad_but_near_hkl)
        rb_group.addButton(self.my_parent.rad_but_near_hkl)
        rb_group_box_layout.addWidget(self.my_parent.rad_but_none_hkl)
        rb_group.addButton(self.my_parent.rad_but_none_hkl)

        my_box = QVBoxLayout()
        my_box.addLayout(bot_box)
        my_box.addWidget(rb_group_box)
        self.setLayout(my_box)
        self.show()


class MyImgWin(QWidget):
    def __init__(self, json_file_path = None, pckl_file_path = None):
        super(MyImgWin, self).__init__()
        my_box = QVBoxLayout()
        top_box = QHBoxLayout()
        left_top_box = QVBoxLayout()
        right_top_box = QVBoxLayout()

        self.img_select = QSpinBox()
        self.img_step = QSpinBox()
        self.num_of_imgs_to_add = QSpinBox()

        self.my_scrollable = QScrollArea()
        self.my_painter = ImgPainter(self)
        self.my_scrollable.setWidget(self.my_painter)

        max_min_validator = QIntValidator(-5, 999999, self)

        sys_font = QFont()
        sys_font_point_size =  sys_font.pointSize()

        self.i_min = -3
        self.min_edit = QLineEdit()
        self.min_edit.setFixedWidth(6 * sys_font_point_size)
        self.min_edit.setValidator(max_min_validator)
        self.min_edit.setText(str(self.i_min))
        self.min_edit.editingFinished.connect(self.min_changed_by_user)

        self.i_max = 100
        self.max_edit = QLineEdit()
        self.max_edit.setFixedWidth(6 * sys_font_point_size)
        self.max_edit.setValidator(max_min_validator)
        self.max_edit.setText(str(self.i_max))
        self.max_edit.editingFinished.connect(self.max_changed_by_user)

        self.chk_box_show = QCheckBox("show reflection info")
        self.chk_box_show.setChecked(True)
        self.chk_box_show.stateChanged.connect(self.set_img)

        self.rad_but_all_hkl = QRadioButton("All HKLs")
        self.rad_but_all_hkl.clicked.connect(self.Action1)

        self.rad_but_all_hkl.setChecked(True)

        self.rad_but_near_hkl = QRadioButton("Nearest HKL")
        self.rad_but_near_hkl.clicked.connect(self.Action2)
        self.rad_but_none_hkl = QRadioButton("No HKL")
        self.rad_but_none_hkl.clicked.connect(self.Action3)


        self.palette_select = QComboBox()
        self.palette_lst = ["hot ascend", "hot descend", "black2white", "white2black"]
        self.palette = self.palette_lst[0]
        for plt in self.palette_lst:
            self.palette_select.addItem(plt)

        self.palette_select.currentIndexChanged.connect(self.palette_changed_by_user)


        img_select_but = QPushButton('Img Select  ...')
        img_select_but.setMenu(PopImgChange(self))

        img_pal_but = QPushButton('Img Palette  ...')
        img_pal_but.setMenu(PopImgTreat(self))

        info_but = QPushButton('Info Handling  ...')
        info_but.setMenu(PopInfoHandl(self))


        self.img_num = 0
        self.img_step_val = 1
        self.stack_size = 1

        self.my_sweep = None
        self.flat_data_lst = [None]
        self.current_qimg = build_qimg()

        if( json_file_path == None ):
            print "\n no datablock given \n"
            n_of_imgs = 1

        else:
            self.ini_datablock(json_file_path)

        if( pckl_file_path == None ):
            print "\n no pickle file given \n"

        else:
            self.ini_reflection_table(pckl_file_path)

        self.set_img()

        self.img_select.valueChanged.connect(self.img_changed_by_user)
        self.img_step.valueChanged.connect(self.step_changed_by_user)
        self.num_of_imgs_to_add.valueChanged.connect(self.stack_changed_by_user)

        top_box.addWidget(img_select_but)
        top_box.addWidget(img_pal_but)
        top_box.addWidget(info_but)

        self.info_label = QLabel("X, Y, I = ?,?,?")

        my_box.addLayout(top_box)
        my_box.addWidget(self.my_scrollable)
        my_box.addWidget(self.info_label)

        self.setLayout(my_box)
        self.show()

    def ini_datablock(self, json_file_path):

        if( json_file_path != None ):

            try:
                datablocks = DataBlockFactory.from_json_file(json_file_path)
                ##TODO check length of datablock for safety
                datablock = datablocks[0]
                self.my_sweep = datablock.extract_sweeps()[0]
                self.img_select.clear()
                print "self.my_sweep.get_array_range() =", self.my_sweep.get_array_range()
                print "self.my_sweep.get_image_size() =", self.my_sweep.get_image_size()
                n_of_imgs = len(self.my_sweep.indices())
                print "n_of_imgs =", n_of_imgs

                self.img_select.setMaximum(n_of_imgs)
                self.img_select.setMinimum(1)

                self.img_step.setMaximum(n_of_imgs / 2)
                self.img_step.setMinimum(1)

                self.num_of_imgs_to_add.setMaximum(n_of_imgs)
                self.num_of_imgs_to_add.setMinimum(1)

            except:
                print "Failed to load images from  datablock.json"


    def ini_reflection_table(self, pckl_file_path):
        if( pckl_file_path != None ):
            firts_time = time_now()

            print "[pickle file] =", pckl_file_path
            table = flex.reflection_table.from_pickle(pckl_file_path)
            print "table =", table
            print "len(table) = ", len(table)
            n_refs = len(table)
            bbox_col = map(list, table["bbox"])
            try:
                hkl_col = map(str, table["miller_index"])

            except:
                hkl_col = []

            n_imgs = self.img_select.maximum()
            self.flat_data_lst = []
            if( n_imgs > 0 ):
                self.flat_data_lst = lst_arange(bbox_col, hkl_col, n_imgs)

            print "\n building flat_data_lst (diff time) =", time_now() - firts_time, "\n"

        else:
            self.flat_data_lst = [None]

        self.set_img()

    def update_beam_centre(self, xb, yb):
        print " update_beam_centre"
        print "new x,y =", xb, yb
        self.my_painter.update_my_beam_centre(xb, yb)

    def set_img(self):
        if( self.my_sweep != None):

            img_pos = self.img_num - 1
            self.img_arr = self.my_sweep.get_raw_data(img_pos)[0]

            if( self.stack_size > 1 ):
                for times in xrange(1, self.stack_size):
                    pos_to_add = (img_pos) + times
                    if( pos_to_add < len(self.my_sweep.indices()) ):
                        self.img_arr = self.img_arr + self.my_sweep.get_raw_data(pos_to_add)[0]

            if(self.flat_data_lst == [None]):
                self.my_painter.set_img_pix(self.current_qimg(self.img_arr, self.palette,
                                                              self.i_min, self.i_max))

            else:
                self.my_painter.set_img_pix(self.current_qimg(self.img_arr, self.palette,
                                                              self.i_min, self.i_max),
                                                              self.flat_data_lst[img_pos])


    def Action1(self):
        #TODO fix the name of this function
        print "rad_but_all_hkl clicked"
        self.set_img()

    def Action2(self):
        #TODO fix the name of this function
        print "rad_but_near_hkl clicked"
        self.set_img()

    def Action3(self):
        #TODO fix the name of this function
        print "rad_but_none_hkl clicked"
        self.set_img()

    def btn_play_clicked(self):
        print "btn_play_clicked(self)"

        self.video_timer = QTimer(self)
        self.video_timer.timeout.connect(self.btn_next_clicked)
        self.video_timer.start(1)

    def btn_stop_clicked(self):
        print "B_stop_clicked(self)"
        self.video_timer.stop()

    def min_changed_by_user(self):
        new_value = self.min_edit.text()
        try:
            self.i_min = int(new_value)
        except:
            self.i_min = 0
        self.set_img()

    def max_changed_by_user(self):
        new_value = self.max_edit.text()
        try:
            self.i_max = int(new_value)
        except:
            self.i_max = 0
        self.set_img()

    def palette_changed_by_user(self, new_palette_num):
        self.palette = self.palette_lst[new_palette_num]
        self.set_img()

    def btn_first_clicked(self):
        #TODO have a look at why is unable to go to
        #TODO the very first image sometimes

        self.img_num = 1
        self.img_select.setValue(self.img_num)

    def btn_rev_clicked(self):
        self.img_num -= 10
        if( self.img_num < 1 ):
            self.img_num = 1

        self.img_select.setValue(self.img_num)

    def btn_prev_clicked(self):
        self.img_num -= self.img_step_val
        if( self.img_num < 1 ):
            self.img_num = 1

        self.img_select.setValue(self.img_num)

    def btn_next_clicked(self):
        self.img_num += self.img_step_val
        if( self.img_num > self.img_select.maximum() ):
            if( self.video_timer.isActive() == True ):
                self.img_num = 1

            else:
                self.img_num = self.img_select.maximum()

        self.img_select.setValue(self.img_num)

    def btn_ffw_clicked(self):
        self.img_num += 10
        if( self.img_num > self.img_select.maximum() ):
            self.img_num = self.img_select.maximum()

        self.img_select.setValue(self.img_num)

    def btn_last_clicked(self):
        self.img_num = self.img_select.maximum()
        self.img_select.setValue(self.img_num)

    def step_changed_by_user(self, value):
        self.img_step_val = value

    def stack_changed_by_user(self, value):
        self.stack_size = value
        self.set_img()

    def img_changed_by_user(self, value):
        self.img_num = value
        if( self.img_num > self.img_select.maximum() ):
            self.img_num = self.img_select.maximum()
            self.img_select.setValue(self.img_num)

        self.set_img()


if( __name__ == "__main__" ):

    app = QApplication(sys.argv)
    print "sys.argv =", sys.argv
    print "len(sys.argv) =", len(sys.argv)

    if( len(sys.argv) > 1 ):
        img_path = sys.argv[1]
        if( len(sys.argv) > 2 ):
            pckl_file_path = sys.argv[2]

        else:
            pckl_file_path = None

    else:
        img_path = None

    print "img_path =", img_path
    print "pckl_file_path =", pckl_file_path


    diag = MyImgWin(img_path, pckl_file_path)
    sys.exit(app.exec_())
    app.exec_()



