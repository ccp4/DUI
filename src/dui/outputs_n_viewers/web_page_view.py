import logging
import os
import sys

from dui.qt import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    Qt,
    QVBoxLayout,
    QWidget,
)

logger = logging.getLogger(__name__)


class WebTab(QWidget):
    def __init__(self):
        super().__init__()

        self.not_web = QLabel()
        self.not_web.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(
            lambda: QApplication.clipboard().setText(self.new_path)
        )
        self.new_path = ""

        logger.debug("No need to load HTML file yet\n")

        self.my_bar = None
        hbox = QHBoxLayout()
        hbox.addWidget(self.not_web)
        hbox.addWidget(self.copy_button)
        self.copy_button.setVisible(False)
        hbox.setAlignment(Qt.AlignTop)
        self.setLayout(hbox)

        self.update_page()

    def update_page(self, new_path=None):
        if not new_path:
            self.not_web.setText("<h3>There is no report available for this step.</h3>")
            self.copy_button.setVisible(False)
        else:
            logger.info("\n >> update_page( %s )", new_path)
            new_path = os.path.abspath(new_path)

            self.new_path = "file://" + new_path  # unix way
            logger.info(" >> new_path: %s", self.new_path)
            label_text = f"<p>Please copy this path to the nx browser address bar to see the report</p><h3>{self.new_path}</h3>"
            self.not_web.setText(label_text)
            self.copy_button.setVisible(True)
            logger.info(" Loading  %s", self.new_path)

    def load_finished(self, ok_bool):
        logger.info("HTML Load(ok) = %s", ok_bool)

        logger.info(" finished Loading HTML ")

        if self.my_bar is not None:
            self.my_bar.ended()


class TmpTstWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.param_widget_parent = self
        self.my_widget = WebTab()
        self.btn1 = QPushButton("Click me", self)
        self.btn1.clicked.connect(self.load_page)
        my_box = QVBoxLayout()
        my_box.addWidget(self.my_widget)
        my_box.addWidget(self.btn1)
        self.npos = 1
        self.setLayout(my_box)

    def load_page(self):
        self.my_widget.update_page(sys.argv[self.npos])
        self.npos += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TmpTstWidget()
    ex.show()
    sys.exit(app.exec_())
