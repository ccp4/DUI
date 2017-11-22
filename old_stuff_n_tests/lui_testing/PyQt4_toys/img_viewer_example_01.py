from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Scrolling(QScrollArea):
    def __init__(self, parent = None):
        super(Scrolling, self).__init__()
        self.my_parent = parent
        self.setBackgroundRole(QPalette.Dark)

    def __call__(self, image_label):
        self.setWidget(image_label)

    def wheelEvent(self, event):
        if( event.delta() > 0 ):
            self.my_parent.scaleImage(1.1)
        else:
            self.my_parent.scaleImage(0.9)

class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()

        self.scaleFactor = 0.0

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored,
                QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.scrollArea = Scrolling(self)
        self.scrollArea(self.imageLabel)

        self.setCentralWidget(self.scrollArea)

        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O",
                triggered=self.open)

        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addSeparator()

        self.menuBar().addMenu(self.fileMenu)

        self.setWindowTitle("Image Viewer")
        self.resize(500, 400)


    def open(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer",
                        "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.imageLabel.adjustSize()

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    imageViewer = ImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())
