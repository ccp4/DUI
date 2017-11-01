'''
DUI's most central gidgets

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
from PyQt4.QtWebKit import *

from outputs_n_viewers.web_page_view import WebTab
from outputs_n_viewers.img_viewer import MyImgWin

import sys, os, psutil
import pickle
from cli_utils import TreeShow, get_next_step
from m_idials import Runner
from gui_utils import CliOutView, Text_w_Bar
from outputs_gui import InfoWidget
from dynamic_reindex_gui import MyReindexOpts
import subprocess

from custom_widgets import  ParamWidget


widg_name_list = ["import", "find_spots", "index", "refine_bravais_settings", "refine", "integrate"]

def build_command_tip(command_lst):
    if(command_lst == [None]):
        str_tip = "?"

    else:
        str_tip = "dials."+ str(command_lst[0])
        for new_cmd in command_lst[1:]:
            str_tip += "\n  " + str(new_cmd)

    return str_tip

def update_info(main_obj):
    main_obj.cli_tree_output(main_obj.idials_runner)
    new_html = main_obj.idials_runner.get_html_report()
    new_img_json = main_obj.idials_runner.get_datablock_path()
    new_ref_pikl = main_obj.idials_runner.get_reflections_path()

    tmp_curr = main_obj.idials_runner.current_node
    if(tmp_curr.success == None):
        tmp_curr = tmp_curr.prev_step

    uni_json = tmp_curr.json_file_out



    print "\n new_html =", new_html , "\n"
    print " new_img_json =", new_img_json , "\n"
    print " new_ref_pikl =", new_ref_pikl , "\n"

    if(main_obj.cur_html != new_html):
        main_obj.cur_html = new_html
        try:
            main_obj.web_view.update_page(new_html)

        except:
            print "No HTML here"

    if(main_obj.cur_pick != new_ref_pikl):
        main_obj.cur_pick = new_ref_pikl
        main_obj.img_view.ini_reflection_table(main_obj.cur_pick)

    if(main_obj.cur_json != new_img_json):
        main_obj.cur_json = new_img_json
        main_obj.img_view.ini_datablock(main_obj.cur_json)


    main_obj.info_widget.update_data(exp_json_path = uni_json,
                                     refl_pikl_path = new_ref_pikl)


class MyThread(QThread):

    str_print_signal = pyqtSignal(str)
    str_fail_signal = pyqtSignal()

    def __init__(self, parent = None):
        super(MyThread, self).__init__()

    def __call__(self, cmd_to_run, ref_to_controler):
        self.cmd_to_run = cmd_to_run
        self.ref_to_controler = ref_to_controler
        self.start()

    def run(self):
        self.ref_to_controler.run(command = self.cmd_to_run, ref_to_class = self)

    def emit_print_signal(self, str_lin):
        #print str_lin, "... Yes"
        self.str_print_signal.emit(str_lin)

    def emit_fail_signal(self):
        self.str_fail_signal.emit()

def kill_w_child(pid_num):
    print "attempting to kill pid #:", pid_num
    parent_proc = psutil.Process(pid_num)
    for child in parent_proc.children(recursive=True):  # or parent_proc.children() for recursive=False
        child.kill()

    parent_proc.kill()


class TreeNavWidget(QTreeView):
    def __init__(self, parent = None):
        super(TreeNavWidget, self).__init__()
        print "TreeNavWidget(__init__)"

    def update_me(self, root_node, lst_path_idx):
        self.lst_idx = lst_path_idx

        print self.lst_idx

        self.std_mod = QStandardItemModel(self)
        self.recursive_node(root_node, self.std_mod)

        self.std_mod.setHorizontalHeaderLabels(["History Tree"])
        self.setModel(self.std_mod)
        self.expandAll()

    def recursive_node(self, root_node, item_in):
        if(len(root_node.next_step_list) > 0):
            for child_node in root_node.next_step_list:
                if(child_node.command_lst != [None]):
                    child_node_name = str(child_node.command_lst[0])

                elif(child_node.success == None):
                    child_node_name = "* None *"

                else:
                    child_node_name = " ? None ? "

                try:
                    child_node_tip = build_command_tip(child_node.command_lst)

                except:
                    child_node_tip = "None"

                new_item = QStandardItem(child_node_name)
                new_item.setToolTip(child_node_tip)
                new_item.idials_node = child_node

                if(self.lst_idx == child_node.lin_num):
                    new_item.setBackground(Qt.blue)
                    if(child_node.success == None):
                        new_item.setForeground(Qt.green)

                    elif(child_node.success == True):
                        new_item.setForeground(Qt.white)

                    elif(child_node.success == False):
                        new_item.setForeground(Qt.red)

                else:
                    new_item.setBackground(Qt.white)
                    if(child_node.success == None):
                        new_item.setForeground(Qt.green)

                    elif(child_node.success == True):
                        new_item.setForeground(Qt.blue)

                    elif(child_node.success == False):
                        new_item.setForeground(Qt.red)

                new_item.setEditable(False)      # not letting the user edit it

                self.recursive_node(child_node, new_item)
                item_in.appendRow(new_item)


class CentreWidget(QWidget):

    user_changed = pyqtSignal(str)
    update_command_lst = pyqtSignal(list)

    def __init__(self, parent = None):
        super(CentreWidget, self).__init__()

        idials_gui_path = str(os.environ["IDIALS_GUI_PATH"])
        print "idials_gui_path =", idials_gui_path

        lst_icons_path = []
        lst_icons_path.append(idials_gui_path + "/resources/import.png")
        lst_icons_path.append(idials_gui_path + "/resources/find_spots.png")
        lst_icons_path.append(idials_gui_path + "/resources/index.png")
        lst_icons_path.append(idials_gui_path + "/resources/reindex.png")
        lst_icons_path.append(idials_gui_path + "/resources/refine.png")
        lst_icons_path.append(idials_gui_path + "/resources/integrate.png")

        lst_grayed_icons_path = []
        lst_grayed_icons_path.append(idials_gui_path + "/resources/import_grayed.png")
        lst_grayed_icons_path.append(idials_gui_path + "/resources/find_spots_grayed.png")
        lst_grayed_icons_path.append(idials_gui_path + "/resources/index_grayed.png")
        lst_grayed_icons_path.append(idials_gui_path + "/resources/reindex_grayed.png")
        lst_grayed_icons_path.append(idials_gui_path + "/resources/refine_grayed.png")
        lst_grayed_icons_path.append(idials_gui_path + "/resources/integrate_grayed.png")


        top_box =  QHBoxLayout()
        self.step_param_widg = QStackedWidget()
        self.widg_lst = []
        self.btn_lst = []
        for num, step_name in enumerate(widg_name_list):
            new_btn = QPushButton(self)
            new_btn.setToolTip(step_name)

            tmp_ico = QIcon()
            tmp_ico.addFile(lst_icons_path[num], mode = QIcon.Normal)
            tmp_ico.addFile(lst_grayed_icons_path[num], mode = QIcon.Disabled)

            new_btn.setIcon(tmp_ico)
            new_btn.setIconSize(QSize(38, 38))
            new_btn.clicked.connect(self.btn_clicked)
            top_box.addWidget(new_btn)

            param_widg = ParamWidget(step_name)
            new_btn.pr_widg = param_widg
            self.step_param_widg.addWidget(param_widg)
            self.widg_lst.append(param_widg)
            param_widg.update_command_lst.connect(self.update_parent_lst)
            self.btn_lst.append(new_btn)


        ctrl_box = QHBoxLayout()

        self.repeat_btn = QPushButton("\n Re Try \n", self)
        re_try_icon_path = str(idials_gui_path +
                              "/resources/re_try.png")
        re_try_grayed_path = str(idials_gui_path +
                              "/resources/re_try_grayed.png")
        tmp_ico = QIcon()
        tmp_ico.addFile(re_try_icon_path, mode = QIcon.Normal)
        tmp_ico.addFile(re_try_grayed_path, mode = QIcon.Disabled)

        self.repeat_btn.setIcon(tmp_ico)
        self.repeat_btn.setIconSize(QSize(28, 28))
        ctrl_box.addWidget(self.repeat_btn)

        self.run_btn = QPushButton("\n  Run  \n", self)
        dials_logo_path = str(idials_gui_path +
                              "/resources/DIALS_Logo_smaller_centred.png")
        dials_grayed_path = str(idials_gui_path +
                                "/resources/DIALS_Logo_smaller_centred_grayed.png")
        tmp_ico = QIcon()
        tmp_ico.addFile(dials_logo_path, mode = QIcon.Normal)
        tmp_ico.addFile(dials_grayed_path, mode = QIcon.Disabled)

        self.run_btn.setIcon(tmp_ico)
        self.run_btn.setIconSize(QSize(80, 48))
        ctrl_box.addWidget(self.run_btn)

        self.stop_btn = QPushButton("\n  Stop  \n", self)
        stop_logo_path = str(idials_gui_path + "/resources/stop.png")
        stop_grayed_path = str(idials_gui_path + "/resources/stop_grayed.png")
        tmp_ico = QIcon()
        tmp_ico.addFile(stop_logo_path, mode = QIcon.Normal)
        tmp_ico.addFile(stop_grayed_path, mode = QIcon.Disabled)
        self.stop_btn.setIcon(tmp_ico)
        self.stop_btn.setIconSize(QSize(28, 28))
        ctrl_box.addWidget(self.stop_btn)

        big_v_box = QVBoxLayout()

        big_v_box.addLayout(ctrl_box)
        big_v_box.addLayout(top_box)

        big_v_box.addWidget(self.step_param_widg)

        self.setLayout(big_v_box)
        self.show()

    def update_parent_lst(self, command_lst):
        self.update_command_lst.emit(command_lst)

    def get_arg_obj(self, sys_arg_in):
        self.widg_lst[0].my_widget.get_arg_obj(sys_arg_in)

    def set_widget(self, nxt_cmd = None, curr_step = None):
        for widget in self.widg_lst:
            if(widget.my_label == nxt_cmd):
                self.step_param_widg.setCurrentWidget(widget)
                try:
                    widget.update_param(curr_step)

                except:
                    print "\n\n Unable to update params\n\n"

    def btn_clicked(self):
        print "btn_clicked"
        my_sender = self.sender()
        self.step_param_widg.setCurrentWidget(my_sender.pr_widg)
        self.user_changed.emit(my_sender.pr_widg.my_label)

        print "\n\n my_sender.pr_widg.my_label =", my_sender.pr_widg.my_label, "\n\n"
        command_lst = [str(my_sender.pr_widg.my_label)]
        self.update_command_lst.emit(command_lst)

    def gray_outs_all(self):
        for btn in self.btn_lst:
            btn.setEnabled(False)

    def gray_outs_from_lst(self, lst_nxt):
        self.gray_outs_all()

        for btn in self.btn_lst:
            for cmd_str in lst_nxt:
                if(str(btn.toolTip()) == cmd_str):
                    btn.setEnabled(True)


class ModeWidget(QWidget):

    def __init__(self, parent = None):
        super(ModeWidget, self).__init__()

        big_layout = QVBoxLayout()
        big_layout.addWidget(QLabel("Guide level"))
        self.rb_group = QButtonGroup()
        self.rb_group_box = QGroupBox()
        self.rb_group_box_layout = QVBoxLayout()
        self.rb_group_box.setLayout(self.rb_group_box_layout)

        self.rb_full_auto = QRadioButton("Fully Automatic")
        self.rb_group.addButton(self.rb_full_auto)
        self.rb_group_box_layout.addWidget(self.rb_full_auto)

        self.rb_semi_auto = QRadioButton("Semi Automatic")
        self.rb_group.addButton(self.rb_semi_auto)
        self.rb_group_box_layout.addWidget(self.rb_semi_auto)

        self.rb_expert = QRadioButton("Expert")
        self.rb_group.addButton(self.rb_expert)
        self.rb_group_box_layout.addWidget(self.rb_expert)

        big_layout.addWidget(self.rb_group_box)

        self.setLayout(big_layout)
        self.show()

class SysArgvData(object):
    make_next = False
    run_all = False
    template = None
    directory = None

class MainWidget(QMainWindow):
    def __init__(self, sys_arg_in = None):
        super(MainWidget, self).__init__()


        #tmp_off = '''
        try:
            with open ('bkp.pickle', 'rb') as bkp_in:
                self.idials_runner = pickle.load(bkp_in)

            #TODO sometimes the following error appears
            #Attribute not found
            #'module' object has no attribute 'CommandNode'

        except Exception as e:
            print "str(e) =", str(e)
            print "e.__doc__ =", e.__doc__
            print "e.message =", e.message
            #'''
            #if you reactivate the recovery thing, remeber to "tab" the next line
            self.idials_runner = Runner()

        #This flag makes the behaviour switch (automatic / explicit)
        if(sys_arg_in == None):
            sys_arg_in = SysArgvData()

        self.idials_runner.make_next = sys_arg_in.make_next

        self.cli_tree_output = TreeShow()
        self.cli_tree_output(self.idials_runner)

        self.cur_html = None
        self.cur_pick = None
        self.cur_json = None
        self.cur_cmd_name = "None"

        main_box = QVBoxLayout()

        h_left_splitter = QSplitter()
        h_left_splitter.setOrientation(Qt.Horizontal)


        self.tree_out = TreeNavWidget()
        h_left_splitter.addWidget(self.tree_out)


        self.centre_widget = CentreWidget()

        self.centre_widget.get_arg_obj(sys_arg_in)

        self.run_all = sys_arg_in.run_all

        h_left_splitter.addWidget(self.centre_widget)

        v_left_splitter = QSplitter()
        v_left_splitter.setOrientation(Qt.Vertical)
        v_left_splitter.addWidget(h_left_splitter)

        self.info_widget = InfoWidget()

        scrollArea = QScrollArea()
        scrollArea.setWidget(self.info_widget)

        v_left_splitter.addWidget(scrollArea)

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)
        h_main_splitter.addWidget(v_left_splitter)

        self.cli_out = CliOutView()
        self.web_view = WebTab()
        self.img_view = MyImgWin()

        self.output_info_tabs = QTabWidget()
        self.output_info_tabs.addTab(self.img_view, "Image View")
        self.output_info_tabs.addTab(self.cli_out, "CLI OutPut")
        self.output_info_tabs.addTab(self.web_view, "Report View")

        h_main_splitter.addWidget(self.output_info_tabs)

        main_box.addWidget(h_main_splitter)

        self.txt_bar = Text_w_Bar()
        main_box.addWidget(self.txt_bar)

        self.connect_all()

        self.custom_thread = MyThread()
        self.custom_thread.finished.connect(self.update_after_finished)
        self.custom_thread.str_fail_signal.connect(self.after_failed)
        self.custom_thread.str_print_signal.connect(self.cli_out.add_txt)
        self.custom_thread.str_print_signal.connect(self.txt_bar.setText)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

        self.user_stoped = False
        self.reconnect_when_ready()

    def connect_all(self):
        self.tree_clickable = True
        self.tree_out.clicked[QModelIndex].connect(self.node_clicked)

        self.centre_widget.repeat_btn.clicked.connect(self.rep_clicked)
        self.centre_widget.run_btn.clicked.connect(self.run_clicked)
        self.centre_widget.stop_btn.clicked.connect(self.stop_clicked)
        self.centre_widget.user_changed.connect(self.cmd_changed_by_user)
        self.centre_widget.update_command_lst.connect(
                          self.update_low_level_command_lst)
        self.centre_widget.step_param_widg.currentChanged.connect(
                                          self.cmd_changed_by_any)
        self.check_gray_outs()

    def disconnect_while_running(self):
        self.tree_clickable = False

        self.centre_widget.repeat_btn.setEnabled(False)
        self.centre_widget.run_btn.setEnabled(False)
        self.centre_widget.stop_btn.setEnabled(True)
        self.centre_widget.gray_outs_all()
        self.centre_widget.step_param_widg.currentWidget().my_widget.gray_me_out()

        self.user_stoped = False

    def reconnect_when_ready(self):
        self.tree_clickable = True

        self.centre_widget.repeat_btn.setEnabled(False)
        self.centre_widget.stop_btn.setEnabled(False)
        self.centre_widget.run_btn.setEnabled(False)

        if(self.user_stoped == True):
            self.idials_runner.current_node.success = None

        if(self.idials_runner.current_node.success == None):
            self.centre_widget.run_btn.setEnabled(True)
            self.centre_widget.step_param_widg.currentWidget().my_widget.activate_me()

        else:
            self.centre_widget.repeat_btn.setEnabled(True)
            self.centre_widget.step_param_widg.currentWidget().my_widget.gray_me_out()

        if(self.idials_runner.current_node.command_lst[0] == "reindex"):
            self.centre_widget.run_btn.setEnabled(False)
            self.centre_widget.repeat_btn.setEnabled(False)

        self.check_gray_outs()
        self.user_stoped = False
        self.update_nav_tree()

    def update_low_level_command_lst(self, command_lst):
        print "self.idials_runner.current_node.command_lst =", self.idials_runner.current_node.command_lst
        print "                                command_lst =", command_lst

        if(self.idials_runner.current_node.success == True and
                self.idials_runner.make_next == True):

            self.rep_clicked()

        self.idials_runner.current_node.command_lst = command_lst
        self.reconnect_when_ready()

    def cmd_changed_by_user(self, my_label):
        print "cmd_changed_by_user()"
        tmp_curr = self.idials_runner.current_node
        if(self.idials_runner.make_next == False and
                tmp_curr.success == True):

            self.cmd_exe(["mkchi"])
            self.idials_runner.current_node.command_lst = [str(my_label)]
            self.centre_widget.step_param_widg.currentWidget().my_widget.reset_par()
            self.cmd_exe(["clean"])

        elif(tmp_curr.success == None):
            self.idials_runner.current_node.command_lst = [str(my_label)]
            self.reconnect_when_ready()

    def cmd_changed_by_any(self):
        tmp_curr_widg = self.centre_widget.step_param_widg.currentWidget()
        self.cur_cmd_name = tmp_curr_widg.my_widget.command_lst[0]
        self.reconnect_when_ready()

    def rep_clicked(self):
        print "rep_clicked"
        self.cmd_exe(["mksib"])
        self.cmd_exe(["clean"])
        self.check_gray_outs()

    def stop_clicked(self):
        print "\n\n <<< Stop clicked >>> \n\n"
        #TODO fix spelling on << dials_comand >>
        pr_to_kill = self.idials_runner.current_node.dials_comand.my_pid
        print "self.idials_runner.current_node.dials_comand.my_pid =", pr_to_kill
        self.user_stoped = True
        kill_w_child(pr_to_kill)

    def run_clicked(self):
        print "run_clicked"
        print "...currentWidget(ref) =", self.centre_widget.step_param_widg.currentWidget()
        cmd_tmp = self.centre_widget.step_param_widg.currentWidget().my_widget.command_lst
        print "cmd_tmp =", cmd_tmp
        self.cmd_launch(cmd_tmp)

    def cmd_exe(self, new_cmd):
        #Running NOT in parallel
        self.idials_runner.run(command = new_cmd, ref_to_class = None)
        self.check_reindex_pop()
        self.reconnect_when_ready()

    def cmd_launch(self, new_cmd):
        #Running WITH theading

        self.txt_bar.start_motion()
        self.txt_bar.setText("Running")
        self.disconnect_while_running()

        self.custom_thread(new_cmd, self.idials_runner)

    def update_after_finished(self):
        update_info(self)

        self.txt_bar.setText("Idle") #TODO put here some clever message to the user
        self.txt_bar.end_motion()
        self.just_reindexed = False

        if(self.idials_runner.make_next == True):
            tmp_curr = self.idials_runner.current_node.prev_step
            nxt_cmd = get_next_step(tmp_curr)
            print "get_next_step(tmp_curr) =", nxt_cmd
            if(nxt_cmd != "reindex" and tmp_curr.success == True):
                self.centre_widget.set_widget(nxt_cmd = nxt_cmd)

            self.idials_runner.current_node.command_lst[0] = nxt_cmd

        else:
            tmp_curr = self.idials_runner.current_node

        if(tmp_curr.command_lst[0] == "refine_bravais_settings" and
                tmp_curr.success == True):

            if(self.idials_runner.make_next == False):
                self.idials_runner.run(command = ["mkchi"],
                                        ref_to_class = None)

            self.idials_runner.current_node.command_lst[0] = "reindex"

        elif(tmp_curr.command_lst[0] == "reindex" and
                tmp_curr.success == True):

            self.just_reindexed = True
            try:
                self.my_pop.close()

            except:
                print "no need to close reindex table"

        elif(tmp_curr.command_lst[0] == "integrate" and
                tmp_curr.success == True):

            if(self.idials_runner.make_next == False):
                self.idials_runner.run(command = ["mkchi"],
                                        ref_to_class = None)

            mtz_name = str(self.centre_widget.widg_lst[5].my_widget.
                           sipler_widget.mtz_name_lin.text())

            print "MTZ name =", mtz_name
            mtz_export_par = "mtz.hklout=" + mtz_name
            self.cmd_launch(["export", mtz_export_par])

        if(tmp_curr.command_lst[0] != "refine_bravais_settings" and
                tmp_curr.command_lst[0] != "integrate" and
                self.run_all == True):

            self.run_clicked()

        self.check_reindex_pop()
        self.check_gray_outs()
        self.reconnect_when_ready()

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(self.idials_runner, bkp_out)

    def check_gray_outs(self):
        tmp_curr = self.idials_runner.current_node
        if(tmp_curr.success != True):
            tmp_curr = tmp_curr.prev_step

        cmd_connects = {"Root"                    : ["import"] ,
                        "import"                  : ["find_spots"] ,
                        "find_spots"              : ["index"] ,
                        "index"                   : ["refine_bravais_settings", "refine", "integrate"] ,
                        "refine_bravais_settings" : [None] ,
                        "reindex"                 : ["refine", "integrate"] ,
                        "refine"                  : ["refine", "integrate"] ,
                        "integrate"               : [None] ,
                        "export"                  : [None] ,
                        "None"                    : [None] }

        #TODO Consider if it worth using this dictionary instead of the function get_next_item()

        lst_nxt = cmd_connects[str(tmp_curr.command_lst[0])]
        self.centre_widget.gray_outs_from_lst(lst_nxt)

    def check_reindex_pop(self):
        tmp_curr = self.idials_runner.current_node
        if(tmp_curr.command_lst[0] == "reindex" and
                self.just_reindexed == False):

            self.my_pop = MyReindexOpts()
            self.my_pop.set_ref(in_json_path = tmp_curr.prev_step.json_file_out)
            self.my_pop.my_inner_table.cellClicked.connect(self.opt_clicked)

        else:
            try:
                self.my_pop.close()

            except:
                print "no need to close reindex table"

        self.just_reindexed = False

    def update_nav_tree(self):
        self.tree_out.update_me(self.idials_runner.step_list[0],
                                self.idials_runner.current_line)

        tmp_cur_nod = self.idials_runner.current_node
        if(self.idials_runner.make_next == False and
                len(tmp_cur_nod.next_step_list) == 0 and
                tmp_cur_nod.success == True):

            nod_ref = tmp_cur_nod

        else:
            nod_ref = tmp_cur_nod.prev_step

        try:
            self.check_gray_outs(nod_ref)

        except:
            print "failed to << check_gray_outs() >>"

    def after_failed(self):
        #TODO handle error outputs
        self.update_nav_tree()
        self.txt_bar.setText("Idle") #TODO put here some clever message to the user
        self.txt_bar.end_motion()

    def opt_clicked(self, row, col):
        re_idx = row + 1
        print "Solution clicked =", re_idx
        cmd_tmp = "reindex solution=" + str(re_idx)
        self.cmd_launch(cmd_tmp)

    def node_clicked(self, it_index):
        if(self.tree_clickable == True):
            #TODO Think of a more robust way to "disconnect" ... next line
            try:
                self.centre_widget.update_command_lst.disconnect(
                                self.update_low_level_command_lst)
            except:
                print "<< update_low_level_command_lst >> already disconnected"

            print "TreeNavWidget(node_clicked)"
            item = self.tree_out.std_mod.itemFromIndex(it_index)
            lin_num = item.idials_node.lin_num
            print "clicked item lin_num (self.tree_out.std_mod) =", lin_num
            cmd_ovr = "goto " + str(lin_num)
            self.cmd_exe(cmd_ovr)
            self.centre_widget.set_widget(nxt_cmd = item.idials_node.command_lst[0],
                                        curr_step = self.idials_runner.current_node)

            self.check_reindex_pop()
            update_info(self)
            self.check_gray_outs()
            self.reconnect_when_ready()

            self.centre_widget.update_command_lst.connect(
                            self.update_low_level_command_lst)



#default_way = '''
if __name__ == '__main__':

    sys_arg = SysArgvData()
    call_arg = sys.argv

    if(len(call_arg) > 1):
        for par_str in call_arg[1:]:
            if(par_str == "e" or par_str == "-e" or
                    par_str == "explicit" or par_str == "--explicit"):

                sys_arg.make_next = False
                sys_arg.run_all = False
                print "Running in << explicit >> mode"

            elif(par_str == "a" or par_str == "-a" or
                 par_str == "automatic" or par_str == "--automatic"):

                sys_arg.make_next = True
                sys_arg.run_all = False
                print "Running in << automatic >> mode"

            elif(par_str == "sa" or par_str == "-sa" or
                 par_str == "superautomatic" or par_str == "--superautomatic"):

                sys_arg.make_next = True
                sys_arg.run_all = True
                print "Running in << SUPER automatic >> mode"

            elif(par_str[0:9] == "template="):
                sys_arg.template = par_str[9:]

            elif(par_str[0:10] == "directory="):
                sys_arg.directory = par_str[10:]


    print "sys_arg.template=", sys_arg.template
    print "sys_arg.directory=", sys_arg.directory
    app =  QApplication(call_arg)
    ex = MainWidget(sys_arg_in = sys_arg)
    ex.show()
    sys.exit(app.exec_())
#'''


debugg_way = '''
if __name__ == '__main__':

    from pycallgraph import PyCallGraph
    from pycallgraph.output import GraphvizOutput
    from pycallgraph import Config
    from pycallgraph import GlobbingFilter

    graphviz = GraphvizOutput(output_file='many_filters.png')

    conf = Config()
    conf.trace_filter = GlobbingFilter(exclude=[
        'pycallgraph.*',
        'libtbx.*',
        'dxtbx.*',
        'scitbx.*',
        'cctbx.*',
        'PyQt4.*',
        'dials.*'

    ])

    with PyCallGraph(output=graphviz, config=conf):
        app =  QApplication(sys.argv)
        ex = MainWidget()
        ex.show()
        sys.exit(app.exec_())
'''
