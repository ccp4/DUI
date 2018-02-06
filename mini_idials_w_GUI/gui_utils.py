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

from time import sleep
from cli_utils import get_next_step

import sys

def get_import_run_string(in_str_lst):

    print "in_str_lst =", in_str_lst

    selected_file_path = str(in_str_lst[0])
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
    if(ext_name == ".h5"):
        print "found h5 file"
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

    return dir_path, out_str


def build_label(com_nam):

    label_connects = {"import"                  :"\n  import ",
                      "find_spots"              :"\n   find  ",
                      "index"                   :"\n  index  ",
                      "refine_bravais_settings" :"\n reindex ",
                      "refine"                  :"\n  refine ",
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

    if(main_obj.cur_json != new_img_json):
        main_obj.cur_json = new_img_json
        main_obj.img_view.ini_datablock(main_obj.cur_json)
        print "\n\n called .ini_datablock() \n\n"

    if(main_obj.cur_pick != new_ref_pikl):
        main_obj.cur_pick = new_ref_pikl
        main_obj.img_view.ini_reflection_table(main_obj.cur_pick)

    main_obj.info_widget.update_data(exp_json_path = uni_json,
                                     refl_pikl_path = new_ref_pikl)


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



class TreeNavWidget(QTreeView):
    def __init__(self, parent = None):
        super(TreeNavWidget, self).__init__()
        print "TreeNavWidget(__init__)"
        self.setMinimumWidth(165)

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




class CliOutView(QTextEdit):
    def __init__(self, app = None):
        super(CliOutView, self).__init__()
        self.setCurrentFont(QFont("Monospace"))

    def add_txt(self, str_to_print):

        #TODO reconcider how elegant is this
        try:
            self.append(str_to_print)

        except:
            self.append(str_to_print[0])


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
            print "\n Failed to setStyle() \n"


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
    def __init__(self):
        super(MainWidget, self).__init__()
        main_box = QVBoxLayout()
        main_box.addWidget(QLabel("Test dummy GUI"))

        self.tst_view = CliOutView(app = app)
        main_box.addWidget(self.tst_view)
        self.txt_bar = Text_w_Bar()
        main_box.addWidget(self.txt_bar)

        btn1 = QPushButton(self)
        btn1.clicked.connect(self.btn_1_clicked)
        main_box.addWidget(btn1)

        btn2 = QPushButton(self)
        btn2.clicked.connect(self.btn_2_clicked)
        main_box.addWidget(btn2)

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

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())


