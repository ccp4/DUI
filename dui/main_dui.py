#!/usr/bin/env python
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

from PyQt4 import QtCore, QtGui
#from PySide import QtCore, QtGui

from stacked_widgets import ImportPage, FindspotstParameterWidget,\
                            IndexParameterWidget, RefineParameterWidget,\
                            IntegrateParameterWidget, ExportParameterWidget

import subprocess
import sys

class ImgTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImgTab, self).__init__(parent)
        readable = QtGui.QCheckBox("CheckBox")
        localLayout = QtGui.QVBoxLayout()
        localLayout.addWidget(readable)
        self.setLayout(localLayout)

class MyQProcess(QtCore.QProcess):
    def __init__(self, parent):
        super(MyQProcess, self).__init__()
        self.super_parent = parent
        self.run_stat = False
        self.started.connect(self.local_start)
        self.readyReadStandardOutput.connect(self.readStdOutput)
        self.readyReadStandardError.connect(self.readStdError)
        self.finished.connect(self.local_finished)

    def local_start(self):
        self.super_parent.on_started()
        self.go_btn_txt = "  Running "
        self.run_stat = True

        self.my_timer = QtCore.QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(300)

    def on_timeout(self):
        self.go_btn_txt = self.go_btn_txt[1:] + self.go_btn_txt[:1]
        self.super_parent.update_go_txt(self.go_btn_txt)

    def readStdOutput(self):
        line_string = str(self.readAllStandardOutput())
        single_line = line_string[0:len(line_string) - 1]
        self.super_parent.append_line(single_line)

    def readStdError(self):
        line_string = str(self.readAllStandardError())
        self.super_parent.append_line(line_string, err_out = True)

    def local_finished(self):
        self.super_parent.on_finished()
        self.my_timer.stop()
        self.run_stat = False

class MyMainDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListView.IconMode)
        #self.contentsWidget.setIconSize(QtCore.QSize(96, 84))
        self.contentsWidget.setIconSize(QtCore.QSize(56, 44))
        self.contentsWidget.setMovement(QtGui.QListView.Static)

        self.contentsWidget.setMaximumWidth(88)
        #self.contentsWidget.setMinimumHeight(724)
        self.contentsWidget.setMinimumHeight(524)
        self.contentsWidget.setSpacing(12)

        self.pagesWidget = QtGui.QStackedWidget(self)
        self.widget_list = []
        self.widget_list.append(ImportPage(self))
        self.widget_list.append(FindspotstParameterWidget(self))
        self.widget_list.append(IndexParameterWidget(self))
        self.widget_list.append(RefineParameterWidget(self))
        self.widget_list.append(IntegrateParameterWidget(self))
        self.widget_list.append(ExportParameterWidget(self))

        self.pagesWidget.setMaximumWidth(650)

        for widg in self.widget_list:
            self.pagesWidget.addWidget(widg)

        self.default_go_label = " \n                      Go \n\n"
        self.go_underline = "\n_________________\n"

        self.Go_button = QtGui.QPushButton(self.default_go_label)
        pop_ref_view_but = QtGui.QPushButton(" \n    show reflection viewer")
        pop_but = QtGui.QPushButton(" \n    show image viewer")
        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        self.Go_button.clicked.connect(self.onGoBtn)
        pop_but.clicked.connect(self.onImgViewBtn)
        pop_ref_view_but.clicked.connect(self.onRefViewBtn)
        horizontalLayout = QtGui.QHBoxLayout()
        horizontalLayout.addWidget(self.contentsWidget)
        horizontalLayout.addWidget(self.pagesWidget, 1)

        exec_layout = QtGui.QHBoxLayout()

        self.gui_line_edit =  QtGui.QLineEdit(self)
        exec_layout.addWidget(self.gui_line_edit)

        exec_layout.addWidget(self.Go_button)

        mainLayout = QtGui.QVBoxLayout()

        self.multi_line_txt = QtGui.QTextBrowser()
        self.multi_line_txt.setMaximumHeight(724)
        self.multi_line_txt.setMinimumHeight(24)
        self.multi_line_txt.setCurrentFont(QtGui.QFont("Monospace"))
        self.multi_line_txt.setTextColor(QtGui.QColor("black"))

        pop_viewers_layout = QtGui.QHBoxLayout()
        pop_viewers_layout.addWidget(pop_ref_view_but)
        pop_viewers_layout.addWidget(pop_but)
        right_side_layout = QtGui.QVBoxLayout()

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(self.multi_line_txt, "Tab 1")
        tabWidget.addTab(ImgTab(), "tab 2")

        right_side_layout.addWidget(tabWidget)

        right_side_layout.addLayout(pop_viewers_layout)
        horizontalLayout.addLayout(right_side_layout)

        mainLayout.addLayout(horizontalLayout)
        mainLayout.addLayout(exec_layout)

        main_widget = QtGui.QWidget()
        main_widget.setLayout(mainLayout)
        self.resize(1200, 900)
        self.setCentralWidget(main_widget)


        self.qProcess  = MyQProcess(self)
        self.qProcess.setProcessChannelMode(QtCore.QProcess.SeparateChannels);

    def update_lin_txt(self, param_name = None, param_value = None):
        if(param_name != None):
            found_param = False
            for local_pname in self.param_changed_lst:
                if( local_pname[0] == param_name ):
                    local_pname[1] = param_value
                    found_param = True

            if(found_param == False):
                self.param_changed_lst.append([param_name,param_value])

            my_cli_string = self.cli_str

            for local_pname in self.param_changed_lst:
                my_cli_string += ( " " + str(local_pname[0]) +
                                   "=" + str(local_pname[1]) )

            self.gui_line_edit.setText(my_cli_string)

    def changePage(self, current, previous):
        if not current:
            current = previous
        self.pagesWidget.setCurrentIndex(self.contentsWidget.row(current))

        idx = self.pagesWidget.currentIndex()
        self.cli_str = self.widget_list[idx].cmd_lin_default

        try:
            self.gui_line_edit.setText(str(self.cli_str))
        except:
            pass
        self.param_changed_lst = []

    def createIcons(self):
        for widget in self.widget_list:
            page_n_button = QtGui.QListWidgetItem(self.contentsWidget)
            page_n_button.setIcon(QtGui.QIcon(widget.logo_path))
            page_n_button.setText(widget.button_label)
            page_n_button.setTextAlignment(QtCore.Qt.AlignHCenter)
            page_n_button.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.contentsWidget.currentItemChanged.connect(self.changePage)

    def onGoBtn(self, event):
        if( self.qProcess.run_stat == False ):
            self.shell_str_to_run = str(self.gui_line_edit.text())

            print "CLI to Run =", self.shell_str_to_run

            self.qProcess.start(self.shell_str_to_run)
            self.gui_line_edit.setText(str("Running >> {" + self.shell_str_to_run + " }" ))

    def on_started(self):
        tmp_txt = "\n" + " Starting " + self.go_underline
        self.Go_button.setText(tmp_txt)

        self.multi_line_txt.setTextColor(QtGui.QColor("green"))
        self.multi_line_txt.append(str("\nRunning >> { " + self.shell_str_to_run + " }" ))

    def update_go_txt(self, txt_str):
        tmp_txt = "\n" + txt_str + self.go_underline
        self.Go_button.setText(tmp_txt)

    def on_finished(self):
        self.Go_button.setText(self.default_go_label)
        self.gui_line_edit.setText(str(""))

    def append_line(self, line_out, err_out = False):
        if( not err_out ):
            self.multi_line_txt.setTextColor(QtGui.QColor("black"))
            self.multi_line_txt.append(line_out)

        else:
            print "Error detected"
            err_line = "ERROR: { \n" + line_out + " } "
            self.multi_line_txt.setTextColor(QtGui.QColor("red"))
            self.multi_line_txt.append(err_line)

    def onImgViewBtn(self):
        subprocess.call("dials.image_viewer datablock.json &", shell=True)

    def onRefViewBtn(self):
        subprocess.call("dials.reflection_viewer strong.pickle &", shell=True)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)


    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()

    print "width, height =", width, height


    dialog = MyMainDialog()
    dialog.show()
    sys.exit(app.exec_())

