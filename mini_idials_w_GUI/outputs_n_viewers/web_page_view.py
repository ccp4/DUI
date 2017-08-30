import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
class WebTab(QWidget):

    def __init__(self):
        super(WebTab, self).__init__()

        print " QWebSettings.JavascriptEnabled =",  QWebSettings.JavascriptEnabled
        QWebSettings.JavascriptEnabled = True

        self.web =  QWebView()
        print "No need to load HTML file yet\n"

        hbox = QHBoxLayout()
        hbox.addWidget(self.web)

        #self.setGeometry(1100, 200, 550, 250)
        self.setLayout(hbox)
        self.show()

    def update_page(self, new_path):
        print " >> update_page(", new_path, ")"
        new_path = "file://" + new_path
        print " >> new_path:", new_path
        self.web.load(QUrl(new_path))


class TmpTstWidget( QWidget):

    def __init__(self, parent = None):
        super(TmpTstWidget, self).__init__()
        #self.param_widget_parent = self
        self.my_widget = WebTab()
        self.btn1 = QPushButton("Click me", self)
        self.btn1.clicked.connect(self.load_page)
        my_box = QVBoxLayout()
        my_box.addWidget(self.my_widget)
        my_box.addWidget(self.btn1)
        self.setLayout(my_box)
        self.show()

    def load_page(self):
        #self.my_widget.update_page("/home/luiso/dui/dui_test/only_9_img/dui_idials_tst_03/dials-1/9_integrate/report.html")
        #self.my_widget.update_page("/scratch/dui/dui_test/only_20_img_X4_wide/dui_tst_02/dials-2/6_refine/report.html")
        self.my_widget.update_page("/home/luiso/dui/dui_test/X4_wide/dui_idials_tst_05/dials-1/5_reindex/report.html")

if(__name__ == "__main__"):
    app =  QApplication(sys.argv)
    ex = TmpTstWidget()
    sys.exit(app.exec_())
