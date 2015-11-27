#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
#web.load(QUrl("http://google.co.uk"))

web.load(QUrl("file:///home/lui/dui_code/xia2-report.html"))
web.show()

sys.exit(app.exec_())
