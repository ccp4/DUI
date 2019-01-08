"""pytest configuration file"""

import os
import pytest

from dui.qt import QApplication, QPixmap, QStyleFactory


def pytest_addoption(parser):
    parser.addoption(
        "--gui", action="store_true", default=False, help="Run interactive GUI tests"
    )


def pytest_collection_modifyitems(config, items):
    """Don't run GUI tests unless --gui passed"""

    if not config.getoption("--gui") and len(items) > 1:
        skip_gui = pytest.mark.skip(reason="need --gui option to run")
        for item in items:
            if "gui" in item.keywords:
                item.add_marker(skip_gui)


@pytest.fixture(params=list(QStyleFactory.keys()))
def qtstyles(request, qtbot):
    "Runs tests with every different available style"
    QApplication.setStyle(request.param)
    return str(request.param)


@pytest.fixture
def screenshots(request):
    """Fixture to simplify making screenshots"""

    # Find the repo root
    project_root = os.path.dirname(__file__)
    # Make a screenshots folder if necessary
    ss_dir = os.path.join(project_root, "screenshots")
    if not os.path.isdir(ss_dir):
        os.mkdir(ss_dir)

    class SSSaver(object):
        """Returnable object to save test-context screenshots"""

        def __init__(self, root_path):
            self.count = 0
            self.root_path = root_path

        def saveWidget(self, widget, filename=None):
            """Save a widget screenshot."""
            if filename is None:
                test_file_name = os.path.splitext(
                    os.path.basename(request.node.parent.name)
                )[0]
                filename = "{}__{}_{}.png".format(
                    test_file_name, request.node.name, self.count
                )
            full_path = os.path.join(self.root_path, filename)
            QPixmap.grabWidget(widget).save(full_path)
            self.count += 1

    return SSSaver(ss_dir)
