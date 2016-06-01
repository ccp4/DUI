import numpy as np
from PIL import Image
from PIL import ImageOps
from PySide.QtGui import QImage, QImageReader, QLabel, QPixmap, QApplication

#building array
arr_i = np.zeros(400 * 400 * 3).reshape(400, 400, 3)
arr_i[20:100, 40:200,0] = 255
arr_i[30:150, 50:250,1] = 255
arr_i[40:200, 60:300,2] = 255

#converting to QImage
img = Image.fromarray(np.uint8(arr_i))
data = img.convert('RGBA').tostring()
q_img = QImage(data, img.size[0], img.size[1], QImage.Format_ARGB32)

#building app with IMG
app = QApplication([])
pix = QPixmap.fromImage(q_img)
lbl = QLabel()
lbl.setPixmap(pix)
lbl.show()

app.exec_()


example_from_stackoverflow = '''
Image.fromarray(pix)
Open I as an array:
>>> I = numpy.asarray(PIL.Image.open('test.jpg'))
Do some stuff to I, then, convert it back to an image:
>>> im = PIL.Image.fromarray(numpy.uint8(I))
'''
