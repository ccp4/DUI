from __future__ import absolute_import, division, print_function

import logging
import os
import sys

from .img_view_tools import ProgBarBox
from ..qt import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QUrl,
    QVBoxLayout,
    QWebSettings,
    QWebView,
    QWidget,
)

logger = logging.getLogger(__name__)


class WebTab(QWidget):
    def __init__(self):
        super(WebTab, self).__init__()

        logger.debug(
            " QWebSettings.JavascriptEnabled = %s", QWebSettings.JavascriptEnabled
        )
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
        logger.debug("No need to load HTML file yet\n")
        self.web.loadFinished.connect(self.load_finished)

        self.my_bar = None
        hbox = QHBoxLayout()
        hbox.addWidget(self.web)
        self.setLayout(hbox)
        # self.show()

    def update_page(self, new_path=None):
        try:
            logger.debug("\n >> update_page( %s )", new_path)
            new_path = os.path.abspath(new_path)

            # new_path = "file://" + new_path # unix way
            new_path = "file:///" + new_path  # Windows way(seems to work on Unix too)
            logger.debug(" >> new_path: %s", new_path)
            self.web.load(QUrl(new_path))

            logger.debug(" Loading  %s", new_path)

            txt_lab = "updating Report view:"
            self.my_bar = ProgBarBox(min_val=0, max_val=10, text=txt_lab)
            self.my_bar(5)

        except BaseException as e:
            # TODO(nick) - Don't know what this generic exception was supposed
            # to catch so catch all for now and work out what it was supposed to be
            logger.debug("\n failed to show << %s >>  on web view (%s)", new_path, e)
            self.web.setHtml(self.dummy_html)

    def load_finished(self, ok_bool):
        logger.debug("HTML Load(ok) = %s", ok_bool)
        if not ok_bool:
            self.web.setHtml(self.dummy_html)

        logger.debug(" finished Loading HTML ")
        if self.my_bar is not None:
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
        # self.show()

    def load_page(self):
        self.my_widget.update_page(sys.argv[1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TmpTstWidget()
    sys.exit(app.exec_())
