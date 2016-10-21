from PySide.QtGui import *
from PySide.QtCore import *
import sys

class Main( QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)

        self.addButton =  QPushButton('button to add 3 QPushButtons')
        self.addButton.clicked.connect(self.addWidget)

        self.delButton =  QPushButton('button to remove one QPushButton')
        self.delButton.clicked.connect(self.delWidget)

        self.scrollLayout = QVBoxLayout()
        #self.scrollLayout.setMargin(0)
        self.scrollLayout.setContentsMargins(QMargins(0,0,0,0))
        self.scrollLayout.setSpacing(0)

        self.scrollWidget =  QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        self.scrollArea =  QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.mainLayout =  QVBoxLayout()
        self.mainLayout.addWidget(self.addButton)
        self.mainLayout.addWidget(self.delButton)
        self.mainLayout.addWidget(self.scrollArea)

        self.centralWidget =  QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.centralWidget)
        self.lst_ops = []


    def delWidget(self):
        print "delWidget"
        lng_lst = len(self.lst_ops)
        print "lng_lst =", lng_lst

        self.scrollLayout.layout().removeWidget(self.lst_ops[lng_lst - 1])
        self.lst_ops[lng_lst - 1].setParent(None)
        self.lst_ops
        del self.lst_ops[-1]


    def addWidget(self):

        import json

        tmp_path = "../../../dui_test/only_9_img/dui_idials_GUI_tst_17/dials-1/8_refine_bravais_settings/bravais_summary.json"
        with open(tmp_path) as json_file:
            json_data = json.load(json_file)

        lst_labels = []

        longest_str_lenght = 0

        for key, value in json_data.iteritems():
            print "key =", key
            print "\n"
            print "value =", value
            print "\n"
            #labl = ""
            for inner_key in value:
                print "inner_key =", inner_key
                print "inner_value =", value[inner_key]
                print "\n"

                if( inner_key == "cc_nrefs" ):
                    cc_nrefs_str = str(value["cc_nrefs"]) + " "

                elif( inner_key == "rmsd" ):
                    rmsd_str = str(value["rmsd"]) + " "

                elif( inner_key == "cb_op" ):
                    cb_op_str = str(value["cb_op"]) + " "

                elif( inner_key ==  "min_cc" ):
                    min_cc_str = str(value["min_cc"]) + " "

                elif( inner_key == "bravais" ):
                    bravais_str = str(value["bravais"]) + " "

                elif( inner_key ==  "nspots" ):
                    nspots_str = str(value["nspots"]) + " "

                elif( inner_key == "max_cc" ):
                    max_cc_str = str(value["max_cc"]) + " "



            labl = cc_nrefs_str + rmsd_str + cb_op_str + min_cc_str + bravais_str + nspots_str + max_cc_str

            if( len(labl) > longest_str_lenght ):
                longest_str_lenght = len(labl)

            print "\n\n"
            lst_labels.append(labl)

        font = QFont("Monospace")
        font.setWeight(75)
        font.setBold(True)
        my_label = QLabel()
        my_label.setFont(font)

        label_str = "Solution Metric fit  rmsd  min/max cc #spots lattice                                 unit_cell volume           cb_op"

        my_label.setText(label_str)


        print "longest_str_lenght =", longest_str_lenght

        self.scrollLayout.addWidget(my_label)

        for labl in lst_labels:
            new_op = QPushButton(labl)
            new_op.setFont(font)
            self.scrollLayout.addWidget(new_op)
            self.lst_ops.append(new_op)



if __name__ == "__main__":

    app =  QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()

