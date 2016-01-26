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

    '''
    Source code generator in a non analytical way, this means this class does
    not read the Phil parameters, just generates the code after and before of
    the Phil dependent code, and writes into disc once passed the Phil
    dependent piece of code
    '''

    def __init__(self):

        self.src_code_1 = []
        self.src_code_1.append("import sys")
        self.src_code_1.append("PyQt4_ver = '''")
        self.src_code_1.append("from PyQt4.QtGui import *")
        self.src_code_1.append("from PyQt4.QtCore import *")
        self.src_code_1.append("print \"using PyQt4\"")
        self.src_code_1.append("#'''")
        self.src_code_1.append("#PySide_ver = '''")
        self.src_code_1.append("from PySide.QtGui import *")
        self.src_code_1.append("from PySide.QtCore import *")
        self.src_code_1.append("pyqtSignal = Signal")
        self.src_code_1.append("print \"using PySide\"")
        self.src_code_1.append("#'''")
        self.src_code_1.append("\n")
        self.src_code_1.append("class inner_widg( QWidget):")
        self.src_code_1.append("    item_changed = pyqtSignal()")
        self.src_code_1.append("    def __init__(self, parent):")
        self.src_code_1.append("        super(inner_widg, self).__init__()")
        self.src_code_1.append("        bg_box =  QVBoxLayout(self)")
        self.src_code_1.append("\n")

        self.src_code_2 = []
        self.src_code_2.append(" ")
        self.src_code_2.append("        self.setLayout(bg_box)")
        self.src_code_2.append("        self.show()")
        self.src_code_2.append("class MainWidget( QWidget):")
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
        self.src_code_2.append("\n")
        self.src_code_2.append("    def to_be_caled_from_son_widg(self):")
        self.src_code_2.append("        print \"from parent parent_widget\"")
        self.src_code_2.append("\n")
        self.src_code_2.append("if __name__ == '__main__':")
        self.src_code_2.append("    app =  QApplication(sys.argv)")
        self.src_code_2.append("    ex = MainWidget()")
        self.src_code_2.append("    sys.exit(app.exec_())")


    def write_file(self, to_insert = None):
        '''
        Writes code into a disc, but includes the "to_insert" list in the middle
        '''

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

class ScopeData(object):
    '''
    class conceived to store only data related to the scope Phil object
    '''
    pass

class tree_2_lineal(object):

    '''
    Recursively navigates the Phil objects in a way that the final
    self.lst_obj is a lineal list without ramifications, this final list
    will be used by phil_list_2_disc() to generate runnable code
    '''

    def __init__(self, phl_obj):
        self.lst_obj = []
        self.deep_in_rec(phl_obj)

    def __call__(self):
        return self.lst_obj

    def deep_in_rec(self, phl_obj):

        for single_obj in phl_obj:
            if( single_obj.is_definition):
                self.lst_obj.append(single_obj)
            elif( single_obj.is_scope ):
                print "scope.name = ", single_obj.name
                scope_info = ScopeData()
                scope_info.name = str(single_obj.name)
                scope_info.f_path = str(single_obj.full_path())

                print "scope_info.f_path =", scope_info.f_path
                scope_info.indent = scope_info.f_path.count('.')
                print "scope_info.f_path.count('.') =", scope_info.indent

                self.lst_obj.append(scope_info)
                self.deep_in_rec(single_obj.objects)

            else:
                print "\n\n _____________ <<< WARNING neither definition or scope\n\n"


def phil_list_2_disc(lst_obj):

    '''
    generator of either PyQt4 or PySide GUI code that lets the user edit
    the Phil parameters, the code auto-generated here should be inserted
    between the s_code.src_code_1 and s_code.src_code_2 lists
    '''

    src_code_aut = []
    for obj in lst_obj:

        if( str(type(obj)) == "<class '__main__.ScopeData'>" ):
            my_str = "        label_tst = QLabel(\"" + " " * obj.indent * 4
            my_str += str(obj.name)  + "\")"
            src_code_aut.append(my_str)

            if( obj.indent < 3 ):
                f_siz = str(14 - obj.indent)
            else:
                f_siz = "13"
            my_str = "        label_tst.setFont(QFont(\"Monospace\", "
            my_str += f_siz + ", QFont.Bold))"
            src_code_aut.append(my_str)
            my_str = "        bg_box.addWidget(label_tst)"
            src_code_aut.append(my_str)

        else:
            h_box_name = "hbox_" + str(obj.name)
            my_str = "        " + h_box_name + " =  QHBoxLayout()"
            src_code_aut.append(my_str)
            label_name = "label_" + str(obj.name)
            indent = str(obj.full_path()).count('.')
            my_str = "        " + label_name + " = QLabel(\""
            my_str += " " * indent * 8 + str(obj.name)  + "\")"
            src_code_aut.append(my_str)

            if( indent < 3 ):
                f_siz = str(int((14 - indent) * 1.3))
            else:
                f_siz = "14"

            my_str = "        " + label_name + ".setFont(QFont(\"Times\","
            my_str += f_siz + ", QFont.Bold))"
            src_code_aut.append(my_str)
            my_str = "        " + h_box_name + ".addWidget(" + label_name + ")"
            src_code_aut.append(my_str)
            box_name = "spn_box_" + str(obj.name)
            something_else = False
            if(obj.type.phil_type == 'float' or
               obj.type.phil_type == 'int'   or
               obj.type.phil_type == 'str'     ):

                if( obj.type.phil_type == 'float' ):
                    widget_type_str =" = QDoubleSpinBox()"

                elif( obj.type.phil_type == 'int' ):
                    widget_type_str =" = QSpinBox()"

                elif( obj.type.phil_type == 'str' ):
                    widget_type_str =" = QLineEdit()"

                my_str = "        " + box_name + widget_type_str
                src_code_aut.append(my_str)

            elif( obj.type.phil_type == 'bool' ):
                my_str = "        " + box_name + " = QComboBox()"
                src_code_aut.append(my_str)
                my_str = "        " + box_name + ".addItem(\"False\")"
                src_code_aut.append(my_str)
                my_str = "        " + box_name + ".addItem(\"True\")"
                src_code_aut.append(my_str)


            elif( obj.type.phil_type == 'choice' ):

                my_str = "        " + box_name + " = QComboBox()"
                src_code_aut.append(my_str)

                for opt in obj.words:
                    my_str = "        " + box_name
                    my_str += ".addItem(\"" + str(opt) + "\")"
                    src_code_aut.append(my_str)

            else:
                '''
                print "_____________________ << WARNING find something ELSE"
                print "_____________________ << find", obj.type.phil_type
                '''
                something_else = True

            if( something_else == False ):
                my_str = "        " + h_box_name + ".addWidget(" + box_name + ")"
                src_code_aut.append(my_str)
                my_str = "        bg_box.addLayout(" + h_box_name + ")"
                src_code_aut.append(my_str)
            print "obj.full_path()    =", obj.full_path()

    s_code = gen_code()
    s_code.write_file(src_code_aut)


if( __name__ == "__main__"):
    #from dials.command_line.integrate import phil_scope
    #from dials.command_line.refine import phil_scope
    from dials.command_line.index import phil_scope
    #from dials.command_line.find_spots import phil_scope
    phl_obj = phil_scope.objects

    lst_obj = tree_2_lineal(phl_obj)
    phil_list_2_disc(lst_obj())

    print phil_scope.show()

