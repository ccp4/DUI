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

def deep_in_rec(phl_obj):
  for single_obj in phl_obj:
    if( single_obj.is_scope ):
      print "is_scope \n" # deep_in_rec here
      deep_in_rec(single_obj.objects)
    elif( single_obj.is_definition):
      print "single_obj.name =", single_obj.name
      local_val = single_obj.extract()

      if( single_obj.name == "d_min" ):
          print "\n\n\n___________________________________________________________found d_min"

          print "dir(single_obj) =", dir(single_obj), "\n\n"
          print "single_obj.extract_format =", single_obj.extract_format()
          print "single_obj.type =", single_obj.type


          print "\n\n\n"

      print "single_obj.extract =", local_val
      print "type(local_type) =", type(local_val)


    lst_obj.append(single_obj)

if( __name__ == "__main__" ):
  #from dials.command_line.integrate import phil_scope
  #from dials.command_line.refine import phil_scope
  #from dials.command_line.index import phil_scope
  from dials.command_line.find_spots import phil_scope
  phl_obj = phil_scope.objects
  lst_obj = []
  deep_in_rec(phl_obj)

  '''
  for single_obj in lst_obj:
    print single_obj
  '''
