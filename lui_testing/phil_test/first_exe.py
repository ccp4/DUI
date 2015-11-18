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

#from dials.command_line.integrate import phil_scope
#from dials.command_line.refine import phil_scope
#from dials.command_line.index import phil_scope
from dials.command_line.find_spots import phil_scope

for single_obj in phil_scope.objects:
  print single_obj

print phil_scope.objects