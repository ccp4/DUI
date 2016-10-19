'''
from PySide.QtCore import *
from PySide.QtGui import *
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OverlayWidg(QWidget):
    def __init__(self, parent=None):
        super(OverlayWidg, self).__init__(parent)

        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)

        self.setPalette(palette)

        self.pos_8 = 1
        self.my_timer = QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(500)


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))

        x1 = int( (float(self.pos_8) * float(self.width()) ) / 8.0)
        y1 = 0
        h = self.height()
        w = self.width() / 8.0
        x1 -= w

        painter.drawRect(x1, y1, w, h)
        painter.fillRect(x1, y1, w, h, QColor(100, 100, 255, 127))

        painter.setPen(QPen(Qt.NoPen))

    def update_cross(self):
        if(self.pos_8 < 8):
            self.pos_8 += 1
        else:
            self.pos_8 = 1


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
            self.painted_overlay.pos_8 = 1

    def resizeEvent(self, event):
        self.painted_overlay.resize(event.size())
        event.accept()

if __name__ == "__main__":
    import  sys

    app = QApplication(sys.argv)
    main = windowOverlay()
    main.show()
    sys.exit(app.exec_())
