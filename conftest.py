"""pytest configuration file"""

import os

import pytest

from dui.qt import QApplication, QPixmap, QStyleFactory


def pytest_addoption(parser):
    parser.addoption(
        "--nogui", action="store_true", default=False, help="Don't run GUI tests"
    )


def pytest_collection_modifyitems(config, items):
    """Don't run GUI tests unless --gui passed"""

    skip_gui = pytest.mark.skip(reason="--nogui specified - skipping gui tests")

    for item in items:
        if config.getoption("--nogui") and "gui" in item.keywords:
            item.add_marker(skip_gui)


def pytest_configure(config):
    config.addinivalue_line("markers", "gui: Mark as a GUI test")


@pytest.fixture(params=list(QStyleFactory.keys()))
def qtstyles(request, qtbot):
    "Runs tests with every different available style"
    QApplication.setStyle(request.param)
    return str(request.param)


@pytest.fixture
def qapp(qapp):
    qapp.setStyle("Fusion")
    return qapp


@pytest.fixture
def screenshots(qapp, qtbot, request):
    """Fixture to simplify making screenshots"""

    # Find the repo root
    project_root = os.path.dirname(__file__)
    # Make a screenshots folder if necessary
    ss_dir = os.path.join(project_root, "screenshots")
    if not os.path.isdir(ss_dir):
        os.mkdir(ss_dir)

    class SSSaver:
        """Returnable object to save test-context screenshots"""

        def __init__(self, root_path):
            self.count = 0
            self.root_path = root_path

        def _filename(self):
            "Generate a filename from the test name"
            test_file_name = os.path.splitext(
                os.path.basename(request.node.parent.name)
            )[0]
            return f"{test_file_name}__{request.node.name}_{self.count}.png"

        def saveWidget(self, widget, filename=None):
            """Save a widget screenshot."""
            filename = filename or self._filename()
            full_path = os.path.join(self.root_path, filename)
            QPixmap.grabWidget(widget).save(full_path)
            self.count += 1

        def saveWindow(self, window, filename=None):
            """Save a screenshot of a whole window, with decoration.

            Slower, and mildly more error-prone than saving the widget
            directly, as it relies on the windowing system.
            """
            filename = filename or self._filename()
            full_path = os.path.join(self.root_path, filename)

            window.activateWindow()
            window.raise_()
            qtbot.waitForWindowShown(window)

            screen = qapp.primaryScreen()
            geom = window.frameGeometry()
            winid = QApplication.desktop().winId()
            desktop = screen.grabWindow(
                winid, geom.x(), geom.y(), geom.width(), geom.height()
            )

            crop = desktop
            crop.save(full_path)

            self.count += 1

    return SSSaver(ss_dir)
