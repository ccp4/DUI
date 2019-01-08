# coding: utf-8

import pytest

from dui.m_idials_gui import MainWidget
from dui.cli_utils import sys_arg


@pytest.fixture
def new_dui(qtbot, tmpdir):
    """Fixture to give a new, empty DUI MainWindow Widget."""
    sys_arg.directory = str(tmpdir)
    win = MainWidget()
    win.show()
    win.resize(1024, 768)
    return win


@pytest.mark.gui
def test_basic_window(new_dui, screenshots):
    screenshots.saveWidget(new_dui)
