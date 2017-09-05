from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *



from outputs_n_viewers.web_page_view import WebTab
from outputs_n_viewers.img_viewer import MyImgWin

import sys, os
import pickle
from cli_utils import TreeShow, get_next_step
from m_idials import Runner
from gui_utils import CliOutView

from dynamic_reindex_gui import MyReindexOpts
import subprocess

from custom_widgets import  ParamWidget

widg_name_list = ["import", "find_spots", "index", "refine", "integrate"]

class MyThread(QThread):

    str_print_signal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyThread, self).__init__()

    def __call__(self, cmd_to_run, ref_to_controler, mk_nxt = True):
        self.cmd_to_run = cmd_to_run
        self.ref_to_controler = ref_to_controler
        self.make_next = mk_nxt
        self.start()

    def run(self):
        # {mk_nxt = False} changes the GUI to "explicit" mode
        self.ref_to_controler.run(command = self.cmd_to_run,
                                  ref_to_class = self, mk_nxt = self.make_next)

    def emit_print_signal(self, str_lin):
        #print str_lin, "... Yes"
        self.str_print_signal.emit(str_lin)


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
        if(type(root_node.next_step_list) is list):
            for child_node in root_node.next_step_list:
                if(child_node.command_lst != [None]):
                    child_node_name = str(child_node.command_lst[0])

                else:
                    child_node_name = "* " + get_next_step(child_node) + " *"

                try:
                    child_node_tip = str(child_node.command_lst[1:])

                except:
                    child_node_tip = "None"

                new_item = QStandardItem(child_node_name)
                new_item.setToolTip(child_node_tip)
                new_item.idials_node = child_node
                #new_item.success = child_node.success

                if(self.lst_idx == child_node.lin_num):
                    new_item.setBackground(Qt.blue)
                    if(child_node_name[0:2] == "* "):
                        new_item.setForeground(Qt.green)

                    else:
                        new_item.setForeground(Qt.white)

                else:
                    new_item.setBackground(Qt.white)
                    if(child_node_name[0:2] == "* "):
                        new_item.setForeground(Qt.green)

                    else:
                        new_item.setForeground(Qt.blue)

                new_item.setEditable(False)      # not letting the user edit it

                self.recursive_node(child_node, new_item)
                item_in.appendRow(new_item)


class CentreWidget(QWidget):
    def __init__(self, parent = None):
        super(CentreWidget, self).__init__()

        idials_gui_path = str(os.environ["IDIALS_GUI_PATH"])
        print "idials_gui_path =", idials_gui_path

        lst_icons_path = []
        lst_icons_path.append(idials_gui_path + "/resources/import.png")
        lst_icons_path.append(idials_gui_path + "/resources/find_spots.png")
        lst_icons_path.append(idials_gui_path + "/resources/index.png")
        lst_icons_path.append(idials_gui_path + "/resources/refine.png")
        lst_icons_path.append(idials_gui_path + "/resources/integrate.png")

        top_box =  QHBoxLayout()
        self.step_param_widg =  QStackedWidget()
        self.widg_lst = []
        for num, step_name in enumerate(widg_name_list):
            new_btn = QPushButton(self)
            new_btn.setToolTip(step_name)
            new_btn.setIcon(QIcon(lst_icons_path[num]))
            new_btn.setIconSize(QSize(38, 38))
            new_btn.clicked.connect(self.btn_clicked)
            top_box.addWidget(new_btn)

            param_widg = ParamWidget(step_name)
            new_btn.pr_widg = param_widg
            self.step_param_widg.addWidget(param_widg)
            self.widg_lst.append(param_widg)

            '''
            try:
                param_widg.my_widget.str_param_signal.connect(self.param_changed)

            except:
                print "Tmp off connection"
            '''

        big_v_box = QVBoxLayout()
        big_v_box.addLayout(top_box)

        dials_logo_path = str(idials_gui_path + "/resources/DIALS_Logo_smaller_centred.png")

        ctrl_box = QHBoxLayout()

        self.repeat_btn = QPushButton("\n Re Try \n", self)
        self.repeat_btn.setIcon(QIcon.fromTheme("edit-redo"))
        self.repeat_btn.setIconSize(QSize(28, 28))

        self.run_btn = QPushButton("\n  Run  \n", self)
        #self.run_btn.setIcon(QIcon(dials_logo_path))
        #self.run_btn.setIconSize(QSize(80, 48))
        self.run_btn.setIcon(QIcon.fromTheme("system-run"))
        self.run_btn.setIconSize(QSize(28, 28))

        self.stop_btn = QPushButton("\n  Stop  \n", self)
        self.stop_btn.setIcon(QIcon.fromTheme("process-stop"))
        self.stop_btn.setIconSize(QSize(28, 28))

        self.next_btn = QPushButton("\n  Next  \n", self)
        self.next_btn.setIcon(QIcon.fromTheme("go-next"))
        #self.next_btn.setIcon(QIcon.fromTheme("media-seek-forward"))
        self.next_btn.setIconSize(QSize(28, 28))

        ctrl_box.addWidget(self.repeat_btn)
        ctrl_box.addWidget(self.run_btn)
        ctrl_box.addWidget(self.stop_btn)
        ctrl_box.addWidget(self.next_btn)

        big_v_box.addLayout(ctrl_box)

        big_v_box.addWidget(self.step_param_widg)

        self.setLayout(big_v_box)
        self.show()

    def set_widget(self, nxt_cmd, curr_step = None):
        for widget in self.widg_lst:
            if(widget.my_label == nxt_cmd):
                self.step_param_widg.setCurrentWidget(widget)
                #try:

                widget.update_param(curr_step)

                #except:
                #    print "\n\n Unable to update params\n\n"

    def btn_clicked(self):
        print "btn_clicked"
        my_sender = self.sender()
        self.step_param_widg.setCurrentWidget(my_sender.pr_widg)

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()

        try:
            with open ('bkp.pickle', 'rb') as bkp_in:
                self.uni_controler = pickle.load(bkp_in)

            '''
            TODO sometimes the following error appears
            Attribute not found
            'module' object has no attribute 'UniStep'
            '''

        except Exception as e:
            print "str(e) =", str(e)
            print "e.__doc__ =", e.__doc__
            print "e.message =", e.message
            self.uni_controler = Runner()

        self.cli_tree_output = TreeShow()
        self.cli_tree_output(self.uni_controler)

        self.cur_html = None
        self.cur_pick = None
        self.cur_json = None

        main_box = QVBoxLayout()

        h_main_splitter = QSplitter()
        h_main_splitter.setOrientation(Qt.Horizontal)

        self.tree_out = TreeNavWidget()
        self.tree_out.clicked[QModelIndex].connect(self.item_clicked)
        self.tree_out.update_me(self.uni_controler.step_list[0], self.uni_controler.current)

        h_main_splitter.addWidget(self.tree_out)

        self.centre_widget = CentreWidget()
        self.centre_widget.run_btn.clicked.connect(self.run_clicked)
        self.centre_widget.next_btn.clicked.connect(self.next_clicked)

        h_main_splitter.addWidget(self.centre_widget)

        self.cli_out = CliOutView()
        self.web_view = WebTab()
        self.img_view = MyImgWin()

        self.my_tabs = QTabWidget()
        self.my_tabs.addTab(self.img_view, "Image View")
        self.my_tabs.addTab(self.cli_out, "CLI OutPut")
        self.my_tabs.addTab(self.web_view, "Report View")

        h_main_splitter.addWidget(self.my_tabs)

        main_box.addWidget(h_main_splitter)
        self.make_next = True
        self.custom_thread = MyThread()
        self.custom_thread.finished.connect(self.update_after_finished)
        self.custom_thread.str_print_signal.connect(self.cli_out.add_txt)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

    def run_clicked(self):
        print "run_clicked"
        print "...currentWidget(ref) =", self.centre_widget.step_param_widg.currentWidget()
        cmd_tmp = self.centre_widget.step_param_widg.currentWidget().my_widget.command_lst
        print "cmd_tmp =", cmd_tmp
        self.cmd_launch(cmd_tmp)
        #TODO think about how to prevent launches from happening when is busy

    def next_clicked(self):
        print "next_clicked"
        cmd_tmp = ["mkchi"]
        print "cmd_tmp =", cmd_tmp
        self.cmd_launch(cmd_tmp)

    def cmd_launch(self, new_cmd):
        self.custom_thread(new_cmd, self.uni_controler, mk_nxt = self.make_next)

    def update_after_finished(self):
        self.cli_tree_output(self.uni_controler)
        new_html = self.uni_controler.get_html_report()
        new_img_json = self.uni_controler.get_datablock_path()
        new_ref_pikl = self.uni_controler.get_reflections_path()

        print "\n new_html =", new_html , "\n"
        print " new_img_json =", new_img_json , "\n"
        print " new_ref_pikl =", new_ref_pikl , "\n"

        if(self.cur_html != new_html):
            self.cur_html = new_html
            try:
                self.web_view.update_page(new_html)

            except:
                print "No HTML here"

        if(self.cur_pick != new_ref_pikl):
            self.cur_pick = new_ref_pikl
            self.img_view.ini_reflection_table(self.cur_pick)

        if(self.cur_json != new_img_json):
            self.cur_json = new_img_json
            self.img_view.ini_datablock(self.cur_json)

        tmp_curr = self.uni_controler.step_list[self.uni_controler.current]
        nxt_cmd = get_next_step(tmp_curr)
        cur_success = tmp_curr.success

        if(tmp_curr.command_lst[0] != "reindex"):
            try:
                self.my_pop.close()

            except:
                print "no need to close reindex table"

        if(nxt_cmd == "refine_bravais_settings"):
           if(cur_success == None):
               self.cmd_launch("refine_bravais_settings")

           else:
               self.centre_widget.set_widget("refine", tmp_curr)

        elif(nxt_cmd == "reindex"):
            self.my_pop = MyReindexOpts()
            self.my_pop.set_ref(in_json_path = tmp_curr.prev_step.json_file_out)
            self.my_pop.my_inner_table.cellClicked.connect(self.opt_clicked)

        else:
            self.centre_widget.set_widget(nxt_cmd, tmp_curr)

        self.tree_out.update_me(self.uni_controler.step_list[0],
                                self.uni_controler.current)

        with open('bkp.pickle', 'wb') as bkp_out:
            pickle.dump(self.uni_controler, bkp_out)

    def opt_clicked(self, row, col):
        re_idx = row + 1
        print "Solution clicked =", re_idx
        cmd_tmp = "reindex solution=" + str(re_idx)
        self.cmd_launch(cmd_tmp)

    def item_clicked(self, it_index):
        print "TreeNavWidget(item_clicked)"
        item = self.tree_out.std_mod.itemFromIndex(it_index)
        lin_num = item.idials_node.lin_num
        print "clicked item lin_num (self.tree_out.std_mod) =", lin_num
        cmd_ovr = "goto " + str(lin_num)
        self.cmd_launch(cmd_ovr)

#default_way = '''
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
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
