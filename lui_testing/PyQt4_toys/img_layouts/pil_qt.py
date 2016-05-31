from PIL import Image
from PySide.QtGui import QImage, QImageReader, QLabel, QPixmap, QApplication

im = Image.open("centroid_diff_x.png")

data = im.convert('RGBA').tostring()

app = QApplication([])

image = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
pix = QPixmap.fromImage(image)
lbl = QLabel()
lbl.setPixmap(pix)
lbl.show()

app.exec_()