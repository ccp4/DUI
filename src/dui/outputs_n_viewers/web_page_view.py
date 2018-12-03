from __future__ import print_function
import sys, os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

from img_view_tools import ProgBarBox


class WebTab(QWidget):
    def __init__(self):
        super(WebTab, self).__init__()

        print(" QWebSettings.JavascriptEnabled =", QWebSettings.JavascriptEnabled)
        QWebSettings.JavascriptEnabled = True

        self.dummy_html = """<html>
            <head>
            <title>A Sample Page</title>
            </head>
            <body>
            <h3>There is no report available for this step.</h3>
            </body>
            </html>"""

        self.web = QWebView()
        print("No need to load HTML file yet\n")
        self.web.loadFinished.connect(self.load_finished)

        hbox = QHBoxLayout()
        hbox.addWidget(self.web)
        self.setLayout(hbox)
        self.show()

    def update_page(self, new_path=None):
        try:
            print("\n >> update_page(", new_path, ")")
            new_path = os.path.abspath(new_path)

            # new_path = "file://" + new_path # unix way
            new_path = "file:///" + new_path  # Windows way(seems to work on Unix too)
            print(" >> new_path:", new_path, "\n")
            self.web.load(QUrl(new_path))

            print(" Loading ", new_path)

            txt_lab = "updating Report view:"
            self.my_bar = ProgBarBox(min_val=0, max_val=10, text=txt_lab)
            self.my_bar(5)

        except:
            print("\n failed to show <<", new_path, ">>  on web view ")
            self.web.setHtml(self.dummy_html)

    def load_finished(self, ok_bool):
        print("HTML Load(ok) =", ok_bool)
        if ok_bool == False:
            self.web.setHtml(self.dummy_html)

        print(" finished Loading HTML ")
        self.my_bar.ended()


class TmpTstWidget(QWidget):
    def __init__(self, parent=None):
        super(TmpTstWidget, self).__init__()
        # self.param_widget_parent = self
        self.my_widget = WebTab()
        self.btn1 = QPushButton("Click me", self)
        self.btn1.clicked.connect(self.load_page)
        my_box = QVBoxLayout()
        my_box.addWidget(self.my_widget)
        my_box.addWidget(self.btn1)
        self.setLayout(my_box)
        self.show()

    def load_page(self):
        self.my_widget.update_page(sys.argv[1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TmpTstWidget()
    sys.exit(app.exec_())
