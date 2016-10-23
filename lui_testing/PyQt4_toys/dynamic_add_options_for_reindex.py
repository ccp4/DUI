from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import json

def ops_list_from_json(json_path = None):
    if( json_path == None ):
        #json_path = "../../../dui_test/X4_wide/dui_idials_test_01/dials-1/4_refine_bravais_settings/bravais_summary.json"
        json_path = "../../../dui_test/X4_wide_first_5_img/dui_idials_test_01/dials-1/7_refine_bravais_settings/bravais_summary.json"
        #json_path = "../../../dui_test/only_9_img/dui_idials_GUI_tst_17/dials-1/8_refine_bravais_settings/bravais_summary.json"

    with open(json_path) as json_file:
        json_data = json.load(json_file)

    lst_ops = []

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
        print "\n"

        labl = str(key).ljust(4) + angular_diff_str + rmsd_str + min_cc_str \
              + max_cc_str + nspots_str + bravais_str +unit_cell_str + cb_op_str

        print "\n\n"
        lst_ops.append(labl)

    return lst_ops



class Main( QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)

        self.addButton =  QPushButton('Add list of QPushButtons')
        self.addButton.clicked.connect(self.addWidget)

        self.delButton =  QPushButton('remove all QPushButton')
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

        self.my_font = QFont("Monospace")
        #self.my_font.setWeight(75)
        #self.my_font.setBold(True)
        my_label = QLabel()

        my_label.setFont(self.my_font)

        self.mainLayout.addWidget(my_label)
        self.mainLayout.addWidget(self.scrollArea)

        self.centralWidget =  QWidget()
        self.centralWidget.setLayout(self.mainLayout)

        self.setCentralWidget(self.centralWidget)
        self.lst_ops = []



        label_str = "Solution Metric fit  rmsd  min/max cc #spots lattice                                 unit_cell volume           cb_op"

        my_label.setText(label_str)


    def delWidget(self):
        print "delWidget"
        lng_lst = len(self.lst_ops)
        print "lng_lst =", lng_lst

        for btn_lst in self.lst_ops:
            self.scrollLayout.layout().removeWidget(btn_lst)
            btn_lst.setParent(None)
            del btn_lst

        '''
        self.scrollLayout.layout().removeWidget(self.lst_ops[lng_lst - 1])
        self.lst_ops[lng_lst - 1].setParent(None)
        self.lst_ops
        del self.lst_ops[-1]
        '''


    def addWidget(self):

        lst_labels = ops_list_from_json(json_path = "../../../dui_test/only_8_img_trimed_data/dui_idials_tst_02/dials-1/8_refine_bravais_settings/bravais_summary.json")

        for labl in lst_labels:
            new_op = QPushButton(labl)
            new_op.setFont(self.my_font)
            self.scrollLayout.addWidget(new_op)
            self.lst_ops.append(new_op)



if __name__ == "__main__":

    app =  QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    app.exec_()

