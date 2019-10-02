"""
QT Cross-compatibility for DUI
"""

# Because we *-import as a shim in this file, ignore for flake8 purposes
# flake8: noqa

from __future__ import absolute_import, division, print_function

import logging
import os

logger = logging.getLogger(__name__)

try:
    # Try preferred interface first - PyQt5
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *

    from PyQt5 import QtWebEngineWidgets as QWebSettings
    from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5 import uic

    # Signal implementation changes slightly across implementations
    Signal = pyqtSignal

    QT5 = True
    # In case we're using pytest-qt, force the same API
    os.environ["PYTEST_QT_API"] = "pyqt5"

    print("Using PyQt5 for QT ...")

except ImportError:
    # Fallback to QT4
    try:
        # Explicitly choose the v2 APIs for QT4
        import sip

        try:
            sip.setapi("QDate", 2)
            sip.setapi("QDateTime", 2)
            sip.setapi("QString", 2)
            sip.setapi("QTextStream", 2)
            sip.setapi("QTime", 2)
            sip.setapi("QUrl", 2)
            sip.setapi("QVariant", 2)
        except ValueError:
            # These may have already been set
            pass

        # Primary interface: PyQt4
        from PyQt4.QtGui import *
        from PyQt4.QtCore import *
        from PyQt4.QtWebKit import *
        from PyQt4 import uic

        Signal = pyqtSignal

        QT5 = False
        # In case we're using pytest-qt, force the same API
        os.environ["PYTEST_QT_API"] = "pyqt4v2"

        print("Using PyQt4 for QT")

    except ImportError:
        # Tying both versions of PySide
        try:
            # Backup: try PySide
            from PySide.QtGui import *
            from PySide.QtCore import *
            from PySide.QtWebKit import *
            #from PySide import uic

            QT5 = False
            # In case we're using pytest-qt, force the same API
            os.environ["PYTEST_QT_API"] = "pyside"

            print("Using PySide for QT")
        except ImportError:
            # Backup: try PySide
            print("Try pyside2")
            from PySide2.QtGui import *
            from PySide2.QtCore import *
            from PySide2.QtWidgets import *
            from PySide2 import QtWebEngineWidgets as QWebSettings
            from PySide2.QtWebEngineWidgets import *
            #QWebSettings = PySide2.QtWebEngineWidgets
            #from PySide2.QtWebKit import *

            QT5 = True
            # In case we're using pytest-qt, force the same API
            os.environ["PYTEST_QT_API"] = "pyside2"

            print("Using PySide2 for QT")
