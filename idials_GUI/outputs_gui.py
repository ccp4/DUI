
from python_qt_bind import GuiBinding
if GuiBinding.pyhon_binding == "PyQt4":
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtWebKit import *
    print "   <<<   using PyQt4"

else:
    #asuming GuiBinding.pyhon_binding == "PySide"
    from PySide.QtGui import *
    from PySide.QtCore import *
    from PySide.QtWebKit import *
    print "using PySide"


#from img_viewer.np_arr_paint import ImgTab
from img_viewer.image_viewer_w_opengl import MyImgWin

class WebTab(QWidget):

    def __init__(self):
        super(WebTab, self).__init__()

        print " QWebSettings.JavascriptEnabled =",  QWebSettings.JavascriptEnabled

        QWebSettings.JavascriptEnabled = True

        self.web =  QWebView()

        self.web.load(QUrl("file:///home/luiso/dui/dui_test/only_9_img/dui_idials_GUI_tst_09/dials-1/8_refine/report.html"))
        hbox = QHBoxLayout()
        hbox.addWidget(self.web)

        #self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.setWindowTitle('Shell dialog')
        self.show()



class outputs_widget1( QTabWidget):
    #item_changed = pyqtSignal()
    def __init__(self, phl_obj, parent = None):
        super(outputs_widget, self).__init__(parent)

        img_view =  ImgTab()
        web_view =  WebTab()

        self.addTab(img_view, "IMG View")
        self.addTab(web_view, "HTML Report")

        self.show()


class outputs_widget( QWidget):

    #item_changed = pyqtSignal()
    def __init__(self, phl_obj, parent = None):
        super(outputs_widget, self).__init__(parent)
        #self.super_parent = parent

        my_box = QVBoxLayout()
        v_splitter = QSplitter()

        v_splitter.setOrientation(Qt.Vertical)
        #img_view = ImgTab()
        img_view = MyImgWin()


        web_view = WebTab()

        v_splitter.addWidget(img_view)
        v_splitter.addWidget(web_view)
        my_box.addWidget(v_splitter)

        self.setLayout(my_box)
        self.show()



