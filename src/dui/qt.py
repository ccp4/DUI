"""
QT Cross-compatibility for DUI
"""

# Because we *-import as a shim in this file, ignore for flake8 purposes
# flake8: noqa

from __future__ import absolute_import, division, print_function

import logging
import os

logger = logging.getLogger(__name__)

QT5 = True

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWidgets import *

# In case we're using pytest-qt, force the same API
os.environ["PYTEST_QT_API"] = "pyside2"

logger.info("Using PySide2 for QT")
