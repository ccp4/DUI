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

from custom_widgets import StepList, TmpRedinexWidget
from idials_gui import IdialsInnerrWidget
from outputs_gui import outputs_widget
from dynamic_reindex_gui import MyReindexOpts
from outputs_gui import InfoWidget

class Text_w_Bar(QProgressBar):

    def __init__(self, parent):
        super(Text_w_Bar,self).__init__()
        self.setAlignment(Qt.AlignCenter)
        self._text = ""

    def setText(self, text):
        self._text = text

    def text(self):
        return self._text

    def start_motion(self):
        print "starting motion"
        self.setRange(0, 0)

    def end_motion(self):
        self.setRange(0, 1)
        print "ending motion"


class CentreWidget( QWidget):
    def __init__(self, parent = None):
        super(CentreWidget, self).__init__(parent)

    def __call__(self, widget_buts = None, btn_stop = None, go_btn = None, param_widg = None):

        main_box = QVBoxLayout()
        #main_box.setContentsMargins(QMargins(0,0,0,0))
        main_box.setSpacing(0)

        main_box.addWidget(widget_buts)

        stop_n_go_box = QHBoxLayout()
        #stop_n_go_box.setContentsMargins(QMargins(0,0,0,0))
        stop_n_go_box.setSpacing(0)
        stop_n_go_box.addWidget(btn_stop)
        stop_n_go_box.addWidget(go_btn)

        main_box.addLayout(stop_n_go_box)

        main_box.addWidget(param_widg)

        self.setLayout(main_box)
        self.show()


def check_previous_runs():
    #print "\n\n", dir(os), "\n\n"
    print "os.path.exists(\"dials.state\") =", os.path.exists("dials.state")

    if( os.path.exists("dials.state") ):
        msgBox = QMessageBox()
        msgBox.setText("DUI Already ran from same dir")
        msgBox.setInformativeText("Reload?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()

        print "\n ret =\n", ret, "\n"
        if( ret == QMessageBox.Yes ):
            print "Clicked YES \n"

        elif( ret ==  QMessageBox.Cancel ):
            print "Clicked CANCEL \n"
            return False

        else:
            print "Clicked NO \n"
            os.rename("dials.state", "dials.state.old")

    return True

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.super_parent = self

        print "\n MainWidget(ID) =", self.winId(), "\n"

        print "sys.argv =", sys.argv, "\n"

        ini_template_path = None
        if( len(sys.argv) > 1 ):
            ini_template_path = sys.argv[1]
            print "must import with template:", ini_template_path, "\n"
            if( os.path.exists("dials.state") ):
                os.rename("dials.state", "dials.state.old")

        else:
            do_continue = check_previous_runs()
            if( do_continue == False ):
                sys.exit()

        # This flag will define the layout orientation of the left side
        # area of the GUI and therefore needs to be taking into account when
        # the rest of the GUI gets build
        self.embedded_reindex = False

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
            new_btn.setIconSize(QSize(38, 38))
            new_btn.par_wig = self.widg_lst[pos]
            new_btn.command = self.command_lst[pos]

            #new_btn.setText(step_data)
            #new_btn.setToolButtonStyle(My_style)
            #new_btn.setFont(QFont("Monospace", 10, QFont.Bold))

            new_btn.clicked.connect(self.btn_clicked)

            v_left_box.addWidget(new_btn)
            self.step_param_widg.addWidget(new_btn.par_wig)
            self.btn_lst.append(new_btn)


        if( self.embedded_reindex ):
            self.reindex_tool = MyReindexOpts(self)
            self.step_param_widg.addWidget(self.reindex_tool)

        else:
            self.reindex_tool = None
            self.tmp_reindex_widg = TmpRedinexWidget(self)
            self.step_param_widg.addWidget(self.tmp_reindex_widg)

        idials_gui_path = os.environ["IDIALS_GUI_PATH"]
        dials_logo_path = str(idials_gui_path + "/resources/DIALS_Logo_smaller_centred.png")

        buttons_widget.setLayout(v_left_box)
        self._refrech_btn_look()

        self.btn_stop = QPushButton("\n  Stop  \n", self)
        #self.btn_stop.setContentsMargins(QMargins(0,0,0,0))
        self.btn_stop.setIcon(QIcon.fromTheme("process-stop"))

        self.btn_go =  QPushButton('\n          Run              \'\n', self)
        self.btn_go.setIcon(QIcon(dials_logo_path))
        self.btn_go.setIconSize(QSize(80, 48))
        self.btn_go.clicked.connect(self.btn_go_clicked)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)
        self.idials_widget = IdialsInnerrWidget(self, dials_logo_path)
        self.idials_widget.rtime_txt_on = True
        self.grayed_out_buttons = True
        self.next_step_on = True
        centre_widget = CentreWidget(self)
        centre_widget(buttons_widget, self.btn_stop, self.btn_go, self.step_param_widg)

        v_control_splitter = QSplitter()

        '''
        v_control_splitter.setOrientation(Qt.Horizontal)
        v_control_splitter.addWidget(self.idials_widget)
        v_control_splitter.addWidget(centre_widget)
        '''

        if( self.embedded_reindex ):
            v_control_splitter.setOrientation(Qt.Vertical)
            v_control_splitter.addWidget(centre_widget)
            v_control_splitter.addWidget(self.idials_widget)

        else:
            v_control_splitter.setOrientation(Qt.Horizontal)
            v_control_splitter.addWidget(self.idials_widget)
            v_control_splitter.addWidget(centre_widget)

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)
        self.output_wg = outputs_widget(self)
        self.txt_out = self.output_wg.in_txt_out

        control_p_info_splitt = QSplitter()
        control_p_info_splitt.setOrientation(Qt.Vertical)
        self.info_widget = InfoWidget(self)
        control_p_info_splitt.addWidget(v_control_splitter)
        scrollArea = QScrollArea()
        scrollArea.setWidget(self.info_widget)
        control_p_info_splitt.addWidget(scrollArea)


        #scrollArea = QScrollArea()
        #scrollArea.setWidget(self.scrollable_widget)


        h_main_splitter.addWidget(control_p_info_splitt)
        h_main_splitter.addWidget(self.output_wg)


        main_box = QVBoxLayout()

        main_box.setContentsMargins(QMargins(0,0,0,0))
        main_box.setSpacing(0)

        main_box.addWidget(h_main_splitter)


        self.bottom_bar_n_info = Text_w_Bar(self)
        main_box.addWidget(self.bottom_bar_n_info)
        self.running = False


        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        fileMenu.addAction("&Import...", self.openFile, "Ctrl+I")
        fileMenu.addAction("E&xit", self.quit, "Ctrl+Q")

        configMenu = menubar.addMenu('config')
        #configMenu.addAction("T&oggle real time text", self.togle_text_rt, "Ctrl+T")
        configMenu.addAction("Real time log text in Pbar", self.togle_text_rt)
        configMenu.addAction("Automatic gray out buttons", self.togle_gray_out)
        configMenu.addAction("Automatic go to next step", self.togle_auto_next_step)
        #starting where it left before
        ini_index = self.idials_widget.controller.get_current().index
        print "self.idials_widget.controller.get_current().index =", ini_index

        if( ini_index == 0 ):
            print "\n Running for first time in this dir \n"
            self._gray_unwanted()

            #TODO Think a bit if you are going a bit
            #back and forward with the next line
            self.idials_widget.update_info()

        else:
            print "\n Already run at least one command here \n"
            self.idials_widget.goto(ini_index)


        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

        if( ini_template_path != None ):
            print "\n\n Time to import with template:"
            print ini_template_path, "\n"


    def closeEvent(self, event):
        try:
            self.reindex_tool.close()
            self.reindex_tool = None
        except:
            print "no need to close reindex tool"

        self.close()

    def _active_btn(self, my_sender):
        self.idials_widget.change_mode(my_sender.command)
        self._refresh_stacked_widget(my_sender.par_wig)
        my_sender.setStyleSheet("background-color: lightblue")
        self.btn_go.setText(str(my_sender.command))

        try:
            my_sender.par_wig.sipler_widget.set_max_nproc()
            print "\n Tunning nproc to maximum \n"

        except:
            print "\n This step runs as fas as it can with nproc = 1 \n"



    def openFile(self):
        print "openFile"
        if( self.running == False ):
            my_sender = self.btn_lst[0]
            # this is not the only place where _active_btn gets called
            self._active_btn(my_sender)

    def quit(self):
        print "quit"
        self.closeEvent(QCloseEvent)

    def _find_next(self, current_command = None):

        if( current_command == "index" or current_command =="reindex" or current_command == "integrate" ):
            cmd_next = "refine"

        elif( current_command == "clean" ):
            cmd_next = "import"

        else:
            cmd_next = None
            for pos, cmd in enumerate(self.command_lst):
                if( cmd == current_command ):
                    cmd_next = self.command_lst[pos + 1]

        return cmd_next

    def _gray_unwanted(self):
        for btn in self.btn_lst:
            btn.setEnabled(True)

        if( self.grayed_out_buttons == True ):
            current_command = self.idials_widget.controller.get_current().name
            print "current_command =", current_command
            cmd_next = self._find_next(current_command)

            for btn in self.btn_lst:
                print btn.command
                if( btn.command == cmd_next ):
                    btn.setEnabled(True)
                else:
                    btn.setEnabled(False)

    def togle_auto_next_step(self):
        if( self.next_step_on == True):
            self.next_step_on = False

        else:
            self.next_step_on = True

        print "self.next_step_on =", self.next_step_on


    def togle_text_rt(self):
        print "self.idials_widget.rtime_txt_on =", self.idials_widget.rtime_txt_on
        if( self.idials_widget.rtime_txt_on == True):
            self.idials_widget.rtime_txt_on = False

        else:
            self.idials_widget.rtime_txt_on = True

        print "self.idials_widget.rtime_txt_on =", self.idials_widget.rtime_txt_on

    def togle_gray_out(self):
        print "self.grayed_out_buttons =", self.grayed_out_buttons
        if( self.grayed_out_buttons == True):
            self.grayed_out_buttons = False

        else:
            self.grayed_out_buttons = True

        print "self.grayed_out_buttons =", self.grayed_out_buttons
        self._gray_unwanted()

    def param_changed(self, new_par_str):
        print "\n MainWidget, param_changed, new_par_str =", new_par_str
        self.idials_widget.change_parameter(new_par_str)

    def reset_param(self):
        self.idials_widget.param_reset()

    def btn_stop_clicked(self):
        if( self.running == True ):
            #self._gray_unwanted()
            self.idials_widget.stop_clicked()
            self.running = False

    def btn_go_clicked(self):

        print "self.running =", self.running
        print "self.idials_widget.failed =", self.idials_widget.failed
        print "...controller.get_current().success", self.idials_widget.controller.get_current().success

        unstable_if_test = '''
        if( self.running == False and
            self.idials_widget.controller.get_current().success == True ):
        '''

        if( self.running == False and self.idials_widget.failed == None ):

            self._gray_unwanted()
            self.idials_widget.run_clicked()
            self.running = True

    def pop_reindex_gui(self):
        print "  <<< Time to show the table "
        sumr_path = self.idials_widget.controller.get_summary()
        if( self.embedded_reindex ):
            self.step_param_widg.setCurrentWidget(self.reindex_tool)
            self.reindex_tool.set_ref(parent = self , in_json_path = sumr_path)

        else:
            self.reindex_tool = MyReindexOpts()
            self.step_param_widg.setCurrentWidget(self.tmp_reindex_widg)
            self.reindex_tool.set_ref(parent = self , in_json_path = sumr_path)

        self.btn_go.setText("reindex")

    def start_pbar_motion(self):
        self.bottom_bar_n_info.setText("Running")
        self.bottom_bar_n_info.start_motion()

    def update_pbar_text(self, rtime_text):
        if( len(rtime_text) > 3):
            self.bottom_bar_n_info.setText(rtime_text)

    def update_after_command_end(self):
        self.bottom_bar_n_info.end_motion()
        self.bottom_bar_n_info.setText("Done")
        print "controller.get_current().success =", self.idials_widget.controller.get_current().success
        self.running = False

        current_command = self.idials_widget.controller.get_current().name

        print "\n\n current_command ==", current_command, "\n\n"

        if( self.idials_widget.controller.get_current().success == True ):
            update_GUI = True
            try:
                repr_path = self.idials_widget.controller.get_report()
                self.update_report(repr_path)
            except:
                print "Not supposed to update report"

            if( current_command == "clean" ):
                print "\n\n <<< failed to import  >>> \n\n"

            elif( current_command == "import" ):
                self.current_widget.success_stat = True

            elif( current_command == "refine_bravais_settings" ):
                self.pop_reindex_gui()

            elif( current_command == "index" ):
                self.idials_widget.change_mode("refine_bravais_settings")
                print "\n  running << refine_bravais_settings >> \n"
                update_GUI = False
                self.btn_go_clicked()

            elif( current_command == "reindex" ):
                print "Time to shrink back reindex GUI"

                if( not(self.embedded_reindex) ):
                    self.reindex_tool.close()
                    self.reindex_tool = None

            elif( current_command == "integrate" ):
                self.idials_widget.change_mode("export")
                self.btn_go_clicked()

            elif(current_command != "export"):
                print "Time to update html << report >>"

            if( update_GUI == True ):
                self._gray_unwanted()
                self._update_img()
                #TODO Think a bit if you are going a bit
                #back and forward with the next line
                self.idials_widget.update_info()
                self.check_next(current_command)

        else:
            print "\n\n something went WRONG \n"
            #TODO show in the GUI that something went WRONG


    def _update_img(self):
        print "attempting to update imgs"
        json_file_path = None
        refl_pikl_path = None

        try:
            json_file_path = str(self.idials_widget.controller.get_current().datablock)
            print "\n images from:", json_file_path, "\n"

        except:
            print "\n <<< trying deeper search for datablock.json"

            try:
                #current = self.controller.get_current()
                #previous = current.parent
                current = self.idials_widget.controller.get_current()
                for times in xrange(50):
                    previous = current.parent
                    if( str(previous.name) =="import"  ):
                        print "found <<< import >>> "

                        json_file_path = str(previous.datablock)
                        print "\n images from:", json_file_path, "\n\n"
                        break

                    else:
                        print "tmp step = ", current.name
                        current = previous

            except:
                print "<<<  failed to find datablock.json  >>>"

        try:
            refl_pikl_path = self.idials_widget.controller.get_current().reflections

        except:
            print "failed to find << refl_pikl_path >>"

        self.output_wg.img_view.ini_datablock(json_file_path)
        self.output_wg.img_view.ini_reflection_table(refl_pikl_path)

        to_work_on_in_the_future = '''

        try:
            exp_json_path = self.idials_widget.controller.get_current().experiments
            print "exp_json_path =", exp_json_path

        except:
            print "failed to find << exp_json_path >>"

        '''



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
            # this is not the only place where _active_btn gets called
            self._active_btn(my_sender)


    def _refrech_btn_look(self):
        for btn in self.btn_lst:
            btn.setStyleSheet("background-color: lightgray")


    def check_next(self, current_command = "clean"):
        print "\n check_next(self)"
        print "current_command =", current_command, "\n"

        print "self.next_step_on =", self.next_step_on


        if( self.next_step_on == True ):
            if( current_command == "clean"):
                print "self.idials_widget.failed =", self.idials_widget.failed

                print "...controller.get_current().success", self.idials_widget.controller.get_current().success

                if( self.idials_widget.failed == None ):
                   self.btn_go_clicked()

                else:
                    print "\n\n Failed to import \n\n"

            else:
                next_command = self._find_next(current_command)
                print "next_command =", next_command, "\n"

                for btn in self.btn_lst:
                    print btn.command
                    if( btn.command == next_command ):
                        self._active_btn(btn)


    def jump(self, cmd_name = None, new_url = None):

        #TODO cmd_name does not have any use any more
        if( self.running == False ):
            if new_url != None:
                self.update_report(new_url)

            if( self.idials_widget.controller.get_current().name == "refine_bravais_settings" ):
                self.pop_reindex_gui()

            else:
                if( not(self.embedded_reindex) ):
                    if( self.reindex_tool != None ):
                        self.reindex_tool.close()
                        self.reindex_tool = None

                self.check_next(self.idials_widget.controller.get_current().name)

            self._gray_unwanted()

        self._update_img()

    def opt_picked(self, opt_num):

        if( self.running == False ):
            print "\n opt_num =", opt_num, " \n"
            self.idials_widget.change_mode("reindex")
            str_par = "solution=" + str(opt_num)
            print "\n change_parameter =", str_par, "\n"
            self.idials_widget.change_parameter(str_par)

            if( self.old_opnum == opt_num ):
                print "\n Supposed to run reindex NOW \n"
                self.btn_go_clicked()

            self.old_opnum = opt_num


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())




