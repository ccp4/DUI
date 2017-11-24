import numpy as np
from PIL import Image

#from PySide.QtGui import QImage, QLabel, QPixmap, QApplication
from PyQt4.QtGui import QImage, QLabel, QPixmap, QApplication

# img sizes
height = 300
width = 400

#building array
arr_i = np.zeros([height, width, 3], dtype=np.uint8)
arr_i[20:100, 40:200,0] = 255
arr_i[50:150, 70:250,1] = 255
arr_i[70:200, 100:300,2] = 255

tmp_off = '''
img_arr_dir = arr_i[:,:,:]
img_arr_dir[:,:,2] = arr_i[:,:,0]
img_arr_dir[:,:,1] = arr_i[:,:,1]
img_arr_dir[:,:,0] = arr_i[:,:,2]
img = Image.fromarray(np.uint8(img_arr_dir))
'''

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


