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
        self.src_code_1.append("#PyQt4_ver = '''")
        self.src_code_1.append("from PyQt4.QtGui import *")
        self.src_code_1.append("from PyQt4.QtCore import *")
        self.src_code_1.append("#Signal = pyqtSignal")
        self.src_code_1.append("print \"using PyQt4\"")
        self.src_code_1.append("#'''")
        #self.src_code_1.append(" ")
        self.src_code_1.append("PySide_ver = '''")
        self.src_code_1.append("from PySide.QtGui import *")
        self.src_code_1.append("from PySide.QtCore import *")
        self.src_code_1.append("pyqtSignal = Signal")
        self.src_code_1.append("print \"using PySide\"")
        self.src_code_1.append("#'''")
        #self.src_code_1.append(" ")
        self.src_code_1.append("class inner_widg( QWidget):")
        self.src_code_1.append("    goClicked = pyqtSignal()")
        self.src_code_1.append("    def __init__(self, parent):")
        self.src_code_1.append("        super(inner_widg, self).__init__()")
        #self.src_code_1.append(" ")
        self.src_code_1.append("        self.btn_go =  QPushButton('\\n      Go   \\n', self)")
        self.src_code_1.append("        #self.btn_go.clicked.connect(self.B_go_clicked)")
        self.src_code_1.append("        self.btn_go.clicked.connect(self.goClicked)")
        self.src_code_1.append("        hbox =  QHBoxLayout()")
        self.src_code_1.append("        hbox.addWidget(self.btn_go)")
        self.src_code_1.append("        bg_box =  QVBoxLayout(self)")
        self.src_code_1.append(" ")

        #between this two pieces of code goes the phil auto-generated  code
        self.src_code_2 = []
        self.src_code_2.append(" ")
        self.src_code_2.append("        bg_box.addLayout(hbox)")
        self.src_code_2.append("        self.setLayout(bg_box)")
        self.src_code_2.append("        self.show()")
        self.src_code_2.append("class MainWidget( QWidget):")
        #self.src_code_2.append(" ")
        self.src_code_2.append("    def __init__(self):")
        self.src_code_2.append("        super(MainWidget, self).__init__()")
        #self.src_code_2.append(" ")
        self.src_code_2.append("        self.inner_btn = inner_widg(self)")
        self.src_code_2.append("        hbox =  QHBoxLayout()")
        self.src_code_2.append("        hbox.addWidget(self.inner_btn)")
        self.src_code_2.append("        self.inner_btn.goClicked.connect(self.to_be_caled_from_son_widg)")
        self.src_code_2.append("        self.setLayout(hbox)")
        self.src_code_2.append("        self.setWindowTitle('Shell dialog')")
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

        if_we_wanna_read = '''
        os.system("./psl_calc.r c ori_SI.cfl")
        myfile = open("calc_pk.dat", "r")
        lines = myfile.readlines()
        myfile.close()
        '''

def deep_in_rec(phl_obj):
    for single_obj in phl_obj:
        if( single_obj.is_scope ):
            #print "is_scope \n" # deep_in_rec here
            deep_in_rec(single_obj.objects)
        elif( single_obj.is_definition):
            #print "single_obj.name =", single_obj.name
            local_val = single_obj.extract()

            #print "dir(single_obj) =", dir(single_obj), "\n\n"
            #print "single_obj.extract_format =", single_obj.extract_format()
            #print "single_obj.type =", single_obj.type.phil_type
            #print "single_obj.extract =", local_val

            elm = [single_obj.name, single_obj.type.phil_type]
            lst_obj.append(elm)


from_JMPs_code = '''

  def createEditor(self, parent, option, index):
    parameter = index.model().data(index, Qt.UserRole+1).toPyObject()
    dtype = parameter.type
    ptype = dtype.phil_type
    if ptype == 'str':
      editor = StringEditor(parent)
    elif ptype == 'float':
      editor = FloatEditor(parent, dtype.value_min, dtype.value_max)
    elif ptype == 'int':
      editor = IntEditor(parent, dtype.value_min, dtype.value_max)
    elif ptype == 'choice':
      def strip(w):
        w = str(w)
        if w.startswith("*"):
          return w[1:]
        return w
      choices = [strip(w) for w in parameter.words]
      editor = ChoiceEditor(parent, choices)
    elif ptype == 'bool':
      editor = BoolEditor(parent)
    else:
      raise RuntimeError("Handle type %s" % dtype)
    return editor

'''

if( __name__ == "__main__"):
    from dials.command_line.integrate import phil_scope
    #from dials.command_line.refine import phil_scope
    #from dials.command_line.index import phil_scope
    #from dials.command_line.find_spots import phil_scope
    phl_obj = phil_scope.objects
    lst_obj = []
    deep_in_rec(phl_obj)

    src_code_aut = []

    for obj in lst_obj:
        print obj

        if(obj[1] == 'float' ):
            print "_________________________ << type float"

            box_name = "box_" + str(obj[0])

            src_code_aut.append("        " + box_name + " = QDoubleSpinBox()")
            src_code_aut.append("        bg_box.addWidget(" + box_name + ")")
            '''
            class FloatEditor(QDoubleSpinBox):

              def __init__(self, parent=None, value_min=None, value_max=None):
                super(FloatEditor, self).__init__(parent)
                if value_min is not None:
                  self.setMinimum(value_min)
                else:
                  self.setMinimum(-1e9)
                if value_max is not None:
                  self.setMaximum(value_max)
                else:
                  self.setMaximum(1e9)
                self.setDecimals(2)

              def setEditorData(self, index):
                value = index.model().data(index, Qt.EditRole).toFloat()
                self.setValue(value[0])

              def setModelData(self, model, index):
                self.interpretText()
                value = self.value()
                model.setData(index, value, Qt.EditRole)
            '''


        elif(obj[1] == 'str' ):
            print "_________________________ << type str"
        elif(obj[1] == 'int' ):
            print "_________________________ << type int"
        elif(obj[1] == 'choice' ):
            print "_________________________ << type choice"
        elif(obj[1] == 'bool' ):
            print "_________________________ << type bool"
        else:
            print "__________________________________ << WARNING find something ELSE"


    s_code = gen_code()

    s_code.write_file(src_code_aut)


