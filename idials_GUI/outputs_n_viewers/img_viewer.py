import sys, os
import numpy as np
from dxtbx.datablock import DataBlockFactory
from dials.array_family import flex
from dials_viewer_ext import rgb_img
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from dxtbx.model.experiment.experiment_list import ExperimentListFactory
from dxtbx.model.experiment.experiment_list import ExperimentList, Experiment
from dxtbx.datablock import DataBlockFactory

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

class flat_data(object):
    box = None
    hkl = None


class img_w_cpp(object):
    def __init__(self):
        self.wx_bmp_arr = rgb_img()

    def __call__(self, flex_data_in, flex_mask_in, show_nums = False,
                 i_min = -3.0, i_max = 200.0, palette = "hot ascend"):

        err_code = self.wx_bmp_arr.set_min_max(i_min, i_max)

        if palette == "black2white":
            palette_num = 1
        elif palette == "white2black":
            palette_num = 2
        elif palette == "hot ascend":
            palette_num = 3
        else: # assuming "hot descend"
            palette_num = 4

        img_array_tmp = self.wx_bmp_arr.gen_bmp(flex_data_in, flex_mask_in, show_nums, palette_num)

        np_img_array = img_array_tmp.as_numpy_array()

        height = np.size(np_img_array[:, 0:1, 0:1])
        width = np.size( np_img_array[0:1, :, 0:1])

        img_array = np.zeros([height, width, 4], dtype=np.uint8)

        #for some strange reason PyQt4 needs to use RGB as BGR
        img_array[:,:,0:1] = np_img_array[:,:,2:3]
        img_array[:,:,1:2] = np_img_array[:,:,1:2]
        img_array[:,:,2:3] = np_img_array[:,:,0:1]

        return img_array


class ImgPainter(MyQWidgetWithQPainter):

    def __init__(self, parent = None):
        super(ImgPainter, self).__init__()
        self.my_parent = parent

        self.img = None
        self.setMouseTracking(True)
        self.show()

        self.my_scale = 1.0

        self.img_width = 247
        self.img_height = 253
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
                print "failed to update i(x,y) label"

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
            #painter.setPen(Qt.blue)


            pen = QPen()  # creates a default pen
            #pen.setBrush(Qt.blue)
            pen.setBrush(QColor(75, 150, 200))

            if( self.my_scale >= 5.0 ):
                #pen.setStyle(Qt.DashDotLine)
                #pen.setStyle(Qt.DotLine)
                pen.setStyle(Qt.SolidLine)
                pen.setWidth(self.my_scale / 3.5)

            else:
                pen.setStyle(Qt.SolidLine)
                pen.setWidth(0.0)

            painter.setPen(pen)

            painter.drawPixmap(rect, pixmap)
            #painter.setFont(QFont("Monospace", 22))
            #painter.setFont(QFont("FreeMono", 22))

            if( self.flat_data_lst != None and self.my_parent.chk_box_show.checkState()):
                tmp_font = QFont()
                tmp_font.setPixelSize(int(5.5 * self.my_scale))
                #TODO consider "tmp_font.setPointSize(..." instead of "tmp_font.setPixelSize(..."
                painter.setFont(tmp_font)

                for reflection in self.flat_data_lst:
                    x = float(reflection.box[0])
                    y = float(reflection.box[1])
                    width = float(reflection.box[2])
                    height = float(reflection.box[3])
                    rectangle = QRectF(x * self.my_scale, y * self.my_scale,
                                       width * self.my_scale, height * self.my_scale)
                    painter.drawRect(rectangle)

                    if( reflection.hkl !=None and self.my_scale > self.my_parent.t_hold ):
                        painter.drawText( QPoint(int((x + width) * self.my_scale),
                                          int(y * self.my_scale)),  reflection.hkl)

            painter.end()


class build_qimg(object):
    def __init__(self):
        self.arr_img = img_w_cpp()

    def __call__ (self, img_flex, palette_in, min_i, max_i):
        flex_2d_data = img_flex.as_double()
        flex_2d_mask = flex.double(flex.grid(flex_2d_data.all()[0], flex_2d_data.all()[1]), 0)
        arr_i = self.arr_img(flex_2d_data, flex_2d_mask, i_min = min_i, i_max = max_i, palette = palette_in)

        q_img = QImage(arr_i.data, np.size(arr_i[0:1, :, 0:1]),
                       np.size(arr_i[:, 0:1, 0:1]), QImage.Format_RGB32)

        return q_img


class PopImgChange(QMenu):
    def __init__(self, parent=None):
        super(PopImgChange, self).__init__(parent)
        self.my_parent = parent

        top_box = QHBoxLayout()

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

        my_layout = QVBoxLayout()

        my_layout.addLayout(top_box)
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

        top_box = QHBoxLayout()
        top_box.addWidget(QLabel("scale threshold 1"))
        top_box.addWidget(self.my_parent.t_hold_edit)

        bot_box = QHBoxLayout()
        bot_box.addWidget(self.my_parent.chk_box_show)

        my_box = QVBoxLayout()
        my_box.addLayout(top_box)
        my_box.addLayout(bot_box)

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
        self.my_scrollable = QScrollArea()
        self.my_painter = ImgPainter(self)
        self.my_scrollable.setWidget(self.my_painter)

        max_min_validator = QIntValidator(-5, 9995, self)

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

        self.t_hold = 3.0
        self.t_hold_edit = QLineEdit()
        self.t_hold_edit.setFixedWidth(6 * sys_font_point_size)
        #self.t_hold_edit.setValidator(QFloatValidator(2.0, 20,0, self)  )
        self.t_hold_edit.setText(str(self.t_hold))
        #self.t_hold_edit.editingFinished.connect(self.min_changed_by_user)
        self.t_hold_edit.editingFinished.connect(self.change_scale_thold)

        self.chk_box_show = QCheckBox("show reflection info")

        self.palette_select = QComboBox()

        self.palette_lst = ["hot ascend", "hot descend", "black2white", "white2black"]
        self.palette = self.palette_lst[0]
        for plt in self.palette_lst:
            self.palette_select.addItem(plt)

        self.palette_select.currentIndexChanged.connect(self.palette_changed_by_user)


        img_select_but = QPushButton('Img Select')
        img_select_but.setMenu(PopImgChange(self))

        img_pal_but = QPushButton('Img Palette')
        img_pal_but.setMenu(PopImgTreat(self))

        info_but = QPushButton('Info Handling')
        info_but.setMenu(PopInfoHandl(self))


        self.img_num = 0
        self.my_sweep = None
        self.flat_data_lst = [None]
        self.current_qimg = build_qimg()

        if( json_file_path == None ):
            print "\n\n no datablock given \n\n"
            n_of_imgs = 1

        else:
            self.ini_datablock(json_file_path)

        if( pckl_file_path == None ):
            print "\n\n no pickle file given \n\n"

        else:
            self.ini_reflection_table(pckl_file_path)

        if( self.my_sweep != None):
            self.set_img()

        #self.img_select.setValue(0)
        self.img_select.valueChanged.connect(self.img_changed_by_user)
        #valueChanged.connect

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
                print"\n self.my_sweep.get_array_range() =", self.my_sweep.get_array_range()
                print "self.my_sweep.get_image_size() =", self.my_sweep.get_image_size()
                n_of_imgs = len(self.my_sweep.indices())
                print "n_of_imgs =", n_of_imgs

                self.img_select.setMaximum(n_of_imgs)
                self.img_select.setMinimum(1)

                '''
                self.img_select.setMaxCount(n_of_imgs)
                for num in xrange(n_of_imgs):
                    labl = "img#" + str(num + 1)
                    self.img_select.addItem(labl)
                '''

            except:
                print "Failed to load images from  datablock.json"


    def ini_reflection_table(self, pckl_file_path):
        if( pckl_file_path != None ):

            print "[pickle file] =", pckl_file_path
            table = flex.reflection_table.from_pickle(pckl_file_path)
            print "table =", table
            local_bbox = table[5]['bbox']
            print "local_bbox =", local_bbox
            print "len(table) = ", len(table)

            n_refs = len(table)

            self.flat_data_lst = []

            if( self.img_select.maximum() > 0 ):
                firts_time = time_now()

                for img_num in xrange(self.img_select.maximum()):
                    tmp_lst = []
                    self.flat_data_lst.append(tmp_lst)

                for i in xrange(n_refs):
                    local_bbox = table[i]['bbox']
                    z_boud = local_bbox[4:6]
                    x_ini = local_bbox[0]
                    y_ini = local_bbox[2]
                    width = local_bbox[1] - local_bbox[0]
                    height = local_bbox[3] - local_bbox[2]

                    try:
                        local_hkl = str(table[i]['miller_index'])

                    except:
                        local_hkl = None

                    for idx in xrange( int(z_boud[0]), int(z_boud[1]) ):
                        reflection_data = flat_data()
                        reflection_data.box = [x_ini, y_ini, width, height]

                        reflection_data.hkl = local_hkl

                        self.flat_data_lst[idx].append(reflection_data)

                print "\n\n building flat_data_lst (diff time) =", time_now() - firts_time, "\n"
        else:
            self.flat_data_lst = [None]

        if( self.my_sweep != None):
            self.set_img()

    def set_img(self):

        print "New self.img_num =", self.img_num
        self.img_arr = self.my_sweep.get_raw_data(self.img_num - 1)[0]

        if(self.flat_data_lst == [None]):
            self.my_painter.set_img_pix(self.current_qimg(self.img_arr, self.palette,
                                                          self.i_min, self.i_max))

        else:
            self.my_painter.set_img_pix(self.current_qimg(self.img_arr, self.palette,
                                                          self.i_min, self.i_max),
                                                          self.flat_data_lst[self.img_num - 1])

    def btn_play_clicked(self):
        print "btn_play_clicked(self)"

        self.video_timer = QTimer(self)
        self.video_timer.timeout.connect(self.btn_next_clicked)
        self.video_timer.start(1)

    def btn_stop_clicked(self):
        print "B_stop_clicked(self)"
        self.video_timer.stop()

    def change_scale_thold(self):
        self.t_hold = float(self.t_hold_edit.text())
        print "self.t_hold =", self.t_hold
        self.set_img()

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
        self.img_num = 1
        self.img_select.setValue(self.img_num)

    def btn_rev_clicked(self):
        self.img_num -= 10
        if( self.img_num < 1 ):
            self.img_num = 1

        self.img_select.setValue(self.img_num)

    def btn_prev_clicked(self):
        self.img_num -= 1
        if( self.img_num < 1 ):
            self.img_num = 1

        self.img_select.setValue(self.img_num)

    def btn_next_clicked(self):
        self.img_num += 1
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



