#!/usr/bin/env python

# FIXME Copied from dials.index.py. This is needed here because scipy needs to
# be imported before cctbx otherwise there will be a segmentation fault. This
# should be fixed in dials.index so that we don't need to import here.
try:
  # try importing scipy.linalg before any cctbx modules, otherwise we
  # sometimes get a segmentation fault/core dump if it is imported after
  # scipy.linalg is a dependency of sklearn.cluster.DBSCAN
  import scipy.linalg # import dependency
except ImportError, e:
  pass


class gen_code(object):
    def __init__(self):

        self.src_code_1 = []
        self.src_code_1.append("import sys")
        #self.src_code_1.append(" ")
        self.src_code_1.append("PyQt4_ver = '''")
        self.src_code_1.append("from PyQt4.QtGui import *")
        self.src_code_1.append("from PyQt4.QtCore import *")
        self.src_code_1.append("#Signal = pyqtSignal")
        self.src_code_1.append("print \"using PyQt4\"")
        self.src_code_1.append("#'''")
        #self.src_code_1.append(" ")
        self.src_code_1.append("#PySide_ver = '''")
        self.src_code_1.append("from PySide.QtGui import *")
        self.src_code_1.append("from PySide.QtCore import *")
        #self.src_code_1.append("pyqtSignal = Signal")
        self.src_code_1.append("print \"using PySide\"")
        self.src_code_1.append("#'''")
        #self.src_code_1.append(" ")
        self.src_code_1.append("class inner_widg( QWidget):")
        #self.src_code_1.append("    goClicked = pyqtSignal()")
        self.src_code_1.append("    def __init__(self, parent):")
        self.src_code_1.append("        super(inner_widg, self).__init__()")
        #self.src_code_1.append(" ")
        self.src_code_1.append("        bg_box =  QVBoxLayout(self)")
        self.src_code_1.append(" ")

        self.src_code_2 = []
        self.src_code_2.append(" ")
        self.src_code_2.append("        self.setLayout(bg_box)")
        self.src_code_2.append("        self.show()")
        self.src_code_2.append("class MainWidget( QWidget):")
        #self.src_code_2.append(" ")
        self.src_code_2.append("    def __init__(self):")
        self.src_code_2.append("        super(MainWidget, self).__init__()")
        self.src_code_2.append("        self.scrollable_widget = inner_widg(self)")
        self.src_code_2.append("        scrollArea = QScrollArea()")
        self.src_code_2.append("        scrollArea.setWidget(self.scrollable_widget)")
        self.src_code_2.append("        hbox =  QHBoxLayout()")
        self.src_code_2.append("        hbox.addWidget(scrollArea)")
        self.src_code_2.append("        self.setLayout(hbox)")
        self.src_code_2.append("        self.setWindowTitle('Phil dialog')")
        self.src_code_2.append("        self.show()")
        #self.src_code_2.append(" ")
        self.src_code_2.append("    def to_be_caled_from_son_widg(self):")
        self.src_code_2.append("        print \"from parent parent_widget\"")
        #self.src_code_2.append(" ")
        self.src_code_2.append("if __name__ == '__main__':")
        self.src_code_2.append("    app =  QApplication(sys.argv)")
        self.src_code_2.append("    ex = MainWidget()")
        self.src_code_2.append("    sys.exit(app.exec_())")
        #self.src_code_2.append(" ")

    def write_file(self, to_insert = None):

        myfile = open("gui_tst_code.py", "w")

        for line in self.src_code_1:
            myfile.write(line)
            myfile.write("\n")

        if( to_insert != None ):
            print "inserting auto-generated code"
            for line in to_insert:
                myfile.write(line)
                myfile.write("\n")

        for line in self.src_code_2:
            myfile.write(line)
            myfile.write("\n")

        myfile.close()

def deep_in_rec(phl_obj, lst_obj):

    for single_obj in phl_obj:

        if( single_obj.is_definition):
            print "         single_obj.name =", single_obj.name
            local_val = single_obj.extract()
            #print "single_obj.type =", single_obj.type.phil_type
            #print "single_obj.extract =", local_val
            elm = [single_obj.name, single_obj.type.phil_type]
            lst_obj.append(elm)

        elif( single_obj.is_scope ):
            #print "is_scope \n" # deep_in_rec here
            lst_obj.append(str(single_obj.name))
            deep_in_rec(single_obj.objects, lst_obj)
            print "scope.name = ",
            nm = single_obj.name
            print nm

        else:
            print "_______________________________________________________ in else"

scope_str = ""

def write_to_disc(lst_obj):
    src_code_aut = []
    for obj in lst_obj:
        #if( obj == "is_scope" ):
        print "type =", str(type(obj))

        if( str(type(obj)) == "<type \'str\'>" ):

            print "[scope] =", obj
            src_code_aut.append("        label_tst = QLabel(\"" +  str(obj)  + "\")")
            src_code_aut.append("        bg_box.addWidget(label_tst)")

        else:
            if(obj[1] == 'float' or obj[1] == 'int' or obj[1] == 'str' or obj[1] == 'bool' ):
                print "___________________ << supported type found "
                h_box_name = "hbox_" + str(obj[0])
                src_code_aut.append("        " + h_box_name + " =  QHBoxLayout()")
                label_name = "label_" + str(obj[0])
                str_to_add = "        " + label_name + " = QLabel(\"" + str(obj[0])  + "\")"
                src_code_aut.append(str_to_add)
                src_code_aut.append("        " + h_box_name + ".addWidget(" + label_name + ")")
                box_name = "spn_box_" + str(obj[0])

                if( obj[1] == 'float' ):
                    src_code_aut.append("        " + box_name + " = QDoubleSpinBox()")

                elif( obj[1] == 'int' ):
                    src_code_aut.append("        " + box_name + " = QSpinBox()")

                elif( obj[1] == 'str' ):
                    src_code_aut.append("        " + box_name + " = QLineEdit()")

                    '''
                elif( obj[1] == 'choice' ):
                    src_code_aut.append("        " + box_name + " = QComboBox()")
                    '''

                elif(obj[1] == 'bool' ):
                    print "________________________________________________________ bool found"
                    src_code_aut.append("        " + box_name + " = QComboBox()")
                    src_code_aut.append("        " + box_name + ".addItem(\"False\")")
                    src_code_aut.append("        " + box_name + ".addItem(\"True\")")

                src_code_aut.append("        " + h_box_name + ".addWidget(" + box_name + ")")
                src_code_aut.append("        bg_box.addLayout(" + h_box_name + ")")


            else:
                print "__________________________________ << WARNING find something ELSE"
                print "__________________________________ << find", obj[1]

    s_code = gen_code()
    s_code.write_file(src_code_aut)


if( __name__ == "__main__"):
    from dials.command_line.integrate import phil_scope
    #from dials.command_line.refine import phil_scope
    #from dials.command_line.index import phil_scope
    #from dials.command_line.find_spots import phil_scope
    phl_obj = phil_scope.objects
    lst_obj = []

    for single_obj in phl_obj:
        print single_obj.name
    print "end \n\n\n"

    deep_in_rec(phl_obj, lst_obj)
    write_to_disc(lst_obj)

    print phil_scope.show()

