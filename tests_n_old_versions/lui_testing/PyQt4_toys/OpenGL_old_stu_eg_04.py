import sys
from PyQt4 import QtGui, QtCore, QtOpenGL
from ccp4mg import opengl, pygl_coord

class ReciprocalLatticeViewer(QtOpenGL.QGLWidget):
    def __init__(self,parent=None):
        QtOpenGL.QGLWidget.__init__(self,parent)
        self.viewsize = 30
        self.NEAR = 0.001
        self.FAR = 1000.0

    def initializeGL(self):
        opengl.glClearColor(1.0,1.0,0.0,1.0)
        self.origin = [0,0,0]
        self.scale = 1.0
        self.quat = pygl_coord.Quat(0.0,0.0,0.0,0)

    def paintGL(self):
        """
        This is the draw method.
        Everything is medieval immediate mode, fixed function OpenGL 1.0 calls.
        CCP4MG's opengl Python bindings do not have the new glVertexAttrib, etc. stuff.
        I would advise doing modern OpenGL in a C++ library and calling that stuff from
        here using appropriate Python bindings generator.
        """
        opengl.glLoadIdentity();
        opengl.glScalef(self.scale,self.scale,1.0)
        opengl.glTranslatef(self.origin[0],self.origin[1],self.origin[2]);
        print self.origin
        self.quat.Print(); print

        glrotmat = self.quat.getMatrix().to_dp()
        opengl.glMultMatrixd(glrotmat)
        opengl.delcdp(glrotmat)

        opengl.glClear(opengl.GL_COLOR_BUFFER_BIT | opengl.GL_DEPTH_BUFFER_BIT)
        opengl.glColor3f(0.0,0.0,0.0)

        opengl.glBegin(opengl.GL_TRIANGLES)
        opengl.glVertex3f(-10,-10,-20)
        opengl.glVertex3f(10,-10,-20)
        opengl.glVertex3f(0,10,-20)
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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.scale *= 1.1

        elif event.key() == QtCore.Qt.Key_Down:
            self.scale /= 1.1

        self.updateGL()

    def mousePressEvent(self, event):
        self.lastPos = QtCore.QPoint(event.pos())

    def setRotation(self,dx,dy,dz):
        print "Now I want to construct a rotation....", dx,dy,dz
        rotQ = pygl_coord.Quat(dx,dy,dz,0)
        self.quat.postMult(rotQ)

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()
        if (dx==0 and abs(dy)<2) or (abs(dy)<2 and dx==0):
            return

        if event.modifiers()&QtCore.Qt.ControlModifier==QtCore.Qt.ControlModifier:
            self.setRotation(dx,dy,0)

        else:
            self.origin[0] += dx/10.
            self.origin[1] -= dy/10.

        self.lastPos = event.pos()
        self.updateGL()

    def wheelEvent(self, event):
        #print dir(event), "\n\n"
        print "event.delta() = ", event.delta(), "\n\n"

        #print "event.pos() = ", event.pos(), "\n\n"



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win = ReciprocalLatticeViewer()
    win.show()
    win.raise_()
    sys.exit(app.exec_())
