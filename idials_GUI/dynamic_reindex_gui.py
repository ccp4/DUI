from python_qt_bind import *
import sys
import json

copied_from_SymmetryExpert_d_py = '''
lattice_to_spacegroup_number = {'aP':1, 'mP':3, 'mC':5, 'oP':16, 'oC':20,
                                'oF':22, 'oI':23, 'tP':75, 'tI':79,'hP':143,
                                'hR':146, 'cP':195, 'cF':196, 'cI':197}
'''


def ops_list_from_json(json_path = None):
    if( json_path == None ):
        #json_path = "../../../dui_test/only_9_img/dui_idials_GUI_tst_17/dials-1/8_refine_bravais_settings/bravais_summary.json"
        return None

    with open(json_path) as json_file:
        json_data = json.load(json_file)

    lst_ops = []
    for key, value in json_data.iteritems():
        recommended_str = "  "
        for inner_key in value:
            if( inner_key == "rmsd" ):
                rmsd_val = value["rmsd"]
                rmsd_str = " {:7.4}".format(rmsd_val)

            elif( inner_key ==  "min_cc" ):
                min_cc_val = value["min_cc"]
                min_cc_str = " {:7.3}".format(min_cc_val)

                if( "Non" in min_cc_str ):
                    min_cc_str = "    - "

                #print "__________________________________________ type(min_cc_val) =", type(min_cc_val)
                #TODO the format here is not always giving the same with

                #TODO think about someting like: "aa = list(round(i, ndigits=6) for i in aa)"

            elif( inner_key ==  "max_cc" ):
                max_cc_val = value["max_cc"]
                max_cc_str = " {:7.3}".format(max_cc_val)

                if( "Non" in max_cc_str ):
                    max_cc_str = "    - "

                #print "__________________________________________ type(max_cc_val) =", type(max_cc_val)
                #TODO the format here is not always giving the same with

                #TODO think about someting like: "aa = list(round(i, ndigits=6) for i in aa)"


            elif( inner_key == "bravais" ):
                bravais_val = value["bravais"]
                bravais_str = " " + str(bravais_val).ljust(3)

            elif( inner_key ==  "max_angular_difference" ):
                angular_diff_val = value["max_angular_difference"]
                angular_diff_str = " {:7.4} ".format(angular_diff_val)

            elif( inner_key ==  "correlation_coefficients" ):
                corr_coeff_val = value["correlation_coefficients"]
                corr_coeff_str =str(corr_coeff_val)

            elif( inner_key ==  "unit_cell" ):
                unit_cell_val = value["unit_cell"]
                uc_d = unit_cell_val[0:3]
                uc_a = unit_cell_val[3:6]
                unit_cell_str_a = "{:6.3}".format(uc_d[0])
                unit_cell_str_b = "{:6.3}".format(uc_d[1])
                unit_cell_str_c = "{:6.3}".format(uc_d[2])

                unit_cell_str_apl = "{:7.4}".format(uc_a[0])
                unit_cell_str_bet = "{:7.4}".format(uc_a[1])
                unit_cell_str_gam = "{:7.4}".format(uc_a[2])


            elif( inner_key ==  "recommended" ):
                recommended_val = value["recommended"]
                if( recommended_val == True ):
                    recommended_str = " Y"
                else:
                    recommended_str = " N"

        single_lin_lst = [int(key), angular_diff_str , rmsd_str , min_cc_str, max_cc_str ,
                       bravais_str , unit_cell_str_a , unit_cell_str_b , unit_cell_str_c ,
                       unit_cell_str_apl, unit_cell_str_bet, unit_cell_str_gam, recommended_str]

        lst_ops.append(single_lin_lst)

    sorted_lst_ops = sorted(lst_ops)

    return sorted_lst_ops


class MyReindexOpts(QWidget):
    def __init__(self, parent=None):
        super(MyReindexOpts, self).__init__(parent)
        self.super_parent = None
        self.setWindowTitle("Reindex")

    def set_ref(self, parent, in_json_path):
        if( self.super_parent == None ):
            self.super_parent = parent
            my_box = QVBoxLayout()
            self.my_inner_table = ReindexTable(self)
            self.my_inner_table.add_opts_lst(json_path = in_json_path)
            my_box.addWidget(self.my_inner_table)
            self.setLayout(my_box)

            #print dir(self.my_inner_table)
            n_col = self.my_inner_table.columnCount()
            tot_width = 80
            for col in xrange(n_col):
                loc_width = self.my_inner_table.columnWidth(col)
                #print "self.my_inner_table.columnWidth(col)", loc_width
                tot_width += loc_width

            n_row = self.my_inner_table.rowCount()
            row_height = self.my_inner_table.rowHeight(1)
            tot_heght = (n_row + 2) * row_height

            self.resize(tot_width, tot_heght)
            #print "self.my_inner_table.PdmWidth =", self.my_inner_table.PdmWidth

            #self.adjustSize()
            self.show()
        else:
            self.my_inner_table.del_opts_lst()
            self.my_inner_table.add_opts_lst(json_path = in_json_path)

        if( self.my_inner_table.rec_col != None ):

            self.super_parent.old_opnum = None

            my_solu = self.my_inner_table.find_best_solu()
            self.my_inner_table.opt_clicked(my_solu, 0)


class ReindexTable(QTableWidget):
    def __init__(self, parent=None):
        super(ReindexTable, self).__init__(parent)
        self.super_parent = parent.super_parent


        self.cellClicked.connect(self.opt_clicked)

        self.v_sliderBar = self.verticalScrollBar()
        self.h_sliderBar = self.horizontalScrollBar()


        sys_font = QFont()
        self.sys_font_point_size =  sys_font.pointSize()
        self.show()


    def opt_clicked(self, row, col):
        print "Solution clicked =", row + 1
        self.super_parent.opt_picked(row + 1)

        p_h_svar = self.horizontalScrollBar().value()
        p_v_svar = self.verticalScrollBar().value()

        print "p_h_svar =", p_h_svar
        print "p_v_svar =", p_v_svar

        v_sliderValue = self.v_sliderBar.value()
        h_sliderValue = self.h_sliderBar.value()

        self.del_opts_lst()
        self.add_opts_lst(lst_labels = self.list_labl, selected_pos = row)

        self.v_sliderBar.setValue(v_sliderValue)
        self.h_sliderBar.setValue(h_sliderValue)

    def find_best_solu(self):
        bst_sol = -1
        for row, row_cont in enumerate(self.list_labl):
            to_debug = '''
            print "\nrow =", row
            print "row_cont[4] =", row_cont[5]
            print "row_cont[", self.rec_col, "] =", row_cont[self.rec_col]
            '''
            if( row_cont[self.rec_col] == " Y"):
                if( row > bst_sol ):
                    bst_sol = row

        print "bst_sol = ", bst_sol



        return bst_sol

    def add_opts_lst(self, lst_labels = None, json_path = None, selected_pos = None):

        if( lst_labels == None ):
            print "json_path =", json_path
            self.list_labl = ops_list_from_json(json_path)

        n_row = len(self.list_labl)
        print "n_row =", n_row
        n_col = len(self.list_labl[0])
        print "n_col =", n_col

        self.setRowCount(n_row)
        self.setColumnCount(n_col - 1)

        alpha_str = " " + u"\u03B1" + " "
        beta_str = " " + u"\u03B2" + " "
        gamma_str = " " + u"\u03B3" + " "

        low_delta_str = u"\u03B4"
        delta_max_str = "max " + low_delta_str

        header_label_lst = [delta_max_str, "rmsd"," min cc", "max cc", "latt",
                            "  a ","  b ","  c ", alpha_str , beta_str , gamma_str, "Ok"]

        self.setHorizontalHeaderLabels(header_label_lst)

        self.rec_col = None

        for row, row_cont in enumerate(self.list_labl):
            for col, col_cont in enumerate(row_cont[1:]):
                item = QTableWidgetItem(col_cont)
                item.setFlags(Qt.ItemIsEnabled)
                if(col_cont == " Y"):
                    item.setBackground(Qt.green)
                    item.setTextColor(Qt.black)
                    self.rec_col = col + 1

                elif(col_cont == " N"):
                    item.setBackground(Qt.red)
                    item.setTextColor(Qt.black)

                else:
                    if(row == selected_pos):
                        item.setBackground(Qt.blue)
                        item.setTextColor(Qt.yellow)

                    else:
                        if(float(row) / 2.0 == int(float(row) / 2.0)):
                            item.setBackground(QColor(50,50,50,50))
                        else:
                            item.setBackground(Qt.white)

                        item.setTextColor(Qt.black)

                item.setFont(QFont("Monospace", self.sys_font_point_size))#, QFont.Bold))
                self.setItem(row, col, item)
                '''
                if( width_lst[col] < len(col_cont) ):
                    width_lst[col] = len(col_cont)
                '''

        self.resizeColumnsToContents()
        '''
        print "width_lst =", width_lst
        for col_n, col_len in enumerate(width_lst):
            #remember that with is given in pixels
            self.setColumnWidth(col_n, (col_len+1) * 10)
        '''


    def del_opts_lst(self):

        print "del_opts_lst"
        self.clear()
        self.setRowCount(1)
        self.setColumnCount(1)



class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.super_parent = self

        self.btn1 = QPushButton("Click me", self)

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("A1"))
        vbox.addWidget(self.btn1)
        vbox.addWidget(QLabel("B2"))

        self.btn1.clicked.connect(self.doit)
        self.my_pop = None

        self.main_widget = QWidget(self)
        self.main_widget.setLayout(vbox)
        self.setCentralWidget(self.main_widget)

    def doit(self):
        print "Opening a new popup window"
        #self.my_pop = MyPopup(tbl = [[1234,"abcd"],[5678,"efgh"]])
        self.my_pop = MyReindexOpts()
        self.my_pop.set_ref(parent = self, in_json_path = str(sys.argv[1]) )

    def opt_picked(self, opt_num):
        print "\n from dynamic_reindex_gui.py MainWindow"
        print "opt_num =", opt_num, "\n"


    def closeEvent(self, event):
        print "<< closeEvent ( from QMainWindow) >>"
        if( self.my_pop != None ):
            self.my_pop.close()


if __name__ == "__main__":
    app =  QApplication(sys.argv)
    myWidget = MainWindow()
    myWidget.show()
    app.exec_()

