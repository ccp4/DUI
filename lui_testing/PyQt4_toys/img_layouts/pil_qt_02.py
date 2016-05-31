import numpy as np
from PIL import Image
from PIL import ImageOps
from PySide.QtGui import QImage, QImageReader, QLabel, QPixmap, QApplication

arr_i = np.arange(400 * 400 * 3).reshape(400, 400, 3)

img = Image.fromarray(np.uint8(arr_i))

data = img.convert('RGBA').tostring()

q_img = QImage(data, img.size[0], img.size[1], QImage.Format_ARGB32)

app = QApplication([])
pix = QPixmap.fromImage(q_img)
lbl = QLabel()
lbl.setPixmap(pix)
lbl.show()

app.exec_()


'''
Image.fromarray(pix)
Open I as an array:

>>> I = numpy.asarray(PIL.Image.open('test.jpg'))
Do some stuff to I, then, convert it back to an image:

>>> im = PIL.Image.fromarray(numpy.uint8(I))


'''