from dials.command_line.refine import phil_scope
objs = phil_scope.objects
print "objs[0] =", objs[0].name
print "objs[1] =", objs[1].name
ref_obj = objs[1]
print "ref_obj.objects[0].name =", ref_obj.objects[0].name
print "ref_obj.objects[1].name =", ref_obj.objects[1].name
print "ref_obj.objects[2].name =", ref_obj.objects[2].name
par_obj = ref_obj.objects[2]
print "par_obj.objects[0].name =", par_obj.objects[0].name
print "par_obj.objects[1].name =", par_obj.objects[1].name

scan_var_obj = par_obj.objects[1]

print "scan_var_obj.type.phil_type =", scan_var_obj.type.phil_type
print "scan_var_obj.extract() =", scan_var_obj.extract()
