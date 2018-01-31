import sys
from PyQt4 import QtGui, QtCore, QtOpenGL
from ccp4mg import opengl

class ReciprocalLatticeViewer(QtOpenGL.QGLWidget):
    def __init__(self,parent=None):
        QtOpenGL.QGLWidget.__init__(self,parent)
        self.viewsize = 30
        self.NEAR = 0.001
        self.FAR = 1000.0

    def initializeGL(self):
        opengl.glClearColor(0.5,0.5,0.5,1.0)
        self.origin = [0,0,0]

    def paintGL(self):
        """
        This is the draw method.
        Everything is medieval immediate mode, fixed function OpenGL 1.0 calls.
        CCP4MG's opengl Python bindings do not have the new glVertyexAttrib, etc. stuff.
        I would advise doing modern OpenGL in a C++ library and calling that stuff from
        here using appropriate Python bindings generator.
        """
        opengl.glLoadIdentity();
        opengl.glTranslatef(self.origin[0],self.origin[1],self.origin[2]);
        print self.origin
        opengl.glClear(opengl.GL_COLOR_BUFFER_BIT | opengl.GL_DEPTH_BUFFER_BIT)
        opengl.glColor3f(0.0,0.0,0.0)

        opengl.glBegin(opengl.GL_TRIANGLES)
        opengl.glVertex3f(-10,-10,-1)
        opengl.glVertex3f(10,-10,-1)
        opengl.glVertex3f(0,10,-1)
        opengl.glEnd()

    def resizeGL(self,w,h):
        if h == 0:
            h = 1
        if w == 0:
            w = 1
        ratio = 1.0*w / h

        opengl.glMatrixMode(opengl.GL_PROJECTION);
        opengl.glLoadIdentity();
        opengl.glViewport(0, 0, w, h);
        opengl.glOrtho(-self.viewsize*ratio,self.viewsize*ratio,-self.viewsize,self.viewsize,self.NEAR,self.FAR)
        print -self.viewsize*ratio,self.viewsize*ratio,-self.viewsize,self.viewsize,self.NEAR,self.FAR
        opengl.glMatrixMode(opengl.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = QtCore.QPoint(event.pos())

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()
        if (dx==0 and abs(dy)<2) or (abs(dy)<2 and dx==0): return
        print dx,dy
        self.origin[0] += dx/10.
        self.origin[1] -= dy/10.
        self.lastPos = event.pos()
        self.updateGL()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = ReciprocalLatticeViewer()
    win.show()
    win.raise_()
    sys.exit(app.exec_())
