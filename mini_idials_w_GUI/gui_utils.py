'''
DUI's utilities

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

from cli_utils import get_next_step, sys_arg, get_phil_par
import sys, os, subprocess, psutil, time

def kill_w_child(pid_num):

    print "attempting to kill pid #:", pid_num
    try:
        parent_proc = psutil.Process(pid_num)
        for child in parent_proc.children(recursive=True):  # or parent_proc.children() for recursive=False
            child.kill()

        parent_proc.kill()

    except:
        print "\n\n failed to kill process(es)"


def get_main_path():
    return str(os.path.dirname(os.path.abspath(__file__)))


def get_import_run_string(in_str_lst):

    print "in_str_lst =", in_str_lst

    selected_file_path = str(in_str_lst[0])
    print "selected_file_path =", selected_file_path

    fnd_sep = False
    sep_chr = None
    for pos, single_char in enumerate(selected_file_path):
        if(single_char == "/" or single_char == "\\"):
            dir_pos_sep = pos

            if(fnd_sep == True and sep_chr != single_char):
                print "inconsistent dir separator"
                return None

            fnd_sep = True
            sep_chr = single_char

    if(fnd_sep == False):
        print "Failed to find dir path"
        return None

    dir_path = selected_file_path[:dir_pos_sep]

    #TODO test if the next << if >> is actually needed
    if(dir_path[0:3] == "(u\'"):
        print "dir_path[0:3] == \"(u\'\""
        dir_path = dir_path[3:]

    templ_r_side = selected_file_path[dir_pos_sep:]

    for pos, single_char in reversed(list(enumerate(templ_r_side))):
        if(single_char == "."):
            ext_pos_sep = pos

    left_sd_name = templ_r_side[:ext_pos_sep]
    ext_name = templ_r_side[ext_pos_sep:]
    if(ext_name == ".h5" or ext_name == ".nxs"):
        print "found h5 or nxs file"
        file_name = left_sd_name
        file_name = file_name + ext_name
        tail_size = 0

    else:
        file_name = left_sd_name

        max_tail_size = int(len(templ_r_side) / 3)
        for tail_size in xrange(max_tail_size):
            prev_str = file_name
            pos_to_replase = len(file_name) - tail_size - 1
            for num_char in '0123456789':
                if file_name[pos_to_replase] == num_char:
                    file_name = file_name[:pos_to_replase] + '#' + file_name[pos_to_replase + 1:]

            if(prev_str == file_name):
                break

        file_name = file_name + ext_name

    if(in_str_lst and len(in_str_lst) == 1):
        out_str = dir_path + file_name
        img_range = None

    else:
        str_lst = []
        for single_qstring in in_str_lst:
            str_lst.append(str(single_qstring))

        out_str = ""
        pos_last_num = 0

        for pos in xrange(len(str_lst[0])):
            all_equal = True
            single_char = str_lst[0][pos]
            for single_string in str_lst:
                try:
                    if(single_string[pos] != single_char):
                        all_equal = False
                except:
                    all_equal =False

            if(all_equal == True):
                out_str = out_str + single_char

            else:
                out_str = out_str + "#"
                pos_last_num = pos

        pos_last_num +=1

        print "pos_last_num =", pos_last_num

        if(pos_last_num > 1):
            lst_num_str = []
            try:

                for single_string in str_lst:
                    lst_num_str.append(int(single_string[pos_last_num-tail_size:
                                                         pos_last_num]))

                print "lst_num_str =", lst_num_str
                img_range = [min(lst_num_str), max(lst_num_str)]

            except:
                print "something went wrong with the range thing 01"
                img_range = None

        else:
            print "something went wrong with the range thing 02"
            img_range = None


    print "out_str( template mode ) =", out_str

    new_cmd = ""
    for single_char in out_str:

        if(single_char != "#"):
            new_cmd += single_char

        elif(prev_char != "#"):
            new_cmd += "*"

        prev_char = single_char

    out_str = new_cmd
    print "img_range =", img_range

    if(img_range != None):
        out_str += " image_range=" + str(img_range[0]) + "," + str(img_range[1])

    print "out_str( * mode ) =", out_str, "\n"
    print "dir_path =", dir_path

    return dir_path, out_str


def build_label(com_nam):

    label_connects = {"import"                  :"\nimport",
                      "find_spots"              :"\nfind",
                      "index"                   :"\nindex",
                      "refine_bravais_settings" :"\nlattice",
                      "refine"                  :"\nrefine",
                      "integrate"               :"\nintegrate"}

    return label_connects[com_nam]


def build_ttip(com_nam):

    tip_connects = {"import"                  :" dials.import ...",
                    "find_spots"              :" dials.find_spots ...",
                    "index"                   :" dials.index ...",
                    "refine_bravais_settings" :" dials.refine_bravais_settings\n" + \
                                               "         + \n" + \
                                               " dials.reindex ...",
                    "refine"                  :" dials.refine ...",
                    "integrate"               :" dials.integrate\n" + \
                                               "         + \n" + \
                                               " dials.export ..."}

    return tip_connects[com_nam]


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
    main_obj.cur_html = main_obj.idials_runner.get_html_report()

    if(main_obj.view_tab_num == 2):
        main_obj.web_view.update_page(main_obj.cur_html)

    new_log = main_obj.idials_runner.get_log_path()

    tmp_curr = main_obj.idials_runner.current_node

    main_obj.cli_out.clear()
    main_obj.cli_out.make_green()
    main_obj.cur_log = new_log
    main_obj.cli_out.refresh_txt(main_obj.cur_log, tmp_curr)

    new_img_json = main_obj.idials_runner.get_datablock_path()
    new_ref_pikl = main_obj.idials_runner.get_reflections_path()

    if(main_obj.view_tab_num == 0):

        if(main_obj.cur_json != new_img_json):
            main_obj.cur_json = new_img_json
            #TODO check if next line should run ALLWAYS
            main_obj.img_view.contrast_initiated = False
            main_obj.img_view.ini_datablock(main_obj.cur_json)

        if(main_obj.cur_pick != new_ref_pikl):
            main_obj.cur_pick = new_ref_pikl
            main_obj.img_view.ini_reflection_table(main_obj.cur_pick)

    if(tmp_curr.success == None):
        tmp_curr = tmp_curr.prev_step

    uni_json = tmp_curr.json_file_out

    main_obj.info_widget.update_data(exp_json_path = uni_json,
                                     refl_pikl_path = new_ref_pikl)

    main_obj.img_view.update_exp(main_obj.info_widget.all_data.ref2exp)

    main_obj.ext_view.update_data(new_pick = new_ref_pikl,
                                  new_json = uni_json)

    try:
        xb = main_obj.info_widget.all_data.xb / main_obj.info_widget.all_data.x_px_size
        yb = main_obj.info_widget.all_data.yb / main_obj.info_widget.all_data.y_px_size

    except:
        xb, yb = None, None

    main_obj.img_view.update_beam_centre(xb, yb)

def update_pbar_msg(main_obj):
    tmp_curr = main_obj.idials_runner.current_node
    txt = str(tmp_curr.command_lst[0])

    #TODO try to change the background when giving advice

    if(tmp_curr.success == False):
        txt = "click << Retry >> or navigate backwards in the tree"

    elif(  (txt == "integrate"
            or txt == "refine_bravais_settings")
            and tmp_curr.success == True):

        txt = "click << Retry >> or navigate elsewhere in the tree"

    elif(txt == "reindex" and tmp_curr.success == None):
        txt = "click the blue row to run reindex"

    elif(tmp_curr.success == None):
        if(tmp_curr.lin_num == 1):
            print "tmp_curr.lin_num == 1"
            templ_text = main_obj.centre_widget.step_param_widg.currentWidget().my_widget.simple_lin.text()
            print "templ_text =", templ_text
            if(templ_text == " ? "):
                txt = "click << Select File(s) >> or edit input line "

            else:
                txt = "click dials icon to run import"

        else:
            txt = "click dials icon to run " + txt

    else:
        nxt_cmd = get_next_step(tmp_curr)

        if(nxt_cmd == None):
            txt  ="Done"

        else:
            lab_nxt_cmd = get_lab_txt(nxt_cmd)
            txt = "click <<" + lab_nxt_cmd + ">> to go ahead, or click << Retry >>"

    main_obj.txt_bar.setText(txt)
    print "update_pbar_msg =", txt


def get_lab_txt(com_nam):

    cmd_to_labl = {"import"                  :" import ",
                   "find_spots"              :" find ",
                   "index"                   :" index ",
                   "refine_bravais_settings" :" reindex ",
                   "refine"                  :" refine ",
                   "integrate"               :" integrate"}

    new_com_nam = cmd_to_labl[com_nam]

    return new_com_nam


class MyQButton(QPushButton):
    def __init__(self, text = "", parent = None):
        super(MyQButton, self).__init__()
        self.setContentsMargins(-1,-1,-1,-1)

    def intro_text(self, my_text):
        btn_txt = build_label(my_text)

        v_box = QVBoxLayout()
        v_box.insertSpacing(1, 24)

        h_box_space = QHBoxLayout()
        h_box_space.insertSpacing(1, 65)
        v_box.addLayout(h_box_space)

        h_box_label = QHBoxLayout()
        h_box_label.addStretch()
        h_box_label.addWidget(QLabel(btn_txt))
        h_box_label.addStretch()

        v_box.addLayout(h_box_label)
        self.cmd_n1 = my_text
        self.setLayout(v_box)
        self.show()


class TreeNavWidget(QTreeView):
    def __init__(self, parent = None):
        super(TreeNavWidget, self).__init__()
        print "TreeNavWidget(__init__)"
        self.setSortingEnabled(False)
        self.setAnimated(True)

        header_view = self.header()
        header_view.setResizeMode(QHeaderView.ResizeToContents)
        header_view.setStretchLastSection(False)

    def update_me(self, root_node, lst_path_idx):
        self.lst_idx = lst_path_idx

        print self.lst_idx

        self.std_mod = QStandardItemModel(self)
        self.recursive_node(root_node, self.std_mod)

        self.std_mod.setHorizontalHeaderLabels([" History Tree "])
        self.setModel(self.std_mod)

        #self.update()
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


class ViewerThread (QThread):

    def __init__(self, parent = None):
        super(ViewerThread, self).__init__()

    def get_pid(self, pid_in):
        self.pid_to_see = pid_in

    def run(self):
        print "Hi from QThread(run)  ___________________<<< Before Loop >>>"
        my_proc = psutil.Process(self.pid_to_see)

        my_proc_stat = my_proc.status()
        print "my_proc_stat =", my_proc_stat

        while(my_proc_stat == 'running' or my_proc_stat == 'sleeping'):
            try:
                my_proc_stat = my_proc.status()
                time.sleep(0.1)

            except:
                print "proc disappeared"
                my_proc_stat = 'None'

        print "_________________________________________>>> Loop ended <<<"


class ExternalProcDialog(QDialog):

    read_phil_file = pyqtSignal(str)

    def __init__(self, parent = None):
        super(ExternalProcDialog, self).__init__()

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("\n          Running a pop-up viewer ...\
                               \n \
                               \n   remember to close the viewer before \
                               \n         performing any other task"))

        to_consider = '''
        my_bar = Text_w_Bar()
        vbox.addWidget(my_bar)
        my_bar.start_motion()
        '''

        self.use_shell = False

        kl_but = QPushButton("Close pop-up viewer")
        kl_but.clicked.connect(self.kill_my_proc)
        vbox.addWidget(kl_but)

        self.setLayout(vbox)
        self.setModal(True)

    def run_my_proc(self, pickle_path = "", json_path = "",
                    command_in = "dials.image_viewer"):

        first_pikl_path = pickle_path[0]

        if(self.use_shell == True):
            cmd_to_run = command_in + " " + str(json_path)
            if(first_pikl_path != None):
                cmd_to_run += " " + str(first_pikl_path)

        else:
            cmd_to_run = [command_in, str(json_path)]
            if(first_pikl_path != None):
                cmd_to_run.append(str(first_pikl_path))

        self.thrd = ViewerThread()


        cwd_path = sys_arg.directory + os.sep + "dui_files"
        self.phil_path = cwd_path + os.sep + "find_spots.phil"
        try:
            os.remove(self.phil_path)

        except:
            print "no ", self.phil_path, " found"

        print "\n running Popen>>>", cmd_to_run, ", ", self.use_shell, "<<< \n"
        self.my_process = subprocess.Popen(args = cmd_to_run, shell = self.use_shell,
                                           cwd = cwd_path)

        time.sleep(0.2)
        self.proc_pid = self.my_process.pid
        print "self.proc_pid =", self.proc_pid
        time.sleep(0.2)
        self.thrd.get_pid(self.proc_pid)

        self.thrd.finished.connect(self.child_closed)
        self.thrd.start()

        self.exec_()

    def kill_my_proc(self):
        print "self.kill_my_proc"
        self.read_phil_file.emit(self.phil_path)
        print "time to kill", self.proc_pid
        kill_w_child(self.proc_pid)
        self.done(0)


    def child_closed(self):
        print "after ...close()"
        self.kill_my_proc()

    def closeEvent(self, event):
        print "from << closeEvent  (QDialog) >>"
        self.kill_my_proc()


class OuterCaller(QWidget):

    pass_parmam_lst = pyqtSignal(list)

    def __init__(self):
        super(OuterCaller, self).__init__()

        v_box = QVBoxLayout()

        recip_lat_but = QPushButton("\n Open Reciprocal Lattice Viewer \n")
        recip_lat_but.clicked.connect(self.run_recip_dialg)
        v_box.addWidget(recip_lat_but)

        img_but = QPushButton("\n Open Image Viewer \n")
        img_but.clicked.connect(self.run_img_dialg)
        v_box.addWidget(img_but)

        self.diag = ExternalProcDialog()
        self.diag.read_phil_file.connect(self.check_phil_is)
        self.setLayout(v_box)
        self.show()

    def update_data(self, new_pick = None, new_json = None):
        self.my_pick = new_pick
        self.my_json = new_json

    def run_recip_dialg(self):
        self.diag.run_my_proc(pickle_path = self.my_pick, json_path = self.my_json,
                              command_in = "dials.reciprocal_lattice_viewer")

    def run_img_dialg(self):
        self.diag.run_my_proc(pickle_path = self.my_pick, json_path = self.my_json,
                              command_in = "dials.image_viewer")

    def check_phil_is(self, path_to_pass):
        if(os.path.isfile(path_to_pass)):
            print "\n time to read:", path_to_pass, "\n"
            lst_params = get_phil_par(path_to_pass)
            self.pass_parmam_lst.emit(lst_params)


class CliOutView(QTextEdit):
    def __init__(self, app = None):
        super(CliOutView, self).__init__()
        #self.setCurrentFont(QFont("Monospace"))
        self.setFont(QFont("Monospace", 10, QFont.Bold))
        self.make_green()

    def add_txt(self, str_to_print):
        try:
            ed_str = str(str_to_print).rstrip()
            self.append(ed_str)

        except:
            print "unwritable char <<", str_to_print, ">>",

    def make_red(self):
        print "turning log fonts to RED"
        style_orign = "color: rgba(220, 0, 0, 255)"
        self.setStyleSheet(style_orign)

    def make_green(self):
        print "turning log fonts to GREEN"
        style_orign = "color: rgba(0, 125, 0, 255)"
        self.setStyleSheet(style_orign)

    def make_blue(self):
        print "turning log fonts to BLUE"
        style_orign = "color: rgba(0, 0, 125, 255)"
        self.setStyleSheet(style_orign)

    def refresh_txt(self, path_to_log, curr_step = None):
        success = curr_step.success

        if(success == True):
            self.make_blue()

        elif(success == False):
            self.make_red()
            path_to_log = curr_step.err_file_out

        else:
            self.make_green()

        print " path_to_log =", path_to_log

        try:
            fil_obj = open(path_to_log, 'r')
            lst_lin = fil_obj.readlines()

        except:
            print "Failed to read log file"
            lst_lin = ["Ready to Run:"]
            self.make_green()

        self.clear()
        print "success =", success, "refresh_txt"

        for lin in lst_lin:
            self.add_txt(lin)


class Text_w_Bar(QProgressBar):
    def __init__(self, parent = None):
        super(Text_w_Bar,self).__init__()
        self.setAlignment(Qt.AlignCenter)
        self._text = ""
        print "test setStyle(QStyleFactory.create())"
        try:
            self.setStyle(QStyleFactory.create("cleanlooks"))
            #self.setStyle(QStyleFactory.create("Plastique"))
            #self.setStyle(QStyleFactory.create("cde"))
            #self.setStyle(QStyleFactory.create("motif"))

        except:
            print "Failed to setStyle()"

    def setText(self, text):
        if(len(text) > 2):
            self._text = text
            self.repaint()

    def text(self):
        return self._text

    def start_motion(self):
        print "starting motion"
        self.setRange(0, 0)

    def end_motion(self):
        self.setRange(0, 1)
        print "ending motion"


class MainWidget(QMainWindow):
    '''
    This is a test GUI only used by the developer
    the user should NEVER see this code running
    '''
    def __init__(self):
        super(MainWidget, self).__init__()
        main_box = QVBoxLayout()
        main_box.addWidget(QLabel("Test dummy GUI"))

        self.tst_view = CliOutView(app = app)
        main_box.addWidget(self.tst_view)
        self.txt_bar = Text_w_Bar()
        main_box.addWidget(self.txt_bar)

        btn1 = QPushButton("\n Do \n", self)
        btn1.clicked.connect(self.btn_1_clicked)
        main_box.addWidget(btn1)

        btn2 = QPushButton("\n Stop \n", self)
        btn2.clicked.connect(self.btn_2_clicked)
        main_box.addWidget(btn2)

        btn3 = QPushButton("\n refresh text \n", self)
        btn3.clicked.connect(self.btn_3_clicked)
        main_box.addWidget(btn3)

        self.n = 1

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)
        self.show()

    def btn_1_clicked(self):
        self.txt_bar.start_motion()
        self.n += 5
        my_text = str(self.n) + "aaaaa bbbbbb a ccccccccc a" + str(self.n * self.n)
        self.tst_view.add_txt(my_text)
        self.txt_bar.setText(my_text)

    def btn_2_clicked(self):
        my_text = " Done "
        self.tst_view.add_txt(my_text)
        self.txt_bar.setText(my_text)
        self.txt_bar.end_motion()

    def btn_3_clicked(self):
        #TODO update this path
        self.tst_view.refresh_txt("../../dui_test/X4_wide/reuse_area/dials_files/2_find_spots.log")


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())

