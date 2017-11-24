
import sys
PyQt4_ver = '''
from PyQt4 import QtGui
from PyQt4 import QtCore
print "using PyQt4"
#'''
#PySide_ver = '''
from PySide import QtGui
from PySide import QtCore
print "using PySide"
#'''

def main():

    app     = QtGui.QApplication(sys.argv)
    palette = QtGui.QPalette()
    label   = QtGui.QLabel("TEST LABEL")

    #palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Foreground, QtGui.QColor(0, 0, 255, 127))
    label.setPalette(palette)

    #w.setCentralWidget(label);
    label.resize(100, 50)
    label.setWindowTitle('PyQt QLabel Text Color')
    label.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
