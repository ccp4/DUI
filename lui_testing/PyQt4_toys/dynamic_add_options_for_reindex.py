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
        tmp_path = "../../../dui_test/X4_wide/dui_idials_test_01/dials-1/4_refine_bravais_settings/bravais_summary.json"
        #tmp_path = "../../../dui_test/X4_wide_first_5_img/dui_idials_test_01/dials-1/7_refine_bravais_settings/bravais_summary.json"
        #tmp_path = "../../../dui_test/only_9_img/dui_idials_GUI_tst_17/dials-1/8_refine_bravais_settings/bravais_summary.json"
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

                if( inner_key == "rmsd" ):
                    rmsd_val = value["rmsd"]
                    rmsd_str = " {:7.3}".format(rmsd_val)
                    print "__________________________________________ type(rmsd_val) =", type(rmsd_val)

                elif( inner_key == "cb_op" ):
                    cb_op_val = value["cb_op"]
                    cb_op_str = str(cb_op_val).rjust(18)
                    print "__________________________________________ type(cb_op_val) =", type(cb_op_val)

                elif( inner_key ==  "min_cc" ):
                    min_cc_val = value["min_cc"]
                    min_cc_str = " {:7.3}".format(min_cc_val)

                    print "__________________________________________ type(min_cc_val) =", type(min_cc_val)

                elif( inner_key ==  "max_cc" ):
                    max_cc_val = value["max_cc"]
                    max_cc_str = " {:7.3}".format(max_cc_val)
                    print "__________________________________________ type(max_cc_val) =", type(max_cc_val)


                elif( inner_key == "bravais" ):
                    bravais_val = value["bravais"]

                    bravais_str = " " + str(bravais_val).ljust(3)
                    #bravais_str = str(bravais_val)
                    print "__________________________________________ type(bravais_val) =", type(bravais_val)

                elif( inner_key ==  "nspots" ):
                    nspots_val = value["nspots"]
                    nspots_str =" {:9} ".format(nspots_val)
                    print "__________________________________________ type(nspots_val) =", type(nspots_val)

                elif( inner_key ==  "max_angular_difference" ):

                    angular_diff_val = value["max_angular_difference"]
                    angular_diff_str = " {:7.4} ".format(angular_diff_val)
                    print "__________________________________________ type(angular_diff_val) =", type(angular_diff_val)

                elif( inner_key ==  "correlation_coefficients" ):
                    corr_coeff_val = value["correlation_coefficients"]
                    corr_coeff_str =str(corr_coeff_val)
                    print "__________________________________________ type(corr_coeff_val) =", type(corr_coeff_val)


                elif( inner_key ==  "unit_cell" ):
                    unit_cell_val = value["unit_cell"]
                    uc_d = unit_cell_val[0:3]
                    uc_a = unit_cell_val[3:6]

                    print "uc_d =", uc_d
                    print "uc_a =", uc_a


                    unit_cell_str = "({:6.3}".format(uc_d[0]) \
                                  + " {:6.3}".format(uc_d[1]) \
                                  + " {:6.3})".format(uc_d[2]) \
                                  + ", " \
                                  + "({:7.4}".format(uc_a[0]) \
                                  +  "{:7.4}".format(uc_a[1]) \
                                  +  "{:7.4})".format(uc_a[2]) \

                    #unit_cell_str = str(unit_cell_val)

                    print "__________________________________________ type(unit_cell_val) =", type(unit_cell_val)


                elif( inner_key ==  "recommended" ):
                    recommended_val = value["recommended"]
                    recommended_str = str(recommended_val)
                    print "__________________________________________ type(recommended_val) =", type(recommended_val)

                    #'''
                elif( inner_key == "cc_nrefs" ):
                    cc_nrefs_val = value["cc_nrefs"]
                    cc_nrefs_str = str(cc_nrefs_val)
                    print "__________________________________________ type(cc_nrefs_val) =", type(cc_nrefs_val)
                    #'''
                print "\n"

            print "\n\n"

            "Solution Metric fit  rmsd  min/max cc #spots lattice                                 unit_cell volume           cb_op"

            #labl = rmsd_str + cb_op_str + min_cc_str + bravais_str + nspots_str + max_cc_str + min_cc_str# + cc_nrefs_str
            labl = str(key).ljust(4) + angular_diff_str + rmsd_str + min_cc_str \
                  + max_cc_str + nspots_str + bravais_str +unit_cell_str + cb_op_str

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

