'''
from PySide.QtCore import *
from PySide.QtGui import *
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OverlayWidg(QWidget):
    def __init__(self, parent = None):
        super(OverlayWidg, self).__init__(parent)

        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)

        self.setPalette(palette)

        self.pos_n = 1.0
        self.n_of_pos = 16.0
        self.my_timer = QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(500)


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 50)))

        x1 = int( (self.pos_n * float(self.width()) ) / self.n_of_pos)
        y1 = 0
        h = self.height()
        w = self.width() / self.n_of_pos
        x1 -= w

        rd = (self.n_of_pos - self.pos_n) / self.n_of_pos  * 255
        gr = 1
        bl = self.pos_n / self.n_of_pos * 255

        painter.drawRect(x1, y1, w, h)
        painter.fillRect(x1, y1, w, h, QColor(rd, gr, bl, 127))

        painter.setPen(QPen(Qt.NoPen))

    def update_cross(self):
        if(self.pos_n < self.n_of_pos):
            self.pos_n += 1.0
        else:
            self.pos_n = 1.0

    def on_timeout(self):
        self.update_cross()
        self.update()


class windowOverlay(QWidget):
    def __init__(self, parent=None):
        super(windowOverlay, self).__init__(parent)

        self.editor = QLineEdit()
        self.editor.setText("AAAAAAAAAAAAAAAAAA11111111111111111333333333333334")
        self.editor.setReadOnly(True)
        self.button = QPushButton("Toggle Overlay")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.editor)
        self.verticalLayout.addWidget(self.button)

        self.painted_overlay = OverlayWidg(self.editor)
        self.painted_overlay.hide()

        self.button.clicked.connect(self.unpdate_w_click)

    def unpdate_w_click(self):
        if self.painted_overlay.isVisible():
            self.painted_overlay.setVisible(False)
        else:
            self.painted_overlay.setVisible(True)
            self.painted_overlay.pos_n = 1

    def resizeEvent(self, event):
        self.painted_overlay.resize(event.size())
        event.accept()

if __name__ == "__main__":
    import  sys

    app = QApplication(sys.argv)
    main = windowOverlay()
    main.show()
    sys.exit(app.exec_())
