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

        self.pos_8 = 8


    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.drawLine(self.width() / self.pos_8, self.height() / 8, 7 * self.width() / self.pos_8, 7 * self.height()/8)
        painter.drawLine(self.width() / self.pos_8, 7*self.height() / 8, 7 * self.width() / self.pos_8, self.height()/8)
        painter.setPen(QPen(Qt.NoPen))

    def update_cross(self):
        if(self.pos_8 > 2):
            self.pos_8 = self.pos_8 - 1
        else:
            self.pos_8 = 8

class windowOverlay(QWidget):
    def __init__(self, parent=None):
        super(windowOverlay, self).__init__(parent)

        self.editor = QTextEdit()
        self.editor.setPlainText("OVERLAY"*100)

        self.button = QPushButton("Toggle Overlay")

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.addWidget(self.editor)
        self.verticalLayout.addWidget(self.button)

        self.painted_overlay = OverlayWidg(self.editor)
        self.painted_overlay.hide()

        self.button.clicked.connect(self.unpdate_w_click)

        self.my_timer = QTimer(self)
        self.my_timer.timeout.connect(self.on_timeout)
        self.my_timer.start(300)

    def on_timeout(self):
        print "on_timeout(self)"
        self.painted_overlay.update_cross()

    def unpdate_w_click(self):
        if self.painted_overlay.isVisible():
            self.painted_overlay.setVisible(False)
        else:
            self.painted_overlay.setVisible(True)

    def resizeEvent(self, event):
        self.painted_overlay.resize(event.size())
        event.accept()

if __name__ == "__main__":
    import  sys

    app = QApplication(sys.argv)
    main = windowOverlay()
    main.show()
    sys.exit(app.exec_())
