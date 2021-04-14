"""
QT Cross-compatibility for DUI
"""

# Because we *-import as a shim in this file, ignore for flake8 purposes
# flake8: noqa


import logging
import os

logger = logging.getLogger(__name__)

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *
from PySide2.QtWidgets import *

# In case we're using pytest-qt, force the same API
os.environ["PYTEST_QT_API"] = "pyside2"

logger.info("Using PySide2 for QT")

try:
    from PySide2.QtUiTools import loadUiType
except ImportError:
    logger.info("no loadUiType in PySide; using backport")

    from io import StringIO
    from xml.etree import ElementTree

    from PySide2 import QtWidgets
    from pyside2uic import compileUi

    # Backport from https://stackoverflow.com/a/56658315/1118662
    # Included in PySide2 from 5.14.2
    def loadUiType(design):
        """
        PySide2 equivalent of PyQt5's `uic.loadUiType()` function.

        Compiles the given `.ui` design file in-memory and executes the
        resulting Python code. Returns form and base class.
        """
        parsed_xml = ElementTree.parse(design)
        widget_class = parsed_xml.find("widget").get("class")
        form_class = parsed_xml.find("class").text
        with open(design) as input:
            output = StringIO()
            compileUi(input, output, indent=0)
            source_code = output.getvalue()
            syntax_tree = compile(source_code, filename="<string>", mode="exec")
            scope = {}
            exec(syntax_tree, scope)
            form_class = scope[f"Ui_{form_class}"]
            base_class = eval(f"QtWidgets.{widget_class}")
        return (form_class, base_class)
