#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
#web.load(QUrl("http://google.co.uk"))

web.load(QUrl("file:///home/luiso/dui/dui_test/only_9_img/dui_idials_tst_01/dials-1/17_integrate/report.html"))

#web.load(QUrl("file:///home/luiso/dui/dui_test/test_nproc_eq_8/dials-report.html"))

web.show()

sys.exit(app.exec_())
