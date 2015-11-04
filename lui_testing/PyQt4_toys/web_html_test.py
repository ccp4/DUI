#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://google.co.uk"))

#web.load(QUrl("file:///home/dev/a_tour_of_dartlang/A_Tour_of_the_Dart_Language__Dart_Up_and_Running__Dart.html"))
web.show()

sys.exit(app.exec_())
