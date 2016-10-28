'''
iDIALS mode higher level DUI QWidget

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

import sys, os

from python_qt_bind import *

from custom_widgets import StepList
from idials_gui import IdialsInnerrWidget, TextOut
from outputs_gui import outputs_widget


class OverlayPaintWidg(QWidget):
    def __init__(self, parent = None):
        super(OverlayPaintWidg, self).__init__(parent)

        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)

        self.setPalette(palette)
        self.pos_n = 1.0
        self.n_of_pos = 64.0
        self.my_timer = QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(800)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 50)))

        moving_block = '''
        x1 = int( (self.pos_n * float(self.width()) ) / self.n_of_pos)
        y1 = 0
        h = self.height()
        w = self.width() / self.n_of_pos
        x1 -= w
        '''

        x1 = 0
        y1 = 0
        h = self.height()
        w = int( (self.pos_n / self.n_of_pos) * float(self.width()) )

        rd = 1
        gr = (self.n_of_pos - self.pos_n) / self.n_of_pos  * 255
        bl = self.pos_n / self.n_of_pos * 255

        painter.drawRect(x1, y1, w, h)
        painter.fillRect(x1, y1, w, h, QColor(rd, gr, bl, 127))

        painter.setPen(QPen(Qt.NoPen))

    def update_cross(self):
        if(self.pos_n < self.n_of_pos):
            self.pos_n += 1.0
        else:
            self.pos_n = 1.0

    def on_timeout(self):
        self.update_cross()
        self.repaint()
        #self.update()


class Text_w_Bar(QWidget):
    def __init__(self, parent=None):
        super(Text_w_Bar, self).__init__(parent)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.info_line = QLineEdit()
        self.info_line.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.info_line.setText("Import images to start")
        self.info_line.setReadOnly(True)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(QMargins(0,0,0,0))
        self.verticalLayout.setSpacing(0)

        self.verticalLayout.addWidget(self.info_line)

        self.painted_overlay = OverlayPaintWidg(self.info_line)
        self.painted_overlay.hide()

    def start_motion(self):
        self.painted_overlay.setVisible(True)
        self.painted_overlay.pos_n = 1

    def end_motion(self):
        self.painted_overlay.setVisible(False)

    def resizeEvent(self, event):
        self.painted_overlay.resize(event.size())
        event.accept()


class CentreWidget( QWidget):
    def __init__(self, parent = None):
        super(CentreWidget, self).__init__(parent)

    def __call__(self, widget_buts = None, go_btn = None, param_widg = None):

        main_box = QVBoxLayout()
        main_box.setContentsMargins(QMargins(0,0,0,0))
        main_box.setSpacing(0)

        h_or_v_box = QHBoxLayout()
        h_or_v_box.setContentsMargins(QMargins(0,0,0,0))
        h_or_v_box.setSpacing(0)

        h_or_v_box.addWidget(widget_buts)
        h_or_v_box.addWidget(go_btn)
        main_box.addLayout(h_or_v_box)
        main_box.addWidget(param_widg)

        self.setLayout(main_box)
        self.show()


class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()

        buttons_widget = QWidget()
        #buttons_widget.setStyleSheet("background-color: solid gray")
        buttons_widget.setStyleSheet("background-color: lightgray")
        v_left_box =  QHBoxLayout()
        self.step_param_widg =  QStackedWidget()
        my_lst = StepList(parent = self)
        label_lst, self.widg_lst, icon_lst, self.command_lst = my_lst()

        #My_style = Qt.ToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setWindowTitle('DUI / idials')

        self.btn_lst = []
        for pos, step_data in enumerate(label_lst):
            print "pos = ", pos
            #new_btn = QToolButton(self)
            new_btn = QPushButton(self)

            new_btn.setToolTip(step_data)
            new_btn.setIcon(icon_lst[pos])
            new_btn.setIconSize(QSize(48, 48))
            new_btn.par_wig = self.widg_lst[pos]
            new_btn.command = self.command_lst[pos]

            #new_btn.setText(step_data)
            #new_btn.setToolButtonStyle(My_style)
            #new_btn.setFont(QFont("Monospace", 10, QFont.Bold))

            new_btn.clicked.connect(self.btn_clicked)

            v_left_box.addWidget(new_btn)
            self.step_param_widg.addWidget(new_btn.par_wig)
            self.btn_lst.append(new_btn)


        idials_path = os.environ["IDIALS_PATH"]
        dials_logo_path = str(idials_path + "/resources/DIALS_Logo_smaller_centred.png")

        buttons_widget.setLayout(v_left_box)
        self._refrech_btn_look()

        v_control_splitter = QSplitter()
        v_control_splitter.setOrientation(Qt.Vertical)
        #v_control_splitter.setOrientation(Qt.Horizontal)

        self.btn_go =  QPushButton('Run', self)

        self.btn_go.setIcon(QIcon(dials_logo_path))
        self.btn_go.setIconSize(QSize(80, 48))

        self.btn_go.clicked.connect(self.btn_go_clicked)

        centre_widget = CentreWidget(self)
        centre_widget(buttons_widget, self.btn_go, self.step_param_widg)
        v_control_splitter.addWidget(centre_widget)

        self.idials_widget = IdialsInnerrWidget(self, dials_logo_path)
        self.idials_widget.rtime_txt_on = True
        v_control_splitter.addWidget(self.idials_widget)

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)
        self.output_wg = outputs_widget(self)
        self.txt_out = self.output_wg.in_txt_out
        h_main_splitter.addWidget(v_control_splitter)
        h_main_splitter.addWidget(self.output_wg)

        main_widget = QWidget()
        main_box = QVBoxLayout()

        main_box.setContentsMargins(QMargins(0,0,0,0))
        main_box.setSpacing(0)

        main_box.addWidget(h_main_splitter)

        self.bottom_bar_n_info = Text_w_Bar()
        main_box.addWidget(self.bottom_bar_n_info)
        main_widget.setLayout(main_box)
        self.running = False

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        fileMenu.addAction("&Open...", self.openFile, "Ctrl+O")
        fileMenu.addAction("E&xit", self.quit, "Ctrl+Q")

        configMenu = menubar.addMenu('config')
        configMenu.addAction("T&oggle real time text", self.togle_text_rt, "Ctrl+T")

        self.resize(1200, 900)
        self.setCentralWidget(main_widget)
        self.show()

    def openFile(self):
        print "openFile"

    def quit(self):
        print "quit"

    def togle_text_rt(self):
        print "self.idials_widget.rtime_txt_on =", self.idials_widget.rtime_txt_on
        if( self.idials_widget.rtime_txt_on == True):
            self.idials_widget.rtime_txt_on = False

        else:
            self.idials_widget.rtime_txt_on = True
        print "self.idials_widget.rtime_txt_on =", self.idials_widget.rtime_txt_on
        print "Toggle real time text"

    def param_changed(self, new_par_str):
        print "\n MainWidget, param_changed, new_par_str =", new_par_str
        self.idials_widget.change_parameter(new_par_str)

    def btn_go_clicked(self):
        if( self.running == False ):
            self.idials_widget.run_clicked()
            self.running = True

    def start_pbar_motion(self):
        self.bottom_bar_n_info.info_line.setText("Running")
        self.bottom_bar_n_info.start_motion()

    def update_pbar_text(self, rtime_text):
        self.bottom_bar_n_info.info_line.setText(rtime_text)
        self.bottom_bar_n_info.painted_overlay.repaint()

    def end_pbar_motion(self):
        self.bottom_bar_n_info.info_line.setText("Done")
        self.bottom_bar_n_info.end_motion()
        print "controller.get_current().success =", self.idials_widget.controller.get_current().success
        self.running = False

        #FIXME controller.get_current().name == "refine_bravais_settings" is NOT the acurate
        #FIXME way to find output the current parameter widget

        if( self.idials_widget.controller.get_current().success == True ):
            if( self.idials_widget.controller.get_current().name == "import" ):
                self.current_widget.success_stat = True

            elif( self.idials_widget.controller.get_current().name == "refine_bravais_settings" ):
                print "\n ________________________ <<< Time to show the table \n"
                sumr_path = self.idials_widget.controller.get_summary()
                self.current_widget.add_opts_lst(in_json_path = sumr_path)

            else:
                print "Time to update html << report >>"
                #put here something that calls << self.update_report
                repr_path = self.idials_widget.controller.get_report()
                self.update_report(repr_path)

        else:
            print "\n\n something went WRONG \n"
            #TODO show in the GUI that something went WRONG


    def update_report(self, report_path):
        print "\n MainWidget update report with:", report_path
        self.output_wg.web_view.update_page(report_path)

    def _refresh_stacked_widget(self, new_widget):
        self.step_param_widg.setCurrentWidget(new_widget)
        self._refrech_btn_look()
        self.current_widget = new_widget

        try:
            print "controller.get_current().name =", self.idials_widget.controller.get_current().name
            self.current_widget()
            print "controller.get_current().success =", self.idials_widget.controller.get_current().success

        except:
            print "\n no __call__ in ", self.current_widget, "\n"

    def btn_clicked(self):
        if( self.running == False ):
            my_sender = self.sender()
            self.idials_widget.change_mode(my_sender.command)
            self._refresh_stacked_widget(my_sender.par_wig)
            my_sender.setStyleSheet("background-color: lightblue")

    def _refrech_btn_look(self):
        for btn in self.btn_lst:
            btn.setStyleSheet("background-color: lightgray")


    def jump(self, cmd_name = None, new_url = None):
        if( self.running == False ):
            print "\n MainWidget swishing to", cmd_name, "\n\n"
            for pos, widget_search in enumerate(self.command_lst):
                if( widget_search == cmd_name ):
                    print "Widget in pos:", pos
                    self._refresh_stacked_widget(self.widg_lst[pos])
                    self.btn_lst[pos].setStyleSheet("background-color: lightblue")

            if new_url != None:
                self.update_report(new_url)


    def opt_picked(self, opt_num):
        if( self.running == False ):
            print "\n from idials_main_widget.py MainWidget"
            print "opt_num =", opt_num, " \n"

            self.idials_widget.change_mode("reindex")
            str_par = "solution=" + str(opt_num)
            print "\n change_parameter =", str_par
            self.idials_widget.change_parameter(str_par)


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())



