from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

import sys
class CliOutView(QTextBrowser):
    def __init__(self, parent = None, app = None):
        super(CliOutView, self).__init__()
        self.main_app = app
        self.setCurrentFont( QFont("Monospace"))

    def add_txt(self, str_to_print):
        self.append(str_to_print)
        self.main_app.processEvents()

class MainWidget(QMainWindow):
    def __init__(self):
        super(MainWidget, self).__init__()
        main_box = QVBoxLayout()
        main_box.addWidget(QLabel("Test dummy GUI"))

        self.tst_view = CliOutView(app = app)
        main_box.addWidget(self.tst_view)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_box)
        self.setCentralWidget(self.main_widget)

        for n in xrange(5):
            self.tst_view.add_txt("aaaaaaaaaaaaaaaaaaaa")


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())


