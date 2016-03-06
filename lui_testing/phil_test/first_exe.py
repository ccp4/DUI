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
      #print "is_scope \n" # deep_in_rec here
      deep_in_rec(single_obj.objects)
    elif( single_obj.is_definition):
      #print "single_obj.name =", single_obj.name
      local_val = single_obj.extract()

      '''
      dir(single_obj) = ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__',
       '__getstate__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__',
       '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__',
       '__subclasshook__', '_all_definitions', '_type_from_words', '_validate', 'alias',
       'alias_path', 'as_str', 'assign_attribute', 'assign_tmp', 'attribute_names', 'caption',
       'copy', 'customized_copy', 'deprecated', 'expert_level', 'extract', 'extract_format',
       'fetch', 'fetch_diff', 'fetch_value', 'format', 'full_path', 'get_without_substitution',
       'has_attribute_with_name', 'help', 'input_size', 'is_definition', 'is_disabled',
       'is_scope', 'is_template', 'merge_names', 'multiple', 'name', 'optional', 'primary_id',
       'primary_parent_scope', 'resolve_variables', 'short_caption', 'show', 'style', 'tmp',
       'try_extract', 'try_extract_format', 'try_tokenize', 'type', 'unique', 'validate',
       'validate_and_format', 'where_str', 'words']

      '''


      if( single_obj.name == "d_min" ):
          print "\n\n\n___________________________________________________________found d_min"

          #print "dir(single_obj) =", dir(single_obj), "\n\n"
          print "single_obj.extract_format =", single_obj.extract_format()
          print "single_obj.type =", str(single_obj.type)


          print "single_obj._all_definitions()", single_obj._all_definitions

          print "single_obj.as_str()", single_obj.as_str()
          print "\n\n\n___________________________________________________________found d_min"

      print "\n\n___________________________________________________________"
      print "single_obj.name =", single_obj.name
      print "single_obj.extract =", local_val
      print "type(single_obj.extract) =", type(single_obj.extract)
      print "type(local_val) =", type(local_val)
      print "single_obj.as_str()", single_obj.as_str()
      #print "type(local_type) =", type(local_val)


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
