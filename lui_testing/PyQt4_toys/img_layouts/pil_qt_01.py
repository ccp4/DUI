from PIL import Image
from PIL import ImageOps
from PySide.QtGui import QImage, QImageReader, QLabel, QPixmap, QApplication

img = Image.open("centroid_diff_x.png")
data = img.convert('RGBA').tostring()

q_img = QImage(data, img.size[0], img.size[1], QImage.Format_ARGB32)

app = QApplication([])
pix = QPixmap.fromImage(q_img)
lbl = QLabel()
lbl.setPixmap(pix)
lbl.show()

app.exec_()