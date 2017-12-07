
from PyQt4 import QtGui, QtOpenGL
import sys

class GLpainter(QtOpenGL.QGLWidget):

    def __init__(self, parent=None):
        super(GLpainter, self).__init__(parent)

        self.setWindowTitle("Painter test")
        self.resize(400, 300)
        tmp_off = '''
        from ccp4mg import opengl
        print dir(opengl)
        '''

if(__name__ == '__main__'):
    app = QtGui.QApplication(sys.argv)
    clock = GLpainter()
    clock.show()
    sys.exit(app.exec_())
