# coding: utf-8

"""Test running DUI, but in a screenshot-friendly way"""

import pytest

from dui.cli_utils import sys_arg
from dui.gui_utils import loading_error_dialog
from dui.m_idials_gui import DUIDataLoadingError, MainWidget


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


def test_error_dialog(screenshots, tmpdir):
    sys_arg.directory = str(tmpdir)
    # Ensure path is created so DUI tries to load
    (tmpdir / "dui_files").mkdir()
    (tmpdir / "dui_files" / "bkp.pickle").open("w").close()
    with pytest.raises(DUIDataLoadingError) as excinfo:
        MainWidget()
    # Load and show the error dialog for a screenshot
    dialog = loading_error_dialog(excinfo.value.original_traceback)
    dialog.show()
    screenshots.saveWindow(dialog)
