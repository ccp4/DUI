import sys
PyQt4_ver = '''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#Signal = pyqtSignal
print "using PyQt4"
#'''

#PySide_ver = '''
from PySide.QtGui import *
from PySide.QtCore import *
pyqtSignal = Signal
print "using PySide"
#'''

class inner_widg(QFileDialog):
    def __init__(self, parent):
        #dir_name = QtGui.QFileDialog.getExistingDirectory(self,"Open Directory")
        super(inner_widg, self).__init__()

        self.setViewMode(QFileDialog.AnyFile)

        #PySide.QtGui.QFileDialog.setViewMode(PySide.QtGui.QFileDialog.ViewMode)

        self.currentChanged.connect(self.on_currentChanged   )
        self.directoryEntered.connect(self.on_directoryEntered )
        self.fileSelected.connect(self.on_fileSelected     )
        self.filesSelected.connect(self.on_filesSelected    )
        self.filterSelected.connect(self.on_filterSelected   )
        self.show()

    def on_currentChanged(self):
        print "on_currentChanged(self)"

    def on_directoryEntered(self):
        print "on_directoryEntered(self)"

    def on_fileSelected(self):
        print "on_fileSelected(self)"

    def on_filesSelected(self):
        print "on_filesSelected(self)"
        print "Dir =", str(self.getExistingDirectory)

    def on_filterSelected(self):
        print "on_filterSelected(self)"



class MainWidget( QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()
        hbox =  QHBoxLayout()
        self.resize(500, 400)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()

        self.file_panel = inner_widg(self)
        #fl = self.file_panel.getExistingDirectory()
        #print "fl =", fl

if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
