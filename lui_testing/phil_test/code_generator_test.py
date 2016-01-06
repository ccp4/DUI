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
        self.src_code_1.append("        bg_box.addLayout(hbox)")
        self.src_code_1.append("        self.setLayout(bg_box)")
        self.src_code_1.append("        self.show()")
        #self.src_code_1.append(" ")

        #between this two pieces of code goes the phil auto-generated  code

        self.src_code_2 = []
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

    def write_file(self):

        myfile = open("gui_tst_code.py", "w")

        for line in self.src_code_1:
            myfile.write(line)
            myfile.write("\n")

        myfile.write("#next class\n")

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

      if( single_obj.name == "d_min"):
          print "\n\n\n___________________________________________________________found d_min"

          #print "dir(single_obj) =", dir(single_obj), "\n\n"
          #print "single_obj.extract_format =", single_obj.extract_format()
          #print "single_obj.type =", single_obj.type


          #print "\n\n\n"

      #print "single_obj.extract =", local_val
      #print "type(local_type) =", type(local_val)
      elm = [single_obj.name, single_obj.type]
      lst_obj.append(elm)



if( __name__ == "__main__"):
  #from dials.command_line.integrate import phil_scope
  #from dials.command_line.refine import phil_scope
  #from dials.command_line.index import phil_scope
  from dials.command_line.find_spots import phil_scope
  phl_obj = phil_scope.objects
  lst_obj = []
  deep_in_rec(phl_obj)
  for obj in lst_obj:
    print obj

  s_code = gen_code()

  s_code.write_file()


