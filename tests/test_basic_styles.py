# coding: utf-8

import pytest

from dui.m_idials_gui import MainWidget
from dui.cli_utils import sys_arg


@pytest.mark.gui
def test_basic_window(qtbot, screenshots, tmpdir):
    sys_arg.directory = str(tmpdir)
    win = MainWidget()
    win.show()
    win.resize(1024, 768)
    screenshots.saveWidget(win)
